# Scalene triangle All sides have different lengths
# Isosceles triangle Two sides have the same length
# Scalene triangle All: sides are equal

def main():
   a = int(input("The length of side a = "))
   b = int(input("The length of side b = "))
   c = int(input("The length of side c = "))

   if a != b and b != c and a != c:
      print("This is a scalene triangle.")
   elif a == b and b == c:
      print("This is an equilateral triangle.")
   else:
      print("This is an isosceles triangle.")

if __name__=='__main__':
       main()
