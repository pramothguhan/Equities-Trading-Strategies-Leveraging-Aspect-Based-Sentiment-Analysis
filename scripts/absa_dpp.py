# -*- coding: utf-8 -*-
"""Harith DPP.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AByryvQZ9cKap8DqqweqRUVc1cuazlqJ
"""

import pandas as pd
import spacy
import re

file_path = '/Users/Aman/Downloads/post_processing_csv_data_final.csv'
post_processing_data = pd.read_csv(file_path)

post_processing_data.head()

post_processing_data.columns

# Loads the spaCy English language model
nlp = spacy.load('en_core_web_sm')

# Defines a function to preprocess text
def preprocess_text_spacy(text):
    # Process the text using spaCy
    doc = nlp(text.lower())  # Convert to lowercase and process
    # Removes stopwords and punctuation, and lemmatize
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return ' '.join(tokens)

# Example usage on a single text
text = "This is an example sentence for testing the preprocessing pipeline."
cleaned_text = preprocess_text_spacy(text)
print(cleaned_text)

# Applys the preprocessing function to the 'cleaned_body' column
post_processing_data['cleaned_body'] = post_processing_data['cleaned_body'].apply(preprocess_text_spacy)

# Prints the first few rows to verify the changes
print(post_processing_data.head())

# Loads spaCy model
nlp = spacy.load("en_core_web_sm")

# Defines custom dictionary for WSB jargon (extend as needed)
wsb_jargon = {"calls", "puts", "tendies", "moon", "yolo", "diamond hands", "bagholder", "stonks"}

def extract_aspects_wsb(text):
    """
    Extracts aspects (stock tickers, jargon, and noun phrases) from WSB text.
    """
    # Extracts stock tickers (e.g., GME, TSLA)
    tickers = re.findall(r'\b[A-Z]{2,5}\b', text)

    # Processes text using spaCy
    doc = nlp(text)

    # Extracts noun chunks and WSB jargon
    aspects = set(tickers)
    for chunk in doc.noun_chunks:
        # Add noun phrases or WSB jargon to aspects
        if chunk.root.pos_ == "NOUN" or chunk.root.lemma_ in wsb_jargon:
            aspects.add(chunk.text)

    # Also adds standalone WSB jargon words
    for token in doc:
        if token.text.lower() in wsb_jargon:
            aspects.add(token.text)

    return list(aspects)

# Applies WSB-specific Aspect Extraction
post_processing_data['aspects'] = post_processing_data['cleaned_body'].apply(extract_aspects_wsb)

post_processing_data.head()

def transform_dataset(df):
    """
    Transforms the dataset by creating one row per aspect.
    """
    rows = []
    for _, row in df.iterrows():
        text = row['cleaned_body']
        sentiment = row['body_sentiment_class']
        aspects = row['aspects']
        date = row['date']
        for aspect in aspects:
            rows.append({'aspect': aspect, 'context': text, 'sentiment': sentiment, 'date': date})
    return pd.DataFrame(rows)

post_processing_data_v1 = transform_dataset(post_processing_data)

post_processing_data_v1.head()

sentiment_mapping = {'Positive': 0, 'Neutral': 1, 'Negative': 2}
post_processing_data['sentiment'] = post_processing_data_v1['sentiment'].map(sentiment_mapping)

post_processing_csv_data = post_processing_data_v1.to_csv('/Users/Aman/Downloads/post_processing_csv_data_final_v1.csv', index=False)