# Создайте список, включающий минимум трех людей, которых вам
# хотелось бы пригласить на обед.
people = ['Sultan', 'Aitunuk', 'Zamira']
# Затем используйте этот список для вывода пригласительного сообщения
# каждому участнику.
for person in people:
    print(f'Привет, {person}! Хочу пригласить тебя на ужин в это воскресенье')


print(f'{people[0]} к сожалению, прийти не сможет')
people.remove('Sultan')
people.insert(0, 'Emir')
print(people)

for person in people:
    print(f'Привет, {person}! Хочу пригласить тебя на ужин в это воскресенье')

print('Список гостей расширяется!')
people.insert(0, 'Bekbolot')
people.insert(2, 'Bakyt')
people.append('Samat')
for person in people:
    print(f'Привет, {person}! Хочу пригласить тебя на ужин в это воскресенье')

print('К сожалению стол привезти не успели! Приглашаются только 2 гостя.')
print(f'{len(people)} - это много, надо уменьшить список')

for person in people[:1:-1]:
    people.pop()
    print(f'{person}, мы сожалеем об отмене')

del people[1]
del people[0]