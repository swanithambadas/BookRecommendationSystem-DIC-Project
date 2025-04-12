from flask import Flask, render_template, request
from recommender import get_recommendations, get_visualization
from top_50 import get_top_50
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            top_50_books = get_top_50(df)
            return render_template('index.html', top_50_books = top_50_books)
        else:
            return render_template('index.html', error="Please upload a valid CSV file.")
    return render_template('index.html')
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods = ['post'])
def recommend():
    file = request.files.get('file')
    user_id = request.form.get('user_id')

    if file and file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        # Assuming get_recommendations takes a dataframe and a user_id and returns recommendations
        recommended_books_df = get_recommendations(df, user_id)
        selected_columns = recommended_books_df[['Image-URL-M','BookTitle', 'BookAuthor', 'BookRating']]
        recommended_books = selected_columns.values.tolist()
        visualizations = get_visualization(recommended_books_df)
        if visualizations is None:
            return render_template('recommend.html', error="Failed to generate visualization.")
        
        return render_template('recommend.html', recommended_books=recommended_books, visualizations = visualizations)
    else:
        return render_template('recommend.html', error="Please upload a valid CSV file.")
    

if __name__ == '__main__':
    app.run(debug=True)
