#Testerino

#Libs
from urllib.request import urlopen as url
from urllib.parse import urljoin
from bs4 import BeautifulSoup

#Loading the page into bs from weapon page url
page_link = 'http://darksouls.wikidot.com/weapons'
page = url(page_link)
soup = BeautifulSoup(page, 'html.parser')

#
page_content = soup.findAll('div',{'id':'page-content'})
weapon_table = page_content[0].table.tr.findAll('td')[1]
weapon_list = weapon_table.findAll('a')

print('There are ' + str(len(weapon_list)) + ' weapons in Dark Souls 1: ')

#Parsing through weapon list - enumerate because printing all of them is slow
for index, wep in enumerate(weapon_list):
	print(wep.text)

	weapon_link = urljoin('http://darksouls.wikidot.com',str(wep.get('href')))
	print(weapon_link)

	#Opening link to specific weapon page
	wep_page = url(weapon_link)
	wep_soup = BeautifulSoup(wep_page, 'html.parser')

	#Getting weapon damage table
	wep_table = wep_soup.findAll('table',{'class':'wiki-content-table'})[0]
	#Weapon Damage -- Formatting is FUCKED, wikidot eats ass
	wep_damage = wep_table.findAll('td')[2]
	print(wep_damage.text+'\n')

	#Limit at 10 weapons
	if index == 10:
		break

#print("This is a test")
