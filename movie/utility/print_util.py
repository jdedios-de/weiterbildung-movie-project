from movie.utility import constant


def print_header():
    print("********** My Movies Database **********")


def print_menu():
    print("Menu:")
    print("0. Exit")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print("9. Movies sorted by year")
    print("10. Filter movies\n")


def print_stats_movies(average_rating, median_rating, best_movie, worst_movie,
                       payload):
    print(f"Average rating: {average_rating:.1f}")
    print(f"Median rating: {median_rating:.1f}")

    print("\n".join(
        [
            f"Best movie: {movie}, "
            f"{payload[movie][constant.RATING_KEY]}"
            for movie in best_movie]
    ))

    print("\n".join(
        [
            f"Worst movie: {movie}, "
            f"{payload[movie][constant.RATING_KEY]}"
            for movie in worst_movie]
    ))


def print_movie_list(total_movies, movies):
    print(f"{total_movies} movies in total")
    print("\n".join(
        [
            f"{movie} ({movies[movie][constant.YEAR_KEY]}): "
            f"{movies[movie][constant.RATING_KEY]}"
            for movie in movies]
    ))


def print_movie_search(movies):
    print("\n".join(
        [
            f"{mov} ({details[constant.YEAR_KEY]}): "
            f"{details[constant.RATING_KEY]}"
            for movie in movies
            for mov, details in movie.items()]
    ))


def print_random_generated_movie(result):
    print(f"Your movie for tonight: {result[constant.PAYLOAD][0]}, "
          f"it's rated {result[constant.PAYLOAD][1][constant.RATING_KEY]}")
