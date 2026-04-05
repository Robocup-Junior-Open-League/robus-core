# TelemetryBroker Node Killer (GROUP VERSION)

import psutil
import os
import signal

def auto_kill_node_scripts():
    own_pid = os.getpid()
    killed_groups = set()
    found = 0

    print("Searching for running node scripts (group mode)...")

    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = proc.info.get('cmdline')

            if not cmdline or len(cmdline) < 2:
                continue

            script_path = cmdline[1]
            script_name = os.path.basename(script_path)

            if "python" in proc.info['name'].lower() and script_name.startswith("node"):
                if proc.pid == own_pid:
                    continue

                try:
                    if os.name == 'posix':
                        pgid = os.getpgid(proc.pid)

                        if pgid not in killed_groups:
                            print(f"[*] Killing group {pgid} (node: {script_name})")
                            os.killpg(pgid, signal.SIGINT)
                            killed_groups.add(pgid)
                            found += 1
                    else:
                        print(f"[*] Terminating (Windows): {script_name} PID {proc.pid}")
                        proc.terminate()
                        found += 1

                except Exception as e:
                    print(f"[!] Error killing {script_name}: {e}")

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if found == 0:
        print("[i] No matching node scripts found.")
    else:
        print(f"[!] Stopped {found} node group(s).")

if __name__ == "__main__":
    auto_kill_node_scripts()