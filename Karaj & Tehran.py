import re
import aiohttp
import asyncio
from bs4 import BeautifulSoup


ostan = int(input('che ostani?(alborz=1/tehran=2)'))


if ostan == 1 :
    ostan = 5
    shahr = int(input('che shahri?(karaj=1)')) 
    shahr = 43
    
elif ostan == 2 :
    ostan = 8
    shahr = int(input('che shahri?(varamin=1/pakdasht=2/eslamshahr=3/rey=4/tehran=5\n\
    /shahriar=6/damavand=7/rodehen=8/firuzkuh=9/malard=10)'))
    shahr += 52
    
    
sal = input('che sali?')
mah = input('che mahi?')
ruz = input('che ruzi?')


async def main() :
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session : 
        url = f'https://www.tabnak.ir/fa/prayer/time/{ostan}/{ostan}_{shahr}/{sal+mah+ruz}'
        async with session.post(url) as response:
            
            data = await response.text()
            bs = BeautifulSoup(data , 'html.parser')
            all_times = bs.div.text
            times = re.findall('\d',all_times)
            
            print(f'azane sonh = {times[0]}{times[1]}:{times[2]}{times[3]}:{times[4]}{times[5]}')
            print(f'tolu aftab = {times[6]}{times[7]}:{times[8]}{times[9]}:{times[10]}{times[11]}')
            print(f'azane zohr = {times[12]}{times[13]}:{times[14]}{times[15]}:{times[16]}{times[17]}')
            print(f'ghorub aftab = {times[18]}{times[19]}:{times[20]}{times[21]}:{times[22]}{times[23]}')
            print(f'azane maghreb = {times[24]}{times[25]}:{times[26]}{times[27]}:{times[28]}{times[29]}')
            print(f'nimeh shab sharii = {times[30]}{times[31]}:{times[32]}{times[33]}:{times[34]}{times[35]}')

            
loop = asyncio.get_event_loop()
loop.run_until_complete(main())



#:)