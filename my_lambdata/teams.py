# example teams.py (oop approach)

class Team():
    def __init__(self, name, city):
        self.name = name
        self.city = city


    def advertise(self):
        #print(f"HEY COME TO {my_team['city'].upper()} TO SEE OUR GAMES!!!")
        print(f"HEY COME TO {self.city.upper()} TO SEE OUR GAMES!!!")

    @property
    def full_name(self):
        #return f"{my_team['city']} {my_team['name']}"
        return f"{self.city} {self.name}"

if __name__ == "__main__":
    teams = [
        {"city": "New York", "name": "Yankees"},
        {"city": "New York", "name": "Mets"},
        {"city": "Boston", "name": "Red Sox"},
       {"city": "New Haven", "name": "Ravens"},
        {"city": "Washington", "name": "Nationals"}
    ]

    for team_attributes in teams:
        team = Team(name= team_attributes['name'], city=team_attributes['city'])
        print("-------")
        #print(full_name(team))
        #advertise(team)
        print(team.city)
        print(team.full_name)
        team.advertise()
    
    # df1 = DataFrame({'x': [1,2,3], 'y': [4,5,6]})
    # df1.head()
    # df1.columns
    # df2 = DataFrame({'x': [7,7,7], 'y': [4,4,4]})
    # df2.head()

    #team = Team(city='Washington', name='Wizards')  # initializ/create instance of objec
    #print(team)
    #print(type(team))
    #print(team.name) # invoking attributes
    #print(team.city) # invoking attributes

    #team2 = Team('Giants', 'New York')  # initializ/create instance of objec
    #print(team2)
    #print(type(team2))
    #print(team2.name) # invoking attributes
    #print(team2.city) # invoking attributes