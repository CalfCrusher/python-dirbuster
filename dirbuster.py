import requests, sys

if len(sys.argv) > 2 or len(sys.argv) < 2 :
	sys.exit('Usage: %s sitename.com' % sys.argv[0])
else:
	site = sys.argv[1]
correct_write = open("open_dirs.txt", "a")
useragent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
with open("dir_list.txt", "r") as check_list:
	for line in check_list:
		site_to_test = "http://" + site + line.replace('\n', "")
		site_request = requests.get(site_to_test, headers=useragent)
		if site_request.status_code == requests.codes.ok:
			correct_write.write(site_to_test + '\n')
			print("\033[0;32m/" + line.replace('\n', "") + " -- Found!\033[0m")
		else:
			print("\033[0;31m/" + line.replace('\n', "") + " -- Not found\033[0m")
correct_write.close()
