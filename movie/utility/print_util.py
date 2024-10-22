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


def print_stats_movies(average_rating, median_rating, best_movie, worst_movie, payload):
    print(f"Average rating: {average_rating:.1f}")
    print(f"Median rating: {median_rating:.1f}")

    for movie in best_movie:
        print(f"Best movie: {movie}, "
              f"{payload[movie][constant.RATING_KEY]}")

    for movie in worst_movie:
        print(f"Worst movie: {movie}, "
              f"{payload[movie][constant.RATING_KEY]}")


def print_movie_list(total_movies, movies):
    print(f"{total_movies} movies in total")
    for movie in movies:
        print(
            f"{movie} ({movies[movie][constant.YEAR_KEY]}): {movies[movie][constant.RATING_KEY]}")


def main():
    pass


if __name__ == '__main__':
    main()
