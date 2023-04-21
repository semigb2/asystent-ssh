Asystent SSH
Asystent SSH to narzędzie do rozwiązywania problemów z serwerem Debian, które wykorzystuje GPT-3 do generowania poleceń do wykonania na serwerze.

Wymagania
Python 3
Paramiko
OpenAI
JSON
Readline
Instalacja
Zainstaluj Python 3 na Debianie:

bash
Copy code
sudo apt update
sudo apt install python3 python3-pip
Zainstaluj wymagane pakiety:

bash
Copy code
pip3 install paramiko openai readline
Konfiguracja
Stwórz plik ustawienia.txt w katalogu, w którym znajduje się skrypt asystent.py, a następnie wprowadź odpowiednie wartości do pliku:

makefile
Copy code
api_key: TWÓJ_KLUCZ_API_OPENAI
localhost: ADRES_HOSTA_SERWERA
username: NAZWA_UŻYTKOWNIKA_SERWERA
password: HASŁO_UŻYTKOWNIKA_SERWERA
Użycie
Uruchom skrypt asystent.py:

bash
Copy code
python3 asystent.py
Wprowadź opis problemu, który napotkałeś na swoim serwerze Debian, gdy zostaniesz o to poproszony przez skrypt. Możesz też wprowadzić opis problemu z prefixem i , jeśli chcesz, aby skrypt automatycznie wykonywał wszystkie polecenia bez pytania o potwierdzenie.

Skrypt użyje GPT-3, aby wygenerować polecenia do rozwiązania problemu. Następnie wyświetli te polecenia i zapyta, czy chcesz je wykonać na serwerze.

Jeśli wyrazisz zgodę, skrypt połączy się z serwerem za pomocą SSH i wykona polecenia. Jeśli napotka komentarz (wiersz zaczynający się od cyfry i kropki), zostanie wyświetlony jako informacja. W przypadku automatycznego wykonywania poleceń, skrypt nie zadaje pytań, ale wykonuje polecenia od razu.

Po zakończeniu wykonywania poleceń, wynik będzie wyświetlony na ekranie.

Interakcje z GPT-3 są zapisywane w pliku interaction_history.json, który zawiera informacje o zapytaniach do GPT-3, odpowiedziach GPT-3 oraz wykonywanych poleceniach.

Ostrzeżenie
Pamiętaj, że skrypt wykonuje polecenia na serwerze. Upewnij się, że rozumiesz, co robią te polecenia, zanim je wykonasz. Jeśli nie jesteś pewien, co robi dane polecenie, wykonaj dodatkowe badania lub skonsultuj się z ekspertem.

Pomoc i wsparcie
Jeśli napotkasz problemy podczas korzystania z Asystenta SSH,
