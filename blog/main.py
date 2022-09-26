from . import models, schemas
from fastapi import FastAPI, Depends, status, Response, HTTPException
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blog", status_code=status.HTTP_200_OK)
def fetch_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    if blogs is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No blogs registered"
        )
    return blogs


@app.get("/blog/{blog_id}", status_code=status.HTTP_200_OK)
def fetch_by_id(blog_id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if blog is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with {blog_id} not found"
        )
    return blog

