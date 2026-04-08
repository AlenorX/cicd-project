import requests
import json
import random


class RandomAnimalFact():
    def GetFact(self):
        count = random.randint(10, 90)
        response = requests.get(f'https://catfact.ninja/fact?max_length={count}')
        result = json.loads(response.content)
        if result is None:
            return "Ошибка"
        else:
            return result['fact']
    
class RandomStudioFact():
    def GetFact(sefl):
        with open('source.txt', 'r+', encoding="UTF-8") as file:
            text = file.readlines()
            randomLine = random.choice(text)
            return randomLine

