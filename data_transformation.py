"""Demonstrate common number and string transformations."""

x = 1
x = str(x)
b = x.zfill(3)
print(x)
print(b)



kata = "Hei python!"
kata = kata.upper()
print(kata , end=" = " )
if (kata.isupper()):
    print("HURUF KAPITAL")
else:
    print("null")
kata = kata.lower()
print(kata, end = " = ")
if (kata.isupper()):
    print("null")
else:
    print("huruf kecil")