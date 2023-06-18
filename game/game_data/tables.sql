CREATE TABLE IF NOT EXISTS trophies (
  id INTEGER PRIMARY KEY NOT NULL,
  trophy_name VARCHAR(255) NOT NULL,
  description VARCHAR(255) NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  unlocked INTEGER CHECK (unlocked IN (0, 1)) DEFAULT 0,
  earned_date TEXT
);

CREATE TABLE IF NOT EXISTS settings (
  sound INTEGER NOT NULL CHECK (sound IN (0, 1)) DEFAULT 1,
  music INTEGER NOT NULL CHECK (music IN (0, 1)) DEFAULT 1,
  volume INTEGER NOT NULL CHECK (volume >= 0 AND volume <= 100) DEFAULT 75
);

CREATE TABLE IF NOT EXISTS levels (
  level INTEGER PRIMARY KEY CHECK (level <=1),
  name VARCHAR(255) NOT NULL,
  high_score INTEGER NOT NULL CHECK (high_score >= 0) DEFAULT 0,
  description TEXT NOT NULL,
  objective TEXT NOT NULL,
  stars INTEGER NOT NULL DEFAULT 0 CHECK (stars >= 0 AND stars <= 3),
  unlocked INTEGER NOT NULL DEFAULT 0 CHECK (unlocked IN (0, 1)),
  completed INTEGER NOT NULL DEFAULT 0 CHECK (completed IN (0, 1))
);

CREATE TABLE IF NOT EXISTS powerups (
    id VARCHAR(10) PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    duration INTEGER NOT NULL,
    rarity TEXT NOT NULL,
    path TEXT NOT NULL
);
