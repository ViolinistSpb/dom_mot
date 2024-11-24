from .forms import OrderForm

LINKS = {
    'Baerenreiter': 'https://www.baerenreiter.com/',
    'Grahl': 'https://www.grahl-haendlershop.de/',
    'Petz': 'https://www.petzkolophonium.com/shop/'
}

FORMS = {'Grahl': OrderForm(company_name='Grahl', number=123),
         'Baerenreiter': OrderForm(company_name='Baer', number=456),
         'Petz': OrderForm(company_name='Petz', number=789)}

