
from models.faiss_model import find_similar
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_headlines(query, faiss_index, df, k=5):
    """
    Summarizes the top k headlines based on the query.
    
    Args:
        query (str): The search query.
        faiss_index: The FAISS index for similarity search.
        df: DataFrame containing news articles.
        k: Number of similar articles to consider for summarization.
    
    Returns:
         tuple: (str, list) where the first element is the summary 
         of the top k headlines and the second is the list of similar results.
    """
       
    # Find similar results using the FAISS model
    similar_results = find_similar(query, faiss_index, df, k)

    # Input for the LLM
    context_text = ""
    for headline in similar_results:
        context_text += f"Title: {headline['title']}\nCategory: {headline['category']}\n\n"
  
    # Build prompt
    prompt = f"""You are a financial news analyst. 
    Based on the following headlines and descriptions, 
    write a 4-5 sentence summary of the general trend, sentiment, and topic.
    Say if it's worth investing in. {context_text}
    Summary:"""

    # Call OpenAI LLM (gpt-4 or gpt-3.5)
    client = openai.OpenAI(api_key=openai.api_key) # Initialize client with API key

    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=200
    )

    summary = response.choices[0].message.content
    # Return the summary and the list of similar results
    return summary, similar_results