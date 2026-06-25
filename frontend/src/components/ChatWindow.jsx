import { useEffect, useRef } from "react"

import MessageBubble from "./MessageBubble"


function ChatWindow(props) {
  // Reference for bottom div
  const bottomRef = useRef(null)

  // Auto scroll when messages change
  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    })
  }, [props.messages, props.loading])

  
  return (
    <div
      className="
        flex-1
        overflow-y-auto
        p-6
        space-y-6
        scrollbar-thin
        scrollbar-thumb-white/10
      "
    >
      {/* Messages */}
      {props.messages.map((msg, index) => (
        <MessageBubble
          key={index}
          role={msg.role}
          text={msg.text}
        />
      ))}

      {/* Loading */}
      {props.loading && (
        <MessageBubble
          role="bot"
          text="Thinking..."
        />
      )}

      {/* Bottom Reference */}
      <div ref={bottomRef} />
    </div>
  )
}

export default ChatWindow