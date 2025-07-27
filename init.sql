CREATE TABLE IF NOT EXISTS countries (
    id SERIAL PRIMARY KEY, 
    country VARCHAR(255) NOT NULL,
    population INT NOT NULL,
    region VARCHAR(255) NOT NULL
);