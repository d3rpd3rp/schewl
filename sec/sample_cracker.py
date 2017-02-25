#http://www.stealthcopter.com/blog/2010/06/cracking-real-world-salted-md5-passwords-in-python-with-several-dictionaries/
# -*- coding: utf-8 -*-
import hashlib, sys, re
from time import time, sleep
from progress_bar import printProgressBar as printbar

def read_am_dump(dump_file):
	# Read the hash file entered
	try:
		hashlist = open(dump_file,'r')
	except IOError:
		print ('Invalid file.')
		#raw_input()
		sys.exit()
	else:
		# Read the csv values seperated by colons into an array
		hashes = []
		userids = []
		login_token = []
		for line in hashlist:
			line = line.replace('\n','')
			parsed = re.split('\'', line, 6)
			cur_hash = parsed[3]
			cur_id = parsed[1]
			cur_login_token = parsed[5]
			hashes.append(cur_hash)
			userids.append(cur_id)
			login_token.append(cur_login_token)
		hashlist.close()
	return(userids, hashes, login_token)

def read_dict(dictfile, hashes, userids, login_tokens):
	# Read wordlist in
	try:
		open_dictionary = open(dictfile,"r")
	except IOError:
		print ("Invalid file.")
		#raw_input()
		sys.exit()
	else:
		pass
		tested_ids = 0
		tested_words = 0
		cracked = 0
		found_pairs = []
		#now we need to cycle through dictionary and hashes
		print('Running dictionary cracker...')
		for i in range(0, len(userids)):
			tested_ids += 1
			printbar(tested_ids, len(userids), prefix = 'Progress', suffix = 'complete', length = 50)
			for line in open_dictionary:
				line = line.replace("\n","")
				tested_words += 1
				m = hashlib.md5()
				#silly AM algorithm to concatenate username and passwords
				#http://cynosureprime.blogspot.co.za/2015/09/how-we-cracked-millions-of-ashley.html
				#print("Testing " + line + " as password.")
				concat_str = userids[i].lower() + '::' + line.lower()
				#print("The concatenated string " + concat_str)
				m.update(concat_str.encode('utf-8'))
				tmp_hash = m.hexdigest()
				#print('Comparing... \n' + tmp_hash + '\n...to hash list.')
				#linear search so this is super slow now O(n^3)
				if tmp_hash in login_tokens:
					found_pairs.append(userid[i] + ',' + line)
					cracked += 1
					print("One found!")

		print ("Tested {total} combinations of userids and passwords.".format(total = tested_ids * tested_words))
		print ("{cracked} login tokens were found.".format(cracked = cracked))
		return (found_pairs)
"""
def brute_force_mode(hashes, userids, login_tokens):
	#http://stackoverflow.com/questions/11747254/python-brute-force-algorithm
	your_list = 'abcdefghijklmnopqrstuvwxyz'
	#complete_list = []
	for current in xrange(10):
    	a = [i for i in your_list]
    	for y in xrange(current):
        	a = [x+i for i in your_list for x in a]
    	#complete_list = complete_list + a
"""

def save_out_id_login_key(found_list):
	crackout = open("sample_cracker_out.txt","w")
	crackout.write(found_list)
	crackout.close()


#adding cmdline argv for input of both hash file and dictionary
if (len(sys.argv) == 1):
	print ("No hash file given, nothing to do...")
elif (len(sys.argv) == 2):
	print ("Hash file: " + sys.argv[1])
	print ("No dictionary given rerun with dictionary...")
else:
	print ("Dictionary and hash file given, running...")
	r_ids, r_hashes, r_login_token = read_am_dump(sys.argv[1])
	print ("Read {ids} ids and {tokens} login tokens.".format(ids = len(r_ids), tokens = len(r_login_token)))
	finds = read_dict(sys.argv[2], r_hashes, r_ids, r_login_token)
	print ("Sample hash: " + r_hashes[1])
	print ("Sample UID: " + r_ids[1])
	print ("Sample login token: " + r_login_token[1])
	save_out(finds)
	#print ("Passwords found: " + cracked + "/" + len(hashes))
	#print ("Wordlist Words :" + tested)
	#print ("Hashes computed: " + len(hashes) + tested)
	#print ("Total time taken: " + time()-tic + 's')
