MENU_PROMPT = "\n Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit \n"
movies = []
i = 0

def add_movie():
        title = input("Enter the movie title: ")
        director = input("Enter the movie director: ")
        year = input("Enter the movie release year: ")
        movies.append({
        'title': title,
        'director': director,
        'year': year
         })
        
def print_movie(movie):
     print(f"Movie title: {movie['title']} \n Movie diretor: {movie['director']} \n Movie year: {movie['year']}")
        
def list(movies= movies):
    for movie in movies:
           print_movie(movie) 


def find(movies=movies):
    title = input("Enter the movie title you want to find \n")
    for movie in movies:
        if title.lower() == movie["title"].lower():
            print("Movie Found")
            print_movie(movie)
            i = 1
    if i == 0:
         print("Movie not found")    
        

user_options = {
     "a": add_movie,
     "l": list,
     "f": find
}

def menu(MENU_PROMPT, movies):
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
             selected_function = user_options[selection]
             selected_function()
                
        else:
            print("Unknown Command, Please try again.")

        selection = input(MENU_PROMPT)

menu(MENU_PROMPT=MENU_PROMPT, movies=movies)