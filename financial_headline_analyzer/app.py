import gradio as gr
import pandas as pd
from financial_headline_analyzer import analyze_sentiment, custom_css, get_yahoo_finance_headlines

def get_headlines():
    # Get the headlines from Yahoo Finance RSS feed
    articles = get_yahoo_finance_headlines()
    return [article['title'] for article in articles]

# Define the Gradio layout
with gr.Blocks() as demo:
    gr.Markdown("## Financial Headline Sentiment Analyzer")
    gr.Markdown(
        "Input a list of financial headlines (one per line) and click **Analyze Sentiment** "
        "to see whether each headline is positive, negative, or neutral."
    )

    with gr.Row():
        headlines_input = gr.Textbox(
            placeholder="Enter headlines, one per line...",
            lines=5,
            label="Headlines Input"
        )

    gr.HTML(custom_css)  # Inject custom CSS into the app

    analyze_ci_btn = gr.Button("Analyze Sentiment on Custom Input", elem_classes=["custom-btn"])
    analyze_y_btn = gr.Button("Analyze Sentiment on Yahoo Finance Headlines", elem_classes=["custom-btn-yahoo"])

    sentiment_output = gr.Dataframe(
        headers=["Sentiment", "Headline"],
        row_count=5,
        col_count=2,
        label="Sentiment Analysis Results"
    )

    # Function to apply sentiment analysis and colorize the output
    def analyze_and_colorize_sentiment(headlines):
        sentiment_results = analyze_sentiment(headlines)

        # Convert the results into a DataFrame
        df = pd.DataFrame(sentiment_results, columns=["Sentiment", "Headline"])

        # Apply color based on sentiment
        def color_sentiment(val):
            if val == "Positive":
                return 'color: green'
            elif val == "Negative":
                return 'color: red'
            else:  # neutral
                return 'color: gray'

        # Apply the color styling to the "Sentiment" column
        styled_df = df.style.applymap(color_sentiment, subset=["Sentiment"])

        return styled_df

    # Function to get Yahoo headlines and analyze them
    def analyze_yahoo_headlines():
        headlines = get_headlines()
        return analyze_and_colorize_sentiment(headlines)

    # Connect the button to the function
    analyze_ci_btn.click(analyze_and_colorize_sentiment, inputs=headlines_input, outputs=sentiment_output)
    analyze_y_btn.click(analyze_yahoo_headlines, inputs=None, outputs=sentiment_output)

# Launch Gradio interface
if __name__ == "__main__":
    demo.launch()
