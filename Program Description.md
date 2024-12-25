# Word Sense Disambiguation Using Decision List Classifier

## Overview
This project implements a Decision List Classifier for Word Sense Disambiguation (WSD), focusing on the word "line" in different contexts. The classifier uses features inspired by Yarowsky’s method to effectively learn from labeled training data and assign the correct sense to ambiguous words in test data.

## Key Features
- **Training with XML Data:** Learns a decision list from annotated examples in `line-train.xml`.
- **Context-Based Classification:** Classifies the sense of the word "line" in test sentences based on the learned decision list.
- **Output:** Generates a decision list log for debugging and outputs predicted sense tags for test sentences.
- **Performance Metrics:** Includes accuracy calculation and confusion matrix generation to evaluate classifier performance.

## How It Works
1. **Training:**
   - The program reads `line-train.xml`, which contains examples of the word "line" annotated with senses (e.g., "phone line" or "product line").
   - A decision list is generated based on contextual features.

2. **Testing:**
   - The decision list is applied to classify the sense of "line" in sentences from `line-test.xml`.
   - Predicted sense tags are compared with the gold standard answers in `line-answers.txt`.

3. **Evaluation:**
   - Calculates accuracy by comparing predicted and actual senses.
   - Generates a confusion matrix to analyze classification performance.

## Usage
Run the program from the command line:

```bash
python decision-list.py line-train.xml line-test.xml my-decision-list.txt > my-line-answers.txt
```

- **Input Files:**
  - `line-train.xml`: Contains labeled examples for training.
  - `line-test.xml`: Contains test sentences to classify.
- **Output Files:**
  - `my-decision-list.txt`: Decision list log for debugging.
  - `my-line-answers.txt`: Predicted sense tags in the required format.

### Additional Evaluation Script
To evaluate the performance of the classifier:

```bash
python scorrer.py my-line-answers.txt line-answers.txt
```

This script calculates accuracy and generates a confusion matrix for detailed analysis.

## Data Description
- **line-train.xml:** Annotated training data with sense labels for the word "line."
- **line-test.xml:** Test data without sense labels.
- **line-answers.txt:** Gold standard sense tags for test sentences.

## Dependencies
Ensure the following Python libraries are installed:
- `pandas`
- `bs4`
- `re`

Install dependencies using pip:

```bash
pip install pandas beautifulsoup4
```

## Repository Structure
- `decision-list.py`: Main script for training and testing the classifier.
- `scorrer.py`: Evaluation script for accuracy and confusion matrix.
- `line-data/`: Directory containing the XML data files.

## Technical Highlights
- **Contextual Features:** Incorporates contextual clues for disambiguation.
- **Decision List:** Implements a robust method for learning word senses based on training data.
- **Performance Analysis:** Includes scripts for accuracy measurement and confusion matrix generation.

## Example
To classify senses and evaluate the model:

1. Train and test the classifier:
   ```bash
   python decision-list.py line-train.xml line-test.xml my-decision-list.txt > my-line-answers.txt
   ```

2. Evaluate performance:
   ```bash
   python scorrer.py my-line-answers.txt line-answers.txt
   ```

## References
- Yarowsky, D. "Unsupervised Word Sense Disambiguation Rivaling Supervised Methods." Proceedings of the ACL.
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/)


