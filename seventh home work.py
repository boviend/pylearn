# task 1 weather forecast for tomorrow
import requests

url = ("https://api.weatherapi.com/v1/forecast.json?key=b2e0030c0bd64a47baf202837241601&q=Гия-де-Исора&days=2&aqi=no"
       "&alerts=no")
response = requests.get(url)
data = response.json()

print(
    f"Tomorrow's weather forecast for Гия-де-Исора, Канарские Острова: {data['forecast']['forecastday'][1]['day']['condition']['text']}. The temperature will range from {data['forecast']['forecastday'][1]['day']['mintemp_c']}°C to {data['forecast']['forecastday'][1]['day']['maxtemp_c']}°C.")


# task 2


def primes(n):
    primes_list = []
    for num in range(2, n + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes_list.append(num)
    return primes_list


print(primes(10))


# task 3

def cube_generator(n):
    i = 1
    while i ** 3 <= n:
        yield i ** 3
        i += 1


print(list(cube_generator(1000)))
