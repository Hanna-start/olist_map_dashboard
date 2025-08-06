# 🚀 Olist Toss Dashboard - Deployment Guide

## 📋 Quick Start Options

### 1. 🎯 Streamlit Cloud (추천! 무료 & 쉬움)

**준비 파일들:**
- ✅ `streamlit_app.py` - 메인 앱 (데이터 내장)
- ✅ `requirements.txt` - 의존성
- ✅ `.streamlit/config.toml` - 테마 설정

**배포 단계:**

1. **GitHub에 업로드**
   ```bash
   git init
   git add .
   git commit -m "Add Toss-style Olist dashboard"
   git branch -M main
   git remote add origin https://github.com/your-username/olist-toss-dashboard.git
   git push -u origin main
   ```

2. **Streamlit Cloud 배포**
   - [share.streamlit.io](https://share.streamlit.io)에 접속
   - GitHub 연결
   - 리포지토리 선택: `your-username/olist-toss-dashboard`
   - 메인 파일: `streamlit_app.py`
   - Deploy 클릭!

3. **완료!** 
   - 자동으로 URL 생성: `https://your-app-name.streamlit.app`

---

### 2. 🌐 Heroku (무료 티어 종료, 유료)

**파일들:**
```
Procfile
runtime.txt
requirements.txt
```

### 3. 🐳 Docker (고급 사용자용)

**파일들:**
```
Dockerfile
docker-compose.yml
```

### 4. 🔗 ngrok (로컬에서 즉시 공유)

**명령어:**
```bash
# ngrok 설치 후
ngrok http 8503
```

---

## 🎨 배포된 앱 특징

### Toss 디자인 요소
- 🎨 **브랜드 컬러**: #3182F6 (토스 블루)
- 📱 **반응형 레이아웃**: 모바일/데스크톱 최적화
- 🔤 **타이포그래피**: Noto Sans 폰트
- 🎯 **미니멀 디자인**: 깔끔하고 직관적

### 인터랙티브 기능
- 🗺️ **2가지 뷰**: Geographic Distribution / Shipping Flows
- 🎮 **인터랙티브 맵**: 줌, 팬, 클릭 가능
- 📊 **실시간 메트릭**: 고객/판매자 통계
- 🖱️ **툴팁**: 호버시 상세 정보

### 성능 최적화
- ⚡ **데이터 캐싱**: @st.cache_data 사용
- 📦 **경량화**: 내장 데이터로 빠른 로딩
- 🎯 **샘플링**: 대용량 데이터 최적화

---

## 🔧 커스터마이징

### 색상 변경
`streamlit_app.py`에서 색상 코드 수정:
```python
get_color=[49, 130, 246, 200]  # 파란색
get_color=[239, 68, 68, 200]   # 빨간색
```

### 데이터 교체
`create_demo_data()` 함수에서 실제 데이터로 변경

### 스타일 조정
CSS 섹션에서 폰트, 간격, 색상 커스터마이징

---

## 📱 공유 방법

### URL 공유
배포 완료 후 받은 URL을 공유:
```
https://your-app-name.streamlit.app
```

### QR 코드 생성
모바일 접속용 QR 코드 생성 가능

### 소셜 미디어
- 📸 스크린샷과 함께 URL 공유
- 🎥 화면 녹화로 데모 영상 제작

---

## 🆘 문제 해결

### 일반적인 문제들

1. **지도가 안 보여요**
   - pydeck 버전 확인: `pip install pydeck>=0.8.0`
   - 브라우저 새로고침

2. **배포가 실패해요**
   - requirements.txt 확인
   - Python 버전 호환성 확인

3. **느려요**
   - 데이터 샘플링 늘리기
   - 캐싱 설정 확인

### 지원

- 📧 **이슈 리포팅**: GitHub Issues
- 💬 **커뮤니티**: Streamlit Community
- 📚 **문서**: [Streamlit Docs](https://docs.streamlit.io)

---

**🎉 축하합니다! 이제 전 세계 어디서나 접속 가능한 멋진 대시보드를 만들었습니다!**