#!/bin/bash

if [ -e 404.log ]; then
	while read err; do
		if [ "$image" = "$err" ]; then
			dup=1
			break
		if
	done <404.log
fi

wres=$?
if [ "$wres" -eq 8 ]; then
	echo "$image" >> 404.log
fi
