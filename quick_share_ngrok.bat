@echo off
echo ========================================
echo 🌐 Quick Share with ngrok
echo ========================================
echo.

echo 🔍 Checking if ngrok is available...
where ngrok >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ ngrok not found!
    echo.
    echo 📥 Download ngrok:
    echo 1. Go to https://ngrok.com/download
    echo 2. Download and extract ngrok.exe
    echo 3. Put ngrok.exe in this folder
    echo.
    pause
    exit /b 1
)

echo ✅ ngrok found!
echo.

echo 🚀 Starting Streamlit app on port 8503...
start /b python -m streamlit run streamlit_app.py --server.port=8503

echo ⏳ Waiting for app to start...
timeout /t 5 /nobreak >nul

echo 🌐 Creating public tunnel...
echo.
echo 🔗 Your dashboard will be available at the HTTPS URL shown below:
echo 📱 Share this URL with anyone to access your dashboard!
echo.
echo 🛑 Press Ctrl+C to stop sharing
echo.

ngrok http 8503