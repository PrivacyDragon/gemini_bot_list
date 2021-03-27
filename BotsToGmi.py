import json, os

def main():
	os.system("curl https://codeberg.org/privacy_dragon/pages/raw/branch/main/bots.json --output \"json.txt\"")
	blup = open("json.txt")
	blupblup = blup.read()
	blup.close()
	blupblupblup = blupblup.replace("\n", "")
	fish = json.loads(blupblupblup)
	bluppingFish = []
	bluppingFish.append("#Gemini bots and proxy's\n\n")
	for item in fish:    #------------------------------------------------------------------V Let the links show as links.
		bluppingFish.append("##{0}:\nIPv6: {1}\nStatic: {2}\nType: {3}\nDescription: {4}\n{5}\n".format(item["IPv4"], item["IPv6"], item["Static"], item["Type"], item["Description"], checksite(item["Website"])))
	bluppingFish = "".join(bluppingFish)
	blah = open("main/bots.gmi", "w")
	blah.write(bluppingFish)
	blah.close()
	return bluppingFish
	
def checksite(value):
	if not re.findall("://", value):
		return "URL: undefined"
	else:
		return "=>{}".format(value)
