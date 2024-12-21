-- Active: 1734460064563@@127.0.0.1@3306@hospital

create DATABASE hospital;
--drop DATABASE hospital;
use hospital;

create Table if not exists Departments(
	department_id int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	name varchar(50) not null,
	location varchar(100) not null,
	PRIMARY KEY(department_id)
);



create Table if not exists Doctors(
	doctor_id int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	doctor_name varchar(50) not null,
	department int(10) unsigned not null,  -- department_id
	specialization varchar(100) not null,
	phone varchar(50) not null,
	primary key(doctor_id),
	foreign key(department) REFERENCES Departments(department_id) ON DELETE RESTRICT ON UPDATE CASCADE
);	
--drop table doctors; -- not allowed by foreign key

create Table if not exists Patients(
	patient_id int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	patient_name varchar(50) not null,
	appointment_no int(10) unsigned not null,  -- appointment_id	
	date varchar(50) not null, --  also in Appointments table
	time varchar(50) not null, --  also in Appointments table		
	primary key(patient_id)
);


create Table if not exists Appointments(
	appointment_id int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	appointment_to int(10) unsigned not null,  -- doctor_id
	patient_id int(10) unsigned not null, -- patient_id
	date varchar(50) not null,
	time varchar(50) not null,	
	status varchar(50) not null,   -- pending/complete
	primary key(appointment_id),
	foreign key(appointment_to) REFERENCES Doctors(doctor_id) ON DELETE RESTRICT ON UPDATE CASCADE,
	foreign key(patient_id) REFERENCES Patients(patient_id) ON DELETE RESTRICT ON UPDATE CASCADE
);



insert into departments(name, location) VALUES
("Emergency", "floor 1"), -- 1
("Cardiology", "floor 2"),  -- 2
("Gynaecology", "floor 3"),  -- 3
("Hematology", "floor 4"),  -- 4
("Nephrology", "floor 5"),  -- 5
("Oncology", "floor 6"),  -- 6
("Orthopedics", "floor 7"); -- 7


insert into doctors(doctor_name, department, specialization, phone) VALUES
("Dr Amirul Islam", 1, "Heart, diabetis, medicuine", "0171"),
("Dr Lutfor Rahman", 2, "Chief Cardiac Surgeon", "0172"),
("Dr Sultana Sharmin", 3, "Surgery", "0193"),
("Dr Khademul Islam", 4, "Surgery", "0191"),
("Dr Abduz Zaher", 2, "Surgery", "0192"),
("Dr Md Sayedul Islam", 1, "Medicine, asthma, chest disease", "0161"); -- 6


insert into patients(patient_name, appointment_no, date, time) VALUES
("Kamal",1,"2024-12-17","10:00:00"), -- 1
("Raju",2,"2024-12-18","11:30:00"),
("Kibria",3,"2024-12-19","10:00:00"),
("M Sultan",4,"2024-12-20","09:00:00"),
("Habib",5,"2024-12-20","11:00:00"); -- 5



insert into appointments(appointment_to, patient_id, date, time, status) VALUES
(1, 1, "2025-01-20","10:00:00", "pending"), -- 1
(2, 1, "2025-01-20","11:00:00", "pending"),
(1, 2, "2025-01-21","10:30:00", "pending"),
(3, 3, "2025-01-21","11:45:00", "pending"),
(4, 4, "2025-01-22","10:50:00", "pending"),
(5, 5, "2025-01-22","11:20:00", "pending"); -- 6




/*
Create tables for Doctors, Patients, Appointments, and Departments with appropriate fields.
Departments: (DepartmentID, Name, and Location.)
Doctors: (DoctorID, Name, Specialization, Phone.)
Appointments (AppointmentID, Date, Time, Status.)
Patients: (PatientID, Name, Age, Gender, Phone.)

Draw an Entity Relationship Diagram (ERD) showing the relationships between tables, primary keys, and foreign keys. Submit a clear image of the diagram.

SQL Queries:
- Write SQL queries to create the above tables, including PRIMARY KEY and FOREIGN KEY constraints.
- Add at least 5 dummy records for each table.
*/
