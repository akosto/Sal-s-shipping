def c_ground_shipping(weight):
  flat = 20.00
  if weight <= 2:
    return (1.50 * weight) + flat
  elif 2 < weight <= 6:
    return (3.00 * weight) + flat
  elif 6 < weight <= 10:
    return (4.00 * weight) + flat
  elif weight > 10:
    return (4.75 * weight) + flat
  else:
    return "No deal."
print(c_ground_shipping(8.4))

c_pr_ground_shipping = 125.00

def c_drone_shipping(weight):
  if weight <= 2:
    return 4.50 * weight
  elif 2 < weight <= 6:
    return 9.00 * weight
  elif 6 < weight <= 10:
    return 12.00 * weight
  elif weight > 10:
    return 14.25 * weight
  else:
    return "No deal."
print(c_drone_shipping(1.5))

def cheapest_shipping(weight):
    
  if (c_ground_shipping(weight) < c_pr_ground_shipping) and (c_drone_shipping(weight) < c_ground_shipping(weight)):
    return ("Cheapest shipping method is drone shipping and the cost is " + str(c_drone_shipping(weight)) + ".")
  elif (c_ground_shipping(weight) < c_drone_shipping(weight)) and (c_ground_shipping(weight) < c_pr_ground_shipping):
    return ("Cheapest shipping method is ground shipping and the cost is " + str(c_ground_shipping(weight)) + ".")
  else:
    return ("Cheapest shipping method is premium ground shipping and the cost is " + str(c_pr_ground_shipping) + ".")
print(cheapest_shipping(41.5))
  
    
  
  
  
  
  