# coding=utf-8
import enmscripting
import csv
import codecs

#enm_url = 'https://enm.hljlt.5genm.cn'
#enm_user = 'Administrator'
#enm_pass = 'TestPassw0rd'

#session = enmscripting.open(enm_url, enm_user, enm_pass)
#terminal = session.terminal()


class NrCell:
    def __init__(self, NRCellDUId, administrativeState, cellLocalId, nRTAC, operationalState, NodeId, gNBId, city):
        self.NRCellDUId = NRCellDUId
        self.administrativeState = administrativeState
        self.cellLocalId = cellLocalId
        self.nRTAC = nRTAC
        self.operationalState = operationalState
        self.NodeId = NodeId
        self.gNBId = gNBId
        self.city = city

    def toSting(self):
        print self.NRCellDUId + ', ' + self.administrativeState + ', ' + self.cellLocalId + ', ' + self.nRTAC + ', ' \
              + self.operationalState + ', ' + self.NodeId + ', ' + self.gNBId + ', ' + self.city



NrCellMap = {}
#output = terminal.execute('cmedit get * NRCellDU.(cellLocalId,nRTAC,administrativeState,operationalState) -t')
#output_lines = output.get_output()
output_lines = open('C:\\Users\\ebenyue\\Desktop\\5G_1.log')

for line in output_lines:
    if '-' in line:
        while '  ' in line:
            line = line.replace('  ', ' ').strip()
        attrs = line.split(' ')
        nrCell = NrCell(attrs[2], attrs[3], attrs[4], attrs[5], attrs[6], attrs[0], 'gNBId', 'city')
        NrCellMap[nrCell.NRCellDUId] = nrCell




#output = terminal.execute('cmedit get * GNBDUFunction.gNBId -t')
#output_lines = output.get_output()

output_lines = open('C:\\Users\\ebenyue\\Desktop\\5G_2.log')
for line in output_lines:
    if '1' in line:
        while '  ' in line:
            line = line.replace('  ', ' ').strip()
        attrs = line.split(' ')
        for key in NrCellMap:
            if attrs[0] in key:
                nrCell = NrCellMap[key]
                nrCell.gNBId = attrs[2]
                NrCellMap[key] = nrCell

for key in NrCellMap:
    nrCell = NrCellMap[key]
    if nrCell.NodeId.startswith('JM'):
        nrCell.city = '佳木斯'
    elif nrCell.NodeId.startswith('JX'):
        nrCell.city = '鸡西'
    elif nrCell.NodeId.startswith('SY'):
        nrCell.city = '双鸭山'
    elif nrCell.NodeId.startswith('QQ'):
        nrCell.city = '齐齐哈尔'
    elif nrCell.NodeId.startswith('QT'):
        nrCell.city = '七台河'
    elif nrCell.NodeId.startswith('DX'):
        nrCell.city = '大兴安岭'
    NrCellMap[key] = nrCell

csvFile = open('5g_export.csv', 'wb')
csvFile.write(codecs.BOM_UTF8)
csv_writer = csv.writer(csvFile)
csv_writer.writerow(['1', '2', '3', '4', '5', '6'])
for key in NrCellMap:
    nrCell = NrCellMap[key]
    csv_writer.writerow([nrCell.city, nrCell.NodeId, nrCell.NRCellDUId, nrCell.gNBId, nrCell.nRTAC, nrCell.operationalState])
csvFile.close()






