def make_album(singer_name, album_name):
    album_dic = {"singer": singer_name, "album": album_name}
    return album_dic


while True:
    print("\nPlease enter your favourite singer's name: ")
    print("(enter \"q\" to quit the input")

    s_name = input("\nThe singer's name: ")
    if s_name == "q":
        break

    a_name = input("The album's name: ")
    if a_name == "q":
        break


    final_album = make_album(s_name, a_name)
    print("\nHere is your favourite album's info: " + "\n")
    print(final_album)