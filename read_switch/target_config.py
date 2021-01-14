import logging
from pyats import aetest
from pyats.topology import loader

log = logging.getLogger(__name__)
testbed = loader.load('testbed.yaml')
device1 = testbed.devices['SafalCisco6']


# COMMON SETUP SECTION

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_devices(self):
        log.info("Connecting to  devices.....")
        device1.connect()


###################################################################
#                    TESTCASES SECTION                            #
###################################################################
class ConfigTarget(aetest.Testcase):
    @aetest.test
    def config_target(self):
        log.info("Target configuration to match source switch port...")
        f = open("eve_log/source_connected.txt", "r")
        for items in f:
            device1.configure('''
                interface ''' + items)
            device1.configure('''
                no shutdown
            ''')

            # device1.execute("interface FastEthernet0/0")
            # device1.execute("switchport access vlan 759")
            # device1.execute("switchport port-security aging time 1")
            # device1.execute("switchport port-security aging type inactivity")
            # device1.execute("switchport port-security")
            # device1.execute("no logging event link-status")
            # device1.execute("no snmp trap link-status")
            # device1.execute("storm-control broadcast level pps 100 90")
            # device1.execute("storm-control multicast level pps 100 90")
            # device1.execute("storm-control unicast level pps 90k 85k")
            # device1.execute("storm-control action trap")
            # device1.execute("no cdp enable")
            # device1.execute("spanning-tree portfast")
            # device1.execute("spanning-tree bpduguard enable")
            # device1.execute("spanning-tree guard root")
            # device1.execute("ip dhcp snooping limit rate 10")
        f.close()


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
