# 1. 베이스 이미지 선택
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 복사
COPY . .

# 5. 애플리케이션 포트 노출
EXPOSE 5000

# 6. 애플리케이션 실행
# Gunicorn을 사용하여 앱을 안정적으로 실행합니다.
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"] 