"""
Author: Sean Poston
Group: Ryan Custard, Jon Harsy, Timothy Schlottman
Date: 1/25/2021
Assignment: Count strings where n > 2 and palindrome (Question 1).
"""

def isPalindrome(string: str) -> bool:
    """
    Function will return true if given string is 
    a palindrome and len(string)>2
    """
    if (len(string) < 2):
        return False
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    
    return True
    

def main():
    checkList = ['abdefc', 'xygyz', 'abeba', '123321']
    count = 0

    #Send each string to the function to check if it's a palindrome
    for string in checkList:
        if isPalindrome(string):
            count += 1
    
    print(f'There are {count} palindromes!')

main()