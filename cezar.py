def cezar(jakie, przesuniecie):
    gotowe = ""
    for znak in jakie:
        kodASCII = ord(znak)
# ord(x)pobierz wartość kodu, który odpowiada znakowi x w tablicy ASCII
        kodASCII += przesuniecie
        while kodASCII > 126:
            kodASCII -= 95
        while kodASCII < 32:
            kodASCII += 95
        gotowe += chr(kodASCII)
# chr(x) zwróć znak o kodzie równym x w tablicy ACII
    return gotowe 
k1 = "/<V5;)j}j6\\<Y)8><\\9Fbu,Hy4ONC}pxP\"4st12wn`?@O$6BgQo7i#gtD|s>3lf="
k2 = "2m{y!\"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0"
#klasyczna zasada definiowanych lewym sleszem np. \t oznacza tabulację
for p in range(-100, 101):
    print(str(p) + "" + cezar(k1, p))
    print(str(p) + "" + cezar(k2, p))