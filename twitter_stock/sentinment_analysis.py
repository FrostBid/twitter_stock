from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import nltk
import pandas as pd

nltk.download('vader_lexicon')


def sa(df):
    siaresults = []
    for txt in df['text']:
        score = SIA().polarity_scores(txt)
        score['Score'] = txt
        siaresults.append(score)
    df['Score'] = pd.DataFrame(siaresults)['compound']
    return df
