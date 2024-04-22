from src.functions import get_repos_stats
from src.postgres_db import PostgresDB

import os
from dotenv import load_dotenv



load_dotenv()

db_config = {
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORT'),
    'dbname': os.getenv('POSTGRES_DB')
}


def main():
    data = get_repos_stats('skypro-008')
    db = PostgresDB(**db_config)
    db.insert_data(data)

    for item in db.get_data(5, 'forks'):
        print(item)

    db.export_to_json()


if __name__ == '__main__':
    main()

def entry_point(name: str):
    # Use a breakpoint in the code line below to debug your script.
    stats = get_repos_stats(name)
    print(stats)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    entry_point('TheShadowfish')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
