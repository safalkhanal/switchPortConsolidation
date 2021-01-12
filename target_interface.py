import logging
from pyats import aetest
from pyats.topology import loader

log = logging.getLogger(__name__)
testbed = loader.load('testbed.yml')
device1 = testbed.devices['SafalCisco6']


###################################################################
#                  COMMON SETUP SECTION                           #
###################################################################
class common_setup(aetest.CommonSetup):
    @aetest.subsection
    def connectdevices(self):
        log.info("Connecting to  devices.....")
        device1.connect()


###################################################################
#                    TESTCASES SECTION                            #
###################################################################
class UsedInterface(aetest.Testcase):
    @aetest.test
    def used_interface(self):
        log.info("Retrieving unused interface information...")
        targetdevice1 = device1.execute("sh ip int br")
        unused_interface = targetdevice1.find("down")
        f = open("eve_log/target_log.txt", "w")
        f.write('\n' + "==========Target port information==========" + '\n')
        f.write(targetdevice1)
        if unused_interface == -1:
            log.info("no unused ports")
            f.write('\n' + "no unused ports" + '\n')
            num = 0
        else:
            num = targetdevice1[(unused_interface - 2)]
        log.info("number of unused ports are %s" % num)
        log.info("device summery:" + '\n' + "%s" % targetdevice1)
        f.write('\n' + "===========================================" + '\n')
        f.close()


class ConnectedPort(aetest.Testcase):
    @aetest.test
    def connected_port(self):
        # new file to store connected source port
        s = open("eve_log/target_unused.txt", "w")
        # break the file into single lines to select connected port information
        with open("eve_log/target_log.txt") as file:
            for line in file:
                line = line.rstrip()
                if "down" in line and line.find('Vlan') == -1 and line.find("Gig") == -1 and line.find("Null") == -1:
                    word = line.split(' ')[0]
                    s.write(word + '\n')
        s.close()


class MatchPort(aetest.Testcase):
    @aetest.test
    def match_port(self):
        port = {'source': [], 'target': []}
        report = open("eve_log/report.txt", "w")
        report.write("=======================Source connected/used port===================")
        report.write('\n')
        length = 0
        with open("eve_log/source_connected.txt") as s:
            for line in s:
                line = line.rstrip()
                length = length+1
                port["source"].append(line)
                report.write(line + '\n')
        report.write("===========================Target unused port=======================")
        report.write('\n')
        with open("eve_log/target_unused.txt") as t:
            for line in t:
                line = line.rstrip()
                port["target"].append(line)
                report.write(line + '\n')
        report.write("=======================Source and target matching===================")
        report.write('\n')
        a = 0
        while a < length:
            log.info("%s ------> %s" % (port['source'][a], port['target'][a]))
            report.write(port["source"][a] + '  ----->  ' + port['target'][a] + '\n')
            a = a + 1


#####################################################################
#                       COMMON CLEANUP SECTION                      #
#####################################################################
class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def clean_everything(self):
        log.info("Aetest Common Cleanup ")
        device1.disconnect()


if __name__ == '__main__':  # pragma: no cover
    logging.getLogger(__name__).setLevel(logging.ERROR)
    logging.getLogger('pyats.aetest').setLevel(logging.ERROR)
    aetest.main()
