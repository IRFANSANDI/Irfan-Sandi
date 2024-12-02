# format string
# kata kunci f dan {}

# contoh generic
# string
nama = "amad dialo"
format_str = f"hallo {nama}"
print(format_str)
print("hallo" , nama)

# boolean
boolean = False
format_str = f"boolean" = {boolean}
print(format_str)

# angka
angka = 2005.5
format_str = f"angka {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"

# bilangan dengan ordo bilangan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3}"
print(format_str)

# menampilkan tanda + dan -
angka_minus = -10
angka_plus = +10.1234
format_str = f"minus = {angka_minus:.+d}"
format_str = f"plus = {angka_plus:.2f}"

print(format_minus)