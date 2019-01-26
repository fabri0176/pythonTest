#Dicionarios
caballero = {'vida':2,'ataque':2,'defensa':2,'alcance':2}
guerrero = {'vida':2,'ataque':2,'defensa':2,'alcance':2}
arquero = {'vida':2,'ataque':2,'defensa':2,'alcance':2}

caballero['vida'] *= guerrero['vida']*2
caballero['defensa'] *= guerrero['vida']*2

guerrero['ataque'] = caballero['ataque']*2
guerrero['alcance'] = caballero['alcance']*2

arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = guerrero['defensa']/2
arquero['alcance'] = guerrero['alcance']*2

for index,value in caballero.items():
    print('Caballero: \t'+index+' = '+ str(value))

for index,value in guerrero.items():
    print('Guerrero: \t'+index+' = '+ str(value))

for index,value in arquero.items():
    print('Arquero: \t'+index+' = '+ str(value))