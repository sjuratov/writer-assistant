# Writing Assistant Project

This repository contains the code for extracting content from scientific paper and creating an abstract based on it. Project is using Azure Document Intelligence for content extraction to markdown format. It is then using Azure OpenAI for creation of the abstract.

## Features

- **Content extraction**: Extract content from PDF documents in markdown format.
- **Abstract generation**: Creates document abstract using specific template.
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

Run Python script to create an abstract. Update main.py with relevant URL or pass URL to PDF document as an optional command line parameter.

```bash
python main.py [url]
```

## Running Project Interactively 

To run project interactively, there are two options:

- **Jupyter Notebook**: Open and run *main.ipynb*
- **Streamlit App**: Run command below. This will open new browser window

```bash
streamlit run streamlit_app.py
```

## One-click deploy

### Prerequisites

To use this solution, you will need access to an [Azure subscription](https://azure.microsoft.com/free/) with permission to create resource groups and resources.

![Deploy to Azure](https://aka.ms/deploytoazurebutton)