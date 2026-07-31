<p align="center">
  <img src="Images/SilentX-Banner.jpg" alt="SilentX-Banner" width="9999">
</p>

<h1 align="center">
  🕶️ SilentX-Tools (v2)
</h1>

<p align="center">
  SilentX-Tools is a multifunction automation tool dedicated to pentesting and OSINT. The project is open source and designed to be fully configurable according to user needs. It also includes a plugin system that allows users to extend or create new features, in order to centralize multiple tools into a single unified platform.
</p>

<h2>⚠️ Disclaimer:</h2>
<p>
  This version is intended exclusively for educational and lawful use. Any malicious use is strictly prohibited and disclaimed.
</p>

<h2>📝 Description:</h2>

<ul>
  <li>⚙️ Compatible with Windows and Linux.</li>
  <li>🧠 Legal, advanced and optimized version.</li>
  <li>🔎 Tool oriented toward pentesting and OSINT.</li>
  <li>🧩 Plugin system allowing users to add or create new features.</li>
  <li>📁 Centralized configuration via JSON files.</li>
  <li>💻 Supports CLI mode and interactive interface.</li>
</ul>

<h2>📸 Preview:</h2>

<p align="center">
  <img src="Images/SilentX-Tool.jpg" alt="SilentX-Tool" width="9999">
</p>

<h2>⚙️ Installation:</h2>

<ol>
  <li>Installed the latest version of Python (3.8+):</li>
  - Windows:
  <pre><a href="https://www.python.org/downloads">Download Here</a> (The "PATH" option must be enabled during installation)</pre>
  - Linux:
  <pre>sudo apt install python3 -y</pre>

  <li>Installed the latest version of Git:</li>
  - Windows:
  <pre><a href="https://git-scm.com/install/windows">Download Here</a> (The "PATH" option must be enabled during installation)</pre>
  - Linux:
  <pre>sudo apt install git -y</pre>
  
  <li>Clone the repository:</li>
  <pre>git clone https://github.com/aryodwww/SilentX-Tool.git</pre>

  <li>Enter the project folder:</li>
  <pre>cd SilentX-Tool</pre>

  <li>Launched the setup:</li>
  - Windows:
  <pre>python setup.py</pre>
  - Linux:
  <pre>python3 setup.py</pre>

  <li>Launch the tool:</li>
  - Windows:
  <pre>python silentx.py</pre>
  - Linux:
  <pre>python3 silentx.py</pre>
</ol>

<h2>🔄 Update:</h2>

<ol>
  <li>Enter the project folder:</li>
  <pre>cd SilentX-Tool</pre>

  <li>Update launch:</li>
  <pre>git pull</pre>
</ol>

<h2>🚀 Features:</h2>

<pre>
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
</pre>

<h2>📁 Project Structure:</h2>

<pre>
SilentX-Tool/
├── silentx.py              # Main entry point
├── setup.py                # Installation script
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
├── LICENSE.txt             # MIT License
├── Config/
│   ├── Utils.py            # Core utilities
│   ├── Credits.json        # Tool credits
│   └── UserSettings.json   # User configuration
├── Data/
│   ├── UserAgents.txt      # User-Agent list
│   ├── Ports.json          # Port definitions
│   ├── DefaultPorts.json   # Default ports
│   ├── DefaultParameters.json # Default parameters
│   ├── VulnerabilityErrors.json # Error patterns
│   ├── VulnerabilityPayloads.json # Payloads
│   ├── VulnerabilitySensitivePaths.json # Sensitive paths
│   └── UsernameTrackerPlateforms.json # Platforms
├── Program/
│   ├── NSAdvancedScanner.py
│   ├── NSVulnerabilityScanner.py
│   ├── NSPortScanner.py
│   ├── NSUrlDiscoveryCrawler.py
│   ├── NSIpPinger.py
│   ├── NSHostDiscovery.py
│   ├── ODorkingQueryEngine.py
│   ├── OWalletTracker.py
│   ├── OUsernameTracker.py
│   ├── OEmailTracker.py
│   ├── OEmailLookup.py
│   ├── OIpLookup.py
│   ├── OPhoneNumerLookup.py
│   ├── OInstagramProfileLookup.py
│   ├── UFileMetadataScanner.py
│   ├── UFileMetadataDeleter.py
│   ├── UWebsiteCloner.py
│   ├── THelp.py
│   ├── TVersion.py
│   ├── TSettingsUpdate.py
│   └── Utils/
│       └── NetworkScanningUtils.py
├── Plugins/
│   └── Example.py          # Plugin template
└── Images/
    └── SilentX-Banner.png  # Banner image
</pre>

<h2>👨‍💻 Credits:</h2>

<ul>
  <li>Developed by: <b>aryodw</b></li>
  <li>GitHub: <a href="https://github.com/aryodw">github.com/aryodw</a></li>
  <li>License: <b>MIT License</b></li>
  <li>Version: <b>v2.0 Beta</b></li>
</ul>

<h2>⭐ Support:</h2>

<p>If you find this tool useful, please consider:</p>
<ul>
  <li>⭐ Starring the repository on GitHub</li>
  <li>🐛 Reporting bugs and issues</li>
  <li>💡 Suggesting new features</li>
  <li>🔗 Sharing with the security community</li>
</ul>

---

<p align="center">
  <b>Remember: Great power comes with great responsibility.</b>
  <br>
  <i>Use SilentX ethically and legally.</i>
</p>
