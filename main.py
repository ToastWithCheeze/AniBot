from api import data
import bs4

romaji = data['data']['Media']['title']['romaji']
native = data['data']['Media']['title']['native']
english = data['data']['Media']['title']['english']
description = data['data']['Media']['description']

# Description Formatter
parserDesc = bs4.BeautifulSoup(description, "html.parser")
outputDescription = parserDesc.get_text()


print('\nNative: ' + romaji)
print('Romaji: ' + native)
print('English: '+ english)
print('Description: \n' + outputDescription)
