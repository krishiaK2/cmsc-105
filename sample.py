import random
import math

#=============================================================================================================================
#MENU / PROGRAM OPENS
#=============================================================================================================================

#PROGRAM or MENU
def menu():
	print "\n---BASIC SAMPLING METHODS---\n"
	print "Menu: \n"
	print "1. Simple Random Sampling\n2. Systematic Sampling\n3. Stratified Sampling\n4. QUIT\n"

	#User input for sampling method
	global menu_response
	menu_response = raw_input("Enter the no. of your desired sampling method: ")

	#if invalid input
	if menu_response not in ("1", "2", "3", "4"):
		print "\nINVALID INPUT: Option not found!"
		menu()

#Run the program
menu()

#==============================================================================================================================
#SIMPLE RANDOM SAMPLING
#==============================================================================================================================

#Simple Random Program
def simple_random_method():
	print "\nSIMPLE RANDOM METHOD\n"

	#User input for target population size in random
	population_size_random = raw_input("Enter the size of the target population: ")
	#if invalid input for population size
	if not population_size_random.isdigit():
		print "\nINVALID INPUT: Please input an integer"
		simple_random_method()
	#valid user input for random size
	global random_pop
	if population_size_random.isdigit():
		random_pop = int(population_size_random)

	#asks the user value for n
	def take_random():

		take_random_no = raw_input("\nEnter the number of sample you wish to take from the population: ")

		#check if user input is valid
		if not take_random_no.isdigit():
			print "INVALID INPUT: Please input an integer."
			take_random()
		elif int(take_random_no) > random_pop:
			print "INVALID INPUT: Number of sample to take should not be greater than the number of population"
			take_random()
		else:
			global take_random_int
			take_random_int = int(take_random_no)

	#run take random
	take_random()

	#random sampling frame
	def random_sampling_frame():
		#user input for random sampling frame
		random_frame = raw_input("\nEnter the sampling frame with " + str(random_pop) + " populations, separated by single spaces.\nEither numbers or characters but not both:\n\n")
		
		#Valid Input! Separate every item and put it in a list
		global el_list_frame_random
		el_list_frame_random = random_frame.split()

		#if invalid input for random sampling frame
		#check if exact population size
		if len(el_list_frame_random) is not random_pop:
			print "INVALID INPUT: Did not reflect the population size inputted"
			random_sampling_frame()
		#check if all integer
		if el_list_frame_random[0].isdigit():
			for i in el_list_frame_random:
				if not i.isdigit():
					print "INVALID INPUT: mixed item type not allowed"
					random_sampling_frame()
		#check if all character
		if not el_list_frame_random[0].isdigit():
			for a in el_list_frame_random:
				if a.isdigit():
					print "INVALID INPUT: mixed item type not allowed"
					random_sampling_frame()

	#run simple ramdom frame
	random_sampling_frame()

	#print the result of the simple randon sampling
	def simple_random_result():
		random_result = []
		global take_random_int
		while take_random_int is not 0:
			pick = random.choice(el_list_frame_random)
			random_result.append(pick)
			el_list_frame_random.remove(pick)
			take_random_int -= 1
		print "\nRANDOM SAMPLE: \n"
		print random_result

	simple_random_result()

	#after sampling menu
	print "\nWhat do you want to do next?\n\n1.) Continue Random Sampling\n2.) Back to Menu"

	def end_option_menu_random():

		end_option_random = raw_input("Enter Option: ")

		if end_option_random not in ('1', "2"):
			print "INVALID INPUT: Please choose between the options given"
			end_option_menu_random()

		if end_option_random is "1":
			simple_random_method()
		if end_option_random is "2":
			menu()

	end_option_menu_random()

#======================================================================================================================
#SYSTEMATIC SAMPLING
#======================================================================================================================

#Systematic Program
def systematic_method():
	print "\nSYSTEMATIC METHOD\n"

	#User input for target population size in systematic
	population_size_systematic = raw_input("Enter the size of the target population: ")
	#if invalid input for population size
	if not population_size_systematic.isdigit():
		print "\nINVALID INPUT: Please input an integer"
		systematic_method()

	#valid user input for systematic size
	global systematic_pop
	if population_size_systematic.isdigit():
		systematic_pop = int(population_size_systematic)

	#asks the user value for n
	def take_systematic():

		take_systematic_no = raw_input("\nEnter the number of sample you wish to take from the population: ")

		#check if user input is valid
		#if n is 0 or 1
		if take_systematic_no is "0" or take_systematic_no is "1":
			print "INVALID INPUT: 1 and 0 not allowed"
			take_systematic()
		#if n is not an integer
		elif not take_systematic_no.isdigit():
			print "INVALID INPUT: Please input an integer"
			take_systematic()
		#if n is greater than N
		elif take_systematic_no.isdigit():
			if int(take_systematic_no) > systematic_pop:
				print "INVALID INPUT: sample to be taken should not be greater than the number of population"
				take_systematic()
				
		global take_systematic_int
		take_systematic_int = int(take_systematic_no)

	#run take systematic
	take_systematic()

	#Solve for K
	k = math.ceil(systematic_pop / (take_systematic_int + 0.0))

	#systematic sampling frame
	def systematic_sampling_frame():
		#user input for systematic sampling frame
		systematic_frame = raw_input("\nEnter the sampling frame with " + str(systematic_pop) + " populations, separated by single spaces.\nEither numbers or characters but not both:\n\n")
		
		#Valid Input! Separate every item and put it in a list
		global el_list_frame_systematic
		el_list_frame_systematic = systematic_frame.split()

		#if invalid input for systematic sampling frame
		#check if exact population size
		if len(el_list_frame_systematic) is not systematic_pop:
			print "INVALID INPUT: Did not reflect the population size inputted"
			systematic_sampling_frame()
		#check if all integer
		if el_list_frame_systematic[0].isdigit():
			for i in el_list_frame_systematic:
				if not i.isdigit():
					print "INVALID INPUT: mixed item type not allowed"
					systematic_sampling_frame()
		#check if all character
		if not el_list_frame_systematic[0].isdigit():
			for a in el_list_frame_systematic:
				if a.isdigit():
					print "INVALID INPUT: mixed item type not allowed"
					systematic_sampling_frame()

	#run systemtic frame frame
	systematic_sampling_frame()

	#print the result of the systematic sampling
	def systematic_result():

		system_result = []

		#pick random starting point
		starting_point = random.choice(range(0, int(k)))

		global take_systematic_int
		while take_systematic_int is not 0:
			pick = el_list_frame_systematic[starting_point]
			system_result.append(pick)
			starting_point += int(k)
			take_systematic_int -= 1
		print "\nRANDOM SAMPLE RESULT (Systematic Sampling):"
		print system_result

	systematic_result()

	#after sampling menu
	print "\nWhat do you want to do next?\n\n1.) Continue Systematic Random Sampling\n2.) Back to Menu"

	def end_option_menu_systematic():

		end_option_systematic = raw_input("Enter Option: ")

		if end_option_systematic not in ('1', "2"):
			print "INVALID INPUT: Please choose between the options given"
			end_option_menu_random()

		if end_option_systematic is "1":
			systematic_method()
		if end_option_systematic is "2":
			menu()

	end_option_menu_systematic()

#================================================================================================================================
#STRATIFIED SAMPLING
#================================================================================================================================

def stratified_method():
	print "\nSTRATIFIED METHOD\n"

	#User input for target population size in stratified
	population_size_stratified = raw_input("Enter the size of the target population: ")
	#if invalid input for population size
	if not population_size_stratified.isdigit():
		print "\nINVALID INPUT: Please input an integer"
		systematic_method()

	#valid user input for stratified size
	global stratified_pop
	if population_size_stratified.isdigit():
		stratified_pop = int(population_size_stratified)

	#stratified sampling frame
	def stratified_sampling_frame():
		#user input for stratified sampling frame
		stratified_frame = raw_input("\nEnter the sampling frame with " + str(stratified_pop) + " populations, separated by single spaces.\nEither numbers or characters but not both:\n\n")
		
		#Valid Input! Separate every item and put it in a list
		global el_list_frame_stratified
		el_list_frame_stratified = stratified_frame.split()

		#if invalid input for stratified sampling frame
		#check if exact population size
		if len(el_list_frame_stratified) is not stratified_pop:
			print "INVALID INPUT: Did not reflect the population size inputted"
			stratified_sampling_frame()
		#check if all integer
		if el_list_frame_stratified[0].isdigit():
			for i in el_list_frame_stratified:
				if not i.isdigit():
					print "INVALID INPUT: mixed item type not allowed"
					stratified_sampling_frame()
		#check if all character
		if not el_list_frame_stratified[0].isdigit():
			for a in el_list_frame_stratified:
				if a.isdigit():
					print "INVALID INPUT: mixed item type not allowed"
					stratified_sampling_frame()

	#run systemtic frame frame
	stratified_sampling_frame()

	#SEPARATE INPUTTED ITEMS INTO STRATA
	def separate_strata():

		#if given frame are integers
		if el_list_frame_stratified[0].isdigit():
			
			global even_strata
			even_strata = []
			global odd_strata
			odd_strata = []

			for i in el_list_frame_stratified:
				if (int(i) % 2) is 0:
					even_strata.append(i)
				else:
					odd_strata.append(i)

		#if given frame are characters
		if not el_list_frame_stratified[0].isdigit():

			global vowel_strata
			vowel_strata = []
			global consonant_strata
			consonant_strata = []

			for i in el_list_frame_stratified:
				if i[0] not in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
					vowel_strata.append(i)
				else:
					consonant_strata.append(i)

	#run to separate the inputted frame into different strata
	separate_strata()

	def stratified_result():

		#user input for percentage to take from every strata from the sampling frame
		percent_to_take = raw_input("\nEnter the percentage you wish to take from each strata of the sampling frame (input a positive number as [number]%) : ")

		#if user did'nt input an integer
		if not percent_to_take.isdigit():
			print "\nINVALID INPUT: Please input a positive number"
			stratified_result()

		#compute items to take from the inputted percentage
		global items_to_take_stratified
		items_to_take_stratified = int(stratified_pop * (int(percent_to_take) * .01))

		#result if sampling frame inputted is integer
		if el_list_frame_stratified[0].isdigit():
			even_strata_sample = []
			odd_strata_sample = []
			#global items_to_take_stratified
			while items_to_take_stratified is not 0:
				pick_even = random.choice(even_strata)
				pick_odd = random.choice(odd_strata)

				even_strata_sample.append(pick_even)
				odd_strata_sample.append(pick_odd)
				
				even_strata.remove(pick_even)
				odd_strata.remove(pick_odd)

				items_to_take_stratified -= 1

			print "\nSTRATIFIED SAMPLE: \n"
			print "Even Strata: "
			print even_strata_sample
			print "Odd Strata: "
			print odd_strata_sample

		#result if sampling frame inputted is not integer
		if not el_list_frame_stratified[0].isdigit():
			vowel_strata_sample = []
			consonant_strata_sample = []
			#global items_to_take_stratified
			while items_to_take_stratified is not 0:
				pick_vowel = random.choice(vowel_strata)
				pick_consonant = random.choice(consonant_strata)

				vowel_strata_sample.append(pick_vowel)
				consonant_strata_sample.append(pick_consonant)
				
				vowel_strata.remove(pick_vowel)
				consonant_strata.remove(pick_consonant)

				items_to_take_stratified -= 1

			print "\nSTRATIFIED SAMPLE: \n"
			print "Vowel Strata: "
			print vowel_strata_sample
			print "Consonant Strata: "
			print consonant_strata_sample

	#run the stratified result
	stratified_result()

	#after sampling menu
	print "\nWhat do you want to do next?\n\n1.) Continue Stratified Sampling\n2.) Back to Menu"

	def end_option_menu_stratified():

		end_option_stratified = raw_input("Enter Option: ")

		if end_option_stratified not in ('1', "2"):
			print "INVALID INPUT: Please choose between the options given"
			end_option_menu_stratified()

		if end_option_stratified is "1":
			stratified_method()
		if end_option_systematic is "2":
			menu()

	end_option_menu_stratified()

#=================================================================================================================================

#if user selects Random Sampling
if menu_response is "1":
	simple_random_method()

#if user selects Systematic Sampling
if menu_response is "2":
	systematic_method()

#if user selects Stratified Sampling
if menu_response is "3":
	stratified_method()

#if user wants to terminate the program
if menu_response is "4":
	raise SystemExit