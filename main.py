from quests import cards
from random import randint

class CardQuiz:
    def __init__(self):
        self.slots = (list(cards.items()), [], [])
        self.box_chance_mul = [4, 2, 1]
        self.correct_count = 0
        self.total_questions = len(cards)
    
    def display_question(self, question, answer):
        print(chr(27) + "[2J")
        print("+" + "-" * 38 + "+")
        print(f"|{'Question':^20}|{'Answer':^15}|")
        print("+" + "-" * 38 + "+")
        print(f"|{question:^38}|{answer:^15}|")
        print("+" + "-" * 38 + "+")
    
    def get_user_input(self, correct_answer):
        user_input = input("Answer: ")
        o = input(correct_answer)
        return user_input, o
    
    def choose_question(self):
        wts = [len(i) * self.box_chance_mul[idx] for idx, i in enumerate(self.slots)]
        f = randint(1, sum(wts)) - 1
        box_idx = 0
        a = 0
        n = 0
        for idx, i in enumerate(wts):
            a += i
            if f < a:
                box_idx = idx
                n = f - a + i
                break
        box = self.slots[box_idx]
        q, a = box.pop(n // self.box_chance_mul[box_idx])
        return q, a, box_idx
    
    def update_performance(self, user_answer, is_correct, box_idx):
        if not is_correct or user_answer.lower() == "n":
            box_idx = max(box_idx - 1, 0)
        else:
            self.correct_count += 1
            box_idx = min(box_idx + 1, len(self.slots) - 1)
        self.slots[box_idx].append((q, a))
        return box_idx

    def run(self):
        try:
            while True:
                q, a, box_idx = self.choose_question()
                self.display_question(q, a)
                user_answer, o = self.get_user_input(f"The answer was: {a}\nWere you correct? (Y/n/exit): ")
                if o and o[0].lower() == "e":
                    break
                box_idx = self.update_performance(user_answer, o and o[0].lower() == "y", box_idx)
                if len(cards) == len(self.slots[-1]):
                    print(f"You have memorised all {self.total_questions} cards")
                    accuracy = self.correct_count / self.total_questions if self.total_questions > 0 else 0
                    print(f"Performance Metrics:\nCorrect Answers: {self.correct_count}/{self.total_questions}\nAccuracy: {accuracy:.2%}")
                    k = input("Exit? (N/y): ")
                    if k and k[0].lower() == "y":
                        break
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")

if __name__ == "__main__":
    quiz = CardQuiz()
    quiz.run()
