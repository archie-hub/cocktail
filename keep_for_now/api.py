# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from make_cocktails.MakeDrinks import MakeDrinks


app = FastAPI(title="OC-compliant FastAPI")


origins = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


cabinet = "./drinkscabinet.txt"
receipes = "./receipes.json"
ourdrinks = MakeDrinks(receipes, cabinet)

@app.get("/")
def read_root():
    return {"message": "Hello from OpenShift-compliant FastAPI!"}

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/component/{drink}")
def read_root(drink):
    return ourdrinks.string_drink_receipe_with_an_ingredient(drink)

@app.get("/receipes")
def drinks_we_can_make_with_receipes_dictionary():
    return ourdrinks.drinks_we_can_make_with_receipes_dictionary
