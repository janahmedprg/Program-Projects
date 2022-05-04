a = int(input("Please enter number (1, 2 or 3) of trilogy: "))
b = int(input("Please enter number  (1, 2 or 3)  of the film in this trilogy: "))
if a <= 0 or a > 3 or b <= 0 or b > 3:
    print("Invalid Input, enter number 1,2 or 3!")
else:
    a = a-1
    b = b-4
    star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
    ]
    print(star_wars_movies[a][b])
