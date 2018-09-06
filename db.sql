CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(500) NOT NULL,
    role INT NOT NULL
);

CREATE TABLE IF NOT EXISTS comments(
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    content text NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES users (id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS user_trail(
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    lastLoggedInAt TIMESTAMP,
    FOREIGN KEY (user_id)
        REFERENCES users (id)
        ON UPDATE CASCADE ON DELETE CASCADE
);
