grades_of_students = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '5a', 'scores': [5,4,4,3,3]}, {'school_class': '10б', 'scores': [4,4,4,3,3]}]

grade_sum_school = 0
for school_class in grades_of_students:
    number_of_students = len(school_class['scores'])
    grade_sum_class = 0
    for score in school_class['scores']:
        grade_sum_class = score + grade_sum_class
    middle_score_class = grade_sum_class / number_of_students
    print('Средняя оценка по классу ' + school_class['school_class'] + ': ' +  str(middle_score_class))
    grade_sum_school = grade_sum_school + grade_sum_class

middle_score_class = grade_sum_school /  len(grades_of_students)
print('Средняя оценка по школе:'  +  str(middle_score_class))