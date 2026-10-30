CREATE TABLE IF NOT EXISTS commandes (
    id SERIAL PRIMARY KEY,
    client_id INT,
    produit VARCHAR(100),
    quantite INT,
    prix_unitaire NUMERIC(10,2),
    date_commande DATE
);

INSERT INTO commandes (client_id, produit, quantite, prix_unitaire, date_commande) VALUES
(1, 'Ordinateur portable', 2, 899.99, '2026-09-05'),
(2, 'Souris sans fil', 5, 19.99, '2026-09-06'),
(3, 'Clavier mecanique', 1, 59.99, '2026-09-07'),
(1, 'Ecran 24 pouces', 1, 179.99, '2026-09-08');
