"""
Author: Sean Poston
Group: Ryan Custard, Jon Harsy, Timothy Schlottman
Date: 1/25/2021
Assignment: Check number of common members in a list (Question 2).
"""

def checkCommon(list1, list2) -> int:
    """
    Calculate the common members in list1 and list2 and return the int
    """
    if (len(list1) == 0 or len(list2) == 0):
        return 0
    list1.sort()
    list2.sort()
    i, j = 0, 0
    common = 0

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            common += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            if i < len(list1):
                i += 1
        else:
            if j < len(list2):
                j += 1
    #This solution should keep us below O(n2)
    return common

def main():
    list1 = ['sean', 'poston', 'string', 'tacocat', 'gyoza']
    list2 = ['poston', 'alfredo', 'spaghetti', 'gyoza', 'tacocat']
    
    print(f'There are {checkCommon(list1, list2)} common elements!')

main()