#!/usr/bin/env python
import yaml
import sqlite3
import sys

def yaml_load(filename):
	'''
	load device information for connection
	'''
	fh = open(filename, "r")
	yamlrawtext = fh.read()
	yamldata = yaml.load(yamlrawtext, Loader=yaml.FullLoader)	
	return yamldata
	
def insert_data_to_db(data):
    sql_create="CREATE TABLE IF NOT EXISTS devices ( id text PRIMARY KEY, hostname text, ipaddr text, port text, username text, password text,type text,version text);"	
    sql_add="INSERT OR REPLACE into devices (id, hostname, ipaddr, port, username, password, type, version) VALUES (?,?,?,?,?,?,?,?);"    
    with sqlite3.connect('devices.db') as conn:
        c=conn.cursor()
        try:
            c.execute(sql_create)
        except:
            sys.exit("couldn't create database")
        try:
            c.executemany(sql_add, data)
        except:
            sys.exit("Error adding data to db")
        return(c)
    return()
	
if __name__ == "__main__":
	print()
	device_list = {}
	device_list = yaml_load("devices_list.yml")	
	data=[]
	i=0
	for device in device_list["devices"]:
		print("Device {}".format(device["hostname"]))
		print("	Type {}".format(device["type"]))
		print("	Admin IP Address {}".format(device["ipaddr"]))
		#do something here
		print('                     DO SOMETHING ON THIS ITEMS')
		data.append((i, device["hostname"], device["ipaddr"],device["port"],device["username"],device["password"],device["type"],device["version"]))
		i+=1
	cursor=insert_data_to_db(data)
	cursor.close()