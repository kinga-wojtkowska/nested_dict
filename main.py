models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

brand=[]
model=[]
for i in models:
    b,m = i.split(' - ')
    brand.append(b)
    model.append(m)

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']
sales_2018 = []
for i in sales2018: 
    sales_2018.append(i.replace(",", ""))
sales_2018_int = [int(i) for i in sales_2018]

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']
sales_2017 = []
for i in sales2017: 
    if i == 'NA':
        sales_2017.append(0)
    elif i != 'NA':
        sales_2017.append(i.replace(",", ""))
sales_2017_int = [int(i) for i in sales_2017]

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']
sales_2016 = []
for i in sales2016: 
    if i == 'NA':
        sales_2016.append(0)
    elif i != 'NA':
        sales_2016.append(i.replace(",", ""))
sales_2016_int = [int(i) for i in sales_2016]

answer1 = "" # wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

cars = {}
for b in brand:
    cars[b]={}

sales_list = [{x:{'sales':{'2016' : a, '2017' : b, '2018' : c}}} for (x, a, b, c) in zip(model, sales_2016_int, sales_2017_int, sales_2018_int)]

cars_list = list(zip(brand, sales_list))
print(type(sales_list))
'''for k, v in cars_list:
    if k in cars.keys():
        cars[k].update({v})
    else:
        cars[k] = {v}'''
import pprint
pp = pprint.PrettyPrinter(depth=5)
pp.pprint(cars)
print(type(cars))
print(len(cars))
print(len(brand))

best_2017 = max(sales_2017_int)
ind_1 = sales_2017_int.index(best_2017)
answer1 = str(models[ind_1])

print(answer1)