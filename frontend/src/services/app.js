import { ForkKnife, Form } from "lucide-react"

export const sendMessageToAI = async (
  message,
  sessionId
) => {
  try {

    console.log({
      message,
      session_id: sessionId,
    })

    const response = await fetch(
      "http://127.0.0.1:8000/chat",
      {
        method: "POST",
        headers: {
          "Content-Type":
            "application/json",
        },
        body: JSON.stringify({
          message,
          session_id: sessionId,
        }),
      }
    )

    const data =
      await response.json()

    return data

  } catch (error) {

    console.log(error)

    return {
      response:
        "Server connection failed.",
    }
  }
}
// export const getMessages = async () => {

//   const response = await fetch(
//     "http://127.0.0.1:8000/messages"
//   );

//   const data = await response.json();

//   return data;
// };


export const getallSessions = async () =>{
  const response = await fetch (
    "http://127.0.0.1:8000/get_all_sessions"
  );
  const data = await response.json();

  return data 
};


export const createSession = async () => {
  const response = await fetch(
    "http://127.0.0.1:8000/sessions",
    {
      method: "POST",
    }
  )

  const data = await response.json()

  return data
}


export const getMessagesBySession =
  async (sessionId) => {

    const response = await fetch(
      `http://127.0.0.1:8000/messages/${sessionId}`
    )

    const data =
      await response.json()

    return data
}

export async function uploadPdf(file) {

  const formData = new FormData();

  formData.append("file", file);

  const response = await fetch(
    "http://localhost:8000/upload_file",
    {
      method: "POST",
      body: formData,
    }
  );

  return response.json();
}