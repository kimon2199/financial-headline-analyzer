__version__ = "1.0.0"
__author__ = "Kimon Softas"

# Importing key functions for easy access at the package level
from .sentiment_analysis import analyze_sentiment
from .yahoo_finance import get_yahoo_finance_headlines
from .styles import custom_css

# Define a list of all public objects in this package
__all__ = ["analyze_sentiment", "custom_css", "get_yahoo_finance_headlines"]
