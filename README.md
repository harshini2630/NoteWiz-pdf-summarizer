# 📄 NoteWiz – PDF Summarizer & Generator

NoteWiz is an AI-powered web application that helps users convert PDFs (like lecture notes) into clean, summarized content and downloadable outputs using modern frontend and backend technologies.

## 🚀 Features

- 🔐 **User Authentication** (Signup/Login)
- 📤 Upload PDF files manually or via input
- 🧠 **AI-Powered Summarization** using Gemini API
- 📄 Downloadable clean **summary PDFs**
- 🎨 Stylish, scroll-snapping UI with modern gradient theme
- 🖥️ Built with **React + Vite** and a **Flask backend**

---

## 🧩 Project Structure

NoteWiz/
│
├── frontend/ # React + Vite based UI
│ └── ...
│
├── backend/ # Flask backend for handling uploads & AI integration
│ └── venv/ # Virtual environment (excluded from Git)
│
└── README.md

yaml
Copy
Edit

---

## 🖼️ UI Preview

> Upload Page Example  
> ![Upload UI](https://via.placeholder.com/600x350.png?text=Upload+Section+Preview)

---

## 🛠️ Tech Stack

| Frontend          | Backend           | AI / NLP         |
|-------------------|-------------------|------------------|
| React + Vite      | Python + Flask    | Gemini 2.5 Flash |
| Tailwind/CSS      | PDF generation    | Whisper (Optional) |
| Scroll Snapping   | File handling     | PDF Summarization |

---

## 🧪 Local Setup

1. **Clone the repo**
```bash
git clone https://github.com/harshini2630/NoteWiz-pdf-summarizer.git
cd NoteWiz
Frontend

bash
Copy
Edit
cd frontend
npm install
npm run dev
Backend

bash
Copy
Edit
cd ../backend
python -m venv venv
venv\Scripts\activate      # (on Windows)
pip install -r requirements.txt
python app.py
📁 .gitignore Highlights
gitignore
Copy
Edit
# Logs and environments
logs/
*.log
backend/venv/

# Node and dist
node_modules/
dist/
.vscode/
📬 Contact
For questions or suggestions, feel free to open an issue or contact me on GitHub: @harshini2630

📜 License
MIT License – Use it freely for educational or personal projects.

yaml
Copy
Edit

---

### ✅ Now, paste that in your `README.md`, save, then:

```bash
git add README.md
git commit -m "Add detailed README for NoteWiz"
git push origin main