import requests

answer = requests.get(
    url="https://fr.wikipedia.org/w/api.php",
    params={
        "action": "query",
        "format": "json",
        "prop": "categories",
        "titles": "Bruxelles"
    },
).json()

for category in list(answer["query"]["pages"].values())[0]['categories']:
    print(category)

print('---')

params = {
        "action": "query",
        "format": "json",
        "prop": "categories",
        "titles": "Bruxelles"
}

while True:
    answer = requests.get(
        url="https://fr.wikipedia.org/w/api.php",
        params=params,
    ).json()

    for category in list(answer["query"]["pages"].values())[0]['categories']:
        print(category)

    if "batchcomplete" in answer:
        break

    params["continue"] = answer["continue"]["continue"]
    params["clcontinue"] = answer["continue"]["clcontinue"]

print('---')

params = {
        "action": "query",
        "format": "json",
        "prop": "categories",
        "titles": "Bruxelles"
}

page = """== Catégories ==

"""

while True:
    answer = requests.get(
        url="https://fr.wikipedia.org/w/api.php",
        params=params,
    ).json()

    for category in list(answer["query"]["pages"].values())[0]['categories']:
        page = page + f"""* [[:{category["title"]}]]
"""

    if "batchcomplete" in answer:
        break

    params["continue"] = answer["continue"]["continue"]
    params["clcontinue"] = answer["continue"]["clcontinue"]

answer = requests.get(
    url="https://fr.wikipedia.org/w/api.php",
    params={
        "action": "query",
        "format": "json",
        "prop": "",
        "meta": "tokens"
    },
).json()

answer = requests.post(
    url="https://fr.wikipedia.org/w/api.php",
    data={
        "action": "edit",
        "format": "json",
        "title": "Arktest/test",
        "section": "new",
        "sectiontitle": "Test",
        "text": page,
        "summary": "Testons",
        "token": answer["query"]["tokens"]["csrftoken"]
    }
).json()

print(answer)
