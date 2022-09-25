from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from person import Person
from address import Address
import json


app = FastAPI()


persons_db = [
    Person(name="Carl Scott", age=32, addresses=[
        Address(name="Thunder Street", number=2),
        Address(name="Bradley Hall", number=665),
        Address(name="Locktown", number=78)
    ]
    ),
    Person(name="John Bon", age=45, addresses=[
        Address(name="St. Gobin", number=35),
        Address(name="Milwaukee", number=10)
    ]
    ),
    Person(name="Melissa Andrews", age=28, addresses=[
        Address(name="Thunder Street", number=15)
    ]
    ),
    Person(name="Jim Terry", age=22, addresses=[
        Address(name="Ball valley", number=478),
        Address(name="Harley Mills", number=147)
    ]
    ),
    Person(name="Sarah Bills", age=48, addresses=[
        Address(name="Catle Bar", number=659),
        Address(name="Langdon Park", number=14)
    ]
    )
]


@app.get('/', response_class=HTMLResponse)
def home():
    return """
    <div>
        <h1>Home</h1>
        <p>This is the home page, feel free to access any other endpoint available</p>
        <ul>
            <li>All persons registered: http://localhost:8000/persons</li>
            <li>Individual person based on given numeric ID: http://localhost:8000/persons/id</li>
            <li>Addresses of a person, given the ID: http://localhost:800/persons/id/addresses</li>
            <li>The API auto generated documentation: http://localhost:8000/docs</li>
        </ul>
    </div>
    """


@app.get("/persons")
def find_all():
    if len(persons_db) > 0:
        return persons_db
    return {"Error": "No person registered"}


@app.get("/persons/{person_id}")
def find_by_id(person_id: int):
    if len(persons_db) >= person_id-1 >= 0:
        return persons_db[person_id-1]
    return {
        "Error": "Person not found",
        "Id": person_id
    }


@app.get("/persons/{person_id}/addresses")
def find_all_addresses(person_id: int):
    if len(persons_db) >= person_id-1 >= 0:
        if len(persons_db[person_id].addresses) > 0:
            return persons_db[person_id-1].addresses
        return {"Error": "This person doesn't have any address registered"}
    return {"Error": "Person not Found", "Id": person_id}


@app.post("/persons")
def add_person(request: Person):
    persons_db.append(request)
    return request
