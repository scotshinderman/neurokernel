#!/usr/bin/env python

"""
Run timing test (GPU) scaled over number of ports.
"""

import numpy as np

import csv
import re
import subprocess
import sys

script_name = 'timing_demo_gpu.py'

w = csv.writer(sys.stdout)
for spikes in np.linspace(500, 15000, 20, dtype=int):
    average_step_sync_time_list = []
    average_throughput_list = []
    total_throughput_list = []
    runtime_all_list = []
    runtime_main_list = []
    runtime_loop_list = []
    for i in xrange(3):
        out = subprocess.check_output(['python', script_name,
                        '-u', '2', '-s', str(spikes), '-g', '0', '-m', '50'])
        average_step_sync_time, average_throughput, total_throughput, \
            runtime_all, runtime_main, runtime_loop = out.strip('()\n\"').split(', ')
        average_step_sync_time_list.append(float(average_step_sync_time))
        average_throughput_list.append(float(average_throughput))
        total_throughput_list.append(float(total_throughput))
        runtime_all_list.append(float(runtime_all))
        runtime_main_list.append(float(runtime_main))
        runtime_loop_list.append(float(runtime_loop))
    w.writerow([spikes,
                np.average(average_step_sync_time_list),
                np.average(average_throughput_list),
                np.average(total_throughput_list),
                np.average(runtime_all_list),
                np.average(runtime_main_list),
                np.average(runtime_loop_list)])
