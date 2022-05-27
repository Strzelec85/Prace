import pickle

dane = {
    "imie" : "Mateusz",
    "szkolenia" : { "Linux", "Python", "git" },
    "xyz" : [5,6,7,8,9],
    "test4" : range(5,10)
}

x = pickle.dump(dane, open("nauka09.dat", "wb"))
