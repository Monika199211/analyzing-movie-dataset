# --------------
from csv import reader
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)
movies_header=movies[0]
movies=movies[1:]
v=movies_header.index('id')
for i in movies:
    if i[v]=='4553':
        movies.remove(i)
#len(movies)
def explore_data(dataset, start, end, rows_and_columns=False):

    print(dataset[start:end])

#explore_data(movies, 0, 5, rows_and_columns=False)   
def duplicate_and_unique_movies(dataset, index_):
    a_list=[x[index_] for x in dataset ]
    b_list=[y for y in a_list if a_list.count(y) > 1]
    c_list=list(set(b_list))
    return c_list
    
    
c_list=duplicate_and_unique_movies(movies, movies_header.index('title_movies'))
reviews_max={}
a=movies_header.index('vote_count')
    
for i in c_list:
    l=[]
    for j in movies:
            if (i in j):
                l.append(j[a])        
    l=list(map(int,l))
    reviews_max[i]=max(l)
movies_clean=[]
for i in reviews_max:
        for j in movies:
            if ((i in j) and (reviews_max[i] == int(j[a]))):
                movies_clean.append(j)
            elif((i in j) and (reviews_max[i] != int(j[a]))):
                continue
            else:
                movies_clean.append(j)
def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    movies_=[]
    for i in dataset:
        if i[index_]==lang_:
            movies_.append(i)
    return movies_
    explore_data(movies_, 0, 5)
    #a_list=[x[index_] for x in dataset if x[a]=='en']
    #b_list=[y for y in a_list if a_list.count(y) > 1]
    #return movies_
   
    
movies_en=movies_lang(movies, movies_header.index('original_language'), 'en')


def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """
    rated_movies=[]
    a=movies_header.index('vote_average')
    b=movies_header.index('title_movies')
    for i in dataset:
        if (rate_low <= float(i[a]) <=rate_high):
            rated_movies.append(i[b])
        
    #explore_data(rated_movies,0, 5)
    return rated_movies
    

high_rated_movies=rate_bucket(movies_en,8,10)
explore_data(high_rated_movies,0,5)


