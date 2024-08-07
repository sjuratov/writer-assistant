import os
import time
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from modules.write_assistant import create_document
from dotenv import find_dotenv, load_dotenv
import json
import pandas as pd

load_dotenv(find_dotenv())

def read_prompt(prompt_file = 'prompts.json'):
    with open(prompt_file, 'r') as file:
        data = json.load(file)
    df = pd.json_normalize(data['prompts'])
    df = df[['Title', 'Description', 'Prompt']]
    return df

def analyze_documents_output_in_markdown(f):

    from azure.core.credentials import AzureKeyCredential
    from azure.ai.documentintelligence import DocumentIntelligenceClient
    from azure.ai.documentintelligence.models import ContentFormat, AnalyzeResult
    import base64

    endpoint = os.environ["FORM_RECOGNIZER_ENDPOINT"]
    key = os.environ["FORM_RECOGNIZER_KEY"]

    base64_encoded_pdf = base64.b64encode(f.read()).decode("utf-8")

    analyze_request = {
        "base64Source": base64_encoded_pdf
    }

    document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-layout",
        analyze_request=analyze_request,
        output_content_format=ContentFormat.MARKDOWN,
    )
    result: AnalyzeResult = poller.result()

    return result

def main():
    st.set_page_config(layout="centered")
    st.title("Write Assistant")

    if 'pdf_ref' not in st.session_state:
        st.session_state.pdf_ref = None

    if 'json_ref' not in st.session_state:
        st.session_state.json_ref = None

    file = st.file_uploader("Upload PDF file that will be used for abstract creation:", type=["pdf"], key='pdf')
    if file:
        df = read_prompt()

        selected_prompt_title = st.selectbox('Select a prompt:', df['Title'], 0, key='json')
        selected_prompt_description = df.loc[df.Title == selected_prompt_title]["Description"].iloc[0]
        selected_prompt = ' '.join(df.loc[df.Title == selected_prompt_title]["Prompt"].iloc[0])
        st.info(f"Prompt description: {selected_prompt_description}")

        if st.session_state.pdf:
            st.session_state.pdf_ref = st.session_state.pdf

        if st.session_state.json:
            st.session_state.json_ref = st.session_state.json

        if st.button('Create'):

            tab1, tab2 = st.tabs(["Input Document", "Generated Content"])

            with tab1:
                if st.session_state.pdf_ref:
                    binary_data = st.session_state.pdf_ref.getvalue()
                    pdf_viewer(input=binary_data, width=700, height=800)

            with tab2:
                if st.session_state.pdf_ref and st.session_state.json_ref:
                    start_time = time.time()

                    st.info("Analyzing input document ...", icon="⏳")
                    doc = analyze_documents_output_in_markdown(file)
                    analysis_time = time.time() - start_time
                    st.info(f"Analysis completed in {analysis_time:.2f} seconds.", icon="✅")

                    st.info(f"Generating {selected_prompt_title} ...", icon="⏳")
                    abstract_start_time = time.time()
                    abstract = create_document(doc.content, selected_prompt)
                    abstract_time = time.time() - abstract_start_time
                    st.info(f"Generation completed in {abstract_time:.2f} seconds.", icon="✅")
                    
                    st.divider()
                    st.markdown(abstract.choices[0].message.content)

if __name__ == "__main__":
    main()