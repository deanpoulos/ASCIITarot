import json
import os
import requests

def quantum_rng(N, dec):
    '''
    This function generates n random numbers between 0 and maxnum
    by calling Australian National University's API. 
    The reason why we're using this custom function instead of the 
    one built-in one is that ANU's numbers are generated in the
    university's lab by measuring the quantum fluctuations of the vacuum. 
    By doing so, we ensure true randomness.
    '''
    anu_data = requests.get('https://qrng.anu.edu.au/API/jsonI.php?length='+str(N)+'&type=uint8').json()

    return round((anu_data['data'][0] / 255) * N, dec)

def main():

    source_dir = os.path.dirname(__file__)  # "~/projects/tarot"  

    # load list of cards
    with open(f"{source_dir}/../assets/cards.json") as f: 
        cards = json.load(f)

    with open(f"{source_dir}/../assets/greetings.json") as f: 
        print(json.load(f)['banner'])
dean
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
        print(card['description'])


if __name__=='__main__':
    main()

