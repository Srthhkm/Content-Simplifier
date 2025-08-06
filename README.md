# Content Simplification Agent

> **Note:** This project is powered by a custom AI agent designed to intelligently simplify complex content based on user proficiency levels.

This web application simplifies complex text content based on the user’s proficiency level (Beginner, Intermediate, Expert). It accepts either text input or a document (PDF/DOCX) and generates a simplified version of the content accordingly.

## Features

- Accepts user input as plain text or file upload (PDF, DOCX).
- Supports three proficiency levels for simplification:
  - Beginner: Simple, concise explanations with examples.
  - Intermediate: Detailed explanations avoiding heavy jargon.
  - Expert: Technical, precise explanations with relevant terms.
- Real-time content processing and display.
- User-friendly responsive frontend with clear error handling.
- Backend built using Python Flask.
- Integrated with AI agent to perform content simplification based on instructions.

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Agent creation - IBM Cloud Lite services
- AI Model: MISTRAL LARGE - Custom agent for content simplification (via API)
- File Handling: Supports PDF and DOCX uploads

## Getting Started

### Prerequisites

- Python 3.x installed
- Flask and other dependencies listed in `requirements.txt`

### Installation

Run the following commands in command prompt/terminal:

1. Clone the repository:  
   git clone https://github.com/Srthhkm/Content-Simplifier.git

2. Navigate into the project directory:  
   cd Content-Simplifier

3. Create and activate a virtual environment (optional but recommended):  
   python -m venv venv  
   # Linux/Mac  
   source venv/bin/activate  
   # Windows  
   venv\Scripts\activate

4. Install dependencies:  
   pip install -r requirements.txt

5. Configure your environment variables (see **Configuration** section below).

6. Run the Flask app:  
   python app.py

7. Open your browser and go to:  
   http://127.0.0.1:5000/

### Configuration

To run the backend properly, you need to provide your AI API credentials and endpoint.

- Create a `.env` file in the project root (same folder as `app.py`).  
- Add the following lines to `.env`:

  API_KEY=your_api_key_here  
  API_ENDPOINT=https://api.youraiendpoint.com/v1/generate

- Replace `your_api_key_here` and `API_ENDPOINT` with your actual API key and endpoint URL.

**Note:** Do **not** commit your `.env` file to GitHub or share your API keys publicly.

### AI Agent Deployment via Jupyter Notebook
This repository includes a Jupyter Notebook (agent_deployment.ipynb) that allows you to deploy your own AI agent using IBM Cloud services.

- Steps to Deploy the Agent:
Open agent_deployment.ipynb in IBM Watson Studio or any Jupyter environment.
Follow the instructions inside the notebook to:

- Authenticate with your IBM Cloud API key.
- Deploy the AI model (e.g., Mistral Large) with the provided prompt instructions.
- Retrieve your custom API_KEY and API_ENDPOINT.
- Use these values in your .env file as described above.
- Once deployed, your Flask app will use your custom AI agent for content simplification.

This allows anyone to replicate or customize the AI agent without relying on an existing deployment.

### Usage

- Select a proficiency level.  
- Upload a PDF or DOCX file **or** enter the text directly.  
- Click **Generate** to get simplified content.  
- View the simplified output below the form.

### Project Structure

- app.py – Flask backend server  
- templates/index.html – Frontend HTML page  
- static/ – CSS, images, and other static files  
- requirements.txt – Python dependencies  
- test.py – Optional test script (if any)  
- .gitignore – Specifies files/folders to exclude from Git

### .gitignore

This project includes a `.gitignore` file to avoid committing unnecessary or sensitive files such as:

- Virtual environment folders (`venv/`)  
- Python cache files (`__pycache__/`)  
- Environment variable files (`.env`)  
- IDE/editor configs (like `.vscode/`, `.idea/`)

This keeps your repository clean and secure.

### License

This project is licensed under the MIT License.

---

Thank you for using the Content Simplification Agent!  
Feel free to contribute or raise issues in the repository.
