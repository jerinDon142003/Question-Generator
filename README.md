
# PDF Question Generator

This Python script extracts text from a PDF file and generates simple questions based on keyword detection. It's a basic prototype for building automated question generation systems using textual content from documents.

## Features

- Extracts text from all pages of a PDF file.
- Scans for sentences containing question-oriented keywords (e.g., who, what, when).
- Generates basic questions from identified sentences.
- Outputs the generated questions to the console.

##  Requirements

- Python 3.x
- [PyPDF2](https://pypi.org/project/PyPDF2/)

Install the required package using pip:

```bash
pip install PyPDF2
```

## Usage

1. Place your target PDF file (e.g., `sample.pdf`) in the same directory as the script.
2. Run the script:

```bash
python your_script_name.py
```

3. Example usage within the script:

```python
pdf_file = "sample.pdf"
questions = generate_questions(pdf_file)

for question in questions:
    print(question)
```

## Notes

- The current implementation uses simple keyword matching to detect question-worthy sentences.
-  You can improve the accuracy by integrating NLP libraries like `spaCy`, `transformers`, or `nltk` for named entity recognition, sentence parsing, or contextual question generation.

## File Structure

```
project_folder/
│
├── sample.pdf             # Example input PDF file
├── your_script_name.py    # The script containing generate_questions()
├── README.md              # Project documentation
```

##  Future Enhancements

- Use NLP for better keyword extraction and sentence parsing.
- Generate WH-style questions using dependency parsing.
- Export generated questions to a `.txt` or `.csv` file.

