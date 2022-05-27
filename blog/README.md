Polecenia django:

```
py manage.py createsuperuser
py manage.py makemigrations
py manage.py migrate
```

Ręczne tworzenie obiektów w bazie danych:

Uruchomienie shella:
```
$ py manage.py shell
```

W shellu:
```
from articles.models import Category
c = Category(name='Cokolwiek', slug='cokolwiek')
c.save()

exit()
```
