# Financial Sentiment Analyzer with FinBERT

A Gradio-powered web application that performs sentiment analysis on financial headlines using FinBERT. The app classifies headlines as positive, negative, or neutral, making it useful for financial market sentiment analysis.

## Features

- **Custom Input Analysis**: Analyze your own financial headlines or news snippets
  
![ezgif-2-ff46e6894c](https://github.com/user-attachments/assets/bc5bf988-2267-4d80-b32c-6bb187766707)

- **Yahoo Finance Integration**: Automatically fetch and analyze latest headlines from Yahoo Finance RSS feeds

![chrome-capture-yahoo](https://github.com/user-attachments/assets/39040cdc-0e1f-4651-9cd4-2548b83126ab)

- **Color-Coded Results**: Easy-to-interpret sentiment results with visual indicators
  - 🟢 Green for positive sentiment
  - 🔴 Red for negative sentiment
  - ⚪ Gray for neutral sentiment

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation & Usage

1. Clone the repository:
```bash
git clone https://github.com/kimon2199/financial-sentiment-analyzer.git
cd financial-sentiment-analyzer
```

2. Install required packages:
```bash
pip3 install -r requirements.txt
```

3. Log into Hugging Face:
```bash
cp .env.example .env
```
Add your Hugging Face token to the .env file.

4. Start the application:
```bash
python3 -m financial_headline_analyzer.app
```

4. Open your web browser and navigate to the URL provided in the terminal (typically `http://127.0.0.1:7860`)

5. Use the application:
   - Enter custom headlines in the text area (one headline per line) and click "Analyze Sentiment on Custom Input"
   - Or click "Analyze Sentiment on Yahoo Finance Headlines" to fetch and analyze latest headlines

## Dependencies

- gradio - Web interface framework
- transformers - For FinBERT model
- torch - PyTorch for deep learning
- pandas - Data manipulation and analysis
- huggingface_hub - For logging into Hugging Face
- python-dotenv - For loading environment variables from .env file

## Acknowledgments

- [FinBERT](https://huggingface.co/yiyanghkust/finbert-tone) for the financial sentiment analysis model
- [Gradio](https://gradio.app/) for the web interface framework
