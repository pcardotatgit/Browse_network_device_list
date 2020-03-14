#!/usr/bin/env python
import yaml

def yaml_load(filename):
	'''
	load device information for connection
	'''
	fh = open(filename, "r")
	yamlrawtext = fh.read()
	yamldata = yaml.load(yamlrawtext, Loader=yaml.FullLoader)	
	return yamldata
	
if __name__ == "__main__":
	print()
	device_list = {}
	device_list = yaml_load("devices_list.yml")	
	for device in device_list["devices"]:
		print("Device {}".format(device["hostname"]))
		print("	Type {}".format(device["type"]))
		print("	Admin IP Address {}".format(device["ipaddr"]))
		#do something here
		print('                     DO SOMETHING ON THIS ITEMS')