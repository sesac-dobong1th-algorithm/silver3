for i in range((n := int(input())), 0, -1):
    print(("*" * (2 * i - 1)).rjust(n + i - 1, " "))
