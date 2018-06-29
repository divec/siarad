#!/bin/sh
set -e # Exit on failure

download_if_missing() {
	url=$1
	out=$2
	if [ -e "$out" ] ; then
		echo "Found $out"
	else
		echo "Downloading $out from $url"
		curl -s "$url" -o "$out"
	fi
}

mkdir -p cha/
download_if_missing "http://bangortalk.org.uk/speakers.php?c=siarad" cha/index.html
names=$(perl -ne 'print "$1 " while s/file=(\w+)//' < cha/index.html)
echo "Found names: ($names)"
for name in $names; do
	download_if_missing "http://bangortalk.org.uk/chats/siarad/$name.cha" cha/"$name".cha
done
