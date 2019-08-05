def binarify(num):
    if num <= 0: return '0'
    number = []
    while num != 0:
        if num % 2 == 0:
            number.append(0)
            num = int(num / 2)
        else:
            number.append(1)
            num = int(num / 2)
    result = [str(i) for i in number]
    return ''.join(result[::-1])

def binarify(num):
    number = []
    while num != 0:
        number.append(str(num % 2))
        num = int(num / 2)
    return ''.join(number[::-1])

print ("Test to convert 357 to base 2")
print (binarify(num = 357))
print ("Test to convert 69 to base 2")
print (binarify(69))

#############

def int_to_base2(num, base):
    number = []
    while num != 0:
        number.append(str(num % base))
        num = int(num / base)
    return ''.join(number[::-1])


def int_to_base(num, base):
    if num<=0:  return '0'
    number = []
    if num <= 0:
        return "Not possible"
    else:
        while num != 0:
            if num % base == 0:
                number.append(0)
                num = int(num / base)
            else:
                number.append(num % base)
                num = int(num / base)
    result = [str(i) for i in number]
    return ''.join(result[::-1])

print ("Test to convert 357 to base 3")
print (int_to_base2(15, 3))
print (int_to_base2(50, 2))
print ("Test to convert 69 to base 7")
print (int_to_base(69, 7))

3^0 = 1
3^1 = 3
3^2 = 9
3^3 = 27

15 = 120
6  = 20
0 = 0



#############

def base_to_int(string, base):
    if string=="0" or base <= 0 : return 0
    base_exp = len(string) - 1
    result = 0
    numbers = list(string)
    for i in numbers:
        result += int(i) * (int(base) ** base_exp)
        base_exp -= 1
    return result

print ("Test to convert 126 from base 7 to base 10")
print (base_to_int("126", 7))
print ("Test to convert 111020 from base 3 to base 10")
print (base_to_int("111020", 3))

##########

def flexibase_add(str1, str2, base1, base2):
  return base_to_int(str1, base1) + base_to_int(str2, base2)

print ("Add 11101 (base 2) to 111020 (base 3)")
print (flexibase_add("11101", "111020", 2, 3))

#######
def flexibase_multiply(str1, str2, base1, base2):
  return base_to_int(str1, base1) * base_to_int(str2, base2)

print ("Multiply 11101 (base 2) to 111020 (base 3)")
print (flexibase_multiply("11101", "111020", 2, 3))


#######
def romanify(num):
  if num <= 0:
      return "Please provide a positive integer"
  else:
      result = []
      while num != 0:
         if num >= 1000:
              result.append("M")
              num -= 1000
         elif num >= 900:
              result.append("CM")
              num -= 900
         elif num >= 500:
              result.append("D")
              num -= 500
         elif num >= 400:
              result.append("CD")
              num -= 400
         elif num >= 100:
             result.append("C")
             num -= 100
         elif num >= 90:
             result.append("XC")
             num -= 90
         elif num >= 50:
             result.append("L")
             num -= 50
         elif num >= 40:
             result.append("XL")
             num -= 40
         elif num >= 10:
             result.append("X")
             num -= 10
         elif num == 9:
             result.append("IX")
             num -= 9
         elif num in (8, 7, 6, 5):
             result.append("V")
             num -= 5
         elif num == 4:
             result.append("IV")
             num -= 4
         elif num in (3, 2, 1):
             result.append("I")
             num -= 1
         else:
             break
  return ''.join(result)

print ("Convert 1001 to Roman")
print (romanify(999))
print ("Convert 3549 to Roman")
print (romanify(3549))
print ("Try to convert 0, it will return an error.")
print (romanify(0))
