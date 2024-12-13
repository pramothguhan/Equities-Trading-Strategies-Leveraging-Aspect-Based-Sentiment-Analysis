# Equities-Trading-Strategies-Leveraging-Aspect-Based-Sentiment-Analysis
# Equities Trading Strategy Using Sentiment Analysis

This project demonstrates the development of an algorithmic trading strategy by integrating sentiment analysis of Reddit posts from the WallStreetBets subreddit with traditional market indicators. The goal is to leverage advanced NLP models to predict sentiment and combine it with financial indicators to enhance trading decisions.

## Key Features
- **Sentiment Analysis:** Utilizes NLP models like BERT, GPT-2, and GPT-Neo to classify sentiments as Positive, Neutral, or Negative.
- **Trading Strategy:** Implements a trend-following strategy using sentiment predictions and market indicators (e.g., OHLC, RSI, moving averages).
- **Performance Evaluation:** Achieved an 8.87% return during 18 months of back-testing using GPT-Neo predictions.

## Project Structure
- `data/`: Contains the preprocessed Reddit posts and financial data.
- `models/`: Includes fine-tuned models for sentiment classification.
- `scripts/`: Python scripts for data preprocessing, model training, and back-testing.
- `results/`: Performance metrics, plots, and back-testing outcomes.

## Technologies Used
- **Python**: For data preprocessing, modeling, and trading strategy implementation.
- **Hugging Face Transformers**: For NLP models.
- **YFinance API**: For retrieving financial data.
- **Backtrader**: For simulating trading strategies.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the data preprocessing script:
   ```bash
   python scripts/preprocess_data.py
   ```
4. Train the sentiment model:
   ```bash
   python scripts/train_model.py --model_name gpt-neo
   ```
5. Back-test the trading strategy:
   ```bash
   python scripts/backtest_strategy.py
   ```

## Results
- The strategy achieved an 8.87% return over 18 months.
- Metrics such as Sharpe Ratio and Returns-to-Drawdown ratio were used for evaluation.

## Contributing
Contributions are welcome! Feel free to fork the repository, open an issue, or submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- **Hugging Face** for the transformer models.
- **WallStreetBets Subreddit** for providing the dataset.
- **Backtrader** for the trading simulation framework.
