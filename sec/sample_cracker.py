#http://www.stealthcopter.com/blog/2010/06/cracking-real-world-salted-md5-passwords-in-python-with-several-dictionaries/
# -*- coding: utf-8 -*-
import hashlib, sys, re
from time import time, sleep
from progress_bar import printProgressBar as printbar

def tobin(c):
    cNum = ord(c)
    ret = ""
    for i in range(8):
        if (cNum >> (7-i) & 0x1):
            ret += "1"
        else :
            ret += "0"
    return ret

def read_am_dump(dump_file):
    try:
        hashlist = open(dump_file,'r')
    except IOError:
        print ('Invalid file.')
        sys.exit()
    else:
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
    try:
        open_dictionary = open(dictfile,'r')
    except IOError:
        print ('Invalid file.')
        sys.exit()
    else:
        pass
        dict_list = []
        for line in open_dictionary:
            line = line.replace('\n','')
            dict_list.append(line)
        open_dictionary.close()
        tested_ids = 0
        tested_words = 0
        cracked = 0
        found_pairs = []
        tested_list = []
        #now we need to cycle through dictionary and hashes
        for i in userids:
            tested_list.append('USER ID: ' + i)
            tested_ids += 1
            printbar(tested_ids, len(userids), prefix = 'Progress', suffix = 'complete', length = 50)
            for key in dict_list:
                key = key.replace('\n','')
                tested_words += 1
                tested_list.append(key + ', ')
                m = hashlib.md5()
                #silly AM algorithm to concatenate username and passwords
				#http://cynosureprime.blogspot.co.za/2015/09/how-we-cracked-millions-of-ashley.html
                concat_str = i.lower() + '::' + key.lower()
                #print(concat_str, end = '')
				#for l in range(0, len(concat_str)):
				#	print(tobin(concat_str[l]), end = '')
                m.update(concat_str.encode('ascii'))
                #print('')
				#print (m)
                tmp_hash = m.hexdigest()
                #print (tmp_hash + '\n')
				#linear search so this is super slow now O(n^3), three nested loops
                if tmp_hash in login_tokens:
                    pos = login_tokens.index(tmp_hash)
                    found_pairs.append(userids[pos] + ',' + key)
                    cracked += 1
                    print('')
                    print("One found! {uid} , {pswd}".format(uid = userids[pos], pswd = key))
                    #break

        print ("Tested {total} combinations of userids and passwords.".format(total = tested_ids * tested_words))
        print ("{cracked} login tokens were found.".format(cracked = cracked))
        #print ('Dump of tested ids and passwords: {list}'.format(list = tested_list))
        with open('tested_pairs.txt', 'w') as tested_file_out:
            for entry in tested_list:
                tested_file_out.write(entry + ', ')
                tested_file_out.close()
        return (found_pairs)

def save_out_id_login_key(found_list):
    crackout = open("sample_cracker_out.txt","w")
    for item in found_list:
        crackout.write(item)
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
    save_out_id_login_key(finds)
    #print ("Passwords found: " + cracked + "/" + len(hashes))
	#print ("Wordlist Words :" + tested)
	#print ("Hashes computed: " + len(hashes) + tested)
	#print ("Total time taken: " + time()-tic + 's')
