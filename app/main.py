from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! I am Desigapperumal. This pipeline was successfully built and deployed via Jenkins and Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
