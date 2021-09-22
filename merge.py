import csv
headers=[]
all_movies=[]
all_movies_links=[]

with open ("movies.csv",encoding='utf8') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]
    headers=data[0]

headers.append("imdb_link")

with open ("movie_links.csv",encoding='utf8') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies_links=data[1:]

with open ("final.csv","a+",encoding='utf8') as f:
    writer=csv.writer(f)
    writer.writerow(headers)
    
for moviesItems in all_movies:
    poster_found=any(moviesItems[8] in movie_link_items for movie_link_items in all_movies_links)
    if poster_found:
        for movie_link_items in all_movies_links:
            if moviesItems[8]==movie_link_items[0]:
                moviesItems.append(movie_link_items[1])
                if len(moviesItems)==28:
                    moviesItems.replace("\n","")
                    with open ("final.csv","a+",encoding='utf8') as f:
                        writer=csv.writer(f)
                        writer.writerow(moviesItems)

