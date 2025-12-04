from hero import Hero

def initialize_heroes():
    
    heroes = {}
    
    # Carries 
    heroes["Anti-Mage"] = Hero("Anti-Mage", "Agility", "Carry", 52.3)
    heroes["Phantom Assassin"] = Hero("Phantom Assassin", "Agility", "Carry", 51.8)
    heroes["Juggernaut"] = Hero("Juggernaut", "Agility", "Carry", 53.1)
    heroes["Sven"] = Hero("Sven", "Strength", "Carry", 50.5)
    heroes["Medusa"] = Hero("Medusa", "Agility", "Carry", 48.9)
    heroes["Faceless Void"] = Hero("Faceless Void", "Agility", "Carry", 49.7)
    
    # Mid 
    heroes["Storm Spirit"] = Hero("Storm Spirit", "Intelligence", "Mid", 50.2)
    heroes["Invoker"] = Hero("Invoker", "Intelligence", "Mid", 48.5)
    heroes["Puck"] = Hero("Puck", "Intelligence", "Mid", 49.8)
    heroes["Queen of Pain"] = Hero("Queen of Pain", "Intelligence", "Mid", 50.9)
    heroes["Shadow Fiend"] = Hero("Shadow Fiend", "Agility", "Mid", 48.3)
    heroes["Templar Assassin"] = Hero("Templar Assassin", "Agility", "Mid", 51.2)
    
    # Offlane 
    heroes["Tidehunter"] = Hero("Tidehunter", "Strength", "Offlane", 52.0)
    heroes["Axe"] = Hero("Axe", "Strength", "Offlane", 51.5)
    heroes["Mars"] = Hero("Mars", "Strength", "Offlane", 50.8)
    heroes["Centaur Warrunner"] = Hero("Centaur Warrunner", "Strength", "Offlane", 51.9)
    heroes["Underlord"] = Hero("Underlord", "Strength", "Offlane", 50.3)
    heroes["Bristleback"] = Hero("Bristleback", "Strength", "Offlane", 52.7)
    
    # Supports 
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
    
    # CARRIES
    
    
    heroes["Anti-Mage"].add_counter("Storm Spirit")
    heroes["Anti-Mage"].add_counter("Invoker")
    heroes["Anti-Mage"].add_counter("Medusa")
    heroes["Anti-Mage"].add_counter("Crystal Maiden")
    heroes["Anti-Mage"].add_counter("Puck")
    heroes["Anti-Mage"].add_counter("Shadow Shaman")
    
    
    heroes["Phantom Assassin"].add_counter("Crystal Maiden")
    heroes["Phantom Assassin"].add_counter("Shadow Shaman")
    heroes["Phantom Assassin"].add_counter("Puck")
    heroes["Phantom Assassin"].add_counter("Rubick")
    heroes["Phantom Assassin"].add_counter("Ancient Apparition")
    
    
    heroes["Juggernaut"].add_counter("Crystal Maiden")
    heroes["Juggernaut"].add_counter("Lion")
    heroes["Juggernaut"].add_counter("Shadow Shaman")
    heroes["Juggernaut"].add_counter("Witch Doctor")
    heroes["Juggernaut"].add_counter("Vengeful Spirit")
    
    
    heroes["Sven"].add_counter("Phantom Assassin")
    heroes["Sven"].add_counter("Crystal Maiden")
    heroes["Sven"].add_counter("Lion")
    heroes["Sven"].add_counter("Shadow Shaman")
    heroes["Sven"].add_counter("Vengeful Spirit")
    
    
    heroes["Medusa"].add_counter("Phantom Assassin")
    heroes["Medusa"].add_counter("Juggernaut")
    heroes["Medusa"].add_counter("Sven")
    heroes["Medusa"].add_counter("Faceless Void")
    
    
    heroes["Faceless Void"].add_counter("Crystal Maiden")
    heroes["Faceless Void"].add_counter("Witch Doctor")
    heroes["Faceless Void"].add_counter("Shadow Shaman")
    heroes["Faceless Void"].add_counter("Ancient Apparition")
    heroes["Faceless Void"].add_counter("Lion")
    
    # MID 
    
    
    heroes["Storm Spirit"].add_counter("Crystal Maiden")
    heroes["Storm Spirit"].add_counter("Shadow Fiend")
    heroes["Storm Spirit"].add_counter("Templar Assassin")
    heroes["Storm Spirit"].add_counter("Shadow Shaman")
    heroes["Storm Spirit"].add_counter("Witch Doctor")
    
    
    heroes["Invoker"].add_counter("Phantom Assassin")
    heroes["Invoker"].add_counter("Crystal Maiden")
    heroes["Invoker"].add_counter("Shadow Shaman")
    heroes["Invoker"].add_counter("Vengeful Spirit")
    
    
    heroes["Puck"].add_counter("Crystal Maiden")
    heroes["Puck"].add_counter("Witch Doctor")
    heroes["Puck"].add_counter("Shadow Shaman")
    heroes["Puck"].add_counter("Shadow Fiend")  
    
    
    heroes["Queen of Pain"].add_counter("Crystal Maiden")
    heroes["Queen of Pain"].add_counter("Shadow Shaman")
    heroes["Queen of Pain"].add_counter("Invoker")
    heroes["Queen of Pain"].add_counter("Shadow Fiend")
    heroes["Queen of Pain"].add_counter("Dazzle")
    
    
    heroes["Shadow Fiend"].add_counter("Crystal Maiden")
    heroes["Shadow Fiend"].add_counter("Puck")
    heroes["Shadow Fiend"].add_counter("Rubick")
    heroes["Shadow Fiend"].add_counter("Ancient Apparition")
    
    
    heroes["Templar Assassin"].add_counter("Phantom Assassin")
    heroes["Templar Assassin"].add_counter("Faceless Void")
    heroes["Templar Assassin"].add_counter("Shadow Fiend")
    heroes["Templar Assassin"].add_counter("Lion")
    
    # OFFLANE
    
    
    heroes["Tidehunter"].add_counter("Phantom Assassin")
    heroes["Tidehunter"].add_counter("Juggernaut")
    heroes["Tidehunter"].add_counter("Sven")
    heroes["Tidehunter"].add_counter("Faceless Void")
    heroes["Tidehunter"].add_counter("Templar Assassin")
    
    
    heroes["Axe"].add_counter("Phantom Assassin")
    heroes["Axe"].add_counter("Dazzle")
    heroes["Axe"].add_counter("Bristleback")
    heroes["Axe"].add_counter("Oracle")
    heroes["Axe"].add_counter("Faceless Void")
    
    
    heroes["Mars"].add_counter("Phantom Assassin")
    heroes["Mars"].add_counter("Juggernaut")
    heroes["Mars"].add_counter("Faceless Void")
    heroes["Mars"].add_counter("Templar Assassin")
    heroes["Mars"].add_counter("Sven")
    
    
    heroes["Centaur Warrunner"].add_counter("Phantom Assassin")
    heroes["Centaur Warrunner"].add_counter("Juggernaut")
    heroes["Centaur Warrunner"].add_counter("Anti-Mage")
    heroes["Centaur Warrunner"].add_counter("Faceless Void")
    
    
    heroes["Underlord"].add_counter("Phantom Assassin")
    heroes["Underlord"].add_counter("Sven")
    heroes["Underlord"].add_counter("Juggernaut")
    heroes["Underlord"].add_counter("Templar Assassin")
    
    
    heroes["Bristleback"].add_counter("Crystal Maiden")
    heroes["Bristleback"].add_counter("Vengeful Spirit")
    heroes["Bristleback"].add_counter("Shadow Shaman")
    heroes["Bristleback"].add_counter("Dazzle")
    
    # SUPPORTS
    
    
    heroes["Crystal Maiden"].add_counter("Axe")
    heroes["Crystal Maiden"].add_counter("Centaur Warrunner")
    heroes["Crystal Maiden"].add_counter("Bristleback")
    
    
    heroes["Lion"].add_counter("Storm Spirit")
    heroes["Lion"].add_counter("Anti-Mage")
    heroes["Lion"].add_counter("Queen of Pain")
    heroes["Lion"].add_counter("Puck")
    heroes["Lion"].add_counter("Faceless Void")
    
    
    heroes["Shadow Shaman"].add_counter("Anti-Mage")
    heroes["Shadow Shaman"].add_counter("Phantom Assassin")
    heroes["Shadow Shaman"].add_counter("Faceless Void")
    heroes["Shadow Shaman"].add_counter("Templar Assassin")
    
    
    heroes["Witch Doctor"].add_counter("Phantom Assassin")
    heroes["Witch Doctor"].add_counter("Axe")
    heroes["Witch Doctor"].add_counter("Centaur Warrunner")
    heroes["Witch Doctor"].add_counter("Sven")
    
    
    heroes["Dazzle"].add_counter("Lion")
    heroes["Dazzle"].add_counter("Queen of Pain")
    heroes["Dazzle"].add_counter("Phantom Assassin")
    heroes["Dazzle"].add_counter("Templar Assassin")
    
    
    heroes["Oracle"].add_counter("Lion")
    heroes["Oracle"].add_counter("Axe")
    heroes["Oracle"].add_counter("Shadow Shaman")
    heroes["Oracle"].add_counter("Phantom Assassin")
    
    
    heroes["Vengeful Spirit"].add_counter("Templar Assassin")
    heroes["Vengeful Spirit"].add_counter("Shadow Fiend")
    heroes["Vengeful Spirit"].add_counter("Invoker")
    
    
    heroes["Rubick"].add_counter("Invoker")
    heroes["Rubick"].add_counter("Tidehunter")
    heroes["Rubick"].add_counter("Earthshaker")
    heroes["Rubick"].add_counter("Lion")
    
    
    heroes["Disruptor"].add_counter("Storm Spirit")
    heroes["Disruptor"].add_counter("Anti-Mage")
    heroes["Disruptor"].add_counter("Queen of Pain")
    heroes["Disruptor"].add_counter("Puck")
    heroes["Disruptor"].add_counter("Faceless Void")
    
    
    heroes["Ancient Apparition"].add_counter("Dazzle")
    heroes["Ancient Apparition"].add_counter("Oracle")
    heroes["Ancient Apparition"].add_counter("Juggernaut")
    heroes["Ancient Apparition"].add_counter("Bristleback")
    
    
    heroes["Earthshaker"].add_counter("Phantom Assassin")
    heroes["Earthshaker"].add_counter("Juggernaut")
    heroes["Earthshaker"].add_counter("Sven")
    
    
    heroes["Ogre Magi"].add_counter("Crystal Maiden")
    heroes["Ogre Magi"].add_counter("Puck")
    heroes["Ogre Magi"].add_counter("Rubick")
    heroes["Ogre Magi"].add_counter("Ancient Apparition")
    
    
    for hero_name, hero in heroes.items():
        for countered_hero_name in hero.counters:
            if countered_hero_name in heroes:
                heroes[countered_hero_name].add_countered_by(hero_name)
    
    return heroes