import requests


def superheroes(names):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    data_superheroes = response.json()
    new_dict = {}
    for name in names:
        for data in data_superheroes:
            if name == data['name']:
                superhero_intellegence = data['powerstats']['intelligence']
        new_dict[name] = superhero_intellegence
    cleverest_hero = max(new_dict, key=new_dict.get)
    print(f'Самый умный супергерой - {cleverest_hero}, его интеллект равен {new_dict[cleverest_hero]}')

if __name__ == '__main__':
    superheroes(['Hulk', 'Captain America', 'Thanos'])


