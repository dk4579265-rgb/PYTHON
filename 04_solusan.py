###########  CREAT A FUNCTION RETURN AREA CIRRCUMFENCE OF CIRCAL  ###
import math
def  circle_stats(redius):
      area=math.pi* redius **2              # firmula area ka
      circumference=2 * math.pi * redius
      return area,circumference

a,c =circle_stats(3)
  
print("Area:",a, "circumference:",c)



### output Area: 28.274333882308138 circumference: 18.84955592153876