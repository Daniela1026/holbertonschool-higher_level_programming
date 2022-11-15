-- unique_id description id name
CREATE TABLE
IF NOT EXISTS unique_id
(
    id INT UNSIGNED DEFAULT 1,
    name VARCHAR(256),
    UNIQUE(id)
);