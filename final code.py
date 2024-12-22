# -*- coding: utf-8 -*-
"""Siversky.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ikC7EkR9yvXVmtsGEKD2KeIdtiHc_9Kt

Шаг 1. генерация кварталов
"""

!pip install blocksnet ipykernel -q

!pip install folium matplotlib mapclassify

import geopandas as gpd

boundary = gpd.read_file('/content/boundary.geojson')
roads = gpd.read_file('/content/road_2.geojson')
water = gpd.read_file('/content/water.geojson')

tags = {
    'roads': {
      "highway": ["construction","crossing","living_street","motorway","motorway_link","motorway_junction","pedestrian","primary","primary_link","raceway","residential","road","secondary","secondary_link","services","tertiary","tertiary_link","track","trunk","trunk_link","turning_circle","turning_loop","unclassified",],
      "service": ["living_street", "emergency_access"]
    },
    'railways': {
      "railway": "rail"
    },
    'water': {
      'riverbank':True,
      'reservoir':True,
      'basin':True,
      'dock':True,
      'canal':True,
      'pond':True,
      'natural':['water','bay'],
      'waterway':['river','canal','ditch'],
      'landuse':'basin',
      'water': 'lake'
    }
}

local_crs = boundary.estimate_utm_crs()

boundary = boundary.reset_index()[['geometry']].to_crs(local_crs)
water = water.reset_index()[['geometry']].to_crs(local_crs)
roads = roads.reset_index()[['geometry']].to_crs(local_crs)
# railways = railways.reset_index()[['geometry']].to_crs(local_crs)

roads = roads[roads.geom_type.isin(['LineString', 'MultiLineString'])]

import momepy
GAP_TOLERANCE = 1
def _get_roads(roads):
    merged = roads.unary_union
    if merged.geom_type == 'MultiLineString':
        roads = gpd.GeoDataFrame(geometry=list(merged.geoms), crs=roads.crs)
    else:
        roads = gpd.GeoDataFrame(geometry=[merged], crs=roads.crs)
    roads = roads.explode(index_parts=False).reset_index(drop=True)
    roads.geometry = momepy.close_gaps(roads, GAP_TOLERANCE)
    roads = roads[roads.geom_type.isin(['LineString'])]
    return roads

roads = _get_roads(roads)
roads

"""Импортируем класс `BlocksGenerator` и инициализируем его экземпляр с помощью наших геометрий. На этапе инициализации:
- все геометрии проверяются по спецификации (можете увидеть при наведении курсора на BlocksGenerator);
- из геометрии границ территории удаляются полигоны водных объектов.
"""

from blocksnet import BlocksGenerator

bg = BlocksGenerator(boundary, roads, None, water)

blocks = bg.run()

"""С помощью библиотеки mapclassify мы можем выводить геометрии на карту через `.explore()`."""

blocks.explore()

!pip install mapclassify -q

import geopandas as gpd
buildings = gpd.read_file("/content/building_g_2.geojson")

buildings.explore()

buildings = buildings.to_crs(local_crs).reset_index()[['geometry']]
buildings.geometry = buildings.representative_point()

from blocksnet import BlocksSplitter

bs = BlocksSplitter(blocks, buildings)

splitted_blocks = bs.run()

len(blocks), len(splitted_blocks)

blocks.plot(linewidth=0.1, figsize=(10,10)).set_axis_off()
splitted_blocks.plot(linewidth=0.1, figsize=(10,10)).set_axis_off()

splitted_blocks.to_file('blocks.geojson')

"""Шаг 2. Генерация графов, расчет доступности и связанности территории"""

!pip install iduedu

boundary.to_crs(4326, inplace=True)

!pip install momepy
import momepy

CRS = 32636
SPEED_M_MIN = 1000

import networkx as nx

def _roads_to_graph(roads):
    graph = momepy.gdf_to_nx(roads)
    graph.graph['crs'] = roads.crs.to_epsg()
    graph = nx.DiGraph(graph)
    for _, _, data in graph.edges(data=True):
        geometry = data['geometry']
        data['time_min'] = geometry.length / SPEED_M_MIN
        # data['weight'] = data['mm_len'] / 1000 / 1000
        # data['length_meter'] = data['mm_len'] / 1000
    for n, data in graph.nodes(data=True):
        graph.nodes[n]['x'] = n[0]  # Assign X coordinate to node
        graph.nodes[n]['y'] = n[1]

    return graph

roads_G = _roads_to_graph(roads)
roads_G

from blocksnet import AccessibilityProcessor
AccessibilityProcessor._fix_graph(roads_G)

from blocksnet import AccessibilityProcessor

ap = AccessibilityProcessor(blocks)
acc_mx = ap.get_accessibility_matrix(roads_G)
acc_mx.head() # вывод первых 5 строк полученной матрицы

import matplotlib.pyplot as plt
import networkx as nx

# Предполагаем, что roads_G уже создан и обработан
# Визуализация графа
plt.figure(figsize=(12, 12))
pos = {n: (data['x'], data['y']) for n, data in roads_G.nodes(data=True)}  # Получаем позиции узлов

# Рисуем рёбра без стрелок
nx.draw_networkx_edges(roads_G, pos, alpha=0.5, edge_color='grey', arrows=False)

# Рисуем узлы
nx.draw_networkx_nodes(roads_G, pos, node_color='black', node_size=10)

# Добавляем подписи узлов (если необходимо)
# nx.draw_networkx_labels(roads_G, pos, font_size=8)

plt.title("Визуализация графа дорог")
plt.axis('equal')  # Сохраняем пропорции
plt.show()

from blocksnet.models import City
from blocksnet import Accessibility, Connectivity

blocks['land_use'] = None

city = City(
    blocks=blocks,
    acc_mx=acc_mx
)

connectivity = Connectivity(city_model=city)
connectivity_result = connectivity.calculate()
connectivity_result

connectivity_result.explore()

from blocksnet.models import City
blocks['land_use'] = None
city = City(
    blocks=blocks,
    acc_mx=acc_mx
)

from blocksnet import Accessibility, Connectivity

accessibility = Accessibility(city_model=city)
block = city[2] # квартал от которого будем считать доступность
result = accessibility.calculate(block)

Accessibility.plot(result, linewidth=0.9, figsize=(30,15))

connectivity = Connectivity(city_model=city)
connectivity_result = connectivity.calculate()

Connectivity.plot(connectivity_result, linewidth=0.9, figsize=(30,15))

import geopandas as gpd
buildings = gpd.read_file("/content/building_g_2.geojson")

buildings = buildings.to_crs(local_crs) # переводим здания в локальную систему координат

buildings = buildings[buildings.geometry.type.isin(['Polygon', 'MultiPolygon'])]

buildings = buildings.reset_index(drop=True)

buildings

import pandas as pd

# Преобразуем столбец 'building:levels' в числовой тип, ошибки будут заменены на NaN
buildings['building:levels'] = pd.to_numeric(buildings['building:levels'], errors='coerce')

# Заполним пропущенные значения (NaN) нулями или другими подходящими значениями
buildings = buildings.fillna(0)

# Добавляем или преобразуем необходимые атрибуты

# 1. Количество этажей (number_of_floors)
buildings['number_of_floors'] = buildings['building:levels']

# 2. Площадь застройки (footprint_area) - как площадь геометрии (основание здания)
buildings['footprint_area'] = buildings.geometry.area

# 3. Общая площадь всех этажей (build_floor_area) - footprint_area * number_of_floors
buildings['build_floor_area'] = buildings['footprint_area'] * buildings['number_of_floors']

# 4. Жилая площадь (living_area) и нежилая площадь (non_living_area)
# Жилая площадь будет рассчитываться только для жилых зданий
residential_tags = ['residential']
buildings['living_area'] = buildings.apply(
    lambda x: 0.8 * x['build_floor_area'] if x['building'] in residential_tags else 0,
    axis=1
)

# Нежилая площадь будет 20% от общей площади этажей
buildings['non_living_area'] = buildings['build_floor_area'] - buildings['living_area']

# 5. Население (population) - для жилых зданий
buildings['population'] = buildings['population']


# Теперь удалим все остальные столбцы, кроме 'geometry', 'build_floor_area', 'living_area', 'non_living_area',
# 'footprint_area', 'number_of_floors', 'population'
buildings = buildings[['geometry', 'build_floor_area', 'living_area', 'non_living_area',
                       'footprint_area', 'number_of_floors', 'population']]

# Проверим результат
buildings

buildings.explore()

city.update_buildings(buildings)

"""Шаг 3. Анализ обеспеченности сервисами"""

from tqdm.auto import tqdm

def remove_inner_polygons(gdf_polygons):
    to_remove = []
    print(len(gdf_polygons))
    for idx, poly1 in tqdm(gdf_polygons.iterrows()):
        for idx2, poly2 in gdf_polygons.iterrows():
            if idx != idx2 and poly1.geometry.contains(poly2.geometry):
                to_remove.append(idx2)
    return gdf_polygons.drop(to_remove)

# Шаг 3: Удаляем близкие центроиды, оставляя одну точку на буфер
def remove_close_centroids(gdf_centroids, buffer_distance=60):
    # Создаем новый GeoDataFrame для хранения итоговых точек
    final_centroids = gpd.GeoDataFrame(columns=gdf_centroids.columns, crs=gdf_centroids.crs)

    # Итерируем по всем точкам
    while not gdf_centroids.empty:
        # Берем первую точку
        current_point = gdf_centroids.iloc[0]

        # Создаем буфер вокруг этой точки
        buffer = current_point.geometry.buffer(buffer_distance)

        # Находим все точки, которые попадают в этот буфер
        close_points = gdf_centroids[gdf_centroids.geometry.within(buffer)]

        # Добавляем одну (например, первую) точку в итоговый результат с помощью concat
        final_centroids = gpd.GeoDataFrame(
            pd.concat([final_centroids, gpd.GeoDataFrame([current_point])], ignore_index=True)
        )

        # Удаляем все точки, попавшие в этот буфер, из исходного списка
        gdf_centroids = gdf_centroids.drop(close_points.index)

    return final_centroids

import os
import geopandas as gpd
from shapely.geometry import Point
from blocksnet import ServiceType

directory = os.fsencode("/content/servises/")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".geojson"):
        service_name = filename.removesuffix(".geojson")
        print(f"Adding service {service_name}")
        service_gdf = gpd.read_file("/content/servises/" + filename)
        service_gdf.to_crs(local_crs, inplace=True)
        service = remove_inner_polygons(service_gdf)
        service['geometry'] = service.centroid
        service = remove_close_centroids(service)
        service = service[["geometry"]]
        try:
          city.update_services(service_name, service)
        except:
          continue
    else:
        continue

from blocksnet import LandUsePrediction # импортируем модуль

lup = LandUsePrediction(city_model=city)
lu_blocks = lup.calculate()
lu_blocks.head()

LandUsePrediction.plot(lu_blocks)

city.update_land_use(lu_blocks)

blocks.plot()

from blocksnet import Provision, ProvisionMethod
service_type = 'school'
prov = Provision(city_model=city)
prov_res = prov.calculate(service_type)

prov.plot(prov_res)
city.to_pickle("lp_bn_model.pkl")

from blocksnet import Provision, ProvisionMethod
service_type = 'polyclinic'
prov = Provision(city_model=city)
prov_res = prov.calculate(service_type)

prov.plot(prov_res)
city.to_pickle("lp_bn_model.pkl")

from blocksnet import Provision, ProvisionMethod
service_type = 'bakery'
prov = Provision(city_model=city)
prov_res = prov.calculate(service_type)

prov.plot(prov_res)
city.to_pickle("lp_bn_model.pkl")

from blocksnet import Provision, ProvisionMethod
service_type = 'bank'
prov = Provision(city_model=city)
prov_res = prov.calculate(service_type)

prov.plot(prov_res)
city.to_pickle("lp_bn_model.pkl")

from blocksnet import Provision, ProvisionMethod
service_type = 'beach'
prov = Provision(city_model=city)
prov_res = prov.calculate(service_type)

prov.plot(prov_res)
city.to_pickle("lp_bn_model.pkl")

from blocksnet import Provision, ProvisionMethod
service_type = 'bus_stop'
prov = Provision(city_model=city)
prov_res = prov.calculate(service_type)

prov.plot(prov_res)
city.to_pickle("lp_bn_model.pkl")

from blocksnet import Provision, ProvisionMethod
service_type = 'cafe'
prov = Provision(city_model=city)
prov_res = prov.calculate(service_type)

prov.plot(prov_res)
city.to_pickle("lp_bn_model.pkl")

from blocksnet import Provision, ProvisionMethod
service_type = 'library'
prov = Provision(city_model=city)
prov_res = prov.calculate(service_type)

prov.plot(prov_res)
city.to_pickle("lp_bn_model.pkl")

from blocksnet import Provision, ProvisionMethod
service_type = 'train_station'
prov = Provision(city_model=city)
prov_res = prov.calculate(service_type)

prov.plot(prov_res)
city.to_pickle("lp_bn_model.pkl")

city.to_pickle("lp_bn_model.pkl")

"""Шаг 4. Вычисление центральности, определение морфотипа застройки"""

Siversk = City.from_pickle("/content/lp_bn_model.pkl")
Siversk

print(Siversk)

from blocksnet import Diversity

diversity = Diversity(city_model=Siversk)
result_devirsity = diversity.calculate()

result_devirsity

Diversity.plot(result_devirsity, figsize =(10,10)) #оценка разнообразия сервисов

from blocksnet import Centrality, PopulationCentrality

centrality = Centrality(city_model=Siversk)
result_centrality = centrality.calculate()

result_centrality
Centrality.plot(result_centrality, figsize =(10,10))

centrality_population = PopulationCentrality(city_model=Siversk)

result_centrlity_population = centrality_population.calculate()

result_centrlity_population
PopulationCentrality.plot(result_centrlity_population, figsize =(10,10))

from blocksnet import Spacematrix

spacematrix = Spacematrix(city_model=Siversk)
result_spacematrix = spacematrix.calculate()

result_spacematrix
Spacematrix.plot(result_spacematrix, figsize =(10,10))