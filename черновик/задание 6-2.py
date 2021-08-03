goods = []
features = {'наименование': '', 'цена': '', 'колличество': '', 'ед.изм': ''}
analytics = {'наименование': [], 'цена': [], 'колличество': [], 'ед.изм': []}
num = 0
feature_ = None
control = None
while True:
    control = input('Для выхода нажмите "Q" , для продолжения нажмите "Enter", для аналитики нажмите "A":').upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Аналитика \n')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Функция ввода "{f}"')
        features[f] = int(feature_) if (f == 'цена' or f == 'колличество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
