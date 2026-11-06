import os
from flask import Flask, abort

app = Flask(__name__)

# Aapka real V2Box / Hysteria2 subscription payload
CONFIG_PAYLOAD = "hy2://XREG-49B5-A1F0-B53A.1793843700.18f9a12063d00b18ef54234d3648d914@wraith-bom3.xreg.site:443?security=tls&insecure=1&alpn=http/1.1&sni=wraith-bom3.xreg.site#BOOSTER X WIRE 1 month"

@app.route('/')
def home():
    return "V2Box Subscription Server is Running Live!"

@app.route('/sub/<key>')
def get_subscription(key):
    clean_key = key.strip()
    
    # Agar key valid format ki hai toh server automatic yeh config return kar dega
    if clean_key.startswith("BX-VIP-") and len(clean_key) >= 10:
        return CONFIG_PAYLOAD
    else:
        abort(404, description="Invalid Key")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
