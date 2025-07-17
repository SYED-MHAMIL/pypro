# import requests
# api_key = f"https://api.openweathermap.org/assistant/session={'009c1b8153d412f26f732d0fe3a4f72'}"
# headers={'Content-Type':'applicaion/json'}
# payload={
#     'message': "what is weather todya"
# }
# response= requests.post(api_key,json=payload,headers=headers)
# if response.status_code == 200:
#     # d=response.json()
#     # print(d)
#     print("hello")


import requests

API_KEY = '009c1b8153d412f26f732d0fe3a4f72'  # replace with your OpenWeatherMap API key

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        return f"The current temperature in {city} is {temp}°C with {description}."
    elif response.status_code == 404:
        return "City not found. Please try another city."
    else:
        return "Failed to retrieve weather data."

def weather_assistant():
    print("Hello! I'm your Weather Assistant. Ask me about the weather in any city.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Assistant: Goodbye!")
            break
        else:
            # Simple extraction of city from the message
            if "weather in" in user_input.lower():
                parts = user_input.lower().split("weather in")
                city = parts[1].strip().capitalize()
                weather_info = get_weather(city)
                print(f"Assistant: {weather_info}")
            else:
                print("Assistant: Please ask me like 'What is the weather in [city]'.")

if __name__ == "__main__":
    weather_assistant()
