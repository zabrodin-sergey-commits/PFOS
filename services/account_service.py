from database.accounts import (
    add_account,
    get_accounts,
    update_balance,
    find_account,
)

class AccountService:

    def create(self, **kwargs):
        return add_account(**kwargs)

    def all(self):
        return get_accounts()

    def find(self, **kwargs):
        return find_account(**kwargs)

    def update_balance(self, **kwargs):
        return update_balance(**kwargs)