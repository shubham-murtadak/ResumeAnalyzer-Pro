from PyPDF2 import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space
from Source.source import resume_analyzer
import warnings
warnings.filterwarnings('ignore')
import os
from dotenv import load_dotenv
load_dotenv()

google_api_key=os.getenv('GEMINI_API_KEY')
print(google_api_key)
# page configuration


st.set_page_config(page_title='Resume Analyzer AI', layout="wide")

# page header transparent color
page_background_color ="""
<style>
[data-testid="stHeader"] 
{
background: rgba(0,0,0,0);
}
</style>
"""

st.markdown(page_background_color, unsafe_allow_html=True)

# title and position
st.markdown(f'<h1 style="text-align: center;">AI-Powered Resume Analyzer</h1>',
            unsafe_allow_html=True)


import time
# file upload
pdf = st.file_uploader(label='', type='pdf')

if pdf is not None:
    st.write("Resume Uploaded Successfully!")

    # time.sleep(3)
    # google_api_key = st.text_input(label='Google API key', type='password')
    # st.spinner("Connecting")

    # time.sleep(10)

    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key)

    if  google_api_key is not None:

        # sidebar
        with st.sidebar:

            add_vertical_space(3)

            option = st.selectbox(
                "Select option to analyze",
                ('Summary', 'Strength', 'Weakness', 'Job Role suggestions'))

        import time


        if option == 'Summary':
            try:
                if pdf is not None and google_api_key is not None:
                    text = resume_analyzer.extract_text(pdf)

                    summary = resume_analyzer.resume_summary(text)
                    result_summary = resume_analyzer.generate_response(google_api_key=google_api_key, llm=llm, task=summary)

                    st.subheader('Summary :')
                    st.write(result_summary)

            except Exception as e:
                col1, col2 = st.columns(2)
                with col1:
                    st.warning(e)


        if option == 'Strength':
            try:
                if pdf is not None and google_api_key is not None:
                    text = resume_analyzer.extract_text(pdf)

                    task = resume_analyzer.resume_strength(text)
                    result_strenght = resume_analyzer.generate_response(google_api_key=google_api_key, llm=llm, task=task)

                    st.subheader('Strengths :')
                    st.write(result_strenght)

            except Exception as e:
                col1, col2 = st.columns(2)
                with col1:
                    st.warning(e)

        if option == 'Weakness':
            try:
                if pdf is not None and google_api_key is not None:
                    text = resume_analyzer.extract_text(pdf)
                    task = resume_analyzer.resume_weakness(text)
                    result_weakness = resume_analyzer.generate_response(google_api_key=google_api_key, llm=llm, task=task)

                    st.subheader('Weaknesses:')
                    st.write(result_weakness)

            except Exception as e:
                col1, col2 = st.columns(2)
                with col1:
                    st.warning(e)

        if option == 'Job Role suggestions':
            try:
                if pdf is not None and google_api_key is not None:
                    text = resume_analyzer.extract_text(pdf)
                    task = resume_analyzer.job_title_suggestion(text)
                    job_titles = resume_analyzer.generate_response(google_api_key=google_api_key, llm=llm, task=task)

                    st.subheader('Job Roles suggestions :')
                    st.write(job_titles)

            except Exception as e:
                col1, col2 = st.columns(2)
                with col1:
                    st.warning(e)
