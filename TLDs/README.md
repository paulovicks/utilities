# UTILS
___
## tlds.py
Pull the current data from ICANN's list of TLDs [Raw Data](https://data.iana.org/TLD/tlds-alpha-by-domain.txt)
### Usage
```shell
tlds.py [-h] [-d] [-s  [...]] [-l]

options:
-h, --help            show this help message and exit
-d, --debug           Enable debug logging
-s, --strip           Patterns to remove from lines (can be used multiple times)
-l, --lowercase       Convert data to lowercase

$> python3 tlds.py                              # General usage, raw data from ICANN
$> python3 tlds.py --strip <pattern>            # Filters out a line matching a pattern (multiple patterns accepted)
$> python3 tlds.py --lower                      # Converts the output to lowercase
$> python3 tlds.py --debug                      # Enables debug logging (INFO is the default)
```

### Examples
```shell
$> python3 tlds.py --strip #                    # Filters out 'comment' lines
$> python3 tlds.py --strip XN--                 # Filters out punycode lines
$> python3 tlds.py --strip # XN--               # Filters out both 'comment' and punycode lines
$> python3 tlds.py --lower --strip # XN--       # Lowercase output and filters out 'comment' and punycode lines
```
