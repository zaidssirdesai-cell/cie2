import sys


def calculate(n1, n2, n3):
    total = n1 + n2 + n3
    avg = total / 3
    per = (total / 300) * 100
    return total, avg, per


if __name__ == "__main__":
    if len(sys.argv) >= 4:
        n1 = float(sys.argv[1])
        n2 = float(sys.argv[2])
        n3 = float(sys.argv[3])

    total, avg, per = calculate(n1, n2, n3)
    print("Total:")
    print(total)
    print("Average:")
    print(avg)
    print("Percentage:")
    print(per)
