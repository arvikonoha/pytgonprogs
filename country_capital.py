class country:
    def __init__(self, name, capital, population):
        self.__name = name
        self.__capital = capital
        self.__population = int(population)

    def getpop(self):
        return self.__population

    def getname(self):
        return self.__name

    def getcap(self):
        return self.__capital


def findcap(lst, name):
    for country in lst:
        if country.getname() == name:
            return country.getcap()
    else:
        return None


countries = []

while True:
    choice = input("Enter your choice (add,capital-country,top-country,exit) ")
    if choice == "add":
        countries.append(
            country(input("Enter the country's name "),
                    input("Enter the country's capital "),
                    input("Enter the country's population ")))
    elif choice == "country-country":
        capital = findcap(countries, input("Enter the name of the country "))
        if capital != None:
            print("The capital is ", capital)
        else:
            print("There is no such country")
    elif choice == "top-country":
        countries = sorted(countries, key=country.getpop, reverse=True)
        if len(countries) != 0:
            print("The most populous country is ", countries[0].getname())
        else:
            print("List is empty")
    elif choice == "exit":
        break
    else:
        print("There is no such choice")