class Person:
    def __init__(self, full_name,age,is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married
       
    def introduce_myself(self):
        print(f'Fullname: {self.full_name}, age: {self.age}, married:{self.is_married}')
        
class Student(Person):
    def __init__(self, full_name, age, is_married,marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks
    
    def arithmetic_mean_mark(self):
        return sum(self.marks.values()) / len(self.marks)

class Teacher(Person):
    base_salary = 35000
    def __init__(self, full_name, age, is_married,experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience
    
    def checking_salary(self):
        if self.experience > 3:
            bonus_year = self.experience - 3
            bonus = (5 / 100) * self.base_salary * bonus_year
            return self.base_salary + bonus
        else:
            return self.base_salary

teacher_Thomas = Teacher('Thomas Anderson',45,True,10)
print(f'Teacher: {teacher_Thomas.full_name},Age: {teacher_Thomas.age},Married: {teacher_Thomas.is_married},Experience: {teacher_Thomas.experience}')
print(teacher_Thomas.checking_salary())

def create_students():
    student_1 = Student('John Johnson',15,False,{'Math':5,'Chemistry':4,'History':3,'PE': 5,'Physic':4})
    student_2 = Student('Jack Daniels Jn',17,False,{'Math':3,'Chemistry':4,'History':5,'PE': 4,'Physic':3})
    student_3 = Student('Tyler Durden',19,False,{'Math':3,'Chemistry':3,'History':5,'PE': 5,'Physic':3})
    
    students_list = [student_1,student_2,student_3]
    
    return students_list

students = create_students()
for student in students:
    print(f'Name: {student.full_name},Age: {student.age}, Married: {student.is_married}, Marks: {student.marks}, Average mark: {student.arithmetic_mean_mark()}')




