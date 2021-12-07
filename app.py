from flask import Flask, render_template, request, redirect, url_for, flash
import os
import database.db_connector as db

# from flask.helpers import url_for
# from werkzeug.utils import redirect

# ************************* CONFIGURATION *************************
app = Flask(__name__)
app.secret_key = "SUPER_SECRET_KEY"

# Connect to database when server is started
db_connection = db.connect_to_database()
db_connection.ping(True)


# db_connection(True)

# ************************* ROUTING *************************
@app.route('/')
def root():
    """
    Serves: index.html page
    """
    return render_template("index.html")


@app.route('/medications', methods=['GET', 'POST'])
def medications():
    """
    Serves: medications.html page
    """

    # GET requests -> fetching all medications data
    if request.method == 'GET':
        query = "SELECT * FROM `medications` ORDER BY `drug_name`;"
        med_info = db.execute_query(db_connection, query).fetchall()
        return render_template('medications.html', med_info=med_info)

    # POST requests
    if request.method == 'POST':
        # delete
        if 'delete' in request.form.keys():
            medication_id = request.form['delete']
            query = "DELETE FROM medications WHERE medication_id = '%s';" % medication_id
            db.execute_query(db_connection=db_connection, query=query)
        # insert
        else:
            drug_name = request.form['drug_name']
            dosage_form = request.form['dosage_form']
            dose_number = request.form['dose_number']
            dose_unit = request.form['dose_unit']
            quantity = request.form['quantity']

            # Define query and data
            query = "INSERT INTO `medications` (`drug_name`, `dosage_form`, `dose_number`, `dose_unit`, `quantity`) VALUES (%s, %s, %s, %s, %s);"
            data = (drug_name, dosage_form, dose_number, dose_unit, quantity)

            print(query)

            # Insert
            try:
                db.execute_query(db_connection, query, data)
            except:
                flash("Error: duplicate entry")
                return redirect(url_for('medications'))

        # After form submission -> reload same page
        return redirect(url_for('medications'))


@app.route('/medication-search', methods=['POST', 'GET'])
def search_medications():
    """Serves: medication-search.html"""
    medications = request.form['search']

    query = "SELECT * FROM medications WHERE drug_name = '%s' ORDER BY drug_name;" % (medications)
    cursor = db.execute_query(db_connection, query)

    # Display the department search results
    med_search = cursor.fetchall()

    return render_template("medication-search.html", med_search=med_search)


@app.route('/suppliers', methods=['GET', 'POST'])
def suppliers():
    """
    Serves: suppliers.html page
    """

    # GET requests -> fetching all suppliers data
    if request.method == 'GET':
        query = "SELECT * FROM `suppliers` ORDER BY `supplier_id`;"
        supplier_info = db.execute_query(db_connection, query).fetchall()
        return render_template('suppliers.html', supplier_info=supplier_info)

    # POST requests -> insert form data
    if request.method == 'POST':
        # delete
        if 'delete' in request.form.keys():
            supplier_id = request.form['delete']
            query = "DELETE FROM suppliers WHERE supplier_id = '%s';" % supplier_id
            db.execute_query(db_connection=db_connection, query=query)
        # insert
        else:
            name = request.form['name']
            zip_code = request.form['zip_code']
            phone = request.form['phone']

            # Define query and data
            query = "INSERT INTO `suppliers` (`name`, `zip_code`, `phone`) VALUES (%s, %s, %s);"
            data = (name, zip_code, phone)

            # Insert
            try:
                db.execute_query(db_connection, query, data)
            except:
                flash("Error: duplicate entry")
                return redirect(url_for('suppliers'))

        # After form submission -> reload same page
        return redirect(url_for('suppliers'))


@app.route('/patients', methods=['GET', 'POST'])
def patients():
    """
    Serves: patients.html page
    """

    # GET requests -> fetching all patients data
    if request.method == 'GET':
        query = "SELECT * FROM `patients` ORDER BY `last_name`;"
        pt_info = db.execute_query(db_connection, query).fetchall()
        return render_template('patients.html', pt_info=pt_info)

    # POST requests -> insert form data
    if request.method == 'POST':
        # delete
        if 'delete' in request.form.keys():
            patient_id = request.form['delete']
            query = "DELETE FROM patients WHERE patient_id = '%s';" % patient_id
            db.execute_query(db_connection=db_connection, query=query)
        # insert
        else:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            phone = request.form['phone']
            street_number = request.form['street_number']
            street_name = request.form['street_name']
            zip_code = request.form['zip_code']

            # Define query and data
            query = "INSERT INTO `patients`(`first_name`, `last_name`, `phone`, `street_number`, `street_name`, `zip_code`) VALUES (%s, %s, %s, %s, %s, %s);"
            data = (first_name, last_name, phone, street_number, street_name, zip_code)

            # Insert
            try:
                db.execute_query(db_connection, query, data)
            except:
                flash("Error: duplicate entry")
                return redirect(url_for('patients'))

        # After form submission -> reload same page
        return redirect(url_for('patients'))


@app.route('/techs', methods=['GET', 'POST'])
def techs():
    """
    Serves: techs.html page
    """

    # GET requests -> fetching all pharmacy technician data
    if request.method == 'GET':
        query = "SELECT * FROM `pharmacy_technicians`;"
        tech_info = db.execute_query(db_connection, query).fetchall()
        return render_template("techs.html", tech_info=tech_info)

    # POST requests -> insert form data
    if request.method == 'POST':
        # delete
        if 'delete' in request.form.keys():
            employee_id = request.form['delete']
            query = "DELETE FROM pharmacy_technicians WHERE employee_id = '%s';" % employee_id
            db.execute_query(db_connection=db_connection, query=query)
        # insert
        else:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            query = "INSERT INTO `pharmacy_technicians` (`first_name`,`last_name`) VALUES (%s, %s);"
            data = (first_name, last_name)

            # Execute query to insert data
            try:
                db.execute_query(db_connection, query, data)
            except:
                flash("Error: duplicate entry")
                return redirect(url_for('techs'))

        # Redirect to same webpage after form submission
        return redirect(url_for('techs'))


@app.route('/prescriptions', methods=['GET', 'POST'])
def prescriptions():
    """
    Serves: prescriptions.html page
    """

    # GET requests -> fetching all prescriptions data
    if request.method == 'GET':
        query = "SELECT * FROM `prescriptions`;"
        prescription_info = db.execute_query(db_connection, query).fetchall()

        # Fetch all patient ids for drop down
        query2 = "SELECT patient_id, first_name, last_name FROM patients;"
        patients_info = db.execute_query(db_connection, query2)

        # Fetch all medication ids for drop down
        query3 = "SELECT medication_id, drug_name FROM medications;"
        medications_info = db.execute_query(db_connection, query3)

        return render_template("prescriptions.html", prescription_info=prescription_info, patients_info=patients_info,
                               medications_info=medications_info)

    # POST requests -> insert form data
    if request.method == 'POST':
        # delete
        if 'delete' in request.form.keys():
            prescription_id = request.form['delete']
            query = "DELETE FROM prescriptions WHERE prescription_id = '%s';" % prescription_id
            db.execute_query(db_connection=db_connection, query=query)
        # insert
        else:
            patient_id = request.form['patient_id']
            medication_id = request.form['medication_id']
            quantity = request.form['quantity']
            query = "INSERT INTO `prescriptions` (`patient_id`,`medication_id`, `quantity`) VALUES (%s, %s, %s);" % (patient_id, medication_id, quantity)

            # Execute query to insert data
            try:
                db.execute_query(db_connection, query)
            except:
                flash("Error: duplicate entry")
                return redirect(url_for('prescriptions'))

        # Redirect to same webpage after form submission
        return redirect(url_for('prescriptions'))


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    """
    Serves: orders.html page
    """

    # GET requests -> fetching all purchase orders data
    if request.method == 'GET':
        query = "SELECT * FROM `purchase_orders`;"
        order_info = db.execute_query(db_connection, query).fetchall()

        # Fetch all patient ids for drop down
        query2 = "SELECT supplier_id, name FROM suppliers;"
        supplier_info = db.execute_query(db_connection, query2)

        # Fetch all medication ids for drop down
        query3 = "SELECT employee_id, first_name, last_name FROM pharmacy_technicians;"
        employee_info = db.execute_query(db_connection, query3)

        # Fetch all medication ids for drop down
        query4 = "SELECT medication_id, drug_name FROM medications;"
        medications_info = db.execute_query(db_connection, query4)

        return render_template('orders.html', order_info=order_info, supplier_info=supplier_info,
                               employee_info=employee_info, medications_info=medications_info)

    # POST requests -> insert form data
    if request.method == 'POST':
        # delete
        if 'delete' in request.form.keys():
            purchase_id = request.form['delete']
            query = "DELETE FROM purchase_orders WHERE purchase_id = '%s';" % purchase_id
            db.execute_query(db_connection=db_connection, query=query)
        # insert
        else:
            supplier_id = request.form['supplier_id']
            employee_id = request.form['employee_id']
            medication_id = request.form['medication_id']
            quantity = request.form['quantity']
            unit_price = request.form['unit_price']
            total_price = str(float(unit_price) * int(quantity))
            date_ordered = request.form['date_ordered']

            if len(employee_id) == 0:
                employee_id = 'NULL'

            # Define query and data
            query = "INSERT INTO `purchase_orders` (`supplier_id`, `employee_id`, `medication_id`, `quantity`, " \
                    "`unit_price`, `total_price`, `date_ordered`) VALUES (%s, %s, %s, %s, %s, %s, '%s');" % (
                supplier_id, employee_id, medication_id, quantity, unit_price, total_price, date_ordered)

            # print(query)

            # Insert
            db.execute_query(db_connection, query)

        # After form submission -> reload same page
        return redirect(url_for('orders'))


# UPDATE
@app.route('/update-medication', methods=['GET', 'POST'])
def update_medication():
    # Bring up new page with data auto-populated
    if request.method == 'GET':
        medication_id = request.args.get("medication_id")
        query = "SELECT * FROM `medications` WHERE `medication_id` = '%s';" % medication_id
        cursor = db.execute_query(db_connection, query)
        med = cursor.fetchone()  # fetchone vs fetchall?
        return render_template('update-medication.html', med=med)
    # Submit updates
    if request.method == 'POST':
        medication_id = request.form['medication_id']
        drug_name = request.form['drug_name']
        dosage_form = request.form['dosage_form']
        dose_number = request.form['dose_number']
        dose_unit = request.form['dose_unit']
        quantity = request.form['quantity']

        query1 = "UPDATE medications SET drug_name = '%s', dosage_form = '%s', dose_number = '%s', dose_unit = '%s', quantity = '%s' WHERE medication_id = '%s';" % (
            drug_name, dosage_form, dose_number, dose_unit, quantity, medication_id)

        try:
            db.execute_query(db_connection, query1)
        except:
            flash("Error: duplicate entry")
            query = "SELECT * FROM `medications` WHERE `medication_id` = '%s';" % medication_id
            cursor = db.execute_query(db_connection, query)
            med = cursor.fetchone()
            return render_template('update-medication.html', med=med)

        # Fetch all
        query2 = "SELECT * FROM medications;"
        med_info = db.execute_query(db_connection, query2).fetchall()
        return render_template('medications.html', med_info=med_info)


@app.route('/update-tech', methods=['GET', 'POST'])
def update_tech():
    # Bring up new page with data auto-populated
    if request.method == 'GET':
        employee_id = request.args.get("employee_id")
        query = "SELECT * FROM `pharmacy_technicians` WHERE `employee_id` = '%s';" % employee_id
        cursor = db.execute_query(db_connection, query)
        tech = cursor.fetchone()
        return render_template('update-tech.html', tech=tech)
    # Submit updates
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        query1 = "UPDATE pharmacy_technicians SET first_name = '%s', last_name = '%s' WHERE employee_id = '%s';" % (
            first_name, last_name, employee_id)

        try:
            db.execute_query(db_connection, query1)
        except:
            flash("Error: duplicate entry")
            query = "SELECT * FROM `pharmacy_technicians` WHERE `employee_id` = '%s';" % employee_id
            cursor = db.execute_query(db_connection, query)
            tech = cursor.fetchone()
            # print(query)
            return render_template('update-tech.html', tech=tech)



        # Fetch all
        query2 = "SELECT * FROM pharmacy_technicians;"
        tech_info = db.execute_query(db_connection, query2).fetchall()
        return render_template('techs.html', tech_info=tech_info)


@app.route('/update-supplier', methods=['GET', 'POST'])
def update_supplier():
    # Bring up new page with data auto-populated
    if request.method == 'GET':
        supplier_id = request.args.get("supplier_id")
        query = "SELECT * FROM `suppliers` WHERE `supplier_id` = '%s';" % supplier_id
        cursor = db.execute_query(db_connection, query)
        supply = cursor.fetchone()
        return render_template('update-supplier.html', supply=supply)
    # Submit updates
    if request.method == 'POST':
        supplier_id = request.form['supplier_id']
        name = request.form['name']
        zip_code = request.form['zip_code']
        phone = request.form['phone']

        query1 = "UPDATE suppliers SET name = '%s', zip_code = '%s', phone = '%s' WHERE supplier_id = '%s';" % (
            name, zip_code, phone, supplier_id)

        try:
            db.execute_query(db_connection, query1)
        except:
            flash("Error: duplicate entry")
            query = "SELECT * FROM `suppliers` WHERE `supplier_id` = '%s';" % supplier_id
            cursor = db.execute_query(db_connection, query)
            supply = cursor.fetchone()
            return render_template('update-supplier.html', supply=supply)

        # Fetch all
        query2 = "SELECT * FROM suppliers;"
        supplier_info = db.execute_query(db_connection, query2).fetchall()
        return render_template('suppliers.html', supplier_info=supplier_info)


@app.route('/update-patient', methods=['GET', 'POST'])
def update_patient():
    # Bring up new page with data auto-populated
    if request.method == 'GET':
        patient_id = request.args.get("patient_id")
        query = "SELECT * FROM `patients` WHERE `patient_id` = '%s';" % patient_id
        cursor = db.execute_query(db_connection, query)
        patient = cursor.fetchone()
        return render_template('update-patient.html', patient=patient)

    # Submit updates
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        street_number = request.form['street_number']
        street_name = request.form['street_name']
        zip_code = request.form['zip_code']

        query1 = "UPDATE patients SET first_name = '%s', last_name = '%s', phone = '%s', street_number = '%s', street_name = '%s', zip_code = '%s' WHERE patient_id = '%s';" % (first_name, last_name, phone, street_number, street_name, zip_code, patient_id)

        try:
            db.execute_query(db_connection, query1)
        except:
            flash("Error: duplicate entry")
            query = "SELECT * FROM `patients` WHERE `patient_id` = '%s';" % patient_id
            cursor = db.execute_query(db_connection, query)
            patient = cursor.fetchone()
            return render_template('update-patient.html', patient=patient)

        # Fetch all
        query2 = "SELECT * FROM patients;"
        pt_info = db.execute_query(db_connection, query2).fetchall()
        return render_template('patients.html', pt_info=pt_info)


# ************************* LISTENER *************************
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 7888))
    app.run(port=port, debug=True)
