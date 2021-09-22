import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df=pd.read_csv("final.csv")
df=df[df["soup"].notna()]
count=CountVectorizer(stop_words="english")
count_matrix=count.fit_transform(df["soup"])
cosine=cosine_similarity(count_matrix,count_matrix)
df=df.reset_index()
indices=pd.Series(df.index,index=df["original_title"])

def get_recommendation(title):
  idx=indices[title]
  sim_score=list(enumerate(cosine[idx]))
  sim_score=sorted(sim_score,key=lambda x:x[1],reverse=True)
  sim_score=sim_score[1:11]
  movies_indices=[i[0] for i in sim_score]
  return df[["original_title","imdb_link","vote_average","score","release_date","overview"]].iloc[movies_indices].value.tolist()