import { useState,useRef } from "react"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { SendHorizontal } from "lucide-react"
import { uploadPdf } from "../services/app"

function ChatInput(props) {
  const [message, setMessage] = useState("")
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [uploadMessage, setUploadMessage] = useState("");
  const inputRef = useRef(null);

  const handleSend = () => {
    if (!message.trim()) return

    props.onSend(message)
    setMessage("")
  }


  const handleClick = () => {
  inputRef.current.click();
};

  const handleUpload = async () => {
  try {

    if (!file) {
      setUploadMessage("Please select a PDF");
      return;
    }

    setUploading(true);

    const data = await uploadPdf(file);

    console.log(data);

    setUploadMessage(
      "PDF uploaded successfully"
    );

  } catch (error) {

    console.error(error);

    setUploadMessage(
      "Upload failed"
    );

  } finally {

    setUploading(false);

  }
}
 

  return (
    <div className="p-6">
      <div
  className="
    flex
    items-center
    gap-4
    bg-white/5
    border
    border-white/10
    rounded-3xl
    p-3
    backdrop-blur-xl
  "
>

 <input
  ref={inputRef}
  type="file"
  accept=".pdf"
  className="hidden"
  onChange={(e) => {
    setFile(e.target.files[0]);
  }}
/>
  <Button
    variant="ghost"
    className="h-12 w-12 rounded-xl"
    onClick={handleClick}
  >
    📎
  </Button>

 <Input
  type="text"
  value={message}
  onChange={(e) => setMessage(e.target.value)}
  placeholder="Ask anything..."
  onKeyDown={(e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  }}
  className="
    border-0
    bg-transparent
    text-white
    placeholder:text-gray-400
    focus-visible:ring-0
    focus-visible:ring-offset-0
  "
/>

  <Button
    onClick={handleSend}
    className="
      h-14
      w-14
      rounded-2xl
      bg-gradient-to-r
      from-purple-600
      to-blue-600
      hover:opacity-90
    "
  >
    <SendHorizontal className="w-5 h-5" />
  </Button>

</div>
{
  file && (
    <div
      className="
        mt-3
        flex
        items-center
        gap-3
      "
    >
      <p
        className="
          text-sm
          text-gray-400
        "
      >
        📄 {file.name}
      </p>

      <Button
        onClick={handleUpload}
        disabled={uploading}
        size="sm"
      >
        {
          uploading
            ? "Uploading..."
            : "Upload"
        }
      </Button>
    </div>
  )
}

{
  uploadMessage && (
    <p
      className="
        mt-2
        text-sm
        text-green-400
      "
    >
      {uploadMessage}
    </p>
  )
}
    </div>
  )
}

export default ChatInput