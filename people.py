import math

#слив акций
def sale(companies, packages):
    prices = []
    price = 0
    for package in packages: 
        for i in package:
            for j in companies:
                if j[0] == i[0]: price += i[1] * j[-1][-1]
        prices.append(price)
        price = 0

    return prices

#Евгений
def Evgeniy(list_of_company, sale):
    sum = 0
    res = []
    for i in list_of_company: sum += i[2] * i[-1][-1]
    for i in list_of_company: res.append([i[0], (i[2] * i[-1][-1] / sum) * sale // i[-1][-1]])
    return res

#Анатолий
def Tolian(list_of_company, sale):
    couples = []

    for i in range(len(list_of_company) // 2, len(list_of_company)):
        for j in range(0, len(list_of_company) // 2):
            if ((list_of_company[j][-1][0] < list_of_company[j][-1][-1]) 
                and (list_of_company[i][-1][0] < list_of_company[i][-1][-1]) 
                and i != j):

                k = math.fabs(correlation(list_of_company[i][-1], list_of_company[j][-1]))
                if len(couples) < 3: couples.append([k, i, j])
                else:
                    max = 0
                    for index in range(len(couples)):
                        if couples[index][0] > couples[max][0]: max = index
                    couples[max] = [k, i, j]

    package = []
    sale /= 6
    for i in couples:
        package.append([list_of_company[i[1]][0], (sale) // list_of_company[i[1]][-1][-1]])
        package.append([list_of_company[i[2]][0], (sale) // list_of_company[i[2]][-1][-1]])
    return package

#Андрей 
def Andrei(list_of_company, sale):    
    couples = []

    for i in range(len(list_of_company) // 2, len(list_of_company)):
        for j in range(0, len(list_of_company) // 2):
            if ((list_of_company[j][-1][0] < list_of_company[j][-1][-1]) 
                and (list_of_company[i][-1][0] < list_of_company[i][-1][-1]) 
                and i != j):

                k = math.fabs(correlation(list_of_company[i][-1], list_of_company[j][-1]))
                if len(couples) < 3: couples.append([k, i, j])
                else:
                    min = 0
                    for index in range(len(couples)):
                        if couples[index][0] < couples[min][0]: min = index
                    couples[min] = [k, i, j]

    package = []
    for i in couples:
        package.append([list_of_company[i[1]][0], (sale / 6) // list_of_company[i[1]][-1][-1]])
        package.append([list_of_company[i[2]][0], (sale / 6) // list_of_company[i[2]][-1][-1]])
    return package

#корреляция
def correlation(list_1, list_2):
    average_one = sum(list_1) / len(list_1)
    average_two = sum(list_2) / len(list_2)
    disp_1 = 0
    disp_2 = 0
    disp_3 = 0

    for i in range(len(list_1)):
        disp_1 += math.pow(list_1[i] - average_one, 2)
        disp_2 += math.pow(list_2[i] - average_two, 2)
        disp_3 += (list_2[i] - average_two) * (list_1[i] - average_one)

    return disp_3 / (math.sqrt(disp_1 * disp_2))
