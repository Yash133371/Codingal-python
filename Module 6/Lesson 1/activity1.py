def printPowerSet(s: list) -> None:
    setSize = len(s)

    powSetSize = 2**setSize

    for outer in range(powSetSize):
        for inner in range(setSize):
            if outer & (1 << inner) > 0:
                print(s[inner], end=" ")
        print()


def main() -> None:
    s = [int(i) for i in input("Enter the set: ").split()]

    printPowerSet(s)

if __name__ == "__main__":
    main()