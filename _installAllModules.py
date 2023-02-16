import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Requests'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'OAuth'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Flask'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Flask-Limiter'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyyaml'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'paramiko'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'matplotlib'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'ansible'])
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sys'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'os'])