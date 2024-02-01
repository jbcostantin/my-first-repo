from cryptography.fernet import Fernet

#############################################################################################
########  encrypted password management    
#############################################################################################

#The next 2 sections create a new encrypton key
#Comment out unless you want to regenerate                                           
# ###########################################################################################
# ########  generate encrypted key                                               
# ###########################################################################################
# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# print(key)
# ###########################################################################################
# ########  store encrypted key to file                                             
# ###########################################################################################
# with open(r'/Users/jeffcostantin/Documents/python/NewStuff/key.bin', 'wb') as file_object:  file_object.write(key)


###########################################################################################
########  encrypt and store password with known key                            
###########################################################################################

pw = input("Enter the password you want to encrypt: ")  

pwfile = input("Enter file name where you want encrypted code stored (no .bin at the end): ")

pwfile = pwfile + '_password.bin'

#### Retreives the encryption key from the file noted
with open(r'/Users/jeffcostantin/Documents/python/NewStuff/key.bin', 'rb') as file_object:
    for line in file_object:
        key = line

cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(bytes(pw,'utf-8'))
with open(rf'/Users/jeffcostantin/Documents/python/NewStuff/{pwfile}', 'wb') as file_object:  file_object.write(ciphered_text)

###########################################################################################
########  encrypt and store password with key stored in file                           
###########################################################################################

#with open(r'\\gsusa-fs2\data\Development\Security\key.bin', 'rb') as file_object:
#    for line in file_object:
#        key = line

#cipher_suite = Fernet(key)
#ciphered_text = cipher_suite.encrypt(b'mypassword')
#with open(r'\\gsusa-fs2\data\Development\Security\pw_test.bin', 'wb') as file_object:  file_object.write(ciphered_text)

###########################################################################################
########  read and un-encrypt and stores password and key                        
###########################################################################################

#### Retreives the encryption key from the file noted
with open(r'/Users/jeffcostantin/Documents/python/NewStuff/key.bin', 'rb') as file_object:
    for line in file_object:
        key = line

### Get Password
with open(rf'/Users/jeffcostantin/Documents/python/NewStuff/{pwfile}', 'rb') as file_object:
    for line in file_object:
        pw = line

cipher_suite = Fernet(key)
uncipher_text = (cipher_suite.decrypt(pw))
plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8") #convert to string
print(plain_text_encryptedpassword)
