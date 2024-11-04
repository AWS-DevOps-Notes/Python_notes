
print('This is app start')
import sales  
import sys
sys.path.append('c:\\Users\h')
print(sys.path)
import os
print(os.__file__)
import math
import purchase
purchase.create_supplier()
sales.add_customer()
sales.add_sales_order()
print(sales.a)
print('This is app end')


import erp