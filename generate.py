# Used for the burp suite authentication lab/alternatively this script generates fake internal IP'S
import random
#10.0.x.x range 254 254 and random
#xorsd forward header request etc
ipClasses = ["10","127","192","172","45","28","1","57"]
ipContent = ["10","10","198","254"] #10.10.198.254
dot = "."
f = open("ipList.txt", "a")
for ip in range(25000):
	ipContent[0] = str(random.choice(ipContent))
	ipContent[1] = str(random.randint(0,254))
	ipContent[2] = str(random.randint(0,254))
	ipContent[3] = str(random.randint(0,254))
	ipaddr = ipContent[0] + dot + ipContent[1] + dot + ipContent[2] + dot + ipContent[3] + "\n"
	#print(ipaddr)
	f.write(ipaddr)
f.close()
print("Complete")
