class Person:
    def __init__(self, name, age, job,**kwargs):
        self.name = name
        self.age = age
        self.job = job
        print("Person init")

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"


class Student(Person):
    def __init__(self, name, age, job, grade, **kwargs):
        super().__init__(name, age, job, **kwargs)
        self.grade = grade
        

    def get_details(self):
        return f"{super().get_details()}, Grade: {self.grade}"

class Professor(Person):
    def __init__(self, name, age, job, courses, **kwargs):
        super().__init__(name, age, job, **kwargs)
        self.courses = courses
        print("Professor init")
    def get_details(self):
        return f"{super().get_details()}, Courses: {self.courses}"


class Employee(Person):
    def __init__(self, name, age, job, department, **kwargs):
        super().__init__(name, age, job, **kwargs)
        self.department = department

    def get_details(self):
        return f"{super().get_details()}, Department: {self.department}"

class StudentProfessor(Student, Professor):
    def __init__(self, name, age, job, courses, grade, **kwargs):
        super(StudentProfessor, self).__init__(name=name, age=age, job=job, courses=courses, grade=grade, **kwargs)

    def get_details(self):
        return f"{super().get_details()}"

class Location:
    __slots__ = ['name', 'longitude', 'latitude']

    def __init__(self, name, longitude, latitude):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude

    def get_coordinates(self):
        return (self.longitude, self.latitude)


if __name__ == "__main__":
    student_professor = StudentProfessor("Dr. Brown", 50, "Professor", ["Computer Science"], "B")
    print(student_professor.get_details())
