from flask import Flask 
app = Flask(__name__) 
 
@app.route('/test') 
def test(): 
    return 'Proxy is working!', 200, {'Access-Control-Allow-Origin': '*'} 
 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000) 
