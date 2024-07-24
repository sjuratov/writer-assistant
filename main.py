# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: main.py

DESCRIPTION:
    This sample demonstrates how to write an abstract based on scientific paper.

USAGE:
    python main.py

    Set the environment variables with your own values before running the sample:
    1) url - points to PDF version of scientific paper.
"""

import time
import colorama
from colorama import Fore

from analyze_document_use_document_intelligence import analyze_documents_output_in_markdown
from write_assistant import create_document

colorama.init(autoreset=True)

print(Fore.GREEN + "Document analysis is in progress...")

start_time = time.time()

#url = "https://cob.silverchair-cdn.com/cob/content_public/journal/jcs/131/14/10.1242_jcs.186254/8/jcs186254.pdf?Expires=1724822537&Signature=SEdkl~B~m8Z8AeMboguMRS4WgAeHACgmN4CEb5bsbtfjN1mIIg2sjLVwkKaB0o5Ys1YGTut8jZjjHqPY6eZtnWr8CDqBrRLGb-N6QQzp7i9qBQBE1fOk86749~2o8gNWkITatoCfDGheDwMcbJo-IrCy4xB1NjbfMdhg1xhRIJDS8aErZsuS2p4nm6m28ycSk-qIB9BxIBp~NIMMRlWb90WmaI~oX2fuspGxmvsFlLni5m5fXJsZxH-ea5mxucnHXiVX2XZOoFwMW5rhUlf6n8oveiCPvHrPusddL6LsLfRHrDNlIj-EdtRcmwEu7PZSp0V~R4UnHXx1ram7zWk1UQ__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA"
url = "https://www.nature.com/articles/s41586-024-07701-9.pdf"

try:
    result = analyze_documents_output_in_markdown(url)
    analysis_time = time.time() - start_time
    print(Fore.GREEN + f"Analysis completed in {analysis_time:.2f} seconds.")
except Exception as error:
    print(Fore.RED + f"An error occurred: {error}")
    raise

try:
    print(Fore.GREEN + "Creating an abstract of the document ...")
    result = create_document(result.content)
    print(f"Here's the abstract of the paper:\n")
    print(result.choices[0].message.content)
except Exception as error:
    print(Fore.RED + f"An error occurred: {error}")
    raise