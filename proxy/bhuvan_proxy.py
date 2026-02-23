from flask import Flask, Response
import requests
import sys

def print_flush(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()

app = Flask(__name__)

@app.route('/tiles/<int:z>/<int:x>/<int:y>.jpg')
def get_tile(z, x, y):
    print_flush(f'[PROXY] Request: {z}/{x}/{y}')
    url = f'https://bhuvan-vec1.nrsc.gov.in/bhuvan/gwc/service/tms/1.0.0/india3@EPSG:900913@jpg/{z}/{x}/{y}.jpg'
    print_flush(f'[PROXY] URL: {url}')
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://bhuvan.nrsc.gov.in/',
            'Origin': 'https://bhuvan.nrsc.gov.in'
        }
        r = requests.get(url, headers=headers, timeout=10)
        print_flush(f'[PROXY] Response: {r.status_code}, Size: {len(r.content)}')
        if r.status_code == 200:
            return Response(r.content, content_type='image/jpeg', headers={'Access-Control-Allow-Origin': '*'})
        else:
            return f'Bhuvan: {r.status_code}', r.status_code
    except Exception as e:
        print_flush(f'[PROXY] Error: {e}')
        return str(e), 500

if __name__ == '__main__':
    print_flush('[PROXY] Starting on http://localhost:5000')
    app.run(host='0.0.0.0', port=5000, debug=False)