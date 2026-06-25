import { Bot } from "lucide-react"

function Header() {
  return (
    <header
      className="
        h-[80px]
        border-b
        border-white/10
        bg-black/20
        backdrop-blur-xl
        flex
        items-center
        justify-between
        px-8
      "
    >
      {/* Left Section */}
      <div className="flex items-center gap-4">
        {/* Logo */}
        <div
          className="
            w-12
            h-12
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
          <Bot className="w-6 h-6 text-white" />
        </div>

        {/* Title */}
        <div>
          <h1 className="text-xl font-bold text-white">
            AI Assistant
          </h1>

          <p className="text-sm text-gray-400">
            FastAPI + React AI Agent
          </p>
        </div>
      </div>
    </header>
  )
}

export default Header