import subprocess
import json

command = 'php derive -g --mnemonic="federal wing spread page youth pioneer hobby island hotel flat hold math" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, error) = p.communicate()
p_status = p.wait()

print(output)