from fastapi import FastAPI, HTTPException, Request, status  
import uuid

app = FastAPI()

# List to store tank objects
tanks = []

# Routes
@app.get("/tank")
async def get_tanks():
    return tanks

@app.get("/tank/{id}")
async def get_tank_id(id:str):
    for i in tanks:
        if i["id"]==id:
            return i
        raise HTTPException(status_code=404, detail="Tank not found")
    
@app.post("/tank", status_code=status.HTTP_201_CREATED)
async def add_tank(request:Request):
    newtank = await request.json()
    new_id = uuid.uuid4() 

    newtank = {"id":str(new_id), **newtank}
    tanks.append(newtank)
    return(newtank)

@app.patch("/tank/{id}", status_code=status.HTTP_200_OK)
async def fix_tanks(id:str, request: Request):
    fix_tank = await request.json()

    for i, tank in enumerate(tanks):
        if tank["id"] == id:
            fix_tank.pop("id",None)
            tanks[i] = {**tank, **fix_tank}
            return tanks[i]
        raise HTTPException(status_code=404, detail="Tank not found")

@app.delete("/tank/{id}", status_code=status.HTTP_200_OK)
def delete_tank(id:str):
    for i in range(len(tanks)):
        if tanks[i]["id"] == id:
           del tanks[i]
        return {}
    raise HTTPException(status_code=404, detail="Tank not found")

        

