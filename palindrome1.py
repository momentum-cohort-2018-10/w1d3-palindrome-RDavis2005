palindrome = input("Enter a word:")

def isPalindrome(palindrome):
    for x in range(0, len (palindrome)):
        if palindrome[0 +1] == palindrome[0 -1]:
            return "This word is a palindrome!" 
        else:
            return "This word is NOT a palindrome!"  

print(isPalindrome(palindrome))