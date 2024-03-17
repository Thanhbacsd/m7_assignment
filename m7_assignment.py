import decimal
import math

# from decimal import *

# 1.
print('The value of Tau is {:^8,.4}, which is 1/2 tau is {:^8,.4}________'.format(math.tau, math.tau/2))
print()

# 2.

n_byte = int(input('Enter number of Bytes you would like to determine the signed range of:'))
n_bit = n_byte * 8
n_encode = 2 ** n_bit
n_above = n_encode/2
n_bellow = -n_above
print('{:^3} Byte(s) integral type with 8 bits can encode {:^18,.0f} numbers. \
The signed range will be from {:^18,.0f} to {:>15,.0f}'.format(n_byte, n_encode, n_bellow, n_above))
print()
# 3.
R = decimal.Decimal(8.3145)
M = decimal.Decimal(3.2e-2)
velocity = lambda t: 3 * R * (t + 273) / M
veloc_decimal = decimal.Decimal(velocity(25)).sqrt()
print('root mean square velocity = ', veloc_decimal)
print("The average velocity or root mean square velocity of a molecule in a sample of oxygen\
 at 25 degrees Celsius is {:^12,.3f} m/sec".format(veloc_decimal))