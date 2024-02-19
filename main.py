from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends
from typing import List, Union
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import uvicorn

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class User(BaseModel):
    user_name: str
    user_email: str
    age: Union[int, None] = None
    recommendations: List[str]
    ZIP: Union[int, None] = None


@app.post('/')
def create_user(user: User, db: Session = Depends(get_db)):
    existing_user = db.query(models.Users).filter(models.Users.user_email == user.user_email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail=f"Already existing user with {user.user_email} email."
        )

    user_model = models.Users()
    user_model.user_name = user.user_name
    user_model.user_email = user.user_email
    user_model.age = user.age
    user_model.recommendations = ','.join(user.recommendations)
    user_model.ZIP = user.ZIP

    db.add(user_model)
    db.commit()

    return db.query(models.Users).filter(models.Users.user_email == user.user_email).first()


@app.put('/{user_id}')
def update_user(user_id: int, user: User, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.user_id == user_id).first()

    if user_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"User id {user_id}: Does not exist"
        )

    user_model.user_name = user.user_name
    user_model.user_email = user.user_email
    user_model.age = user.age
    user_model.recommendations = ','.join(user.recommendations)
    user_model.ZIP = user.ZIP

    db.add(user_model)
    db.commit()

    return db.query(models.Users).filter(models.Users.user_id == user_id).first()


@app.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Users).all()


@app.get('/{user_id}')
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.user_id == user_id).first()

    if user_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"User id {user_id}: Does not exist"
        )

    return user_model


@app.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.user_id == user_id).first()

    if user_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"User id {user_id}: Does not exist"
        )

    db.query(models.Users).filter(models.Users.user_id == user_id).delete()

    db.commit()


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=True)
