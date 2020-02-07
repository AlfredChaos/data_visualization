import json
import os
import pygal

from country_codes import get_country_code
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

# 将数据加载到一个列表中
filename = os.getcwd() + '\\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
# 打印每个国家2010年的人口数量
for pop_dic in pop_data:
    if pop_dic['Year'] == '2010':
        country_name = pop_dic['Country Name']
        population = int(float(pop_dic['Value']))
        code = get_country_code(country_name)
        if code:
            #print(code + ": " + str(population))
            cc_populations[code] = population

# 根据人口数量将所有国家分为三组
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

# 每组包含几个国家
#print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2020, by Country'
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('world_population.svg')