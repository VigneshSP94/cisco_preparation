initial_input = input("Enter the String to check palindrome: ")

length = len(initial_input) - 1
count = 0

def check_pali(string2check):
    orig = string2check
    exact = ''
    reversed = ''

    for letter in orig:
        exact += letter
        reversed = exact[::-1]
        if len(exact) > 1:
            if exact == reversed:
                print(exact, "possible palindrom")


for word in range(length):
    check_pali(initial_input[count:length+1])
    count+=1

