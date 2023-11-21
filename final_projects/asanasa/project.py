from tkinter import *
import tkinter as tk
from tkinter import Canvas, messagebox

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
        "A1": "Спокійний і обдуманий.",
        "B1": "Товариський і дружелюбний.",
        "C1": "Енергійний і веселий.",
        "D1": "Оптимістичний і творчий."
    },
    "2": {
        "A2": "Аналітичний і мислитель.",
        "B2": "Емоційний і комунікабельний.",
        "C2": "Енергійний і активний.",
        "D2": "Оптимістичний і підприємливий."
    },
    "3": {
        "A3": "Духовний розвиток і самопізнання.",
        "B3": "Стосунки з близькими і друзями.",
        "C3": "Фізичне здоров'я та фізична активність.",
        "D3": "Досягнення особистих і професійних цілей."
    },
    "4": {
        "A4": "Осінь, коли можна усамітнитися і міркувати.",
        "B4": "Весна, коли природа прокидається, і можна проводити час з друзями.",
        "C4": "Літо, коли можна займатися спортом та бути на свіжому повітрі.",
        "D4": "Зима, коли можна святкувати та створювати нові плани."
    },
    "5": {
        "A5": "Глибокий синій.",
        "B5": "Яскравий червоний.",
        "C5": "Палаючий помаранчевий.",
        "D5": "Світло-зелений."
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
    # Створюємо фрейм для кнопки "Відповісти"
    button_frame = tk.Frame(main_frame)
    button_frame.pack(side="bottom", pady=100)

    # Створюємо кнопку "Відповісти" у фреймі
    answer_button = tk.Button(
        button_frame,
        text="Відповісти",
        font=("Helvetica", 14),
        command=next_question,
        image=background_image,
        compound="center",
        width=200,
        height=50,
        bd=4,
        highlightthickness=4
    )
    answer_button.pack()
def answer_selected(value):
    selected_answers[current_question] = value

def display_question():
    question_label.config(text=questions[str(current_question + 1)])
    question_label.pack(pady=30)

    for i, (option_key, option_value) in enumerate(answer_options[str(current_question + 1)].items()):
        radio_button = tk.Radiobutton(
            main_frame,
            text=option_value,
            variable=selected_answers[current_question],
            value=option_key,
            font=("Helvetica", 12),
            command=lambda value=option_key: answer_selected(value),
            tristatevalue=current_question*4+1,
            bg="LightSkyBlue"
        )
        radio_buttons.append(radio_button)
        radio_button.pack()

def next_question():
    global current_question
    selected_option = selected_answers[current_question]

    if not selected_option:
        tk.messagebox.showerror("Error", "Оберіть один варіант відповіді.")
        return

    if current_question < len(questions) - 1:
        current_question += 1
        for radio_button in radio_buttons:
            radio_button.destroy()
        display_question()
    else:
        show_result()
        print(selected_answers)

# Створюємо головне вікно
window = Tk()
window.geometry("600x400")
window.title("Тест: Який талісман підходить саме вам?")
window.resizable(width=False, height=False)
img = PhotoImage(file="9391712.png")
window.iconphoto(False, img)

result_images = {
    "A": PhotoImage(file="sphir.png"),
    "B": PhotoImage(file="jemj.png"),
    "C": PhotoImage(file="kristal.png"),
    "D": PhotoImage(file="ametist.png")
}
def show_result():
    global image_path
    option_scores = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }
    for selected_option in selected_answers:
        if selected_option:
            option_key = selected_option[0]
            option_scores[option_key] += 1

    max_score = max(option_scores.values())
    result = ""
    for option, score in option_scores.items():
        if score == max_score:
            result = results[option]
            print(result)
            image_path = result_images[option]
            break

    result_window = tk.Toplevel(window)
    result_window.geometry("600x450")
    result_window.title("Результат тесту")
    result_window.resizable(width=False, height=False)
    result_window.iconphoto(False, img)
    result_label = tk.Label(
        result_window,
        text=result,
        font=("Helvetica", 14),
        wraplength=500,
        image=background_image,
        compound="center",
        width=600,
        height=50
    )
    result_label.pack()

    image_path = image_path.subsample(2, 2)
    image_label = Label(result_window)
    image_label.image = image_path
    image_label['image'] = image_label.image
    image_label.pack()
    image_label.place(x=100, y=60)

    result_window.mainloop()


background_image = PhotoImage(file="fon.png")
canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=background_image)

main_frame = tk.Frame(window)
main_frame.place(relx=0.5, rely=0.5, anchor="center")
background_label = tk.Label(main_frame, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Створюємо мітку для назви тесту
title_label = tk.Label(
    main_frame,
    text="Тест: Який талісман підходить саме вам?",
    font=("Helvetica", 16),
    image=background_image,
    compound="center",
    width=400,
    height=50
)
title_label.pack()

# Створюємо кнопку для початку тесту
start_button = tk.Button(
    main_frame,
    text="Пройти тест",
    command=start_test,
    font=("Helvetica", 14),
    image=background_image,
    compound="center",
    width=200,
    height=50,
    bd=4,
    highlightthickness=4
)
start_button.pack()

# Створюємо мітку для питання
question_label = tk.Label(
    main_frame,
    text="",
    anchor="w",
    font=("Helvetica", 12),
    image=background_image,
    compound="center",
    width=600,
    height=50
)
question_label.pack()

# Запускаємо Tkinter event loop
window.mainloop()
