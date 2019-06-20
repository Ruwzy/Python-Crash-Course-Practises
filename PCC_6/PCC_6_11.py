cities = {
    "chongqing": {
        "nation": "China",
        "population": "3200W",
        "fact": "Chongqing has the best hotpot!",
        },
    "guangzhou": {
        "nation": "China",
        "population": "2000W",
        "fact": "Guangzhou has the best soup!",
        },
    "Tokyo": {
        "nation": "Japan",
        "population": "5000W",
        "fact": "Tokyo is Japan's capital.",
        },
    }

for city, city_info in cities.items():
    print("\nCity name: " + city)
    nation = city_info["nation"]
    population = city_info["population"]
    fact = city_info["fact"]

    print("\nNation is: " + nation.title())
    print("\nPopulation is: " + population.title())
    print("\nFact is: " + fact)