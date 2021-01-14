"""
<PYATS_JOBFILE>
"""
import pyats.easypy


def main(runtime):
    pyats.easypy.run(testscript='main.py', runtime=runtime)
