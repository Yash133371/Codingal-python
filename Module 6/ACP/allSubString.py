def printSubStrings(strn: str) -> None:
    strnSize = len(strn)

    powStrnSize = 2**strnSize

    for outer in range(powStrnSize):
        for inner in range(strnSize):
            if outer & (1 << inner) > 0:
                print(strn[inner], end="")
        print()


strn = input("Enter a string: ")

printSubStrings(strn)