# Equities Trading Strategy Using Sentiment Analysis

This project demonstrates the development of an algorithmic trading strategy by integrating sentiment analysis of Reddit posts from the WallStreetBets subreddit with traditional market indicators. Using advanced NLP models, the project aims to enhance trading decisions by combining sentiment predictions with financial metrics.

## Key Features
- **Sentiment Analysis:** Utilizes transformer-based models like BERT, GPT-2, and GPT-Neo to classify sentiments as Positive, Neutral, or Negative.
- **Trading Strategy:** Implements a trend-following strategy using sentiment predictions and market indicators such as OHLC, RSI, and moving averages.
- **Performance Evaluation:** Achieved an 8.87% return over 18 months of back-testing, showcasing the integration of sentiment-driven insights with traditional trading metrics.

## Project Structure
- `data/`: Contains cleaned Reddit posts and financial data.
- `scripts/`: Python scripts for data preprocessing, model training, and back-testing.
- `results/`: Performance metrics, plots, and back-testing outcomes.
- `documentation/`: Includes the project documentation and detailed reports.

## Technologies Used
- **Python**: For data preprocessing, modeling, and trading strategy implementation.
- **Hugging Face Transformers**: For implementing NLP models.
- **YFinance API**: For retrieving historical financial data.
- **Backtrader**: For simulating and back-testing trading strategies.

## Results
- **Sentiment Classification:** GPT-Neo outperformed other models, achieving the highest accuracy (88%) in predicting sentiments.
- **Trading Strategy Performance:** The trading strategy yielded an 8.87% return during 18 months of back-testing.
- **Metrics Evaluated:** Metrics like Sharpe Ratio and Returns-to-Drawdown ratio validate the profitability and resilience of the strategy.

## Documentation and Resources
- **Project Documentation:** [View Documentation](./documentation/project_report.pdf)
- **Video Presentation:** [Watch Video](https://northeastern-my.sharepoint.com/personal/anand_ha_northeastern_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fanand%5Fha%5Fnortheastern%5Fedu%2FDocuments%2FRecordings%2FMeeting%20in%20NLP%20project%2D20241212%5F214445%2DMeeting%20Recording%2Emp4&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ee3911246%2D0665%2D4489%2Da1ab%2D661e690ecde1)

## Contributing
Contributions are welcome! Feel free to fork the repository, open an issue, or submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- **Hugging Face** for providing transformer models.
- **WallStreetBets Subreddit** for the dataset.
- **Backtrader** for the trading simulation framework.

## References
- Chen, Y., Li, X., & Zhang, Z. (2022). Aspect-based Sentiment Analysis in Financial News. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP).
- Kumar, R., & Shankar, A. (2021). Sentiment Analysis on Reddit’s WallStreetBets. Stanford CS229 Machine Learning Final Projects.
- Liu, J., Zhao, R., & Xu, Y. (2019). Multimodal Aspect-based Sentiment Analysis: Integrating Text and Image Data. In Proceedings of the 2019 Conference on Computer Vision and Pattern Recognition (CVPR).
- Zhang, L., Wang, Y., & Liu, H. (2020). Deep Q-Networks for Stock Trading with Composite Sentiment Scores. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL).

