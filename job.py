"""
<PYATS_JOBFILE>
"""
# To run the job:
# pyats run job example_job.py
import os
import time
import pyats.easypy


# All run() must be inside a main function
def main(runtime):
    # Execute the testscript
    pyats.easypy.run(testscript='source_interface.py', runtime=runtime)
    pyats.easypy.run(testscript='target_interface.py', runtime=runtime)
