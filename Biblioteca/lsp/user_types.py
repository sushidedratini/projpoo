
from srp.user import User

class StudentUser(User):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

class TeacherUser(User):
    def __init__(self, user_id, name, teacher_id):
        super().__init__(user_id, name)
        self.teacher_id = teacher_id