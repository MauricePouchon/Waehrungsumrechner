import urllib2
import json

waehrung = input("Aus welcher Währung möchten Sie umwandeln? ").upper()
umwand = input("In welche Währung möchten Sie umwandeln? ").upper()
betrag = input("Wie viel möchten Sie umwandeln? ") 

class Currency_convertor: 

    def __init__(self, url):
        urlrequest = urllib2.Request(url)
        responseStr = urllib2.urlopen(urlrequest)
        response = json.load(responseStr)
        self.rates = response["rates"]
    def convert(self, von_waehrung, zu_waehrung, betrag): 
        try:
            betrag = int(betrag)
            start_betrag = betrag 
            if von_waehrung != 'EUR' : 
                betrag = betrag / self.rates[von_waehrung] 
            
            betrag = round(betrag * self.rates[zu_waehrung], 2)
            print('{} {} = {} {}'.format(start_betrag, von_waehrung, betrag, zu_waehrung)) 
        except:
            print("Überprüfen Sie Ihre Eingaben und versuchen Sie es erneut. ")

if __name__ == "__main__": 
    
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', "bd6e7f994406c5031b81062282268e98")
    c = Currency_convertor(url)
    c.convert(waehrung, umwand, betrag)