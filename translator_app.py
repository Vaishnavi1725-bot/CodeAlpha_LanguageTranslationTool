from tkinter import *
from tkinter import messagebox
from deep_translator import GoogleTranslator

# Translate function
def translate_text():
    try:
        input_text = text_input.get("1.0", END).strip()
        src = src_lang.get()
        tgt = tgt_lang.get()

        if not input_text:
            messagebox.showwarning("Empty Input", "Please enter some text to translate.")
            return

        translated = GoogleTranslator(source=src, target=tgt).translate(text=input_text)
        translated_output.delete("1.0", END)
        translated_output.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# UI setup
root = Tk()
root.title("Language Translator - CodeAlpha")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

Label(root, text="Language Translator", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

# Input Text
Label(root, text="Enter Text:", font=("Arial", 12), bg="#f0f0f0").pack()
text_input = Text(root, height=5, width=60)
text_input.pack(pady=5)

# Language options (ISO 639-1 codes)
languages = ["auto", "en", "hi", "te", "fr", "es", "de", "ta", "zh", "ja", "ru"]
src_lang = StringVar(value="auto")
tgt_lang = StringVar(value="hi")

frame = Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

Label(frame, text="From:", font=("Arial", 10), bg="#f0f0f0").grid(row=0, column=0)
OptionMenu(frame, src_lang, *languages).grid(row=0, column=1)

Label(frame, text="To:", font=("Arial", 10), bg="#f0f0f0").grid(row=0, column=2)
OptionMenu(frame, tgt_lang, *languages).grid(row=0, column=3)

# Translate Button
Button(root, text="Translate", command=translate_text, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=5)

# Output Text
Label(root, text="Translated Text:", font=("Arial", 12), bg="#f0f0f0").pack()
translated_output = Text(root, height=5, width=60)
translated_output.pack(pady=5)

root.mainloop()
