from collections import defaultdict
from quests import cards
from random import choice

class CardQuiz:
    def __init__(self):
        self.card_display_count = defaultdict(int)
        self.incorrect_answers = defaultdict(int)
        self.correct_count = 0
        self.total_questions = len(cards)
    
    def display_question(self, question):
        print("\n" + "-" * 40)
        print(question)
        print("-" * 40)
    
    def get_user_input(self, correct_answer):
        user_input = input("Answer: ")
        o = input(correct_answer)
        return user_input, o
    
    def choose_question(self):
        card = choice(list(cards.items()))
        question, answer = card
        self.card_display_count[question] += 1
        return question, answer
    
    def update_performance(self, question, user_answer, is_correct):
        if not is_correct:
            self.incorrect_answers[question] += 1
        else:
            self.correct_count += 1

    def run(self):
        try:
            while True:
                question, answer = self.choose_question()
                self.display_question(question)
                user_answer, o = self.get_user_input(f"The answer was: {answer}\nWere you correct? (Y/n/exit): ")
                if o and o[0].lower() == "e":
                    break
                is_correct = o and o[0].lower() == "y"
                self.update_performance(question, user_answer, is_correct)
                
                remaining_cards = self.total_questions - self.correct_count
                if remaining_cards == 0:
                    print(f"You have memorized all {self.total_questions} cards")
                    accuracy = self.correct_count / self.total_questions if self.total_questions > 0 else 0
                    print(f"Performance Metrics:\nCorrect Answers: {self.correct_count}/{self.total_questions}\nAccuracy: {accuracy:.2%}")

                    print("\nTop 5 wrongly answered cards:")
                    sorted_incorrect = sorted(self.incorrect_answers.items(), key=lambda x: x[1], reverse=True)[:5]
                    for card, incorrect_count in sorted_incorrect:
                        display_count = self.card_display_count[card]
                        percentage_incorrect = (incorrect_count / display_count) * 100 if display_count > 0 else 0
                        print(f"Question: {card}\nIncorrect Answers: {incorrect_count}/{display_count} ({percentage_incorrect:.2f}%)\n")

                    k = input("Exit? (N/y): ")
                    if k and k[0].lower() == "y":
                        break
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")

if __name__ == "__main__":
    quiz = CardQuiz()
    quiz.run()
