# acon3d-assignment

### 환경설정
```
# virtualenv 설치
pip3 install virtualenv
virtualenv venv

# 가상환경 실행
source venv/bin/activate      #가상환경 종료 커맨드:deactivate

# venv에서 사용되는 파이썬 버전 변경
virtualenv venv --python=/usr/bin/python3 # python3.8설치

# 모듈설치
pip3 install -r requirements.txt
```

### .env 생성
프로젝트의 루트에 아래 acon3d-assignment 폴더 밑 .env 생성

```
#vi .env
DRIVER_PATH=                          # chromedriver 위치 ex)"/Users/jk/work/acon3d-assignment/acon3d-assignment/Drivers/chromedriver"
URL="https://www.acon3d.com/ko/toon/" # 테스트 URL
IS_HEADLESS=0                         # 0:크롬창 있음 1:크롬창 없이 실행
USER_ID=                              # acon3d 로그인 아이디  
USER_PW=                              # acon3d 로그인 패스워드
```

### 실행
프로젝트의 루트 acon3d-assignment 폴더 밑에서 실행 
```
pytest Tests/ --html-report=./Reports 
```

### 리포트 확인
Report/pytest_html_report.html(크롬) 확인가능
