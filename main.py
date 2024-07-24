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
    python main.py [url]

    Set the environment variables with your own values before running the sample:
    1) url - points to PDF version of scientific paper. This is now an optional command line argument.
"""

import time
import colorama
from colorama import Fore
import sys

from analyze_document_use_document_intelligence import analyze_documents_output_in_markdown
from write_assistant import create_document

colorama.init(autoreset=True)

start_time = time.time()

# Check if a URL is provided as a command line argument
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = "https://www.nature.com/articles/s41586-024-07701-9.pdf"

print(Fore.GREEN + f"Analyzing following document --> {url}")

try:
    result = analyze_documents_output_in_markdown(url)
    analysis_time = time.time() - start_time
    print(Fore.GREEN + f"Analysis completed in {analysis_time:.2f} seconds.")
except Exception as error:
    print(Fore.RED + f"An error occurred: {error}")
    raise

try:
    print(Fore.GREEN + "Creating an abstract of the document ...")
    abstract_start_time = time.time()
    result = create_document(result.content)
    abstract_time = time.time() - abstract_start_time
    print(Fore.GREEN + f"Analysis completed in {abstract_time:.2f} seconds.")
    print(f"Here's the abstract of the paper:\n")
    print(result.choices[0].message.content)
except Exception as error:
    print(Fore.RED + f"An error occurred: {error}")
    raise