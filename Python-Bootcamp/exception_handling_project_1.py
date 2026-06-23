
import requests
def json():
    try:
        response = requests.get("https://jsonplaceholder.typicodie.com/todos/")
        response.raise_for_status()
    except requests.exceptions.RequestException:
        err = "Failed to connect to server"
        return err
    else:
        # This runs ONLY if the network call was 100% successful.
        # If 'user' is missing here, the app crashes loudly (which we want, so we can fix the bug).
        user_data = response.json()[1]["title"]
        return user_data
print(json())