Pipeline ELT — Commandes

Pipeline de données automatisé qui extrait, charge et transforme des données clients, orchestré avec Apache Airflow et entièrement conteneurisé avec Docker.

Description

Ce projet simule un cas réel de data engineering : des données clients arrivent sous forme de CSV brut (avec des doublons, des valeurs manquantes, des formats incohérents), et doivent être nettoyées puis rendues disponibles dans une base PostgreSQL pour être exploitées de façon fiable. L'ensemble du pipeline est orchestré automatiquement par Airflow, une fois par jour.

Pourquoi ELT et pas ETL ?

Je m'étais entraîné jusque-là uniquement sur des architectures ETL (Extract, Transform, Load), où les données sont nettoyées en Python (avec pandas) avant d'être insérées en base. Je voulais aussi savoir faire de l'ELT, l'approche aujourd'hui la plus répandue en entreprise.
Changer de structure m'a fait bizarre au début : au lieu de nettoyer les données en pandas comme j'en avais l'habitude, il faut charger les données brutes telles quelles dans une table de landing (commandes_brutes), et laisser PostgreSQL lui-même, via des requêtes SQL, faire tout le nettoyage — casse, typage, filtrage des valeurs invalides. Le résultat propre est ensuite écrit dans une seconde table (commandes_propres).
Ce changement de logique (nettoyer en SQL plutôt qu'en Python) demande de penser différemment, mais c'est une compétence utile à avoir en plus de l'ETL classique, pas un remplacement.

Architecture
Outil	Rôle
Docker / Docker Compose	Conteneurise et orchestre l'ensemble des services (base de données + Airflow)
PostgreSQL	Stocke les données brutes et les données transformées
Apache Airflow	Orchestre l'exécution des 3 étapes du pipeline, une fois par jour
Python (pandas, SQLAlchemy)	Extraction du CSV et chargement en base
SQL	Nettoyage et transformation des données, exécuté directement dans PostgreSQL


Ce que j'ai appris

Écrire des requêtes SQL de nettoyage robustes : typage (CAST), formatage de texte (INITCAP, LOWER), nettoyage par expressions régulières (regexp_replace), filtrage de valeurs nulles ou invalides
Orchestrer un pipeline multi-étapes avec Apache Airflow (DAG, BashOperator, dépendances entre tâches)
Conteneuriser une infrastructure complète avec Docker Compose (plusieurs services interdépendants, volumes, réseau interne)
