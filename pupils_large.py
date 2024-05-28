import time

# 1)
class Pupil:
    def __init__(self, Surname, Name, Mark):
        self.Surname = Surname
        self.Name = Name
        self.Mark = Mark

pupils = []
number_pupils = 0
total_mark = 0


start_time = time.time()
# 2) read pupils and append into list
with open("pupil_large.txt", "r") as file:
    for line in file:
        data = line.split(' ')
        pupil = Pupil(Surname=data[0],Name=data[1], Mark=int(data[2]))
        
        
        if pupil.Mark == 5:
            pupils.append(pupil)
        number_pupils += 1

        total_mark += int(pupil.Mark)



for pupil in pupils:
    print(pupil.Surname, pupil.Name, pupil.Mark)
print('\n')

print("Average grade:", (total_mark/number_pupils))

print("Runtime: ", (time.time()-start_time), "seconds")