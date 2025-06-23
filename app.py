from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    # 환경 정보 수집
    info = {
        'message': 'CI/CD Pipeline is LIVE!',
        'image_tag': os.environ.get('IMAGE_TAG', 'N/A'),
        'environment': os.environ.get('ENVIRONMENT', 'unknown'),
        'branch': os.environ.get('BRANCH_NAME', 'unknown'),
        'commit_sha': os.environ.get('COMMIT_SHA', 'N/A'),
        'hostname': socket.gethostname(),
        'timestamp': datetime.now().isoformat()
    }
    
    # HTML 응답 (더 보기 좋게)
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>TestJSON CI/CD</title>
        <style>
            body {{ 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh; color: white;
            }}
            .container {{ 
                max-width: 800px; margin: 0 auto; background: rgba(255,255,255,0.1);
                padding: 30px; border-radius: 15px; backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            }}
            .header {{ text-align: center; margin-bottom: 30px; }}
            .status {{ 
                background: #4CAF50; padding: 15px; border-radius: 8px; 
                text-align: center; font-weight: bold; margin: 20px 0;
            }}
            .info-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
            .info-card {{ 
                background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px;
                border-left: 4px solid #4CAF50;
            }}
            .info-label {{ font-weight: bold; opacity: 0.8; font-size: 0.9em; }}
            .info-value {{ font-size: 1.1em; margin-top: 5px; }}
            .links {{ margin-top: 30px; text-align: center; }}
            .link {{ 
                display: inline-block; margin: 0 10px; padding: 10px 20px;
                background: rgba(255,255,255,0.2); border-radius: 5px;
                color: white; text-decoration: none; transition: all 0.3s;
            }}
            .link:hover {{ background: rgba(255,255,255,0.3); }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚀 {info['message']}</h1>
                <div class="status">✅ APPLICATION RUNNING</div>
            </div>
            
            <div class="info-grid">
                <div class="info-card">
                    <div class="info-label">Image Tag</div>
                    <div class="info-value">{info['image_tag']}</div>
                </div>
                <div class="info-card">
                    <div class="info-label">Environment</div>
                    <div class="info-value">{info['environment']}</div>
                </div>
                <div class="info-card">
                    <div class="info-label">Branch</div>
                    <div class="info-value">{info['branch']}</div>
                </div>
                <div class="info-card">
                    <div class="info-label">Commit SHA</div>
                    <div class="info-value">{info['commit_sha'][:12]}...</div>
                </div>
                <div class="info-card">
                    <div class="info-label">Hostname</div>
                    <div class="info-value">{info['hostname']}</div>
                </div>
                <div class="info-card">
                    <div class="info-label">Deployed At</div>
                    <div class="info-value">{info['timestamp'][:19]}</div>
                </div>
            </div>
            
            <div class="links">
                <a href="/health" class="link">🏥 Health Check</a>
                <a href="/info" class="link">📊 JSON Info</a>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'hostname': socket.gethostname(),
        'version': os.environ.get('IMAGE_TAG', 'unknown')
    }), 200

@app.route('/info')
def info():
    """System information in JSON format"""
    return jsonify({
        'message': 'CI/CD Pipeline is LIVE!',
        'image_tag': os.environ.get('IMAGE_TAG', 'N/A'),
        'environment': os.environ.get('ENVIRONMENT', 'unknown'),
        'branch': os.environ.get('BRANCH_NAME', 'unknown'),
        'commit_sha': os.environ.get('COMMIT_SHA', 'N/A'),
        'hostname': socket.gethostname(),
        'timestamp': datetime.now().isoformat(),
        'registry': 'Self-hosted Docker Registry'
    })

if __name__ == "__main__":
    # 포트는 8080을 사용하도록 설정
    app.run(host='0.0.0.0', port=8080, debug=False) 