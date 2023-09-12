-- CREATE TABLE new_offers (
--     id SERIAL PRIMARY KEY,
--     offer_link VARCHAR(255),
--     offer_name VARCHAR(255),
--     company VARCHAR(255),
--     main_location VARCHAR(255),
--     other_location VARCHAR(255)
-- );
-- CREATE TABLE new_offers (
--     id SERIAL PRIMARY KEY,
--     offer_link VARCHAR(255),
--     offer_name VARCHAR(255),
--     company VARCHAR(255),
--     main_location VARCHAR(255),
--     other_location VARCHAR(255),
--     salary VARCHAR(255),
--     salary_type VARCHAR(255),
--     main_requirements_description TEXT,
--     main_offer_description TEXT,
--     your_responsibilities TEXT,
--     offer_details TEXT,
--     equipment_supplied TEXT,
--     methodology TEXT,
--     perks_in_the_office TEXT,
--     benefits TEXT,
--     company_info_Founded_in VARCHAR(255),
--     company_info_Company_size VARCHAR(255),
--     company_info_Main_location VARCHAR(255),
--     date_of_scrapping DATE,
--     when_published_relatively VARCHAR(255),
--     categories TEXT,
--     skills_maturity VARCHAR(255),
--     tags_mandatory TEXT,
--     tags_nice_to_have TEXT
-- );

-- -- Dodaj nowe kolumny z właściwymi typami danych
-- ALTER TABLE new_offers
-- ADD COLUMN categories_new TEXT,
-- ADD COLUMN tags_mandatory_new TEXT,
-- ADD COLUMN tags_nice_to_have_new TEXT;

-- -- Skopiuj dane z istniejących kolumn do nowych kolumn
-- UPDATE new_offers
-- SET categories_new = categories::TEXT,
--     tags_mandatory_new = tags_mandatory::TEXT,
--     tags_nice_to_have_new = tags_nice_to_have::TEXT;

-- -- Usuń stare kolumny, jeśli to konieczne
-- ALTER TABLE new_offers
-- DROP COLUMN categories,
-- DROP COLUMN tags_mandatory,
-- DROP COLUMN tags_nice_to_have;

-- -- Zmień nazwy nowych kolumn na oryginalne, jeśli to konieczne
-- ALTER TABLE new_offers
-- RENAME COLUMN categories_new TO categories,
-- RENAME COLUMN tags_mandatory_new TO tags_mandatory,
-- RENAME COLUMN tags_nice_to_have_new TO tags_nice_to_have;


-- Zmień nazwy nowych kolumn na oryginalne, jeśli to konieczne
-- ALTER TABLE new_offers
-- RENAME COLUMN categories_new TO categories;
-- ALTER TABLE new_offers
-- RENAME COLUMN tags_mandatory_new TO tags_mandatory;
-- ALTER TABLE new_offers
-- RENAME COLUMN tags_nice_to_have_new TO tags_nice_to_have;

TRUNCATE new_offers RESTART IDENTITY;