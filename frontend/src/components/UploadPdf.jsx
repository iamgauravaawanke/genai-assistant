import { useState } from "react";
import { uploadPdf } from "../services/app";

function UploadPdf() {

  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {

    try {

      if (!file) {
        setMessage("Please select a PDF");
        return;
      }

      setUploading(true);

      const data = await uploadPdf(file);

      console.log(data);

      setMessage("PDF uploaded successfully");

    } catch (error) {

      console.error(error);

      setMessage("Upload failed");

    } finally {

      setUploading(false);

    }
  };

  return (
    <div>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        onClick={handleUpload}
        disabled={uploading}
      >
        {uploading ? "Uploading..." : "Upload PDF"}
      </button>

      <p>{message}</p>

    </div>
  );
}

export default UploadPdf;