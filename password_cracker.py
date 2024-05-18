import hashlib

def crack_sha1_hash(hash, use_salts = False):
    password_dictionary_file = open('top-10000-passwords.txt',"r",encoding='utf-8');
    
    for x in password_dictionary_file:
        x = x.replace("\n","")

        if use_salts:
            known_salts_file = open('known-salts.txt',"r",encoding='utf-8');
            for salt in known_salts_file:
                salt = salt.replace("\n","")
                pre_salt_password = salt + x 
                post_salt_password = x + salt  
                wrodlist_with_presalt_hash = getHash(pre_salt_password)
                wrodlist_with_postsalt_hash = getHash(post_salt_password)
                if hash == wrodlist_with_presalt_hash or hash == wrodlist_with_postsalt_hash:
                    password_dictionary_file.close()
                    known_salts_file.close();
                    return x
            known_salts_file.close()
        else:
            wordlist_element_hash = getHash(x)
            if hash == wordlist_element_hash:
                password_dictionary_file.close()
                return x
    password_dictionary_file.close()
    return "PASSWORD NOT IN DATABASE"


def getHash(data):
    hash=""
    sha1 = hashlib.sha1() 
    sha1.update(data.encode('utf-8'))
    hash = sha1.hexdigest()
    return hash
