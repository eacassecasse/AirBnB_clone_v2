-- Creates a database and a user o manage this database
USE hbnb_dev_db;

CREATE TABLE IF NOT exists states
(
    id         VARCHAR(60)  NOT NULL PRIMARY KEY,
    name       VARCHAR(128) NOT NULL,
    created_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    updated_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE IF NOT exists cities
(
    id         VARCHAR(60)  NOT NULL PRIMARY KEY,
    name       VARCHAR(128) NOT NULL,
    state_id   VARCHAR(60)  NOT NULL,
    created_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    updated_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    FOREIGN KEY (state_id) REFERENCES states (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT exists users
(
    id         VARCHAR(60)  NOT NULL PRIMARY KEY,
    email      VARCHAR(128) NOT NULL,
    password   VARCHAR(128) NOT NULL,
    first_name VARCHAR(128),
    last_name  VARCHAR(128),
    created_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    updated_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE IF NOT exists amenities
(
    id         VARCHAR(60)  NOT NULL PRIMARY KEY,
    name       VARCHAR(128) NOT NULL,
    created_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    updated_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE IF NOT exists places
(
    id               VARCHAR(60)  NOT NULL PRIMARY KEY,
    name             VARCHAR(128) NOT NULL,
    description      VARCHAR(1024),
    number_rooms     INT          NOT NULL DEFAULT 0,
    number_bathrooms INT          NOT NULL DEFAULT 0,
    max_guest        INT          NOT NULL DEFAULT 0,
    price_by_night   INT          NOT NULL DEFAULT 0,
    latitude         FLOAT,
    longitude        FLOAT,
    user_id          VARCHAR(60)  NOT NULL,
    city_id          VARCHAR(60)  NOT NULL,
    created_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    updated_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (city_id) REFERENCES cities (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT exists place_amenity
(
    amenity_id VARCHAR(60) NOT NULL,
    place_id   VARCHAR(60) NOT NULL,
    PRIMARY KEY (amenity_id, place_id),
    FOREIGN KEY (amenity_id) REFERENCES amenities (id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES places (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT exists reviews
(
    id         VARCHAR(60)   NOT NULL PRIMARY KEY,
    text       VARCHAR(1024) NOT NULL,
    user_id    VARCHAR(60)   NOT NULL,
    place_id   VARCHAR(60)   NOT NULL,
    created_at DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    updated_at DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES places (id) ON DELETE CASCADE
);
