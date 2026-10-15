
# Decision Tree-Based Health Prediction

A beginner machine learning project using Python, pandas, and scikit-learn to explore health-category prediction using the DoctorContacts dataset.

## Overview

This project loads the DoctorContacts dataset, selects `educdec` as the input feature and `health` as the target variable, trains a decision tree classifier, and predicts a health category for a sample input.

## Technologies Used

- Python
- pandas
- scikit-learn

## Dataset

DoctorContacts dataset from the Rdatasets repository:

https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/DoctorContacts.csv

## Installation

Install Python 3, then install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python decision_tree.py
```

The program prints the predicted health category for the sample input.

## Current Limitations

- Uses a single input feature: `educdec`.
- Does not yet include a train/test split or model evaluation.
- Predictions have not been validated for clinical use.

## Future Improvements

- Add exploratory data analysis.
- Evaluate model performance on held-out data.
- Compare the decision tree with other classification algorithms.
- Document the dataset variables and their meanings.
