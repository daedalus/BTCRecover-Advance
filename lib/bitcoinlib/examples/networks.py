# -*- coding: utf-8 -*-
#
#    BitcoinLib - Python Cryptocurrency Library
#
#    EXAMPLES - Network class
#
#    © 2017 - 2019 February - 1200 Web Development <http://1200wd.com/>
#

from bitcoinlib.networks import *

#
# Network examples
#

network = Network('bitcoin')
print("\n=== Get all WIF prefixes ===")
print(f"WIF Prefixes: {network_values_for('prefix_wif')}")

print("\n=== Get all HDkey private prefixes ===")
print(f"HDkey private prefixes: {network_values_for('prefix_wif')}")

print("\n=== Get network(s) for WIF prefix B0 ===")
print(f"WIF Prefixes: {network_by_value('prefix_wif', 'B0')}")

print("\n=== Get HD key private prefix for current network ===")
print(f"self.prefix_hdkey_private: {network.wif_prefix()}")

print("\n=== Network parameters ===")
for k in network.__dir__():
    if k[:1] != '_':
        v = eval(f'network.{k}')
        if not callable(v):
            print("%25s: %s" % (k, v))

wif = 'Zpub74CSuvLPQxWkdW7bivQAhomXZTzbE8quAakKRg1C3x7uDcCCeh7zPp1tZrtJrscihJRASZWjZQ7nPQj1SHTn8gkzAHPZL3dC' \
      'MbMQLFwMKVV'
print("\n=== Search for WIF prefix ===")
print(f"WIF: {wif}")
print(wif_prefix_search(wif))
