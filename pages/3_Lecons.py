import streamlit as st

st.title("Leçons et quiz")

lecons = {
    "Épargne": {
        "texte": (
            "Épargner, c’est mettre de l’argent de côté pour un besoin futur. "
            "Quand les intérêts restent dans le capital, ils peuvent à leur tour "
            "produire des intérêts. C’est le principe des intérêts composés."
        ),
        "questions": [
            ("Combien verses-tu en un an à raison de 100 € par mois ?",
             ["100 €", "1 000 €", "1 200 €"], 2,
             "Il y a 12 versements de 100 €, soit 1 200 €."),
            ("À 0 % de rendement et sans frais, quel est ton capital après ces versements ?",
             ["1 200 €", "1 260 €", "0 €"], 0,
             "À 0 %, le capital est égal à la somme versée."),
            ("Que deviennent les intérêts quand ils sont réinvestis ?",
             ["Ils sont retirés du capital", "Ils peuvent produire des intérêts", "Ils disparaissent"], 1,
             "Les intérêts réinvestis s’ajoutent au capital qui produit les intérêts suivants."),
        ],
    },
    "ETF": {
        "texte": (
            "Un ETF est un fonds négocié en bourse. Beaucoup d’ETF cherchent à "
            "suivre un indice. Un ETF qui répartit ses investissements sur plusieurs "
            "entreprises réduit l’exposition à une seule d’entre elles, mais sa valeur peut baisser."
        ),
        "questions": [
            ("Qu’est-ce qu’un ETF ?", ["Un livret", "Un fonds négocié en bourse", "Une cryptomonnaie"], 1,
             "Les parts d’un ETF s’achètent et se vendent en bourse."),
            ("Un ETF qui suit un indice peut-il perdre de la valeur ?",
             ["Oui", "Non", "Seulement si l’indice monte"], 0,
             "Si l’indice baisse, un ETF qui le suit peut aussi baisser."),
            ("Que signifie diversifier ?", ["Acheter une seule action", "Éviter tous les frais",
                                             "Répartir ses investissements"], 2,
             "Répartir ses investissements réduit la dépendance à un seul actif."),
        ],
    },
    "Cryptomonnaies": {
        "texte": (
            "Le Bitcoin est un actif numérique. Son prix varie au fil du temps. "
            "Sur la page Marchés, la volatilité mesure à quel point les variations "
            "observées se dispersent autour de leur moyenne."
        ),
        "questions": [
            ("Que peut indiquer une forte volatilité ?", ["Un prix garanti", "Des variations très dispersées",
                                                           "Une hausse certaine"], 1,
             "Les variations peuvent être fortes à la hausse comme à la baisse."),
            ("Si un prix passe de 100 € à 80 €, quelle est sa variation ?",
             ["−20 %", "+20 %", "−80 %"], 0,
             "La baisse est de 20 € par rapport aux 100 € de départ."),
            ("Une forte hausse passée garantit-elle une hausse future ?",
             ["Oui", "Oui, si elle a duré un an", "Non"], 2,
             "Les performances passées ne garantissent pas les performances futures."),
        ],
    },
}

theme = st.selectbox("Choisis une leçon", list(lecons))
lecon = lecons[theme]
st.write(lecon["texte"])

with st.form(f"quiz_{theme}"):
    reponses = []
    for question, options, _, _ in lecon["questions"]:
        reponses.append(st.radio(question, options, index=None))

    valider = st.form_submit_button("Corriger le quiz")

if valider:
    if None in reponses:
        st.warning("Réponds aux trois questions avant de corriger le quiz.")
    else:
        score = 0
        for reponse, (question, options, bonne_reponse, explication) in zip(
            reponses, lecon["questions"]
        ):
            if reponse == options[bonne_reponse]:
                score += 1
                st.success(f"{question} {explication}")
            else:
                st.error(
                    f"{question} Bonne réponse : {options[bonne_reponse]}. {explication}"
                )

        st.write(f"**Score : {score}/3**")