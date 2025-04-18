class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

class Manager:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("该学号已存在，请重新输入！")
                return
        new_student = Student(name, age, student_id)
        self.students.append(new_student)
        print("学生信息添加成功！")

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("学生信息删除成功！")
                return
        print("未找到该学号的学生信息！")

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(f"学生姓名：{student.name}，年龄：{student.age}，学号：{student.student_id}")
                return
        print("未找到该学号的学生信息！")

    def display_all_students(self):
        if not self.students:
            print("当前没有学生信息！")
        else:
            print("所有学生信息如下：")
            for student in self.students:
                print(f"学生姓名：{student.name}，年龄：{student.age}，学号：{student.student_id}")

def main():
    manager = Manager()
    while True:
        print("\n简易学生管理系统")
        print("1. 添加学生信息")
        print("2. 删除学生信息")
        print("3. 查询学生信息")
        print("4. 显示所有学生信息")
        print("5. 退出系统")
        choice = input("请输入您的选择（1-5）：")

        if choice == "1":
            name = input("请输入学生姓名：")
            age = int(input("请输入学生年龄："))
            student_id = input("请输入学生学号：")
            manager.add_student(name, age, student_id)
        elif choice == "2":
            student_id = input("请输入要删除的学生学号：")
            manager.delete_student(student_id)
        elif choice == "3":
            student_id = input("请输入要查询的学生学号：")
            manager.search_student(student_id)
        elif choice == "4":
            manager.display_all_students()
        elif choice == "5":
            print("感谢使用简易学生管理系统，再见！")
            break
        else:
            print("无效的输入，请重新选择！")

if __name__ == "__main__":
    main()