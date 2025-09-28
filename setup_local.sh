#!/usr/bin/env bash
# Local development setup for GenAI Linux Agent

echo "🚀 Setting up GenAI Linux Agent for local development..."

# Create logs directory
mkdir -p logs

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cat > .env << EOF
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
EOF
    echo "⚠️  Please edit .env and add your actual Gemini API key!"
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "🔑 Next steps:"
echo "1. Get a Gemini API key from: https://aistudio.google.com/app/apikey"
echo "2. Edit .env file and replace 'your_gemini_api_key_here' with your actual key"
echo "3. Run: uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload"
echo "4. In another terminal, test with: ./agentctl \"show system info\""
