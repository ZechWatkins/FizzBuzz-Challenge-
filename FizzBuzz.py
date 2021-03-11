def main():
    for num in range(1,101):
        line=""
        if num % 3 == 0:
            line = line + 'Fizz'
        if num % 5 == 0:
            line = line + 'Buzz'
        if (num % 3 != 0) and (num % 5 != 0):
            line = line + str(num)
        print(line)
main()