#Есть два списка
#Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
#Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
# чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None)

from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Владимир', 'Станислав', 'Leo']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


tutors_klasses = (i for i in zip_longest(tutors, klasses[:len(tutors)]))

print(*tutors_klasses)
print(type(tutors_klasses))
print(list(tutors_klasses))