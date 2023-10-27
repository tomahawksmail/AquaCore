from main import app

host = '0.0.0.0'
port = 5543

# run the app
if __name__ == "__main__":
    # app.run(debug=False, passthrough_errors=True, use_reloader=False, host=host, port=port)
    app.run(debug=True, host='0.0.0.0', port=5543)