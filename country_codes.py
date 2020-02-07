import pygal

def get_country_code(country_name):
    """根据指定的国家，返回pygal的国别码"""
    for code, name in pygal.maps.world.COUNTRIES.items():
        if name == country_name:
            return code
    return None

#print(get_country_code('China'))