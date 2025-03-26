from flask import Flask, render_template, jsonify, request
import asyncio
from threading import Thread
from provider import Provider

app = Flask(__name__)

providers = {}

@app.route('/')
def index():
    return render_template('index.html', providers=providers)

@app.route('/register_provider', methods=['POST'])
def register_provider():
    provider_name = request.form['provider_name']
    rate_limit = int(request.form['rate_limit'])
    window_duration = int(request.form['window_duration'])

    if provider_name not in providers:
        providers[provider_name] = Provider(provider_name, rate_limit, window_duration)
        # Start processing requests for the provider in a separate thread
        Thread(target=asyncio.run, args=(providers[provider_name].process_requests(),)).start()

    return jsonify({"status": "success", "message": f"Provider {provider_name} registered successfully!"})

@app.route('/get_providers', methods=['GET'])
def get_providers():
    providers_list = []
    for provider in providers.values():
        providers_list.append({
            'name': provider.name,
            'rate_limit': provider.rate_limit_per_window,
            'window_duration': provider.window_duration
        })
    return jsonify({'providers': providers_list})


@app.route('/send_request/<provider_name>', methods=['POST'])
def send_request(provider_name):
    if provider_name in providers:
        asyncio.run(providers[provider_name].add_request())
        return jsonify({"status": "success", "message": f"Request for {provider_name} added successfully!"})
    return jsonify({"status": "error", "message": f"Provider {provider_name} not found!"})

@app.route('/provider_status/<provider_name>', methods=['GET'])
def provider_status(provider_name):
    if provider_name in providers:
        status = providers[provider_name].get_status()
        return jsonify(status)
    return jsonify({"status": "error", "message": f"Provider {provider_name} not found!"})

if __name__ == '__main__':
    app.run(debug=True)
