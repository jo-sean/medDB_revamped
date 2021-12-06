-- **********************************************************************
-- Project Step 4 Draft Version: DML and DDL Queries (CS340)
-- Chris Mannina & Sean Perez (Group 66)
-- **********************************************************************
 
-- enter your database here to use
-- USE `cs340_perejos`;
 
DROP TABLE IF EXISTS `purchase_orders`;
DROP TABLE IF EXISTS `pharmacy_technicians`;
DROP TABLE IF EXISTS `suppliers`;
DROP TABLE IF EXISTS `prescriptions`;
DROP TABLE IF EXISTS `patients`;
DROP TABLE IF EXISTS `medications`;
 
-- ************** MEDICATIONS **************
 
-- Create table
 
CREATE TABLE `medications` (
    `medication_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `drug_name` varchar(255) NOT NULL,
    `dosage_form` varchar(255) DEFAULT NULL,
    `dose_number` int(11) NOT NULL,
    `dose_unit` varchar(255) DEFAULT NULL,
    `quantity` int(11) NOT NULL,
	UNIQUE (drug_name, dose_number)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
-- Insert sample data
LOCK TABLES `medications` WRITE;
 
INSERT INTO `medications` (`medication_id`, `drug_name`, `dosage_form`, `dose_number`, `dose_unit`, `quantity`)
VALUES (1,'metoprolol','tablet',25,'mg',180), (2,'glipizide','tablet',10,'mg',90), (3,'promethazine','suppository',25,'mg',10), (4, 'acetaminophen', 'capsule', 500, 'mg', 360);
 
UNLOCK TABLES;
 
 
-- ************** SUPPLIERS **************
 
-- Create table
 
CREATE TABLE `suppliers` (
  `supplier_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `name` varchar(255) NOT NULL,
  `zip_code` int(6) NOT NULL,
  `phone` bigint(11) NULL,
   UNIQUE (name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
-- Insert sample data
LOCK TABLES `suppliers` WRITE;
 
INSERT INTO `suppliers` (`supplier_id`, `name`, `zip_code`, `phone`)
VALUES (1, 'McKesson', 75000, 8007939875), (2, 'Cardinal Health', 43016, 6147575000), (3, 'AmerisourceBergen', 19428, 6107277000);
 
UNLOCK TABLES;
 
-- ************** PATIENTS **************
 
-- Create table
 
CREATE TABLE `patients` (
  `patient_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `phone` bigint(11) NOT NULL,
  `street_number` int(11) NOT NULL,
  `street_name` varchar(255) DEFAULT NULL,
  `zip_code` int(6) NOT NULL,
  UNIQUE (first_name, last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
-- Insert sample data
LOCK TABLES `patients` WRITE;
 
INSERT INTO `patients` (`patient_id`, `first_name`, `last_name`, `phone`, `street_number`, `street_name`, `zip_code`)
VALUES (87,'Sydney','Crosby',1234567890,101,'The Next One St',19734), (99,'Wayne','Gretzky',1234567899,99,'The Great One Blvd.',90210), (9,'Gordie','Howe',1234567809,1928,'Mr. Hockey Highway',48127);
 
UNLOCK TABLES;
 
 
-- ************** PHARMACY TECHNICIANS **************
 
-- Create table
CREATE TABLE `pharmacy_technicians` (
  `employee_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
   UNIQUE (first_name, last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
-- Insert sample data
LOCK TABLES `pharmacy_technicians` WRITE;
 
INSERT INTO `pharmacy_technicians` (`employee_id`, `first_name`, `last_name`)
VALUES (6, 'LeBron', 'Jones'), (33, 'Lawrence', 'Byrd'), (8, 'Kobe', 'Brian'), (23, 'Michelle', 'Jordan'), (30, 'Steven', 'Burry');
 
UNLOCK TABLES;
 
-- ************** PRESCRIPTIONS **************
 
-- Create table
 
CREATE TABLE `prescriptions` (
    `prescription_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `patient_id` int(11) NOT NULL,
    `medication_id` int(11) NOT NULL,
    `quantity` varchar(255) DEFAULT NULL,
    -- CONSTRAINT `fk_prescriptions_patient_id`
    FOREIGN KEY (`patient_id`) REFERENCES `patients`(`patient_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    -- CONSTRAINT `fk_prescriptions_medication_id`
    FOREIGN KEY (`medication_id`) REFERENCES `medications`(`medication_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
-- Insert sample data
LOCK TABLES `prescriptions` WRITE;
 
INSERT INTO `prescriptions` (`prescription_id`, `patient_id`, `medication_id`, `quantity`)
VALUES (1,87,4,30),(2,9,1,60),(3,9,2,30);
 
UNLOCK TABLES;
 
 
-- ************** PURCHASE ORDER **************

-- Create table
 
CREATE TABLE `purchase_orders` (
    `purchase_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `supplier_id` int(11) NOT NULL,
    `employee_id` int(11),
    `medication_id` int(11) NOT NULL,
    `quantity` int(11) NOT NULL,
    `unit_price` decimal(13,2) NOT NULL,
    `total_price` decimal(13,2) NOT NULL,
    `date_ordered` date NOT NULL,
    -- CONSTRAINT `fk_PO_supplier_id`
    FOREIGN KEY (`supplier_id`) REFERENCES `suppliers`(`supplier_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    -- CONSTRAINT `fk_PO_employee_id`
    FOREIGN KEY (`employee_id`) REFERENCES `pharmacy_technicians`(`employee_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    -- CONSTRAINT `fk_PO_medication_id`
    FOREIGN KEY (`medication_id`) REFERENCES `medications`(`medication_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
-- Insert sample data
LOCK TABLES `purchase_orders` WRITE;
 
INSERT INTO `purchase_orders` (`purchase_id`, `supplier_id`, `employee_id`, `medication_id`, `quantity`, `unit_price`, `total_price`, `date_ordered`)
VALUES (1, 2, 33, 1, 270, 0.10, 27.00, '2021-09-30'), (2, 1, 30, 1, 120, 0.05, 6.00, '2021-10-17'), (3, 3, 6, 3, 5, 1.25, 6.25, '2021-11-01');
 
UNLOCK TABLES;
