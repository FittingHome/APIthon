from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    userId: str
    avatar_id: str
    # garmentsId: [str, None] = None

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/create_obj/")
async def create_obj(item: Item):
    # from script import md_configurator
    # md_configurator.simple_automate(Item.garment_id)
    print(item.userId)
    print(item.avatar_id)
    return item

@app.get("/upload_obj/")
async def upload_obj():
    import uuid
    id = uuid.uudi1()
    return {id.hex}

#json = {"user_id" = 328947,"avatar_id" = 123, "garment_id" = {23, 87}, "simgarment_id" = 98765}