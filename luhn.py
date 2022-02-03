def luhn(cardno):
     
    no_of_digits = len(cardno)
    digit_sum = 0
    value = False
    if no_of_digits>13 and no_of_digits<=16:
     
        for i in range(no_of_digits - 1, -1, -1):
            d = ord(cardno[i]) - ord('0')
        
            if (value == True):
                d = d * 2
            digit_sum += d // 10
            digit_sum += d % 10
    
            value = not value
        
        if (digit_sum % 10 == 0):
            return True
        else:
            return False
    else:
    
        return False
  
if __name__=="__main__":
     
    cardno = input()
     
    if (luhn(cardno)):
        print("This is a valid credit card")
    else:
        print("This is not a valid credit card")
