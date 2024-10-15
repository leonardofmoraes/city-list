cityList = []  # list = list()
numCities = int(input("Enter the number of cities: "))
while len(cityList) != numCities:
    city = input("Enter the city you want to store: ").lower()
    cityList.append(city)