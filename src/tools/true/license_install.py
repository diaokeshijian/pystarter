#!/usr/bin/python
import os
from time import sleep

base_log_file_path = '/eniq/home/dcuser/install_license/20191129/log/'
command_check_license = '/eniq/sw/bin/licmgr -getlicinfo'
command_check_date = 'date'
license_file_path = '/eniq/home/dcuser/install_license/20191129/'
licmgr_command_path = '/eniq/sw/bin/licmgr -install '
host_name = 'rosseniqstyn1[stats_coordinator] {dcuser} #: '
license_file_name = ['logs', 'lservrc_10.80.124.36_190918_052130_4968094306_LTE.txt', 'lservrc_10.80.124.36_190920_120611_4968088694_LTE.txt', 'lservrc_10.80.124.36_190920_121103_4968088694_WCDMA.txt', 'lservrc_10.80.124.36_190923_063839_4968094309_WCDMA.txt', 'lservrc_10.80.124.36_190923_070804_4968094309_LTE.txt', 'lservrc_10.80.124.36_190923_084232_4968096514_LTE.txt', 'lservrc_10.80.124.36_190923_104306_4968096514_WVDMA.txt', 'lservrc_10.80.124.36_190923_120530_4968096550_WCDMA.txt', 'lservrc_10.80.124.36_190923_120858_4968096550_LTE.txt', 'lservrc_10.80.124.36_190923_122942_4968097575_LTE.txt', 'lservrc_10.80.124.36_190923_123409_4968097575_WCDMA.txt', 'lservrc_10.80.124.36_190923_131245_4968098139_LTE.txt', 'lservrc_10.80.124.36_190923_131557_4968098139_WCDMA.txt', 'lservrc_10.80.124.36_190924_091655_4968097577_LTE.txt', 'lservrc_10.80.124.36_190924_092008_4968097577_WCDMA.txt', 'lservrc_10.80.124.36_190924_093435_4968098198_LTE.txt', 'lservrc_10.80.124.36_190924_093756_4968098198_WCDMA.txt', 'lservrc_10.80.124.36_190924_094447_4968098418_LTE.txt', 'lservrc_10.80.124.36_190924_094749_4968098418_WCDMA.txt', 'lservrc_10.80.124.36_190924_100800_4968088694_LTE.txt', 'lservrc_10.80.124.36_190924_100800_4968098420_LTE.txt', 'lservrc_10.80.124.36_190924_101107_4968088694_WCDMA.txt', 'lservrc_10.80.124.36_190924_101107_4968098420_WCDMA.txt', 'lservrc_10.80.124.36_190924_124144_4968094309_LTE.txt', 'lservrc_10.80.124.36_190924_124505_4968094309_WCDMA.txt', 'lservrc_10.80.124.36_190925_085532_4968096763_LTE.txt', 'lservrc_10.80.124.36_190925_085838_4968096763_WCDMA.txt', 'lservrc_10.80.124.36_190925_090457_4968096765_LTE.txt', 'lservrc_10.80.124.36_190925_090756_4968096765_WCDMA.txt', 'lservrc_10.80.124.36_190925_092014_4968096766_LTE.txt', 'lservrc_10.80.124.36_190925_092308_4968096766_WCDMA.txt', 'lservrc_10.80.124.36_190925_093312_4968097071_LTE.txt', 'lservrc_10.80.124.36_190925_093558_4968097071_WCDMA.txt', 'lservrc_10.80.124.36_190925_094143_4968097080_LTE.txt', 'lservrc_10.80.124.36_190925_094455_4968097080_WCDMA.txt', 'lservrc_10.80.124.36_190925_114622_4968098421_LTE.txt', 'lservrc_10.80.124.36_190925_115117_4968098421_WCDMA.txt', 'lservrc_10.80.124.36_190925_123958_4968096763_LTE.txt', 'lservrc_10.80.124.36_190925_124245_4968096763_GSM.txt', 'lservrc_10.80.124.36_190925_124725_4968096765_GSM.txt', 'lservrc_10.80.124.36_190925_125204_4968096766_LTE.txt', 'lservrc_10.80.124.36_190925_125519_4968096766_WCDMA.txt', 'lservrc_10.80.124.36_190925_125909_4968097071GSM.txt', 'lservrc_10.80.124.36_190925_125909_4968097071_GSM.txt', 'lservrc_10.80.124.36_190925_130334_4968097080_LTE.txt', 'lservrc_10.80.124.36_190925_130624_4968097080_WCDMA.txt', 'lservrc_10.80.124.36_190925_131139_4968097081_GSM.txt', 'lservrc_10.80.124.36_190925_131628_4968097149_LTE.txt', 'lservrc_10.80.124.36_190925_131950_4968097149_WCDMA.txt', 'lservrc_10.80.124.36_190925_132342_4968097518_LTE.txt', 'lservrc_10.80.124.36_190925_132611_4968097518_GSM.txt', 'lservrc_10.80.124.36_190925_132955_4968097520_LTE.txt', 'lservrc_10.80.124.36_190925_133214_4968097520_WCDMA.txt', 'lservrc_10.80.124.36_190925_133540_4968098197_LTE.txt', 'lservrc_10.80.124.36_190925_133805_4968098197_WCDMA.txt', 'lservrc_10.80.124.36_190926_054526_4968098196_LTE.txt', 'lservrc_10.80.124.36_190926_054820_4968098196_WCDMA.txt', 'lservrc_10.80.124.36_190926_055142_4968098419_LTE.txt', 'lservrc_10.80.124.36_190926_055419_4968098419_WCDMA.txt', 'lservrc_10.80.124.36_190926_055730_4968098760_LTE.txt', 'lservrc_10.80.124.36_190926_060028_4968098760_WCDMA.txt', 'lservrc_10.80.124.36_190926_060526_4968098849_LTE.txt', 'lservrc_10.80.124.36_190926_060747_4968098849_WCDMA.txt', 'lservrc_10.80.124.36_190926_061537_4968099171_LTE.txt', 'lservrc_10.80.124.36_190926_061844_4968099171_GSM.txt', 'lservrc_10.80.124.36_190926_062210_4968100656_LTE.txt', 'lservrc_10.80.124.36_190926_062454_4968100656_GSM.txt', 'lservrc_10.80.124.36_190926_062826_4968100691_LTE.txt', 'lservrc_10.80.124.36_190926_063107_4968100691_GSM.txt', 'lservrc_10.80.124.36_190926_063436_4968100767_LTE.txt', 'lservrc_10.80.124.36_190926_063716_4968100767_WCDMA.txt', 'lservrc_10.80.124.36_190926_064205_4968100769_LTE.txt', 'lservrc_10.80.124.36_190926_064427_4968100769_WCDMA.txt', 'lservrc_10.80.124.36_190926_064835_4968100783_LTE.txt', 'lservrc_10.80.124.36_190926_065202_4968100783_GSM.txt', 'lservrc_10.80.124.36_190926_065733_4968100804_LTE.txt', 'lservrc_10.80.124.36_190926_070030_4968100804_WCDMA.txt', 'lservrc_10.80.124.36_190926_070338_4968100806_LTE.txt', 'lservrc_10.80.124.36_190926_070612_4968100806_WCDMA.txt', 'lservrc_10.80.124.36_190926_070924_4968100816_LTE.txt', 'lservrc_10.80.124.36_190926_071153_4968100816_WCDMA.txt', 'lservrc_10.80.124.36_190926_071828_4968100835_LTE.txt', 'lservrc_10.80.124.36_190926_072101_4968100835_GSM.txt', 'lservrc_10.80.124.36_190926_072424_4968101372_LTE.txt', 'lservrc_10.80.124.36_190926_072700_4968101372_WCDMA.txt', 'lservrc_10.80.124.36_190926_073028_4968101613_LTE.txt', 'lservrc_10.80.124.36_190926_073253_4968101613_WCDMA.txt', 'lservrc_10.80.124.36_190926_085029_4968101660_LTE.txt', 'lservrc_10.80.124.36_190926_085315_4968101660_GSM.txt', 'lservrc_10.80.124.36_190926_085725_4968101663_LTE.txt', 'lservrc_10.80.124.36_190926_090019_4968101663_WCDMA.txt', 'lservrc_10.80.124.36_190926_090539_4968101759_LTE.txt', 'lservrc_10.80.124.36_190926_090847_4968101759_WCDMA.txt', 'lservrc_10.80.124.36_190926_091643_4968101943_LTE.txt', 'lservrc_10.80.124.36_190926_091927_4968101943_WCDMA.txt', 'lservrc_10.80.124.36_190926_092713_4968101944_LTE.txt', 'lservrc_10.80.124.36_190926_092938_4968101944_WCDMA.txt', 'lservrc_10.80.124.36_190926_093317_4968102765_LTE.txt', 'lservrc_10.80.124.36_190926_093615_4968102765_WCDMA.txt', 'lservrc_10.80.124.36_190926_094210_4968102781_LTE.txt', 'lservrc_10.80.124.36_190926_094456_4968102781_WCDMA.txt', 'lservrc_10.80.124.36_190926_094845_4968103454_LTE.txt', 'lservrc_10.80.124.36_190926_095130_4968103454_WCDMA.txt', 'lservrc_10.80.124.36_190926_095544_4968103775_LTE.txt', 'lservrc_10.80.124.36_190926_095820_4968103775_WCDMA.txt', 'lservrc_10.80.124.36_190926_100500_4968103776_LTE.txt', 'lservrc_10.80.124.36_190926_101013_4968103776_WCDMA.txt', 'lservrc_10.80.124.36_190926_101507_4968103777_LTE.txt', 'lservrc_10.80.124.36_190926_101802_4968103777_WCDMA.txt', 'lservrc_10.80.124.36_190926_111309_4968104083_LTE.txt', 'lservrc_10.80.124.36_190926_111933_4968104083_WCDMA.txt', 'lservrc_10.80.124.36_190926_112722_4968104128_LTE.txt', 'lservrc_10.80.124.36_190926_112948_4968104128_WCDMA.txt', 'lservrc_10.80.124.36_190926_113341_4968105795_LTE.txt', 'lservrc_10.80.124.36_190926_113614_4968105795_ECDMA.txt', 'lservrc_10.80.124.36_190926_113933_4968106307_LTE.txt', 'lservrc_10.80.124.36_190926_114212_4968106307_WCDMA.txt', 'lservrc_10.80.124.36_190926_114912_4968106337_LTE.txt', 'lservrc_10.80.124.36_190926_115131_4968106337_WCDMA.txt', 'lservrc_10.80.124.36_190927_114412_4968094307_LTE.txt', 'lservrc_10.80.124.36_190927_115058_4968094307_GSM.txt']

for license_name in license_file_name:
    # create log file:
    log_file_name = base_log_file_path + license_name
    log_file = open(log_file_name, 'a')
    # check date:
    out_put_date = os.popen('date').read()
    log_file.writelines(host_name + command_check_date)
    log_file.write('\n')
    log_file.writelines(out_put_date)
    # check license status before install a new license:
    output = os.popen(command_check_license).read()
    # write the command and output to log file:
    log_file.write(host_name + command_check_license)
    log_file.writelines(output)
    print output
    sleep(1)
    # check date:
    out_put_date = os.popen('date').read()
    log_file.writelines(host_name + command_check_date)
    log_file.write('\n')
    log_file.writelines(out_put_date)
    # install license:
    command_install_license = licmgr_command_path + license_file_path + license_name
    output = os.popen(command_install_license).read()
    print output
    # write the command and output to log file:
    log_file.write(host_name + command_install_license)
    log_file.write('\n')
    log_file.writelines(output)
    sleep(3)
    # check date:
    out_put_date = os.popen('date').read()
    log_file.writelines(host_name + command_check_date)
    log_file.write('\n')
    log_file.writelines(out_put_date)
    # check license status after install the new license:
    output = os.popen(command_check_license).read()
    print output
    # write the command and output to log file:
    log_file.write(host_name + command_check_license)
    log_file.writelines(output)
    # check date:
    out_put_date = os.popen('date').read()
    log_file.writelines(host_name + command_check_date)
    log_file.write('\n')
    log_file.writelines(out_put_date)
    log_file.write(host_name)
    log_file.close()
    sleep(1)
