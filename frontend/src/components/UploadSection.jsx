import { useState } from "react";
import axios from "axios";

const UploadSection = () => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [pdfLink, setPdfLink] = useState("");

  const handleUpload = async () => {
    if (!file) return alert("Please select a file first.");

    const formData = new FormData();
    formData.append("file", file);
    setLoading(true);

    try {
      const res = await axios.post(
        "http://127.0.0.1:5000/generate-pdf-from-audio",
        formData,
        { responseType: "blob" }
      );
      const url = window.URL.createObjectURL(new Blob([res.data]));
      setPdfLink(url);
    } catch (err) {
      console.error(err);
      alert("Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section style={styles.section}>
      <div style={styles.card}>
        <input
          type="file"
          accept="audio/*,video/*"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button onClick={handleUpload} disabled={loading}>
          {loading ? "Processing..." : "Generate PDF"}
        </button>
        {pdfLink && (
          <a href={pdfLink} download="summary.pdf" style={styles.download}>
            ⬇️ Download Summary PDF
          </a>
        )}
      </div>
    </section>
  );
};

const styles = {
  section: {
    display: "flex",
    justifyContent: "center",
    padding: "2rem",
  },
  card: {
    background: "rgba(255,255,255,0.08)",
    padding: "2rem",
    borderRadius: "15px",
    textAlign: "center",
    boxShadow: "0 0 25px rgba(255, 255, 255, 0.1)",
    maxWidth: "450px",
    width: "100%",
  },
  download: {
    display: "inline-block",
    marginTop: "1rem",
    padding: "0.5rem 1rem",
    backgroundColor: "#00c9ff",
    color: "black",
    borderRadius: "8px",
    textDecoration: "none",
  },
};

export default UploadSection;
