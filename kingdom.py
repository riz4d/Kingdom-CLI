import requests as req
from bs4 import BeautifulSoup
import time
from colorama import Fore

print(Fore.RED+"""
      
##    ## #### ##    ##  ######   
##   ##   ##  ###   ## ##    ##  
##  ##    ##  ####  ## ##        
#####     ##  ## ## ## ##   #### 
##  ##    ##  ##  #### ##    ##  
##   ##   ##  ##   ### ##    ##  
##    ## #### ##    ##  ######   

########   #######  ##     ## 
##     ## ##     ## ###   ### 
##     ## ##     ## #### #### 
##     ## ##     ## ## ### ## 
##     ## ##     ## ##     ## 
##     ## ##     ## ##     ## 
########   #######  ##     ## 

This tool helps to fetch/learn
about a country.

             @riz4d/Kingdom-CLI
 
      """)

print(Fore.GREEN)
base_url='https://kingdomapi.riz4d.tk/?query='
input_country=input('Enter a Country : ')
query_url=base_url+input_country
quotes = ["'", '"']
status =''
query_result=''
url_request=req.get(query_url)
url_status=url_request.status_code
if str(url_status)=='200':
  status='true'
  query_result=url_request.json()
else:
  status='false'

def provinces():

   prov_result=query_result['provinces']
   province = ""
   for character in prov_result:
      if character not in quotes:
         province += ' - '+character+'\n'
   print('\nProvinces \n----------\n\n'+province)

def languages():
    
    lang_reult=query_result['languages']
    language=""
    for character in lang_reult:
      if character not in quotes:
        language += ' - '+character+'\n'
    print('Languages \n-----------\n\n'+language)

def poppulation():
    pop_result=query_result['population']
    print('Population \n------------\n\n - '+str(pop_result))
    
def region():
    reg_res=query_result['region']
    reg=""
    for character in reg_res:
      if character not in quotes:
        reg +=character+'\n'
    print('\nRegion \n---------\n\n - '+reg_res)
 
def subregion():
    subreg_res=query_result['subregion']
    subreg=""
    for character in subreg_res:
      if character not in quotes:
        subreg +=character
    print('\nSub-Region \n----------\n - '+subreg)
    
def timezone():
    timezn_res=query_result['timezones']
    timezn=""
    for character in timezn_res:
      if character not in quotes:
        timezn += ' - '+character+'\n'
    print('\nTime zone \n----------\n\n'+timezn)
    
def countrycode():
    cc_res=query_result['callingCodes']
    cc="+"
    for character in cc_res:
      if character not in quotes:
        cc +=character
    print('\nCountry code \n-----------\n\n - '+cc)
    
def capital():
    capital_res=query_result['capital']
    capital_t=""
    for character in capital_res:
      if character not in quotes:
        capital_t += character
    print('\nCapital \n--------\n\n - '+capital_t)
    
def knownnames():
    altnames_res=query_result['altSpellings']
    alt_names=""
    for character in altnames_res:
      if character not in quotes:
        alt_names += ' - '+character+'\n'
    print('Other Names \n------------\n\n'+alt_names)
    
def borders():
  border_res=query_result['borders']
  border=""
  for character in border_res:
      if character not in quotes:
        border += ' - '+character+'\n'
  print('Borders\n---------\n\n'+border)
 
def currency():
  currency_res=query_result['currencies']
  currenci=""
  for character in currency_res:
      if character not in quotes:
        currenci += ' - '+character+'\n'
  print('\nCurrency \n---------\n\n'+currenci)
   
def nativename():
  native_res=query_result['nativeName']
  native=""
  for character in native_res:
      if character not in quotes:
        native +=character
  print('Native name \n-----------\n\n - '+native)
  
def wiki():
  
  wiki_res=query_result['wiki']
  wki=""
  for character in wiki_res:
      if character not in quotes:
        wki +=character
  print('Refrerance \n-----------\n\n - '+wki +'\n')
  


if status=='true':
  
   currency()
   time.sleep(.4)
   poppulation()
   time.sleep(.4)
   countrycode()
   time.sleep(.4)
   region()
   time.sleep(.4)
   subregion()
   time.sleep(.4)
   capital()
   time.sleep(.4)
   timezone()
   time.sleep(.4)
   nativename()
   time.sleep(.4)
   provinces()
   time.sleep(.4)
   languages()
   time.sleep(.4)
   knownnames()
   time.sleep(.4)
   borders()
   time.sleep(.4)
   wiki()
else:
  print('Inavalid Country \nTry again !')
