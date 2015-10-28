#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import sys

# Indicates if script should finish execution.
STOP_BASELINE_SCRIPT = False


class KeyEventThread(threading.Thread):
    def run(self):
        global STOP_BASELINE_SCRIPT
        while not STOP_BASELINE_SCRIPT:
            z = sys.stdin.read(1)[0]
            if z=='q': STOP_BASELINE_SCRIPT = True
