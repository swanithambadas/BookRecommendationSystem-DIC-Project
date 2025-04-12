import pandas as pd
from scipy.sparse.linalg import svds
from scipy.sparse import csr_matrix
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

# Assuming 'top_prediction_per_book' is your DataFrame
#top_prediction_per_book = None

def get_recommendations(URB, user_id):
    try:
        # Attempt to convert user_id to an integer
        user_id_int = int(user_id)
    except ValueError:
        # Handle the case where conversion fails
        return "Invalid user ID. Please enter a valid number."
    
    if not 1 <= user_id_int <= 290:
        raise ValueError("User ID must be between 1 and 291.")
    
    global top_prediction_per_book
    counts1 = URB['UserID'].value_counts()
    ratings_explicit = URB[URB['UserID'].isin(counts1[counts1 >= 100].index)]
    ratings_matrix = ratings_explicit.pivot(index='UserID', columns='ISBN', values='BookRating').fillna(0)
    sparse_ratings_matrix = csr_matrix(ratings_matrix)
    U, sigma, Vt = svds(sparse_ratings_matrix, k = 30)
    sigma = np.diag(sigma)
    all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) 
    preds_df = pd.DataFrame(all_user_predicted_ratings, columns = ratings_matrix.columns)
    userID = ratings_matrix.iloc[user_id_int-1, :].name
    sorted_user_predictions = preds_df.iloc[user_id_int].sort_values(ascending=False)
    user_data = ratings_explicit[ratings_explicit.UserID == (userID)]
    book_data = ratings_explicit[ratings_explicit.ISBN.isin(user_data.ISBN)]
    user_full_info = user_data.merge(book_data)
    recommendations = (ratings_explicit[~ratings_explicit['ISBN'].isin(user_full_info['ISBN'])]
    .merge(pd.DataFrame(sorted_user_predictions).reset_index(), how = 'left', left_on = 'ISBN',right_on = 'ISBN'))  .rename(columns = {user_id_int: 'Predictions'})
    recommendations['predicted_rating'] = recommendations['Predictions'] * 10
    unique_predictions = recommendations['predicted_rating'].unique()
    unique_predictions_sorted = sorted(unique_predictions, reverse=True)
    top_10_unique_predictions = unique_predictions_sorted[:10]
    top_10_predictions = recommendations[recommendations['predicted_rating'].isin(top_10_unique_predictions)]
    top_prediction_per_book = top_10_predictions.sort_values('predicted_rating', ascending=False).drop_duplicates(['BookTitle'])
    return top_prediction_per_book

def get_visualization(df):
    
    errors = df['BookRating'] - df['predicted_rating']
    plt.figure(figsize=(10, 6))
    plt.hist(errors, bins=15, alpha=0.7, color='r')
    plt.title('Histogram of Prediction Errors')
    plt.xlabel('Prediction Error (Actual - Predicted)')
    plt.ylabel('Frequency')
    plt.grid(True)
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png', bbox_inches='tight')
    plt.close()  # Close the plot to free up memory
    img_base64 = base64.b64encode(img_buf.getvalue()).decode('utf8')
    return f"data:image/png;base64,{img_base64}"