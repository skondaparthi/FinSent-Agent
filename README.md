# FinSent-Agent

A sophisticated financial sentiment analysis AI-agent that fetches real-time market news, analyzes sentiment using FinBERT, and provides AI-powered summaries to help with investment decisions.

## 🚀 Features

- **Real-time News Fetching**: Automatically retrieves latest trending financial news from multiple sources
- **Advanced Sentiment Analysis**: Uses FinBERT (Financial BERT) model for accurate financial sentiment scoring and embedding
- **Semantic Search**: FAISS-powered similarity search to find relevant articles
- **AI-Powered Summaries**: OpenAI GPT integration for intelligent market sentiment summaries
- **Interactive Queries**: Ask specific questions about market sentiment and get tailored insights

## 🛠️ Technology Stack

- **Python 3.11+**
- **Transformers & FinBERT**: Financial sentiment analysis
- **FAISS**: Vector similarity search for semantic matching
- **OpenAI GPT**: Advanced natural language summarization
- **Sentence Transformers**: Text embedding generation
- **pandas**: Data manipulation and analysis
- **News API**: Real-time news data ingestion

## 📋 Prerequisites

- Python 3.11 or higher
- OpenAI API key
- News API key

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/skondaparthi/FinSent-Agent.git
cd FinSent-Agent
```

### 2. Set Up Virtual Environment
```bash
python3 -m venv finsentenv
source finsentenv/bin/activate  # On macOS/Linux
# or
finsentenv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

### 5. Run the Agent
```bash
python main.py
```

## 📁 Project Structure

```
FinSent-Agent/
├── main.py                # Main application entry point
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── Finsent.ipynb          # Google Colab playground (experimental notebook)
├── ingest/
│   └── news_api.py        # News data ingestion module using NewsAPI
├── models/
│   ├── finbert_model.py   # FinBERT sentiment analysis
│   ├── faiss_model.py     # FAISS similarity search
│   └── llm_model.py       # OpenAI integration
└── README.md              # This file
```

## 🔧 Configuration

### API Keys Setup

1. **OpenAI API Key**: Get your OpenAI key at [OpenAI Platform](https://platform.openai.com/api-keys)
2. **News API Key**: Get NewsAPI key at [NewsAPI.org](https://newsapi.org/)

Add these to your `.env` file:
```env
OPENAI_API_KEY=sk-your-actual-openai-key
NEWS_API_KEY=your-actual-news-api-key
```

## 💡 Usage Examples

### Basic Usage
Run the script and enter your query when prompted:
```
Enter a query to summarize market news: Tesla stock analysis
```

### Example Queries
- "Should I invest in Tesla right now?"
- "AI market sentiment analysis"
- "Cryptocurrency market trends"
- "Tech stock outlook"
- "Federal Reserve interest rate impact"

## 🧠 How It Works

1. **News Ingestion**: Fetches latest financial news from News API
2. **Sentiment Scoring**: FinBERT analyzes each article for financial sentiment
3. **Embedding Generation**: Creates vector embeddings for semantic search
4. **FAISS Indexing**: Builds searchable index for similarity matching efficiently
5. **Query Processing**: Finds articles relevant to your specific query
6. **AI Summarization**: OpenAI GPT generates comprehensive market insights

## 📊 Output Example

```
Summary of Market News:
The current market sentiment surrounding Tesla appears predominantly positive, despite some underlying concerns. Recent headlines highlight optimism about potential investment returns, with Elon Musk suggesting that a $150,000 investment could lead to millionaire status. Additionally, there's a recognition that Tesla is evolving beyond just a car manufacturer, which could open up new revenue streams. However, analysts express caution regarding dwindling sales and critical revenue sources, indicating a mixed outlook. Given this context, investing in Tesla could be worthwhile for those who believe in its long-term vision and innovations, but potential investors should remain aware of the challenges the company faces in the short term.
```

## 🔍 Advanced Features

- **Semantic Search**: Find articles similar to your specific interests
- **Multi-source Analysis**: Aggregates sentiment from diverse news sources
- **Customizable Analysis**: Adjust the number of articles analyzed (k parameter)
- **Real-time Processing**: Always uses the latest available market news

## 🚨 Troubleshooting

### Common Issues

1. **Missing API Keys**: Ensure your `.env` file contains valid API keys
2. **Package Conflicts**: Use a fresh virtual environment
3. **FAISS Installation**: On some systems, use `pip install faiss-cpu==1.10.0` (M-Series Macs)
4. **Tokenizer Warnings**: These are handled automatically in the code

### Error Solutions

- **ImportError**: Run `pip install -r requirements.txt` in your virtual environment
- **API Errors**: Check your API keys and quotas
- **No Articles Found**: Try broader search terms or check News API status, or change date so that it is within one month of current date (NewsAPI limitation)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **FinBERT**: For financial sentiment analysis capabilities
- **FAISS**: For efficient similarity search
- **OpenAI**: For advanced text generation
- **News API**: For real-time news data

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Review the documentation for each component

---

**Happy Trading! 📈**
