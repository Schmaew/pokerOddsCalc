from table import HoldemTable
from pprint import pprint

# Initialize the HoldemTable with the desired number of players and deck type
ht = HoldemTable(num_players=5, deck_type='full')

# Assign cards to Player 1
ht.add_to_hand(1, ['Td', 'Ad'])

# Proceed to the next round, which randomly assigns cards to the other players
ht.next_round()

# Enter current community cards (e.g., ['Kh', 'Qh', 'Jd'] for the flop)
ht.add_to_community(['Kh', 'Qh', 'Jd'])

# Simulate the game and get the results
result = ht.simulate()

# Pretty-print the results for easier monitoring
pprint(result)
