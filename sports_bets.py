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
  def __init__(self, name, money, broke, house, bets, record):
    self.name = name
    self.money = money
    self.broke = broke
    self.house = house
    self.bets = bets
    self.record = record
  
  def chooseMatchTeamMoney(self, match, result, respos, money):
    gambling = []    
    if match in self.house.bets:
       gambling.append(match)
       gambling.append(result)
       gambling.append(respos)
       gambling.append(money)
       self.bets = gambling
       return self.bets
    else:
       print("Match not found")

  def checkResults(self, match):
    # if "team chosen" = "winner team in list"
    if self.bets[1] == self.house.bets[match][3]:
      # bug always calculating the visitant quote for the winner
      won = (self.house.bets[match][self.bets[2]] * self.bets[3]) - self.bets[3]
      self.money += won
      self.bets = []
      print("You won: " + str(won))
    else:
      self.money -= self.bets[3]
      self.bets = []
      print("You lost: " + str(self.bets[3]))

     
     
  
  

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

diego = Gambler("Diego", 1000, False, betplay, [], [])
# diego.chooseMatch("Crystal Palace vs Manchester City")
print("Important test ")
diego.chooseMatchTeamMoney("Crystal Palace vs Manchester City", "Manchester City", 2, 100)
#diego.chooseMatchTeamMoney("Manchester United vs Liverpool", 2, 100)
print(diego.bets)
print("Check results function on gambler")
diego.checkResults("Crystal Palace vs Manchester City")

print("----------second match--------")
# tests adding a second match
betplay.addMatch("Brighton vs Arsenal", [5.94, 4.45, 1.48])
betplay.setWinner("Brighton vs Arsenal", "Arsenal")
diego.chooseMatchTeamMoney("Brighton vs Arsenal", "Arsenal", 2, 100)
diego.checkResults("Brighton vs Arsenal")
print("Account balance: " + str(diego.money))

print("----------third match--------")
betplay.addMatch("PSG vs Clermont Foot", [1.33, 5.51, 8.01])
diego.chooseMatchTeamMoney("PSG vs Clermont Foot", "PSG", 0, 181)
betplay.setWinner("PSG vs Clermont Foot", "PSG")
diego.checkResults("PSG vs Clermont Foot")
print("Account balance: " + str(diego.money))

