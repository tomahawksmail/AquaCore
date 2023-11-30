import os
host = '192.168.50.1'
port = 80
path = 'lock1'





if os.path.isfile(path):
    app.run(debug=False, passthrough_errors=True, use_reloader=False, host=host, port=port)
else:
    ap()

