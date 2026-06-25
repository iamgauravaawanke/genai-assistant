import { Card } from "@/components/ui/card"
import { Bot, User } from "lucide-react"

function MessageBubble(props) {
  const isUser = props.role === "user"

  return (
    <div
      className={`
        flex
        items-start
        gap-4
        animate-in
        fade-in
        slide-in-from-bottom-2
        duration-300
        ${
          isUser
            ? "justify-end"
            : "justify-start"
        }
      `}
    >
      {/* Bot Avatar */}
      {!isUser && (
        <div
          className="
            w-10
            h-10
            rounded-full
            bg-gradient-to-r
            from-purple-600
            to-blue-600
            flex
            items-center
            justify-center
            shrink-0
            shadow-md
          "
        >
          <Bot className="w-5 h-5 text-white" />
        </div>
      )}

      {/* Message Bubble */}
      <Card
        className={`
          max-w-[85%]
          md:max-w-[700px]
          px-5
          py-4
          border
          border-white/10
          text-white
          shadow-lg
          break-words
          ${
            isUser
              ? `
                bg-gradient-to-r
                from-purple-600
                to-blue-600
                rounded-3xl
                rounded-tr-sm
              `
              : `
                bg-slate-800/70
                backdrop-blur-xl
                rounded-3xl
                rounded-tl-sm
              `
          }
        `}
      >
        <p className="leading-7 whitespace-pre-wrap">
          {props.text}
        </p>
      </Card>

      {/* User Avatar */}
      {isUser && (
        <div
          className="
            w-10
            h-10
            rounded-full
            bg-blue-600
            flex
            items-center
            justify-center
            shrink-0
            shadow-md
          "
        >
          <User className="w-5 h-5 text-white" />
        </div>
      )}
    </div>
  )
}

export default MessageBubble