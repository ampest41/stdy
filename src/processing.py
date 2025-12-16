def filter_by_state(transactions,state_value='EXECUTED'):
    '''Фунция принимает список и сортирует по ключу state'''
    filtered_transactions=[]
    for transaction in transactions:
        if transaction['state']==state_value:
            filtered_transactions.append(transaction)
    return filtered_transactions






