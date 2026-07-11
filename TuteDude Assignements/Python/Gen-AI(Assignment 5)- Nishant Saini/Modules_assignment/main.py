import math_utils
from math_utils import square

print(math_utils.add(5,10))
print(math_utils.subtract(100,500))
print(square(50))

# ---------------------------------------

import string_utils

text = "python"
print(string_utils.reverse_string(text))
print(string_utils.word_count(text))

#----------------------------------------

import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package import apply_tax


print(disc.apply_discount(1000,10))
print(disc.flat_discount(500))
print(calculate_total([500,800,750,450]))
print(apply_tax(1400))
