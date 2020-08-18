import os

from tkinter import *
from tkinter.filedialog import askopenfilename
from .exc.FileNotSelected import FileNotSelected
from .exc.WrongFileType import WrongFileType
from models.processing.Process import Process


class Gui:
    def __init__(self):
        self.init_window()
        self.init_labels()
        self.init_input()
        self.init_processing_button()
        self.master.mainloop()

    def init_window(self):
        self.master = Tk()
        self.master.title("Descrição de Ambientes")
        self.master.geometry("800x600")
        self.master.resizable(0, 0)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        self.top_frame = Frame(self.master, height=100)
        self.center_frame = Frame(self.master, height=100, padx=15)
        self.bottom_frame = Frame(self.master, height=100, pady=150)
        self.top_frame.grid(row=0, sticky="ew")
        self.center_frame.grid(row=1, sticky="nsew")
        self.bottom_frame.grid(row=2, sticky="nsew")

    def init_labels(self):
        self.label_title = Label(
            self.top_frame,
            text="Descrição espacial de objetos em ambientes internos",
            pady=50,
        )
        self.label_title.config(font=("Courier", 14))
        self.label_title.pack(side=TOP)

    def init_input(self):
        self.text_filepath = Text(
            self.center_frame, height=1.4, width=80, bd=3, relief="groove", pady=2.4
        )

        self.text_filepath.grid(row=0, column=0)

        self.btn_ask_open_file = Button(
            self.center_frame, text="Escolha um arquivo", command=self.ask_file,
        )
        self.btn_ask_open_file.grid(row=0, column=2, padx=5, pady=2.5)

    def init_processing_button(self):
        self.btn_process_image = Button(
            self.bottom_frame,
            text="Processar",
            command=lambda: self.process(self.text_filepath.get("1.0", "end-1c")),
            bd=3,
            relief="solid",
            padx=50,
            pady=50,
        )
        self.btn_process_image.config(font=("Courier", 14))
        self.btn_process_image.pack(side=TOP)

    def ask_file(self):
        try:
            self.filename = askopenfilename(
                initialdir=os.path.join("~", "Images"),
                title="Selecione um Arquivo",
                filetypes=(("Arquivos jpeg", "*.jpg"), ("Arquivos png", "*.png")),
            )
            if not self.filename:
                raise FileNotFoundError

            if not self.filename.endswith((".jpg", ".png")):
                raise ValueError

        except FileNotFoundError:
            FileNotSelected()

        except ValueError:
            WrongFileType()

        else:
            self.text_filepath.insert(INSERT, self.filename)

    @staticmethod
    def process(text):
        try:
            if not text:
                raise FileNotFoundError

            if not text.endswith((".jpg", ".png")):
                raise ValueError

        except FileNotFoundError:
            FileNotSelected()

        except ValueError:
            WrongFileType()

        else:
            Process().run(text)
