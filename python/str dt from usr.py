usr = {}
name = input('Your Name: ')
age = input('Your Age: ')
favMovies = input('Comma Seprated,Your Favourite Movies: ').split(",")
favSongs = input('Comma Seprated,Your Favourite Songs: ').split(",")
usr['name'] = name
usr['age'] = age
usr['favMovies'] = favMovies
usr['favSongs'] = favSongs

print(usr)
