import unittest
import os
from Database import Database


DATABASE_TEST_PATH = "sampledatabase.json"


class TestDatabaseCreation(unittest.TestCase):
    def test_file_exists(self) -> None:
        Database(DATABASE_TEST_PATH)
        file_exists = os.path.isfile(DATABASE_TEST_PATH)
        self.assertTrue(file_exists)

    # def test_user_catagory_exists():
    #     Database(DATABASE_TEST_PATH)
    #     with open(DATABASE_TEST_PATH, 'r') as f:
    #         json_data = json.load(f.read())


# class TestAccountMethods(unittest.TestCase):
# def test_create_account(self) -> None:
#     sample_name = "Billy"
#     sample_password = "BillyB0b"


if __name__ == "__main__":
    unittest.main()
