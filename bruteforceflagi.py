# Funkcja brute-force generująca hasła
def brute_force():
    # Zakres od 00000 do 99999 (5 cyfr)
    for i in range(100000):  # Pętla do 100000
        password = f"ctflag{i:05d}"  # Formatowanie liczby na 5 cyfr
        print(f"Próba hasła: {password}")

# Uruchomienie brute-force
brute_force()
