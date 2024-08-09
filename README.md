# Server without Pip3
As long as server has Python3, the CLI tool can still run
```shell
git clone https://github.com/Holius/gr8s.git
cd gr8s;
export PYTHONPATH=$(pwd)/src:${PYTHONPATH};
# important to put quotes around output, so the output is passed as a singler argument to argv
python3 -m gr8s "$(ps -aux | grep apiserver)";
# up/down keys or 'k'/'j' keys to navigate TLS certs
# enter to view cert details (up/down or 'k'/'j' to view off screen details of cert)
# 'q' key to exit any menu (to includ sub menu)
```

# Server with Pip3 
```shell
make i; # pip3 install .
python3 -m gr8s "$(ps -aux | grep apiserver)";
```