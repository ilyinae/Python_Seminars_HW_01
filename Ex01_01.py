# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

days = ['Понедельник', 'Вторник','Среда', 'Четверг','Пятница','Суббота', 'Воскресенье']
days_num = ['1','2','3','4','5','6','7']                                #строки - чтобы не ловить ошибке на операции int(input()), в случае если введено неправильно    
day = input('Введите номер дня недели:')
if day not in days_num:                                                 #сначала обработаем исключения - все вводы, кроме цифр от 1 до 7
    print('В неделе только 7 дней :( - Введите номер от 1 до 7')
elif int(day) in range(1,6):
    print(f'Трудовые будни - {days[days_num.index(day)]}')              
else:
    print(f'Ура! Выходной! - {days[days_num.index(day)]}')


# То же, с использованием словаря:

# work_day_week = {
#     '1': 'Понедельник',
#     '2': 'Вторник',
#     '3': 'Среда',
#     '4': 'Четверг',
#     '5': 'Пятница',
#     '6': 'Cуббота',
#     '7': 'Воскресенье'
# }
# day = input('Введите номер дня недели:')
# if day not in work_day_week:
#     print('В неделе только 7 дней :( - Введите номер от 1 до 7')
# elif int(day) in range(1,6):
#     print(f'Трудовые будни - {work_day_week.get(day)}')
# else:
#     print(f'Ура! Выходной! - {work_day_week.get(day)}')
