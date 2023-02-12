#!/bin/bash

IP=$(head -n 1 config.py)
IP=${IP:12:-1}
while [ "$(curl $IP:5601)" != "" ]; do sleep 10; done
sleep 10
curl -X POST "http://$IP:5601/api/index_patterns/index_pattern" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d' { "index_pattern": { "title": "classify_domains" } } ' | echo SELKS_DGA
./selks_dga.py
