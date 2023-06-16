import logging
from logging import StreamHandler
from waitress import serve
from flask import Flask, jsonify, send_from_directory
import requests
from snoopify import snoopify

app = Flask(__name__)

ZENQUOTES_API_URL = 'https://zenquotes.io/api/random'

# Remove default logger handler
app.logger.handlers.clear()

# Add custom logging handler for Replit
handler = StreamHandler()
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# Log when the application starts
app.logger.info("Application started")


def fetch_zen_quote():
  response = requests.get(ZENQUOTES_API_URL)
  if response.status_code == 200:
    result = response.json()
    quote = result[0]['q']
    return quote
  else:
    raise Exception(f"Error: {response.status_code}, {response.text}")


@app.route('/', methods=['GET'])
def serve_snoop_quote():
  app.logger.info("Fetching Snoopified Zen Quote")
  try:
    quote = fetch_zen_quote()
    snoop_quote = snoopify(quote)
    return jsonify({"quote": snoop_quote})
  except Exception as e:
    return jsonify({"error": str(e)}), 400


@app.route('/.well-known/ai-plugin.json')
def serve_ai_plugin():
  app.logger.info("Serving ai-plugin.json")
  return send_from_directory('.',
                             'ai-plugin.json',
                             mimetype='application/json')


@app.route('/.well-known/openapi.yaml')
def serve_openapi_yaml():
  app.logger.info("Serving openapi.yaml")
  return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')


if __name__ == '__main__':
  serve(app, host="0.0.0.0", port=8080)
