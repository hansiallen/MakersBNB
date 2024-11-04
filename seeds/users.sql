DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (email, name, password) VALUES 
('user1@example.com', 'User One', 'password1'),
('user2@example.com', 'User Two', 'password2'),
('user3@example.com', 'User Three', 'password3');
