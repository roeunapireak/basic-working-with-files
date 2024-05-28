### Task 1. Analyzing a class list
You are given a pupils.txt file containing information about class performance (grades for a quarter in computer science).

In the pupils_small.py file, write a program to calculate the average grade of the class and display a list of the best students. To do this:

1) Create a Pupil class in which the student’s last name, first name, and grade will be stored. Also create a pupils[] list in which objects of type Pupil will be stored.
2) Open the pupils.txt file for reading. Convert each row of data into an object of type Pupil and add students to the list. Use the str.split() method to split the string into parts.
3) Calculate the average grade and find the top students(maximum grade is 5, minimum is 0). Display the class list and calculated data on the console (see screenshot)


### Task 2. Analyzing a large amount of information
Similar to task 1, analyze the pupils_large.txt file. It contains information about diagnostic work written by students living in a large city (surnames may be repeated).
We need to optimize the last program so that data analysis will take less time.

To do this, make reading and processing the necessary information (grades and last names) line-by-line. The program should have only 1 object of type Pupil and the variables Sum, Amount, and Best_pupils[], which stores the already processed data.

# BONUS TASKS
### Task 3. Bonus. Comparing running times
Compare the running times of the Task 1 and Task 2 programs. To do this:

1) Change the file name in Task 1 from pupils.txt to pupils_large.txt. Now the programs will work with the same data set.

2) Calculate the running time of the Task 1 and Task 2 programs. Use the time module to do this. In both programs:
- import the time module
- start the timer before reading the file (start_time = time.time())
- at the end of the program, display the running time of the program (current time time.time() minus starting time).

3) Make a conclusion as to which program runs faster. How did you come to that conclusion?

### Task 4. Bonus. Analyzing your group
Let's automate the process of calculating the average age in a group of students.

1) Create a my_class.txt file and type a group list in it in the following format:
Name Age
Name Age
...

2) In the my_class.py file, write a program to calculate the average age of the students in the group. The program should display the average age and the oldest student.

