from Question import Question


def build_question(line_array, question_array):


# this version is before add the option to change answers
def analyze_data():
    file = open("data.txt", "r")
    questions_array = {}
    for line in file:
        line_array = line.split(", ")
        question_number = line_array[0]
        question_text = line_array[1]
        # dict - question_number : Question object
        question_answers = {}
        # insert answers to dictionary
        for i in range(2, len(line_array)):
            answer_text = line_array[i]
            answer_next_question = int(line_array[i+1])
            # next question object already exist
            if answer_next_question in questions_array.keys():
                question_answers[answer_text] = questions_array[answer_next_question]
            # next question object doesn't exist
            else:


