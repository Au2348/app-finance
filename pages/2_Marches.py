import plotly.express as px
import streamlit as st
import yfinance as yf
from pathlib import Path
import pandas as pd

"""La page Marchés. Elle va comparer l’évolution du Bitcoin
et du S&P 500 sur un an, puis mesurer lequel a le plus fluctué sur la période.
Le Bitcoin cote aussi le week-end. Le code garde les dates où les deux séries ont
une clôture, puis calcule les variations sur ces mêmes intervalles. 
La base 100 est choisi pour que l'on puisse comparer la progression des deux courbes sur un seul graphique. Doc: yfinance.download"""

st.title("Marchés")
st.caption("Comparaison pédagogique du Bitcoin et du S&P 500 sur un an.")

noms = {"BTC-USD": "Bitcoin", "^GSPC": "S&P 500"}


@st.cache_data(ttl=3600)
def charger_cours():
    donnees = yf.download(
        list(noms),
        period="1y",
        interval="1d",
        auto_adjust=False,
        progress=False,
    )

    if donnees is None or donnees.empty or "Close" not in donnees:
        return None

    cours = donnees["Close"].reindex(columns=list(noms)).dropna()
    return cours.rename(columns=noms).sort_index()


fichier_secours = Path(__file__).resolve().parents[1] / "data" / "cours_marches.csv"
mode_hors_ligne = st.checkbox("Tester le mode hors ligne")

cours = None
if not mode_hors_ligne:
    try:
        cours = charger_cours()
    except Exception:
        cours = None

if cours is None or len(cours) < 3:
    try:
        cours = pd.read_csv(fichier_secours, index_col="Date", parse_dates=["Date"])
        cours = cours[["Bitcoin", "S&P 500"]].apply(pd.to_numeric)
        cours = cours.dropna().sort_index()
    except (OSError, ValueError, KeyError):
        cours = None

    if cours is None or len(cours) < 3:
        st.error("Impossible de charger les cours. Vérifie le fichier data/cours_marches.csv.")
        st.stop()

    st.warning("Données de secours affichées.")

# Sur chaque date commune, on compare la clôture à celle de la date commune précédente.
variations = cours.pct_change().dropna()
volatilite = variations.std() * 100

# Les deux courbes partent de 100 pour comparer leur évolution.
base_100 = cours.div(cours.iloc[0]) * 100
graphique = px.line(
    base_100,
    labels={"index": "Date", "value": "Valeur en base 100", "variable": "Série"},
)

st.write(f"Période observée du {cours.index[0]:%d/%m/%Y} au {cours.index[-1]:%d/%m/%Y}")
st.plotly_chart(graphique)
st.download_button(
    "Télécharger les cours",
    data=cours.to_csv(index_label="Date").encode("utf-8"),
    file_name="cours_marches.csv",
    mime="text/csv",
)
st.caption("Une valeur de 110 correspond à une hausse de 10 % depuis le début de la période.")

st.subheader("Volatilité observée")
for nom, valeur in volatilite.items():
    st.metric(nom, f"{valeur:.2f} %")

st.write("La volatilité mesure ici la dispersion des variations entre deux clôtures communes.")
st.caption("Source des cours : Yahoo Finance via yfinance. Les performances passées ne préjugent pas des performances futures.")