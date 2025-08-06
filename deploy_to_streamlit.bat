@echo off
echo ========================================
echo 🚀 Olist Toss Dashboard - Quick Deploy
echo ========================================
echo.

echo 📋 Deployment Checklist:
echo ✅ streamlit_app.py (main app)
echo ✅ requirements.txt (dependencies)  
echo ✅ .streamlit/config.toml (theme)
echo.

echo 🔧 Next Steps:
echo.
echo 1. Create GitHub Repository:
echo    - Go to https://github.com/new
echo    - Repository name: olist-toss-dashboard
echo    - Make it Public
echo    - Don't initialize with README
echo.

echo 2. Upload Files to GitHub:
git init
git add .
git commit -m "🚀 Add Toss-style Olist dashboard for deployment"
echo.
echo    Copy these commands to run:
echo    git remote add origin https://github.com/YOUR-USERNAME/olist-toss-dashboard.git
echo    git branch -M main  
echo    git push -u origin main
echo.

echo 3. Deploy to Streamlit Cloud:
echo    - Go to https://share.streamlit.io
echo    - Click "New app"
echo    - Connect your GitHub account
echo    - Select repository: YOUR-USERNAME/olist-toss-dashboard
echo    - Main file path: streamlit_app.py
echo    - Click "Deploy!"
echo.

echo 🎉 Your app will be live at:
echo https://your-app-name.streamlit.app
echo.

echo 📱 Alternative - Quick Local Share with ngrok:
echo    1. Download ngrok from https://ngrok.com
echo    2. Run: ngrok http 8503
echo    3. Share the https URL it gives you!
echo.

pause