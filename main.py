from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/status')
def status():
    status_data = {
        "いるか線": "工事のため10分以上遅延",
        "いるか電鉄": "停止",
        "山岳線": "運休中",
        "海風線": "一部遅延 (10分程度)"
    }
    return jsonify(status_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
