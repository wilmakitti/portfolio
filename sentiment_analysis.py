import pandas as pd
from textblob import TextBlob
import spacy
import re

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Function to load and clean DataFrame
def load_and_clean_data(filepath):
    # Load the DataFrame
    dataframe = pd.read_csv(filepath, low_memory=False)
    # Drop rows with missing 'reviews.text'
    dataframe.dropna(subset=['reviews.text'], inplace=True)
    return dataframe

# Preprocessing function to clean text and remove stopwords
def preprocess_text(text):
    # Basic text cleaning
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    text = re.sub(r'\s+', ' ', text, re.I|re.A)
    text = text.strip()
    # Remove stopwords
    doc = nlp(text)
    clean_text = " ".join([token.text for token in doc if not token.is_stop])
    return clean_text

# Function for sentiment analysis using TextBlob
def analyze_sentiment(text):
    text = preprocess_text(text)
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Main function to process the data
def process_reviews(filepath):
    dataframe = load_and_clean_data(filepath)
    # Apply preprocessing and sentiment analysis, assign sentiment score to a new column
    dataframe['sentiment_score'] = dataframe['reviews.text'].apply(analyze_sentiment)
    # Assign sentiment label based on the sentiment score
    dataframe['sentiment_label'] = dataframe['sentiment_score'].apply(lambda score: 'positive' if score > 0 else 'negative' if score < 0 else 'neutral')
    return dataframe

# Use the function to process reviews
dataframe = process_reviews('amazon_product_reviews.csv')
# Example output
print(dataframe[['reviews.text', 'sentiment_score', 'sentiment_label']].head())


def predict_sentiment_from_input(review_text):
    # Assuming preprocess_text and analyze_sentiment are defined as before
    cleaned_text = preprocess_text(review_text)
    analysis = TextBlob(cleaned_text)
    sentiment_score = analysis.sentiment.polarity
    sentiment_label = 'positive' if sentiment_score > 0 else 'negative' if sentiment_score < 0 else 'neutral'
    return sentiment_label, sentiment_score

# User interaction loop
while True:
    user_input = input("Enter a product review index (0 to {}) to analyze its sentiment or press 'x' to exit: ".format(len(dataframe) - 1))
    if user_input.lower() == 'x':
        break
    try:
        index = int(user_input)
        if 0 <= index < len(dataframe):
            review_text = dataframe.loc[index, 'reviews.text']
            sentiment_label, sentiment_score = predict_sentiment_from_input(review_text)
            print(f"Review: {review_text}\nPredicted Sentiment: {sentiment_label}, Score: {sentiment_score}")
        else:
            print("Invalid index. Please enter a number within the provided range.")
    except ValueError:
        print("Please enter a valid number or 'x' to exit.")

