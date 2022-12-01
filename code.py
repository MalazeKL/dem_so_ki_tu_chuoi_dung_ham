def count_chars(txt):
    count = 0
    for char in txt:
        count += 1
    return count
txt = input("Nhập chuỗi: ")
print("trong chuỗi có {count} kí tự". format(count = count_chars(txt)))
