#!/bin/bash
grepimages=( $(grep def file.html) )
getimages=[]
i=0
dupes=0
for image in "${grepimages[@]}"; do
	if [ ! -e image ]; then
		for queue in "${getimages[@]}"; do
			if [ "$image" = "$queue" ]; then
				break
			fi
			getimages[$i]="$image"
			let "i+=1"
		done
	else
		let "dupes+=1"
	fi
done
total="$i"
each=$(echo "100/$total" | bc -l)
i=0
prog=0
(
for image in "${getimages[@]}"; do
	let "i+=1"
	echo "# Getting image $i/$total"
	wget --quiet $image
	prog=$(echo "$i*$each" | bc -l)
	echo "$prog"
done
) |
zenity --progress --title="Getting Images" --text="Fetching images..." --percentage=0 --auto-kill

if [ "$?" = -1 ] ; then
	killall wget
	zenity --error --text="Operation canceled"
fi

echo "Got $i/$total images, skipped $dupes dupes"
