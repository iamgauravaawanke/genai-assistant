import { useState, useEffect } from "react"

import Sidebar from "../components/Sidebar"
import Header from "../components/Header"
import ChatWindow from "../components/ChatWindow"
import ChatInput from "../components/ChatInput"
import UploadPdf from "../components/UploadPdf";

import {
  sendMessageToAI,
  // getMessages,
  getallSessions,
  createSession,
  getMessagesBySession,
  

} from "../services/app"



function Home() {
  const [messages, setMessages] = useState([])

  const [loading, setLoading] = useState(false)

  const [activeSessionId, setActiveSessionId] = useState(null)

  const [sessions , setSessions] = useState([])

  // Load chat history from backend
  useEffect(() => {
    // loadMessages()
    loadSessions()

  }, [])

  // const loadMessages = async () => {
  //   try {
  //     const data = await getMessages()

  //     const formattedMessages = []

  //     data.forEach((msg) => {
  //       formattedMessages.push({
  //         role: "user",
  //         text: msg.user_input,
  //       })

  //       formattedMessages.push({
  //         role: "bot",
  //         text: msg.ai_response,
  //       })
  //     })

  //     setMessages(formattedMessages)
  //   } catch (error) {
  //     console.log("Load Messages Error:", error)
  //   }
  // }

  const loadSessions = async () =>{
    try{
      const data = await getallSessions()
      console.log("API DATA:", data)

      

      setSessions(data)

      console.log(
        "Sessions:--",
        data

      )

    } catch(error){
      console.log("load sessions error:-" , error)
    }

  }

  const handleNewChat = async () => {
  try {

    const data = await createSession()

    console.log(
      "New Session:",
      data
    )

    setActiveSessionId(
      data.session_id
    )

    loadSessions()

  } catch (error) {

    console.log(
      "Create Session Error:",
      error
    )

  }
}



  // Handle Send Message
  const handleSendMessage = async (message) => {
    

    console.log("ACTIVE SESSION ID:",activeSessionId)


    if (!message.trim()) return
    if (!activeSessionId) {
  alert("Please create a new chat first")
  return
}

    const userMessage = {
      role: "user",
      text: message,
    }

    setMessages((prev) => [...prev, userMessage])

    setLoading(true)

    try {
      const data = await sendMessageToAI(message,activeSessionId)



      const botMessage = {
        role: "bot",
        text: data.response,
      }

      setMessages((prev) => [...prev, botMessage])
    } catch (error) {
      console.log(error)

      const errorMessage = {
        role: "bot",
        text: "Something went wrong. Please try again.",
      }

      setMessages((prev) => [...prev, errorMessage])
    } finally {
      setLoading(false)
    }
    loadSessions()
    
  }


  ///handlesessionclick 
 
  const handleSessionClick = async (sessionId) =>{

    console.log("session clicked:---", sessionId)


    setActiveSessionId(sessionId)


    const data =
    await getMessagesBySession(
      sessionId
    )


    const formattedMessages = []

    data.forEach((msg) => {

  formattedMessages.push({
    role: "user",
    text: msg.user_input,
  })

  formattedMessages.push({
    role: "bot",
    text: msg.ai_response,
  })

})

setMessages(
  formattedMessages
)

  }

  return (
    <div
      className="
        flex
        h-screen
        overflow-hidden
        bg-[#020617]
        text-white
      "
    >
  
      <Sidebar
      sessions={sessions}
      onNewChat={handleNewChat}
      onSessionClick={handleSessionClick}
      activeSessionId={activeSessionId}
      

       />

      <div className="flex flex-1 flex-col">
        <Header />

        <ChatWindow
          messages={messages}
          loading={loading}
        />

        <ChatInput
          onSend={handleSendMessage}
        />
         
      </div>
      
    </div>
  )
}

export default Home