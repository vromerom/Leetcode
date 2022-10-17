def solution(inputArray):
   final = []
   for i in range (len(inputArray)-1):
    final.append(inputArray[i]*inputArray[i+1])

    resultado = max(final)
    return resultado

inputArray = [3, 6, -2, -5, 7, 3]



