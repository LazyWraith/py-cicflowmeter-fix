# Python CICFlowMeter

> This project is cloned from [Python Wrapper CICflowmeter](https://gitlab.com/hieulw/cicflowmeter) and customized to fit my need. Therefore, it is not maintained actively. If there are any problems, please create an issue or a pull request.  

# Changelog
### v1.0
- Fixed conversion TypeError in `utils.py`
- Fixed incorrect date_time cast that causes TypeError in `packet_time.py`
- Fixed empty sequence in min() causing errors in `flow_bytes.py`
- Fixed packet flags incorrectly showing IP layer flags instead of TCP layer flags in `flag_count.py`

# Installation
```sh
git clone https://github.com/LazyWraith/py-cicflowmeter-fix
cd py-cicflowmeter-fix
python setup.py install
```

Alternatively, install from current directory:
```sh
git clone https://github.com/LazyWraith/py-cicflowmeter-fix
cd py-cicflowmeter-fix
pip install -e ./
```

# Usage
```sh
usage: cicflowmeter [-h] (-i INPUT_INTERFACE | -f INPUT_FILE) [-c] [-u URL_MODEL] output

positional arguments:
  output                output file name (in flow mode) or directory (in sequence mode)

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_INTERFACE    capture online data from INPUT_INTERFACE
  -f INPUT_FILE         capture offline data from INPUT_FILE
  -c, --csv, --flow     output flows as csv
```

Convert pcap file to flow csv:

```
cicflowmeter -f example.pcap -c flows.csv
```

Sniff packets real-time from interface to flow csv: (**need root permission**)

```
cicflowmeter -i eth0 -c flows.csv
```

- Reference: https://www.unb.ca/cic/research/applications.html#CICFlowMeter
