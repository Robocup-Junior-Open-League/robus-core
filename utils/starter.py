# TelemetryBroker Node Starter (GROUP VERSION)

import os
import sys
import subprocess
import time
import shutil
import signal

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from libs.lib_telemtrybroker import TelemetryBroker
import utils.detect_nodes as detect_nodes

print("Waiting for Redis connection:")
while True:
    try:
        print("Trying to connect to Redis... ", end="")
        mb = TelemetryBroker()
        break
    except:
        time.sleep(0.5)

mb.clearall()

files = detect_nodes.detect()
print("Start of", len(files), "nodes")

python_exec = sys.executable

# Optional: store PIDs
node_processes = []

for file in files:
    print(file)

    if os.name == 'posix':
        command = f'"{python_exec}" "{file}"'

        terminal = None
        for t in ["lxterminal", "gnome-terminal", "konsole", "x-terminal-emulator"]:
            if shutil.which(t):
                terminal = t
                break

        if terminal:
            if terminal == "gnome-terminal":
                proc = subprocess.Popen(
                    [terminal, "--", "bash", "-c", command],
                    preexec_fn=os.setsid
                )
            elif terminal == "konsole":
                proc = subprocess.Popen(
                    [terminal, "-e", "bash", "-c", command],
                    preexec_fn=os.setsid
                )
            else:
                proc = subprocess.Popen(
                    [terminal, "-e", f"bash -c '{command}'"],
                    preexec_fn=os.setsid
                )
        else:
            print("No GUI terminal found → running in background")
            proc = subprocess.Popen(
                command,
                shell=True,
                preexec_fn=os.setsid
            )

        node_processes.append(proc.pid)

    elif os.name == 'nt':
        # Windows: approximate group behavior
        command = f'"{python_exec}" "{file}"'
        proc = subprocess.Popen(
            f'start cmd /k "{command}"',
            shell=True,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
        )
        node_processes.append(proc.pid)

print("Started node PIDs:", node_processes)