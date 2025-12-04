class Hero:
    def __init__(self, name, attribute, role, win_rate):
        self.name = name
        self.attribute = attribute
        self.role = role
        self.win_rate = win_rate
        self.counters = [] 
        self.countered_by = [] 
    
    def add_counter(self, hero_name):
        if hero_name not in self.counters:
            self.counters.append(hero_name)
    
    def add_countered_by(self, hero_name):
        if hero_name not in self.countered_by:
            self.countered_by.append(hero_name)
    
    def __str__(self):
        return f"{self.name} ({self.attribute} - {self.role}) - Win Rate: {self.win_rate}%"
    
    def __repr__(self):
        return f"Hero('{self.name}', '{self.attribute}', '{self.role}', {self.win_rate})"