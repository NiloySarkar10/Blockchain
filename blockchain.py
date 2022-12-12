blockchain = [[1]]


def get_last_blockchain_value():
    ''' Returns the last blockchain value '''
    return blockchain[-1]


def add_value(transaction_amount):
    ''' Adds value to the blockchain 
    
    Arguments:
        :transaction_amount {int} -- amount to add to the blockchain
    '''
    blockchain.append([get_last_blockchain_value(), transaction_amount])

# Get user data
def get_user_data():
    ''' Returns the user data entered by the user '''
    return float(input('Please enter the amount: '))


