DROP TABLE IF EXISTS spaces CASCADE;

CREATE TABLE spaces (
    space_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    owner_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    price_per_night DECIMAL NOT NULL,
    available_dates JSONB
);

INSERT INTO spaces (title, description, owner_id, price_per_night, available_dates) VALUES 
('Cozy Cottage', 'A cozy cottage in the countryside', 1, 100.00, '["2024-11-10", "2024-11-11"]'),
('Urban Loft', 'A stylish loft in the city', 2, 150.00, '["2024-11-15", "2024-11-16"]'),
('Beach House', 'A relaxing beach house with ocean views', 3, 200.00, '["2024-11-20", "2024-11-21"]');
