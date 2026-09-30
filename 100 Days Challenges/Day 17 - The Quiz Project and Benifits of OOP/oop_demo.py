# a small runnable tour of classes and OOP, using a bank account as the example.
# run the file and read the output next to the code - each part prints its own header.
# notes.py covers the syntax, this file is about why any of it is worth doing.


def banner(title):
    # a plain helper, not part of the lesson - it just makes the terminal output easy to read
    print('\n' + '=' * 62)
    print(title)
    print('=' * 62)


# ------------------------------------------------------------------------------
# PART 1 - A CLASS AND ITS OBJECTS
# a class is a blueprint. an object is one real thing built from that blueprint.
# the whole class is written here in one go, and the later parts point at the bits
# of it that carry each idea.
# ------------------------------------------------------------------------------

class BankAccount:      # PascalCase for the class, snake_case for everything else
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance      # a default value, so the second argument is optional but settable
        self._transactions = []     # see PART 2 - the underscore means 'the class's own business'
        self._record(f'opened with {balance}')

    def __repr__(self):
        # without this, print(acc_1) gives you <__main__.BankAccount object at 0x000001A...>
        return f'BankAccount(owner={self.owner!r}, balance={self.balance})'

    def _record(self, note):
        self._transactions.append(note)

    def deposit(self, amount):
        if amount <= 0:                                 # the rule lives inside the class
            print(f'  refused: {amount} is not a deposit')
            return False
        self.balance += amount
        self._record(f'deposit {amount}')
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print(f'  refused: {amount} is not a withdrawal')
            return False
        if amount > self.balance:
            print(f'  refused: {self.owner} asked for {amount} but only holds {self.balance}')
            return False
        self.balance -= amount
        self._record(f'withdraw {amount}')
        return True

    def transfer_to(self, other_account, amount):
        # one object taking another object as an argument - the same shape as user_1.follow(user_2)
        if self.withdraw(amount):
            other_account.deposit(amount)
            self._record(f'transfer {amount} to {other_account.owner}')
            return True
        return False

    def history(self):
        return list(self._transactions)     # hand back a copy so outside code can't edit the real log

    def statement(self):
        return f'{self.owner}: {self.balance}'

    def describe(self):
        return f'{self.owner} holds {self.balance} in a plain account'


# ------------------------------------------------------------------------------
# PART 3 - INHERITANCE
# a child class starts out as a full copy of its parent, then changes only what's different
# ------------------------------------------------------------------------------

class SavingsAccount(BankAccount):      # 'a SavingsAccount is a BankAccount'
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)    # let the parent do the setup it already knows how to do
        self.interest_rate = interest_rate  # then add the one thing that's new

    def add_interest(self):
        interest = round(self.balance * self.interest_rate, 2)
        self.deposit(interest)              # deposit was never written here, it came from the parent
        return interest

    def describe(self):
        return f'{self.owner} holds {self.balance} in savings at {self.interest_rate:.0%}'


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # overriding: same method name as the parent, different rules
        if amount <= self.balance:
            return super().withdraw(amount)     # the normal case - reuse the parent's version
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self._record(f'withdraw {amount} (into overdraft)')
            print(f'  allowed: {self.owner} is now overdrawn at {self.balance}')
            return True
        print(f"  refused: {amount} is past {self.owner}'s overdraft limit")
        return False

    def describe(self):
        return f'{self.owner} holds {self.balance} in checking, with {self.overdraft_limit} of overdraft'


if __name__ == '__main__':
    # this line means 'only run the demo when this file is run directly'.
    # if another file ever does `import oop_demo`, it gets the classes and none of the printing.

    banner('PART 1 - a class and its objects')
    acc_1 = BankAccount('faisal', 500)      # BankAccount is the blueprint, acc_1 is one thing built from it
    acc_2 = BankAccount('nada')             # no balance passed, so the default 0 is used
    print(acc_1)
    print(acc_2)

    acc_1.deposit(250)
    acc_1.withdraw(100)
    print(f'{acc_1.statement():<16}<- faisal moved money around')
    print(f'{acc_2.statement():<16}<- nada is untouched by all of it')
    # one class, two objects, two completely separate sets of data

    banner('PART 2 - encapsulation (the object guards its own data)')
    print(f'balance before the bad ideas: {acc_1.balance}')
    acc_1.withdraw(9999)        # more than he has
    acc_1.deposit(-50)          # negative money
    print(f'balance after the bad ideas:  {acc_1.balance}   <- unchanged, the class said no')
    # the checks live inside deposit() and withdraw(), so every caller gets them for free
    # and nobody can forget to write them. the account also keeps its own log:

    print("\nfaisal's history, which only the account itself writes to:")
    for line in acc_1.history():
        print('  -', line)
    # _transactions and _record start with an underscore: a promise between programmers
    # that says 'internal, leave this alone'. python doesn't enforce it, it just trusts you.

    banner('PART 3 - inheritance (write it once, reuse it)')
    savings = SavingsAccount('faisal', 1000, interest_rate=0.05)
    checking = CheckingAccount('nada', 50, overdraft_limit=100)

    earned = savings.add_interest()
    print(f'savings earned {earned} in interest -> {savings.statement()}')
    savings.withdraw(200)       # withdraw was never written in SavingsAccount
    print(f'after withdrawing 200            -> {savings.statement()}')
    # SavingsAccount is about 10 lines long, and those 10 lines also bought it
    # deposit, withdraw, transfer_to, history, statement and __repr__

    print('\nCheckingAccount overrides withdraw, so the same call behaves differently:')
    checking.withdraw(120)      # more than the 50 it holds, but inside the 100 overdraft
    checking.withdraw(500)      # far past the limit

    banner('PART 4 - polymorphism (one method name, different behaviour)')
    for account in [acc_1, savings, checking]:
        print(' ', account.describe())
    # the loop never asks what kind of account it is holding - each object already knows
    # its own version of describe(). without it you would be writing:
    #     if kind == 'savings': ...
    #     elif kind == 'checking': ...
    # and adding one more branch every single time a new account type appears.

    banner('PART 5 - abstraction (a simple outside over a busy inside)')
    print(f'before:  {acc_1.statement()}  |  {acc_2.statement()}')
    acc_1.transfer_to(acc_2, 300)       # one line
    print(f'after:   {acc_1.statement()}  |  {acc_2.statement()}')
    # that one line checked the balance, took money out of one object, put it into another,
    # and wrote three log entries. the caller needs to know the name transfer_to and nothing else.
    # (later you'll meet abc.ABC, which lets a parent class force its children to define
    #  describe() instead of just hoping they do. same idea, enforced - not needed today.)

    banner('PART 6 - why bother? the same job without classes')

    # ---- the old way: a dict holds the data, loose functions do the work ----
    old_account = {'owner': 'faisal', 'balance': 500}

    def old_deposit(account, amount):
        account['balance'] += amount

    old_deposit(old_account, 250)
    print(f'dict version: {old_account}')

    old_account['balance'] = -999999        # nothing stopped that
    old_account['balence'] = 0              # and a typo just quietly adds a new key
    print(f'dict version: {old_account}')
    print('              ^ neither of those two lines should have been possible')
    # what went wrong:
    #   1. any line of code anywhere can set balance to nonsense - no rules are attached to the data
    #   2. nothing ties old_deposit to old_account, they only happen to fit
    #   3. a mistyped key doesn't crash, it silently creates a new one
    #   4. a savings version means more loose functions and more if-branches, not 10 clean lines

    print('\nthe class refuses the exact same abuse:')
    acc_1.withdraw(999999)
    acc_1.deposit(-999999)

    print('\nthat is the benefit of OOP in one sentence:')
    print('data and the rules that protect it travel together, inside one object.')
