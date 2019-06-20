def describe_city(city_name, nation = "China"):
    print(city_name.title() + " is in " + nation.title())

describe_city("Chongqing")
describe_city(city_name = "Beijing")
describe_city("Tokyo", nation = "Japan")