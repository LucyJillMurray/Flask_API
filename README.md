# Setup

## Create a virtual environment:
```bash
python -m venv venv
```

## Activate the virtual environment:
- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- On Unix or macOS:
  ```bash
  source venv/bin/activate
  ```

## Install dependencies using `requirements.txt`
```bash
pip install -r requirements.txt
```

## Download NLTK data in Python
```bash
python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('averaged_perceptron_tagger')
>>> exit()
```

## Run the application
```bash
python sentiment.py
```
This should output a link.

## Test the API using Postman
- Method: `POST`
- URL: `<link>/analyse`
- Body (raw JSON):
  ```json
  {"text":"I love dogs"}
  {"text":"I like this API"}
  {"text":"I somewhat dislike this API"}
  {"text":"Not bad, could be better."}
  ```

## Run the tests
```bash
python -m unittest test_app.py