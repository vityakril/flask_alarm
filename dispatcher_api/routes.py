from dispatcher_api import app

@app.route('/')
@app.route('/index')
def index():
    return "Test"
