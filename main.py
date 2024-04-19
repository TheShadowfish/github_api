from src.functions import get_repos_stats


def entry_point(name: str):
    # Use a breakpoint in the code line below to debug your script.
    stats = get_repos_stats(name)
    print(stats)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    entry_point('TheShadowfish')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
