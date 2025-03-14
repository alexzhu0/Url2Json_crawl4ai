from flask import Flask, render_template, request, jsonify
import asyncio
import json
import os
from main import crawl_and_analyze, check_dependencies

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "URL不能为空"}), 400
    
    # 检查依赖
    if not check_dependencies():
        return jsonify({"error": "缺少必要的依赖，请安装playwright"}), 500
    
    # 创建事件循环并运行异步函数
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(crawl_and_analyze(url))
        loop.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)