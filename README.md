usage: python3 simplehttpsprobe.py + url

If you want to probe a list of them, in linux you can basically write: for x in $(cat urllist.txt); do python3 simplehttpsrobe.py $x; done
