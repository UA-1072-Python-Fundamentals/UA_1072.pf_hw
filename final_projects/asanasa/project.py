import tkinter as tk

# Список питань і варіантів відповідей
questions = {
    "1": "Як ви себе почуваєте, коли настає важкий час у вашому житті?",
    "2": "Який опис найкраще вас характеризує?",
    "3": "Яка сфера життя важливіша для вас?",
    "4": "Яку пору року ви віддаєте перевагу?",
    "5": "Який колір найближчий до вас?"
}

answer_options = {
    "1": {
        "A": "Спокійний і обдуманий.",
        "B": "Товариський і дружелюбний.",
        "C": "Енергійний і веселий.",
        "D": "Оптимістичний і творчий."
    },
    "2": {
        "A": "Аналітичний і мислитель.",
        "B": "Емоційний і комунікабельний.",
        "C": "Енергійний і активний.",
        "D": "Оптимістичний і підприємливий."
    },
    "3": {
        "A": "Духовний розвиток і самопізнання.",
        "B": "Стосунки з близькими і друзями.",
        "C": "Фізичне здоров'я та фізична активність.",
        "D": "Досягнення особистих і професійних цілей."
    },
    "4": {
        "A": "Осінь, коли можна усамітнитися і міркувати.",
        "B": "Весна, коли природа прокидається, і можна проводити час з друзями.",
        "C": "Літо, коли можна займатися спортом та бути на свіжому повітрі.",
        "D": "Зима, коли можна святкувати та створювати нові плани."
    },
    "5": {
        "A": "Глибокий синій.",
        "B": "Яскравий червоний.",
        "C": "Палаючий помаранчевий.",
        "D": "Світло-зелений."
    }
}



# Результати тесту
results = {
    "A": "Ваш талісман - Сапфір, символ мудрості та внутрішньої рівноваги.",
    "B": "Ваш талісман - Жемчуг, символ дружелюбності та спілкування з оточуючими.",
    "C": "Ваш талісман - Кристал, символ енергії та фізичної активності.",
    "D": "Ваш талісман - Аметист, символ оптимізму та нових початків."
}

current_question = 0  # Змінна для відстеження поточного питання

selected_answers = [None] * len(questions)

radio_buttons = []

def start_test():
    start_button.pack_forget()  # Приховуємо кнопку старту
    display_question()

def answer_selected(value):
    selected_answers[current_question] = value

def display_question():
    question_label.config(text=questions[str(current_question + 1)])
    for i, (option_key, option_value) in enumerate(answer_options[str(current_question + 1)].items()):
        radio_button = tk.Radiobutton(
            window,
            text=option_value,
            variable=selected_answers[current_question],
            value=option_key,
            font=("Helvetica", 12),
            command=lambda value=option_key: answer_selected(value)
        )
        radio_buttons.append(radio_button)
        radio_button.pack()
    answer_button.pack()


def next_question():
    global current_question
    if current_question < len(questions) - 1:
        current_question += 1
        for radio_button in radio_buttons:
            radio_button.destroy()  # Удаляем радиокнопки
        display_question()
    else:
        show_result()
        print(selected_answers)  # Выводим selected_answers в консоль


def show_result():
    # Оценка ответов
    scores = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    for answer in selected_answers:
        if answer:
            scores[answer] += 1

    # Находим максимальный результат
    max_score = max(scores.values())

    # Определяем результат теста
    result = ""
    for option, score in scores.items():
        if score == max_score:
            result = results[option]
            break

    # Выводим результат в новом окне
    result_window = tk.Toplevel(window)
    result_window.title("Результат тесту")
    result_label = tk.Label(result_window, text=result, font=("Helvetica", 14), wraplength=500)
    result_label.pack()
    result_window.mainloop()

# Створюємо головне вікно
window = tk.Tk()
window.geometry("600x400")
window.title("Тест: Який талісман підходить саме вам?")

# Створюємо мітку для назви тесту
title_label = tk.Label(window, text="Тест: Який талісман підходить саме вам?", font=("Helvetica", 16))
title_label.pack()

# Створюємо кнопку для початку тесту
start_button = tk.Button(window, text="Пройти тест", command=start_test, font=("Helvetica", 14))
start_button.pack()

# Створюємо мітку для питання
question_label = tk.Label(window, text="", anchor="w", font=("Helvetica", 12))
question_label.pack()



# Створюємо кнопку для перевірки відповіді
answer_button = tk.Button(window, text="Відповісти", font=("Helvetica", 14), command=next_question)

# Запускаємо Tkinter event loop
window.mainloop()
