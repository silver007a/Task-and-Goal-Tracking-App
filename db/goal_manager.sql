DROP TABLE IF EXISTS milestone;
DROP TABLE IF EXISTS goals;

CREATE TABLE goals (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  description VARCHAR(255),
  position INT,
  event_date VARCHAR(255)
);

CREATE TABLE milestone (
  id SERIAL PRIMARY KEY,
  mile_title VARCHAR(255),
  mile_desc VARCHAR(255),
  mile_position INT,
  mile_date VARCHAR(255),
  goal_id INT REFERENCES goals(id)
);
