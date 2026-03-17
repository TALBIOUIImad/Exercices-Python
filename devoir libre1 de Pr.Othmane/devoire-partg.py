def error_handler(n):
    if n < 15:
        return False, "nombre non valide, inférieur à 15"
    if n % 2 == 0:
        return False, "nombre non valide, pair"
    return True, None


def algorithm(n):
    mid = n // 2
    stable = 4

    for y in range(n):
        for x in range(n):
            c = " "

            # Coins
            if (x, y) in [(0, 0), (0, n-1), (n-1, 0), (n-1, n-1)]:
                c = "+"

            # Bordures
            elif (y == 0 or y == n-1) and x != mid:
                c = "#"
            elif x == 0 or x == n-1:
                c = "#"

            # Ligne verticale centrale
            elif x == mid and y not in (mid, mid-1, mid+1):
                c = "|"

            # Ligne horizontale centrale
            elif y == mid:
                c = "-"

            # Centre
            elif (x == mid and y == mid) or abs(x - mid) == 4 and y == mid:
                c = "+"

            # Bloc central +
            elif y < mid:
                d = mid - y
                if d <= 4 and abs(x - mid) <= (5 - d):
                    c = "+"
            elif y > mid:
                d = y - mid
                if d <= 4 and abs(x - mid) <= (5 - d):
                    c = "+"

            # Diagonales \
            elif (y < mid and x + stable == mid - (mid - y - 1)) or \
                 (y > mid and x - stable == mid + (y - mid - 1)):
                c = "\\"

            # Diagonales /
            elif (y < mid and x - stable == mid + (mid - y - 1)) or \
                 (y > mid and x + stable == mid - (y - mid - 1)):
                c = "/"

            print(c, end=" ")
        print()


def main():
    n = int(input("Entrez la taille de la figure (impaire ≥ 15) : "))
    ok, msg = error_handler(n)
    if not ok:
        print(msg)
    else:
        algorithm(n)


main()