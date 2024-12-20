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


create Table if not exists Appointments(
	appointment_id int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	appointment_to int(10) unsigned not null,  -- doctor_id
	date varchar(50) not null,
	time varchar(50) not null,	
	status varchar(50) not null,   -- pending/complete
	primary key(appointment_id),
	foreign key(appointment_to) REFERENCES Doctors(doctor_id) ON DELETE RESTRICT ON UPDATE CASCADE
);


create Table if not exists Patients(
	patient_id int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	patient_name varchar(50) not null,
	appointment_no int(10) unsigned not null,  -- appointment_id
	/*
	--date varchar(50) not null, --  exits in Appointments table
	--time varchar(50) not null, --  exits in Appointments table	
	*/
	primary key(patient_id),
	foreign key(appointment_no) REFERENCES Appointments(appointment_id) ON DELETE RESTRICT ON UPDATE CASCADE
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


insert into appointments(appointment_to, date, time, status) VALUES
(1, "20-1-2025","10 am", "pending"),
(1, "21-1-2025","10 am", "pending"),
(2, "21-1-2025","11 am", "pending"),
(3, "21-1-2025","11:30 am", "pending"),
(4, "22-1-2025","10 am", "pending"),
(5, "22-1-2025","11 am", "pending"); -- 6


insert into patients(patient_name, appointment_no) VALUES
("Kamal",1),
("Raju",2),
("Kibria",3),
("M Sultan",4),
("Habib",5),
("Jakaria",6);

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