
# assertions to find irrecoverable errors in a program, not to signal file not found
# meant to be internal selfchecks, by declaring some conditions are impossible in the code.
# not a mechanism for handling runtime errors.
# asserts can be globally disabled with an interpreter setting - beware

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price
# this should work
shoes = {'name':'Fancy Shoes', 'price':14900}
print(apply_discount(shoes, 0.25))

# raises an AssertionError b/c violates condition
print(apply_discount(shoes, 2.0))