import logging
from pyats import aetest
from pyats.topology import loader

log = logging.getLogger(__name__)
testbed = loader.load('testbed.yml')
device1 = testbed.devices['SafalCisco4']


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
        log.info("Retrieving connected interface information...")
        sourcedevice1 = device1.execute("sh ip int br")
        connected_interface = sourcedevice1.find("up")
        f = open("eve_log/source_log.txt", "w")
        f.write('\n' + "==========Source port information==========" + '\n')
        f.write(sourcedevice1)
        if connected_interface == -1:
            log.info("no connected ports")
            f.write('\n' + "no connected ports" + '\n')
            num = 0
        else:
            num = sourcedevice1[(connected_interface - 2)]
        log.info("number of connected ports are %s" % num)
        log.info("device summery:" + '\n' + "%s" % sourcedevice1)
        f.write('\n' + "===========================================" + '\n')
        f.close()


class ConnectedPort(aetest.Testcase):
    @aetest.test
    def connected_port(self):
        # new file to store connected source port
        s = open("eve_log/source_connected.txt", "w")
        # break the file into single lines to select connected port information
        with open("eve_log/source_log.txt") as file:
            for line in file:
                line = line.rstrip()
                if "up" in line and line.find('Vlan') == -1 and line.find("Gig") == -1 and line.find("Null") == -1:
                    word = line.split(' ')[0]
                    s.write(word + '\n')
        s.close()


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
