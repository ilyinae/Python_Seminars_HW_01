# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

days = ['Понедельник', 'Вторник','Среда', 'Четверг','Пятница','Суббота', 'Воскресенье']
days_num = [1,2,3,4,5,6,7]
day = int(input('Введите номер дня недели:'))
day_name = days[days_num.index(day)]
if day in range(6):
    print(f'Трудовые будни - {day_name}')
elif day in [6,7]:
    print(f'Ура! Выходной! - {day_name}')
else:
    print('В неделе только 7 дней :( Введите номер от 1 до 7')