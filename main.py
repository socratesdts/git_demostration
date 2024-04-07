# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm# /
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="APIs en clase de Mlops 5",
    version="0.0.1"
)

@app.post("/api/v1/users", status_code=201)
async def create_user(username: str, name: str):
    user_id = str(uuid.uuid4())
    # Aquí deberías insertar los datos del usuario en tu almacenamiento o base de datos.
    # Por ahora, sólo devolveremos un ID simulado.
    return {
        "username": username,
        "name": name,
        "ID": user_id,
        "message": "The user was created successfully",
    }

@app.get("/api/v1/users/{user_id}")
async def get_user(user_id: str):
    users = {
        "hola43443": {
            "username": "asdelgado",
            "name": "asdelgado506"
        },
        "ide-67": {
            "username": "andrey",
            "name": "andrey506"
        }
    }

    user = users.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    return JSONResponse(
        content=user,
        status_code=status.HTTP_200_OK
    )




