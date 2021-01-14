import logging
from pyats import aetest
from pyats.topology import loader

log = logging.getLogger(__name__)
testbed = loader.load('testbed.yaml')
device1 = testbed.devices['SafalCisco4']


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
        log.info("Switch port status after migrating source port to target switch.")
        interface = open("eve_log/source_connected.txt")
        f = open("eve_log/port_status.txt", "w")
        for items in interface:
            data = device1.execute("sh mac address-table | i Fa0/1")
            f.write(data)


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
