def priceCheck(products, productPrices, productSold, soldPrice):
    errors = 0
    products_dict = dict(zip(products, productPrices))
    for i in range(len(productSold)):
        if products_dict[productSold[i]] != soldPrice[i]:
            errors += 1
    return errors



def recursive_digit_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + recursive_digit_sum(n // 10)

