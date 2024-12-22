## Цель проекта
Цель проекта заключается в разработке и обосновании трех гипотез по развитию проектной территории, расположенной в границах Сиверского городского поселения, применении методов анализа данных и моделирования для их оценки, а также выборе наиболее оптимальной гипотезы для дальнейшей реализации.
## Информация о команде
Работу выполнили студенты 2 курса Института дизайна и урбанистики Университета ИТМО:
1. Пьянкова Екатерина (разработка сценария 1)
2. Рябошлык Полина (оформление репозитория)
3. Туманова Елизавета (разработка сценария 2)
4. Глушакова Елизавета (оформление презентации)
5. Гапонова Яна (разработка сценария 3)
## Работа с гипотезами
### Нулевой сценарий
Для предварительного анализа проектной территории, расположенной в границах Сиверского городского поселения, были проведены следующие шаги:
1. Отрисовка геометрии [границ](https://github.com/apolliness/Data-analysis-Siversky/blob/716bb9d574dbb9b1225627c5554fc0f456d3ca80/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/geojson/boundaries.geojson) территории.
2. Получение геометрии водных объектов, дорог и железных дорог с помощью библиотеки OSMNX.
3. Получение слоя городских [кварталов](https://github.com/apolliness/Data-analysis-Siversky/blob/c9a3744320546645aecc04d326b33a30434140a3/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/geojson/blocks_zero.geojson) с помощью BlocksGenerator.
4. Вычисление [матрицы доступности](https://github.com/apolliness/Data-analysis-Siversky/blob/134d8b0e0472ff1377d5291e84986a21823d17ad/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C.png) и [матрицы связанности](https://github.com/apolliness/Data-analysis-Siversky/blob/134d8b0e0472ff1377d5291e84986a21823d17ad/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C.png) на основе предварительно полученного [графа](https://github.com/apolliness/Data-analysis-Siversky/blob/134d8b0e0472ff1377d5291e84986a21823d17ad/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D0%B3%D1%80%D0%B0%D1%84.png) улично-дорожной сети по полигону территории с помощью библиотеки IduEdu.
5. Получение данных по зданиям и сервисам для проектной территории с помощью библиотеки OSMNX и расчет обеспеченности для каждого типа сервиса: [школы](https://github.com/apolliness/Data-analysis-Siversky/blob/3cf3c1e0c1a4580459d4ba169eb834f98c77bbd1/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D1%88%D0%BA%D0%BE%D0%BB%D1%8B.png), [поликлиники](https://github.com/apolliness/Data-analysis-Siversky/blob/3cf3c1e0c1a4580459d4ba169eb834f98c77bbd1/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%BF%D0%BE%D0%BB%D0%B8%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D0%BA%D0%B0.png), [автобусные остановки](https://github.com/apolliness/Data-analysis-Siversky/blob/3cf3c1e0c1a4580459d4ba169eb834f98c77bbd1/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81%D0%BD%D1%8B%D0%B5%20%D0%BE%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8.png), [банки](https://github.com/apolliness/Data-analysis-Siversky/blob/3cf3c1e0c1a4580459d4ba169eb834f98c77bbd1/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%B1%D0%B0%D0%BD%D0%BA.png), [пекарни](https://github.com/apolliness/Data-analysis-Siversky/blob/3cf3c1e0c1a4580459d4ba169eb834f98c77bbd1/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%BF%D0%B5%D0%BA%D0%B0%D1%80%D0%BD%D0%B8.png).
6. Подсчет [разнообразия](https://github.com/apolliness/Data-analysis-Siversky/blob/148cf92ad394ded1e09b53b91d8262e9b72a0335/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BD%D0%BE%D0%B5%20%D1%80%D0%B0%D0%B7%D0%BD%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%B8%D0%B5.png) сервисов, центральности кварталов ([центральность населения](https://github.com/apolliness/Data-analysis-Siversky/blob/148cf92ad394ded1e09b53b91d8262e9b72a0335/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F.png), [центральность сервисов](https://github.com/apolliness/Data-analysis-Siversky/blob/148cf92ad394ded1e09b53b91d8262e9b72a0335/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BE%D0%B2.png)), определение типа землепользования ([LandUse](https://github.com/apolliness/Data-analysis-Siversky/blob/072b200d235483dadc0ff6a29bbfed73a4ad7f94/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/LandUse/land_use_0.png)) и морфотипа застройки (метрика [SpaceMatrix](https://github.com/apolliness/Data-analysis-Siversky/blob/148cf92ad394ded1e09b53b91d8262e9b72a0335/%D0%BD%D1%83%D0%BB%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9/SpaceMatrix/SpaceMatrix.png)).
### Гипотеза №1
Гипотеза №1 подразумевает преобладающую жилую застройку территории с разнообразными сервисами. Для разработки данной гипотезы была использована rTIM - платформа автоматизированного проектирования развития территории. [Кварталы](https://github.com/apolliness/Data-analysis-Siversky/blob/c0a9938afe4ad4793312f240304b45956e8898c2/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/geojson/blocks.geojson) для территории были отрисованы вручную, а далее с помощью rTIM были получены параметры [жилой застройки](https://github.com/apolliness/Data-analysis-Siversky/blob/f5f1de2ec1665e770c45b9fc8cd2e254f60e59c9/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/geojson/buildings_1.geojson) и ТЭП. Высота зданий в данном сценарии достигает 9 этажей.

Были использованы следующие методы оценки территории: вычисление [матрицы доступности](https://github.com/apolliness/Data-analysis-Siversky/blob/c08361242234565dcf63bd5368999ebae1200d23/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C.png), [матрицы связанности](https://github.com/apolliness/Data-analysis-Siversky/blob/4507fe6d6488b91464c7953d5de68ed508ba3a64/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C.png) на основе [графа](https://github.com/apolliness/Data-analysis-Siversky/blob/4507fe6d6488b91464c7953d5de68ed508ba3a64/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D0%B3%D1%80%D0%B0%D1%84.png). 
Далее были добавлены планируемые к размещению сервисы и расчитана обеспеченность для каждого типа сервиса: [школы](https://github.com/apolliness/Data-analysis-Siversky/blob/4507fe6d6488b91464c7953d5de68ed508ba3a64/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D1%88%D0%BA%D0%BE%D0%BB%D1%8B.png), [поликлиники](https://github.com/apolliness/Data-analysis-Siversky/blob/4507fe6d6488b91464c7953d5de68ed508ba3a64/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%BF%D0%BE%D0%BB%D0%B8%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D0%BA%D0%B8.png), [автобусные остановки](https://github.com/apolliness/Data-analysis-Siversky/blob/4507fe6d6488b91464c7953d5de68ed508ba3a64/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81%D0%BD%D0%B0%D1%8F%20%D0%BE%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0.png), [банки](https://github.com/apolliness/Data-analysis-Siversky/blob/4507fe6d6488b91464c7953d5de68ed508ba3a64/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%B1%D0%B0%D0%BD%D0%BA%D0%B8.png), [железнодорожные станции](https://github.com/apolliness/Data-analysis-Siversky/blob/4507fe6d6488b91464c7953d5de68ed508ba3a64/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%B6%D0%B4%20%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D1%8F.png), [кафе](https://github.com/apolliness/Data-analysis-Siversky/blob/4507fe6d6488b91464c7953d5de68ed508ba3a64/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%BA%D0%B0%D1%84%D0%B5.png), [пекарни](https://github.com/apolliness/Data-analysis-Siversky/blob/4507fe6d6488b91464c7953d5de68ed508ba3a64/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%BF%D0%B5%D0%BA%D0%B0%D1%80%D0%BD%D0%B8.png), [пляжи](https://github.com/apolliness/Data-analysis-Siversky/blob/4507fe6d6488b91464c7953d5de68ed508ba3a64/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%BF%D0%BB%D1%8F%D0%B6%D0%B8.png). В результате на основе этих данных был произведен подсчет [разнообразия сервисов](https://github.com/apolliness/Data-analysis-Siversky/blob/b1234a72abd2d75ff10b59aedef60071eb093550/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D1%80%D0%B0%D0%B7%D0%BD%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%B8%D0%B5%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BE%D0%B2.png), центральности кварталов ([центральность населения](https://github.com/apolliness/Data-analysis-Siversky/blob/b1234a72abd2d75ff10b59aedef60071eb093550/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BF%D0%BE%20%D0%BB%D1%8E%D0%B4%D1%8F%D0%BC.png), [центральность сервисов](https://github.com/apolliness/Data-analysis-Siversky/blob/b1234a72abd2d75ff10b59aedef60071eb093550/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BF%D0%BE%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC.png)), определение типа землепользования ([LandUse](https://github.com/apolliness/Data-analysis-Siversky/blob/b1234a72abd2d75ff10b59aedef60071eb093550/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/LandUse/land_use_1.png)) и морфотипа застройки (метрика [SpaceMatrix](https://github.com/apolliness/Data-analysis-Siversky/blob/b1234a72abd2d75ff10b59aedef60071eb093550/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%201/SpaceMatrix/SpaceMatrix.png)).

Преимущество гипотезы №1 выражается в размещении большего количества жителей и сервисов на ограниченной территории, что может способствовать экономическому развитию.

Недостатки гипотезы №1:
- Перегруженность инфраструктуры: Высокая плотность может привести к перегрузке транспортной и социальной инфраструктуры.
- Меньшая комфортность проживания: Высокие здания могут создавать ощущение замкнутости и недостатка зеленых зон.
- Риски для экологии: Увеличение застройки может негативно сказаться на окружающей среде, включая ухудшение качества воздуха и уменьшение зеленых насаждений.

### Гипотеза №2

Разработка второй гипотезы производилась без использования внешних платформ. В этом сценарии изменяются планировка и характеристики жилой застройки: вводится блокированная застройка и индивидуальное жилищное строительство (ИЖС), при этом высота зданий не превышает пяти этажей. [Кварталы](https://github.com/apolliness/Data-analysis-Siversky/blob/43bb36ec34ec06cffd48fa539a8f9ee3acb14509/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/geojson/blocks_2.geojson), [геометрии зданий](https://github.com/apolliness/Data-analysis-Siversky/blob/43bb36ec34ec06cffd48fa539a8f9ee3acb14509/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/geojson/buildings_2.geojson) и [дороги](https://github.com/apolliness/Data-analysis-Siversky/blob/43bb36ec34ec06cffd48fa539a8f9ee3acb14509/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/geojson/roads_2.geojson) были отрисованы вручную.

Также были использованы следующие методы оценки территории: вычисление [матрицы доступности](https://github.com/apolliness/Data-analysis-Siversky/blob/08be13d232edf90237a116a4d1779591ef00e1b3/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C.png), [матрицы связанности](https://github.com/apolliness/Data-analysis-Siversky/blob/08be13d232edf90237a116a4d1779591ef00e1b3/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C.png) на основе [графа](https://github.com/apolliness/Data-analysis-Siversky/blob/08be13d232edf90237a116a4d1779591ef00e1b3/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D0%B3%D1%80%D0%B0%D1%84.png). Далее вручную были добавлены планируемые к размещению сервисы и расчитана обеспеченность для каждого типа сервиса: [школы](https://github.com/apolliness/Data-analysis-Siversky/blob/08be13d232edf90237a116a4d1779591ef00e1b3/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D1%88%D0%BA%D0%BE%D0%BB%D1%8B.png), [поликлиники](https://github.com/apolliness/Data-analysis-Siversky/blob/08be13d232edf90237a116a4d1779591ef00e1b3/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%BF%D0%BE%D0%BB%D0%B8%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D0%BA%D0%B0.png), [детские сады](https://github.com/apolliness/Data-analysis-Siversky/blob/08be13d232edf90237a116a4d1779591ef00e1b3/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%B4%D0%B5%D1%82%20%D1%81%D0%B0%D0%B4%D1%8B.png), [автобусные остановки](https://github.com/apolliness/Data-analysis-Siversky/blob/08be13d232edf90237a116a4d1779591ef00e1b3/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81%D0%BD%D1%8B%D0%B5%20%D0%BE%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8.png) . В результате на основе этих данных был произведен подсчет [разнообразия сервисов](https://github.com/apolliness/Data-analysis-Siversky/blob/08be13d232edf90237a116a4d1779591ef00e1b3/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC%D0%B8/%D1%80%D0%B0%D0%B7%D0%BD%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%B8%D0%B5%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BE%D0%B2.png), центральности кварталов ([центральность населения](https://github.com/apolliness/Data-analysis-Siversky/blob/31160b11f39ef7ec39e9e4d07a692136940f02bf/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F.png), [центральность сервисов](https://github.com/apolliness/Data-analysis-Siversky/blob/31160b11f39ef7ec39e9e4d07a692136940f02bf/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C_%D0%BF%D0%BE_%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%D0%BC.png)), определение типа землепользования ([LandUse](https://github.com/apolliness/Data-analysis-Siversky/blob/31160b11f39ef7ec39e9e4d07a692136940f02bf/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/LandUse/land_use_2.png)) и морфотипа застройки (метрика [SpaceMatrix](https://github.com/apolliness/Data-analysis-Siversky/blob/31160b11f39ef7ec39e9e4d07a692136940f02bf/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%202/SpaceMatrix/SpaceMatrix.png)).

Достоинства гипотезы №3:
- Низкая этажность: Создает более комфортные условия для проживания, улучшает восприятие территории жителями.
- Устойчивое развитие: Блокированная застройка и ИЖС могут способствовать более гармоничному развитию территории с учетом существующих ресурсов.

Недостатком гипотезы №3 является меньшая плотность застройки, которая может привести к недостаточному количеству жилья и сервисов для растущего населения.

### Гипотеза №3

Гипотеза №3 существенно отличается от первых двух: в данном сценарии территория преобразуется в промышленную, без планов на жилую застройку и развитие сервисов. [Кварталы](https://github.com/apolliness/Data-analysis-Siversky/blob/31160b11f39ef7ec39e9e4d07a692136940f02bf/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%203/geojson/blocks_3.geojson) и промышленные [здания](https://github.com/apolliness/Data-analysis-Siversky/blob/31160b11f39ef7ec39e9e4d07a692136940f02bf/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%203/geojson/buildings_3.geojson) были отрисованы вручную.

Были использованы следующие методы оценки территории: вычисление [матрицы доступности](https://github.com/apolliness/Data-analysis-Siversky/blob/31160b11f39ef7ec39e9e4d07a692136940f02bf/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%203/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C.png), [матрицы связанности](https://github.com/apolliness/Data-analysis-Siversky/blob/f092af775d8b1419651a55c3865f94a5525634da/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%203/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C.png) на основе [графа](https://github.com/apolliness/Data-analysis-Siversky/blob/f092af775d8b1419651a55c3865f94a5525634da/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%203/%D0%B3%D1%80%D0%B0%D1%84%2C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D1%8C%2C%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D0%B3%D1%80%D0%B0%D1%84.png). Также была произведена оценка [центральности населения](https://github.com/apolliness/Data-analysis-Siversky/blob/f092af775d8b1419651a55c3865f94a5525634da/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%203/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C/%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BF%D0%BE%20%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8E.png) и определение и морфотипа застройки (метрика [SpaceMatrix](https://github.com/apolliness/Data-analysis-Siversky/blob/f092af775d8b1419651a55c3865f94a5525634da/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0%203/SpaceMatrix/SpaceMatrix.png)).

Преимущества гипотезы №3:
- Простота реализации: Промышленная застройка может быть проще в реализации с точки зрения получения разрешений и финансирования.
- Создание рабочих мест: Промышленная зона может привлечь инвесторов и создать новые рабочие места, что положительно скажется на экономике региона.
  
Недостатки гипотезы №3:
- Экологические риски: Промышленные предприятия могут негативно влиять на экологическую обстановку в районе, что может вызвать недовольство среди жителей близлежащих жилых зон из-за возможного загрязнения воздуха и шума.
- Ограничения по зонированию: Промышленная застройка может ограничивать возможности для дальнейшего развития жилой зоны, создавая препятствия для расширения социальной инфраструктуры или увеличения зеленых пространств.
  
## Анализ результатов

В ходе разработки проекта по развитию проектной территории в Сиверском городском поселении была выбрана вторая гипотеза, которая предполагает использование блокированной застройки и индивидуального жилищного строительства (ИЖС) с максимальной высотой зданий до пяти этажей. 

В отличие от первой гипотезы, которая основывалась на высокой жилой застройке (до 9 этажей), вторая гипотеза предлагает более низкие здания, что может лучше соответствовать существующей городской среде и предпочтениям жителей. Блокированная застройка и ИЖС создают более уютные и комфортные условия для проживания, что является важным фактором для повышения качества жизни населения. Вторая гипотеза акцентирует внимание на устойчивом развитии территории, избегая чрезмерной плотности застройки. Это может способствовать созданию более сбалансированной инфраструктуры с учетом потребностей местных жителей, таких как доступ к образовательным и медицинским учреждениям, а также общественному транспорту.
