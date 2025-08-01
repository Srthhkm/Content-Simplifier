# NOTE: For security, do NOT hardcode real credentials in public repos.
# Replace 'API_KEY' and 'DEPLOYMENT_URL' with your own if testing locally.

from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
import requests
import time
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# Config
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Replace with your IBM Cloud API Key
API_KEY = "YOUR_IBM_CLOUD_API_KEY_HERE"

# Replace with your Watson Deployment URL
DEPLOYMENT_URL = "YOUR_DEPLOYMENT_URL_HERE"

cached_token = None
token_expiry = 0

def get_iam_token_cached(api_key):
    global cached_token, token_expiry
    current_time = time.time()

    if cached_token and current_time < token_expiry:
        return cached_token

    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={api_key}"

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    token_data = response.json()

    cached_token = token_data["access_token"]
    token_expiry = current_time + token_data["expires_in"] - 60
    return cached_token

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/simplify', methods=['POST'])
def simplify_content():
    try:
        level = request.form.get('level')
        content = request.form.get('content', '').strip()
        file = request.files.get('file')

        if not level:
            return jsonify({"error": "Proficiency level is required."}), 400

        if not file and not content:
            return jsonify({"error": "Provide text or upload a file."}), 400

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext == ".pdf":
                import fitz
                with fitz.open(filepath) as doc:
                    content = "\n".join(page.get_text() for page in doc)
            elif file_ext == ".docx":
                import docx
                doc = docx.Document(filepath)
                content = "\n".join(paragraph.text for paragraph in doc.paragraphs)
            else:
                os.remove(filepath)
                return jsonify({"error": "Unsupported file type. Only PDF and DOCX allowed."}), 400

            os.remove(filepath)

        if not content.strip():
            return jsonify({"error": "Uploaded file is empty."}), 400

        prompt_text = f"Simplify for {level} level : {content}"

        # ✅ Correct payload for foundation model
        payload = {
            "messages": [
                {
                    "content": prompt_text,
                    "role": "user"
                }
            ]
        }

        token = get_iam_token_cached(API_KEY)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        response = requests.post(DEPLOYMENT_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        generated_text = result["choices"][0]["message"]["content"]
        return jsonify({"result": generated_text})

    except requests.exceptions.HTTPError as http_err:
        if http_err.response is not None:
            print("Status Code:", http_err.response.status_code)
            print("Error Response:", http_err.response.text)  # PRINT THIS
            return jsonify({"error": f"API request failed: {http_err.response.text}"}), 500
        else:
            print("HTTPError without response:", str(http_err))
            return jsonify({"error": f"API request failed: {str(http_err)}"}), 500

    except Exception as e:
        print(f"Server Exception: {str(e)}")
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
