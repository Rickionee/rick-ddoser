## ABOUT TOOL :

very powerful tool to DDoS attack specific targets

## AVAILABLE ON :

* Windows
* Linux
* Termux

### TESTED ON :

* Windows
* Linux
* Termux

## REQUIREMENTS :

* python 3
* pip
* git

## INSTALLATION :

* `git clone https://github.com/Rickionee/rick-ddoser`
* `cd rick-ddoser`
* `pip install requirements.txt`

## USAGE :
you have four arguments:
* `-u` set user agents [***not required, default: user_agents.txt***]
* `-t` set target URL [***required***]
* `-tr` set number of threads [***not required, default: 1000***]
* `-s` set breakpoint after number of threads processed [***not required, default: 200***]

Example:
- `python DDoS.py -u user_agents.txt -t https://www.example.com -tr 1000 -s 200`
- or
- `python DDoS.py -t https://www.example.com`
- if you want to use default settings
- use `http://xxx.xxx.xxx.xxx` if you want to attack an IP addres

## WARNING :
***This tool is only for educational purpose. If you use this tool for other purposes except education i will not be responsible in such cases.***
