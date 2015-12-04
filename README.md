##Slides:

- [Link](http://pt.slideshare.net/AugustaRaposoMarques/testes-com-bdd-behaveseleniumpython)

##Requisitos de ambiente:
- Python 3.4
- [virtualenv](https://virtualenv.readthedocs.org/en/latest/installation.html)

##Preparação do ambiente:
O chromedriver deste projeto funciona apenas em ambientes MacOS, baixe a versão correta do chromedriver para seu sistema operacional [aqui](http://chromedriver.storage.googleapis.com/index.html?path=2.20/).

Executar os seguintes comandos

`git clone https://github.com/augustaraposo/google-search-behave-selenium-.git`

`virtualenv google-search-behave-selenium-`

`cd google-search-behave-selenium-`

Mac OS:
`source bin/activate`

Windows:
`Scripts\activate`

`pip install -r requirements.txt`

Para executar a feature:

`behave`
