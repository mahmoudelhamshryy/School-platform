from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    id: int
    name: str
    grade: str

students_db = [Student(id=1, name="John Doe", grade="A"), Student(id=2, name="Jane Smith", grade="B")]

@app.get("/")
async def read_root():
    return students_db

@app.post("/students/")
async def create_student(student: Student):
    students_db.append(student)
    return student

@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    for i, s in enumerate(students_db):
        if s.id == student_id:
            students_db[i] = student
            return student
    return {"error": "Student not found"}

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for i, s in enumerate(students_db):
        if s.id == student_id:
            del students_db[i]
            return {"message": "Student deleted"}
    return {"error": "Student not found"}

