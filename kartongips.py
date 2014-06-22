#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# kartongips wersja 0.1
# autor Bart Grzybicki <bgrzybicki@gmail.com>
# program do obliczania materialow oraz ich kosztow
# potrzebnych do postawienia sciany dzialowej z plyt G-K

import math

__version__ = '0.1'

class Sciana(object):
    def powierzchnia(self, wymiary):
        self.wymiary = []
        self.wymiary = wymiary
        self.wymiary = self.wymiary.split(' ')
        self.dlugosc_sciany = float(self.wymiary[0])
        self.wysokosc_sciany = float(self.wymiary[1])
        self.obwod_sciany = self.dlugosc_sciany * 2 + self.wysokosc_sciany * 2
        self.powierzchnia_sciany = self.dlugosc_sciany * self.wysokosc_sciany
        self.powierzchnia_plyt = self.powierzchnia_sciany * 2
        return self.powierzchnia_sciany, self.powierzchnia_plyt

    def plyta(self, cena=17.76):
        '''Plyta G-K o wymiarach 120 x 260 cm
        '''
        #self.cena = cena
        self.ilosc_plyt = self.powierzchnia_plyt / (1.20 * 2.60)
        self.ilosc_plyt = math.ceil(self.ilosc_plyt)
        self.koszt_plyty = round(self.ilosc_plyt * cena, 2)
        return self.ilosc_plyt, self.koszt_plyty # zaokraglamy w gore do calosci

    def profil_uw(self, cena=7.99):
        '''Profil UW na sufit i na podloge
        '''
        #self.cena = cena
        self.dlugosc_uw = 2 * self.dlugosc_sciany
        self.ilosc_uw = self.dlugosc_uw / 3
        self.ilosc_uw = math.ceil(self.ilosc_uw)
        self.koszt_uw = round(self.ilosc_uw * cena, 2)
        return self.dlugosc_uw, self.ilosc_uw, self.koszt_uw

    def profil_cw(self, cena=9.30):
        '''Profil CW montowane pionowo do profili UW.
        To do nich bedziemy przykrecac plyty G-K
        '''
        self.ilosc_cw = self.dlugosc_sciany / 0.6
        self.ilosc_cw = math.ceil(self.ilosc_cw)
        self.koszt_cw = round(self.ilosc_cw * cena, 2)
        return self.ilosc_cw, self.koszt_cw

    def profil_ua(self):
        '''Profil UA - wzmacniany do oscieznicy drzwi
        to be done...
        '''
        pass

    def tasma_akustyczna(self, cena=15.57):
        '''Tasma akustryczna 30 metrow, szer. 3 cm, gr. 0,1 cm
        '''
        self.dlugosc_tasmy_aku = self.obwod_sciany
        self.ilosc_tasmy_aku = math.ceil(self.dlugosc_tasmy_aku / 30)
        self.koszt_tasmy_aku = round(self.ilosc_tasmy_aku * cena, 2)
        return self.dlugosc_tasmy_aku, self.koszt_tasmy_aku

    def tasma_antyrysowa(self, cena=6.75):
        '''Tasma antyrysowa z wlokna szklanego 20 metrow
        Naklada sie ja na polaczenia plyt G-K i zaszpachlowuje.
        '''
        self.dlugosc_tasmy_anty = self.wysokosc_sciany * (self.dlugosc_sciany / 1.2) * 2
        self.ilosc_tasmy_anty = math.ceil(self.dlugosc_tasmy_anty / 20)
        self.koszt_tasmy_anty = round(self.ilosc_tasmy_anty * cena, 2)
        return self.dlugosc_tasmy_anty, self.koszt_tasmy_anty

    def welna_mineralna(self, cena=6.35):
        '''Welna mineralna URSA FKP 39 grubosc 40 mm
        przykladowa cena za 1 m2 ze strony www.artbud.pl
        '''
        self.welna_miner = self.powierzchnia_sciany
        self.koszt_welny = round(self.welna_miner * cena, 2)
        return self.welna_miner, self.koszt_welny

    def kolki_rozporowe(self, cena=0.20):
        '''Kolki rozporowe 6x40 mm
        '''
        self.ilosc_kolkow = self.obwod_sciany / 1
        self.ilosc_kolkow = math.ceil(self.ilosc_kolkow)
        self.koszt_kolkow = round(self.ilosc_kolkow * cena, 2)
        return self.ilosc_kolkow, self.koszt_kolkow

    def wkrety_fosfatowane(self, cena=4.90):
        '''Wkrety Technox do przykrecania plyt G-K 3,5x25 mm
        mocowanie na profilu metalowym
        cena za opakowanie 200 szt. - na wage taniej :)
        '''
        self.ilosc_wkretow = 2 * (2.6/0.2) * (self.dlugosc_sciany / 0.6)
        self.ilosc_opakowan_wkr = math.ceil(self.ilosc_wkretow / 200)
        self.koszt_wkretow = round(self.ilosc_opakowan_wkr * cena, 2)
        return self.ilosc_wkretow, self.koszt_wkretow

    def masa_szpachlowa(self, cena=9.79):
        '''Masa szpachlowa
        cena: Cekol gladz szpachlowa GS 200 - 5 kg
        '''
        self.grubosc_szpachli = 2 # 2 mm
        self.powierzchnia_szpachli = 0.1 * self.wysokosc_sciany * (self.dlugosc_sciany / 1.2) * 2
        self.ilosc_szpachli = 1.5 * self.grubosc_szpachli * self.powierzchnia_szpachli
        self.koszt_szpachli = math.ceil(self.ilosc_szpachli / 5) * cena
        return self.powierzchnia_szpachli, self.ilosc_szpachli, self.koszt_szpachli

    def koszt_calkowity(self):
        '''Koszt calkowity sciany G-K
        '''
        self.koszt = self.koszt_plyty + self.koszt_uw + self.koszt_cw + self.koszt_cw + self.koszt_tasmy_aku \
        + self.koszt_tasmy_anty + self.koszt_welny + self.koszt_kolkow + self.koszt_wkretow + self.koszt_szpachli
        return self.koszt

def main():
    print('kartongips ' + __version__)
    print('ceny sa zahardkowane - wzialem przecietne ceny z Internetu')
    print('do zrobienia: wprowadzanie cen przez uzytkownika')
    sc = Sciana()
    wymiary = raw_input('\nPodaj dlugosc i wysokosc sciany (w metrach oddzielone spacja): ')
    powierzchnia = sc.powierzchnia(wymiary)
    plyta_gk = sc.plyta()
    profil_uw = sc.profil_uw()
    profil_cw = sc.profil_cw()
    tasma_akustyczna = sc.tasma_akustyczna()
    tasma_antyrysowa = sc.tasma_antyrysowa()
    welna_mineralna = sc.welna_mineralna()
    kolki_rozporowe = sc.kolki_rozporowe()
    wkrety_fosfatowane = sc.wkrety_fosfatowane()
    masa_szpachlowa = sc.masa_szpachlowa()
    koszt_calkowity = sc.koszt_calkowity()
    print('powierzchnia sciany (obie strony): ' + str(powierzchnia[1]) + 'm2')
    print('ilosc plyt G-K (120 x 260 cm grubosc 12,5 mm): ' + str(plyta_gk[0]) + 'szt.')
    print('koszt plyt: ' + str(plyta_gk[1]) + ' zl')
    print('\nProfile UW 50x30x0,6 mm, dlug. 300 cm (montowane do sufitu, podlogi i scian):')
    print('dlugosc profili: ' + str(profil_uw[0]) + 'mb')
    print('ilosc profili: ' + str(profil_uw[1]) + 'szt.')
    print('koszt profili: ' + str(profil_uw[2]) + ' zl')
    print('\nProfile CW 50x50x0,6 mm, dlug. 260 cm:')
    print('ilosc profili:' + str(profil_cw[0]))
    print('koszt profili: ' + str(profil_cw[1]) + ' zl')
    print('\ndlugosc tasmy akustycznej: ' + str(tasma_akustyczna[0]) + ' mb')
    print('koszt: ' + str(tasma_akustyczna[1]) + ' zl')
    print('\ndlugosc tasmy antyrysowej: ' + str(tasma_antyrysowa[0]) + ' mb')
    print('koszt: ' + str(tasma_antyrysowa[1]) + ' zl')
    print('\nwelna mineralna 40 mm do izolacji akustycznej: ' + str(welna_mineralna[0]) + ' m2')
    print('koszt: ' + str(welna_mineralna[1]) + ' zl')
    print('\nkolki rozporowe do mocowania profili UW: ' + str(kolki_rozporowe[0]) + ' szt.')
    print('koszt: ' + str(kolki_rozporowe[1]) + ' zl')
    print('\nwkrety fosfatowane TN 3,5x25 mm (co 20 cm): ' + str(wkrety_fosfatowane[0]) + ' szt.')
    print('koszt: ' + str(wkrety_fosfatowane[1]) + ' zl')
    print('\npowierzchnia do szpachlowania: ' + str(masa_szpachlowa[0]) + ' m2')
    print('ilosc suchej masy szpachlowej: ' + str(masa_szpachlowa[1]) + ' kg')
    print('koszt: ' + str(masa_szpachlowa[2]) + ' zl')
    print('\n\nKOSZT CALKOWITY: ' + str(koszt_calkowity) + ' zl')

if __name__ == '__main__':
        main()
