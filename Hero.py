class Hero:
    """
    Represents a Dota 2 hero with attributes and statistics.
    """
    
    def __init__(self, name, attribute, role, win_rate):
        """
        Initialize a Hero object.
        
        Args:
            name (str): Hero name (e.g., "Anti-Mage")
            attribute (str): Primary attribute ("Strength", "Agility", "Intelligence")
            role (str): Primary role ("Carry", "Support", "Mid", "Offlane", "Roamer")
            win_rate (float): Win rate percentage (e.g., 52.5)
        """
        self.name = name
        self.attribute = attribute
        self.role = role
        self.win_rate = win_rate
        self.counters = []  # List of hero names this hero counters
        self.countered_by = []  # List of hero names that counter this hero
    
    def add_counter(self, hero_name):
        """Add a hero that this hero counters."""
        if hero_name not in self.counters:
            self.counters.append(hero_name)
    
    def add_countered_by(self, hero_name):
        """Add a hero that counters this hero."""
        if hero_name not in self.countered_by:
            self.countered_by.append(hero_name)
    
    def __str__(self):
        """String representation of the hero."""
        return f"{self.name} ({self.attribute} - {self.role}) - Win Rate: {self.win_rate}%"
    
    def __repr__(self):
        """Official string representation."""
        return f"Hero('{self.name}', '{self.attribute}', '{self.role}', {self.win_rate})"