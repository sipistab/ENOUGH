import os

def compile_and_organize_week(week_number):
    compiled_data = {}

    for day_number in range(1, 6):
        exercise_file_name = f"Week{week_number}_Day{day_number}_exercises.txt"
        if os.path.exists(exercise_file_name):
            with open(exercise_file_name, "r") as exercise_file:
                lines = exercise_file.read().split('\n\n')
                for block in lines:
                    if not block.strip():
                        continue
                    question, *responses = block.strip().split('\n')
                    compiled_data.setdefault(question, []).extend(responses)

    compiled_file_name = f"Week{week_number}_compiled_organized_data.txt"
    with open(compiled_file_name, "w") as compiled_file:
        for question, answers in compiled_data.items():
            compiled_file.write(question + '\n')
            compiled_file.write('\n'.join(answers).replace('Response:', '') + '\n\n')

    print(f"Organized exercises for Week {week_number} created in '{compiled_file_name}'.")

def present_and_collect_answers(week_number, file_path):
    with open(file_path, 'r') as file:
        lines = file.read().split('\n\n')

    questions = []
    current_question = None
    answers = []

    for line in lines:
        if line.startswith("Question:"):
            if current_question is not None:
                questions.append((current_question, answers))
                answers = []
            current_question = line.strip()
        else:
            answers.append(line.strip())

    new_answers = {}
    for question, answer_options in questions:
        print(question)
        for i, answer in enumerate(answer_options):
            print(f"{i + 1}. {answer}")

        print("If any of what I have been writing this week is true...")
        user_answers = []
        for i in range(5):
            user_answer = input(f"{i + 1}. ")
            user_answers.append(user_answer)

        new_answers[question] = user_answers

    new_file_name = f"Week{week_number}_assessment.txt"
    with open(new_file_name, "w") as new_file:
        for question, user_answers in new_answers.items():
            new_file.write(question + "\n")
            new_file.write("\n".join(user_answers) + "\n\n")

    print(f"User answers saved in '{new_file_name}'.")

def read_questions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    questions = {}
    current_week = None

    for line in lines:
        line = line.strip()
        if line.startswith("Week"):
            current_week = line
            questions[int(current_week.split()[1])] = []
        elif line.startswith("ID"):
            questions[int(current_week.split()[1])].append(line[4:])  # Exclude the "IDxx " part

    return questions

def main():
    while True:
        choice = input("[1] Daily Log [2] Weekly Assessment [Q] Quit: ")
        
        if choice == '1':
            file_path = "SentenceCompletion.txt"
            questions = read_questions(file_path)

            try:
                week_number = int(input("Enter the week number (1-30): "))
                if 1 <= week_number <= 30:
                    if week_number in questions:
                        day_number = int(input("Enter the day number (1-5): "))
                        if 1 <= day_number <= 5:
                            responses = []
                            for question in questions[week_number]:
                                print(f"Question: {question}")
                                print("5 endings.")
                                response = ""
                                for _ in range(5):
                                    line = input()
                                    if line.strip() == "":
                                        break
                                    response += line + "\n"
                                responses.append(response.strip())
                            save_file_name = f"Week{week_number}_Day{day_number}_exercises.txt"
                            with open(save_file_name, "w") as save_file:
                                for question, response in zip(questions[week_number], responses):
                                    save_file.write(f"Question: {question}\n")
                                    save_file.write(f"Response:\n{response}\n\n")
                            print("Responses saved successfully.")
                        else:
                            print("Invalid day number. Please enter a number between 1 and 5.")
                    else:
                        print(f"No questions found for Week {week_number}.")
                else:
                    print("Invalid week number. Please enter a number between 1 and 30.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '2':
            week_number = input("Enter the week number (1-30): ")
            if 1 <= int(week_number) <= 30:
                compile_and_organize_week(int(week_number))
                file_path = f"Week{week_number}_compiled_organized_data.txt"
                present_and_collect_answers(week_number, file_path)
            else:
                print("Invalid week number. Please enter a number between 1 and 30.")
        
        elif choice.upper() == 'Q':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or Q to quit.")

if __name__ == "__main__":
    main()