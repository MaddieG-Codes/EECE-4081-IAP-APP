DROP TABLE IF EXISTS locations;

CREATE TABLE locations (
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    city        TEXT NOT NULL,
    category    TEXT NOT NULL,
    description TEXT NOT NULL,
    latitude    REAL NOT NULL,
    longitude   REAL NOT NULL
);
