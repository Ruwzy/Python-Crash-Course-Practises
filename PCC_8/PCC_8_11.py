def show_magicians(names):
    for name in names:
        print(name)


def make_great(names):
        great_names = []

        while names:
                current_name = names.pop()
                great_name = "the Great " + current_name.title()
                great_names.append(great_name)

        for great_name in great_names:
                magicians.append(great_name)

magicians = ["Jack", "Susan", "Cece"]
show_magicians(magicians)

great_magicians = make_great(magicians[:])
show_magicians(great_magicians)
