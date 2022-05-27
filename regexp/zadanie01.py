import re

napis = """Tralalala m.adamowski@alx.pl hihihi biuro@alx.pl
cokolwiek innego admin@gmail.com kontakt@firma.com.pl
i jakieś inne adresy:
* wojtek81@costam.pl
* blabla123@hihi-hihi.net
abc@xyz
No i to tyle
"""

wzorzec = re.compile(r'[-\w.]+@[-\w.]+')
# w findall (i innych) można podać albo string z regexpem, albo już skompilowany regexp
for x in re.findall(wzorzec, napis):
    print(f"* {x}")

# Druga część
wzorzec = re.compile(r'(([-\w.]+)@([-\w.]+))')
# w findall (i innych) można podać albo string z regexpem, albo już skompilowany regexp
for adres, skrzynka, domena in re.findall(wzorzec, napis):
    print(f"* {skrzynka} at {domena}    ({adres})")