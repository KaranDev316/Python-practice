
import requests
def json():
    url = "https://jsonplaceholder.typicodie.com/todos/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()[1]["title"]
    except requests.exceptions.ConnectionError:
        print("[Log] Connection failed. Please check the URL or your network.")
        return None
    else:
        # This runs ONLY if the network call was 100% successful.
        # If 'user' is missing here, the app crashes loudly (which we want, so we can fix the bug).
        user_data = response.json()[1]["title"]
        return user_data
print(json())