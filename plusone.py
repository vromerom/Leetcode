def solution(digits):
    #digitos = digits[::-1]   ## Tener en consideracion caso 999 a 1000,usar append - se deberia usar un while
    len_digitos = len(digits)
    for i in reversed(range(len_digitos)):
        digits[i] += 1
        if digits[i] < 10:
            return digits
        else:
            digits[i] = 0 #hago cero  
    if digits[0] == 0:
        digits.insert(0,1)
    return digits       