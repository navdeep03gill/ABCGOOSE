# Flask-ML-App

## Overview

A Flask-based API service for predicting if two words are synonyms using a trained logistic regression model.

## Running the App

1. Create a virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the tester

   ```
   cd tests
   python3 test_model.py
   ```

Example input:

```json
{
  "word1": "absolute",
  "word2": "downright"
}
```

Example output:

```
{'confidence': 0.9928566424289941, 'is_synonym': True, 'result': 'synonyms', 'word1': 'absolute', 'word2': 'downright'}
```
