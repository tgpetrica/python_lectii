from random import randint

class PigGame:
    SCORE = 30

    def __init__(self, player_name: str) -> None:
        self.player_name: str = player_name
        self.player_score: int = 0
        self.computer_score: int = 0
    
    @staticmethod
    def update_score(current_score: int, die_value: int) -> int:
        if die_value == 1:
            return 0
        return current_score + die_value
    
    def display_dash(self) -> None:
        print()
        print("*" * 25)
        print(f"Player {self.player_name}: {self.player_score}")
        print(f"Computer: {self.computer_score}")
        print("*" * 25)
        print()
    
    @staticmethod
    def simulate_roll_die() -> int:
        return randint(1, 6)
    
    def roll_dice(self) -> tuple[int, int]:
        player_die = self.simulate_roll_die()
        computer_die = self.simulate_roll_die()

        print(f"{self.player_name} rolls a {player_die}")
        print(f"Computer rolls a {computer_die}")

        return player_die, computer_die
    
    def is_winner(self) -> bool:
        if self.player_score >= self.SCORE:
            print(f"{self.player_name} won")
            return True
        
        if self.computer_score >= self.SCORE:
            print(f"Computer won")
            return True
        
        return False
    
    def welcome(self) -> None:
        print(
            f"""
            Bine ai venit la Pig Game!

            Reguli:
            - La fiecare runda, cei doi jucatori ({self.player_name}, Computer) arunca un zar.
            - Daca zarul afiseaza 1, pierzi TOATE punctele.
            - Altfel, valoarea afisata de zar se adauga scorului tau total.
            - Primul jucator care ajunge la {self.SCORE} puncte castiga jocul.

            Apasa ENTER pentru a incepe urmatoarea runda.
            Distractie placuta! Succes!
            """)
    
    def start(self) -> None:
        self.welcome()

        while True:
            input("Apasa ENTER pentru o runda noua")
            player, computer = self.roll_dice()

            self.player_score = self.update_score(self.player_score, player)
            self.computer_score = self.update_score(self.computer_score, computer)

            self.display_dash()

            if self.is_winner():
                break

if __name__ == "__main__":
    user = input("Care este numele tau? ")
    game = PigGame(user.strip() or "Player")
    game.start()

