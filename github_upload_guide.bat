@echo off
echo =========================================
echo 📁 GitHub Repository 파일 업로드 가이드
echo =========================================
echo.

echo 🎯 Step 1: 필수 파일들 확인
echo.
echo ✅ 다음 파일들이 준비되었는지 확인하세요:
echo    streamlit_app.py
echo    requirements.txt  
echo    .streamlit/config.toml
echo.

echo 📋 Step 2: 기존 repository로 이동
echo.
echo    cd your-existing-repository-folder
echo.

echo 📤 Step 3: 파일들 복사
echo.
echo    다음 파일들을 기존 repository 폴더에 복사하세요:
echo.
echo    필수 파일들:
echo    - streamlit_app.py          (메인 앱)
echo    - requirements.txt          (의존성)
echo    - .streamlit\config.toml    (테마)
echo.
echo    권장 파일들:
echo    - README_DEPLOY.md          (배포 가이드)
echo    - DEPLOYMENT_GUIDE.md       (상세 설명)
echo.

echo 🔄 Step 4: Git 명령어로 업로드
echo.
echo    git add .
echo    git commit -m "🚀 Add Toss-style dashboard for deployment"
echo    git push origin main
echo.

echo 🎉 Step 5: Streamlit Cloud에서 배포
echo.
echo    1. https://share.streamlit.io 접속
echo    2. 기존 repository 선택
echo    3. Main file: streamlit_app.py 지정
echo    4. Deploy 클릭!
echo.

echo 💡 Tip: 파일 구조 예시
echo.
echo    your-repository/
echo    ├── streamlit_app.py      ⭐ 메인 파일
echo    ├── requirements.txt      📦 의존성
echo    ├── .streamlit/
echo    │   └── config.toml      🎨 테마
echo    ├── README_DEPLOY.md     📖 가이드
echo    └── (기존 파일들...)
echo.

pause