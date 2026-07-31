SilentX-Tool is a multifunction automation tool dedicated to pentesting and OSINT. The project is open source and designed to be fully configurable according to user needs. It also includes a plugin system that allows users to extend or create new features, in order to centralize multiple tools into a single unified platform.

⚠️ Disclaimer:
This version is intended exclusively for educational and lawful use. Any malicious use is strictly prohibited and disclaimed, in accordance with the provisions of the French Penal Code relating to attacks against automated data processing systems (Articles 323-1 to 323-7).

📝 Description:
⚙️ Compatible with Windows and Linux.
🧠 Legal, advanced and optimized version.
🔎 Tool oriented toward pentesting and OSINT.
🧩 Plugin system allowing users to add or create new features in the /Plugins folder. (If you want to create a plugin and publish it on github put the tag "#redtiger-tools" in your repository, the example script can be found in: /Plugins/Example.py)
📁 Centralized configuration via JSON files in the /Data folder.
💻 Supports CLI mode and interactive interface.

⚙️ Installation:
Installed the latest version of Python (3.14):
- Windows:
Download Here (The "PATH" option must be enabled during installation)
- Linux:
sudo apt install python3 -y
Installed the latest version of Git:
- Windows:
Download Here (The "PATH" option must be enabled during installation)
- Linux:
sudo apt install git -y
Clone the repository:
git clone https://github.com/aryodwww/SilentX-Tool.git
Enter the project folder:
cd SilentX-Tool
Launched the setup:
- Windows:
python setup.py
- Linux:
python3 setup.py
Launch the tool:
- Windows:
python silentx.py
- Linux:
python3 silentx.py
🔄 Update:
Enter the project folder:
cd SilentX-Tool
Update launch:
git pull
🚀 Features:
Tools:
  --help            / -h  : Shows all tools options.
  --version         / -v  : Displays the version and information of the tool.
  --settings-update / -su : Update the tools settings.
  * --mode          / -m  : Mode: decorated / interface
  * --status        / -s  : Status: enable / disable

Pentesting:
  --advanced-scanner      / -as  : Advanced scanning performing all scans. (website, domain, IP, server)
  * --target              / -t   : Service target: <URL> / <domain> / <IP[:port]> / <localhost[:port]>
    --output              / -o   : Creating additional JSON output.
    --http-timeout        / -HT  : Set the maximum HTTP timeout in seconds: <timeout>
    --socket-timeout      / -ST  : Set the maximum socket timeout in seconds: <timeout>
    --http-proxy          / -HP  : Set an HTTP proxy: <proxy:port>
    --socket-proxy        / -SP  : Set a socket proxy: <proxy:port>
    --useragent           / -u   : Set a user-agent: random / <useragent>
    --cookie              / -c   : Set a cookie: <cookie>
  --vulnerability-scanner / -vs  : Scan all vulnerabilities of a website.
  * --target              / -t   : Website target: <URL> / <domain> / <IP:port> / <localhost:port>
    --output              / -o   : Creating additional JSON output.
    --http-timeout        / -HT  : Set the maximum HTTP timeout in seconds: <timeout>
    --http-proxy          / -HP  : Set an HTTP proxy: <proxy:port>
    --useragent           / -u   : Set a user-agent: random / <useragent>
    --cookie              / -c   : Set a cookie: <cookie>
  --port-scanner          / -ps  : Scan the ports of an IP.
  * --target              / -t   : IP target: <IP>
  * --mode                / -m   : Scan mode: single / multiple / range / default / all
    --port                / -p   : Port(s): single: <port> / multiple: <port>,<port> / range: <port>-<port>
    --protocol-scan       / -PS  : Protocol(s): TCP / UDP / TCP,UDP
    --output              / -o   : Creating additional JSON output.
    --socket-timeout      / -ST  : Set the maximum socket timeout in seconds: <timeout>
    --socket-proxy        / -SP  : Set a socket proxy: <proxy:port>
  --url-discovery-crawler / -udc : Scan all urls of a website.
  * --target              / -t   : Website target: <URL> / <domain> / <IP:port> / <localhost:port>
  * --mode                / -m   : Scan mode: onlypage / allwebsite
    --output              / -o   : Creating additional JSON output.
    --http-timeout        / -HT  : Set the maximum HTTP timeout in seconds: <timeout>
    --http-proxy          / -HP  : Set an HTTP proxy: <proxy:port>
    --useragent           / -u   : Set a user-agent: random / <useragent>
    --cookie              / -c   : Set a cookie: <cookie>
  --ip-pinger             / -ip  : Continuously ping an IP.
  * --target              / -t   : IP target: <IP>
  * --mode                / -m   : Ping mode: ICMP / TCP
    --bytes               / -b   : Set the number of bytes for an ICMP ping: <bytes>
    --port                / -p   : Set the port for a TCP ping: <port>
    --interval            / -i   : Set the interval between each ping in seconds: <interval>
    --socket-timeout      / -ST  : Set the maximum socket timeout in seconds: <timeout>
    --socket-proxy        / -SP  : Set a socket proxy: <proxy:port>
  --host-discovery        / -hd  : Determines which hosts are online.
  * --target              / -t   : CIDR target: <IP>/<CIDR prefix>
    --port                / -p   : Set the port for a TCP ping: <port>
    --output              / -o   : Creating additional JSON output.
    --tcp-icmp-timeout    / -TIT : Set the maximum TCP/ICMP timeout in seconds: <timeout>
    --socket-proxy        / -SP  : Set a socket proxy: <proxy:port>

Osint:
  --dorking-query-engine     / -dqe : Query builder for Google, Bing and DuckDuckGo with advanced operators.
  * --engine                 / -e   : Search engine: google / bing / duckduckgo
  --wallet-tracker           / -wt  : Track a crypto wallet's transactions with APIs.
  * --address                / -a   : Wallet target address: <address>
    --output                 / -o   : Creating additional JSON output.
    --http-timeout           / -HT  : Set the maximum HTTP timeout for the API in seconds: <timeout>
    --http-proxy             / -HP  : Set an HTTP proxy for the API: <proxy:port>
    --useragent              / -u   : Set a user-agent for the API: random / <useragent>
  --username-tracker         / -ut  : Track a username across multiple platforms.
  * --target                 / -t   : The target username: <username>
    --output                 / -o   : Creating additional JSON output.
    --http-timeout           / -HT  : Set the maximum HTTP timeout in seconds: <timeout>
    --http-proxy             / -HP  : Set an HTTP proxy: <proxy:port>
    --useragent              / -u   : Set a user-agent: random / <useragent>
  --email-tracker            / -et  : track an email registered on several platforms.
  * --email                  / -e   : Email target: <email>
    --output                 / -o   : Creating additional JSON output.
    --http-timeout           / -HT  : Set the maximum HTTP timeout in seconds: <timeout>
    --http-proxy             / -HP  : Set an HTTP proxy: <proxy:port>
    --useragent              / -u   : Set a user-agent: random / <useragent>
  --email-lookup             / -el  : Retrieve public data from an email.
  * --email                  / -e   : Email target: <email>
    --output                 / -o   : Creating additional JSON output.
    --socket-timeout         / -ST  : Set the maximum socket timeout in seconds: <timeout>
    --socket-proxy           / -SP  : Set a socket proxy: <proxy:port>
  --ip-lookup                / -il  : Fetch public IP data using the "ip-api.com" API.
  * --ip                     / -i   : IP target: <IP>
    --output                 / -o   : Creating additional JSON output.
    --http-timeout           / -HT  : Set the maximum HTTP timeout for the API in seconds: <timeout>
    --http-proxy             / -HP  : Set an HTTP proxy for the API: <proxy:port>
    --useragent              / -u   : Set a user-agent for the API: random / <useragent>
  --phone-number-lookup      / -pnl : Retrieve public data from a phone number.
  * --phone                  / -p   : Phone number target: <number>
    --output                 / -o   : Creating additional JSON output.
  --instagram-profile-lookup / -ipl : Retrieve public data from an instagram username.
  * --target                 / -t   : Username target: <username>
  * --sessionid              / -s   : Your instagram id session: <sessionid>
    --output                 / -o   : Creating additional JSON output.
    --http-proxy             / -HP  : Set an HTTP proxy: <proxy:port>
    --useragent              / -u   : Set a user-agent: random / <useragent>

Utilities:
  --file-metadata-scanner / -fms : Scan all file metadata.
  * --path                / -p   : The file path: <path>
    --output              / -o   : Creating additional JSON output.
  --file-metadata-deleter / -fmd : Remove all file metadata.
  * --path                / -p   : The file path: <path>
  --website-cloner        / -wc  : Clone the entire web page.
  * --target              / -t   : Website target: <URL> / <domain> / <IP:port> / <localhost:port>
    --http-timeout        / -HT  : Set the maximum HTTP timeout in seconds: <timeout>
    --http-proxy          / -HP  : Set an HTTP proxy: <proxy:port>
    --useragent           / -u   : Set a user-agent: random / <useragent>
    --cookie              / -c   : Set a cookie: <cookie>

Notations:
  /  : Or
  [] : Optional
  <> : Value
  *  : Required
👨‍💻 Credits:
Developed by: aryodw
GitHub: github.com/aryodwww
Doxbean: https://doxbean.cc/@aryodw
License: MIT License
Version: v2.0 Beta
