from flask import Flask, render_template, request, session, send_file, redirect, flash
from datetime import datetime
import os
from dotenv import load_dotenv
import pymysql
import hashlib
import csv
import logging

app = Flask(__name__)
# logging.basicConfig(filename='app.log',
#                     level=logging.WARNING,
#                     format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

load_dotenv()
connection = pymysql.connect(host=os.environ.get('HOST'),
                             user=os.environ.get('USER'),
                             password=os.environ.get('PASSWORD'),
                             database=os.environ.get('DATABASE'))

version = os.environ.get('VERSION')
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SESSION_PERMANENT'] = False


@app.route("/", methods=['POST', 'GET'])
def start():
    return redirect("/login")


@app.route("/logout", methods=['POST', 'GET'])
def logout():
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
                return redirect("/login")
            if password != getpass:
                flash("Wrong username or password")
                return redirect("/login")
            else:
                session['user'] = request.form['user']
                session['role'] = getrole
                return redirect("/aquarium")
        else:
            return render_template('login.html', version=version)
    else:
        return redirect("/aquarium")


# @app.route("/aquarium", methods=['POST', 'GET'])
# def dashboard():
#     # insert()
#     if 'user' in session:
#         if request.method == 'GET':
#             connection.connect()
#             SQLrequest = """SELECT DATE_FORMAT(DATETIME, '%D %H:%i'), temp, ph, tds FROM `data` ORDER BY id ASC LIMIT 48"""
#             min_temp_request = """SELECT min_temp FROM options"""
#             max_temp_request = """SELECT max_temp FROM options"""
#             min_ph_request = """SELECT min_ph FROM options"""
#             max_ph_request = """SELECT max_ph FROM options"""
#             tds_request = """SELECT tds FROM options"""
#             current = """SELECT temp, ph, tds FROM `data` ORDER BY id DESC LIMIT 1"""
#
#             try:
#                 with connection.cursor() as cursor:
#                     cursor.execute(SQLrequest)
#                 result = cursor.fetchall()
#
#                 with connection.cursor() as cursor:
#                     cursor.execute(min_temp_request)
#                 min = cursor.fetchone()[0]
#                 min_temp = [min for i in range(48)]
#
#                 with connection.cursor() as cursor:
#                     cursor.execute(max_temp_request)
#                 max = cursor.fetchone()[0]
#                 max_temp = [max for i in range(48)]
#
#                 with connection.cursor() as cursor:
#                     cursor.execute(min_ph_request)
#                 minph = cursor.fetchone()[0]
#                 min_ph = [minph for i in range(48)]
#
#                 with connection.cursor() as cursor:
#                     cursor.execute(max_ph_request)
#                 maxph = cursor.fetchone()[0]
#                 max_ph = [maxph for i in range(48)]
#
#                 with connection.cursor() as cursor:
#                     cursor.execute(tds_request)
#                 tds = cursor.fetchone()[0]
#                 tds = [tds for i in range(48)]
#
#                 with connection.cursor() as cursor:
#                     cursor.execute(current)
#                 current = cursor.fetchone()
#             except Exception as E:
#                 return render_template('aquarium.html', version=version)
#             else:
#                 cursor.close()
#                 connection.close()
#             return render_template('aquarium.html', version=version, result=result, min_temp=min_temp, max_temp=max_temp, min_ph=min_ph, max_ph=max_ph, tds=tds, current=current)
#         else:
#             return render_template('aquarium.html', version=version, result=None)
#     else:
#         flash("You are not logged in")
#         return redirect("/login")

def getDatatoOptions():
    SQLrequest = """SELECT * FROM options"""
    status = """SELECT * FROM status"""
    try:
        connection.connect()
        with connection.cursor() as cursor:
            cursor.execute(SQLrequest)
        options = cursor.fetchone()
        with connection.cursor() as cursor:
            cursor.execute(status)
        status = cursor.fetchall()[0]
        result = (options, status)
    except Exception as E:
        print(E)
    else:
        cursor.close()
        connection.close()
    return result


def setData(formstatus):
    print(formstatus)
    for i in formstatus:
        print(i)
    # statuslistDB = getDatatoOptions()
    # print(statuslistDB)
    #
    # SQL = """UPDATE `status` SET %s=%s"""
    # try:
    #     with connection.cursor() as cursor:
    #         for i in formstatus:
    #             if i == 'on':
    #                 i = 'checked'
    #             else:
    #                 i = 'unchecked'
    #                 print(i)
    # #             cursor.execute(SQL, ( , i))
    # #         connection.commit()
    #         cursor.close()
    #         connection.close()
    # except Exception as E:
    #     print(E)


@app.route("/options", methods=['POST', 'GET'])
def options():
    if 'user' in session:
        if request.method == 'GET':
            result = getDatatoOptions()
            return render_template('options.html', version=version, result=result[0], status=result[1])
        elif request.method == 'POST':
            if "submit" in request.form:
                # get all data from form and save to list "formstatus"

                # co2
                formstatus = []
                co2 = request.form.get("co2")
                formstatus.append(('co2', co2))
                CO2_on = request.form.get("CO2_on")
                formstatus.append(('CO2_on', CO2_on))
                CO2_off = request.form.get("CO2_off")
                formstatus.append(('CO2_off', CO2_off))

                # o2
                o2 = request.form.get("o2")
                formstatus.append(('o2', o2))
                o2_on = request.form.get("o2_on")
                formstatus.append(('o2_on', o2_on))
                o2_off = request.form.get("o2_off")
                formstatus.append(('o2_off', o2_off))

                # heater
                heater_status = request.form.get("heater_status")
                formstatus.append(('heater_status', heater_status))
                heater = request.form.get("heater")
                formstatus.append(('heater', heater))









                Master_light_status = request.form.get("Master_light_status")
                formstatus.append(('Master_light_status', Master_light_status))
                RedL_status = request.form.get("RedL_status")
                formstatus.append(('RedL_status', RedL_status))
                BlueL_status = request.form.get("BlueL_status")
                formstatus.append(('BlueL_status', BlueL_status))
                MoonL_status = request.form.get("MoonL_status")
                formstatus.append(('MoonL_status', MoonL_status))
                ProjectorL_status = request.form.get("ProjectorL_status")
                formstatus.append(('ProjectorL_status', ProjectorL_status))



                Master_light_on = request.form.get("Master_light_on")
                formstatus.append(('Master_light_on', Master_light_on))



                setData(formstatus)

                result = getDatatoOptions()
                return render_template('options.html', version=version, result=result[0], status=result[1])
    else:
        flash("You are not logged in")
        return redirect("/login")


@app.route("/alerts", methods=['POST', 'GET'])
def alerts():
    return render_template('alerts.html', version=version)


@app.route("/core_dashboard", methods=['POST', 'GET'])
def core_dashboard():
    return render_template('core_dashboard.html', version=version)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5555)
