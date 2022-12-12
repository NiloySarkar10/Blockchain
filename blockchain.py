# initializing empty blockchain value
blockchain = []


def get_last_blockchain_value():
    ''' Returns the last blockchain value '''
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    ''' Adds value to the blockchain 
    
    Arguments:
        :transaction_amount {int} -- amount to add to the blockchain
        :last_transaction {list} -- list of the last transactions in the blockchain (default = [1])
    '''
    blockchain.append([last_transaction, transaction_amount])

# Get user data
def get_user_data():
    ''' Returns the user data entered by the user '''
    return float(input('Please enter the amount: '))


def get_user_input_and_add_to_blockchain(last_transaction_value=[1]):
    ''' Returns the user input and adds it to the blockchain
    
    Arguments:
        :last_transaction_value {int} -- indicator if the blockchain is empty or not
        (default = [1] indicates it is empty)'''
    tx_amount = get_user_data()
    if last_transaction_value == [1]:
        add_value(tx_amount)
    else:
        add_value(tx_amount, last_transaction_value)


get_user_input_and_add_to_blockchain()

while True:
    get_user_input_and_add_to_blockchain(get_last_blockchain_value())
    for value in blockchain:
        print(value)


