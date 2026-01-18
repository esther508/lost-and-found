from fastapi import FastAPI,  Depends
from typing import Optional
from typing import Annotated
from pydantic import BaseModel
from fastapi import HTTPException
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class CreateItem(BaseModel):
    item_name: str
    description: str
    location: str
    date: str
    contact_information: str
    status: str


class UpdateItem(BaseModel):
    item_name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    date: Optional[str] = None
    contact_information: Optional[str] = None
    status: Optional[str] = None

# create a db for our sessionlocal.....and we close the connection so that we dont have to keep it opn for too long


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/get-all-item", status_code=200)
def get_all_item(db: db_dependency):
    item = db.query(models.Item).all()
    return item


@app.get("/get-item/{item_id}", status_code=200)
def get_item(item_id:  int, db: db_dependency):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail='Item does not exist')
    return db_item


@app.get("/get-lost-item", status_code=200)
def get_lost_item(db: db_dependency):
    lost_item = db.query(models.Item).filter(
        models.Item.status == "lost").all()
    return lost_item


@app.get("/get-found-item/", status_code=200)
def get_found_item(db: db_dependency):
    found_item = db.query(models.Item).filter(
        models.Item.status == "found").all()
    return found_item


# status_code=status.HTTP_201_CREATED

@app.post("/create-item", status_code=201)
def create_item(item: CreateItem, db: db_dependency):
    # ** unpack a dictionary into kry arguments
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem, db: db_dependency):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail='Item does not exist')

    if item.item_name is not None:
        db_item.item_name = item.item_name

    if item.description is not None:
        db_item.description = item.description

    if item.location is not None:
        db_item.location = item.location

    if item.date is not None:
        db_item.date = item.date

    if item.contact_information is not None:
        db_item.contact_information = item.contact_information

    if item.status is not None:
        db_item.status = item.status

    db.commit()
    db.refresh(db_item)

    return db_item


@app.delete("/delete-item/{item_id}", status_code=200)
def delete_item(item_id: int, db: db_dependency):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item doesn't exists")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted Successfully"}
