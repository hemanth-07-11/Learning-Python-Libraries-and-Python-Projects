def moveTower(height, fromPole, toPole, withPole):

    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)

def main():
    height = int(input("Height of hanoi: ").strip())
    moveTower(height, "A", "B", "C")


if __name__ == "__main__":
    main()
