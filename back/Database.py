import os
import json


class Database:
    def __init__(self, path: str) -> None:
        self.path = path

        self.__create_file()
        self.__create_accounts_catagory()

    def __get_database_json_data(self) -> dict:
        with open(self.path, "r") as f:
            return json.load(f)

    def __write_new_json_data(self, new_json: dict) -> dict:
        with open(self.path, "w") as f:
            f.write(json.dumps(new_json))

    def __create_file(self) -> None:
        with open(self.path, "w+") as f:
            f.write("{}")

    def __create_accounts_catagory(self) -> None:
        current_json_data = self.__get_database_json_data()
        current_json_data["accounts"] = {}
        self.__write_new_json_data(current_json_data)
