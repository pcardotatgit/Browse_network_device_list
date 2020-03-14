import sys
import sqlite3
	
def read_db(database):
	liste=[]
	with sqlite3.connect(database) as conn:
		cursor=conn.cursor()
		sql_request = "SELECT * from devices"
		try:
			cursor.execute(sql_request)
			for resultat in cursor:
				#print(resultat)		
				liste.append(resultat)
		except:
			sys.exit("couldn't read database")
	return(liste)

def main():
	database="devices.db"
	devices = read_db(database)	
	if devices :
		for device in devices:
			print(device)
	else:
		print('NO RESULTS')
if __name__=='__main__':
	main()
