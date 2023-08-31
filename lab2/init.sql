CREATE TABLE offers (
    id SERIAL PRIMARY KEY,
    offer_link VARCHAR(255),
    offer_name VARCHAR(255),
    company VARCHAR(255),
    main_location VARCHAR(255),
    other_location VARCHAR(255)
);