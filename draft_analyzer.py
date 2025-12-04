from sorting import quick_sort


class DraftRecommendation:
    
    def __init__(self, heroes_dict):
        """
        Initialize with the heroes dictionary.
        
        Args:
            heroes_dict: Dictionary of all heroes (hash map)
        """
        self.heroes = heroes_dict
    
    def get_counter_score(self, hero, enemy_team):
        """
        Calculate how many enemies this hero counters and which ones.
        
        Args:
            hero: Hero object
            enemy_team: List of enemy hero names
        
        Returns:
            Tuple: (counter_score, list of enemy names countered)
        """
        countered_enemies = []
        for enemy_name in enemy_team:
            if enemy_name in hero.counters:
                countered_enemies.append(enemy_name)
        return len(countered_enemies), countered_enemies
    
    def strategy_counter_most(self, enemy_team, top_n=5):
        """
        Strategy A: Recommend heroes that counter the MOST enemies.
        
        Algorithm:
        1. Calculate counter score for each hero (O(n * m) where m = enemy team size)
        2. Sort heroes by counter score using Quick Sort (O(n log n))
        3. Return top N heroes
        
        Total Complexity: O(n * m + n log n) ≈ O(n log n) for small m
        
        Args:
            enemy_team: List of enemy hero names
            top_n: Number of recommendations to return
        
        Returns:
            List of (hero, counter_score) tuples
        """
        # Validate enemy team
        valid_enemies = []
        for enemy_name in enemy_team:
            if enemy_name in self.heroes:
                valid_enemies.append(enemy_name)
            else:
                print(f"Warning: '{enemy_name}' not found in database.")
        
        if not valid_enemies:
            return []
        
        # Calculate counter scores for all heroes
        hero_scores = []
        for hero_name, hero in self.heroes.items():
            # Don't recommend heroes that are already picked by enemy
            if hero_name not in valid_enemies:
                score, countered_list = self.get_counter_score(hero, valid_enemies)
                if score > 0:  # Only include heroes that counter at least 1 enemy
                    hero_scores.append((hero, score, countered_list))
        
        # Sort using Quick Sort - descending order by score
        sorted_heroes = quick_sort(
            hero_scores,
            key=lambda x: x[1],  # Sort by score
            reverse=True  # Highest score first
        )
        
        return sorted_heroes[:top_n]
    
    def strategy_counter_strongest(self, enemy_team, top_n=5):
        """
        Strategy B: Recommend heroes that counter the STRONGEST enemy 
        (enemy with highest win rate).
        
        Algorithm:
        1. Find enemy with highest win rate (O(m))
        2. Get all heroes that counter this enemy (O(n))
        3. Sort by their own win rate using Quick Sort (O(k log k) where k = counters)
        4. Return top N
        
        Args:
            enemy_team: List of enemy hero names
            top_n: Number of recommendations to return
        
        Returns:
            List of (hero, enemy_countered, enemy_win_rate) tuples
        """
        # Validate and get enemy hero objects
        valid_enemies = []
        for enemy_name in enemy_team:
            if enemy_name in self.heroes:
                valid_enemies.append(self.heroes[enemy_name])
            else:
                print(f"Warning: '{enemy_name}' not found in database.")
        
        if not valid_enemies:
            return []
        
        # Find strongest enemy (highest win rate)
        strongest_enemy = max(valid_enemies, key=lambda h: h.win_rate)
        
        print(f"\nTarget: {strongest_enemy.name} (Win Rate: {strongest_enemy.win_rate}%)")
        print(f"Finding heroes that counter {strongest_enemy.name}...\n")
        
        # Find all heroes that counter the strongest enemy
        counter_heroes = []
        for hero_name, hero in self.heroes.items():
            # Don't recommend heroes already picked by enemy
            if hero_name not in enemy_team:
                if strongest_enemy.name in hero.counters:
                    counter_heroes.append(hero)
        
        if not counter_heroes:
            print(f"No heroes in database counter {strongest_enemy.name} yet.")
            return []
        
        # Sort counters by their own win rate (best counters first)
        sorted_counters = quick_sort(
            counter_heroes,
            key=lambda h: h.win_rate,
            reverse=True
        )
        
        # Return as tuples with context
        results = []
        for hero in sorted_counters[:top_n]:
            results.append((hero, strongest_enemy.name, strongest_enemy.win_rate))
        
        return results
    
    def display_recommendations_strategy_a(self, recommendations):
        """Display Strategy A results (counter most enemies)."""
        if not recommendations:
            print("No recommendations found.")
            return
        
        print("\n" + "=" * 80)
        print("DRAFT RECOMMENDATIONS - STRATEGY A: Counter Most Enemies")
        print("=" * 80)
        print(f"{'Rank':<6} {'Hero':<25} {'Win Rate':<12} {'Counters':<35}")
        print("-" * 80)
        
        for rank, (hero, counter_score, countered_list) in enumerate(recommendations, 1):
            counters_str = ", ".join(countered_list)
            print(f"{rank:<6} {hero.name:<25} {hero.win_rate}%{'':<8} {counters_str}")
        
        print("=" * 80)
    
    def display_recommendations_strategy_b(self, recommendations):
        """Display Strategy B results (counter strongest enemy)."""
        if not recommendations:
            print("No recommendations found.")
            return
        
        print("\n" + "=" * 70)
        print("DRAFT RECOMMENDATIONS - STRATEGY B: Counter Strongest Enemy")
        print("=" * 70)
        print(f"{'Rank':<6} {'Hero':<25} {'Counters':<20} {'Win Rate':<10}")
        print("-" * 70)
        
        for rank, (hero, enemy_name, enemy_wr) in enumerate(recommendations, 1):
            print(f"{rank:<6} {hero.name:<25} {enemy_name:<20} {hero.win_rate}%")
        

        print("=" * 70)
