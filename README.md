# App Finance : apprendre les bases de l'épargne, des ETF et des cryptomonnaies

Application web éducative réalisée dans le cadre du projet Y-Days (Labo Dev Web).
Elle aide un débutant à comprendre l'épargne, les ETF et les cryptomonnaies avec des simulations et de vraies données de marché.

> **Avertissement** : ce projet est strictement éducatif. Il ne constitue pas un conseil en investissement
> (activité réglementée en France). Les performances passées ne préjugent pas des performances futures.

## Démo

- Application en ligne : [à compléter : lien Streamlit Community Cloud]
- Capture d'écran : [à compléter : ajouter une image dans le dossier docs/ puis la référencer ici]

## Pitch

[à compléter, 3 phrases: le problème, ce que fait l'app, le cadre éducatif]

## Fonctionnalités

- [ ] Calculateur d'intérêts composés (curseurs + graphique)
- [ ] Page « Marchés » : Bitcoin vs S&P 500, avec calcul de la volatilité
- [ ] 3 mini-leçons, chacune avec un court texte et un quiz de 3 questions
- [ ] Données de secours (CSV) si la récupération en ligne échoue
- [ ] Bonus (si le temps le permet) : comparateur de frais d'ETF, portefeuille virtuel, regroupement d'actifs (KMeans)

(A Cocher au fur et à mesure : `- [x]`.)

## Installation (Windows)

1. Installer Python 3 (en cochant « Add python.exe to PATH »).
2. Récupérer le projet :
   ```
   git clone [à compléter : adresse du dépôt]
   cd app-finance
   ```
3. Installer les bibliothèques :
   ```
   py -m pip install -r requirements.txt
   ```

## Utilisation

```
py -m streamlit run app.py
```

Une page s'ouvre dans le navigateur (http://localhost:8501). Le menu de gauche permet de passer d'un module à l'autre.

## Structure du projet

```
app-finance/
├── app.py            # page d'accueil
├── pages/            # une page par module
├── utils.py          # fonctions de calcul (à créer)
├── data/             # fichiers CSV de secours
├── requirements.txt
└── README.md
```

## Sources de données

- Prix du Bitcoin et de l'indice S&P 500 : bibliothèque `yfinance` (données Yahoo Finance, source non officielle).
- Fichiers CSV de secours dans `data/` : [à compléter : date de la dernière sauvegarde].

## Limites

[à compléter honnêtement, au moins 2 points. Pistes :]
- yfinance n'est pas une source officielle : le service peut changer ou limiter les requêtes.
- Les données passées ne permettent pas de prédire les prix : l'app n'essaie donc pas de le faire.
- Les simulations utilisent un rendement constant, ce qui n'est pas réaliste.

## Pour mon alternance

[à compléter en fin de projet, une demi-page :]
- **Compétences montrées** : [ex. récupération et nettoyage de données, calcul d'indicateurs, application web, Git]
- **Difficultés rencontrées** : [ex. API indisponible, comment tu as réglé le problème]
- **Évolutions possibles** : [ex. React/FastAPI, portefeuille virtuel, base de données SQL]

## Auteur

 Aurélie Malgorn, B2 IA/Data, 2026-2027