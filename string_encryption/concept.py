from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, GT, pair
from charm.toolbox.symcrypto import AuthenticatedCryptoAbstraction, SymmetricCryptoAbstraction
from charm.core.math.pairing import hashPair as extractor
from CPabe09 import CPabe09


group = PairingGroup("SS512")

# use random pairing to encrypt byte message
pairing = group.random(GT)
msg = b"This is a secret message that is larger than the group elements and has to be encrypted symmetrically"

# extractor can cope with multiple datatypes, actually its just a hash function
symcrypt_sender = AuthenticatedCryptoAbstraction(extractor(pairing))

# setup cp-abe
g1, g2 = group.random(G1), group.random(G2)
alpha, a = group.random(), group.random()
cpabe = CPabe09(group)
(master_secret_key, master_public_key) = cpabe.setup(g1, g2, alpha, a)

# set up the policy for abe
policy = '((ONE or THREE) and (TWO or FOUR))'

# define the attributes for abe
attr_list = ['ONE', 'TWO', 'THREE']

# get the secret key for abe
secret_key = cpabe.keygen(master_public_key, master_secret_key, attr_list)


# encryption of byte message with the pairing
msg_cipher = symcrypt_sender.encrypt(msg)

# encrypt the pairing
pairing_cipher = cpabe.encrypt(master_public_key, pairing, policy)


# send data (msg_cipher and pairing_cipher) to client


# retrieve pairing used to encrypt byte message
decrypted_pairing = cpabe.decrypt(
    master_public_key, secret_key, pairing_cipher)
# generate decoder with decrypted_pairing
symcrypt_resciever = AuthenticatedCryptoAbstraction(
    extractor(decrypted_pairing))


# decryption
recoveredMsg = symcrypt_resciever.decrypt(msg_cipher)

print(recoveredMsg)


'''
>>> cpabe = CPabe09(group)
>>> msg = group.random(GT)
>>> (master_secret_key, master_public_key) = cpabe.setup()
>>> policy = '((ONE or THREE) and (TWO or FOUR))'
>>> attr_list = ['THREE', 'ONE', 'TWO']
>>> secret_key = cpabe.keygen(master_public_key, master_secret_key, attr_list)
>>> cipher_text = cpabe.encrypt(master_public_key, msg, policy)
>>> decrypted_msg = cpabe.decrypt(master_public_key, secret_key, cipher_text)
>>> decrypted_msg == msg
'''
