def make_album(singer_name, album_name):
    album_dic = {"singer": singer_name, "album": album_name}
    return album_dic


album_one = make_album("Sarah", "X")
print(album_one)

album_two = make_album("Dion", "My heart")
print(album_two)

alnum_three = make_album("Faye", "Fary tale")
print(alnum_three)


def make_album(singer_name, album_name, song_num = ""):
    if song_num:
        album_dic = {"singer": singer_name, "album": album_name, "has songs": song_num}
    else:
        album_dic = {"singer": singer_name, "album": album_name}
    return album_dic

album_four = make_album("Jack", "Hola", song_num = "18")
print(album_four)