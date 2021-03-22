import json
import os
import textwrap

from ascii_tarot.rng import quantum_rng

def main():
    # load list of cards
    with open(f"assets/cards.json") as f: 
        cards = json.load(f)

    with open(f"assets/greetings.json") as f: 
        print(json.load(f)['banner'])

    # pick a card using the quantum random number generator 
    n = int(quantum_rng(len(cards), 0))
    card = cards[n-1]

    while 'description' not in card.keys():
        n = int(quantum_rng(len(cards), 0))
        card = cards[n-1]
        
    # display the card 
    print(f"You drew the ~{card['name']}~")
    print(card['card'])
    if 'description' in card.keys():
        print(f"{textwrap.fill(card['description'])}\n")


if __name__=='__main__':
    main()
