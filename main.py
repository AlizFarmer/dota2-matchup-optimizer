from hero_data import initialize_heroes, initialize_counter_relationships
from draft_analyzer import DraftRecommendation


class DotaDraftAnalyzer:
    
    def __init__(self):
        print("Loading heroes...")
        self.heroes = initialize_heroes()
        self.heroes = initialize_counter_relationships(self.heroes)
        self.draft_analyzer = DraftRecommendation(self.heroes)
        print(f"Loaded {len(self.heroes)} heroes successfully!\n")
    
    def display_menu(self):
        print("=" * 50)
        print("       DOTA 2 HERO DRAFT ANALYZER")
        print("=" * 50)
        print("1. View All Heroes")
        print("2. Search Hero by Name")
        print("3. Filter Heroes by Role")
        print("4. Filter Heroes by Attribute")
        print("5. View Hero Counters")
        print("6. Get Draft Recommendations")
        print("7. Exit")
        print("=" * 50)
    
    def view_all_heroes(self):
        print("\n" + "=" * 50)
        print("ALL HEROES")
        print("=" * 50)
        for hero_name in sorted(self.heroes.keys()):
            hero = self.heroes[hero_name]
            print(hero)
        print(f"\nTotal: {len(self.heroes)} heroes")
        print("=" * 50)
    
    def search_hero_by_name(self):
        hero_name = input("\nEnter hero name: ").strip()
        if hero_name in self.heroes:
            hero = self.heroes[hero_name]
            print("\n" + "-" * 50)
            print(f"Found: {hero}")
            print(f"Counters: {', '.join(hero.counters) if hero.counters else 'None yet'}")
            print(f"Countered by: {', '.join(hero.countered_by) if hero.countered_by else 'None yet'}")
            print("-" * 50)
        else:
            print(f"\nHero '{hero_name}' not found!")
    
    def filter_by_role(self):
        role = input("\nEnter role (Carry/Mid/Offlane/Support): ").strip()
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
        attribute = input("\nEnter attribute (Strength/Agility/Intelligence): ").strip()
        matching_heroes = [hero for hero in self.heroes.values() if hero.attribute.lower() == attribute.lower()]
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
        hero_name = input("\nEnter hero name: ").strip()
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
    
    def get_draft_recommendations(self):
        print("\n" + "=" * 70)
        print("DRAFT RECOMMENDATIONS")
        print("=" * 70)
        enemy_input = input("\nEnter enemy team heroes (comma-separated): ").strip()
        if not enemy_input:
            print("No enemy heroes entered!")
            return
        enemy_team = [hero.strip() for hero in enemy_input.split(",")]
        print(f"\nEnemy Team: {', '.join(enemy_team)}")
        print("\nChoose recommendation strategy:")
        print("A) Counter the MOST enemy heroes")
        print("B) Counter their STRONGEST hero")
        strategy = input("\nEnter choice (A/B): ").strip().upper()
        if strategy == "A":
            recommendations = self.draft_analyzer.strategy_counter_most(enemy_team, top_n=5)
            self.draft_analyzer.display_recommendations_strategy_a(recommendations)
        elif strategy == "B":
            recommendations = self.draft_analyzer.strategy_counter_strongest(enemy_team, top_n=5)
            self.draft_analyzer.display_recommendations_strategy_b(recommendations)
        else:
            print("Invalid choice!")
    
    def run(self):
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
                self.get_draft_recommendations()
            elif choice == "7":
                print("\nThank you for using Dota 2 Draft Analyzer!")
                break
            else:
                print("\nInvalid choice!")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    app = DotaDraftAnalyzer()
    app.run()
    