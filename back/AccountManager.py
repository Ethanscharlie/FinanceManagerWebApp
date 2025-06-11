import Account
import Database


class AccountManager:
    def __init__(self, database: Database) -> None:
        self.__database = database
        self.__accounts = list[Account]

    def register(self, account: Account) -> None:
        self.__accounts.append(account)
