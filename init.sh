#!/bin/bash

./update_coins.sh
./update_mm2.sh
./gen_conf.py
./mm2 > ./mm2.log &
sleep 5
./version.sh
tail -f ./mm2.log