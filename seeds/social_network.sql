DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(255),
    username text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content text,
    view_count INTEGER,
    account_id INTEGER
);



-- Finally, we add any records that are needed for the tests to run
INSERT INTO accounts (email_address, username) VALUES ('1234@gmail.com', '1234');
INSERT INTO accounts (email_address, username) VALUES ('5678@gmail.com', '5678');


INSERT INTO posts (title, content, view_count, account_id) VALUES ('Title 1', 'some content', 50, 1);
INSERT INTO posts (title, content, view_count, account_id) VALUES ('Title 2', 'some more content', 21, 1);
INSERT INTO posts (title, content, view_count, account_id) VALUES ('Title 3', 'even more content', 104324, 2);
