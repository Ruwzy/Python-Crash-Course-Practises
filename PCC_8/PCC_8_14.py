def make_car(producer, model, **other_info):
    car_profile = {}
    car_profile['producer_name'] = producer
    car_profile['model_name'] = model
    for key, value in other_info.items():
        car_profile[key] = value
    return car_profile

Japanese_car = make_car('sunaru', 'outback', color = "blue", tow_package = True)
print(Japanese_car)