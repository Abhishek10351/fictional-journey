CREATE TABLE IF NOT EXISTS trophies (
  id INTEGER PRIMARY KEY NOT NULL,
  trophy_name VARCHAR(255) NOT NULL,
  description VARCHAR(255) NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  earned INTEGER NOT NULL CHECK (earned IN (0, 1)),
  earned_date TEXT DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS settings (
  sound INTEGER NOT NULL CHECK (sound IN (0, 1)),
  music INTEGER NOT NULL CHECK (music IN (0, 1)),
  volume INTEGER NOT NULL CHECK (volume >= 0 AND volume <= 100)
);

CREATE TABLE IF NOT EXISTS high_scores (
  level INTEGER PRIMARY KEY CHECK (level >= 1),
  score INTEGER NOT NULL CHECK (score >= 0) DEFAULT 0
);
