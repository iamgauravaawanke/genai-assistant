import { Button } from "@/components/ui/button"
import {
  MessageSquarePlus,
  Sparkles,
  Trash2,
} from "lucide-react"

function Sidebar({
  sessions,
  onNewChat,
  onSessionClick,
  activeSessionId,

}) {
  return (
    <aside
      className="
        w-[300px]
        h-screen
        bg-[#0B1120]
        border-r
        border-white/10
        p-5
        flex
        flex-col
        text-white
      "
    >
      {/* Logo */}
      <div className="flex items-center gap-3">
        <div
          className="
            h-10
            w-10
            rounded-2xl
            bg-gradient-to-r
            from-purple-600
            to-blue-600
            flex
            items-center
            justify-center
            shadow-lg
          "
        >
          <Sparkles className="h-5 w-5 text-white" />
        </div>

        <h1 className="text-2xl font-bold tracking-wide">
          NeuralAI
        </h1>
      </div>

      {/* New Chat */}
      <Button
        onClick={onNewChat}
        className="
          mt-8
          h-12
          rounded-2xl
          bg-gradient-to-r
          from-purple-600
          to-blue-600
          hover:opacity-90
          transition-all
        "
      >
        <MessageSquarePlus className="mr-2 h-5 w-5" />
        New Chat
      </Button>

      {/* Sessions */}
      <div className="mt-10 flex flex-col gap-3">

  {sessions.map((session) => (

    <div
      key={session.session_id}

      onClick={() =>
        onSessionClick(
          session.session_id
        )
      }

      className={`
        group
        border
        rounded-2xl
        p-4
        transition-all
        cursor-pointer
        flex
        items-center
        justify-between
        backdrop-blur-xl

        ${
          activeSessionId === session.session_id
            ? "bg-purple-600/30 border-purple-500"
            : "bg-white/5 hover:bg-white/10 border-white/10"
        }
      `}
    >
            <span className="text-sm font-medium truncate">
              {session.title || "Untitled Chat"}
            </span>

            <button
              className="
                opacity-0
                group-hover:opacity-100
                transition
                text-red-400
                hover:text-red-500
              "
            >
              <Trash2 className="h-4 w-4" />
            </button>
          </div>
        ))}
      </div>
    </aside>
  )
}

export default Sidebar