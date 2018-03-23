#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import cryptocompare
import datetime

now = datetime.datetime.now()
api_list = cryptocompare.get_coin_list(format=True)


print('*------------------------------------------------------------------------*')
print('|			RealTime Crypto-monnaie				|')
print('| 			  ', now.strftime("%d-%m-%Y %H:%M"), '			    	|')
print('|			  By Alexis Aubineau				|')
print('*------------------------------------------------------------------------* \n')

while True :
	print('*---------------------------------------------------------------------------------------------*')
	print('|	1) Liste des crypto-monnaies	2) Valeur d\'une crypto-monnaie	   3) Quitter	     |')
	print('*---------------------------------------------------------------------------------------------* \n')

	user_question = input('> ')
	if(user_question.startswith('1')):
		for list_crypto in api_list:
			print(list_crypto)

	elif(user_question.startswith('2')):
		print('Entrez la crypto-monnaie dont vous voulez connaître le cour en USD \n')
		user_value = input('> ')
		print(cryptocompare.get_price(user_value, curr='USD'))

	elif(user_question.startswith('3')):
		exit()
	else:
		print("Répondez par '1', '2' ou '3' \n")
