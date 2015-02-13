#!/usr/bin/python

import sys, getopt, subprocess

def main(argv):
	inputplan = ''
	opposite=0
	try:
		opts, args = getopt.getopt(argv,"hop:",["plan="])
	except getopt.GetoptError:
		print 'sidecode.py (-o) -p "<flight plan>"'
		sys.exit(2)
	for opt, arg in opts:
		if opt=='-h':
			print 'sidecode.py (-o) -p "<flight plan>"'
			sys.exit()
		elif opt in ("-o", "--opposite"):
			opposite=1
		elif opt in ("-p", "--plan"):
			plan=arg
	print "Opposite="+str(opposite)
	print "Plan="+plan
	
	segs1=plan.split()
	
	
	#List of SIDs
	#Fields = (name, alias, version, primary, secondary)
	sids=(("CASCADE", "CASCD", "2", "RIVRR COSUG HADIS CHISM", "PEGTY KELYY WANOS TOSEH CHISM"),
		("HRMNS", "", "4", "RIVRR COSUG LEZLI HRMNS", "PEGTY KELYY WANOS TOSEH HRMNS"),
		("LAVAA", "", "6", "RIVRR COSUG OKKOR LAVAA", "PEGTY KELYY ARUPT LAVAA"),
		("MINNE", "", "4", "RIVRR COSUG BISLE MINNE", "PEGTY KELYY DUDRE MINNE"),
		("WHAMY", "", "4", "RIVRR COSUG HADIS WHAMY", "PEGTY KELYY WANOS TOSEH WHAMY"),
		("PORTLAND", "PTLD", "1", "", ""),
		("BANGR", "", "7", "RENBE RICHR TOMRE BANGR", "WUREL ATOME BREMM BANGR"),
		("HAROB", "", "4", "RENBE RICHR EMRLD HAROB", "WUREL ATOME BREMM HAROB"),
		("SUMMA", "", "7", "NEVJO SUMMA", "NEZUG SUMMA"))
	textout=""
	i=0
	decode=""
	wp=segs1[0]
	while i<2:
		if decode="":
			for sid in sids:
				if sid[0] in wp or sid[1] in wp:
					sidpath=sid[3] if opposite==0 else sid[4]
					parts=plan.partition() if i==0 else plan.partition(".")
					textout=sidpath+" "+parts[2]
					break
			segs2=plan.split(".")
			wp=segs2[0]
		i+=1
	
	print textout

	webparts=textout.split()
	first=1
	getplan=""
	for wp in webparts:
		delim="" if first==1 else ":"
		if len(wp)==3:
			pre="V.K1."
		elif len(wp)==4:
			pre="A.K1."
		elif len(wp)==5:
			pre="F.K1."
		else:
			pre=""
		if pre!="":
			getplan=getplan+delim+pre+wp
		first=0
	
	url="http://skyvector.com/?ll=41.425154827969706,-117.3603515586436&chart=301&zoom=10&plan="+getplan
	print url
	subprocess.call(['/usr/bin/chromium', 'url'])


if __name__ == "__main__":
	main(sys.argv[1:])

		
IFS=' ' read -a plan <<< "$planstring"

for i in "${plan[@]}"; do
	if [[ "$sid" -eq 0 ]]; then
		j="$i"
		k=0
		while [ "$k" -lt 2 ]; do
			if [ "$j" == 'CASCADE2' ] || [ "$j" == 'CASCD2' ]; then
				if [ "$dir" -eq 0 ]; then
					sidout="RIVRR COSUG HADIS CHISM"
				else
					sidout="PEGTY KELYY WANOS TOSEH CHISM"
				fi
				break
			elif [ "$j" == 'HRMNS4' ]; then
				if [ "$dir" -eq 0 ]; then
					sidout="RIVRR COSUG LEZLI HRMNS"
				else
					sidout="PEGTY KELYY WANOS TOSEH HRMNS"
				fi
				break
			elif [ "$j" == 'LAVAA6' ]; then
				if [ "$dir" -eq 0 ]; then
					sidout="RIVRR COSUG OKKOR LAVAA"
				else
					sidout="PEGTY KELYY ARUPT LAVAA"
				fi
				break
			elif [ "$j" == 'MINNE4' ]; then
				if [ "$dir" -eq 0 ]; then
					sidout="RIVRR COSUG BISLE MINNE"
				else
					sidout="PEGTY KELYY DUDRE MINNE"
				fi
				break
			elif [ "$j" == 'WHAMY4' ]; then
				if [ "$dir" -eq 0 ]; then
					sidout="RIVRR COSUG HADIS WHAMY"
				else
					sidout="PEGTY KELYY WANOS TOSEH WHAMY"
				fi
				break
			elif [ "$j" == 'PORTLAND1' ] || [ "$j" == 'PTLD1' ]; then
					sidout="${rv[1]}"
				else
					sidout=""
				fi
				break
			fi
			IFS='.' read -a plan2 <<< "$planstring"
			j="${plan2[0]}"
			k=$(($k+1))
		done
		sid=1
		output="$sidout"
	else
		output="$output $i"
	fi
done

echo "$output"

IFS=' ' read -a fplan <<< "$output"
first=1
getplan=""
for i in "${plan[@]}"; do
	if [ "$first" -eq 0 ]; then
		delim=":"
	else
		delim=""
	fi
	if [ "${#i}" -eq 3 ]; then
		pre="V.K1."
	elif [ "${#i}" -eq 4 ]; then
		pre="A.K1."
	elif [ "${#i}" -eq 5 ]; then
		pre="F.K1."
	else
		pre=""
	getplan="$getplan$delim$pre$i"
	first=0
done

#chromium "http://skyvector.com/?ll=41.425154827969706,-117.3603515586436&chart=301&zoom=10&plan=$getplan"


chromium http://www.google.com/

http://skyvector.com/?ll=44.85833495663246,-122.9580688441531&chart=301&zoom=4&plan=A.K1.KPDX:A.K1.KEUG

http://skyvector.com/?ll=45.33464247455257,-119.69897460566618&chart=301&zoom=8&plan=F.K1.PEGTY:F.K1.KELYY:F.K1.WANOS:F.K1.TOSEH:F.K1.WHAMY:V.K1.IMB:V.K1.BOI

http://skyvector.com/?ll=41.425154827969706,-117.3603515586436&chart=301&zoom=10&plan=F.K1.SUMMA:V.K1.LTJ:V.K1.IMB:F.K2.CORKR:F.K2.TENTS

http://skyvector.com/?ll=36.48490726073845,-84.03515624404052&chart=301&zoom=10&plan=F.K1.SUMMA:V.K1.LTJ:V.K1.IMB:F.K2.CORKR:F.K2.TENTS:G.37.456255285577775,-105.81738280791517:A.K3.KMHK:G.37.19999788774751,-89.17675780686501:F.K7.GIYEP
