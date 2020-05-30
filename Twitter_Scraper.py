"""
This program is to scrape tweets on the real estate, 
or "der Immobilien" in German, from the Twitter network.
In this program, we specify the time period from 2017 April 24th to 28th. 
However, One might modify his/her own time periods.
After running this program, the excel and CSV files are produced
Programmer: Phuong V. Nguyen
phuong.nguyen@economics.uni-kiel.de
"""

from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
from IPython.display import display

def main():
    begin_date=dt.date(2017,4,24)
    end_date=dt.date(2017,4,28)
    limit=10
    lang='english'
    tweet=query_tweets('Immobilien', begindate=begin_date, enddate= end_date, limit=limit, lang=lang)
    df= pd.DataFrame(t.__dict__ for t in tweet)
    display(df.head(5).T)
    df.to_excel("test_Tweet_Immobilien.xlsx")  
    df.to_csv("test_Tweet_Immobilien.csv")

if __name__ == '__main__':
    main()
