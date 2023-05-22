from api import data
import bs4

romaji = data['data']['Media']['title']['romaji']
native = data['data']['Media']['title']['native']
english = data['data']['Media']['title']['english']
description = data['data']['Media']['description']

if not data['data']['Media']['nextAiringEpisode'] == None:
    airingepisodeavailable = "true"
    nextairingepisode = data['data']['Media']['nextAiringEpisode']['episode']
    airingAt = data['data']['Media']['nextAiringEpisode']['airingAt']
else:
    airingepisodeavailable = "false"



# Description Formatter
parserDesc = bs4.BeautifulSoup(description, "html.parser")
outputDescription = parserDesc.get_text()


print('\nNative: ' + native)
print('Romaji: ' + romaji)
print('English: '+ english)
print('Description: \n' + outputDescription)

if airingepisodeavailable == "true":
    print('Next Airing Episode: ' + str(nextairingepisode))
    print('Episode will air in: ' + str(airingAt))
