def price_mapper(price):
    """
    Behaviour : The function does the following:
        1.Transform the Price into required format
        2. Transform the datatype of Price from string to numerical number.
   
    Args
        price(string) : form of price in original data
    Returns:
        price(string) : float form of price.
    """
    price = price.replace('$','')
    price = price.replace('.00','')
    price = price.replace(',','')
    return float(price)