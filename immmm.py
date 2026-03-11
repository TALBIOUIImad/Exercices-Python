def figure():
    while True:
        try:
            n = int(input("Entrez la taille de la figure (taille impaire >= 15) : "))
            if n >= 15 and n % 2 != 0:
                break
            else:
                print("Erreur : La taille doit être impaire et >= 15.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier.")
    width = 2 * n - 1
    height = n - 11
    def top_ligne():
        h = "#" * (n - 2)
        print(f"+{h}|{h}+")
    def middle():
        moin = "-" * (n - 2)
        print(f"#{moin}+{moin}#")
    def get_row_content(j):
        plus_count = 4 - j
        left_part = list(" " * (n - 1))
        left_part[0] = '#'  
        left_part[1] = ' '
        left_part[3] = '/'
        if plus_count >= 0:
            left_part[2] = '\\'
            if plus_count > 0:
                for k in range(plus_count):
                    if 4 + k < n - 1:
                        left_part[4 + k] = '+'
        left_str = "".join(left_part)
        center_char = "|"
        right_str = left_str[::-1].replace('\\', '/')
        return left_str + center_char + right_str
    print_top_bottom_border()
    for j in range(half_height - 1, -1, -1):
        print(get_row_content(j))
    print_middle_separator()
    for j in range(half_height):
        print(get_row_content(j))
    print_top_bottom_border()
if __name__ == "__main__":
   print(generate_figure())