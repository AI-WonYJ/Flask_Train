from asyncio.base_futures import _format_callbacks
from flask import Flask

app = Flask(__name__)

app.route('/')
def hello():
  return 'Hello, World!'
