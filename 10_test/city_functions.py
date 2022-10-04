def getCityCountry(city, country, population=''):
    if population:
        cityName = city + ', ' + country + ' - population ' + population
    else:
        cityName = city + ', ' + country
    return cityName