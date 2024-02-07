def hash_str(st):
    alfabet = 'ёйцукенгшщзхфывапролджэячсмитьбюъЁЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮЪ '
    d = {simbol: num for num, simbol in enumerate(alfabet, 1)}
    p = 67
    m = 10**9 + 9
    hash_st, i = 0, 0  
    for char in st:
        hash_st += d[char] * p**i
        i += 1
    return str(hash_st % m) 

fin = open('students_new.csv', 'r', encoding='utf-8') #открываем файл для чтения
title = fin.readline() # считываем строку с заголовками
# считываем данные из файла в список
students = [x.strip().split(',') for x in fin]
fin.close() # закрыть файл

fout = open('students_with_hash.csv', 'w', encoding='utf-8')
fout.write(title)
for x in students:
    fout.write(','.join((hash_str(x[1]), x[1], x[2], x[3], x[4])) + '\n')
fout.close()
 
