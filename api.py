from forms import *

@app.route('/assets/<path:path>')
def send_all(path):
    return send_from_directory('assets', path)