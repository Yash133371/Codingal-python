def ask_question(question: str, correct_answer: str) -> None:
    answer = input(question)
    if answer.lower() == correct_answer:
        print("Correct!")
    else:
        print("Wrong!")


ask_question("What type of data is CSV (relational or nonrelational)? ", "relational")
ask_question("What type of data is JSON (relational or nonrelational)? ", "nonrelational")