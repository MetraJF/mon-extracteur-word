import streamlit as st
from docx import Document

# 1. Titre de l'application
st.title("🔍 Extracteur de texte en GRAS")
st.write("Chargez un document Word pour extraire uniquement les passages en gras.")

# 2. Le "Guichet" (Upload du fichier)
uploaded_file = st.file_uploader("Choisissez votre fichier .docx", type="docx")

if uploaded_file is not None:
    # 3. Lecture du fichier (sans se soucier du chemin !)
    document = Document(uploaded_file)
    
    texte_gras_trouve = []
    
    # 4. Analyse (Paragraphe par paragraphe, puis morceau par morceau)
    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            # Si le morceau est en gras
            if run.bold:
                texte_gras_trouve.append(run.text)
    
    # 5. Affichage du résultat
    if texte_gras_trouve:
        st.success(f"{len(texte_gras_trouve)} éléments trouvés !")
        
        # On affiche chaque élément trouvé
        st.subheader("Voici le texte en gras extrait :")
        for bout_de_texte in texte_gras_trouve:
            st.write(f"- {bout_de_texte}")
            
        # 6. Bouton pour télécharger le résultat (Optionnel)
        resultat_final = "\n".join(texte_gras_trouve)
        st.download_button(
            label="Télécharger le résultat en .txt",
            data=resultat_final,
            file_name="resultat_gras.txt",
            mime="text/plain"
        )
    else:
        st.warning("Aucun texte en gras trouvé dans ce document.")