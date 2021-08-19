# ostrichGuard

![bannerOstrichstudy](https://user-images.githubusercontent.com/56032914/130114721-cc816e20-f764-4561-8623-4c52e26026dd.png)

**A Scapy-based sniffer which logs ARP requests and attacks blacklisted IPs.**

An idea for simple network protection against naive incursions.

---
## Installation/Usage

1-  Install the Scapy library

> pip install scrapy

2-  Edit the script to insert whitelisted MAC Addresses:

> whitelist = ["insert","MAC","addresses","to","whitelist","as","such"]

3- Run it with Python.

> The PoD attack needs to be uncommented before it is used. Otherwise it will just work as a sniffer/logger

---
## Suggestions/Doubts

If you have any doubts/suggestions, please open an issue in this repository.


## License

OstrichGuardian is available for free via a [MIT](https://choosealicense.com/licenses/mit/) license.
