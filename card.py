import random


SUITS = {
    "Diamonds": 1,
    "Hearts": 2, 
    "Spades": 3,
    "Clubs":4
}

RANKS = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14
}

class PlayingCard:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.face_up = False

    def get_name(self):
        return " ".join([self.rank, "of", self.suit])
    
    def is_better_than(self, other_card):
        other_rank = RANKS[other_card.rank]
        our_rank = RANKS[self.rank]
        if our_rank > other_rank:
            return True
        if our_rank < other_rank:
            return False
        
        other_suit = SUITS[other_card.suit]
        our_suit = SUITS[self.suit]
        return (our_suit > other_suit)

class HighCardGameEvaluator:
    def find_winner(self, players):
        best_rank = None
        best_rank_suit = None
        best_candidate = None

        for player in players:
            if best_candidate is None:
                best_candidate = player
            print("Best Candidate", best_candidate.hand.card_by_index(0).get_name(), "Player :", player.hand.card_by_index(0).get_name())
            
            if player.hand.card_by_index(0).is_better_than(
                    best_candidate.hand.card_by_index(0)):
                best_candidate = player
        return best_candidate
    
class Deck:
    def __init__(self):
        self.cards = []
        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(PlayingCard(suit, rank))
    
    def add_card(self, card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def remove_top_card(self):
        return self.cards.pop()
    
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def card_by_index(self, index):
        try:
            return self.cards[index]
        except Exception:
            return None

    def remove_card(self):
        if not self.cards:
            return None
        return self.cards.pop()
      
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

class InternetStreamingView:    
    def show_player_and_hand(self, player_name, hand):
        # meaningful code goes here
        pass
    
    def show_winner(self, winner_name):
        # Meaningful code here
        pass
    
class BroadcastView:    
    def show_player_and_hand(self, player_name, hand):
        # meaningful code goes here
        pass
    
    def show_winner(self, winner_name):
        # Meaningful code here
        pass

    
class PlayerView:
    def prompt_for_new_player(self):
        new_player = input("Type the name of the player: ")
        if new_player == "":
            return None
        return new_player
    
    def show_player_and_hand(self, player_name, hand):
        print("[" + player_name + "]" )
        for card in hand.cards:
            if card.face_up:
                print(card.get_name())
            else:
                print("(hidden card)")
    
    def prompt_for_flip_cards(self):
        print("")
        prompt = input("Ready to see who won?")
        return True
    
    def show_winner(self, winner_name):
        print("")
        print("Congratulations", winner_name.name, "!")
    
    def prompt_for_new_game(self):
        print("")
        while True:
            prompt = input("Play again? Y/N: ")
            if prompt.capitalize() == "Y":
                return True
            if prompt.capitalize() == "N":
                return False

class GameController:
    def __init__(self, deck, player_view, broadcast_view, internet_streaming_view, game_evaluator):
        # Model
        self.players = []
        self.deck = deck

        # View
        self.views = [player_view, broadcast_view, internet_streaming_view]
        self.player_view = player_view
        # Controller
        self.game_evaluator = game_evaluator

    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            next_card = self.deck.remove_top_card()
            if next_card is not None:
                player.hand.add_card(next_card)

    def evaluate_game(self):
        best_candidate = None

        for player in self.players:
            if best_candidate is None:
                best_candidate = player
            
            if player.hand.card_by_index(0).is_better_than(
                    best_candidate.hand.card_by_index(0)):
                best_candidate = player
            return best_candidate

    def rebuild_deck(self):
        for player in self.players:
            while player.hand.cards:
                this_card = player.hand.remove_card()
                this_card.face_up = False
                self.deck.add_card(this_card)
        self.deck.shuffle()

    def add_player(self, player):
        new_player = Player(player)
        self.players.append(new_player)

    def run(self):
        while len(self.players) < 5:
            new_player = player_view.prompt_for_new_player()
            if new_player is None:
                print("here")
                break
            print(new_player)
            self.add_player(new_player)
                    
        while True:
            self.start_game()
            for view in self.views:
                for player in self.players:
                    view.show_player_and_hand(player.name, player.hand)
            player_view.prompt_for_flip_cards()
            for player in self.players:
                for card in player.hand.cards:
                    card.face_up = True
                for view in self.views:
                    view.show_player_and_hand(player.name, player.hand)
            
            for view in self.views:
                view.show_winner(self.game_evaluator.find_winner(self.players))
            
            
            if not player_view.prompt_for_new_game():
                break
            self.rebuild_deck()
            
            

# Calling code to build MVC and start the controller
deck = Deck()
player_view = PlayerView()
broadcast_view = BroadcastView()
internet_streaming_view = InternetStreamingView()
game_evaluator = HighCardGameEvaluator()

game_controller = GameController(deck, player_view, broadcast_view, internet_streaming_view, game_evaluator)
game_controller.run()