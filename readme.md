# Content Generation Assistant

This repository contains the code for generating new content from existing documents. Type of newly generated content is driven by predifined templates (system prompt), and selected during runtime.

Project is using Azure Document Intelligence for text extraction to markdown format. Extracted text is then sent, together with relevant system prompt, to Azure OpenAI for generation of new content.

At the moment, PDF is the only supported input document format.

## Features

- **Text extraction**: Extract content from documents in markdown format.
- **Content generation**: Creates new document using specific template.
- **Error Handling**: Includes generic error handling to catch and report issues during the analysis process.
- **Performance Metrics**: Measures and reports the time taken to perform the content extraction and abstract generation.
- **Abstract output**: Created abstract will be saved to 'abstracts' folder

## Getting Started

This project has been created using Python 3.12.2.

To get started with this project, clone the repository to your local machine:

```bash
git clone https://github.com/sjuratov/writer-assistant
```

Create and activate virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate.bat #On Windows
```

Install Python libraries

```bash
pip install -r requirements.txt
```

Run Python script to create an abstract. Make sure to provide parameter, which is path to local PDF document.

```bash
python main.py [path_to_local_PDF_document]
```

Copy *.env.example* to *.env* and update environment variables as appropriate.


## Running Project Interactively 

To run project interactively, there are two options:

- **Jupyter Notebook**: Open and run *main.ipynb*
- **Streamlit App**: Run command below. This will open new browser window

```bash
streamlit run streamlit_app.py
```

## One-click deploy

### Prerequisites

To use this solution, you will need access to an [Azure subscription](https://azure.microsoft.com/free/) with permissions to create resource group and resources. Following resources will be created:

- Azure AI services multi-service account
- Azure OpenAI
- Azure Container App
- Azure Container Registry

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fsjuratov%2Fwriter-assistant%2Fmain%2Finfra%2Fmain.json)

*Note: Make sure to update .env file after deployment has completed.*