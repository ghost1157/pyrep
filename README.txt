#script converts site like "xxx.com" to another format eligible for insert to resolv.conf in linux:
#Insert list of domains to the "input.txt" in the following format:
#xxx.com
#yyy.com
#zzz.com
#run script an it will convert to:
#local-zone: "xxx.com." nodefault
#local-data: "xxx.com. A 127.0.0.1"
#...
#and return to the file "output.txt" (creates, if it's not exist).
#
#
