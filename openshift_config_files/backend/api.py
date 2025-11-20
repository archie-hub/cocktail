#Openshift is a little different so needed to borrow some of this :)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from make_cocktails.MakeDrinks import MakeDrinks


app = FastAPI(title="OC-compliant FastAPI")


origins = [
    "http://127.0.0.1:8080",  # or wherever your frontend runs
    "http://localhost:8080",
    "*"  # you can use this during development to allow all
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # allowed origins
    allow_credentials=True,
    allow_methods=["*"],            # allow all HTTP methods
    allow_headers=["*"],            # allow all headers
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
