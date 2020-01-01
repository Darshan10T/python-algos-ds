import heapq

class MovieRating:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

def GetTopK(listMovieName, listMovieRating, k):
    final_list = {}

    if len(listMovieName) == len(listMovieRating):
        for i in range(len(listMovieName)):
            if listMovieName[i] not in final_list:
                final_list[listMovieName[i]] = 0

            final_list[listMovieName[i]] += listMovieRating[i]
    topKRatedMovies = heapq.nlargest(k, final_list.items(), key=lambda i: i[1])
    print(topKRatedMovies)
    for movie in topKRatedMovies:
        print(movie[0])

listMovieName = ["abc","def","ghi","abc","xyz"]
listMovieRating = [10,15,10,12,100]
#listMovieName = ["Trump","Obama","Obama","Obama","Trump", "Sanders"]
#listMovieRating = [1,1,1,1,1,1]
k = 2
GetTopK(listMovieName, listMovieRating, k)