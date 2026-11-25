import pandas as pd
import streamlit as st

"""Le calculateur d’intérêts composés.La boucle simule un mois à la fois. Elle applique le rendement
 au capital déjà accumulé, puis ajoute le versement de fin de mois. Cette lignepermet d’expliquer pourquoi
les intérêts déjà gagnés peuvent eux-mêmes produire des intérêts.""" 

st.title("Calculateur d’intérêts composés")
st.caption("Simulation éducative avec un rendement constant et non garanti.")

versement = st.slider("Versement mensuel (€)", 0, 1000, 100)
taux_annuel = st.slider("Rendement annuel (%)", 0.0, 10.0, 5.0, step=0.1)
duree = st.slider("Durée (années)", 1, 40, 10)

taux_mensuel = (1 + taux_annuel / 100) ** (1 / 12) - 1
capital = 0.0
historique = [capital]

for mois in range(duree * 12):
    capital = capital * (1 + taux_mensuel) + versement
    historique.append(capital)

donnees = pd.DataFrame({
    "Mois": range(len(historique)),
    "Capital (€)": historique,
})

st.line_chart(donnees, x="Mois", y="Capital (€)")
st.metric("Capital final", f"{capital:.2f} €")
st.metric("Total versé", f"{versement * duree * 12:.2f} €")