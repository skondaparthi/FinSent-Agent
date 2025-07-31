from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sentence_transformers import SentenceTransformer
import torch
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

def score(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    scores = torch.nn.functional.softmax(outputs.logits, dim=1)
    labels = ['negative', 'neutral', 'positive']
    return dict(zip(labels, scores[0].detach().numpy()))

def score_df(df):
    df["sent_scores"] = df['description'].apply(score)
    df['category'] = df['sent_scores'].apply(lambda x: max(x, key=x.get))
    return df


def embed(text):
    llm_tok = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    encoded = llm_tok.encode(text)
    return encoded
