import unittest
import os
from Database import Database
import json


DATABASE_TEST_PATH = "sampledatabase.json"


class TestDatabaseCreation(unittest.TestCase):
    def test_file_exists(self) -> None:
        db = Database(DATABASE_TEST_PATH)
        db.create_file()

        file_exists = os.path.isfile(DATABASE_TEST_PATH)
        self.assertTrue(file_exists)

    def test_can_append_data(self) -> None:
        db = Database(DATABASE_TEST_PATH)
        db.create_file()

        db.data["t"] = []
        self.assertEqual(db.data, {"t": []})

    def test_write_data(self) -> None:
        db = Database(DATABASE_TEST_PATH)
        db.create_file()

        db.data["t"] = []
        db.write()

        with open(DATABASE_TEST_PATH) as f:
            json_data = json.load(f)
            self.assertEqual(json_data, {"t": []})

    def test_read_data(self) -> None:
        db = Database(DATABASE_TEST_PATH)
        db.create_file()

        with open(DATABASE_TEST_PATH, "w") as f:
            f.write('{"t": []}')

        db.load()
        self.assertEqual(db.data, {"t": []})


# class TestAccountMethods(unittest.TestCase):
#     def test_create_account(self) -> None:
#         db = Database(DATABASE_TEST_PATH)
#         account_manager = AccountManager(db)
#
#         sample_name = "Billy"
#         sample_password = "BillyB0b"
#         acc = Account(sample_name, sample_password)
#
#         account_manager.register(acc)


if __name__ == "__main__":
    unittest.main()
