DROP TABLE IF EXISTS bookings CASCADE;

CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,
    space_id INTEGER REFERENCES spaces(space_id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

INSERT INTO bookings (space_id, user_id, start_date, end_date) VALUES 
(1, 2, '2024-11-10', '2024-11-12'),
(2, 3, '2024-11-15', '2024-11-18'),
(3, 1, '2024-11-20', '2024-11-25');
