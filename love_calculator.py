from __future__ import print_function

def love_calculator(v1,v2):
    return((v1+v2/1982462)/10000)

if __name__ == "__main__":
    val1 = int(input("Enter your DOB in YYMMDD format : "))
    val2 = int(input("Enter your partner's DOB in YYMMDD format : "))
    result=love_calculator(val1,val2)
    print(f"Your partner loves you {result}")
