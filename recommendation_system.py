# Simple Movie Recommendation System

movies = {
    "action": [
        "Avengers",
        "Iron Man",
        "Batman Begins",
        "The Dark Knight",
        "Mission Impossible"
    ],

    "comedy": [
        "Mr. Bean",
        "Home Alone",
        "The Mask",
        "Jumanji",
        "Free Guy"
    ],

    "romance": [
        "Titanic",
        "The Notebook",
        "La La Land",
        "Pride and Prejudice",
        "A Walk to Remember"
    ],

    "science fiction": [
        "Interstellar",
        "Inception",
        "The Martian",
        "Avatar",
        "Gravity"
    ],

    "animation": [
        "Frozen",
        "Toy Story",
        "Finding Nemo",
        "Coco",
        "Moana"
    ]
}

print("=" * 40)
print("MOVIE RECOMMENDATION SYSTEM")
print("=" * 40)

while True:

    print("\nAvailable Genres:")
    for genre in movies:
        print("-", genre.title())

    user_choice = input("\nEnter your favorite genre: ").lower()

    if user_choice in movies:

        print("\nRecommended Movies:\n")

        for movie in movies[user_choice]:
            print("★", movie)

    else:
        print("Genre not found!")

    again = input("\nTry again? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you!")
        break