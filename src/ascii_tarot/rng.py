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
