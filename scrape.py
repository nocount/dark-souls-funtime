#Testerino

#Libs
from urllib.request import urlopen as url
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from util import parse_damage_stats
import csv
import MySQLdb

#Loading the page into bs from weapon page url
page_link = 'http://darksouls.wikidot.com/weapons'
page = url(page_link)
soup = BeautifulSoup(page, 'html.parser')

#Writing to local mysql db
conn=MySQLdb.connect(host='localhost',user='root',passwd='Fr0ntranger')
cursor = conn.cursor()
cursor.execute('USE dark_souls')
#
page_content = soup.findAll('div',{'id':'page-content'})
weapon_table = page_content[0].table.tr.findAll('td')[1]
weapon_list = weapon_table.findAll('a')

print('There are ' + str(len(weapon_list)) + ' weapons in Dark Souls 1: ')

#Write weapon stats to a csv
with open('weapon_data.csv', 'w') as csv_file:

	writer = csv.writer(csv_file)
	header = ["Name", "Physical", "Magic", "Fire", "Lightning", "Total AR"]
	writer.writerow(header)

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
		types = parse_damage_stats(wep_damage.text)
		if(len(types) >= 4):
			sumAR = int(types[0]) + int(types[1]) + int(types[2]) + int(types[3])
			writer.writerow([wep.text, types[0], types[1], types[2], types[3], sumAR])
			sql = "INSERT INTO weapon_stats (name, phys, magic, fire, lightning, total, weapon_category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
			val = (wep.text, types[0], types[1], types[2], types[3], sumAR, "ITS like a sword or something")
			cursor.execute(sql, val)
			conn.commit()
		else:
			writer.writerow([wep.text])
		#print(wep_damage.text+'\n')

		#Limit at 10 weapons
		# if index == 10:
		# 	break

#print("This is a test")

#


