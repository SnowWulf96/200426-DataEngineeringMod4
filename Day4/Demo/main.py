from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()


#Data Model
class Book(BaseModel):
    id: int
    title: str
    author: str


    # Fake DB
books: List[Book] = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald"),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee"),
    Book(id=3, title="1984", author="George Orwell"),
    Book(id=4, title="Pride and Prejudice", author="Jane Austen"),
    Book(id=5, title="The Catcher in the Rye", author="J.D. Salinger")
    ]

    # Root Endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}
    
    # Get all books
@app.get("/books", response_model=List[Book])
def read_books():
    return books

## uvicorn main:app --reload to run the server


##write an endpoint that takes a book id and returns the specific book
@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
##write an endpoint that takes a book id and deletes the specific book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")

##write an endpoint that takes a book id and updates the specific book
@app.put("/books/{book_id}", response_model=Book)   
def update_book(book_id: int, updated_book: Book):
    for book in books:
        if book.id == book_id:
            book.title = updated_book.title
            book.author = updated_book.author
            return book
    raise HTTPException(status_code=404, detail="Book not found")

##write an endpoint that takes a book id and creates a new book
@app.post("/books", response_model=Book) 
def create_book(new_book: Book):
    books.append(new_book)
    return new_book


## How to authenticate users with FastAPI