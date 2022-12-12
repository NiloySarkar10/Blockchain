# initializing empty blockchain value
blockchain = []
open_transactions = []
owner = 'Niloy'


def get_last_blockchain_value():
    ''' Returns the last value of the current blockchain'''
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    ''' Append a new value as well as the last blockchain value to the blockchain
    
    Arguments:
        :sender: The sender of the coins
        :recipient: The recipient of the coins
        :amount: The amount of coins to be sent in the transaction (default = 1.0)
    '''
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    pass


def get_transaction_value():
    '''Returns the input of the user (a new transaction amount and recipient)'''
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Enter the transaction amount: '))
    return tx_amount, tx_recipient


def get_user_choice():
    '''Prompts user for their choice and returns it'''
    user_input = input('Enter your choice: ')
    return user_input


def print_blockchain_elements():
    '''Output all blocks of the blockchain'''
    for block in blockchain:
        print(block)
    else:
        print('-' * 50)


def verify_chain():
    '''Verify the current blockchain and return true if it is valid.'''
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            # for the first block, we will be skipping as there will be no previous block
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid


waiting_for_input = True

# A while loop for the user to enter the transaction
while waiting_for_input:
    print('Please choose:')
    print('1. Add a new transaction')
    print('2. View the current blockchain')
    print('x. Try to manipulate the blockchain (will result in invalidating the blockchain, as it is not permitted')
    print('q. Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data     # Tuple unpacking
        # Adding transaction to the blockchain
        add_transaction(recipient, amount=amount)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'x':
        if len(blockchain) >= 1:
            # This condition is purely experimental to check if we are able to prevent user from manipulating
            # the blockchain. This option will not be provided to the user, but in order to test the prevention of
            # manipulation, we are adding this so that our blockchain is secure
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Invalid choice. Kindly select one from the list.')

    # if the user tried manipulating the blockchain by entering 'x'
    if not verify_chain():
        print('----------------------Blockchain invalid--------------------------------')
        print_blockchain_elements()
        print('*' * 50)
        break
else:
    print('User left!')


print('OVER.')













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


