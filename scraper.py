"""

async def fetch_invite(self, *, with_counts: bool = True) -> Invite:
    invite_id = resolve_invite(self._invite)
    data = await self._state.http.get_invite(invite_id, with_counts=with_counts)
    return Invite.from_incomplete(state=self._state, data=data)

"""

import re, requests, random
from colorama import *

init()

HTTP = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text.strip().split('\n')
Words = eval(requests.get('https://raw.githubusercontent.com/3xq/Discord_Vanity_Checker/main/Words.txt').text)

Taken = open('Taken.txt', 'w+')
Not_Taken = open('Not_Taken.txt', 'w+')

def resolve_invite(Invite_URL):
    Regex_Pattern  =  r'(?:https?\:\/\/)?discord(?:\.gg|(?:app)?\.com\/invite)\/(.+)'
    Regex_Group    =  re.match(Regex_Pattern, Invite_URL)
    if Regex_Group:
        return Regex_Group.group(1)
    else:
        return Invite_URL

def get_invite(Invite_ID):
    Data = requests.get(
        f'https://discord.com/api/v9/invites/{Invite_ID}?with_counts=true&with_expiration=false',
        proxies = {
            'http': f'http://{random.choice(HTTP)}',
        }
    ).text

    if '<!DOCTYPE html>' in Data:
        get_invite(Invite_ID)
    else:
        if Data == '{"message": "Unknown Invite", "code": 10006}':
            return False
        else:
            return True

def fetch_invite(Invite_URL):
    Invite_ID = resolve_invite(Invite_URL)
    Data = get_invite(Invite_ID)
    return Data

for Vanity in Words:
    Vanity_Valid = fetch_invite(Vanity)

    if Vanity_Valid == True:
        Taken.write(f'discord.gg/{Vanity}\n')
        Taken.flush()
        print(f'[{Fore.RED}TAKEN{Style.RESET_ALL}]: discord.gg/{Vanity}')
    elif Vanity_Valid == False:
        Not_Taken.write(f'discord.gg/{Vanity}\n')
        Not_Taken.flush()
        print(f'[{Fore.GREEN}VALID{Style.RESET_ALL}]: discord.gg/{Vanity}')