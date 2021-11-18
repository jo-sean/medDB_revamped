
-- ************** MEDICATIONS **************
 
-- get all tuples and order by drug name -> shown on medications page
SELECT * FROM medications
ORDER BY drug_name;
 
-- add a new medication
INSERT INTO medications (drug_name, dosage_form, dose_number, dose_unit, quantity)
VALUES (:medName, :medForm, :medDose, :medUnit, :medQuantity);
 
-- edit existing medication entry
UPDATE medications
SET quantity = :quantityInput
WHERE medication_id = :medIdInput;


-- delete medication
DELETE FROM medications WHERE medication_id = :medIDSelected;

-- search for medication
SELECT * FROM medications
WHERE drug_name = :medName;


-- ************** PRESCRIPTIONS**************

-- get all tuples 
SELECT * FROM prescriptions;

-- add a new prescription
INSERT INTO prescriptions (patient_id, medication_id, quantity)
VALUES (:setPatientId, :setMedId, :setQuantity);


-- ************** PURCHASE ORDERS**************

-- get all tuples
SELECT * FROM purchase_orders;

-- add a new purchase_orders
INSERT INTO purchase_orders (supplier_id, employee_id, medication_id, quantity, unit_price, total_price,  date)
VALUES (:setSupplierId, :setEmployeeId, :setMedId, :setQuantity, :setUnitPrice, :setQuantity*:setUnitPrice, :setDate);



-- ************** SUPPLIERS**************

-- get all tuples and order by supplier_id-> shown on suppliers page
SELECT * FROM suppliers
ORDER BY name;

-- add a new supplier
INSERT INTO suppliers(name, zip_code, phone)
VALUES (:supName, :supZip, :supPhone);


--DELETE Suppliers
DELETE FROM suppliers WHERE supplier_id= :supplierIDSelected;




-- ************** PATIENTS**************

-- get all tuples and order by patient_id-> shown on patients page
SELECT * FROM patients
ORDER BY last_name;

-- add a new patient
INSERT INTO patients(first_name, last_name, phone, street_number, street_name, zip_code)
VALUES (:patFName, :patLName, :patPhone, :patStreetNum, :patStreetName, :patZip);

-- edit patient
UPDATE patients Set 
    phone= :phoneInput,
    street_number= :streetNumInput,
    street_name= :streetNameInput;

-- delete patient
DELETE FROM patients WHERE patient_id= :patientIDSelected;


-- ************** PHARMACY TECHNICIANS**************

-- get all tuples and order by employee_id-> shown on pharmacy technicians page
SELECT * FROM pharmacy_technicians
ORDER BY employee_id;

-- add a new pharmacy technician
INSERT INTO pharmacy_technicians(first_name, last_name)
VALUES (:techFName, :techLNname);

--DELETE pharmacy technicians
DELETE FROM pharmacy_technicians WHERE employee_id= :employeeIDSelected;

