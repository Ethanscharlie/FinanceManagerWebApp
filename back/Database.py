import os


class Database:
    def __init__(self, path: str) -> None:
        self.path = path

        self.__create_file()

    def __create_file(self) -> None:
        with open(self.path, "w+") as f:
            f.write("")
