import sys

def getEnmNodeCredId():
    enmNodeCredentialId = 0  # type: int
    isEnmCredential = False
    output = open('C:\\Users\\ebenyue\\Desktop\\nodecred.txt')
    lines = output.readlines()
    for line in lines:
        line = line.replace('\n', '')
        #print line
        fdn = ''
        if line.startswith('FDN'):
            fdn = line.split('NodeCredential=')
            enmNodeCredentialId = fdn[1]
        if line.startswith('certificateContent '):
            if 'http://10.81.10' in line:
                isEnmCredential = True
                break
    return enmNodeCredentialId


id = getEnmNodeCredId()
print id




