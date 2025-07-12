from datetime import date

class Person:
    def __init__(self, personId, firstName, lastName, dateOfBirth, nationality):
        self.personId = personId
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.nationality = nationality

    def getFullName(self):
        return f"{self.firstName} {self.lastName}"

    def getAge(self):
        return date.today().year - self.dateOfBirth.year

class Coach(Person):
    def __init__(self, personId, firstName, lastName, dateOfBirth, nationality, role, experienceYears):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self.role = role
        self.experienceYears = experienceYears

    def coachTeam(self):
        return f"{self.getFullName()} is coaching the team as {self.role}"

class Player(Person):
    def __init__(self, personId, firstName, lastName, dateOfBirth, nationality, position, contractStartDate, contractEndDate):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self.position = position
        self.contractStartDate = contractStartDate
        self.contractEndDate = contractEndDate

    def playGame(self):
        return f"{self.getFullName()} is playing in position {self.position}"

    def renewContract(self, newEndDate, newValue):
        self.contractEndDate = newEndDate
        return f"Contract renewed until {newEndDate} with value {newValue}"

class Staff(Person):
    def __init__(self, personId, firstName, lastName, dateOfBirth, nationality, duty, assignedTeam):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self.duty = duty
        self.assignedTeam = assignedTeam

    def assist(self):
        return f"{self.getFullName()} is assisting with {self.duty}"

class PersonFactory:
    def createPerson(self, role, personId, firstName, lastName, birthDate, nationality, extraInfo):
        if role == 'coach':
            return Coach(personId, firstName, lastName, birthDate, nationality, extraInfo, 10)
        elif role == 'player':
            return Player(personId, firstName, lastName, birthDate, nationality, extraInfo, date(2021, 1, 1), date(2024, 1, 1))
        elif role == 'staff':
            return Staff(personId, firstName, lastName, birthDate, nationality, extraInfo, 'Team A')
        else:
            raise ValueError("Unknown role")

class Club:
    def __init__(self, clubId, name, foundingDate, budget, league, stadiumId):
        self.clubId = clubId
        self.name = name
        self.foundingDate = foundingDate
        self.budget = budget
        self.league = league
        self.stadiumId = stadiumId
        self.teams = []

    def manageBudget(self):
        return f"Managing budget of {self.budget}."

    def signSponsor(self, sponsor):
        return f"Signed sponsor {sponsor.getFullName()}."

    def getTeams(self):
        return self.teams

    def addTeam(self, team):
        self.teams.append(team)

class Team:
    def __init__(self, teamId, name, clubId):
        self.teamId = teamId
        self.name = name
        self.clubId = clubId
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        self.players.remove(player)

factory = PersonFactory()

coach = factory.createPerson('coach', 'C001', 'John', 'Doe', date(1980, 1, 1), 'USA', 'Head Coach')
player = factory.createPerson('player', 'P001', 'Jane', 'Smith', date(2000, 5, 15), 'England', 'Striker')
staff = factory.createPerson('staff', 'S001', 'James', 'Lee', date(1995, 3, 25), 'Canada', 'Medical')

club = Club('CL001', 'FC Cakrawala', date(2000, 1, 1), 5000000, 'Premier League', 'ST001')
team = Team('T001', 'Cakrawala Muda', 'CL001')

team.addPlayer(player)
team.addPlayer(Player('P002', 'Bob', 'Johnson', date(1999, 2, 10), 'USA', 'Midfielder', date(2021, 1, 1), date(2024, 1, 1)))
team.addPlayer(Player('P003', 'Alice', 'Williams', date(1998, 3, 15), 'UK', 'Defender', date(2022, 1, 1), date(2025, 1, 1)))

club.addTeam(team)

print(coach.coachTeam())
print(player.playGame())
print(staff.assist())
print(club.manageBudget())
print(f"Club {club.name} has teams: {[team.name for team in club.getTeams()]}")
