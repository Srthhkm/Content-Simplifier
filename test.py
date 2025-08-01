import requests

API_KEY = "tZGZ2aSCF8XyoSUF6qSY3Qz-eDm7ySNkfntHadGzUx_g"
IAM_TOKEN_URL = "https://iam.cloud.ibm.com/identity/token"
DEPLOYMENT_ENDPOINT = "https://au-syd.ml.cloud.ibm.com/ml/v1/deployments/a013e03b-c321-41f7-ae77-43904993017b/text/generation?version=2021-05-01"

def get_iam_token(api_key):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": api_key
    }
    response = requests.post(IAM_TOKEN_URL, headers=headers, data=data)
    response.raise_for_status()  # raise error if any
    return response.json()["access_token"]

def generate_text(iam_token, input_text):
    headers = {
        "Authorization": f"Bearer {iam_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": input_text,
        "max_tokens": 100,
        "temperature": 0.7,
        "top_p": 0.9,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = requests.post(DEPLOYMENT_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    try:
        token = get_iam_token(API_KEY)
        input_text = (
            "Multithreading in operating systems allows multiple threads to exist within "
            "the context of a single process, enabling concurrent execution. It helps optimize "
            "CPU utilization, improves responsiveness in interactive applications, and is "
            "commonly used in server applications for handling multiple requests simultaneously."
        )
        result = generate_text(token, input_text)
        print("Response JSON:")
        print(result)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")
