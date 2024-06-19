#Odpalanie
wiersz poleceń, w folderze z projektem komendy:
-> pip install flask
-> pip install flask_sqlalchemy
-> python -m flask run

#Co jest zrobione:
->strona główna - rejestracja i logowanie wyskakują w panelach na środku strony
->przyciski na panelach są funkcjonalne
->użytkownik nie jest zarejestrowany - wyskakuje alert że nie istnieje takie konto
->użytkownik podaje złe hasło dla istniejącego użytkownika - wyskakuje komunikat o błędnym haśle
->po zalogowaniu użytkownik zostaje przeniesiony do podstrony /home
->/home - panel z powitaniem użytkownika, możliwość wylogowania, możliwość wyboru kwiatka

#co jest do zrobienia:
->funkcjonalność kwiatka (możliwe że jest już przypisywany do bazy użytkownika)
->stworzenie podstrony ze WSPÓLNYM dla użytkowników ogrodem, gdzie użytkownik będzie miał możliwość "posadzenia" wybranego przez siebie kwiatka
->współgranie z istnieniem innych użytkowników - widoczność kwiatów innych, zajmowanie danych pól - przypisanie ich do użytkownika i wyrzucenie z potencjalnych pól do wyboru

#moja propozycja
->ograniczenie ilości pól - stworzenie wstępnie siatki z 25 polami gdzie użytkownicy mogą wybierać swoje miejsce
->POTEM ewentualnie rozwinięcie tego dostosowując rozmiar ogrodu do ilości użytkowników - ilosc * ilość, o ile ilość<(ilość-1)^2 ?
->no trzeba by to sprawdzać jakimś dodatkowym algorytmem sprawdzając najmniejszy kwadrat liczby mniejszej od ilość
