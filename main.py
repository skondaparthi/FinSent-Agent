import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from ingest.news_api import *
from models.finbert_model import *
from models.faiss_model import *
from models.llm_model import *

def main():
    # Web search for news articles
    print("Fetching latest market news...")
    print("This may take a few seconds...")
    news_df = find_news()
    news_df = score_df(news_df)
    news_df = embed_df(news_df)
    print("News articles fetched and processed.")

    # Create FAISS index for similarity search
    faiss_index = create_index(news_df)

    # Summarize the headlines using the FAISS index
    print("Summarizing market news...")
    print("This may take a few seconds...")
 
    if not news_df.empty:
        print(f"Found {len(news_df)} articles.")
    else:
        print("No articles found.")

    query = input("Enter a query to summarize market news (e.g., 'Latest updates on Tesla'): ")
    if not query:
        query = "Should I invest in Tesla right now? What is the market sentiment towards it?"

    summary, _ = summarize_headlines(
        userquery=query,
        query=query,
        faiss_index=faiss_index,
        df=news_df,
        k=5 
    )

    print("Summary of Market News:")
    print(summary)


    

if __name__ == "__main__":
    main()