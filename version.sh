#!/bin/bash
source rpc
curl --url "http://${rpc_ip}:${port}" --data "{\"method\":\"version\",\"userpass\":\"$userpass\"}"
echo ""

