## Цель проекта
Цель проекта заключается в разработке и обосновании трех гипотез по развитию проектной территории, расположенной в границах Сиверского городского поселения, применении методов анализа данных и моделирования для их оценки, а также выборе наиболее оптимальной гипотезы для дальнейшей реализации.
## Информация о команде
Работу выполнили студенты 2 курса Института Дизайна и Урбанистики университета ИТМО:
1. Пьянкова Екатерина (разработка сценария 1)
2. Рябошлык Полина (оформление репозитория)
3. Туманова Елизавета (разработка сценария 2)
4. Глушакова Елизавета (оформление презентации)
5. Гапонова Яна (разработка сценария 3)
## Работа с гипотезами
### Нулевой сценарий
Для предварительного анализа территории были проведены следующие шаги:
1. Отрисовка геометрии границ территории - [границы](https://github.com/apolliness/Data-analysis-Siversky/blob/716bb9d574dbb9b1225627c5554fc0f456d3ca80/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/geojson/boundaries.geojson).
2. Получение геометрии водных объектов, дорог и железных дорог с помощью библиотеки OSMNX.
3. Получение слоя городских кварталов с помощью BlocksGenerator - [кварталы](https://github.com/apolliness/Data-analysis-Siversky/blob/c9a3744320546645aecc04d326b33a30434140a3/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/geojson/blocks_zero.geojson).
4. Вычисление матрицы доступности ([матрица доступности](https://github.com/apolliness/Data-analysis-Siversky/blob/134d8b0e0472ff1377d5291e84986a21823d17ad/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C.png)) и матрицы связанности ([матрица связанности](https://github.com/apolliness/Data-analysis-Siversky/blob/134d8b0e0472ff1377d5291e84986a21823d17ad/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C.png)) на основе предварительно полученного графа улично-дорожной сети ([граф](https://github.com/apolliness/Data-analysis-Siversky/blob/134d8b0e0472ff1377d5291e84986a21823d17ad/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D0%B3%D1%80%D0%B0%D1%84.png)) по полигону территории с помощью библиотеки IduEdu.
5. Подсчет разнообразия сервисов ([разнообразие](https://github.com/apolliness/Data-analysis-Siversky/blob/148cf92ad394ded1e09b53b91d8262e9b72a0335/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BD%D0%BE%D0%B5%20%D1%80%D0%B0%D0%B7%D0%BD%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%B8%D0%B5.png)), центральности кварталов ([центральность населения](https://github.com/apolliness/Data-analysis-Siversky/blob/148cf92ad394ded1e09b53b91d8262e9b72a0335/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F.png), [центральность сервисов](https://github.com/apolliness/Data-analysis-Siversky/blob/148cf92ad394ded1e09b53b91d8262e9b72a0335/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BE%D0%B2.png)), определение типа землепользования ([LandUse](https://github.com/apolliness/Data-analysis-Siversky/blob/072b200d235483dadc0ff6a29bbfed73a4ad7f94/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/LandUse/land_use_0.png)) и морфотипа застройки (метрика [SpaceMatrix](https://github.com/apolliness/Data-analysis-Siversky/blob/148cf92ad394ded1e09b53b91d8262e9b72a0335/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/SpaceMatrix/SpaceMatrix.png)).
### Гипотеза №1
Гипотеза №1 подразумевает преобладающую жилую застройку территории с разнообразными сервисами. Для разработки данной гипотезы была использована rTIM - платформа автоматизированного проектирования развития территории.
