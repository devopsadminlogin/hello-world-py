from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Read environment variables
FLASK_APP = os.getenv("FLASK_APP")
FLASK_RUN_HOST = os.getenv("FLASK_RUN_HOST")
FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT")

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host=FLASK_RUN_HOST, port=FLASK_RUN_PORT, debug=True)

