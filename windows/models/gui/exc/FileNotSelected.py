from tkinter.messagebox import showwarning


class FileNotSelected:
    def __init__(self) -> None:
        showwarning(title="Aviso", message="Arquivo não selecionado")
