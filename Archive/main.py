#!/usr/bin/python
import logging
from pyats import aetest
import csv

log = logging.getLogger(__name__)
port = {'source': [], 'target': []}
source_file = 'output/source.txt'
target_file = 'output/target.txt'
log_file = 'output/out.txt'


class CompareChange2(aetest.Testcase):
    @aetest.test
    def comparechange2(self):
        log.info("Opening change2 source switch file....")
        with open('files/chanegs2.csv', 'r') as details:
            switch2 = csv.DictReader(details, delimiter=",")
            s = open(source_file, 'w')
            f = open(log_file, 'w')
            f.write('\n')
            f.write('======================Change2 used switch===========================' + '\n')
            f.write("Port, VLAN, Connected MAC" + '\n')
            f.write('\n')
            log.info("Retrieving used port information....")
            for rows in switch2:
                setting = rows['Port Setting']
                status = rows['Port Status']
                if setting == 'Up' and status == 'Up' and rows['Port'].find("Gig") == -1 and rows['Port'].find("Vlan") == -1 and rows['Port'].find("Null") == -1:
                    log.info("%s" % rows['Port'])
                    port['source'].append(rows['Port'])
                    f.write(rows['Port'] + ',' + rows['VLAN Membership'] + ',' + rows['Node MAC'] + '\n')
                    s.write(rows['Port'] + ',' + rows['VLAN Membership'] + ',' + rows['Node MAC'] + '\n')
            f.close()


class CompareChange3(aetest.Testcase):
    @aetest.test
    def comparechange3(self):
        log.info("Opening change3 source switch file....")
        with open('files/chanegs3.csv', 'r') as details:
            switch2 = csv.DictReader(details, delimiter=",")
            s = open(source_file, 'a')
            f = open(log_file, 'a')
            f.write('\n')
            f.write('======================Change3 used switch===========================' + '\n')
            f.write("Port, VLAN, Connected MAC" + '\n')
            f.write('\n')
            log.info("Retrieving used port information....")
            for rows in switch2:
                setting = rows['Port Setting']
                status = rows['Port Status']
                if setting == 'Up' and status == 'Up' and rows['Port'].find("Gig") == -1 and rows['Port'].find("Vlan") == -1 and rows['Port'].find("Null") == -1:
                    log.info("%s" % rows['Port'])
                    port['source'].append(rows['Port'])
                    f.write(rows['Port'] + ',' + rows['VLAN Membership'] + ',' + rows['Node MAC'] + '\n')
                    s.write(rows['Port'] + ',' + rows['VLAN Membership'] + ',' + rows['Node MAC'] + '\n')
            f.close()


class CompareChange6(aetest.Testcase):
    @aetest.test
    def comparechange6(self):
        log.info("Opening change6 target switch file....")
        with open('files/chanegs6.csv', 'r') as details:
            switch2 = csv.DictReader(details, delimiter=",")
            t = open(target_file, 'w')
            f = open(log_file, 'a')
            log.info("Retrieving unused port information....")
            for rows in switch2:
                status = rows['Port Status']
                if status == 'Down' and rows['VLAN Membership'] != "":
                    log.info("%s" % rows['Port'])
                    t.write(rows['Port'] + ',' + rows['VLAN Membership'] + '\n')
                    port['target'].append(rows['Port'])
            log.info("Source to target switch matching......")
            length = len(port['source'])
            a = 0
            f.write('\n')
            f.write('==================source to target switch=======================' + '\n')
            while a < length:
                log.info("%s ------> %s" % (port['source'][a], port['target'][a]))
                f.write(port['source'][a] + '  ----->  ' + port['target'][a] + '\n')
                a = a + 1
            f.close()


if __name__ == '__main__':
    logging.getLogger(__name__).setLevel(logging.ERROR)
    logging.getLogger('pyats.aetest').setLevel(logging.ERROR)
    aetest.main()
