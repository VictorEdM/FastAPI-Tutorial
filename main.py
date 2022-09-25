from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

persons_db = {
    1: {
        "name": "Carl Scott",
        "age": 32,
        "addresses": {
            1: {
                "street": "Thunder Street",
                "number": 2
            },
            2: {
                "street": "Bradley Hall",
                "number": 665
    
            },
            3: {
                "street": "Locktown",
                "number": 78
        
            }
    
        }
    },
    2: {
        "name": "John Bon",
        "age": 45,
        "addresses": {
            1: {
                "street": "St. Gobain",
                "number": 35
            },
            2: {
                "street": "Milwaukee",
                "number": 10
            }
        }
    },
    3: {
        "name": "Melissa Andrews",
        "age": 28,
        "addresses": {
            1: {
                "street": "Thunder Street",
                "number": 2
            }
        }
    },
    4: {
        "name": "Jim Terry",
        "age": 22,
        "addresses": {
            1: {
                "street": "Ball valley",
                "number": 478
            },
            2: {
                "street": "Harley Mills",
                "number": 145
            }
        }
    },
    5: {
        "name": "Sarah Bills",
        "age": 48,
        "addresses": {
            1: {
                "street": "Catle bar",
                "number": 659
            },
            2: {
                "street": "Langdon Paris",
                "number": 14
            }
        }
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
            <li>Addresses of a person, given the ID: http://localhost:800/persons/id/addresses</li>
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


@app.get("/persons/{person_id}/addresses")
def findAllAddress(person_id: int):
    return persons_db.get(person_id).get("addresses")
    

    