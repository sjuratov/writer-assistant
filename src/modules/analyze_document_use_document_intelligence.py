# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: analyze_document_use_document_intelligence.py

DESCRIPTION:
    This sample demonstrates how to analyze an document in markdown output format.

USAGE:
    python analyze_document_use_document_intelligence.py

    Set the environment variables with your own values before running the sample:
    1) FORM_RECOGNIZER_ENDPOINT - the endpoint to your Document Intelligence resource.
    2) FORM_RECOGNIZER_KEY - your Document Intelligence API key.

IMPORTANT:
    This sample is using new azure-ai-documentintelligence library. It's important that "Azure AI services multi-service account" resource
    is created in one of following regions: eastus, westus2 or westeurope. This is required for the new API to work.
"""

import os

from azure.core.exceptions import HttpResponseError
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def analyze_documents_output_in_markdown(document: str):

    from azure.core.credentials import AzureKeyCredential
    from azure.ai.documentintelligence import DocumentIntelligenceClient
    from azure.ai.documentintelligence.models import ContentFormat, AnalyzeResult
    import base64

    endpoint = os.environ["FORM_RECOGNIZER_ENDPOINT"]
    key = os.environ["FORM_RECOGNIZER_KEY"]

    with open(document, "rb") as f:
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

if __name__ == "__main__":

    document = "documents/2407.16375v1.pdf"

    try:
        result = analyze_documents_output_in_markdown(document)
        print(f"Here's the full content in format {result.content_format}:\n")
        print(result.content)
    except Exception as error:
        print(f"An error occurred: {error}")
        raise