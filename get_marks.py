import csv 
import random
import os

from constants import STUDENT


subjects = [ "maths", "science", "social", "english", "nepali",] 
base_dir  = os.getcwd()

with open("stdinfo/student.csv", "w") as outfile:
    writer = csv.writer(outfile, delimiter=',')
    for i,student in enumerate(STUDENT):
        writer.writerow([student, f'073/BEL/{300+i}'])

for subject in subjects:
    file = subject + ".csv"
    filepath = os.path.join(base_dir, "marks", file)

    with open(filepath, "w") as outfile:
        writer = csv.writer(outfile, delimiter=',')

        for student in STUDENT:
            marks = random.randint(0,100)
            writer.writerow([student, marks])


