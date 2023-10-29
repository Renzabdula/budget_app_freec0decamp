class Category:
  def __init__(self,category):
    self.category = category
    self.ledger = []

  def __str__(self):
    s = self.category.center(30,"*") + "\n"

    for item in self.ledger:
      temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
      s += temp + "\n"

    s += "Total: " + str(self.get_balance())
    return s
    
    
  
  def deposit(self,amount,description = ""):
    self.ledger.append({"amount":amount,"description":description})

  def withdraw(self,amount,description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount":-amount,"description":description})
      return True
    return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def transfer(self,amount,budget_cat):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to " + budget_cat.category)
      budget_cat.deposit(amount,"Transfer from " + self.category)
      return True
    return False

  def check_funds(self,amount):
    return amount <= self.get_balance()
      



def create_spend_chart(categories):
  spend = []
  
  # Calculate the total spending for each category
  for category in categories:
      temp = sum(abs(item['amount']) for item in category.ledger if item['amount'] < 0)
      spend.append(temp)
  
  total = sum(spend)
  percentage = [i / total * 100 for i in spend]
  
  s = "Percentage spent by category"
  
  # Build the spending chart
  for i in range(100, -1, -10):
      s += "\n" + str(i).rjust(3) + "|"
      for j in percentage:
          if j > i:
              s += " o "
          else:
              s += "   "
      s += " "
  
  s += "\n    ----------"
  
  cat_length = [len(category.category) for category in categories]
  max_length = max(cat_length)
  
  # Build the category names at the bottom
  for i in range(max_length):
      s += "\n    "
      for j in range(len(categories)):
          if i < cat_length[j]:
              s += " " + categories[j].category[i] + " "
          else:
              s += "   "
      s += " "
  
  return s