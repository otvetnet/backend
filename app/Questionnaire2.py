import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

def get_screen_size():
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    return screen_width, screen_height

class Questionnaire:
    def __init__(self, master):
        self.master = master
        master.title("Опрос о зависимости от гаджетов")

        screen_width, screen_height = get_screen_size()
        window_width = int(screen_width * 0.75)
        window_height = int(screen_height * 0.30)
        master.geometry(f"{window_width}x{window_height}")


        self.questions = [
            "1. Думаешь ли ты в школе о том, что придешь домой и будешь сидеть в социальных сетях (Тикток, Лайк и другие)?",
            "2. Легко ли тебе отложить телефон по первой просьбе родителей/ прожить день без социальных сетей?",
            "3. Чувствуешь ли ты себя злым, грустным или одиноким, когда не можешь пользоваться телефоном?",
            "4. Бывает ли, что у тебя болит голова, глаза, спина или трудности с засыпанием после времени, проведенного за смартфоном?",
            "5. Отвлекаешься ли ты на телефон во время учебы?",
            "6. Случается ли, что ты играешь в телефон или компьютер дольше, чем планировал?",
            "7. Часто ли из-за игр на телефоне (компьютере, планшете) ты забываешь сделать домашнее задание или выполнить обязанности по дому?",
            "8. Приходилось ли тебе скрывать от родителей, сколько времени ты провел за игрой в телефон, планшет или компьютер?",
            "9. Бывает, что из-за игр в телефоне, планшете или компьютере ты ссоришься с друзьями или родителями?",
            "10. Как ты относишься к людям, которые всё своё время проводят за компьютерными играми?"
        ]

        self.answers = [None] * len(self.questions)  # сохранение ответов
        self.scores = [
            {"А": 3, "Б": 2, "В": 1, "Г": 0},  # Баллы (экранная зависимость)
            {"А": 3, "Б": 2, "В": 1, "Г": 0},  # Баллы (игровая зависимость)
        ]

        self.current_question = 0
        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="", wraplength=550, font=("Arial", 14)) 
        self.question_label.pack(pady=10)

        self.radio_var = tk.StringVar()  # Для хранения выбранного ответа
        self.radio_buttons = []
        options = ["А", "Б", "В", "Г"]
        for i, option in enumerate(options):
            radio_button = tk.Radiobutton(self.master, text=option, variable=self.radio_var, value=option, font=("Arial", 12))
            radio_button.pack(anchor=tk.W, padx=20) 
            self.radio_buttons.append(radio_button)


        self.next_button = tk.Button(self.master, text="Следующий вопрос", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])
            self.radio_var.set(None)  # <--- Очистка значения radio_var
        else:
            self.calculate_results()

    def next_question(self):
        if self.current_question < len(self.questions): # проверка на окончание вопросов
            answer = self.radio_var.get()
            if not answer:
                messagebox.showinfo("Внимание", "Пожалуйста, выберите ответ.")
                return

            self.answers[self.current_question] = answer
            self.current_question += 1
            self.show_question()
        else:
            self.calculate_results()

    def calculate_results(self):
        screen_score = 0
        game_score = 0

        # Расчет баллов для вопросов 2-6 (экранная зависимость)
        for i in range(2, 7):  
            answer = self.answers[i-2]  
            if answer:
                screen_score += self.scores[0][answer]

        # Расчет баллов для вопросов 7-11 
        for i in range(7, 11): 
            answer = self.answers[i-2]
            if answer:
                game_score += self.scores[1][answer]

        # Определение результата
        screen_result = self.get_result_text(screen_score, "экранной")
        game_result = self.get_result_text(game_score, "игровой")

        messagebox.showinfo("Результаты опроса",
                            f"Результаты по экранной зависимости: {screen_score} баллов ({screen_result})\n"
                            f"Результаты по игровой зависимости: {game_score} баллов ({game_result})")

    def get_result_text(self, score, dependency_type):
        """Получает текстовое описание результата в зависимости от набранных баллов."""
        if dependency_type == "экранной":
            if score >= 9:
                return "Высокая зависимость"
            elif score >= 5:
                return "Средняя зависимость"
            else:
                return "Низкая зависимость"
        elif dependency_type == "игровой":
            if score >= 9:
                return "Высокая зависимость"
            elif score >= 5:
                return "Средняя зависимость"
            else:
                return "Низкая зависимость"
        return "Невозможно определить" # на всякий случай

root = tk.Tk()
questionnaire = Questionnaire(root)
root.mainloop()