## Linki
* http://bit.ly/alx-kpython-formularz 
* https://github.com/piotrgradzinski/python_20201121 
* https://ludzkastrona.it/blog/grzechy-glowne-juniora
* https://github.com/
* https://slack.com
* https://pl.wikipedia.org/wiki/Metoda_gumowej_kaczuszki

## Przygotowanie środowiska
### Python
https://www.python.org/downloads/
### GIT
https://git-scm.com/download/win
### PyCharm Community Edition
https://www.jetbrains.com/pycharm/download
### Notepad++ - https://notepad-plus-plus.org/downloads/
### Sublime Text - https://www.sublimetext.com/

## O pythonie
* https://www.tiobe.com/tiobe-index/ 
* Guido van Rossum - twórca Pythona
* działa na popularnych systemach operacyjnych: Windows, Mac, Linux
* zastosowania pythona:
    * do pisania skryptów uruchamianych z poziomu konsoli
    * programy okienkowe
    * strony internetowe (framework django, flask)
    * gry
    * aplikacje mobilne
    * przetwarzanie danych
        * obliczenia
        * analiza tekstu
        * AI / Machine Learning
        * data science
    * kto używa Pythona
        * youtube
        * google
        * dropbox
        * instagram
        * spotify
        * NASA

https://en.wikipedia.org/wiki/List_of_Python_software

## Systemy kontroli wersji (VCS)
### GIT
w tym momencie najpopularniejszy
gdzie możemy przechowywać projekty oparte o GIT
* https://github.com
* https://bitbucket.org/
* i inne
### SVN
Subversion, dość rzadko wykorzystywany
### CVS
najstarsze narzędzie, coraz rzadziej wykorzystywane

# Podstawowe operacje

## Print
służy do wyświetlania czegoś na ekranie

jest to funkcja, która wygląda w taki sposób

    print(“Hello world!”)
    nazwa(argumenty)

definicja:

    f(x) = x + 1
    g(y) = y + 10

uruchomienie:

    f(5) -> 6
    f(10) -> 11

    f(g(5)) -> 16

## Nazewnictwo zmiennych
* nie używam polskich znaków
* nie używam spacji, zamiast nich używam znaku podkreślenia (`_`)
    * `pole_trapezu` - tak nazywamy zmienne w Pythonie
    * `poleTrapezu` - tak nie robimy w pythonie, ale w innych językach programowania często tak się robi

https://www.python.org/dev/peps/


## PyCharm skróty klawiszowe
Mac: https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard_mac.pdf?_ga=2.22968888.2012450160.1585349603-1711384716.1567926562

Windows: https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf?_ga=2.22968888.2012450160.1585349603-1711384716.1567926562

## Formatowanie stringów
Format specifier
https://docs.python.org/3.8/library/string.html#formatspec


## Operatory
### operatory arytmetyczne
* wynikiem ich działania jest `int` albo `float`

* `+`, `-`, `*`, `/`, `//`, `%`, `**`

### operatory działające z `str`
* `+` - konkatenacja
* `*` - powielanie napisu

### operatory porównania
* wynikiem ich działania jest `bool`, czyli `True` albo `False`

* `==`, `!=`, `<`, `>`, `<=`, `>=`

### operatory przypisania
* proste przypisanie: `=`
* przypisanie bazujące na obecnej wartości: `+=`, `-=`, `*=`, `/=`, `//=` i inne

### operatory logiczne
* koniunkcja (logiczne i) - `and`
* alternatywa (logiczne lub) - `or `
* negacja, zaprzeczenie (logiczne nie) - `not`
    * `not True` -> `False`
    * `not False` -> `True`

| A | B | A and B | A or B |
|:-:|:-:|:-------:|:------:|
| 0 | 0 |    0    |    0   |
| 0 | 1 |    0    |    1   |
| 1 | 0 |    0    |    1   |
| 1 | 1 |    1    |    1   |

## Instrukcja warunkowa `if`
```
if warunek:
    zrób jak warunek będzie prawdziwy (True)
```
```
if warunek:
    zrób jak warunek będzie prawdziwy (True)
else:
    zrób jak warunek będzie fałszywy (False)
```
```
if warunek1:
    zrób jak warunek1 będzie prawdziwy (True)
elif warunek2:
    zrób jak warunek2 będzie prawdziwy (True)
else:
    zrób jak wszystkie wcześniejsze warunki będą fałszywe (False)
```
```
if warunek1:
    zrób jak warunek1 będzie prawdziwy (True)
elif warunek2:
    zrób jak warunek2 będzie prawdziwy (True)
elif warunek3:
    zrób jak warunek3 będzie prawdziwy (True)
else:
    zrób jak wszystkie wcześniejsze warunki będą fałszywe (False)
```
```
if warunek1:
    zrób jak warunek1 będzie prawdziwy (True)
elif warunek2:
    zrób jak warunek2 będzie prawdziwy (True)
```

## Bity i bajty
* https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html 
* https://pl.wikipedia.org/wiki/Systemy_pozycyjne 
* https://pl.wikipedia.org/wiki/Dw%C3%B3jkowy_system_liczbowy 
* http://pgradzinski.students.alx.pl/~pgradzinski/kpython/system_pozycyjny.pdf

## Liczby zmiennoprzecinkowe
* https://ryanstutorials.net/binary-tutorial/binary-floating-point.php 
* https://stackoverflow.com/questions/15004944/max-value-of-integer 
* http://www.exploringbinary.com/why-0-point-1-does-not-exist-in-floating-point/

## Napisy
* https://realpython.com/python-f-strings/
* https://www.python.org/dev/peps/pep-0498/#format-specifiers 
* https://docs.python.org/3.4/library/string.html#formatspec 


## Pętla while
* sprawdzamy warunek
* jak jest prawdziwy, to wykonujemy ciało pętli
* jak jest fałszywy, to kończymy wykonywanie pętli
* najpierw sprawdzamy warunek, później wykonujemy ciało pętli

## Kolekcje
* indeksowanie: https://realpython.com/python-lists-tuples/ 

### Tupla, krotka (ang. tuple)
* definiujemy w `( )` lub `tuple( )`
* tupli po utworzeniu NIE możemy zmodyfikować, tupla jest **niemutowalna**
* to oznacza, że przy próbie użycia operatora przypisania dostaniemy błąd
* Do czego używamy tupli? Używamy do trzymania danych heterogeniczne.
* tupla jest uporządkowana, tzn. zachowuje porządek, w jakim zostały dodane elementy

### Lista (ang. list)
* definiujemy w `[ ]` lub `list( )`
* jest mutowalna, czyli możemy dodawać do niej elementy po utworzeniu, albo zmieniać istniejące elementy listy
podobnie jak tupla lista jest uporządkowana
* Do czego używamy list? Używamy do trzymania danych homogenicznych.

### Zbiór (ang. set)
* definiujemy w `{ }` lub `set( )`

### Słownik (ang. dictionary)
* definiujemy w `{ klucz: wartość }` lub `dict()`
* jest mutowalny, nieuporządkowany
* restrykcje na klucz:
    * prawie wszystkie typy danych z pythona mogą być kluczem
    * można powiedzieć, że typy niemutowalne mogą być kluczem
    * precyzyjnie, tylko te typy danych, które są hashowalne, czyli posiadają metodę `__hash__()` mogą być używane jako klucz
* wartością może być cokolwiek
* https://realpython.com/python-dicts/ 
