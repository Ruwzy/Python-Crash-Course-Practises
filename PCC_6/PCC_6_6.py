fav_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

invest_namelists = ["jen", "ruby", "phil", "cherry"]
for user in fav_languages.keys():
    print("Thank you " + user.title() + "for taking the investigation." )

    if user not in invest_namelists:
        print("Please come to take the investigation, " + user.title())
