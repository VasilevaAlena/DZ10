import requests


def superhero_stats(name, powerstats):
    dict_new = {}
    for n in name:
        response = requests.get('https://superheroapi.com/api/2619421814940190/search/' + n)
        response.raise_for_status()
        results = response.json()['results']
        for result in results:
            if n == result['name']:
                id_name = result['id']
                response = requests.get('https://superheroapi.com/api/2619421814940190/' + id_name + '/powerstats')
                response.raise_for_status()
                stats = int(response.json()[powerstats])
                dict_new[n] = stats
            else:
                break
    return dict_new


def main():
    name = list(
        input('Введите имена супергероев, через запятую (Например: Hulk,Captain America,Thanos): ').title().split(','))
    powerstats = input(
        'Введите статистические данные, которые хотите сравнить, одно из списка: Intelligence, Strength, Speed, '
        'Durability, Power, Combat: ').lower()
    dict_new = superhero_stats(name, powerstats)
    max_value = max(dict_new.values())
    max_dict = {k: v for k, v in dict_new.items() if v == max_value}
    for k, v in max_dict.items():
        print(f'Супергерой - {k} самый "{powerstats}" - {v}')

main()
