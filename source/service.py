import requests

database={
    1:"admin",
    2:"Alice",
    3:"Bob",
}

def get_user_from_database(id):
    return database.get(id)

def get_users(id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

