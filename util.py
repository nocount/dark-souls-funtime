#Util functions for DS Scraper

def parse_damage_stats(weapon):
	types = weapon.split("/")

	if(len(types) >= 4):
		print('Physical: '+ types[0])
		print('Fire: ' + types[1])
		print('Magic: ' + types[2])
		dLightning = types[3].split()[0]
		types[3] = dLightning
		print('Lightning: ' + types[3])
	else:
		print('ALERTALERTALERT This weapon has busted formatting')

	return types