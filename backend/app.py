from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os, tempfile, traceback
from pydub import AudioSegment
from google.generativeai import configure, GenerativeModel
import whisper
from dotenv import load_dotenv

# 🔧 Load environment variables and configure Gemini
load_dotenv()
configure(api_key=os.getenv("GEMINI_API_KEY"))

# 🔧 Flask app config
app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp3', 'wav', 'm4a', 'mp4'}

# ✅ File type checker
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# 🎵 Convert audio to MP3 (if needed)
def convert_to_mp3(filepath):
    if filepath.endswith(".mp3"):
        return filepath
    audio = AudioSegment.from_file(filepath)
    mp3_path = filepath + ".mp3"
    audio.export(mp3_path, format="mp3")
    return mp3_path

# 🧠 Main Route: Upload audio → Transcribe → Summarize → PDF
@app.route('/generate-pdf-from-audio', methods=['POST'])
def generate_pdf_from_audio():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "Empty file name"}), 400

        # Save file
        filename = secure_filename(file.filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        print(f"📁 File saved at: {filepath}")

        # Convert to mp3
        audio_path = convert_to_mp3(filepath)
        print(f"🔄 Converted audio path: {audio_path}")

        # Transcribe with Whisper
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        transcript = result.get("text", "")
        print("📝 Transcription completed.")

        # Summarize with Gemini
        gemini_model = GenerativeModel(model_name="models/gemini-1.5-flash")  # or gemini-1.5-pro if needed
        prompt = f"""
        Please summarize the following lecture audio in structured form:
        1. Key topics covered
        2. Main concepts
        3. Examples (if any)
        4. Key takeaways

        Transcript:
        {transcript}
        """
        response = gemini_model.generate_content(prompt)
        summary = response.text.strip()
        print("📄 Summary generated.")

        # Generate PDF
        pdf_path = os.path.join(tempfile.gettempdir(), "summary.pdf")
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = [
            Paragraph("Lecture Summary", styles['Title']),
            Paragraph(summary, styles['Normal'])
        ]
        doc.build(story)
        print(f"✅ PDF created at: {pdf_path}")

        return send_file(pdf_path, as_attachment=True, download_name="summary.pdf", mimetype="application/pdf")

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def index():
    return "Backend is running. Use the React frontend."
