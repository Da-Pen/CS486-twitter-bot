## Project Overview
We created a Twitter bot with two different machine learning models:
1. LSTM (Long Short-Term Memory)
2. Transformer model (GPT-2)

The goal of each model is to generate Tweets that are grammatically correct, and transfer the style of the Twitter user that they were trained on.

## Sample Generated Tweets
### From the GPT-2 Model
#### Trained on Trump Tweets
![GPT-2 Trump 1](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/README-images/GPT2-Trump-1.jpg)
![GPT-2 Trump 2](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/README-images/GPT2-Trump-2.jpg)
[see more](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/GPT-2/trump_output)

#### Trained on News Organization Tweets
![GPT-2 News 1](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/README-images/GPT2-News-1.jpg)
![GPT-2 News 2](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/README-images/GPT2-News-2.jpg)
[see more](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/GPT-2/news_output)

### From the LSTM Model
#### Trained on Trump Tweets
![LSTM Trump 1](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/README-images/LSTM-Trump-1.jpg)
![LSTM Trump 2](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/README-images/LSTM-Trump-2.jpg)
[see more](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/LSTM/test-outputs/LSTM_trump_test_output)

#### Trained on News Organization Tweets
![LSTM News 1](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/README-images/LSTM-News-1.jpg)
![LSTM News 2](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/README-images/LSTM-News-2.jpg)
[see more](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/LSTM/test-outputs/LSTM_news_test_output)

## Findings
Overall, we found that the GPT-2 model generated much more coherent text, and was slightly better at generating text that matched the style of the original Twitter user. The methodology and results details can be found in our [Project Report](https://github.com/Da-Pen/CS486-twitter-bot/blob/main/Report.pdf).

## Tools used
- Python
- Keras
- Jupyter Notebooks
- Google Colab
- Tweepy API (to collect data)
