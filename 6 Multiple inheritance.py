class People:
    def __init__(self,name,age,nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def method_speak(self):
        print("probe i can speak anything")
        
class WitchHunter:
    def __init__(self,skill):
            self.skill = skill
    def show_skill(self):
            print(f"My skill is: {self.skill}")
        
class MercenaryWitchHunter(People,WitchHunter):
    def __init__(self,name,age,nationality,skill,reward,company):
        People.__init__(self,name,age,nationality)
        WitchHunter.__init__(self,skill)
        self.reward = reward
        self.company = company
    
    def show(self):
        print(f'{self.show_skill()}')
    
mr_salary_man = MercenaryWitchHunter("paco",22,"czech","crafting of potions",1500,"tink")

mr_salary_man.show()
