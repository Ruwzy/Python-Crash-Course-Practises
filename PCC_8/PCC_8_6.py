def city_country(city, country):
    full_output = city + ", " + country
    return full_output.title()

city_one = city_country("Chongqing", "china")
print(city_one)

city_two = city_country("tokyo", "japan")
print(city_two)

city_three = city_country("baltimore", "the U.S")
print(city_three)