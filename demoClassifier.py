import pandas as pd
import numpy as np

df2=pd.read_csv("final.csv")
C=df2["vote_average"].mean()
m=df2["vote_count"].quantile(0.9)
qmovies=df2.copy().loc[df2["vote_count"]>=m]

def weight_rating(x,m=m,C=C):
  v=x["vote_count"]
  R=x["vote_average"]
  return (((v/(v+m))*R)+((m/(v+m))*C))

qmovies["score"]=qmovies.apply(weight_rating,axis=1)
qmovies=qmovies.sort_values("score",ascending=False)
output=qmovies[["original_title","imdb_link","vote_average","score","release_date","overview"]].head(20).values.tolist()

