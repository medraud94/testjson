from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # GitHub Actions에서 전달한 이미지 태그를 화면에 표시 (환경변수 사용)
    image_tag = os.environ.get('IMAGE_TAG', 'N/A')
    return f'<h1>CI/CD Pipeline is LIVE!</h1><p>Image Tag: {image_tag}</p>'

if __name__ == "__main__":
    # 포트는 8080을 사용하도록 설정
    app.run(host='0.0.0.0', port=8080) 