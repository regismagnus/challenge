'''
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
isMAC48Address(inputString) = false.

	best solution by dni-blkv:
		return bool(re.match(('^' + '[\dA-F]{2}-' * 6)[:-1] + '$', s))
'''
def isMAC48Address(inputString):
    r=['A','B','C','D','E','F']
    if len(inputString)!=17:
        return False
    inputString=inputString.split('-')
    if len(inputString)!=6:
        return False
    for i in range(6):
        if len(inputString[i])!=2 or (not inputString[i].isnumeric() and (inputString[i][0] not in r and not inputString[i][0].isnumeric()) or (inputString[i][1] not in r and not inputString[i][1].isnumeric())):
            return False
    return True
print(isMAC48Address('00-1B-63-84-45-E6'))