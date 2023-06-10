import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
movies = pd.read_csv("movies_metadata.csv", low_memory=False)
print(movies.head(3))
c = movies["vote_average"].mean()
print("C ", c)
m = movies['vote_count'].quantile(0.90)
print("m ", m)
q_movies = movies.copy().loc[movies['vote_count'] >= m]
print("after filtering", q_movies.shape)
print("overall data", movies.shape)
def weighted_rating(x, m =m, C= c):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C)
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)
print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(10))
tfidf = TfidfVectorizer(stop_words='english')
movies['overview'] = movies['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(movies['overview'])
print(tfidf_matrix.shape)
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
print(cosine_sim.shape)
print(cosine_sim[1])
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()
print(indices[:10])
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]
print(get_recommendations('The Dark Knight Rises'))