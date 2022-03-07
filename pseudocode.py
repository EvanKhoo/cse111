

"""Netflix
    User Credentials
    Movies 
        summary 
        image 
        preview 
        Rating
        favourite:bool
        duration
        related movies"""

def netflix():
    movie1={
        "summary": "This is a decent movie",
        "image": "google.com/123asdfasfwea",
        "preview": "youtube.com/10aksjhd89a",
        "rating": "high",
        "favourite": True,
        "duration": 138,
        "RelatedMovies": [123,4543,23,786]
    }
    
    movies = [movie1]
    movie=input("Search movies: ")
    if movie in movies:
        value = movies[movie]

        print(value)
    else:
        print("Sorry that movie is not available")

user = {
    "first_name": "Jenny",
    "last_name": "Smith",
    "phone": "885-555-3333",
    "email": "jsmith@gmail.com",
    "username": "jennySmith",
    "password": "password"
    }
user2={
    "first_name": "Benny",
    "last_name": "Mith",
    "phone": "885-777-2222",
    "email": "bmith@gmail.com",
    "username": "bennymith",
    "password": "password"
}
users = [user, user2]

for key in user2.items():
    print(key)

netflix()