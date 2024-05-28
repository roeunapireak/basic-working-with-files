#write your code here
import time


# 1)
class Pupil:
    def __init__(self, Surname, Name, Mark):
        self.Surname = Surname
        self.Name = Name
        self.Mark = Mark

pupils = []


# 3) print pupils from list
def print_class(pupils):
    for pupil in pupils:
        print(pupil.Surname, pupil.Name, "-", pupil.Mark)
    print('\n')

# 4) calculate average of marks
def find_average(pupils):
    total_marks = 0
    for pupil in pupils:
        total_marks += pupil.Mark
    average = total_marks/len(pupils)
    print("Average grade for the class:", average)

# 5) print top student 
def print_top_student(pupils):
    for pupil in pupils:
        if pupil.Mark == 5:
            print(pupil.Surname, pupil.Name, pupil.Mark)
    print('\n')


start_time = time.time()
# 2) read pupils and append into list
with open("pupils_txt.txt", "r") as file:
    for line in file:
        data = line.split(' ')
        pupil = Pupil(Surname=data[0],Name=data[1], Mark=int(data[2]))
        pupils.append(pupil)


# calling functions
print_class(pupils)
print_top_student(pupils)
find_average(pupils)

print("Runtime: ", (time.time()-start_time), "seconds")