import json
import os

# 将数据加载到一个列表中
filename = os.getcwd() + '\\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家2010年的人口数量
for pop_dic in pop_data:
    if pop_dic['Year'] == '2010':
        country_name = pop_dic['Country Name']
        population = int(float(pop_dic['Value']))
        print(country_name + ": " + str(population))