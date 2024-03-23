import logging
import time

class Student:
    def __init__(self, name, grade, money):
        self.name = name
        self.grade = grade
        self.money = money
        logging.basicConfig(level=logging.WARNING, filename="logs.log", filemode="w", format="You need to try harder %(asctime)s : %(levelname)s, %(message)s")
        logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w",format="All great %(asctime)s : %(levelname)s, %(message)s")
    def study(self, hours):
        self.grade += hours * 0.1

    def play(self, hours):
        self.grade -= hours * 0.5
        self.money -= hours * 0.5


    def work(self, hours):
        self.money += hours * 0.1
    def get_grade(self):
        return self.grade
        logging.debug("debug")

    def check_myself(self):

        if self.money <= 0:
            qi = input("Some low money you need to work harder Y/N")
            logging.warning("Low money")
            if qi.lower() == "y":
                print("Working...")
                time.sleep(2)
                self.work(game * 24)
            else:
                quit()

        if self.grade <= 0:
            q = input("low grade you need to study harder Y/N:")
            logging.warning("Low grade")
            if q.lower() == "y":
                print("Styding...")
                time.sleep(2)
                self.study(game * 12)
            else:
                quit()


            print(f"Mark: {student.grade} money: {student.money}")

student = Student("Tyler durden", 2, 2)
for i in range(366):
    print(f"day {i}")
    lesson = float(input("Teach student: "))
    student.study(lesson)

    game = float(input("Play with student: "))
    student.play(game)

    work = float(input("Work in hours: "))
    grade = student.get_grade()

    student.check_myself()
    print(f"Mark: {student.grade} money: {student.money}")