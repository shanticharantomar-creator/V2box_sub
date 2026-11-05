from flask import Flask, abort
import time

app = Flask(__name__)

ACTIVE_KEYS = {
    "BX-VIP-4AAY12": {
        "exp": time.time() + 86400,
        "payload": "hy2://XREG-49B5-A1F0-B53A.1793843700.18f9a12063d00b18ef54234d3648d914@wraith-bom3.xreg.site:443?security=tls&insecure=1&alpn=http/1.1&sni=wraith-bom3.xreg.site#BOOSTER X WIRE 1 month"
    }
}

@app.route('/sub/<key>')
def get_subscription(key):
    if key not in ACTIVE_KEYS:
        abort(404, description="Invalid Key")
    
    data = ACTIVE_KEYS[key]
    if time.time() > data["exp"]:
        abort(403, description="Subscription Expired")
        
    return data["payload"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
