class Owner:
    
    def __init__(self, name, monthly_income, spending_habit):
        self.name = name
        self.monthly_income = monthly_income
        self.spending_habit = spending_habit
        self.monthly_income_incr_rate = 0.01
    
    def get_monthly_income(self):
        print('monthly income; "  self.monthly_income)
    
    def get_monthly_spending(self):
        print(self.monthly_income * self.spending_habit)
    
    def update_monthly_income(self, rate):
        self.monthly_income = self.monthly_income (1+ self.monthly_income_incr_rate)
        
    def halve_spending(self):
        self.spending_habit = spending_habit /2
        
    def __str__(self):
        pass
    
    

class Wallet:
    
    def __init__(self, initial_amount, owner):
        self.initial_amount = initial_amount
        self.owner = owner      
        
    def deposit(self, amount):
        pass
        
    def withdraw(self, amount):
        pass
    
    def check(self):
        pass
    
    def get_owner(self):
        pass


import random, urllib.request, time, copy

class WalletGame:
      
    def __init__(self, num_players, income_mean, income_sigma, spend_mean, spend_sigma, epoch):
        pass
            
    def play(self):
        pass



if __name__ == '__main__':
    wg = WalletGame(200, 5000, 500, 0.7, 0.5, 120)
    wg.play()
