from ingest.news_api import *
from models.finbert_model import *
from models.faiss_model import *
from models.llm_model import *

def main():
    news_df = find_news()
    news_df = score_df(news_df)
    news_df = embed_df(news_df)
    print(news_df.head())

    #Create FAISS index for similarity search
    faiss_index = create_index(news_df)

    summary, _ = summarize_headlines(
        query="AI in finance",
        faiss_index=faiss_index,
        df=news_df,
        k=5 
    )

    print("Summary of Market News:")
    print(summary)


    

if __name__ == "__main__":
    main()