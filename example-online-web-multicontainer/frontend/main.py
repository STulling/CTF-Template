from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://multicontainer-backend:5001/flag')
    if response.status_code == 200:
        flag = response.json().get('flag')
        return flag, 200
    else:
        return 'Error fetching flag from backend', 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
