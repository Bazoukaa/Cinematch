import pandas as pd

# Load the IMDb CSV file
imdb_df = pd.read_csv('/content/imdb.csv', encoding='ISO-8859-1')

def greet_user():
    name = input("Hey! What's your name? ")
    print(f"Hi {name}! Welcome to CineMatch, Your Personal Movie Matchmaker!")

def choose_genres():
    available_genres = imdb_df['genres'].str.split('|').explode().unique()
    print("Here are the available genres:")

    for genre in available_genres:
        print(f"- {genre}")

    while True:
        genres = input("What genre(s) are you interested in today? (Separate multiple genres with commas): ")
        chosen_genres = [genre.strip() for genre in genres.split(',')]

        if all(any(genre in g for g in available_genres) for genre in chosen_genres):
            return chosen_genres
        else:
            print("Invalid genre(s). Please try again.")

def choose_era():
    while True:
        era_choice = input("Would you like movies from the old era (till 1999) or from 2000 onwards? (Enter 'old' or 'new'): ").lower()
        if era_choice in ['old', 'new']:
            return era_choice
        else:
            print("Invalid choice. Please enter 'old' or 'new'.")

def choose_top_10():
    while True:
        top_10_choice = input("Would you like to see the top 10 movies by vote average? (yes/no): ").lower()
        if top_10_choice in ['yes', 'no']:
            return top_10_choice == 'yes'
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

def get_movies_by_genres_and_era(chosen_genres, era_choice, top_10):
    genre_filter = imdb_df['genres'].apply(lambda x: all(genre in x for genre in chosen_genres))

    if era_choice == 'old':
        era_filter = imdb_df['release_year'] < 2000
    else:  # era_choice == 'new'
        era_filter = imdb_df['release_year'] >= 2000

    filtered_movies = imdb_df[genre_filter & era_filter]

    if top_10:
        filtered_movies = filtered_movies.sort_values(by='vote_average', ascending=False).head(10)

    return filtered_movies

def show_movies(movies_df):
    print("Here are the movie titles from the selected genres:")
    for index, title in enumerate(movies_df['original_title'], 1):
        print(f"{index}. {title}")

    while True:
        try:
            movie_choice = int(input("Please choose a movie by entering its number: "))
            if 1 <= movie_choice <= len(movies_df):
                return movies_df.iloc[movie_choice - 1]
            else:
                print("Invalid choice. Please enter a number corresponding to the movie list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_basic_movie_info(movie):
    print("\nMovie Information:")
    print(f"Title: {movie['original_title']}")
    print(f"Overview: {movie['overview']}")
    print(f"Vote Average: {movie['vote_average']}")
    print(f"Cast: {movie['cast']}")
    print(f"Director: {movie['director']}")
    print(f"Release Date: {movie['release_date']}")
    print(f"Runtime: {movie['runtime']} minutes")

def display_additional_movie_info(movie):
    print(f"Genres: {movie['genres']}")
    print(f"Tagline: {movie['tagline']}")
    print(f"Budget: ${movie['budget']}")
    print(f"Revenue: ${movie['revenue']}")
    print(f"Popularity: {movie['popularity']}")
    print(f"Vote Count: {movie['vote_count']}")

    keywords = movie.get('keywords', 'N/A')
    homepage = movie.get('homepage', 'N/A')
    print(f"Keywords: {keywords}")
    print(f"Homepage: {homepage}")

def main():
    greet_user()

    while True:
        try:
            chosen_genres = choose_genres()
            era_choice = choose_era()
            top_10 = choose_top_10()
            filtered_movies = get_movies_by_genres_and_era(chosen_genres, era_choice, top_10)

            if filtered_movies.empty:
                print("No movies found for the selected genre(s) and era. Please choose again.")
                continue

            selected_movie = show_movies(filtered_movies)
            display_basic_movie_info(selected_movie)

            more_info = input("Would you like to know more details about this movie? (yes/no): ").lower()
            if more_info == 'yes':
                display_additional_movie_info(selected_movie)

            repeat = input("Would you like to choose another genre, era, or view another top 10 list? (yes/no): ").lower()
            if repeat != 'yes':
                break
        except Exception as e:
            print(f"An error occurred: {e}. Let's try that again.")

if __name__ == "__main__":
    main()
