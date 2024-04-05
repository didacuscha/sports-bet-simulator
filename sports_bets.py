class House:
  #bets is a dictionary of matches and their quotes
  def __init__(self, name, money, bets):
    self.name = name
    self.money = money
    self.bets = bets

  def addMatch(self, match, odds, winner=None):
    self.bets[match] = odds + [winner]

  def removeMatch(self, match):
    self.bets.pop(match)
    return self.bets
  
  def updateOdds(self, match, newodds):
    if match in self.bets:
        current_winner = self.bets[match][-1]  # Get the current winner or None if not set
        self.bets[match] = newodds + [current_winner]
    else:
        print("Match not found.")
    return self.bets

  def setWinner(self, match, winner):
      if match in self.bets:
          current_odds = self.bets[match][:-1]  # Get the current odds
          self.bets[match] = current_odds + [winner]  # Update the list with the new winner
      else:
          print("Match not found.")
      return self.bets

  
  def calculateWinOrLoss():
    pass


class Gambler:
  def __init__(self, name, money, broke, house):
    self.name = name
    self.money = money
    self.broke = broke
    self.house = house
  
  def chooseMatch(self, match):
    if match in self.house.bets:
       return match
    else:
       print("Match not found")

  def placeWage():
    pass
  
  def chooseOutcome():
    pass

betplay = House("betplay", "1000000000", {})
betplay.addMatch("Crystal Palace vs Manchester City", [10.96, 5.48, 1.28])
print(betplay.bets)
betplay.removeMatch("Crystal Palace vs Manchester City")
print(betplay.bets)
betplay.addMatch("Crystal Palace vs Manchester City", [10.96, 5.48, 1.28])
betplay.updateOdds("Crystal Palace vs Manchester City", [10.15, 5.40, 1.33])
print(betplay.bets)
betplay.setWinner("Crystal Palace vs Manchester City", "Manchester City")
print(betplay.bets)

diego = Gambler("Diego", 1000000, False, betplay)
diego.chooseMatch("Crystal Palace vs Manchester City")
