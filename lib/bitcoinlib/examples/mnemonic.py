# -*- coding: utf-8 -*-
#
#    BitcoinLib - Python Cryptocurrency Library
#
#    EXAMPLES - Mnemonic class examples
#
#    © 2017 - 2019 January - 1200 Web Development <http://1200wd.com/>
#

from bitcoinlib.mnemonic import *
from bitcoinlib.keys import HDKey
from bitcoinlib.encoding import to_hexstring

#
# Mnemonic examples
#

# Convert hexadecimal to Mnemonic and back again to hex
print("\nConvert hexadecimal to Mnemonic and back again to hex")
pk = '7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f'
words = Mnemonic().to_mnemonic(pk)
print(f"Hex                {pk}")
print(f"Checksum bin       {Mnemonic().checksum(pk)}")
print(f"Mnemonic           {words}")
print(f"Seed for HD Key    {to_hexstring(Mnemonic().to_seed(words, 'test'))}")
print(f"Back to Entropy    {to_hexstring(Mnemonic().to_entropy(words))}")

# Generate a random Mnemonic HD Key
print("\nGenerate a random Mnemonic HD Key")
entsize = 128
words = Mnemonic('english').generate(entsize)
print(f"Your Mnemonic is   {words}")
print("  (An avarage of %d tries is needed to brute-force this password)" % ((2 ** entsize) // 2))
seed = Mnemonic().to_seed(words)
hdk = HDKey.from_seed(seed)
print(f"Seed for HD Key    {to_hexstring(seed)}")
print(f"HD Key WIF is      {hdk.wif()}")
print(f"HD Key WIF is      {HDKey.from_passphrase(words).wif()} (method 2)")

# Generate a key from a Mnemonic passphrase
print("\nGenerate a key from a Mnemonic passphrase")
words = "type fossil omit food supply enlist move perfect direct grape clean diamond"
print(f"Your Mnemonic is   {words}")
seed = Mnemonic().to_seed(words)
hdk = HDKey.from_seed(seed)
print(f"Seed for HD Key    {to_hexstring(seed)}")
print(f"HD Key WIF is      {hdk.wif()}")

# Let's talk Spanish
print("\nGenerate a key from a Spanish Mnemonic passphrase")
words = "laguna afirmar talón resto peldaño deuda guerra dorado catorce avance oasis barniz"
print(f"Your Mnemonic is   {words}")
seed = Mnemonic(language='spanish').to_seed(words)
hdk = HDKey.from_seed(seed)
print(f"Seed for HD Key    {to_hexstring(seed)}")
print(f"HD Key WIF is      {hdk.wif()}")

# Want some Chinese?
print("\nGenerate a key from a Chinese Mnemonic passphrase")
words = "信 收 曉 捐 炭 祖 瘋 原 強 則 岩 蓄"
print(f"Your Mnemonic is   {words}")
seed = Mnemonic(language='chinese_traditional').to_seed(words)
hdk = HDKey.from_seed(seed)
print(f"Seed for HD Key    {to_hexstring(seed)}")
print(f"HD Key WIF is      {hdk.wif()}")

# Spanish Unicode mnemonic sentence
print("\nGenerate a key from a Spanish UNICODE Mnemonic passphrase")
words = u"guion cruz envío papel otoño percha hazaña salir joya gorra íntimo actriz"
print(f"Your Mnemonic is   {words}")
seed = Mnemonic(language='spanish').to_seed(words, '1200 web development')
hdk = HDKey.from_seed(seed)
print(f"Seed for HD Key    {to_hexstring(seed)}")
print(f"HD Key WIF is      {hdk.wif()}")

# And Japanese
print("\nGenerate a key from a Japanese UNICODE Mnemonic passphrase")
words = "あじわう　ちしき　たわむれる　おくさま　しゃそう　うんこう　ひてい　みほん　たいほ　てのひら　りこう　わかれる　かいすいよく　こもん　ねもと"
print(f"Your Mnemonic is   {words}")
seed = Mnemonic(language='japanese').to_seed(words, '1200 web development')
hdk = HDKey.from_seed(seed)
print(f"Seed for HD Key    {to_hexstring(seed)}")
print(f"HD Key WIF is      {hdk.wif()}")
