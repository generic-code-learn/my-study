from flask import Flask, Response
import time

app = Flask(__name__)

@app.route('/chunked')
def chunked_response():
    def generate_chunks():
        for i in range(10):  # 假设我们有10个数据块
            yield f"Chunk #{i}\n"
            time.sleep(1)  # 模拟数据生成延迟

    return Response(generate_chunks(), mimetype='text/plain', headers={'Transfer-Encoding': 'chunked'})

if __name__ == '__main__':
    app.run(port=5000)
