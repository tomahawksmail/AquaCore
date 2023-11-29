import os
from main import app, AP
host = '0.0.0.0'
port = 80
path = 'lock1'





if os.path.isfile(path):
    app.run(debug=False, passthrough_errors=True, use_reloader=False, host=host, port=port)
else:
    AP()

