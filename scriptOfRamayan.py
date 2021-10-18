import streamlit as st

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

st.set_page_config(layout="wide",
                  page_title="Script Translation and Analysis")

raw_data = st.container()
scriptArea = st.container()
footer = st.container()


with raw_data:
    st.markdown("<h1 style='text-align: center;color: white;'>Indian Cultural Play (Hindi) Translated to English</h1>", unsafe_allow_html=True)
    st.text("The story of Ramayana is synonymous with Indian Culture as it shows us the life journey of Rama, Lakshmana, Sita, etc")
    st.text("who we consider to be our Gods. This website contains the translation of the Hindi play to English Language.")
    selected_state = st.selectbox("Choose the state whose data you want to see", options=["Act 1","Act 2","Act 3","Act 4","Act 5","Act 6","Act 7","Act 8",], index=0)
    state = (selected_state[-1:])

with scriptArea:
    st.title("Scripts")
    st.text("The scripts in Hindi to the left and the translated scripts in English to the right")
    hindiCol, englishCol = st.columns(2)

    txt = getText("hindi/act%sh.docx"%state)
    hindiCol.markdown("<h3 style='text-align: center;color: Red;'>Hindi</h3>", unsafe_allow_html=True)
    hindiCol.text(txt)


    txt = getText("english/act%se.docx"%state)
    englishCol.markdown("<h3 style='text-align: center;color: Green;'>English</h3>", unsafe_allow_html=True)
    englishCol.text(txt)

with footer:
	st.write("For the entire script, Click this [link](https://drive.google.com/file/d/1FGRYaE_gh9bPw44e2yOHHQx1AGn1orDj/view?usp=sharing) for Hindi and this [link](https://drive.google.com/file/d/1E2SbEYYXiUESsrzk0zIyqalKepOAKBsw/view?usp=sharing) for English!")
	st.markdown("<h5 style='text-align: center; color: red;'>Translated and Designed By Aryan Dawer</h5>", unsafe_allow_html=True)
