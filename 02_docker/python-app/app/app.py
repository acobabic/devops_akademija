from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Read the content of the /etc/hostname file
    try:
        with open('/etc/hostname', 'r') as f:
            hostname = f.read().strip()
    except Exception as e:
        hostname = f"Error reading /etc/hostname: {e}"

    # Return the hostname as part of an HTML response
    return f"<html><body><h1>Zdravo, ja se vrtim na doker kontejneru čiji je ID: {hostname}</h1></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

