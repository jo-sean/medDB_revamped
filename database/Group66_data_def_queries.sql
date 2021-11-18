-- **********************************************************************
-- Project Step 4 Draft Version: DML and DDL Queries (CS340)
-- Chris Mannina & Sean Perez (Group 66)
-- **********************************************************************
 
-- enter your database here to use
-- USE `cs340_perejos`;
 
-- DROP ALL TABLES IF THEY EXIST
DROP TABLE IF EXISTS `Purchase_Orders`;
DROP TABLE IF EXISTS `Pharmacy_Technicians`;
DROP TABLE IF EXISTS `Suppliers`;
DROP TABLE IF EXISTS `Prescriptions`;
DROP TABLE IF EXISTS `Patients`;
DROP TABLE IF EXISTS `Medications`;
 
-- ************** MEDICATIONS **************
 
-- Create table
 
CREATE TABLE `Medications` (
    `medication_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `drug_name` varchar(255) NOT NULL,
    `doseage_form` varchar(255) DEFAULT NULL,
    `dose_number` int(11) NOT NULL,
    `dose_unit` varchar(255) DEFAULT NULL,
    `quantity` int(11) NOT NULL
) ;
 
-- Insert sample data
LOCK TABLES `Medications` WRITE;
 
INSERT INTO `Medications` (`medication_id`, `drug_name`, `doseage_form`, `dose_number`, `dose_unit`, `quantity`)
VALUES (1,'metoprolol','tablet',25,'mg',180), (2,'glipizide','tablet',10,'mg',90);
 
UNLOCK TABLES;
 
 
-- ************** SUPPLIERS **************
 
-- Create table
 
CREATE TABLE `Suppliers` (
  `supplier_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `name` varchar(255) NOT NULL,
  `zip_code` int(11) NOT NULL,
  `phone` int(11) NULL
);
 
-- Insert sample data
LOCK TABLES `Suppliers` WRITE;
 
INSERT INTO `Suppliers` (`supplier_id`, `name`, `zip_code`, `phone`)
VALUES (1, 'McKesson', 75000, 18007939875);
 
UNLOCK TABLES;
 
-- ************** PATIENTS **************
 
-- Create table
 
CREATE TABLE `Patients` (
  `patient_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `phone` int(11) NOT NULL, 
  `street_number` int(11) NOT NULL,
  `street_name` varchar(255) DEFAULT NULL,
  `zip_code` int(11) NOT NULL
);
 
-- Insert sample data
LOCK TABLES `Patients` WRITE;
 
INSERT INTO `Patients` (`patient_id`, `first_name`, `last_name`, `phone`, `street_number`, `street_name`, `zip_code`)
VALUES (101,'Jonathan','Smith',1234567890,123,'Baker St',97003);
 
UNLOCK TABLES;
 
 
-- ************** PHARMACY TECHNICIANS **************
 
-- Create table
CREATE TABLE `Pharmacy_Technicians` (
  `employee_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL
);
 
-- Insert sample data
LOCK TABLES `Pharmacy_Technicians` WRITE;
 
INSERT INTO `Pharmacy_Technicians` (`employee_id`, `first_name`, `last_name`)
VALUES (99, 'Wayne', 'Gretzky');
 
UNLOCK TABLES;
 
-- ************** PRESCRIPTIONS **************
 
-- Create table
 
CREATE TABLE `Prescriptions` (
    `prescription_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `patient_id` int(11) NOT NULL,
    `medication_id` int(11) NOT NULL,
    `quantity` varchar(255) DEFAULT NULL,
    -- CONSTRAINT `fk_prescriptions_patient_id`
    FOREIGN KEY (`patient_id`) REFERENCES `Patients`(`patient_id`),
    -- ON DELETE CASCADE
    -- ON UPDATE CASCADE,
    -- CONSTRAINT `fk_prescriptions_medication_id`
    FOREIGN KEY (`medication_id`) REFERENCES `Medications`(`medication_id`)
    -- ON DELETE CASCADE
    -- ON UPDATE CASCADE
);
 
-- Insert sample data
LOCK TABLES `Prescriptions` WRITE;
 
INSERT INTO `Prescriptions` (`prescription_id`, `patient_id`, `medication_id`, `quantity`)
VALUES (11,101,1,90), (12,101,2,30);
 
UNLOCK TABLES;
 
 
-- ************** PURCHASE ORDER **************
 
-- Create table
 
CREATE TABLE `Purchase_Orders` (
    `purchase_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `supplier_id` int(11) NOT NULL,
    `employee_id` int(11) NOT NULL,
    `medication_id` int(11) NOT NULL,
    `quantity` int(11) NOT NULL,
    `unit_price` int(11) NOT NULL,
    `total_price` int(11) NOT NULL,
    `date` date NOT NULL,
    -- CONSTRAINT `fk_PO_supplier_id`
    FOREIGN KEY (`supplier_id`) REFERENCES `Suppliers`(`supplier_id`),
    -- ON DELETE CASCADE
    -- ON UPDATE CASCADE,
    -- CONSTRAINT `fk_PO_employee_id`
    FOREIGN KEY (`employee_id`) REFERENCES `Pharmacy_Technicians`(`employee_id`),
    -- ON DELETE CASCADE
    -- ON UPDATE CASCADE,
    -- CONSTRAINT `fk_PO_medication_id`
    FOREIGN KEY (`medication_id`) REFERENCES `Medications`(`medication_id`)
    -- ON DELETE CASCADE
    -- ON UPDATE CASCADE
);
 
-- Insert sample data
LOCK TABLES `Purchase_Orders` WRITE;
 
INSERT INTO `Purchase_Orders` (`purchase_id`, `supplier_id`, `employee_id`, `medication_id`, `quantity`, `unit_price`, `total_price`, `date`) 
VALUES (1001, 1, 99, 1, 270, 0.10, 27.00, 2021-09-31);
 
UNLOCK TABLES;
 
 
 


