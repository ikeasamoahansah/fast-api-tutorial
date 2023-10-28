from fastapi import FastAPI


app = FastAPI()

users = {
    1: {
        'first_name': 'Ike',
        'last_name': 'Asamoah',
        'age': 19
    },
    2: {
        'first_name': 'Ruby',
        'last_name': 'Arthur',
        'age': 53
    },
    3: {
        'first_name': 'Ekow',
        'last_name': 'Arthur',
        'age': 21
    }
}


@app.get('/users')
def getAllUsers():
    return users


@app.get('/user/{user_id}')
def getUser(user_id: int):
    return users[user_id]
