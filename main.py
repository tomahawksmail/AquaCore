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
            name = request.form["user"]
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
                getpass = result["UserPassword"]
                getrole = result["Role"]
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






@app.route("/aquarium", methods=['POST', 'GET'])
def dashboard():
    # insert()
    if 'user' in session:
        if request.method == 'GET':
            connection.connect()
            SQLrequest = """SELECT DATETIME, temp, ph, tds FROM `data`"""
            try:
                with connection.cursor() as cursor:
                    cursor.execute(SQLrequest)
                result = cursor.fetchall()
                print(result)
            except Exception as E:
                return render_template('aquarium.html', version=version)


            return render_template('aquarium.html', version=version, result=result)
        else:
            return render_template('aquarium.html', version=version, result=None)
    else:
        flash("You are not logged in")
        return redirect("/login")

def insert():
    import random
    connection.connect()
    for i in range(24):
        temp = random.randint(25, 35)
        ph   = round(random.uniform(4, 8))
        tds  = random.randint(200, 800)
        dttemp = "'" + str(datetime.strptime(f"2023-10-27 {i}:00:00", '%Y-%m-%d %H:%M:%S')) + "'"

        sql = f"""INSERT INTO data (datetime, temp, ph, tds) VALUES ({dttemp}, {temp}, {ph}, {tds})"""
        # print(sql)

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)

        except Exception as E:
            print(E)
        connection.commit()





if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0', port=5555)
