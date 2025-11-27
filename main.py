from hero_data import initialize_heroes, initialize_counter_relationships


class DotaDraftAnalyzer:
    """
    Main application class for Dota 2 Draft Analyzer.
    Uses a hash map (dictionary) to store heroes for O(1) lookup.
    """
    
    def __init__(self):
        """Initialize the application with hero data."""
        print("Loading heroes...")
        self.heroes = initialize_heroes()  # Dictionary (Hash Map)
        self.heroes = initialize_counter_relationships(self.heroes)
        print(f"Loaded {len(self.heroes)} heroes successfully!\n")
    
    def display_menu(self):
        """Display the main menu."""
        print("=" * 50)
        print("       DOTA 2 HERO DRAFT ANALYZER")
        print("=" * 50)
        print("1. View All Heroes")
        print("2. Search Hero by Name")
        print("3. Filter Heroes by Role")
        print("4. Filter Heroes by Attribute")
        print("5. View Hero Counters")
        print("6. Get Draft Recommendations (Coming Soon)")
        print("7. Exit")
        print("=" * 50)
    
    def view_all_heroes(self):
        """Display all heroes in the database."""
        print("\n" + "=" * 50)
        print("ALL HEROES")
        print("=" * 50)
        
        for hero_name in sorted(self.heroes.keys()):
            hero = self.heroes[hero_name]
            print(hero)
        
        print(f"\nTotal: {len(self.heroes)} heroes")
        print("=" * 50)
    
    def search_hero_by_name(self):
        """Search for a hero by exact name (Hash map O(1) lookup)."""
        hero_name = input("\nEnter hero name: ").strip()
        
        # Hash map lookup - O(1) average case
        if hero_name in self.heroes:
            hero = self.heroes[hero_name]
            print("\n" + "-" * 50)
            print(f"Found: {hero}")
            print(f"Counters: {', '.join(hero.counters) if hero.counters else 'None yet'}")
            print(f"Countered by: {', '.join(hero.countered_by) if hero.countered_by else 'None yet'}")
            print("-" * 50)
        else:
            print(f"\nHero '{hero_name}' not found!")
            print("Tip: Check spelling or use option 1 to see all heroes.")
    
    def filter_by_role(self):
        """Filter heroes by role using linear search O(n)."""
        role = input("\nEnter role (Carry/Mid/Offlane/Support/Roamer): ").strip()
        
        # Linear search through dictionary - O(n)
        matching_heroes = [hero for hero in self.heroes.values() if hero.role.lower() == role.lower()]
        
        if matching_heroes:
            print(f"\n{'=' * 50}")
            print(f"{role.upper()} HEROES ({len(matching_heroes)} found)")
            print("=" * 50)
            for hero in sorted(matching_heroes, key=lambda h: h.name):
                print(hero)
            print("=" * 50)
        else:
            print(f"\nNo heroes found with role '{role}'")
    
    def filter_by_attribute(self):
        """Filter heroes by attribute using linear search O(n)."""
        attribute = input("\nEnter attribute (Strength/Agility/Intelligence): ").strip()
        
        # Linear search - O(n)
        matching_heroes = [hero for hero in self.heroes.values() 
                          if hero.attribute.lower() == attribute.lower()]
        
        if matching_heroes:
            print(f"\n{'=' * 50}")
            print(f"{attribute.upper()} HEROES ({len(matching_heroes)} found)")
            print("=" * 50)
            for hero in sorted(matching_heroes, key=lambda h: h.name):
                print(hero)
            print("=" * 50)
        else:
            print(f"\nNo heroes found with attribute '{attribute}'")
    
    def view_hero_counters(self):
        """Display what heroes counter a specific hero."""
        hero_name = input("\nEnter hero name: ").strip()
        
        # Hash map lookup - O(1)
        if hero_name in self.heroes:
            hero = self.heroes[hero_name]
            print(f"\n{'=' * 50}")
            print(f"COUNTER INFORMATION: {hero.name}")
            print("=" * 50)
            print(f"\n{hero.name} COUNTERS:")
            if hero.counters:
                for counter in hero.counters:
                    print(f"  - {counter}")
            else:
                print("  - None defined yet")
            
            print(f"\n{hero.name} IS COUNTERED BY:")
            if hero.countered_by:
                for counter in hero.countered_by:
                    print(f"  - {counter}")
            else:
                print("  - None defined yet")
            print("=" * 50)
        else:
            print(f"\nHero '{hero_name}' not found!")
    
    def run(self):
        """Main application loop."""
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == "1":
                self.view_all_heroes()
            elif choice == "2":
                self.search_hero_by_name()
            elif choice == "3":
                self.filter_by_role()
            elif choice == "4":
                self.filter_by_attribute()
            elif choice == "5":
                self.view_hero_counters()
            elif choice == "6":
                print("\n[Feature coming in Phase 3!]")
            elif choice == "7":
                print("\nThank you for using Dota 2 Draft Analyzer!")
                print("Good luck with your drafts!")
                break
            else:
                print("\nInvalid choice! Please enter 1-7.")
            
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    app = DotaDraftAnalyzer()
    app.run()