DROP TABLE IF EXISTS available_dates CASCADE;

CREATE TABLE available_dates (
    date_id SERIAL PRIMARY KEY,
    space_id INTEGER REFERENCES spaces(space_id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

INSERT INTO available_dates (space_id, user_id, start_date, end_date) VALUES 
(1, 2, '2024-10-10', '2024-12-12'),
(2, 3, '2024-11-13', '2024-11-20'),
(3, 1, '2024-11-01', '2024-12-25');