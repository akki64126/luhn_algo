def luhn(cardno):
     
    no_of_digits = len(cardno)
    digit_sum = 0
    isSecond = False
     
    for i in range(no_of_digits - 1, -1, -1):
        d = ord(cardno[i]) - ord('0')
     
        if (isSecond == True):
            d = d * 2
        digit_sum += d // 10
        digit_sum += d % 10
  
        isSecond = not isSecond
     
    if (digit_sum % 10 == 0):
        return True
    else:
        return False
  
if __name__=="__main__":
     
    cardno = input("Enter your credit card number..")
     
    if (luhn(cardno)):
        print("This is a valid credit card")
    else:
        print("This is not a valid credit card")
