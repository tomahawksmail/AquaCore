from flask import Flask, render_template, request, session, redirect, flash
import functions
import time
import os
from dotenv import load_dotenv
import pymysql
import hashlib
import accesspoint


app = Flask(__name__)
appAP = Flask(__name__)
load_dotenv()
connection = pymysql.connect(host=os.environ.get('HOST'),
                             user=os.environ.get('USER'),
                             password=os.environ.get('PASSWORD'),
                             database=os.environ.get('DATABASE'),
                             autocommit=True)


version = os.environ.get('VERSION')
app.secret_key = os.environ.get('SECRET_KEY')
appAP.secret_key = os.environ.get('SECRET_KEY')
app.config['SESSION_PERMANENT'] = False
appAP.config['SESSION_PERMANENT'] = False





@app.route("/", methods=['POST', 'GET'])
def start():
    return redirect("/login")


@app.route("/logout", methods=['POST', 'GET'])
def logout():
    functions.log("logout")
    session.pop('user', None)
    return redirect("/login")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if 'user' not in session:
        if request.method == 'POST':
            name = request.form["user"].lower()
            password = hashlib.md5(request.form["password"].encode('utf-8')).hexdigest()
            if name == '':
                flash("Enter username and password")
                return render_template('login.html', version=version)
            SQLrequest = """SELECT UserPassword, Role FROM users WHERE Username = %s"""
            try:
                connection.connect()
                with connection.cursor() as cursor:
                    cursor.execute(SQLrequest, name)
                result = cursor.fetchone()
                if result is None:
                    flash("Wrong username or password")
                    return render_template('login.html', version=version)
                getpass = result[0]
                getrole = result[1]
                cursor.close()
                connection.close()
            except Exception as E:
                flash("Something wrong...")
                functions.log(E)
                return redirect("/login")
            if password != getpass:
                flash("Wrong username or password")
                return redirect("/login")
            else:
                session['user'] = request.form['user']
                session['role'] = getrole
                functions.log("login")
                return redirect("/aquarium")
        else:
            return render_template('login.html', version=version)
    else:
        return redirect("/aquarium")


@app.route("/aquarium", methods=['POST', 'GET'])
def dashboard():
    if 'user' in session:
        if request.method == 'GET':
            connection.connect()
            SQLrequest = """SELECT DATE_FORMAT(DATETIME, '%D %H:%i'), temp, ph, tds FROM `data` ORDER BY id ASC LIMIT 48"""
            min_temp_request = """SELECT min_temp FROM options"""
            max_temp_request = """SELECT max_temp FROM options"""
            min_ph_request = """SELECT min_ph FROM options"""
            max_ph_request = """SELECT max_ph FROM options"""
            tds_request = """SELECT tds FROM options"""
            current = """SELECT temp, ph, tds FROM `data` ORDER BY id DESC LIMIT 1"""

            try:
                with connection.cursor() as cursor:
                    cursor.execute(SQLrequest)
                result = cursor.fetchall()

                with connection.cursor() as cursor:
                    cursor.execute(min_temp_request)
                min = cursor.fetchone()[0]
                min_temp = [min for i in range(48)]

                with connection.cursor() as cursor:
                    cursor.execute(max_temp_request)
                max = cursor.fetchone()[0]
                max_temp = [max for i in range(48)]


                with connection.cursor() as cursor:
                    cursor.execute(min_ph_request)
                minph = cursor.fetchone()[0]
                min_ph = [minph for i in range(48)]

                with connection.cursor() as cursor:
                    cursor.execute(max_ph_request)
                maxph = cursor.fetchone()[0]
                max_ph = [maxph for i in range(48)]

                with connection.cursor() as cursor:
                    cursor.execute(tds_request)
                tds = cursor.fetchone()[0]
                tds = [tds for i in range(48)]

                with connection.cursor() as cursor:
                    cursor.execute(current)
                current = cursor.fetchone()
            except Exception as E:
                functions.log(E)
                return render_template('aquarium.html', version=version)
            else:
                cursor.close()
                connection.close()
            return render_template('aquarium.html', version=version, result=result, min_temp=min_temp, max_temp=max_temp, min_ph=min_ph, max_ph=max_ph, tds=tds, current=current)
        else:
            return render_template('aquarium.html', version=version, result=None)
    else:
        flash("You are not logged in")
        return redirect("/login")


@app.route("/options", methods=['POST', 'GET'])
def options():
    if 'user' in session:
        if request.method == 'GET':
            result = functions.getDatatoOptions()
            return render_template('options.html', version=version, result=result[0], status=result[1])
        elif request.method == 'POST':
            if "submit" in request.form:
                formstatus = []
                formoptions = []
                # get all data from form and save to list "formstatus"
                # history
                formoptions.append(('history', request.form.get("history")))

                # temp
                formoptions.append(('min_temp', request.form.get("min_temp")))
                formoptions.append(('max_temp', request.form.get("max_temp")))

                # ph
                formoptions.append(('min_ph', request.form.get("min_ph")))
                formoptions.append(('max_ph', request.form.get("max_ph")))

                # tds
                formoptions.append(('tds', request.form.get("tds")))


                # co2
                formstatus.append(('co2_status', request.form.get("co2")))
                formoptions.append(('co2_on', request.form.get("co2_on")))
                formoptions.append(('co2_off', request.form.get("co2_off")))

                # o2
                formstatus.append(('o2_status', request.form.get("o2")))
                formoptions.append(('o2_on', request.form.get("o2_on")))
                formoptions.append(('o2_off', request.form.get("o2_off")))

                # heater
                formstatus.append(('heater_status', request.form.get("heater_status")))
                formoptions.append(('heater_temp', request.form.get("heater_temp")))

                # UV
                formstatus.append(('UV_status', request.form.get("UV_status")))
                formoptions.append(('UV_on', request.form.get("UV_on")))
                formoptions.append(('UV_off', request.form.get("UV_off")))



                # light
                # Master Light
                formstatus.append(('MasterL_status', request.form.get("MasterL_status")))
                formoptions.append(('Master_light_on', request.form.get("Master_light_on")))
                formoptions.append(('Master_light_off', request.form.get("Master_light_off")))

                formstatus.append(('Projector_status', request.form.get("Projector_status")))
                formoptions.append(('ProjectorL_on', request.form.get("ProjectorL_on")))
                formoptions.append(('ProjectorL_off', request.form.get("ProjectorL_off")))

                formstatus.append(('MoonL_status', request.form.get("MoonL_status")))
                formoptions.append(('MoonL_on', request.form.get("MoonL_on")))
                formoptions.append(('MoonL_off', request.form.get("MoonL_off")))

                formstatus.append(('PlantL_status', request.form.get("PlantL_status")))
                formoptions.append(('PlantL_on', request.form.get("PlantL_on")))
                formoptions.append(('PlantL_off', request.form.get("PlantL_off")))

                functions.setDataOptions(formoptions)
                functions.setDataStatus(formstatus)

                result = functions.getDatatoOptions()
                return render_template('options.html', version=version, result=result[0], status=result[1])
    else:
        flash("You are not logged in")
        return redirect("/login")

@app.route("/loging", methods=['POST', 'GET'])
def loging():
    SQLrequest = """SELECT * FROM loging ORDER BY id DESC LIMIT 30"""
    try:
        connection.connect()
        with connection.cursor() as cursor:
            cursor.execute(SQLrequest)
        log = cursor.fetchall()
        cursor.close()
        connection.close()
    except Exception as E:
        functions.log(E)
    return render_template('log.html', version=version, log=log)


@app.route("/core_dashboard", methods=['POST', 'GET'])
def core_dashboard():
    data = functions.get_core_data()
    temp_data = functions.get_temp_data()
    cur_data = functions.get_cur_data()
    RAM_data = functions.get_RAM_data()
    return render_template('core_dashboard.html', version=version, data=data, cur_data=cur_data, temp_data=temp_data, RAM_data=RAM_data)


@app.route("/terminal", methods=['POST', 'GET'])
def terminal():
    if 'user' in session:
        if request.method == 'GET':
            from gpio import readGPIO
            return render_template('terminal.html', version=version, readall=readGPIO())
        else:
            pass
    else:
        flash("You are not logged in")
        return redirect("/login")



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True)







