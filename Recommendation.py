# TASK 3 - RECOMMENDATION SYSTEM

# Create a simple recommendation system that suggests items to
# users based on their preferences. You can use techniques like
# collaborative filtering or content-based filtering to recommend
# movies, books, or products to users.

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.metrics import pairwise_distances

data = {
    'User': ['User1', 'User1', 'User2', 'User2', 'User3', 'User3', 'User4', 'User4'],
    'Movie': ['Movie1', 'Movie2', 'Movie2', 'Movie3', 'Movie1', 'Movie3', 'Movie4', 'Movie5'],
    'Rating': [5, 4, 3, 4, 5, 2, 3, 1]
}

df = pd.DataFrame(data)

user_movie_ratings = df.pivot_table(index='User', columns='Movie', values='Rating', fill_value=0)

train_data, test_data = train_test_split(user_movie_ratings, test_size=0.2, random_state=42)

user_similarity = 1 - pairwise_distances(train_data, metric='cosine')

# Predicting movie ratings for the test set
def predict_ratings(user_similarity, ratings):
    mean_user_rating = ratings.mean(axis=1)
    ratings_diff = (ratings - mean_user_rating[:, None])
    pred = mean_user_rating[:, None] + user_similarity.dot(ratings_diff) / user_similarity.sum(axis=1)[:, None]
    return pred

user_ratings_pred = predict_ratings(user_similarity, train_data.values)

def recommend_movies(user_ratings_pred, user, n=5):
    user_ratings = user_ratings_pred[user]
    already_rated = train_data.loc[user, train_data.loc[user] > 0].index
    unrated_movies = user_ratings.drop(already_rated, errors='ignore')
    recommended_movies = unrated_movies.sort_values(ascending=False).head(n)
    return recommended_movies

user_to_recommend = 'User1'
recommendations = recommend_movies(user_ratings_pred, user_to_recommend, n=3)

print(f"Recommended movies for {user_to_recommend}:")
for movie in recommendations.index:
    print(f"- {movie}")
