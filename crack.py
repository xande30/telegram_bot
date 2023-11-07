from passlib.hash import nthash

passwordlist = input('Enter the passwordlist: ')
hashfile = input('Enter the hashfile: ')

hashfile = open(hashfile)
hashfile = hashfile.readlines()

print('Select Username: ')
for i in range(len(hashfile)):
    username = hashfile[i].split(':')[0]
    print('\t{} - {}'.format(i + 1, username))

index = int(input('\n' + '>>> '))
index -= 1

username = hashfile[index].split(':')[0]
hash_of_password = hashfile[index].split(':')[3]

print('Cracking for {}'.format(username))
print('HASH: {}'.format(hash_of_password))

passwordlist = open(passwordlist,encoding='latin-1')
i = 0
for password in passwordlist:
    password = password.strip('\n')
    hash = nthash.hash(password)

    if hash == hash_of_password:
        print('\n')
        print('*' * 60)
        print('Password cracked!')
        print('Password: [[{}]]'.format(password))
        break

    i += 1
    print('{} passwords tested .'.format(i), end='\r')
