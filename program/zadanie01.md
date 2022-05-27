# Zadanie

Napisać program, który będzie generował wskazaną liczbę plików zawierających fikcyjne dane pogodowe z różnych miast w zadanamy przedziale czasowym.

```
 C:\> py generator_raportow.py --ile 5 --od '2000-01-01' --do '2000-06-30'
```

Plik wyjściowy `pomiary-QWEADA.json` wygląda tak:
```
{
    "miasto" : "QWEADA",
    pomiary : [
        { "data" : "2000-01-01", "temp" : 3.0 },
        { "data" : "2000-01-02", "temp" : 4.0 },
        { "data" : "2000-01-03", "temp" : 4.1 },
        { "data" : "2000-01-04", "temp" : 2.0 }
    ]
}
``` 

Program musi upewnić się, że plik o danej nazwie nie istnieje, aby nie nadpisać istniejących danych.

Cały program można też wykorzystać jako moduł w innych programach.
