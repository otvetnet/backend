from sqlalchemy.orm import Session
from app.schemas.student import StudentCreate
from app.models.student import Student


def create_student(student: StudentCreate, db: Session) -> Student:
    try:
        new_student = Student(
            first_name=student.first_name,
            last_name=student.last_name,
            age=student.age,
            city_id=student.city_id,
            school=student.school
        )

        db.add(new_student)
        db.commit()
        db.refresh(new_student)

        return new_student
    except Exception as e:
        db.rollback()
        raise e
