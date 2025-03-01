import re

def find_strings_in_file(filename, min_length=4):
    """
    Funkcja wyszukuje ciągi tekstowe w pliku binarnym.
    
    :param filename: ścieżka do pliku, w którym będą wyszukiwane ciągi
    :param min_length: minimalna długość ciągu, który będzie wyświetlany (domyślnie 4)
    """
    try:
        with open(filename, 'rb') as f:
            # Odczytujemy plik binarnie (w trybie 'rb')
            data = f.read()
            
            # Wyszukujemy ciągi znaków o długości co najmniej min_length
            strings = re.findall(b'[ -~]{%d,}' % min_length, data)
            
            # Wypisujemy ciągi (konwertując je na tekst, czyli 'decode' z 'utf-8')
            for s in strings:
                print(s.decode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")

# Przykład użycia
find_strings_in_file('przykladowy_plik.bin')
