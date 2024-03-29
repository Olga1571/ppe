"""
Все ребята сдали свои проекты и получили оценки на защите, но Хадаров Владимир все прослушал 
и просит помочь ему узнать какую оценку за проект он получил. Пожалуйста, подскажите 
Владимиру какую оценку он получил. Формат вывода: Ты получил: <ОЦЕНКА>, за проект - <id>
Пока помогали Владимиру увидели, что многие ученики потеряли свои оценки при выкачке с 
сайта. Из-за этого нет возможности посмотреть общую статистику. Чтобы избежать путаницы 
поставьте вместо ошибки среднее значение по классу и округлите до трех знаков после запятой. 
Сохраните данные в новую таблицу с названием student_new.csv.
"""
# открыть файл с данными(имя файла, режим открытия файла, кодировка)
fin = open('students.csv', 'r', encoding='utf-8')
title = fin.readline() # считать строку с заголовками
#print(title)
students = [x.strip().split(',') for x in fin] # считываем данные из файла в двумерный массив
fin.close() # закрыть файл
bal_sum = {} # bal_sum{key - номер класса, value - сумма оценок}
bal_cnt = {} # bal_сnt{key - номер класса, value - количество оценок}
for x in students: # просмотр всех записей
    # x[0] - порядковый №
    # x[1] - ФИО
    # x[2] - № проекта
    # x[3] - класс
    # x[4] - оценка за проект
    if x[4] != 'None': # если оценка отсутствует, в алфавитно частноный словарь собираем сумму оценок и их количество
        if x[3] in bal_sum: 
            bal_sum[x[3]] += int(x[4])
            bal_cnt[x[3]] += 1
        else:
            bal_sum[x[3]] = int(x[4])
            bal_cnt[x[3]] = 1
    
    fio = x[1].split() # разбиваем ФИО на фамилию, имя, отчество отдельно
    if fio[0] == 'Хадаров' and fio[1] == 'Владимир': # ответ на 1 задачу
        print(f'Ты получил: {x[4]}, за проект – {x[2]}')

for x in students: # просмотр всех записей
    if x[4] == 'None': # если оценка отсутсвует, заменяем None на среднюю оценку по классу
        x[4] = f'{bal_sum[x[3]] / bal_cnt[x[3]]:.3f}'

fout = open('students_new.csv', 'w', encoding='utf-8') # открываем файл для записи
fout.write(title) # записываем строку с заголовком в файл
for x in students: # записываем данные в файл
    fout.write(','.join(x) + '\n')
fout.close() # закрываем файл students_new.csv



