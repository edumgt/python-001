## 사용할 python 지정 및 env 만드는 명령

c:\Python310\python -m venv venv
c:\Python313\python -m venv venv2
venv\Scripts\activate

## http 서버 실행

uvicorn app:app --reload

## 라이브러리 목록 보기

pip list
pip freeze > requirements.txt
