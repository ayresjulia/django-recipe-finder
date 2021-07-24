import requests

ALLRG_BASE_URL = "https://60f5adf918254c00176dffc8.mockapi.io/api/v1/allergens/"

# helper function to get a list of BIG-8 allergens for the form select field


def get_allergens():
    responses = requests.get(ALLRG_BASE_URL)
    if responses.status_code == 200:
        res = responses.json()
        allergens = []
        count = 0
        for allrg in res:
            count = count + 1
            allergens.append((allrg['name'], allrg['name']))
    return tuple(allergens)
