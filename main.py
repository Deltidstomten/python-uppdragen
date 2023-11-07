"""
namn = "Elias"
nummer = 4

nummer2 = 8

nummer3 = nummer + nummer2

print("Hej! blalbal")

nummer = input()
nummer2 = input()

print(int(nummer) + int(nummer2))
"""

nummer = int(input())

if nummer < 10:
    print("Numret är mindre än 10!")

if nummer > 10:
    print("Numret är större än 10!")

if nummer == 10:
    print("Numret är 10")

if nummer < 10:
    print("Numret är mindre än 10!")
elif nummer > 10:
    print("Numret är större än 10!")
else:
    print("Numret är 10")
    