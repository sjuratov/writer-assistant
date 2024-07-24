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

def analyze_documents_output_in_markdown(url: str = "https://cob.silverchair-cdn.com/cob/content_public/journal/jcs/131/14/10.1242_jcs.186254/8/jcs186254.pdf?Expires=1724822537&Signature=SEdkl~B~m8Z8AeMboguMRS4WgAeHACgmN4CEb5bsbtfjN1mIIg2sjLVwkKaB0o5Ys1YGTut8jZjjHqPY6eZtnWr8CDqBrRLGb-N6QQzp7i9qBQBE1fOk86749~2o8gNWkITatoCfDGheDwMcbJo-IrCy4xB1NjbfMdhg1xhRIJDS8aErZsuS2p4nm6m28ycSk-qIB9BxIBp~NIMMRlWb90WmaI~oX2fuspGxmvsFlLni5m5fXJsZxH-ea5mxucnHXiVX2XZOoFwMW5rhUlf6n8oveiCPvHrPusddL6LsLfRHrDNlIj-EdtRcmwEu7PZSp0V~R4UnHXx1ram7zWk1UQ__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA"):

    from azure.core.credentials import AzureKeyCredential
    from azure.ai.documentintelligence import DocumentIntelligenceClient
    from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, ContentFormat, AnalyzeResult

    endpoint = os.environ["FORM_RECOGNIZER_ENDPOINT"]
    key = os.environ["FORM_RECOGNIZER_KEY"]
    url = url

    document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-layout",
        AnalyzeDocumentRequest(url_source=url),
        output_content_format=ContentFormat.MARKDOWN,
    )
    result: AnalyzeResult = poller.result()

    return result

if __name__ == "__main__":

    try:
        result = analyze_documents_output_in_markdown()
        print(f"Here's the full content in format {result.content_format}:\n")
        print(result.content)
    except Exception as error:
        print(f"An error occurred: {error}")
        raise