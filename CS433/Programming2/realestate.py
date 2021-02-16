""" Sacramentorealestatetransactions.csv file row list indices:
0 - street
1 - city
2 - zip
3 - state
4 - beds
5 - baths
6 - sq_ft
7 - type (Residential, Condo, Multi-Family)
8 - sale_date
9 - price
10 - latitude
11 - longitude
"""

def rowGen(file):
    # Generator function for each row of a .csv file
    file.readline() #skip the first line of headers
    for row in file:
        yield row.split(',')

def minmaxNumFromString(arr:list):
    # Function to find the max integer value 
    #  from a list of strings
    #  returns min value followed by max value
    #  O(n)
    currMax = int(arr[0])
    currMin = int(arr[0])
    for val in arr:
        if int(val) > currMax:
            currMax = int(val)
        if int(val) < currMin:
            currMin = int(val)
    return currMin, currMax

def printPrices(estateType:str = '' ) -> None:
    #type:String
    file.seek(0) #reset file
    gen = rowGen(file) #reset generator

    if estateType == '':
        prices = [row[9] for row in gen]
    else:
        prices = [row[9] for row in gen if row[7] == estateType]
        if (len(prices) == 0):
            print('Valid Types are:\n')
    priceMax, priceMin = minmaxNumFromString(prices)

    if estateType == '':
        estateType = 'Real Estate'
    print(f'\nMin {estateType} Price: {priceMin}')
    print(f'Max {estateType} Price: {priceMax}')

    gen.close()
    return

if __name__ == '__main__':
    file = open('Sacramentorealestatetransactions.csv', 'r')

    #Get Residential Prices
    printPrices('Residential')

    #Get Condo Prices
    printPrices('Condo')

    #Get Multi-Family Prices
    printPrices('Multi-Family')

    #Get All Prices
    printPrices()

    file.close()