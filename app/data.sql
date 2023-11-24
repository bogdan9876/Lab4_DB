INSERT INTO HotelChain (name) VALUES
('Marriott'),
('Hilton'),
('Hyatt'),
('InterContinental'),
('Radisson'),
('Accor'),
('Four Seasons'),
('Shangri-La'),
('Mandarin Oriental'),
('The Ritz-Carlton');

INSERT INTO Hotel (name, address, contact_info, rating, HotelChain_id) VALUES
('Marriott Marquis', 'New York, USA', '1234567890', 4.5, 1),
('Hilton Times Square', 'New York, USA', '0987654321', 4.3, 2),
('Hyatt Regency', 'Chicago, USA', '1122334455', 4.2, 3),
('InterContinental London', 'London, UK', '2233445566', 4.6, 4),
('Radisson Blu Aqua Hotel', 'Chicago, USA', '3344556677', 4.1, 5),
('Accor Sydney', 'Sydney, Australia', '4455667788', 4.4, 6),
('Four Seasons Hotel Sydney', 'Sydney, Australia', '5566778899', 4.7, 7),
('Shangri-La Hotel Paris', 'Paris, France', '6677889900', 4.8, 8),
('Mandarin Oriental Barcelona', 'Barcelona, Spain', '7788990011', 4.9, 9),
('The Ritz-Carlton Berlin', 'Berlin, Germany', '8899001122', 4.0, 10);

INSERT INTO HotelLocation (country, city, Hotel_id) VALUES
('USA', 'New York', 1),
('USA', 'New York', 2),
('USA', 'Chicago', 3),
('UK', 'London', 4),
('USA', 'Chicago', 5),
('Australia', 'Sydney', 6),
('Australia', 'Sydney', 7),
('France', 'Paris', 8),
('Spain', 'Barcelona', 9),
('Germany', 'Berlin', 10);

INSERT INTO User (name, email, password, role) VALUES
('John Doe', 'john.doe@example.com', 'password1', 'client'),
('Jane Doe', 'jane.doe@example.com', 'password2', 'client'),
('Admin User', 'admin@example.com', 'adminpass', 'administrator'),
('Alice Smith', 'alice.smith@example.com', 'password3', 'client'),
('Bob Johnson', 'bob.johnson@example.com', 'password4', 'client'),
('Eve White', 'eve.white@example.com', 'password5', 'client'),
('Charlie Brown', 'charlie.brown@example.com', 'password6', 'client'),
('David Lee', 'david.lee@example.com', 'password7', 'client'),
('Grace Wilson', 'grace.wilson@example.com', 'password8', 'client'),
('Harry Davis', 'harry.davis@example.com', 'password9', 'client');

INSERT INTO Review (review_text, rating, User_id, Hotel_id) VALUES
('Great hotel!', 4.5, 1, 1),
('Excellent service.', 4.7, 2, 2),
('Wonderful experience!', 4.9, 4, 3),
('Perfect location.', 4.6, 3, 4),
('Highly recommended.', 4.8, 5, 5),
('Lovely staff.', 4.4, 6, 6),
('Clean and comfortable.', 4.3, 7, 7),
('Amazing views.', 4.5, 8, 8),
('Friendly atmosphere.', 4.2, 9, 9),
('Top-notch service.', 4.7, 10, 10);

INSERT INTO Room (room_type, price_per_night, Hotel_id) VALUES
('Deluxe Room', 200.00, 1),
('Standard Room', 150.00, 2),
('Suite', 250.00, 3),
('Superior Room', 180.00, 4),
('Penthouse Suite', 400.00, 5),
('Executive Room', 220.00, 6),
('Family Room', 170.00, 7),
('Ocean View Room', 280.00, 8),
('Studio', 210.00, 9),
('Double Room', 160.00, 10);

INSERT INTO Availability (booking_start_date, booking_start_end, Room_id) VALUES
('2023-11-01', '2023-11-30', 1),
('2023-12-01', '2023-12-31', 2),
('2023-11-01', '2023-11-30', 3),
('2023-12-01', '2023-12-31', 4),
('2023-11-01', '2023-11-30', 5),
('2023-12-01', '2023-12-31', 6),
('2023-11-01', '2023-11-30', 7),
('2023-12-01', '2023-12-31', 8),
('2023-11-01', '2023-11-30', 9),
('2023-12-01', '2023-12-31', 10);

INSERT INTO RegistrationConfirmation (send_date, status, User_id) VALUES
('2023-10-23', 'confirmed', 1),
('2023-10-23', 'pending', 2),
('2023-10-24', 'confirmed', 3),
('2023-10-24', 'confirmed', 4),
('2023-10-25', 'confirmed', 5),
('2023-10-25', 'pending', 6),
('2023-10-26', 'confirmed', 7),
('2023-10-26', 'confirmed', 8),
('2023-10-27', 'confirmed', 9),
('2023-10-27', 'confirmed', 10);

INSERT INTO FundBlock (block_amount, block_date, User_id, RegistrationConfirmation_id) VALUES
(200.00, '2023-10-23', 1, 1),
(150.00, '2023-10-23', 2, 2),
(220.00, '2023-10-24', 3, 3),
(180.00, '2023-10-24', 4, 4),
(280.00, '2023-10-25', 5, 5),
(170.00, '2023-10-25', 6, 6),
(240.00, '2023-10-26', 7, 7),
(200.00, '2023-10-26', 8, 8),
(260.00, '2023-10-27', 9, 9),
(210.00, '2023-10-27', 10, 10);

INSERT INTO Reservation (start_date, end_date, status, User_id, Room_id, FundBlock_id) VALUES
('2023-11-01', '2023-11-30', 'confirmed', 1, 1, 1),
('2023-12-01', '2023-12-31', 'pending', 2, 2, 2),
('2023-11-01', '2023-11-30', 'confirmed', 3, 3, 3),
('2023-12-01', '2023-12-31', 'confirmed', 4, 4, 4),
('2023-11-01', '2023-11-30', 'pending', 5, 5, 5),
('2023-12-01', '2023-12-31', 'confirmed', 6, 6, 6),
('2023-11-01', '2023-11-30', 'confirmed', 7, 7, 7),
('2023-12-01', '2023-12-31', 'confirmed', 8, 8, 8),
('2023-11-01', '2023-11-30', 'confirmed', 9, 9, 9),
('2023-12-01', '2023-12-31', 'confirmed', 10, 10, 10);
