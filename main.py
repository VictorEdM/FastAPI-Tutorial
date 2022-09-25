from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

persons_db = {
    1: {
        "name": "Carl Scott",
        "age": 32
    },
    2: {
        "name": "John Bon",
        "age": 45
    },
    3: {
        "name": "Melissa Andrews",
        "age": 28
    },
    4: {
        "name": "Jim Terry",
        "age": 22
    },
    5: {
        "name": "Sarah Bills",
        "age": 48
    }
}


@app.get('/', response_class=HTMLResponse)
def home():
    return """
    <div>
        <h1>Home</h1>
        <p>This is the home page, feel free to access any other endpoint available</p>
        <ul>
            <li>All persons registered: http://localhost:8000/persons</li>
            <li>Individual person based on given numeric ID: http://localhost:8000/persons/id</li>
            <li>The API auto generated documentation: http://localhost:8000/docs</li>
        </ul>
    </div>
    """


@app.get("/persons")
def findAll():
    return persons_db



@app.get("/persons/{person_id}")
def findById(person_id: int):
    return persons_db.get(person_id, {
        "Error": "Person not found",
        "Id": person_id
    })

    