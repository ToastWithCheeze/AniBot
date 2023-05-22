import requests
#import json # Uncomment this if you have enabled the whole json puller
url = 'https://graphql.anilist.co' 

query = '''
query ($search: String, $id: Int) {
  Media (search: $search, id: $id) {
    id
    title {
      romaji
      native
      english
    }
    description
    nextAiringEpisode {
      episode
      airingAt
    }
  }
}
'''
print("id or name")
useroption = input()

if useroption.lower() == "id":
    print("Enter Id: ")
    Id = input()
    print(Id)
    variables = {'id': Id}
elif useroption.lower() == "name":
    print("Enter Name: ")
    Name = input()
    variables = {'search': Name}
else:
    print("You didnt choose an option")
    exit()



def main_request():
    r = requests.post(url, json={'query': query, 'variables': variables})
    return r.json()

data = main_request()

#Debugger/Json info output to console, uncomment import json if this is enabled
# response = requests.post(url, json={'query': query, 'variables': variables})
# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

# jprint(response.json())


