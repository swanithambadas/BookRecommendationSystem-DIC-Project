import pandas as pd
import numpy as np

def get_top_50(URB):
    avg_rating_df =URB.groupby('BookTitle')['BookRating'].mean().reset_index()
    avg_rating_df.rename(columns={'BookRating':'avg_rating'},inplace=True)
    num_rating_df = URB.groupby('BookTitle')['BookRating'].count().reset_index()
    num_rating_df.rename(columns={'BookRating':'num_ratings'},inplace=True)
    popular_df = num_rating_df.merge(avg_rating_df,on='BookTitle')
    popular_df_100 = popular_df[popular_df['num_ratings']>=100].sort_values('avg_rating',ascending=False).head(50)
    popular_df_image_100 = popular_df_100.merge(URB,on='BookTitle').drop_duplicates('BookTitle')[['BookTitle','BookAuthor','Image-URL-M','num_ratings','avg_rating']]
    selected_columns = popular_df_image_100[['Image-URL-M','BookTitle', 'BookAuthor', 'num_ratings','avg_rating' ]]
    top_50_books_list = selected_columns.values.tolist()
    return top_50_books_list