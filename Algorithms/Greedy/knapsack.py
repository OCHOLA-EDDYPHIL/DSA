class Question:
    def __init__(self, id, marks):
        self.id = id
        self.marks = marks


def select_questions(questions, questions_to_answer=10):
    # Sort questions based on marks in descending order
    sorted_questions = sorted(questions, key=lambda q: q.marks, reverse=True)

    # Select the top 'questions_to_answer' questions
    selected_questions = sorted_questions[:questions_to_answer]

    # Return the IDs of the selected questions
    return [q.id for q in selected_questions]


# Example usage
questions = [
    Question(1, 10), Question(2, 8), Question(3, 5), Question(4, 10),
    Question(5, 3), Question(6, 7), Question(7, 9), Question(8, 6),
    Question(9, 4), Question(10, 2), Question(11, 1), Question(12, 10)
]
selected_questions = select_questions(questions)
print(f"Selected questions to answer: {selected_questions}")
