import streamlit as st
import pandas as pd
import os

# Charger le fichier Excel
file_path = "Calculateur_Economie_Energie_Pompes.xlsx"

# Vérifiez si le fichier existe avant de charger les données
if not os.path.exists(file_path):
    st.error(f"Le fichier Excel '{file_path}' est introuvable. Veuillez vérifier qu'il est bien dans le même dossier que ce script.")
else:
    # Charger les deux feuilles pertinentes
    def load_data():
        sll_sheet = pd.read_excel(file_path, sheet_name='Calculateur SLL vs SP').dropna(how='all').reset_index(drop=True)
        dsf_sheet = pd.read_excel(file_path, sheet_name='Calculateur StarFlo-StarFloVS').dropna(how='all').reset_index(drop=True)
        return sll_sheet, dsf_sheet

    sll_data, dsf_data = load_data()

    # Fonction pour extraire les informations clés d'une feuille
    def extract_results(sheet):
        params = {
            "Coût du kWh": sheet.iloc[1, 2],
            "Volume de la piscine (m3)": sheet.iloc[1, 3],
            "Puissance de la pompe actuelle (CV)": sheet.iloc[1, 4],
            "Nombre d'heures de filtration": sheet.iloc[1, 5],
            "Durée de la saison (mois)": sheet.iloc[1, 6]
        }
        
        results = {
            "Économies d'énergie": sheet.iloc[2, 4],
            "Économies chaque année": sheet.iloc[3, 4],
            "Modèle préconisé": sheet.iloc[3, 3]
        }
        return params, results

    sll_params, sll_results = extract_results(sll_data)
    dsf_params, dsf_results = extract_results(dsf_data)

    # Construire l'application Streamlit
    st.title("Calculateur d'Économies d'Énergie des Pompes")

    # Section SLL
    st.header("Scénario : Calculateur SLL vs SP")
    st.subheader("Paramètres")
    for key, value in sll_params.items():
        st.write(f"**{key}**: {value}")

    st.subheader("Résultats")
    for key, value in sll_results.items():
        st.write(f"**{key}**: {value}")

    # Section DSF
    st.header("Scénario : Calculateur StarFlo-StarFloVS")
    st.subheader("Paramètres")
    for key, value in dsf_params.items():
        st.write(f"**{key}**: {value}")

    st.subheader("Résultats")
    for key, value in dsf_results.items():
        st.write(f"**{key}**: {value}")
