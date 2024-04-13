insert into members(first_name, last_name, email, start_date, weight, bodyfat_percent, card_no) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01', 225, 35, '123456789'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-01-01', 150, 22,'246728210'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-28',184, 15,'918762715');

insert into admins(first_name, last_name, email) VALUES
('James', 'Dean', 'james.dean@admin.com'),
('Amanda', 'Smith', 'amanda.smith@admin.com');

insert into equipment(equipment, last_maintenance_date, days_per_maintenance, needs_maintenance) VALUES
('Bench Press', '2024-02-01', 180, FALSE),
('Treadmill', '1992-08-22', 90, TRUE),
('Dumbbell', '2023-06-12', 365, FALSE);

insert into goals(member_id, goal) VALUES
(1, 'Lose 25 lbs'),
(2, 'Gain 20 lbs'),
(2, 'Reach 15 percent body fat'),
(3, 'Bench two plates');

insert into billing(member_id, cost, card_no, transaction_date) VALUES
(1, 29.99, '123456789', '2023-09-01'),
(1, 29.99, '123456789', '2023-09-15'),
(1, 29.99, '123456789', '2023-09-29'),
(2, 12.99, '246728210', '2023-01-15'),
(2, 29.99, '246728210', '2023-01-29'),
(3, 29.99, '918762715', '2023-10-10');

insert into trainers(first_name, last_name, email) VALUES
('Chad', 'Chad', 'chad.chad@trainer.com'),
('Stacie', 'Star', 'stacie.star@admin.com');

insert into personalSession(member_id, trainer_id, session_date, session_start,session_end) VALUES
(1,1,'2024-06-12', '09:00:00', '11:00:00'),
(2,1,'2024-07-2', '14:30:00', '15:45:00'),
(3,2,'2024-05-4', '12:00:00', '15:00:00');

insert into groupClass(class_date, class_start, class_end) VALUES
('2024-05-9', '12:00:00', '15:00:00'),
('2024-05-9', '09:00:00', '11:00:00'),
('2024-05-10', '06:00:00', '07:30:00');

insert into classList(member_id, class_id) VALUES
(1,1),
(2,1),
(3,1);

insert into assignedClass(trainer_id, class_id) VALUES
(1,1),
(2,2),
(2,3);

insert into classRoom(room_no, class_id) VALUES
(101,1),
(101,2),
(102,3);

insert into trainerPayroll(trainer_id, salary) VALUES
(1,75000),
(2,90000);

insert into adminPayroll(admin_id, salary) VALUES
(1,100000),
(2,80000);

insert into trainerSchedule(trainer_id, availible, start_time, end_time) VALUES
(1,'2024-05-02','09:00:00','17:00:00'),
(2,'2024-05-16','12:00:00','17:00:00'),
(2,'2024-06-16','8:00:00','16:00:00');