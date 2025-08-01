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
- AI Model: Custom agent for content simplification (via API)
- File Handling: Supports PDF and DOCX uploads

## Getting Started

### Prerequisites

- Python 3.x installed
- Flask and other dependencies listed in `requirements.txt`

### Installation
Run the following commands in command prompt/terminal

1. Clone the repository: 
  -> git clone https://github.com/Srthhkm/Content-Simplifier.git

2. Navigate into the project directory:
  -> cd Content-Simplifier

3. Create and activate a virtual environment (optional but recommended):
  -> python -m venv venv
  -> source venv/bin/activate      # Linux/Mac
  -> venv\Scripts\activate         # Windows

4. Install dependencies:
  -> pip install -r requirements.txt

5. Run the Flask app:
  -> python app.py

6. Open your browser and go to http://127.0.0.1:5000/

### Usage 
- Select a proficiency level.
- Upload a PDF or DOCX file or enter the text directly.
- Click Generate to get simplified content.
- View the simplified output below the form.

### Project Structure
- app.py – Flask backend server
- templates/index.html – Frontend HTML page
- static/ – CSS, images, and other static files
- requirements.txt – Python dependencies
- test.py – Optional test script (if any)

### License
This project is licensed under the MIT License.

 " Thank you for using the Content Simplification Agent!
Feel free to contribute or raise issues in the repository. "


