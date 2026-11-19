# Règles de transformation (TP 3)

| Réf. | Étape | Règle | Justification |
|------|-------|-------|---------------|
| R01 | raw -> trusted | Produit : espaces supprimés, première lettre en majuscule, reste en minuscules | Un même produit doit avoir un seul libellé pour être regroupé et joint au stock |
| R02 | raw -> trusted | Prix : virgule remplacée par un point, puis conversion en nombre | Les prix doivent être numériques pour calculer les montants |
| R03 | raw -> trusted | Lignes invalides (client vide ou inconnu, prix ou quantité invalide, date invalide) isolées dans `_rejets/` avec un motif | On ne devine pas une valeur manquante ; la ligne est gardée pour être corrigée avec la source |
| R04 | trusted -> curated | Email remplacé par un pseudonyme (SHA-256 avec sel), nom et téléphone retirés | Les analystes n'ont pas besoin de l'identité des clients (minimisation RGPD) |
| R05 | raw -> trusted | Dates : format AAAA-MM-JJ, puis JJ/MM/AAAA si le premier échoue | Le partenaire envoie des dates au format français |
| R06 | raw -> trusted | Doublons exacts supprimés et comptés dans le journal | Une commande en double fausserait le chiffre d'affaires |
