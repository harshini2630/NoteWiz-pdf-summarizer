import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [pdfLink, setPdfLink] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setPdfLink("");
  };

  const handleGeneratePDF = async () => {
    if (!file) {
      alert("Please upload an audio or video file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/generate-pdf-from-audio",
        formData,
        { responseType: "blob" }
      );

      const url = window.URL.createObjectURL(new Blob([response.data]));
      setPdfLink(url);
    } catch (error) {
      console.error("Error:", error);
      alert("Something went wrong while generating the PDF.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      {/* 🌐 NAVBAR */}
      <nav className="navbar">
        <div className="logo">🎧 NoteWiz</div>
        <ul>
          <li><a href="#hero">Home</a></li>
          <li><a href="#upload">Upload</a></li>
          <li><a href="#how">How It Works</a></li>
        </ul>
      </nav>

      {/* 🏠 HERO SECTION */}
      <section className="hero" id="hero">
        <h1>Turn Lectures into Smart Summaries</h1>
        <p>Upload your audio/video lecture and get a structured PDF in seconds.</p>
        <a href="#upload" className="cta-btn">Get Started</a>
      </section>

      {/* 🎤 UPLOAD SECTION */}
      <section className="upload-section" id="upload">
        <div className="glass-container">
          <h2>Upload Lecture File</h2>
          <br></br>
          <br></br>
          <input
            type="file"
            accept="audio/*,video/*"
            onChange={handleFileChange}
          /><br></br>
          <br></br>
          <button onClick={handleGeneratePDF} disabled={loading}>
            {loading ? "Generating..." : "Generate PDF"}
          </button>
          <br></br>
          <br></br>

          {pdfLink && (
            <a href={pdfLink} download="summary.pdf" className="download-link">
              ⬇️ Download Summary PDF
            </a>
          )}
        </div>
      </section>

      {/* ⚙️ HOW IT WORKS */}
      <section className="how-section" id="how">
        <div className="head_steps">
          <h2>How It Works</h2>
        </div>
        <div className="steps">
          <div className="step1">
            <h3>1. Upload</h3><br></br>
            <p>Choose your audio or video lecture file.</p>
          </div>
          <div className="step2">
            <h3>2. Transcribe</h3><br></br>
            <p>Our AI converts the content into accurate text.</p>
          </div>
          <div className="step3">
            <h3>3. Summarize</h3><br></br>
            <p>We summarize your lecture into a structured PDF.</p>
          </div>
        </div>
      </section>

      {/* 📩 FOOTER */}
      <footer className="footer">
        <p>© 2025 NoteWiz.<br></br> <br></br> Built with ❤️ to make learning smarter.</p>
      </footer>
    </div>
  );
}

export default App;
