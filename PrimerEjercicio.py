def main():
    arreglo = ["a","b","c","d","e","f","g","h","i","j"]
    saltos = [0,1,3,6]
    espacios = 3
    for i in range(0,4):
        for j in range(espacios):
            print("",end=" ")
        for k in range(i+1):
            print(arreglo[k+saltos[i]],end=" ")
        print(" ")
        espacios=espacios-1

main()