from fastapi import FastAPI, Body
import data

app = FastAPI()

@app.get('/random/information')
def root():
    return {"status": True, "message": "CI/CD Project - мой репозиторий, который позволяется понять работу CI/CD + GitLab. Этот микросервис отправляет случайный факт обо всём. Данный репозиторий создан для образовательных целей"}


@app.get('/random/get')
def random():
    factAboutCat = data.RandomAnimalFact()
    factAboutStudio = data.RandomStudioFact()
    return {"status": True, "factCat": factAboutCat.GetFact(), "factStudio": factAboutStudio.GetFact()}


@app.get('/random/status')
def status():
    return {"status": True, "message": "Microservice is alive"}

