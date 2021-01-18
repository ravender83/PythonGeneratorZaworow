class Wejscie:
    def __init__(self, nazwa, adres, tag, komentarz):
        self.nazwa = nazwa
        self.adres = adres
        self.tag = tag
        self.komentarz = komentarz
        if tag[1:] == 'nc':
            self.nc = True
        else:
            self.nc = False

    @property
    def nazwa_cc(self):
        return chr(34) + self.nazwa + chr(34) + ";"

    @property
    def nazwa_a(self):
        return '      A  ' + self.nazwa_cc

    @property
    def nazwa_an(self):
        return '      AN ' + self.nazwa_cc

    def msg_brak_pw(self, nr, *hmi):
        if self.nc == True:
            _status = 'nieaktywny'
        else:
            _status = 'aktywny'
            
        _a = ' - '
        for i in hmi:
            if i:
                _a = '\t'
 
        _tmp = f'{str(nr)}{_a}Brak PW - {self.komentarz} {self.adres} {_status}'
        return _tmp
