create table members (
	member_id serial primary key,
	first_name text not null,
	last_name text not null,
	email text not null unique,
    start_date date not null,
	weight int not null check (weight > 0),
	bodyfat_percent int not null check (0 < bodyfat_percent and bodyfat_percent <= 100),
	card_no char(9) unique,
	membership_cost decimal not null check (membership_cost > 0)
);

create table admins (
	admin_id serial primary key,
	first_name text not null,
	last_name text not null,
	email text not null unique
);

create table equipment (
	equipment_id serial primary key,
	equipment text not null,
	last_maintenance_date Date,
	days_per_maintenance int not null,
	needs_maintenance bool not null
);

create table goals (
	member_id int,
	foreign key (member_id)
		references members (member_id)
		on delete cascade,
	goal text not null,
	primary key (member_id, goal)
);

create table billing (
	member_id int,
	transaction_no serial primary key,
	foreign key (member_id)
		references members (member_id),
	cost decimal,
	card_no char(9),
    transaction_date date not null
);

create table trainers (
	trainer_id serial primary key,
	first_name text not null,
	last_name text not null,
	email text not null unique
);

create table personalSession(
	member_id int,
	trainer_id int,
	session_id serial primary key,
	foreign key (member_id)
		references members (member_id)
		on delete cascade,
	foreign key (trainer_id)
		references trainers (trainer_id)
		on delete cascade,
	session_date date not null,
	session_start time not null,
	session_end time not null,
    check(session_start < session_end)
);

create table groupClass(
	class_id serial primary key,
	class_date date not null,
	class_start time not null,
	class_end time not null
);

create table classList (
	member_id int not null,
	class_id int not null,
	foreign key (member_id)
		references members (member_id),
	foreign key (class_id)
		references groupClass (class_id)
		on delete cascade,
	primary key (member_id, class_id)
);

create table assignedClass (
	trainer_id int not null,
	class_id int not null,
	foreign key (trainer_id)
		references trainers (trainer_id)
		on delete cascade,
	foreign key (class_id)
		references groupClass (class_id)
		on delete cascade,
	primary key (trainer_id, class_id)
);

create table Room (
	room_no char(3) not null primary key
);

create table classRoom (
	room_no char(3) not null,
	class_id int not null,
	foreign key (class_id)
		references groupClass (class_id)
		on delete cascade,
	foreign key (room_no)
		references Room (room_no)
		on delete cascade,
	primary key (class_id)
);

create table trainerSchedule (
	trainer_id int not null,
	available date,
	start_time time,
	end_time time,
	foreign key (trainer_id)
		references trainers (trainer_id)
		on delete cascade,
	primary key (trainer_id, available)
);