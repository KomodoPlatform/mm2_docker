#!/usr/bin/env python3
import json
import string
import random
import os.path
import mnemonic

from dotenv import load_dotenv
load_dotenv()
MM2_GUI = os.getenv('MM2_GUI')
MM2_SEED = os.getenv('MM2_SEED')
MM2_USERPASS = os.getenv('MM2_USERPASS')
MM2_NETID = os.getenv('MM2_NETID')
if MM2_NETID: MM2_NETID = int(MM2_NETID)
MM2_PORT = os.getenv('MM2_PORT')
if MM2_PORT: MM2_PORT = int(MM2_PORT)
if os.getenv('MM2_RPC_LOCAL_ONLY') != "":
	MM2_RPC_LOCAL_ONLY = os.getenv('MM2_RPC_LOCAL_ONLY') == "True"
else:
	MM2_RPC_LOCAL_ONLY = True
if os.getenv('MM2_I_AM_SEED') != "":
	MM2_I_AM_SEED = os.getenv('MM2_I_AM_SEED') == "True"
else:
	MM2_I_AM_SEED = True
MM2_I_AM_SEED = os.getenv('MM2_I_AM_SEED') == "True"
MM2_SEEDNODES = os.getenv('MM2_SEEDNODES').split(" ")
MM2_RPC_IP = os.getenv('MM2_RPC_IP')

special_chars = ["@", "~", "-", "_", "|", ":", "+"]

def generate_rpc_pass(length):
	rpc_pass = ""
	quart = int(length/4)
	while len(rpc_pass) < length:
		rpc_pass += ''.join(random.sample(string.ascii_lowercase, random.randint(1,quart)))
		rpc_pass += ''.join(random.sample(string.ascii_uppercase, random.randint(1,quart)))
		rpc_pass += ''.join(random.sample(string.digits, random.randint(1,quart)))
		rpc_pass += ''.join(random.sample(special_chars, random.randint(1,quart)))
	str_list = list(rpc_pass)
	random.shuffle(str_list)
	return ''.join(str_list)

if os.path.exists("MM2.json"):
	update = False
	with open("MM2.json", "r") as f:
		conf = json.load(f)

	if MM2_NETID != conf['netid']:
		update = True
		conf.update({"netid": MM2_NETID})

	if MM2_RPC_IP != conf['rpcip']:
		update = True
		conf.update({"rpcip": MM2_RPC_IP})

	if MM2_PORT != conf['rpcport']:
		update = True
		conf.update({"rpcport": MM2_PORT})

	if MM2_RPC_LOCAL_ONLY != conf['rpc_local_only']:
		update = True
		conf.update({"rpc_local_only": MM2_RPC_LOCAL_ONLY})

	if MM2_SEEDNODES != conf['seednodes']:
		update = True
		conf.update({"seednodes": MM2_SEEDNODES})

	if MM2_I_AM_SEED != conf['i_am_seed']:
		update = True
		conf.update({"i_am_seed": MM2_I_AM_SEED})

	if MM2_GUI != conf['gui']:
		update = True
		conf.update({"gui": MM2_GUI})

	if MM2_USERPASS != conf['rpc_password']:
		update = True
		conf.update({"rpc_password": MM2_USERPASS})

	if MM2_SEED != conf['passphrase']:
		update = True
		conf.update({"passphrase": MM2_SEED})

	if update:
		with open("MM2.json", "w+") as f:
			json.dump(conf, f, indent=4)
		print("MM2.json file created.")

		with open("rpc", "w+") as f:
			f.write(f'userpass="{MM2_USERPASS}"\n')
			f.write(f'rpc_ip="{MM2_RPC_IP}"\n')
			f.write(f'port={MM2_PORT}\n')
		print("rpc file created.")

else:
	conf = {
	    "gui": "MM2_Docker",
	    "netid": 7777,
	    "i_am_seed": False,
	    "rpc_local_only": True,
	    "rpcport": 7783,
	    "rpcip": "127.0.0.1",
	    "rpc_password": "",
	    "passphrase": "",
	    "seednodes": ["80.82.76.214", "89.248.168.39", "89.248.173.231"],
	    "userhome": "/${HOME#\"/\"}",
	    "metrics": 120
	}

	if not MM2_USERPASS:
		MM2_USERPASS = generate_rpc_pass(16)

	if not MM2_SEED:
		m = mnemonic.Mnemonic('english')
		MM2_SEED = m.generate(strength=256)

	conf.update({"rpc_password": MM2_USERPASS})
	conf.update({"passphrase": MM2_SEED})
	if MM2_NETID: conf.update({"netid": MM2_NETID})
	if MM2_GUI: conf.update({"gui": MM2_GUI})
	if MM2_RPC_IP: conf.update({"rpcip": MM2_RPC_IP})
	if MM2_PORT: conf.update({"rpcport": MM2_PORT})
	conf.update({"rpc_local_only": MM2_RPC_LOCAL_ONLY})
	conf.update({"i_am_seed": MM2_I_AM_SEED})
	if MM2_SEEDNODES: conf.update({"seednodes": MM2_SEEDNODES})

	with open("MM2.json", "w+") as f:
		json.dump(conf, f, indent=4)

	print("MM2.json file created.")

	with open("rpc", "w+") as f:
		f.write(f'userpass="{MM2_USERPASS}"\n')
		f.write(f'rpc_ip="{MM2_RPC_IP}"\n')
		f.write(f'port={MM2_PORT}\n')
	print("rpc file created.")
