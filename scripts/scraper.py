import requests
from bs4 import BeautifulSoup
import json
import time
from collections import defaultdict

USERS_LINK = 'https://myanimelist.net/users.php/'

def get_users(url,number_of_users=1000):

    master_user_list = []

    users_queried = 0
    number_of_iterations = 0

    while len(master_user_list) < number_of_users:

        number_of_iterations += 1

        print(number_of_iterations)

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            users = [a.get_text(strip=True) for a in soup.select('a[href^="/profile/"]')]

            # There is always one user who is '' so I have to ignore that
            _ = [master_user_list.append(user) for user in users if user != '']

            master_user_list = list(set(master_user_list))

            users_queried += len(master_user_list)


    return master_user_list

def write_data(file, name, extension, location='./data'):

    if extension == 'txt':
        with open(f'{location}/{name}.{extension}', 'w') as output:
            output.write(str(file))

    elif extension == 'json':
        with open(f'{location}/{name}.{extension}', 'w') as json_file:
            json.dump(file, json_file, indent=4)
    
    else:
        print('Please add a supported extension type.')
    


def get_user_data(list_of_users):
    status = 2
    user_data = defaultdict(dict)

    for user in list_of_users:
        print(user)
        offset = 0

        while True:
            # This is to not get banend
            time.sleep(3)
            url = f"https://myanimelist.net/animelist/{user}/load.json"
            params = {"offset": offset, "status": status}
            response = requests.get(url, params=params)

            try:
                data = response.json()
            except ValueError:
                print(f"{user}: Does not have a valid JSON")
                break

            if not isinstance(data, list):
                print(f"{user}: returned {type(data)}. likely private or invalid")
                break

            if not data:
                break

            for item in data:
                user_data[user][item["anime_title"]] = item["score"]

            offset += 300

    return dict(user_data)



if __name__ == '__main__':
    users = get_users(url=USERS_LINK)
    write_data(file=users,
               name='usernames',
               extension='txt')
    
    user_data = get_user_data(users[:100])
    write_data(file=user_data,
               name='data',
               extension='json')
    

