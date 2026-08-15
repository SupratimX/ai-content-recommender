import requests
import json
from flask import Flask, render_template, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# --- GEMINI API Configuration ---
API_KEY = "AIzaSyA5ZmHpwNSI5jeOUVA6r0tQue-TzTy_miQ"
MODELS = ["gemini-3.5-flash-lite", "gemini-3.5-flash", "gemini-flash-latest"]

@app.route('/')
def index():
    """
    This is the main page. It serves your HTML file.
    """
    return render_template('index.html')

@app.route('/get_books', methods=['POST'])
def get_books():
    """
    This is your new AI-powered API. It queries the Gemini model online.
    """
    data = request.json or {}
    branch = data.get('branch', 'Engineering').strip()
    semester = data.get('semester', '').strip()
    subject = data.get('subject', '').strip()

    if not subject:
        return jsonify({"error": "Subject cannot be empty."}), 400

    # 1. UPDATED prompt for the AI model.
    system_instruction = (
        "You are an expert academic librarian for university students in India. "
        "Your task is to recommend the top 5 textbooks for a given engineering subject. "
        "The books must be sorted with the most reputable and classic texts first, based on community consensus from sources like Reddit. "
        "For each book, include a concise, 1-2 sentence description explaining why it is recommended. "
        "You must respond ONLY with a valid JSON array of objects. Do not include any other text or explanations."
    )
    
    user_prompt = (
        f"Find the top 5 textbooks for a university student in India studying '{branch}' "
        f"in semester '{semester}' for the subject '{subject}'. For each book, provide the title, all authors, "
        "a real link to buy it on Amazon India, and a link to a free version if one exists. "
        "Most importantly, provide a short 'description' for each book explaining its strengths, and sort the results by reputation."
    )

    # 2. UPDATED JSON schema to include the 'description'.
    json_schema = {
        "type": "ARRAY",
        "items": {
            "type": "OBJECT",
            "properties": {
                "title": {"type": "STRING"},
                "author": {"type": "STRING"},
                "description": {"type": "STRING"},
                "buy_link": {"type": "STRING"},
                "free_link": {"type": "STRING"}
            },
            "required": ["title", "author", "description", "buy_link", "free_link"]
        }
    }

    # 3. Construct the payload for the Gemini API.
    payload = {
        "systemInstruction": {"parts": [{"text": system_instruction}]},
        "contents": [{"parts": [{"text": user_prompt}]}],
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseSchema": json_schema
        }
    }

    # 4. Make the API call to Gemini with model fallback
    last_error = None
    for model_name in MODELS:
        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={API_KEY}"
        try:
            response = requests.post(api_url, json=payload, timeout=30)
            if response.status_code == 200:
                result = response.json()
                candidate = result.get("candidates", [{}])[0]
                content_part = candidate.get("content", {}).get("parts", [{}])[0]
                json_string = content_part.get("text", "[]")
                found_books = json.loads(json_string)
                return jsonify(found_books)
            else:
                print(f"Model {model_name} returned status {response.status_code}: {response.text}")
                last_error = response.text
        except Exception as e:
            print(f"Error calling {model_name}: {e}")
            last_error = str(e)

    return jsonify({"error": f"Could not fetch recommendations. Details: {last_error}"}), 500


if __name__ == '__main__':
    app.run(debug=True)

