Asystent SSH
Asystent SSH to narzędzie do rozwiązywania problemów z serwerem Debian, które wykorzystuje GPT-3 do generowania poleceń do wykonania na serwerze.

Wymagane pakiety
Wymagane pakiety do działania skryptu:

paramiko
openai
json
readline
Instalacja
Aby zainstalować wymagane pakiety, wykonaj poniższe polecenie:

bash
Copy code
pip install paramiko openai readline
Opis działania
Skrypt asystent.py używa GPT-3 do generowania poleceń do rozwiązania problemów z serwerem Debian. Skrypt wczytuje ustawienia z pliku ustawienia.txt, który powinien zawierać następujące informacje:

makefile
Copy code
api_key: TWÓJ_KLUCZ_API_OPENAI
localhost: ADRES_HOSTA_SERWERA
username: NAZWA_UŻYTKOWNIKA_SERWERA
password: HASŁO_UŻYTKOWNIKA_SERWERA
Zastąp TWÓJ_KLUCZ_API_OPENAI, ADRES_HOSTA_SERWERA, NAZWA_UŻYTKOWNIKA_SERWERA i HASŁO_UŻYTKOWNIKA_SERWERA odpowiednimi wartościami.

Aby uruchomić skrypt, wykonaj poniższe polecenie:

bash
Copy code
python asystent.py
Skrypt poprosi Cię o opis problemu, który napotkałeś na swoim serwerze Debian. Następnie użyje GPT-3, aby wygenerować polecenia, które można wykonać na serwerze w celu rozwiązania problemu. Skrypt wyświetli te polecenia i zapyta, czy chcesz je wykonać na serwerze. Jeśli wyrazisz zgodę, skrypt połączy się z serwerem za pomocą SSH i wykona polecenia.

Interakcje z GPT-3 są zapisywane w pliku interaction_history.json, który zawiera informacje o zapytaniach do GPT-3, odpowiedziach GPT-3 oraz wykonywanych poleceniach.

Uwagi
Pamiętaj, żeby nie udostępniać swojego klucza API OpenAI ani danych uwierzytelniających serwera w publicznych repozytoriach.
Skrypt może wykonywać polecenia na serwerze, więc używaj go z rozwagą i upewnij się, że rozumiesz, co robią te polecenia, zanim je wykonasz.
