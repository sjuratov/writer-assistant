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
    python main.py [document]

    Set the environment variables with your own values before running the sample:
    1) document - points to PDF version of scientific paper e.g. documents/academic_paper.pdf
"""

import time
import colorama
from colorama import Fore
import sys
import os

from src.modules.analyze_document_use_document_intelligence import analyze_documents_output_in_markdown
from src.modules.write_assistant import create_document

colorama.init(autoreset=True)

def write_abstract_to_file(abstract, file_name):
    # Check if the abstracts directory exists, if not create it
    abstracts_directory = "abstracts"
    if not os.path.exists(abstracts_directory):
        os.makedirs(abstracts_directory)

    try:
        with open(f"{abstracts_directory}/{file_name}", "w") as abstract_file:
            abstract_file.write(abstract)
    except Exception as error:
        print(Fore.RED + f"An error occurred: {error}")
        raise

start_time = time.time()

# Check if a document is provided as a command line argument
if len(sys.argv) > 1:
    document = sys.argv[1]
    if not os.path.isfile(document):
        print(Fore.RED + f"Document {document} not found")
        sys.exit()
else:
    print(Fore.RED + f"Please provide path to input document")
    sys.exit()

print(Fore.GREEN + f"Analyzing following document --> {document}")

try:
    result = analyze_documents_output_in_markdown(document)
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
    file_name_without_extension = os.path.splitext(os.path.basename(document))[0]
    abstract_file_name = f"abstract_{file_name_without_extension}.md"
    write_abstract_to_file(result.choices[0].message.content, abstract_file_name)
except Exception as error:
    print(Fore.RED + f"An error occurred: {error}")
    raise