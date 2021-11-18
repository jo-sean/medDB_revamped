from flask import Flask, render_template, request, redirect, url_for, json
from flask_mysqldb import MySQL
import dbconfig

import os
from flask.helpers import url_for
from werkzeug.utils import redirect
# import database.db_connector as db

# Configuration
# Accessible ports: 1024 < PORT < 65535
Port = 8645  # designates what port to host on
###Change back to 0.0.0.0
hostingURL = '127.0.0.1'  # designates what url to host on

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

app.config['MYSQL_HOST'] = dbconfig.host
app.config['MYSQL_USER'] = dbconfig.user
app.config['MYSQL_PASSWORD'] = dbconfig.passwd
app.config['MYSQL_DB'] = dbconfig.db

mysql = MySQL(app)


# def get_clients():
#     """
#     :return: tuple of all client information in form (clientID, firstName, lastName, dietician, trainer)
#     """
#     cur = mysql.connection.cursor()
#     users = cur.execute("SELECT * FROM Clients")
#     # if users > 0:
#     clientDetails = cur.fetchall()
#     cur.close()
#     return clientDetails
#
#
# def get_trainers():
#     """
#     :return: tuple of all trainer information in form (empID, empFirstName, empLastName)
#     """
#     cur = mysql.connection.cursor()
#     trainer_tuples = cur.execute("SELECT * FROM Trainers")
#     trainer_tuples = cur.fetchall()
#     cur.close()
#     return trainer_tuples
#
#
# def get_dieticians():
#     """
#     :return: tuple of dietician information in form (rdID, rdFirstName, rdLastName, diabeticEd)
#     """
#     cur = mysql.connection.cursor()
#     dieticians = cur.execute("SELECT * FROM Dieticians")
#     dieticians = cur.fetchall()
#     cur.close()
#     return dieticians
#
#
# """
# Client Page
#
# Features:
#     Create Client
#     Display Clients
#     Remove Clients - work in progress
# """
#
#
# # remove client from client page
#
# # -----add remove client stuff here-----#
# @app.route('/remove_client', methods=['GET', 'POST'])
# def remove_client():
#     if request.method == "POST":
#         clientID = request.form['to_delete']
#         cur = mysql.connection.cursor()
#         cur.execute("DELETE FROM Clients WHERE clientID = %s", (clientID,))
#         mysql.connection.commit()
#         cur.close()
#     return redirect(url_for("displayClients"))
#
#
# # Filter clients by trainer
# @app.route("/filter_clients", methods=["GET", "POST"])
# def filterClients():
#     if request.method == "POST":
#         trainerID = request.form['trainers']
#
#         # Filter clients by trainerID
#         cur = mysql.connection.cursor()
#         trainer_clients = cur.execute("SELECT firstName, lastName FROM Clients WHERE trainer = %s", (trainerID,))
#         trainer_clients = cur.fetchall()
#         cur.close()
#
#         # get trainer name from trainerID (there's gotta be an easier way to do this)
#         cur = mysql.connection.cursor()
#         trainer_name = cur.execute("SELECT empFirstName, empLastName FROM Trainers WHERE empID = %s", (trainerID,))
#         trainer_name = cur.fetchone()
#         cur.close()
#
#     return render_template("clients_by_trainer.html", trainer_clients=trainer_clients, trainer_name=trainer_name)
#
#
# # display clients on client page
# @app.route('/')
# def displayClients():
#     # get list of clients
#     clientDetails = get_clients()
#
#     # get list of trainers
#     trainers = get_trainers()
#
#     # get list of dieticians
#     dieticians = get_dieticians()
#
#     return render_template('clients.html', clientDetails=clientDetails, trainers=trainers, dieticians=dieticians)
#
#
# # create client on client page
# @app.route('/', methods=['GET', 'POST'])
# def createClient():
#     if request.method == 'POST':
#         lastName = request.form['lastName']
#         firstName = request.form['firstName']
#         trainer = request.form['trainer_list']
#         dietician = request.form['dietician_list']
#
#         cur = mysql.connection.cursor()
#         cur.execute("SET FOREIGN_KEY_CHECKS=0")
#         if dietician == "NULL":
#             cur.execute("INSERT INTO Clients(lastName, firstName, trainer, dietician) VALUES(%s, %s, %s, NULL)",
#                         (lastName, firstName, trainer))
#         else:
#             cur.execute("INSERT INTO Clients(lastName, firstName, trainer, dietician) VALUES(%s, %s, %s, %s)",
#                         (lastName, firstName, trainer, dietician))
#         cur.execute("SET FOREIGN_KEY_CHECKS=1")
#         mysql.connection.commit()
#
#         cur.close()
#
#     return redirect(url_for("displayClients"))
#
#
# """
# Trainer Page
#
# Features:
#     Create Trainer
#     Display Trainer
#     Remove Trainer - work in progress
# """
#
#
# # remove trainers from trainers page
#
# # -----add remove trainers stuff here-----#
# @app.route('/remove_trainer', methods=["GET", "POST"])
# def removeTrainer():
#     if request.method == "POST":
#         trainerID = request.form['to_delete']
#         cur = mysql.connection.cursor()
#         cur.execute("DELETE FROM Trainers WHERE empID = %s", (trainerID,))
#         mysql.connection.commit()
#         cur.close()
#     return redirect(url_for("displayTrainers"))
#
#
# # display trainers on trainers page
# @app.route('/trainers.html')
# def displayTrainers():
#     cur = mysql.connection.cursor()
#
#     users = cur.execute("SELECT * FROM Trainers")
#
#     # if trainers > 0:
#     trainerDetails = cur.fetchall()
#
#     cur.close()
#
#     return render_template('trainers.html', trainerDetails=trainerDetails)
#
#
# # create trainer on trainers page
# @app.route('/trainers.html', methods=['GET', 'POST'])
# def createTrainer():
#     if request.method == 'POST':
#         empLastName = request.form['empLastName']
#         empFirstName = request.form['empFirstName']
#
#         cur = mysql.connection.cursor()
#
#         cur.execute("INSERT INTO Trainers (empLastName, empFirstName) VALUES(%s, %s)", (empLastName, empFirstName))
#
#         mysql.connection.commit()
#
#         cur.close()
#
#     return displayTrainers()
#
#
# """
# Dietician Page
#
# Features:
#     Create Dietician
#     Display Dietician
#     Remove Dietician - work in progress
# """
#
#
# # remove Dieticians from Dieticians page
#
# # -----add remove Dieticians stuff here-----#
#
#
# # display Dieticians on Dieticians page
# @app.route('/dieticians.html')
# def displayDieticians():
#     cur = mysql.connection.cursor()
#
#     users = cur.execute("SELECT * FROM Dieticians")
#
#     # if Dieticians > 0:
#     dieticianDetails = cur.fetchall()
#
#     cur.close()
#
#     return render_template('dieticians.html', dieticianDetails=dieticianDetails)
#
#
# # create Dietician on Dieticians page
# @app.route('/dieticians.html', methods=['GET', 'POST'])
# def createDietician():
#     if request.method == 'POST':
#         rdLastName = request.form['rdLastName']
#         rdFirstName = request.form['rdFirstName']
#         diabeticEd = request.form['diabeticEd']
#
#         cur = mysql.connection.cursor()
#
#         cur.execute("INSERT INTO Dieticians (rdLastName, rdFirstName, diabeticEd) VALUES(%s, %s, %s)",
#                     (rdLastName, rdFirstName, diabeticEd))
#
#         mysql.connection.commit()
#
#         cur.close()
#
#     return displayDieticians()
#
#
# """
# Exercise Page
#
# Features:
#     Create Exercise
#     Display Exercise
#     Remove Exercise - work in progress
# """
#
#
# # remove Exercises from Exercises page
#
# # -----add remove Exercises stuff here-----#
#
#
# # display Exercises on Exercises page
# @app.route('/exercise-library.html')
# def displayExercises():
#     cur = mysql.connection.cursor()
#
#     users = cur.execute("SELECT * FROM Exercise")
#
#     # if Exercises > 0:
#     exerciseDetails = cur.fetchall()
#
#     cur.close()
#
#     return render_template('exercise-library.html', exerciseDetails=exerciseDetails)
#
#
# # create Exercise on Exercises page
# @app.route('/exercise-library.html', methods=['GET', 'POST'])
# def createExercise():
#     if request.method == 'POST':
#         exName = request.form['exName']
#         primaryMover = request.form['primaryMover']
#         secondaryMover = request.form['secondaryMover']
#         weights = request.form['weights']
#
#         cur = mysql.connection.cursor()
#
#         cur.execute("INSERT INTO Exercise(exName, primaryMover, secondaryMover, weights) VALUES(%s, %s, %s, %s)",
#                     (exName, primaryMover, secondaryMover, weights))
#
#         mysql.connection.commit()
#
#         cur.close()
#
#     return displayExercises()


#
# Static page generation
#

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/medications.html')
def medications():
    # return createClient()
    return render_template('medications.html')


@app.route('/prescriptions.html')
def prescriptions():
    # return createDietician()
    return render_template('prescriptions.html')


@app.route('/orders.html')
def purchase_orders():
    # return createExercise()
    return render_template('orders.html')


@app.route('/suppliers.html')
def suppliers():
    # return createTrainer()
    return render_template('suppliers.html')


@app.route('/patients.html')
def patients():
    return render_template('patients.html')


@app.route('/techs.html')
def pharmacy_technicians():
    return render_template('techs.html')


if __name__ == "__main__":
    app.run(host=hostingURL, port=Port, debug=True)
