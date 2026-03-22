# Creating lists for Movies genres

movie_title = []
movie_rating = []
movie_genre = []
valid_genre = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Documentary"]
print(f" Valid genres : {", ".join(valid_genre)}")

# Introction message to the user
collecting_data = True
print("=" * 50)
print("Welcome to the Movie Data Collection Program!")
print("Enter 'done' at any time to finish.")
print("=" * 50)
movie_count = 0

# Loop to collect movie data
while collecting_data:
    print(f"...Movie {movie_count + 1}...")
    title = input("Enter the movie title: ").strip()
    if title.lower() == "done":
        print("Data collection completed.")
        break
    if title == "":
        print("Movie title cannot be empty. Please try again.")
        continue
    while True:
        try:
            rating = float(input("Rating (1-5): "))
            if rating < 1 or rating > 5:
                print("Rating must be between 1-5. Please try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid number between 1 and 5.")
    while True:
        genre = input(f"Genre {valid_genre}: ").strip().title()
        if genre in valid_genre:
            break
        else:
            print(f" Please choose from: {", ".join(valid_genre)}")
    
    movie_title.append(title)
    movie_rating.append(rating)
    movie_genre.append(genre)
    movie_count += 1

    if movie_count >= 3:
        continue_choice = input("Add another movie? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            collecting_data = False
            break
    
# Display collected movie data
if len(movie_title) == 0:
    print("No movie data collected. Exiting the program.")
    exit()

for i in range(len(movie_title)):
    print(f"""
          Movie Title: {movie_title[i]}
          Rating: {movie_rating[i]})
            Genre: {movie_genre[i]}
            """)

# Stats:
Total_rating = sum(movie_rating)
Average_rating = Total_rating / len(movie_rating)
Highest_rating = max(movie_rating)
Lowest_rating = min(movie_rating)

print(f" Total Movies Analyzed: {len(movie_title)}")
print(f" Average rating: {Average_rating:.2f}")
print(f" Highest rating: {Highest_rating}")
print(f" Lowest rating: {Lowest_rating}")

print("Thank you for using the Movie Data Collection Program!")