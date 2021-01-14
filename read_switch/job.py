"""
<PYATS_JOBFILE>
"""
import pyats.easypy


def main(runtime):
    pyats.easypy.run(testscript='source_interface.py', runtime=runtime)
    pyats.easypy.run(testscript='target_interface.py', runtime=runtime)
