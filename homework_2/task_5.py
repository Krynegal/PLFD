violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.7],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
songs_number = int(input("Сколько песен выбрать? "))
duration = 0
song_names = [song[0] for song in violator_songs]

for i in range(songs_number):
    song_name = input(f"Название {i + 1}-й песни: ")
    song_index = song_names.index(song_name)
    duration += violator_songs[song_index][1]

print(f"Общее время звучания песен: {round(duration, 2)} минуты")
