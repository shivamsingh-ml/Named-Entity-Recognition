# Named Entity Recognition (NER) System

This repository contains a Named Entity Recognition (NER) system built using the spaCy NLP library. The current model is based on the retrained **spaCy's small English model (`en_core_web_sm`)** using the **CoNLL-2003** dataset.

## Dataset

The model has been trained on the **CoNLL-2003** dataset, which contains labeled entities for four entity types:

- **LOC**: Locations (e.g., cities, countries)
- **MISC**: Miscellaneous (e.g., nationalities, events)
- **ORG**: Organizations (e.g., companies, institutions)
- **PER**: Persons (e.g., people's names)

## Evaluation Results

The retrained model has achieved the following evaluation metrics:

| Entity Type | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| LOC         | 0.86      | 0.83   | 0.85     | 1668    |
| MISC        | 0.72      | 0.78   | 0.75     | 702     |
| ORG         | 0.76      | 0.72   | 0.74     | 1661    |
| PER         | 0.76      | 0.87   | 0.81     | 1617    |
| **Micro Avg** | 0.78      | 0.80   | 0.79     | 5648    |
| **Macro Avg** | 0.78      | 0.80   | 0.79     | 5648    |
| **Weighted Avg** | 0.79      | 0.80   | 0.79     | 5648    |

## Installation

To use this NER system, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ner-system.git
    cd ner-system
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Download the spaCy model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

## Usage

To test the model on sample text, run the following command:

```python
import spacy

nlp = spacy.load("path/to/your/retrained_model")
doc = nlp("Barack Obama was the 44th President of the United States.")

for ent in doc.ents:
    print(ent.text, ent.label_)
```

## Future Plans

I plan to continue improving the NER system by:

- Training medium, large, and transformer-based spaCy models on the CoNLL-2003 dataset.
- Fine-tuning the model for domain-specific datasets.
- Exploring optimization techniques to enhance model performance.

Stay tuned for future updates!

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request.



