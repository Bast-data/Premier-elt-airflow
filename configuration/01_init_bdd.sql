
CREATE TABLE IF NOT EXISTS commandes_brutes(
    id_brute SERIAL PRIMARY KEY,
    prenom VARCHAR(50),
    nom VARCHAR(50),
    email VARCHAR(50),
    age VARCHAR(50),
    telephone VARCHAR(20),
    ville VARCHAR(50),
    date_inscription VARCHAR(50),
    charge_le TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS commandes_propres(
    id_propre SERIAL PRIMARY KEY,
    prenom VARCHAR(50),
    nom VARCHAR(50),
    email VARCHAR(50),
    age INT, 
    telephone VARCHAR(20),
    ville VARCHAR(50),
    date_inscription DATE

);
