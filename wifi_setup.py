#!/usr/bin/env python3
from flask import Flask, render_template_string, request, redirect
import os
import subprocess

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Log in form</title>
    <link href="/static/css/login.css" rel="stylesheet">
</head>

<body>
{% block content %}
<div class="form">
    <form method="post" action="ap">
        <h2>AquaCore</h2>
        <h3>Please, enter credentials from your WI-FI network</h3>
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <ul class=flashes >
            {% for message in messages %}
            <h3>{{ message | safe }}</h3>
            {% endfor %}
        </ul>
        {% endif %}
        {% endwith %}

        <input type="text" placeholder="SSID" name="ssid" autofocus><br>
        <h3>&nbsp;</h3>
        <input type="password" placeholder="Password" name="password"><br>
        <h2>&nbsp;</h2>
        <input type="submit" value="Save and reboot" name="submit"><br>
        <h2>&nbsp;</h2>
    </form>
</div>
{% endblock %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ssid = request.form["ssid"]
        password = request.form["password"]

        conf = f'''
network={{
    ssid="{ssid}"
    psk="{password}"
}}
'''
        with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a") as f:
            f.write(conf)

        os.system("sync")
        os.system("reboot")

        return "Rebooting..."
    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
