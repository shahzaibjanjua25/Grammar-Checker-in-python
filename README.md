﻿# Verb Tense Correction Tool

The **Verb Tense Correction Tool** is a Python script that corrects verb tenses in a given text. It utilizes natural language processing techniques, part-of-speech tagging, lemmatization, and spell checking to ensure accurate and grammatically correct verb forms. The tool handles regular and irregular verbs, providing a reliable solution for writers and language enthusiasts.

## Features

- **Verb Tense Correction:** Corrects verb tenses to ensure consistency and accuracy in written content.
- **Irregular Verb Handling:** Handles irregular verb forms, converting them to the appropriate tense.
- **Spell Checking:** Checks and corrects spelling errors in the text for enhanced readability.
- **Paragraph-level Processing:** Corrects verbs within individual paragraphs, preserving the structure of the input text.

## Prerequisites

- **Python 3.x**
- **Libraries:**
  - [spaCy](https://spacy.io/): 'pip install spacy'
  - [NLTK](https://www.nltk.org/): 'pip install nltk'
  - [SpellChecker](https://pypi.org/project/pyspellchecker/): 'pip install pyspellchecker'

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/shahzaibjanjua25/Grammar-Checker-in-python.git
   cd verb-tense-correction
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script:**
   ```bash
   python verb_tense_correction.py
   ```

   Replace 'verb_tense_correction.py' with the actual filename if different.

4. **Input:**
   Provide the input text when prompted. The tool processes the text and displays the corrected output.

## Customization

- **Irregular Verbs:** Customize the 'irregular_words' dictionary in the script to include specific irregular verbs and their forms.

```python
irregular_words = {
    # Example: 'arise': ['arise', 'arose', 'arisen', 'arising'],
    # Add more irregular verbs as needed
}
```

## Example

```plaintext
Input:
"Your input text goes here. It can contain multiple paragraphs. Each paragraph will be processed individually."

Output:
"Your input text goes here. It can contain multiple paragraphs. Each paragraph will be processed individually."
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please [open an issue](https://github.com/shahzaibjanjua25/Grammar-Checker-in-python.git/issues) or [create a pull request](https://github.com/shahzaibjanjua25/Grammar-Checker-in-python.git/pulls).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
