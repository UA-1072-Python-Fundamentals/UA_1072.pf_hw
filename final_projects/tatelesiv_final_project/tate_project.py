from PIL import Image, ImageTk
import tkinter as tk


def translate_text(input_text, translation_map):
    translated_text = ""
    for char in input_text:
        if char in translation_map:
            translated_text += translation_map[char]
        else:
            translated_text += char
    return translated_text


def translate_text_button_clicked():
    input_text = input_text_entry.get()
    input_text = input_text.lower()
    translation_direction = translation_direction_var.get()
    if translation_direction == "Eng to Ukr":
        translated_text = translate_text(input_text, translation_map_eng_to_ukr)
    elif translation_direction == "Ukr to Eng":
        translated_text = translate_text(input_text, translation_map_ukr_to_eng)

    # Очищаємо попередній текст
    translated_text_display.delete(1.0, tk.END)
    # Вставляємо новий текст
    translated_text_display.insert(tk.END, translated_text)


# Функція для копіювання тексту
def copy_text(event=None):
    root.clipboard_clear()
    text_to_copy = translated_text_display.get(1.0, tk.END)
    root.clipboard_append(text_to_copy)
    root.update()


# Функція для вставки тексту
def paste_text(event=None):
    text_to_paste = root.clipboard_get()
    input_text_entry.insert(tk.INSERT, text_to_paste)


# Створюємо головне вікно
root = tk.Tk()
root.title("Text Translator")
root.geometry("600x250")
root.configure(bg="lightblue")

# Створюємо мітку для введеного тексту
input_text_label = tk.Label(root, text="Enter the text you want to translate:", bg="lightblue")
input_text_label.grid(row=0, column=0, columnspan=2, pady=5)

# Створюємо поле для введення тексту
input_text_entry = tk.Entry(root)
input_text_entry.grid(row=1, column=0, columnspan=2, pady=5)

# Створюємо радіокнопки для вибору напрямку перекладу
translation_direction_var = tk.StringVar()
translation_direction_var.set("Eng to Ukr")  # За замовчуванням англійська на українську
translation_direction_label = tk.Label(root, text="Choose translation direction:", bg="lightblue")
translation_direction_label.grid(row=2, column=0, columnspan=2, pady=5)
eng_to_ukr_radio = tk.Radiobutton(root, text="Eng to Ukr", variable=translation_direction_var,
                                  value="Eng to Ukr", bg="lightblue")
ukr_to_eng_radio = tk.Radiobutton(root, text="Ukr to Eng", variable=translation_direction_var,
                                  value="Ukr to Eng", bg="lightblue")
eng_to_ukr_radio.grid(row=3, column=0, pady=5)
ukr_to_eng_radio.grid(row=3, column=1, pady=5)

# Створюємо кнопку для перекладу
translate_button = tk.Button(root, text="Translate", command=translate_text_button_clicked, bg="lightblue")
translate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Створюємо мітку для відображення перекладеного тексту
translated_text_label = tk.Label(root, text="Translated text:", bg="lightblue")
translated_text_label.grid(row=5, column=0, columnspan=2, pady=5)

# Створюємо Text для відображення перекладеного тексту
translated_text_display = tk.Text(root, wrap="word", height=4, width=50)
translated_text_display.grid(row=6, column=0, columnspan=2, pady=5)

# Завантаження зображення
original_image = Image.open("plant.png")
# Зміна розміру зображення
resized_image = original_image.resize((100, 100))
# Конвертація до формату PhotoImage
tk_image = ImageTk.PhotoImage(resized_image)

# Створення мітки для відображення зображення
image_label = tk.Label(root, image=tk_image, bg="lightblue")
image_label.grid(row=0, column=2, rowspan=6, padx=10)

# Словник для перекладу з англійської на українську
translation_map_eng_to_ukr = {
    'q': 'й',
    'w': 'ц',
    'e': 'у',
    'r': 'к',
    't': 'е',
    'y': 'н',
    'u': 'г',
    'i': 'ш',
    'o': 'щ',
    'p': 'з',
    'a': 'ф',
    's': 'і',
    'd': 'в',
    'f': 'а',
    'g': 'п',
    'h': 'р',
    'j': 'о',
    'k': 'л',
    'l': 'д',
    'z': 'я',
    'x': 'ч',
    'c': 'с',
    'v': 'м',
    'b': 'и',
    'n': 'т',
    'm': 'ь',
    '?': ',',
    '.': 'ю',
    '/': '.',
    ';': 'ж',
    '\'': 'є',
    '[': 'х',
    ']': 'ї',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '0': '0',
    '-': '-',
    '=': '=',
    '\\': '\\',
    '|': '/',
    ',': ',',
}

# Словник для перекладу з української на англійську
translation_map_ukr_to_eng = {
    'й': 'q',
    'ц': 'w',
    'у': 'e',
    'к': 'r',
    'е': 't',
    'н': 'y',
    'г': 'u',
    'ш': 'i',
    'щ': 'o',
    'з': 'p',
    'ф': 'a',
    'і': 's',
    'в': 'd',
    'а': 'f',
    'п': 'g',
    'р': 'h',
    'о': 'j',
    'л': 'k',
    'д': 'l',
    'я': 'z',
    'ч': 'x',
    'с': 'c',
    'м': 'v',
    'и': 'b',
    'т': 'n',
    'ь': 'm',
    ',': '?',
    'ю': '.',
    '.': '/',
    'ж': ';',
    'ї': '\'',
    'х': '[',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '0': '0',
    '-': '-',
    '=': '=',
    '\\': '\\',
    '/': '|',
    'б': ',',
}

# Додаємо можливість копіювання тексту
translated_text_display.bind("<Control-c>", copy_text)

# Додаємо можливість вставки тексту
input_text_entry.bind("<Control-v>", paste_text)

root.mainloop()