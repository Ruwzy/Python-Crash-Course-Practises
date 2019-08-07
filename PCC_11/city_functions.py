def city_country(city, country, population_num=''):
    neat_cityname = city.title() + ', ' + country.title()
    if population_num:
        neat_cityname = neat_cityname + ' - population ' + str(population_num)
    else:
        neat_cityname = neat_cityname

    return neat_cityname
