import requests

API_KEY = "fc475dca3916ee9f2f8b5928f5164dce"

def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]

    return filtered_data

if __name__ == '__main__':
    print(get_data(place='Guadalajara', days=2))