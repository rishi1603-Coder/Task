
def is_palindrome(string):
    clean_string = ''.join(string.split()).lower()
    return clean_string == clean_string[::-1]

user_input = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome!')
else:
    print(f'"{user_input}" is not a palindrome.')

    
Output:
Enter a string to check if it's a palindrome: hello
"hello" is not a palindrome.
Enter a string to check if it's a palindrome: madam
"madam" is a palindrome!
