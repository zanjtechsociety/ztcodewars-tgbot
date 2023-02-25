import asyncio

from emoji import emojize
import requests


def get_user_stats(username):
    url = f"https://www.codewars.com/api/v1/users/{username}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        raise ValueError("Failed to get user. Maybe there was an error in url")


def get_stats(username):
    try:
        stats = get_user_stats(username)
        output = []

        output.append(f'Name:\t {stats["name"]}')
        output.append(f'Clan:\t {stats["clan"]}')
        output.append(f'Honor:\t {stats["honor"]}')
        languages = stats["ranks"]["languages"].keys()
        output.append(f'Languages:\t {", ".join(languages)}')
        output.append(f'Score:\t {stats["ranks"]["overall"]["score"]}')
        rank = stats["ranks"]["overall"]
        rank_color = f':{rank["color"]}_circle:'
        output.append(f'Rank:\t {emojize(rank_color)} {rank["name"]}')
        output.append(f'Completed:\t {stats["codeChallenges"]["totalCompleted"]}')
        return "\n".join(output)
    except ValueError as e:
        return e.__repr__()
