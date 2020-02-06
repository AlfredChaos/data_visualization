import pygal.maps.world

i = 1
for country_code in pygal.maps.world.COUNTRIES.keys():
    print(str(i), country_code, pygal.maps.world.COUNTRIES[country_code])
    i += 1