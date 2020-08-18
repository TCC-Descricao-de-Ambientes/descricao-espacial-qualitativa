from tkinter.messagebox import showerror


class WrongFileType:
    def __init__(self) -> None:
        showerror(title="Erro", message="Tipo de arquivo inválido. Deve ser .png ou .jpg")
