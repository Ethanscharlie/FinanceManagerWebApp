import os
import json


class Database:
    def __init__(self, path: str) -> None:
        self.__path = path
        self.data = {}

    def write(self) -> None:
        with open(self.__path, "w") as f:
            f.write(json.dumps(self.data))

    def load(self) -> None:
        with open(self.__path, "r") as f:
            self.data = json.load(f)

    def create_file(self) -> None:
        with open(self.__path, "w+") as f:
            f.write("{}")
