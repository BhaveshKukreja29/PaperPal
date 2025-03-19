# PaperPal

PaperPal is a command-line research paper reading assistant designed to help users extract and analyze content from academic documents. It supports various file formats, including PDFs, DOCX, and TXT, making research more efficient and accessible.

## Features
- **Multi-format support**: Extracts text from PDF, DOCX, and TXT files.
- **Quick text extraction**: Retrieves readable text efficiently.
- **Error handling**: Identifies invalid file paths and permission issues.

## Installation

Ensure you have Python 3.8+ installed. Then, clone the repository and install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage
Run the program from the command line:

```sh
python main.py
```

Follow the prompts to provide a file path, and PaperPal will extract the text for you.

## Dependencies
- `pymupdf` (for PDF parsing)
- `python-docx` (for DOCX support)

## Future Improvements
- **Summarization**: Add support for research paper summarization.
- **Keyword Extraction**: Identify key topics from documents.
- **Citations Handling**: Extract and analyze references from academic papers.
