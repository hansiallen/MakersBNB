DROP TABLE IF EXISTS spaces CASCADE;

CREATE TABLE spaces (
    space_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    owner_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    price_per_night DECIMAL NOT NULL
);

INSERT INTO spaces (name, description, owner_id, price_per_night) VALUES 
('Cozy Cottage', 'A cozy cottage in the countryside', 1, 100.00),
('Urban Loft', 'A stylish loft in the city', 2, 150.00),
('Beach House', 'A relaxing beach house with ocean views', 3, 200.00);
