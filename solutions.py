# Price Check
def priceCheck(products, productPrices, productSold, soldPrice):
    errors = 0
    products_dict = dict(zip(products, productPrices))
    for i in range(len(productSold)):
        if products_dict[productSold[i]] != soldPrice[i]:
            errors += 1
    return errors

# SQL
# I did not do the sql question because I know nosql, I would be happy to receive a nosql question if relevant

# Recursive Digit “Summer”
def recursive_digit_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + recursive_digit_sum(n // 10)

