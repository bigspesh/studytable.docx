from classautomation import get_validated_time
from docx import Document

document = Document()


def study_count():
    while True:
        try:
            class_count = int(input('Enter number of study period in a day (4 only) : '))
            if class_count == 4:
                table = document.add_table(5, 4, 'Table Grid')
                return table, class_count
            else:
                print('study period should only be 4')
        except ValueError:
            print('enter 3 or 4')


table, class_count = study_count()

class_times = [
    'Enter the time interval for the first study period eg 00:00AM/PM - 00:00AM/PM:',
    'Enter the time interval for the second study period eg 00:00AM/PM - 00:00AM/PM:',
    'Enter the time interval for the third study period eg 00:00AM/PM - 00:00AM/PM:',
    'Enter the time interval for the fourth study period eg 00:00AM/PM - 00:00AM/PM:',
]

# to store the time intervals that have been used
used_intervals = set()

# to iterate through the 6 cells in the first row
for col in range(len(class_times)):
    if col < class_count:
        table.cell(0, col).text = get_validated_time(class_times[col], used_intervals)


# To make the code shorter, you can use loops and a dictionary to manage the courses. Here's a concise version:

def course_count_prompt():
    while True:
        try:
            print('The top 3 courses should be your most important courses')
            course_count = int(input("Enter the number of courses (5-12): "))
            if 5 <= course_count <= 12:
                return course_count
            else:
                print('course count should be between 5 and 12')
        except ValueError:
            print('enter 5 or 12')


course_count = course_count_prompt()

courses = {f'course{i}': input(f'Course{i}:') for i in range(1, course_count + 1)}

for i in range(1, 5):
    table.cell(i, 0).text = courses['course1']
    table.cell(i, 1).text = courses.get(f'course{8 - i}', courses['course2'])
    table.cell(i, 2).text = courses.get(f'course{5 - i}', courses['course3'])
    table.cell(i, 3).text = courses.get(f'course{4 + i}', courses[f'course{4 if i < 4 else course_count}'])

document.save("study_table.docx")
