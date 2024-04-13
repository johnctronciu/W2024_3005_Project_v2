insert into members(first_name, last_name, email, start_date, weight, bodyfat_percent) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01', 225, 35),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01', 150, 22),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02',184, 15);

insert into admins(first_name, last_name, email) VALUES
('James', 'Dean', 'james.dean@admin.com'),
('Amanda', 'Smith', 'amanda.smith@admin.com');

insert into equipment(equipment, last_maintenance_date, days_per_maintenance, needs_maintenance) VALUES
('Bench Press', '2024-02-01', 180, FALSE),
('Treadmill', '1992-08-22', 90, TRUE),
('Dumbbell', '2023-06-12', 365, FALSE);

insert into goals(member_id, goal) VALUES
(1, "Lose 25 lbs")
(2, "Gain 20 lbs")
(2, "Reach 15 percent body fat"),
(3, "Bench two plates");

insert into Billing(member_id, cost, card_no) VALUES
(1, 29.99, '123456789'),