c = input("Nhập chữ cái hoa: ")

lower = c.lower()   # đổi sang chữ thường

if lower == 'a':
    print('z')
else:
    print(chr(ord(lower) - 1))