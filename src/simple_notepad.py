import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, simpledialog
from tkinter.font import Font


class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("simple notepad app")
        self.root.geometry("800x600")

        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        self.menu_bar = tk.Menu(self.root)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Новый", command=self.new_file)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выйти", command=self.root.quit)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)

        # Settings menu
        self.settings_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.settings_menu.add_command(label="Цвет фона", command=self.change_bg_color)
        self.settings_menu.add_command(label="Цвет текста", command=self.change_text_color)
        self.settings_menu.add_command(label="Шрифт", command=self.change_font)
        self.settings_menu.add_command(label="Размер шрифта", command=self.change_font_size)
        self.menu_bar.add_cascade(label="Настройки", menu=self.settings_menu)

        # Info menu
        self.info_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.info_menu.add_command(label="О программе", command=self.show_info)
        self.menu_bar.add_cascade(label="Инфо", menu=self.info_menu)
        self.root.config(menu=self.menu_bar)

        # Default settings
        self.text_font = Font(family="Arial", size=12)
        self.text_area.config(font=self.text_font)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

    @staticmethod
    def show_info():
        messagebox.showinfo("Информация", "Привет, это приложение содал Шкапа Михаил. И оно простое."
                                          "Больше никакой информации =)")

    def change_bg_color(self):
        color = colorchooser.askcolor(title="Выберите цвет фона")
        if color[1]:
            self.text_area.config(bg=color[1])

    def change_text_color(self):
        color = colorchooser.askcolor(title="Выберите цвет текста")
        if color[1]:
            self.text_area.config(fg=color[1])

    def change_font(self):
        font_family = simpledialog.askstring("Шрифт", "Введи название шрифта (Arial, Courier, Times):")
        if font_family:
            self.text_font.config(family=font_family)
            self.text_area.config(font=self.text_font)

    def change_font_size(self):
        font_size = simpledialog.askinteger("Размер шрифта", "Введите размер шрифта:", minvalue=1, maxvalue=100)
        if font_size:
            self.text_font.config(size=font_size)
            self.text_area.config(font=self.text_font)


if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
