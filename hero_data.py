from hero import Hero

def initialize_heroes():
    """
    Creates and returns a dictionary (hash map) of 30 Dota 2 heroes.
    Key: Hero name (string)
    Value: Hero object
    """
    
    heroes = {}
    
    # Carries (6 heroes)
    heroes["Anti-Mage"] = Hero("Anti-Mage", "Agility", "Carry", 52.3)
    heroes["Phantom Assassin"] = Hero("Phantom Assassin", "Agility", "Carry", 51.8)
    heroes["Juggernaut"] = Hero("Juggernaut", "Agility", "Carry", 53.1)
    heroes["Sven"] = Hero("Sven", "Strength", "Carry", 50.5)
    heroes["Medusa"] = Hero("Medusa", "Agility", "Carry", 48.9)
    heroes["Faceless Void"] = Hero("Faceless Void", "Agility", "Carry", 49.7)
    
    # Mid Heroes (6 heroes)
    heroes["Storm Spirit"] = Hero("Storm Spirit", "Intelligence", "Mid", 50.2)
    heroes["Invoker"] = Hero("Invoker", "Intelligence", "Mid", 48.5)
    heroes["Puck"] = Hero("Puck", "Intelligence", "Mid", 49.8)
    heroes["Queen of Pain"] = Hero("Queen of Pain", "Intelligence", "Mid", 50.9)
    heroes["Shadow Fiend"] = Hero("Shadow Fiend", "Agility", "Mid", 48.3)
    heroes["Templar Assassin"] = Hero("Templar Assassin", "Agility", "Mid", 51.2)
    
    # Offlane (6 heroes)
    heroes["Tidehunter"] = Hero("Tidehunter", "Strength", "Offlane", 52.0)
    heroes["Axe"] = Hero("Axe", "Strength", "Offlane", 51.5)
    heroes["Mars"] = Hero("Mars", "Strength", "Offlane", 50.8)
    heroes["Centaur Warrunner"] = Hero("Centaur Warrunner", "Strength", "Offlane", 51.9)
    heroes["Underlord"] = Hero("Underlord", "Strength", "Offlane", 50.3)
    heroes["Bristleback"] = Hero("Bristleback", "Strength", "Offlane", 52.7)
    
    # Supports (12 heroes)
    heroes["Crystal Maiden"] = Hero("Crystal Maiden", "Intelligence", "Support", 50.1)
    heroes["Lion"] = Hero("Lion", "Intelligence", "Support", 51.4)
    heroes["Shadow Shaman"] = Hero("Shadow Shaman", "Intelligence", "Support", 50.6)
    heroes["Witch Doctor"] = Hero("Witch Doctor", "Intelligence", "Support", 52.8)
    heroes["Dazzle"] = Hero("Dazzle", "Intelligence", "Support", 49.9)
    heroes["Oracle"] = Hero("Oracle", "Intelligence", "Support", 48.7)
    heroes["Vengeful Spirit"] = Hero("Vengeful Spirit", "Agility", "Support", 50.4)
    heroes["Rubick"] = Hero("Rubick", "Intelligence", "Support", 49.5)
    heroes["Disruptor"] = Hero("Disruptor", "Intelligence", "Support", 50.0)
    heroes["Ancient Apparition"] = Hero("Ancient Apparition", "Intelligence", "Support", 51.1)
    heroes["Earthshaker"] = Hero("Earthshaker", "Strength", "Support", 50.7)
    heroes["Ogre Magi"] = Hero("Ogre Magi", "Intelligence", "Support", 53.2)
    
    return heroes


def initialize_counter_relationships(heroes):
    """
    Sets up counter relationships between heroes.
    This creates the graph structure (adjacency list).
    """
    
    # Anti-Mage counters (mana-dependent heroes)
    heroes["Anti-Mage"].add_counter("Storm Spirit")
    heroes["Anti-Mage"].add_counter("Invoker")
    heroes["Anti-Mage"].add_counter("Medusa")
    heroes["Anti-Mage"].add_counter("Crystal Maiden")
    
    # Storm Spirit counters
    heroes["Storm Spirit"].add_counter("Crystal Maiden")
    heroes["Storm Spirit"].add_counter("Shadow Fiend")
    heroes["Storm Spirit"].add_counter("Templar Assassin")
    
    # Axe counters
    heroes["Axe"].add_counter("Phantom Assassin")
    heroes["Axe"].add_counter("Dazzle")
    heroes["Axe"].add_counter("Bristleback")
    
    # Queen of Pain counters
    heroes["Queen of Pain"].add_counter("Crystal Maiden")
    heroes["Queen of Pain"].add_counter("Shadow Shaman")
    heroes["Queen of Pain"].add_counter("Invoker")
    
    # Juggernaut counters
    heroes["Juggernaut"].add_counter("Crystal Maiden")
    heroes["Juggernaut"].add_counter("Lion")
    heroes["Juggernaut"].add_counter("Witch Doctor")
    
    # Tidehunter counters
    heroes["Tidehunter"].add_counter("Phantom Assassin")
    heroes["Tidehunter"].add_counter("Juggernaut")
    heroes["Tidehunter"].add_counter("Sven")
    
    # Lion counters
    heroes["Lion"].add_counter("Storm Spirit")
    heroes["Lion"].add_counter("Anti-Mage")
    heroes["Lion"].add_counter("Queen of Pain")
    
    # Oracle counters
    heroes["Oracle"].add_counter("Axe")
    heroes["Oracle"].add_counter("Lion")
    
    # Silencer-like counters (using Disruptor as substitute)
    heroes["Disruptor"].add_counter("Storm Spirit")
    heroes["Disruptor"].add_counter("Anti-Mage")
    heroes["Disruptor"].add_counter("Queen of Pain")
    
    # Now set up reverse relationships (countered_by)
    for hero_name, hero in heroes.items():
        for countered_hero_name in hero.counters:
            if countered_hero_name in heroes:
                heroes[countered_hero_name].add_countered_by(hero_name)
    
    return heroes