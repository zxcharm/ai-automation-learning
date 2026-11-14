import requests

url = "https://api.github.com/users/zxcharm"

try:
    response = requests.get(url, timeout=10)
except requests.exceptions.RequestException as e:
    print("Ошибка запроса:", e)
    response = None

if response is not None:
    print("Статус:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        print("Логин:", data["login"])
        print("Публичных репозиториев:", data["public_repos"])
        print("Аккаунт создан:", data["created_at"])
    elif response.status_code == 404:
        print("Такого пользователя нет")
    else:
        print("Неожиданный ответ сервера:", response.status_code)