export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      <div className="flex flex-col items-center justify-center min-h-screen px-4">
        <div className="text-center space-y-8">
          {/* Header */}
          <div className="space-y-4">
            <h1 className="text-6xl font-bold text-white tracking-tighter">
              AI Reel Generator
            </h1>
            <p className="text-xl text-slate-300">
              Generate cinematic videos from stories
            </p>
          </div>

          {/* Status Section */}
          <div className="flex items-center justify-center">
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-r from-blue-500 to-cyan-500 rounded-lg blur opacity-25"></div>
              <div className="relative bg-slate-800 border border-slate-700 rounded-lg px-8 py-4">
                <div className="flex items-center gap-3">
                  <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
                  <span className="text-slate-200 font-semibold">System Ready</span>
                </div>
              </div>
            </div>
          </div>

          {/* Features Grid */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mt-16">
            <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur hover:bg-slate-800/80 transition">
              <div className="text-3xl mb-3">🎬</div>
              <h3 className="text-lg font-semibold text-white mb-2">Story Input</h3>
              <p className="text-slate-400 text-sm">Input your story and let AI generate videos</p>
            </div>

            <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur hover:bg-slate-800/80 transition">
              <div className="text-3xl mb-3">✨</div>
              <h3 className="text-lg font-semibold text-white mb-2">AI Generation</h3>
              <p className="text-slate-400 text-sm">Automated character, voice, and scene generation</p>
            </div>

            <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-6 backdrop-blur hover:bg-slate-800/80 transition">
              <div className="text-3xl mb-3">🎥</div>
              <h3 className="text-lg font-semibold text-white mb-2">Video Export</h3>
              <p className="text-slate-400 text-sm">Export cinematic videos ready for sharing</p>
            </div>
          </div>

          {/* CTA */}
          <div className="flex gap-4 justify-center mt-12">
            <button className="bg-gradient-to-r from-blue-500 to-cyan-500 text-white font-semibold px-8 py-3 rounded-lg hover:opacity-90 transition">
              Get Started
            </button>
            <button className="border border-slate-600 text-slate-300 font-semibold px-8 py-3 rounded-lg hover:bg-slate-800 transition">
              Documentation
            </button>
          </div>
        </div>
      </div>
    </main>
  );
}
