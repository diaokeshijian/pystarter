class Directory(object):

    def __init__(self):
        self.FDN = FDN
        self.cert = cert


direct = Directory('12', '3333')
direct.FDN = '11'
print direct.FDN
print direct.cert

