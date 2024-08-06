import os
import time
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from modules.write_assistant import create_document
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

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

    file = st.file_uploader("Upload PDF file that will be used for abstract creation:", type=["pdf"], key='pdf')

    if st.session_state.pdf:
        st.session_state.pdf_ref = st.session_state.pdf

    if file:

        tab1, tab2 = st.tabs(["Input Document", "Generated Abstract"])

        with tab1:
            if st.session_state.pdf_ref:
                binary_data = st.session_state.pdf_ref.getvalue()
                pdf_viewer(input=binary_data, width=700, height=800)

        with tab2:
            start_time = time.time()

            st.info("Analyzing the document ...", icon="⏳")
            doc = analyze_documents_output_in_markdown(file)
            analysis_time = time.time() - start_time
            st.info(f"Analysis completed in {analysis_time:.2f} seconds.", icon="✅")

            st.info("Creating an abstract of the document ...", icon="⏳")
            abstract_start_time = time.time()
            abstract = create_document(doc.content)
            abstract_time = time.time() - abstract_start_time
            st.info(f"Abstract created in {abstract_time:.2f} seconds.", icon="✅")
            
            st.divider()
            st.markdown(abstract.choices[0].message.content)

if __name__ == "__main__":
    main()