class Bank:
  def __init__(self, bank_name, bank_address):
    self.bank_name = bank_name
    self.bank_address = bank_address
    self.member_dictionary = {}

#we are adding new members by creating members with our Member class and putting them in our member dictionary object
  def add_new_member(self, member_first_name, member_last_name, member_account_number):
    temp = Member(member_first_name, member_last_name, member_account_number)
    self.member_dictionary[member_account_number] = {temp}

#getting our
  def find_member_by_account_number(self, member_account_number):
    print(self.member_dictionary[member_account_number])

#still need to do this
  def find_member_by_name(self, member_first_name):
    pass

  def delete_member(self, member_account_number):
    del self.member_dictionary[member_account_number]



#here is our Member class, which creates an account number for each member, stores their first and last names, and stores which accounts each member has
class Member:
  def __init__(self, member_first_name, member_last_name, member_account_number):
    self.member_first_name = member_first_name
    self.member_last_name = member_last_name
    self.member_account_number = member_account_number #later will change this to random
    self.member_accounts = []

  def add_checking_account(self):
    temp = Checking(account_balance)
    self.member_accounts.append(temp)
    print(member_accounts)

  def add_savings_account(self):
    temp = Savings(account_balance)
    self.member_accounts.append(temp)

  def add_money_market_account(self):
    temp = MoneyMarket(account_balance)
    self.member_accounts.append(temp)



class Account:
  def __init__(self, account_balance, member_account_number):
    self.reserve_balance = 100000
    self.account_balance = account_balance

  def withdraw_money(self, amount_to_withdraw):
    self.account_balance = self.account_balance - amount_to_withdraw

  def deposit_money(self, amount_to_deposit):
    self.account_balance = self.account_balance + amount_to_deposit

class MoneyMarket(Account):
  def __init__(self, account_balance):
    self.interest = .05
    self.monthly_fees = 20
    self.account_name = 'Money Market Account'
    self.account_balance = account_balance

class Checking(Account):
  def __init__(self, account_balance):
    self.interest = .01
    self.monthly_fees = 5
    self.account_name = 'Checking Account'
    self.account_balance = account_balance

class Savings(Account):
  def __init__(self, account_balance):
    self.interest = .02
    self.monthly_fees = 10
    self.account_name = 'Savings Account'
    self.account_balance = account_balance


our_bank = Bank('Bank of DigitalCrafts', '123 Happy Coder Road')
our_bank.add_new_member('Sabrina', 'Goldfarb', 1)
our_bank.add_new_member('Michael', 'Goldfarb', 2)
our_bank.add_new_member('Steven', 'Goldfarb', 3)
our_bank.add_new_member('Barbara', 'Goldfarb', 4)

