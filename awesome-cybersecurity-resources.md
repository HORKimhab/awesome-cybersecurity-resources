# Awesome Cybersecurity Resources

## Password Cracking

### Hashcat

Advanced password recovery utility focused on high-performance cracking across CPUs, GPUs, and other accelerators. Useful for password auditing, recovery workflows, and security research.

- GitHub: https://github.com/hashcat/hashcat
- Official site: https://hashcat.net/hashcat/
- Wiki: https://hashcat.net/wiki/
- Forum: https://hashcat.net/forum/
- Example docs entry point: https://github.com/hashcat/hashcat/blob/master/README.md

### John the Ripper

Popular open source password cracker used for offline password auditing and recovery. It supports wordlist attacks, incremental brute force, rules-based mutations, and many hash and file formats commonly encountered in Linux and Windows environments.

- GitHub: https://github.com/openwall/john
- Official site: https://www.openwall.com/john/
- Documentation: https://github.com/openwall/john/blob/bleeding-jumbo/doc/README.md
- Community wiki: https://openwall.info/wiki/john

### THC Hydra

Open source network login cracker for online password attacks against services such as SSH, FTP, RDP, SMB, HTTP forms, and many other protocols. It is designed for credential auditing where authentication happens over the network rather than against offline hashes.

- GitHub: https://github.com/vanhauser-thc/thc-hydra
- Official site: https://www.thc.org/thc-hydra/
- Documentation: https://github.com/vanhauser-thc/thc-hydra/blob/master/README

### Medusa

Fast, parallel, modular login brute-forcer for online authentication services. Medusa is commonly used for authorized credential auditing against protocols such as SSH, FTP, HTTP, SMB, and database services.

- GitHub: https://github.com/jmk-foofus/medusa
- Official site: https://foofus.net/goons/jmk/medusa/medusa.html

### Ncrack

High-speed network authentication cracking tool from the Nmap project, designed for online password auditing of services such as SSH, RDP, FTP, SMB, Telnet, VNC, and web logins.

- GitHub: https://github.com/nmap/ncrack
- Official site: https://nmap.org/ncrack/
- Documentation: https://nmap.org/ncrack/guide.html

### CeWL

Custom wordlist generator that crawls websites and builds password candidate lists from discovered words and metadata. It is commonly used to create targeted dictionaries before running offline or online password attacks.

- GitHub: https://github.com/digininja/CeWL
- Official site: https://digi.ninja/projects/cewl.php
- Documentation: https://github.com/digininja/CeWL/blob/main/README.md

### Crunch

Open source wordlist generator that creates custom password candidate lists from character sets, patterns, and length ranges. It is commonly used to prepare targeted dictionaries before running tools such as Hydra, John the Ripper, or Hashcat.

- GitHub mirror: https://github.com/crunchsec/crunch
- Kali tool page: https://www.kali.org/tools/crunch/

### ophcrack

Open source Windows password recovery tool best known for cracking LM and NTLM hashes with rainbow tables. It is commonly used in legacy Windows password recovery and forensic lab workflows.

- GitHub: https://github.com/ophcrack/ophcrack
- Official site: https://ophcrack.sourceforge.io/

### CUPP

Common User Passwords Profiler is an open source password profiling tool that generates targeted wordlists from personal information, keywords, and user-provided patterns. It is typically used for authorized password auditing and red team simulations.

- GitHub: https://github.com/Mebus/cupp
- Kali tool page: https://www.kali.org/tools/cupp/
- Documentation: https://github.com/Mebus/cupp/blob/master/README.md

### brutus

Fast, zero-dependency credential testing tool in Go. Brute force SSH, MySQL, PostgreSQL, Redis, MongoDB, SMB, and 20+ protocols. Hydra alternative with native nerva/naabu pipeline integration.

- GitHub: https://github.com/praetorian-inc/brutus
- Documentation: https://github.com/praetorian-inc/brutus/blob/main/README.md
- Topics: brute-force, capability, credential-testing, cybersecurity, external-network-security, golang, hacking-tools, hydra-alternative

### Major-project-list

A list of practical projects that anyone can solve in any programming language (See solutions). These projects are divided into multiple categories, and each category has its own folder. To get started, simply fork th...

- GitHub: https://github.com/ManojKumarPatnaik/Major-project-list
- Documentation: https://github.com/ManojKumarPatnaik/Major-project-list/blob/main/README.md

### haiti

:key: Hash type identifier (CLI & lib)

- GitHub: https://github.com/noraj/haiti
- Official site: https://noraj.github.io/haiti/
- Documentation: https://github.com/noraj/haiti/blob/master/README.md
- Topics: ctf, ctf-tools, cyber, cybersecurity, digest, hacking, hackthebox, hacktoberfest

### sippts

Set of tools to audit SIP based VoIP Systems

- GitHub: https://github.com/Pepelux/sippts
- Documentation: https://github.com/Pepelux/sippts/blob/master/README.md
- Topics: asterisk, elastix, freepbx, hacking, hacking-tool, password-cracker, pbx, penetration-testing

### crowbar

Brute forcing tool This package contains Crowbar (formally known as Levye). It is a brute forcing tool that can be used during penetration tests. It was developed to brute force some protocols in a different manner according to other popular brute forcing tools. As an example, while most brute forcing tools use username and password for SSH brute force, Crowbar uses SSH key(s). This allows for any private keys that have been obtained during penetration tests, to be used to attack other SSH servers. Currently Crowbar supports: * OpenVPN (-b openvpn) * Remote Desktop Protocol (RDP) with NLA support (-b rdp) * SSH private key authentication (-b sshkey) * VNC key authentication (-b vpn)

- https://github.com/galkan/crowbar
- https://gitlab.com/parrotsec/packages/crowbar

### cyberchef

Cyber Swiss Army Knife This package contains a simple, intuitive web app for carrying out all manner of "cyber" operations within a web browser. These operations include simple encoding like XOR and Base64, more complex encryption like AES, DES and Blowfish, creating binary and hexdumps, compression and decompression of data, calculating hashes and checksums, IPv6 and X.509 parsing, changing character encodings, and much more. The tool is designed to enable both technical and non-technical analysts to manipulate data in complex ways without having to deal with complex tools or algorithms. It was conceived, designed, built and incrementally improved by an analyst in their 10% innovation time over several years.

- https://github.com/gchq/CyberChef
- https://gitlab.com/parrotsec/packages/cyberchef

### ddrescue

data recovery and protection tool When your disk has crashed and you try to copy it over to another one, standard Unix tools like cp, cat, and dd will abort on every I/O error, dd_rescue does not. It optimizes copying by using large blocks as long as no errors occur and falls back to smaller blocks. It supports reverse direction copying (to approach a bad spot from the top), sparse copying, preallocating space, splice zerocopy, and bypassing the kernel pagecache with O_DIRECT. dd_rescue provides safe deletion of data by overwriting files (or better partitions/disks) multiple times with fast random numbers. With the ddr_hash plugin, it supports calculating a hash value (such as a sha256sum) or an HMAC during copying.

- http://www.garloff.de/kurt/linux/ddrescue/
- https://gitlab.com/parrotsec/packages/ddrescue

### email2phonenumber

OSINT tool to obtain a target's phone number by having their email address This package contains an OSINT tool that allows you to obtain a target's phone number just by having their email address. This tool helps automate discovering someone's phone number by abusing password reset design weaknesses and publicly available data. It supports 3 main functions: * "scrape" - scrapes websites for phone number digits by initiating password reset using the target's email address. * "generate" - creates a list of valid phone numbers based on the country's Phone Numbering Plan publicly available information. * "bruteforce" - iterates over a list of phone numbers and initiates password reset on different websites to obtain associated masked emails and correlate it to the victim's one.

- https://github.com/martinvigo/email2phonenumber
- https://gitlab.com/parrotsec/packages/email2phonenumber

### evil-ssdp

Spoof SSDP replies to phish for NTLM hashes on a network This tool responds to SSDP multicast discover requests, posing as a generic UPNP device on a local network. Your spoofed device will magically appear in Windows Explorer on machines in your local network. Users who are tempted to open the device are shown a configurable webpage.

- https://github.com/initstring/evil-ssdp
- https://gitlab.com/parrotsec/packages/evil-ssdp

### golang-github-andrew-d-go-termutil

Terminal utilities for golang (library) This package contains terminal utilities. It exposes some very basic, useful functions: - Isatty(file *os.File) bool: this function will return whether or not the given file is a TTY, attempting to use native operations when possible. It wil fall back to using the isatty() function from unistd.h through cgo if on an unknown platform. - GetPass(prompt string, prompt_fd, input_fd uintptr) ([]byte, error): this function will print the prompt string to the file identified by prompt_fd, prompt the user for a password without echoing the password to the terminal, print a newline, and then return the given password to the user.

- https://github.com/andrew-d/go-termutil
- https://gitlab.com/parrotsec/packages/golang-github-andrew-d-go-termutil

### golang-github-ne0nd0g-ja3transport

Impersonating JA3 signatures (library) This package contains an Go library to mock JA3 easily JA3 signatures. JA3 is a method for fingerprinting TLS clients using options in the TLS ClientHello packet like SSL version and available client extensions. At its core, this method of detecting malicious traffic is marginally better than the User-Agent header in HTTP since the client is in control of the ClientHello packet. Currently, there is no tooling available to easily craft ClientHello packets, so the JA3 hash is a great detection mechanism.

- https://github.com/Ne0nd0g/ja3transport
- https://gitlab.com/parrotsec/packages/golang-github-ne0nd0g-ja3transport

### hash-identifier

Tool to identify hash types Software to identify the different types of hashes used to encrypt data and especially passwords.

- https://github.com/blackploit/hash-identifier
- https://gitlab.com/parrotsec/packages/hash-identifier

### ident-user-enum

Query ident to determine the owner of a TCP network process This package is a simple PERL script to query the ident service (113/TCP) in order to determine the owner of the process listening on each TCP port of a target system. This can help to prioritise target service during a pentest (you might want to attack services running as root first). Alternatively, the list of usernames gathered can be used for password guessing attacks on other network services.

- https://pentestmonkey.net/tools/user-enumeration/ident-user-enum
- https://gitlab.com/parrotsec/packages/ident-user-enum

### johnny

GUI for John the Ripper Johnny is provides a GUI for the John the Ripper password cracking tool.

- https://openwall.info/wiki/john/johnny
- https://gitlab.com/parrotsec/packages/johnny

### lapsdumper

Tool that dumps LAPS passwords A tool that dumps every LAPS password the account has the ability to read with a domain.

- https://github.com/n00py/LAPSDumper
- https://gitlab.com/parrotsec/packages/lapsdumper

### mimikatz

Uses admin rights on Windows to display passwords in plaintext Mimikatz uses admin rights on Windows to display passwords of currently logged in users in plaintext.

- https://blog.gentilkiwi.com/mimikatz
- https://gitlab.com/parrotsec/packages/mimikatz

### multiforcer

GPU accelerated password cracking tool A CUDA & OpenCL accelerated rainbow table implementation from the ground up, and a CUDA hash brute forcing tool with support for many hash types including MD5, SHA1, LM, NTLM, and lots more.

- https://sourceforge.net/projects/cryptohaze/
- https://gitlab.com/parrotsec/packages/multiforcer

### name-that-hash

Identify MD5, SHA256 and 300+ other hash types This package contains a utility to identify hash types. Have you ever come across a hash such as 5f4dcc3b5aa765d61d8327deb882cf99 and wondered what type of hash type that is? Name-that-hash will name it for you.

- https://github.com/HashPals/Name-That-Hash
- https://gitlab.com/parrotsec/packages/name-that-hash

### oclgausscrack

Cracks verification hashes of the Gauss Virus The goal of the program is to crack the verification hash of the encrypted payload of the Gauss Virus. Uses OpenCL to accelerate the 10k MD5 loop Uses optimizations also used in oclHashcat-plus for maximum performance Able to handle multi-GPU setups (of the same type) VCL (Virtual CL) v1.18 compatible Open Source Supports integration into distributed computing environments Supports resume

- https://github.com/jsteube/oclGaussCrack
- https://gitlab.com/parrotsec/packages/oclgausscrack

### oscanner

Oracle assessment framework Oscanner is an Oracle assessment framework developed in Java. It has a plugin-based architecture and comes with a couple of plugins that currently do: - Sid Enumeration - Passwords tests (common & dictionary) - Enumerate Oracle version - Enumerate account roles - Enumerate account privileges - Enumerate account hashes - Enumerate audit information - Enumerate password policies - Enumerate database links The results are given in a graphical java tree.

- http://www.cqure.net/wp/tools/database/oscanner/
- https://gitlab.com/parrotsec/packages/oscanner

### passing-the-hash

Patched tools to use password hashes as authentication input This package contains modified versions of Curl, Iceweasel, FreeTDS, Samba 4, WinEXE and WMI. They are installed as executables starting with the "pth-" string.

- http://passing-the-hash.blogspot.fr
- https://gitlab.com/parrotsec/packages/passing-the-hash

### passwordmeter

Package entry imported from the ParrotSec package index.

- https://github.com/cadithealth/passwordmeter
- https://gitlab.com/parrotsec/packages/passwordmeter

### photon

Incredibly fast crawler designed for open source intelligence This package includes a fast and flexible crawler designed for open source intelligence (OSINT). Photon can extract the following data while crawling: - URLs (in-scope & out-of-scope) - URLs with parameters (example.com/gallery.php?id=2) - Intel (emails, social media accounts, amazon buckets etc.) - Files (pdf, png, xml etc.) - Secret keys (auth/API keys & hashes) - JavaScript files & Endpoints present in them - Strings matching custom regex pattern - Subdomains & DNS related data The extracted information is saved in an organized manner or can be exported as json.

- https://github.com/s0md3v/Photon
- https://gitlab.com/parrotsec/packages/photon

### pipal

Statistical analysis on password dumps All this tool does is to give you the stats and the information to help you analyse the passwords. The real work is done by you in interpreting the results.

- https://www.digininja.org/projects/pipal.php
- https://gitlab.com/parrotsec/packages/pipal

### rainbowcrack

Rainbow table password cracker RainbowCrack is a general propose implementation of Philippe Oechslin's faster time-memory trade-off technique. It crack hashes with rainbow tables. RainbowCrack uses time-memory tradeoff algorithm to crack hashes. It differs from the hash crackers that use brute force algorithm.

- http://project-rainbowcrack.com/index.htm
- https://gitlab.com/parrotsec/packages/rainbowcrack

### ridenum

Null session RID cycle attack tool Rid Enum is a RID cycling attack that attempts to enumerate user accounts through null sessions and the SID to RID enum. If you specify a password file, it will automatically attempt to brute force the user accounts when its finished enumerating.

- https://github.com/trustedsec/ridenum
- https://gitlab.com/parrotsec/packages/ridenum

### rling

better rli This package is similar to the rli utility found in hashcat-utils, but much, much faster. rli compares a single file against another file(s) and removes all duplicates.

- https://github.com/Cynosureprime/rling
- https://gitlab.com/parrotsec/packages/rling

### ruby-sha3

SHA3 for Ruby This package contains a native (C) FIPS 202 compliant implementation of SHA3 (Keccak) cryptographic hashing algorithm.

- https://github.com/johanns/sha3
- https://gitlab.com/parrotsec/packages/ruby-sha3

### seclists

Collection of multiple types of security lists SecLists is a collection of multiple types of lists used during security assessments. List types include usernames, passwords, URLs, sensitive data grep strings, fuzzing payloads, and many more. The goal is to enable a security tester to pull this repo onto a new testing box and have access to every type of list that may be needed.

- https://www.owasp.org/index.php/Projects/OWASP_SecLists_Project
- https://gitlab.com/parrotsec/packages/seclists

### sprayingtoolkit

Scripts to make password spraying attacks against Lync/S4B, OWA & O365 A set of Python scripts/utilities that tries to make password spraying attacks against Lync/S4B & OWA a lot quicker, less painful and more efficient.

- https://github.com/byt3bl33d3r/SprayingToolkit
- https://gitlab.com/parrotsec/packages/sprayingtoolkit

### sqlmap

automatic SQL injection tool sqlmap goal is to detect and take advantage of SQL injection vulnerabilities in web applications. Once it detects one or more SQL injections on the target host, the user can choose among a variety of options to perform an extensive back-end database management system fingerprint, retrieve DBMS session user and database, enumerate users, password hashes, privileges, databases, dump entire or user's specific DBMS tables/columns, run his own SQL statement, read specific files on the file system and more.

- http://sqlmap.org/
- https://gitlab.com/parrotsec/packages/sqlmap

### thc-pptp-bruter

THC PPTP Brute Force Brute force program against pptp vpn endpoints (tcp port 1723). Fully standalone. Supports latest MSChapV2 authentication. Tested against Windows and Cisco gateways. Exploits a weakness in Microsoft's anti-brute force implementation which makes it possible to try 300 passwords the second.

- http://www.thc.org/releases.php
- https://gitlab.com/parrotsec/packages/thc-pptp-bruter

### truecrack

Bruteforce password cracker for TrueCrypt volumes TrueCrack is a bruteforce password cracker for TrueCrypt (Copyright) volume. It is optimazed with Nvidia Cuda technology. It works with PBKDF2 (defined in PKCS5 v2.0) based on RIPEMD160 Key derivation function and XTS block cipher mode of operation used for hard disk encryption based on AES.

- https://github.com/lvaccaro/truecrack
- https://gitlab.com/parrotsec/packages/truecrack

### twofi

Twitter words of interest When attempting to crack passwords custom word lists are very useful additions to standard dictionaries. An interesting idea originally released on the "7 Habits of Highly Effective Hackers" blog was to use Twitter to help generate those lists based on searches for keywords related to the list that is being cracked. I've expanded this idea into twofi which will take multiple search terms and return a word list sorted by most common first.

- https://www.digininja.org/projects/twofi.php
- https://gitlab.com/parrotsec/packages/twofi

### username-anarchy

Username tool for penetration testing. Tool to generate common passwords based on usernames or other known information This is useful for user account/password brute force guessing and username enumeration when usernames are based on the users' names. By attempting a few weak passwords across a large set of user accounts, user account lockout thresholds can be avoided. Users' names can be identified through a variety of methods: Web scraping employee names from LinkedIn, Facebook, and other social networks. Extracting metadata from document types such as PDF, Word, Excel, etc. This can be performed with FOCA. Common aliases, or self chosen usernames, from forums are also included.

- https://github.com/urbanadventurer/username-anarchy
- https://gitlab.com/parrotsec/packages/username-anarchy

### wordlistraider

Tool to prepare existing wordlists This package contains a Python tool for preparing existing wordlists. It returns a selection of words that matches the passed conditions in an existing list. As an example you have a GB big wordlist and you only want passwords with a length of at least 8 characters. This optimizes word lists and saves unnecessary requests.

- https://github.com/GregorBiswanger/WordlistRaider
- https://gitlab.com/parrotsec/packages/wordlistraider

### wpa-sycophant

tool to relay phase 2 authentication attempts to access corporate wireless This package contains a tool to relay phase 2 authentication attempts to access corporate wireless without cracking the password. To use this technique it is required that you run a rogue access point so that a legitimate user will connect to you so that you may relay the authentication attempt to Sycophant.

- https://github.com/sensepost/wpa_sycophant
- https://gitlab.com/parrotsec/packages/wpa-sycophant


## Bluetooth Security and Analysis

### Wireshark

Open source network protocol analyzer with support for inspecting Bluetooth traffic captures. Commonly used for Bluetooth protocol study, packet troubleshooting, and defensive traffic analysis.

- Official site: https://www.wireshark.org/
- User guide: https://www.wireshark.org/docs/
- Wiki: https://wiki.wireshark.org/

### Ubertooth One

Open source 2.4 GHz wireless development platform for Bluetooth experimentation and packet capture workflows. Frequently used in Bluetooth lab setups for monitoring and protocol analysis.

- Official site: https://greatscottgadgets.com/ubertoothone/
- GitHub: https://github.com/greatscottgadgets/ubertooth
- Documentation: https://ubertooth.readthedocs.io/

### BlueZ

Official Linux Bluetooth protocol stack with utilities for device management, diagnostics, and traffic inspection. Useful for Bluetooth development, protocol testing, and host-side troubleshooting on Linux.

- GitHub: https://github.com/bluez/bluez
- Documentation: https://github.com/bluez/bluez/tree/master/doc

### btmon

Bluetooth monitoring utility included with BlueZ for capturing and inspecting Bluetooth activity at the host stack level. Useful for debugging adapters, pairing flows, and protocol behavior on Linux systems.

- Source and docs: https://github.com/bluez/bluez
- BlueZ documentation: https://github.com/bluez/bluez/tree/master/doc

### Kismet

Wireless monitoring platform with Bluetooth support for discovering nearby devices and collecting wireless telemetry. Useful for passive monitoring, inventory, and situational awareness in authorized environments.

- Official site: https://www.kismetwireless.net/
- GitHub: https://github.com/kismetwireless/kismet

### Scapy

Extensible packet manipulation framework that supports low-level protocol analysis and custom packet workflows. Useful for controlled Bluetooth-related protocol research and defensive lab automation.

- Documentation: https://scapy.readthedocs.io/en/latest/
- GitHub: https://github.com/secdev/scapy

### PyShark

Python wrapper around TShark and Wireshark dissectors for scripted packet parsing. Useful for automating Bluetooth capture analysis and extracting protocol metadata from packet traces.

- GitHub: https://github.com/KimiNewt/pyshark

### Bleak

Cross-platform Python Bluetooth Low Energy client library for discovering and interacting with BLE devices. Useful for inventory, diagnostics, and testing of devices you own or are authorized to assess.

- GitHub: https://github.com/hbldh/bleak
- Documentation: https://bleak.readthedocs.io/

### Bless

Cross-platform Python Bluetooth Low Energy server library for creating BLE peripherals in test environments. Useful for building mock devices and validating Bluetooth application behavior in a controlled lab.

- GitHub: https://github.com/kevincar/bless

### Frida

Dynamic instrumentation toolkit for observing and modifying application behavior at runtime. Commonly used to inspect how Android and iOS apps interact with Bluetooth APIs during security reviews.

- Official site: https://frida.re/
- Documentation: https://frida.re/docs/home/
- GitHub: https://github.com/frida/frida

### Objection

Runtime mobile application exploration toolkit built on top of Frida. Useful for authorized assessment of Android and iOS applications, including inspection of Bluetooth-related application logic.

- GitHub: https://github.com/sensepost/objection
- Wiki: https://github.com/sensepost/objection/wiki

### MobSF

Automated mobile application security testing framework for static and dynamic analysis. Useful for reviewing Android and iOS apps that use Bluetooth features, permissions, or device communication workflows.

- GitHub: https://github.com/MobSF/Mobile-Security-Framework-MobSF
- Documentation: https://mobsf.github.io/docs/

### Ghidra

Software reverse engineering framework widely used for firmware and binary analysis. Useful for studying Bluetooth-enabled device firmware during defensive research and hardware security reviews.

- GitHub: https://github.com/NationalSecurityAgency/ghidra
- Documentation: https://github.com/NationalSecurityAgency/ghidra/tree/master/Docs

### ida-pro-mcp

MCP server for integrating IDA Pro into reverse engineering workflows.

- GitHub: https://github.com/mrexodia/ida-pro-mcp
- Documentation: https://github.com/mrexodia/ida-pro-mcp/blob/master/README.md

### reverse-skill

AI agent workflow router and tool orchestration pack for reverse engineering, security analysis, and CTF-oriented tasks. Useful as a structured skill pack for authorized research and lab workflows.

- GitHub: https://github.com/zhaoxuya520/reverse-skill
- Overview: https://github.com/zhaoxuya520/reverse-skill/blob/main/OVERVIEW.md

### Binwalk

Firmware analysis tool for extracting and inspecting embedded system images. Commonly used before reverse engineering Bluetooth device firmware and related update packages.

- GitHub: https://github.com/ReFirmLabs/binwalk

### Firmware Mod Kit

Utilities for unpacking, modifying, and rebuilding embedded Linux firmware images in lab workflows. Useful for understanding firmware layout before deeper Bluetooth-related device analysis.

- GitHub: https://github.com/rampageX/firmware-mod-kit

### Bluetooth SIG Specifications

Official Bluetooth specifications, assigned numbers, and developer resources from the Bluetooth Special Interest Group. Essential reference material for protocol learning, interoperability, and standards-based analysis.

- Official specifications: https://www.bluetooth.com/specifications/specs/
- Assigned numbers: https://www.bluetooth.com/specifications/assigned-numbers/

### OWASP Mobile Security Testing Guide

Open security testing guidance for mobile applications, including methodology relevant to Bluetooth-enabled app assessments. Useful for structuring defensive reviews and mobile testing workflows.

- Project page: https://owasp.org/www-project-mobile-security-testing-guide/
- OWASP MAS portal: https://owasp.org/mas

### OWASP Mobile Security Project

OWASP mobile security project resources covering best practices, testing methodology, and defensive guidance for Android and iOS applications.

- Project page: https://owasp.org/www-project-mobile-security/
- OWASP MAS portal: https://owasp.org/mas

## Attack Surface Discovery

### Amass

OWASP Amass is an attack surface mapping and external asset discovery framework that combines open source intelligence gathering with active reconnaissance techniques. It is widely used for subdomain enumeration, asset discovery, and broader reconnaissance workflows.

- GitHub: https://github.com/owasp-amass/amass
- OWASP project page: https://owasp.org/www-project-amass/
- Documentation: https://owasp-amass.github.io/docs/
- Discord: https://discord.gg/OWASP

### OSINT-Cheat-sheet

OSINT cheat sheet, list OSINT tools, wiki, dataset, article, book , red team OSINT for hackers and OSINT tips and OSINT branch. This repository will grow every time will research, there is a research, science and tech...

- GitHub: https://github.com/Jieyab89/OSINT-Cheat-sheet
- Official site: https://jieyab89.github.io/OSINT-Cheat-sheet/Web-Based/
- Documentation: https://github.com/Jieyab89/OSINT-Cheat-sheet/blob/main/README.md
- Topics: cheatsheet, cybersecurity, datasets, education, hacking, imint, information-gathering, information-security

### AutoAR

AutoAR is an automated security reconnaissance tool, ASM and Discord bot for bug bounty hunters and penetration testers. It automates gathering subdomains, scanning ports, detecting technologies, mapping GitHub reposi...

- GitHub: https://github.com/h0tak88r/AutoAR
- Documentation: https://github.com/h0tak88r/AutoAR/blob/master/README.md
- Topics: asm, attack-surface-managment, automation, bash, bughunting, cybersecurity, pentesting, scanning

### Buildware-Tools

Buildware-Tools is an all-in-one multitool for security research and automation.

- GitHub: https://github.com/v4lkyr0/Buildware-Tools
- Official site: https://guns.lol/sg0r
- Documentation: https://github.com/v4lkyr0/Buildware-Tools/blob/main/README.md
- Topics: cybersecurity, discord-token, discord-tool, ethical-hacking, hacking-tool, ip-scanner, multitool, network-scanner

### rekono

Pentesting automation platform that combines hacking tools to complete assessments

- GitHub: https://github.com/pablosnt/rekono
- Official site: https://github.com/pablosnt/rekono/wiki
- Documentation: https://github.com/pablosnt/rekono/blob/main/README.md
- Topics: bug-bounty, bug-hunter, easm, external-attack-surface-management, hacking, hacking-collaboration-platform, hacking-copilot, infosec

### wpprobe

A fast WordPress plugin enumeration tool

- GitHub: https://github.com/Chocapikk/wpprobe
- Documentation: https://github.com/Chocapikk/wpprobe/blob/main/README.md
- Topics: bug-bounty, enumeration, exploit, pentest, recon, rest-api, security, security-tools

### omnisci3nt

Omnisci3nt is an open-source web reconnaissance and intelligence tool for extracting deep technical insights from domains, including subdomains, SSL certificates, exposed services, archived content, and configuration...

- GitHub: https://github.com/spyboy-productions/omnisci3nt
- Documentation: https://github.com/spyboy-productions/omnisci3nt/blob/main/README.md
- Topics: admin-login-finder, admin-panel-finder, admin-panel-finder-of-any-website, directory-enumeration, dmarc-record-examination, dns-enumeration, ip-lookup, osint

### vesper

A simple username osint tool built in rust

- GitHub: https://github.com/krishpranav/vesper
- Documentation: https://github.com/krishpranav/vesper/blob/master/README.md
- Topics: cli, golang, information-gathering, information-retrieval, osint, reconnaissance, rust, tools
### nuclei

Nuclei is a fast, customizable vulnerability scanner powered by the global security community and built on a simple YAML-based DSL, enabling collaboration to tackle trending vulnerabilities on the internet. It helps y...

- GitHub: https://github.com/projectdiscovery/nuclei
- Official site: https://docs.projectdiscovery.io/tools/nuclei
- Topics: attack-surface, cve-scanner, dast, hacktoberfest, nuclei-engine, security, security-scanner, subdomain-takeover
### sx

:vulcan_salute: Fast, modern, easy-to-use network scanner

- GitHub: https://github.com/v-byte-cpu/sx
- Documentation: https://github.com/v-byte-cpu/sx/blob/master/README.md
- Topics: arp, docker, go, icmp, infosec, ipv4, lan, network

### NetShark

All-in-one CLI security scanner: port scanning, web security, subdomain enumeration, network monitoring. Multi-threaded, cross-platform.

- GitHub: https://github.com/kalachbeg/NetShark
- Documentation: https://github.com/kalachbeg/NetShark/blob/main/README.md
- Topics: cli-tool, cybersecurity, hacking-tools, netsec, network-security, open-source, penetration-testing, port-scanner

### H4X-Tools

A modular, terminal-based toolkit for OSINT, reconnaissance, and scraping - built in Python, runs on Linux and Windows.

- GitHub: https://github.com/vil/H4X-Tools
- Official site: https://vili.dev
- Documentation: https://github.com/vil/H4X-Tools/blob/master/README.md
- Topics: data-gathering, dirbuster, email-osint, h4x-tools, hacking, hacking-tool, hacktools, igscraper

### subfinder

Fast passive subdomain enumeration tool.

- GitHub: https://github.com/projectdiscovery/subfinder
- Official site: https://projectdiscovery.io
- Documentation: https://github.com/projectdiscovery/subfinder/blob/dev/README.md
- Topics: bugbounty, hacking, hacktoberfest, osint, reconnaissance, subdomain-enumeration, subdomains

### X-osint

This is an Open source intelligent framework ie an osint tool which gathers valid information about a phone number, user's email address, perform VIN Osint, and reverse, perform subdomain enumeration, able to find ema...

- GitHub: https://github.com/TermuxHackz/X-osint
- Official site: https://termuxhackz.github.io/How-to-get-information-using-Xosint.html
- Documentation: https://github.com/TermuxHackz/X-osint/blob/master/README.md
- Topics: dns-lookup, dns-reverse, email-osint, google-dork, google-hacking, info-gathering, information-gathering, ip-osint
### ivre

Network recon framework. Build your own, self-hosted and fully-controlled alternatives to Shodan / ZoomEye / Censys and GreyNoise, run your Passive DNS service, build your taylor-made EASM tool, collect and analyse ne...

- GitHub: https://github.com/ivre/ivre
- Official site: https://ivre.rocks/
- Documentation: https://github.com/ivre/ivre/blob/master/README.md
- Topics: bro, easm, external-attack-surface-management, hacktoberfest, masscan, network, network-discovery, network-recon

### urlfinder

A high-speed tool for passively gathering URLs, optimized for efficient and comprehensive web asset discovery without active scanning.

- GitHub: https://github.com/projectdiscovery/urlfinder
- Documentation: https://github.com/projectdiscovery/urlfinder/blob/dev/README.md
- Topics: bugbounty, endpoint, hacking, osint, reconnaissance, url, urls

### WhatsMyName

Community-maintained dataset of 700+ websites for finding accounts by username — powers OSINT and digital footprint tools.

- GitHub: https://github.com/WebBreacher/WhatsMyName
- Documentation: https://github.com/WebBreacher/WhatsMyName/blob/main/README.md
- Topics: cybersecurity, dataset, json, osint, osint-tool, recon, user-enumeration, username

### leaker

Passive leak enumeration tool.

- GitHub: https://github.com/vflame6/leaker
- Official site: https://maksimradaev.com/posts/introducing-leaker/
- Documentation: https://github.com/vflame6/leaker/blob/main/README.md
- Topics: bugbounty, hacking, leak-detection, leaks, osint, reconnaissance

### Pentest-Swarm-AI

Autonomous penetration testing using a swarm of AI agents. Orchestrates recon, classification, exploitation, and reporting specialists with ReAct reasoning — supports bug bounty, continuous monitoring, and CTF modes....

- GitHub: https://github.com/Armur-Ai/Pentest-Swarm-AI
- Documentation: https://github.com/Armur-Ai/Pentest-Swarm-AI/blob/main/README.md
- Topics: ai-agents, bug-bounty, cybersecurity, offensive-security, penetration-testing, penetration-testing-framework, penetration-testing-tools

### Nightingale

Nightingale Docker for Pentesters is a comprehensive Dockerized environment tailored for penetration testing and vulnerability assessment. It comes preconfigured with all essential tools and utilities required for eff...

- GitHub: https://github.com/RAJANAGORI/Nightingale
- Official site: https://nightingale-security.com/
- Documentation: https://github.com/RAJANAGORI/Nightingale/blob/main/README.md
- Topics: bugbounty, cybersecurity, docker-image, hacking, hacking-tools, htb, nightingale, osint

### nomore403

🚫 Advanced tool for security researchers to bypass 403/40X restrictions through smart techniques and adaptive request manipulation. Fast. Precise. Effective.

- GitHub: https://github.com/devploit/nomore403
- Documentation: https://github.com/devploit/nomore403/blob/main/README.md
- Topics: 403, 403-bypass, bugbounty, bypass, ctf, go, http, pentest

### findme

FindME is a CLI tool for searching social media and online profiles linked to a username. It’s ideal for reconnaissance, digital footprint verification, or checking username availability.

- GitHub: https://github.com/0xSaikat/findme
- Official site: https://findme.hackzar.com
- Documentation: https://github.com/0xSaikat/findme/blob/main/README.md
- Topics: osint, osint-python, osint-reconnaissance, osint-resources, osint-tool, osint-toolkit, osint-tools, osinttool

### Awesome-OSINT-List

📡 Comprehensive collection of OSINT tools for cybersecurity professionals, researchers, and bug bounty hunters. Topics: information gathering, reverse search, red team, trust & safety, AI.

- GitHub: https://github.com/Astrosp/Awesome-OSINT-List
- Official site: https://astrosp.github.io/osint-web/
- Documentation: https://github.com/Astrosp/Awesome-OSINT-List/blob/main/README.md
- Topics: ai, ai-tools, awesome-list, bug-bounty, cybersecurity, information-gathering, osint, pentest

### MailAccess

Free email OSINT tool, 2500+ platforms, identity clustering, breach detection. No API keys required. pip install mailaccess

- GitHub: https://github.com/KatrielMoses/MailAccess
- Documentation: https://github.com/KatrielMoses/MailAccess/blob/main/README.md
- Topics: cybersecurity, email, email-automation, email-osint, holehe, infosec, maltego, open-source

### Refloow-Geo-Forensics

❤️ Free batch image & video geolocation digital forensics tool. Automatically extract EXIF data, visualize GPS coordinates on maps, and reconstruct event timelines for OSINT

- GitHub: https://github.com/Refloow/Refloow-Geo-Forensics
- Official site: https://refloow.com/open-source-software/refloow-geo-forensics
- Documentation: https://github.com/Refloow/Refloow-Geo-Forensics/blob/main/README.md
- Topics: digital-forensics, exif, geolocation, image-forensics, investigation-tool, metadata-extraction, open-source, osint

### reconftw

reconFTW is a tool designed to perform automated recon on a target domain by running the best set of tools to perform scanning and finding out vulnerabilities

- GitHub: https://github.com/six2dez/reconftw
- Official site: https://docs.reconftw.com/
- Topics: bug-bounty, bugbounty, bugbounty-tool, dns, hacking, nuclei, osint, penetration-testing

### tookie-osint

Tookie is a advanced OSINT information gathering tool that finds social media accounts based on inputs.

- GitHub: https://github.com/Alfredredbird/tookie-osint
- Official site: https://alfredredbird.github.io/tookie-osint/
- Documentation: https://github.com/Alfredredbird/tookie-osint/blob/main/README.md
- Topics: cyber-security, cybersecurity, hacking-tool, hacking-tools, information-gathering, osint, osint-framework, osint-kali

### altdns

Subdomain discovery through alterations and permutations This package contains a DNS recon tool that allows for the discovery of subdomains that conform to patterns. Altdns takes in words that could be present in subdomains under a domain (such as test, dev, staging) as well as takes in a list of subdomains that you know of. From these two lists that are provided as input to altdns, the tool then generates a massive output of "altered" or "mutated" potential subdomains that could be present. It saves this output so that it can then be used by your favourite DNS bruteforcing tool.

- https://github.com/infosec-au/altdns
- https://gitlab.com/parrotsec/packages/altdns

### assetfinder

Find domains and subdomains related to a given domain assetfinder is a command-line tool designed to find domains and subdomains associated with a specific domain. The main objective of the tool is to help security researchers and IT professionals discover and understand how the domains and sub-domains of a given organization are distributed, trying to find possible security flaws and vulnerabilities. assetfinder uses multiple data sources to perform its research, including: - crt.sh - certspotter - hackertarget - threatcrowd - Wayback Machine - dns.bufferover.run - Facebook Graph API - Virustotal - findsubdomains This expands coverage and increases the accuracy of results.

- https://github.com/tomnomnom/assetfinder
- https://gitlab.com/parrotsec/packages/assetfinder

### bettercap

Complete, modular, portable and easily extensible MITM framework This package contains a Swiss Army knife for 802.11, BLE and Ethernet networks reconnaissance and attacks.

- https://www.bettercap.org
- https://gitlab.com/parrotsec/packages/bettercap

### dbd

Netcat clone with encryption dbd is a Netcat-clone, designed to be portable and offer strong encryption. It runs on Unix-like operating systems and on Microsoft Win32. dbd features AES-CBC-128 + HMAC-SHA1 encryption (by Christophe Devine), program execution (-e option), choosing source port, continuous reconnection with delay, and some other nice features. dbd supports TCP/IP communication only. Source code and binaries are distributed under the GNU General Public License.

- https://github.com/gitdurandal/dbd
- https://gitlab.com/parrotsec/packages/dbd

### dnsx

perform multiple dns queries This package contains a fast and multi-purpose DNS toolkit allow to run multiple probes using retryabledns library, that allows you to perform multiple DNS queries of your choice with a list of user supplied resolvers, additionally supports DNS wildcard filtering like shuffledns (https://github.com/projectdiscovery/shuffledns). Features * Simple and Handy utility to query DNS records * Supports A, AAAA, CNAME, PTR, NS, MX, TXT, SOA * Supports DNS Status Code probing * Supports DNS Tracing * Handles wildcard subdomains in automated way. * Stdin and stdout support to work with other tools.

- https://github.com/projectdiscovery/dnsx
- https://gitlab.com/parrotsec/packages/dnsx

### hosthunter

tool to discover and extract hostnames providing a set of target IP addresses This package contains a tool to efficiently discover and extract hostnames providing a large set of target IP addresses. HostHunter utilises simple OSINT techniques to map IP addresses with virtual hostnames. It generates a CSV or TXT file containing the results of the reconnaissance. Latest version of HostHunter also takes screenshots of the targets, it is currently a beta functionality.

- https://github.com/SpiderLabs/HostHunter
- https://gitlab.com/parrotsec/packages/hosthunter

### intrace

Traceroute-like application piggybacking on existing TCP connections InTrace is a traceroute-like application that enables users to enumerate IP hops exploiting existing TCP connections, both initiated from local network (local system) or from remote hosts. It could be useful for network reconnaissance and firewall bypassing.

- https://github.com/robertswiecki/intrace
- https://gitlab.com/parrotsec/packages/intrace

### jd-gui

GUI Java .class decompiler JD-GUI is a standalone graphical utility that displays Java source codes of ".class" files. You can browse the reconstructed source code with the JD-GUI for instant access to methods and fields.

- http://jd.benow.ca/
- https://gitlab.com/parrotsec/packages/jd-gui

### legion

Semi-automated network penetration testing framework Legion, a fork of SECFORCE's Sparta, is an open source, easy-to-use, super-extensible and semi-automated network penetration testing framework that aids in discovery, reconnaissance and exploitation of information systems.

- https://github.com/Hackman238/Legion
- https://gitlab.com/parrotsec/packages/legion

### recon-ng

Web Reconnaissance framework written in Python Recon-ng is a full-featured Web Reconnaissance framework written in Python. Complete with independent modules, database interaction, built in convenience functions, interactive help, and command completion, Recon-ng provides a powerful environment in which open source web-based reconnaissance can be conducted quickly and thoroughly. Recon-ng has a look and feel similar to the Metasploit Framework, reducing the learning curve for leveraging the framework. However, it is quite different. Recon-ng is not intended to compete with existing frameworks, as it is designed exclusively for web-based open source reconnaissance. If you want to exploit, use the Metasploit Framework. If you want to Social Engineer, use the Social Engineer Toolkit.

- https://github.com/lanmaster53/recon-ng
- https://gitlab.com/parrotsec/packages/recon-ng

### rtpbreak

Detects, reconstructs, and analyzes RTP sessions With rtpbreak you can detect, reconstruct and analyze any RTP session. It doesn't require the presence of RTCP packets and works independently form the used signaling protocol (SIP, H.323, SCCP, ...). The input is a sequence of packets, the output is a set of files you can use as input for other tools (wireshark/tshark, sox, grep/awk/cut/ cat/sed, ...). It supports also wireless (AP_DLT_IEEE802_11) networks.

- http://dallachiesa.com/code/rtpbreak/
- https://gitlab.com/parrotsec/packages/rtpbreak

### sbd

Secure backdoor for linux and windows sbd is a Netcat-clone, designed to be portable and offer strong encryption. It runs on Unix-like operating systems and on Microsoft Win32. sbd features AES-CBC-128 + HMAC-SHA1 encryption (by Christophe Devine), program execution (-e option), choosing source port, continuous reconnection with delay, and some other nice features. sbd supports TCP/IP communication only.

- https://mirrors.kernel.org/gentoo/distfiles/sbd-1.37.tar.gz
- https://gitlab.com/parrotsec/packages/sbd

### skipfish

fully automated, active web application security reconnaissance tool Skipfish is an active web application security reconnaissance tool. It prepares an interactive sitemap for the targeted site by carrying out a recursive crawl and dictionary-based probes. The resulting map is then annotated with the output from a number of active (but hopefully non-disruptive) security checks. The final report generated by the tool is meant to serve as a foundation for professional web application security assessments.

- https://gitlab.com/parrotsec/packages/skipfish

### theharvester

tool for gathering e-mail accounts and subdomain names from public sources The package contains a tool for gathering subdomain names, e-mail addresses, virtual hosts, open ports/ banners, and employee names from different public sources (search engines, pgp key servers).

- https://github.com/laramies/theHarvester
- https://gitlab.com/parrotsec/packages/theharvester

### zonedb

Public Zone Database (program) This package provides a free, open-source database (http://opendatacommons.org/licenses/odbl/1.0/) containing a list and associated metadata of public DNS zones (http://en.wikipedia.org/wiki/DNS_zone) (domain name extensions). It attempts to be exhaustive, including current, retired, and withdrawn top-level domains and subdomains.

- https://github.com/zonedb/zonedb
- https://gitlab.com/parrotsec/packages/zonedb


## Scanning


### immunity-agent

The security layer for AI coding agents : Skill governance, safe package recommendations, MCP/tools guardrails, secret protection, runtime policy enforcement and full audit visibility with a self-serve dashboard.

- GitHub: https://github.com/PrismorSec/immunity-agent
- Official site: https://prismor.dev
- Documentation: https://github.com/PrismorSec/immunity-agent/blob/main/README.md
- Topics: agent-security, agentic-ai, agents, ai-security, cybersecurity, prompt-injection, prompt-security, security

### naabu

A fast port scanner written in go with a focus on reliability and simplicity. Designed to be used in combination with other tools for attack surface discovery in bug bounties and pentests

- GitHub: https://github.com/projectdiscovery/naabu
- Official site: https://projectdiscovery.io
- Documentation: https://github.com/projectdiscovery/naabu/blob/dev/README.md
- Topics: cdn-exclusion, hacktoberfest, nmap, port-enumeration, portscanner, scan-ports

### NetExec

The Network Execution Tool

- GitHub: https://github.com/Pennyw0rth/NetExec
- Official site: https://netexec.wiki/
- Documentation: https://github.com/Pennyw0rth/NetExec/blob/main/README.md
- Topics: active-directory, hacking, infosec, infosectools, networks, pentest, pentest-tool, pentest-tools

### tsunami-security-scanner

Tsunami is a general purpose network security scanner with an extensible plugin system for detecting high severity vulnerabilities with high confidence.

- GitHub: https://github.com/google/tsunami-security-scanner
- Documentation: https://github.com/google/tsunami-security-scanner/blob/master/README.md

### Malcolm

Malcolm is a powerful, easily deployable network traffic analysis tool suite for full packet capture artifacts (PCAP files), Zeek logs and Suricata alerts.

- GitHub: https://github.com/cisagov/Malcolm
- Official site: https://cisagov.github.io/Malcolm/
- Documentation: https://github.com/cisagov/Malcolm/blob/main/README.md
- Topics: arkime, cybersecurity, infosec, network-security, network-traffic-analysis, networksecurity, networktrafficanalysis, opensearch

### dpi-detector

DPI detection tool for internet censorship testing. It identifies TLS, TCP, HTTP, and DNS blocking, including 16-20KB connection drops commonly associated with DPI-based interference.

- GitHub: https://github.com/Runnin4ik/dpi-detector
- Documentation: https://github.com/Runnin4ik/dpi-detector/blob/main/README.md

### L0p4Map

Professional network monitoring & visualization tool. L0P4Map combines high-speed ARP discovery with full nmap integration and a real-time interactive network topology engine. Works on both local networks and custom I...

- GitHub: https://github.com/HaxL0p4/L0p4Map
- Documentation: https://github.com/HaxL0p4/L0p4Map/blob/main/README.md
- Topics: arp-scan, cybersecurity, hacking-tools, infosec, kali-linux, linux, network-scanner, network-visualization

### airgeddon

a multi-use bash script to audit wireless networks a multi-use bash script to audit wireless networks

- https://gitlab.com/parrotsec/packages/airgeddon

### asleap

A tool for exploiting Cisco LEAP networks Demonstrates a serious deficiency in proprietary Cisco LEAP networks.

- https://www.willhackforsushi.com/
- https://gitlab.com/parrotsec/packages/asleap

### broadcom-sta

Common files for the Broadcom STA Wireless driver Broadcom STA is a binary-only device driver to support the following IEEE 802.11a/b/g/n wireless network cards: BCM4311-, BCM4312-, BCM4313-, BCM4321-, BCM4322-, BCM43142-, BCM43224-, BCM43225-, BCM43227-, BCM43228-, BCM4331-, BCM4360-, and BCM4352-based hardware. This package contains the common files and it should not be installed manually (it will be installed automatically as needed).

- http://www.broadcom.com/support/802.11/linux_sta.php
- https://gitlab.com/parrotsec/packages/broadcom-sta

### calico

networking and network security solution for Kubernetes This package contains the command line tool for calico. Calico is a widely adopted, battle-tested open source networking and network security solution for Kubernetes, virtual machines, and bare-metal workloads.

- https://github.com/projectcalico/calico
- https://gitlab.com/parrotsec/packages/calico

### chisel

fast TCP/UDP tunnel over HTTP (program) This package contains a fast TCP/UDP tunnel, transported over HTTP, secured via SSH. Single executable including both client and server. Chisel is mainly useful for passing through firewalls, though it can also be used to provide a secure endpoint into your network.

- https://github.com/jpillora/chisel
- https://gitlab.com/parrotsec/packages/chisel

### cisco-ocs

Mass Cisco scanner A mass Cisco scanning tool.

- http://hacklab.altervista.org/
- https://gitlab.com/parrotsec/packages/cisco-ocs

### cryptcat

lightweight version netcat extended with twofish encryption Cryptcat is a simple Unix utility which reads and writes data across network connections, using TCP or UDP protocol while encrypting the data being transmitted. It is designed to be a reliable "back-end" tool that can be used directly or easily driven by other programs and scripts. At the same time, it is a feature-rich network debugging and exploration tool, since it can create almost any kind of connection you would need and has several interesting built-in capabilities.

- http://farm9.com/content/Free_Tools/cryptcat_linux2.tar
- https://gitlab.com/parrotsec/packages/cryptcat

### dhcplib

Pure-Python, spec-compliant DHCP-packet-processing library (Python 3) This package contains a fork of staticDHCPd’s libpydhcpserver aiming to provide Python 3 compatility and dropping decoupling it from a network API so you can use it with either sync or async networking libs. This package installs the library for Python 3.

- https://github.com/jansegre/dhcplib/
- https://gitlab.com/parrotsec/packages/dhcplib

### dnscat2

DNS tunnel (metapackage) This tool is designed to create an encrypted command-and-control (C&C) channel over the DNS protocol, which is an effective tunnel out of almost every network.

- https://github.com/iagox86/dnscat2
- https://gitlab.com/parrotsec/packages/dnscat2

### eaphammer

toolkit for targeted evil twin attacks against WPA2-Enterprise networks This package contains a toolkit for performing targeted evil twin attacks against WPA2-Enterprise networks. It is designed to be used in full scope wireless assessments and red team engagements. As such, focus is placed on providing an easy-to-use interface that can be leveraged to execute powerful wireless attacks with minimal manual configuration. To illustrate just how fast this tool is, the Quick Start section provides an example of how to execute a credential stealing evil twin attack against a WPA/2-EAP network in just commands.

- https://github.com/s0lst1c3/eaphammer
- https://gitlab.com/parrotsec/packages/eaphammer

### fern-wifi-cracker

Automated Wi-Fi cracker This package contains a Wireless security auditing and attack software program written using the Python Programming Language and the Python Qt GUI library, the program is able to crack and recover WEP/WPA/WPS keys and also run other network based attacks on wireless or ethernet based networks.

- https://github.com/savio-code/fern-wifi-cracker
- https://gitlab.com/parrotsec/packages/fern-wifi-cracker

### firejail

sandbox to restrict the application environment Firejail is a SUID security sandbox program that reduces the risk of security breaches by restricting the running environment of untrusted applications using Linux namespaces and seccomp-bpf. It allows a process and all its descendants to have their own private view of the globally shared kernel resources, such as the network stack, process table, mount table.

- https://firejail.wordpress.com
- https://gitlab.com/parrotsec/packages/firejail

### fragrouter

IDS evasion toolkit Fragrouter is a network intrusion detection evasion toolkit.

- http://www.anzen.com/research/nidsbench/fragrouter.html
- https://gitlab.com/parrotsec/packages/fragrouter

### golang-github-mwitkow-go-http-dialer

Go net.Dialer for HTTP(S) CONNECT Tunneling. (library) A net.Dialer drop-in that establishes the TCP connection over an HTTP CONNECT Tunnel (https://en.wikipedia.org/wiki/HTTP_tunnel#HTTP_CONNECT_tunneling). Some enterprises have fairly restrictive networking environments. They typically operate HTTP forward proxies (https://en.wikipedia.org/wiki/Proxy_server) that require user authentication. These proxies usually allow HTTPS (TCP to :443) to pass through the proxy using the CONNECT (https://tools.ietf.org/html/rfc2616#section-9.9) method. The CONNECT method is basically a HTTP-negotiated "end-to-end" TCP stream... which is exactly what net.Conn (https://golang.org/pkg/net/#Conn) is :)

- https://github.com/mwitkow/go-http-dialer
- https://gitlab.com/parrotsec/packages/golang-github-mwitkow-go-http-dialer

### hb-honeypot

Heartbleed Honeypot Script This Perl script listens on TCP port 443 and responds with completely bogus SSL heartbeat responses, unless it detects the start of a byte pattern similar to that used in Jared Stafford's (jspenguin@jspenguin.org) demo for CVE-2014-0160 'Heartbleed'. Run as root for the privileged port. Outputs IPs of suspected heartbleed scan to the console. Rickrolls scanner in the hex dump.

- https://packetstormsecurity.com/files/126068/Heartbleed-Honeypot-Script.html
- https://gitlab.com/parrotsec/packages/hb-honeypot

### hubble

Network, Service & Security Observability for Kubernetes using eBPF (program) Hubble is a fully distributed networking and security observability platform for cloud native workloads. It is built on top of Cilium (https://github.com/cilium/cilium) and eBPF (https://ebpf.io) to enable deep visibility into the communication and behavior of services as well as the networking infrastructure in a completely transparent manner.

- https://github.com/cilium/hubble
- https://gitlab.com/parrotsec/packages/hubble

### libcrafter

Library to generate and sniff network packets Libcrafter is a high level library for C++ designed to make easier the creation and decoding of network packets. It is able to craft or decode packets of most common network protocols, send them on the wire, capture them and match requests and replies. It enables the creation of networking tools in a few lines with an interface very similar to Scapy. A packet is described as layers that you stack one upon the other. Fields of each layer have useful default values that you can overload.

- https://github.com/pellegre/libcrafter
- https://gitlab.com/parrotsec/packages/libcrafter

### mitmproxy-wireguard

proxy any device that can be configured as a WireGuard client (Python 3) This package contains a Python module to proxy any device that can be configured as a WireGuard client. * multithreaded / asynchronous WireGuard server using tokio: - one worker thread for the user-space WireGuard server - one worker thread for the user-space network stack - one worker thread for communicating with the Python runtime * full support for IPv4 packets (TCP and UDP) * basic support for IPv6 packets (TCP and UDP) * partial support for IPv6 packets * Python interface similar to the Python asyncio module * integration tests in mitmproxy This package installs the library for Python 3.

- https://github.com/decathorpe/mitmproxy_wireguard
- https://gitlab.com/parrotsec/packages/mitmproxy-wireguard

### nbtscan-unixwiz

Scanner for open NETBIOS nameservers This package contains a command-line tool that scans for open NETBIOS nameservers on a local or remote TCP/IP network, and this is a first step in finding of open shares. It is based on the functionality of the standard Windows tool nbtstat, but it operates on a range of addresses instead of just one.

- http://unixwiz.net/tools/nbtscan.html
- https://gitlab.com/parrotsec/packages/nbtscan-unixwiz

### ncat-w32

Netcat for the 21st century Ncat is a feature-packed networking utility which reads and writes data across networks from the command line. Ncat was written for the Nmap Project as a much-improved reimplementation of the venerable Netcat. It uses both TCP and UDP for communication and is designed to be a reliable back-end tool to instantly provide network connectivity to other applications and users. Ncat will not only work with IPv4 and IPv6 but provides the user with a virtually limitless number of potential uses. Among Ncat’s vast number of features there is the ability to chain Ncats together, redirect both TCP and UDP ports to other sites, SSL support, and proxy connections via SOCKS4 or HTTP (CONNECT method) proxies (with optional proxy authentication as well). Some general principles apply to most applications and thus give you the capability of instantly adding networking support to software that would normally never support it.

- https://nmap.org/ncat/
- https://gitlab.com/parrotsec/packages/ncat-w32

### nikto

web server security scanner Nikto is a pluggable web server and CGI scanner written in Perl, using rfp's LibWhisker to perform fast security or informational checks. Features: - Easily updatable CSV-format checks database - Output reports in plain text or HTML - Available HTTP versions automatic switching - Generic as well as specific server software checks - SSL support (through libnet-ssleay-perl) - Proxy support (with authentication) - Cookies support

- https://github.com/sullo/nikto
- https://gitlab.com/parrotsec/packages/nikto

### nipper-ng

Device security configuration review tool Nipper-ng is the next generation of nippper, and will always remain free and open source. This software will be used to make observations about the security configurations of many different device types such as routers, firewalls, and switches of a network infrastructure. This is a fork from nipper 0.11.10 release of the GNUv3 GPL code.

- https://gitlab.com/parrotsec/packages/nipper-ng

### nmap

The Network Mapper Nmap is a utility for network exploration or security auditing. It supports ping scanning (determine which hosts are up), many port scanning techniques, version detection (determine service protocols and application versions listening behind ports), and TCP/IP fingerprinting (remote host OS or device identification). Nmap also offers flexible target and port specification, decoy/stealth scanning, sunRPC scanning, and more. Most Unix and Windows platforms are supported in both GUI and commandline modes. Several popular handheld devices are also supported, including the Sharp Zaurus and the iPAQ.

- https://nmap.org/
- https://gitlab.com/parrotsec/packages/nmap

### oracle-instantclient-basic

Oracle Instant Client Basic This package contains the Oracle Instant Client Basic. It enables applications to connect to a local or remote Oracle Database for development and production deployment. The Instant Client libraries provide the necessary network connectivity, as well as basic and high end data features, to make full use of Oracle Database.

- https://www.oracle.com/technetwork/database/database-technologies/instant-client/overview/index.html
- https://gitlab.com/parrotsec/packages/oracle-instantclient-basic

### pontos

Greenbone Python Utilities and Tools (common documentation) This package contains a collection of utilities, tools, classes and functions maintained by Greenbone Networks. Pontos is the German name of the Greek titan Pontus, the titan of the sea. This is the common documentation package.

- https://github.com/greenbone/pontos
- https://gitlab.com/parrotsec/packages/pontos

### powercat

netcat features all in powershell v2 This package contains a netcat powershell version. It's a simple utility which reads and writes data across network connections using DNS or UDP protocol.

- https://github.com/besimorhino/powercat
- https://gitlab.com/parrotsec/packages/powercat

### powershell-empire

PowerShell and Python post-exploitation agent This package contains a post-exploitation framework that includes a pure-PowerShell2.0 Windows agent, and a pure Python Linux/OS X agent. It is the merge of the previous PowerShell Empire and Python EmPyre projects. The framework offers cryptologically-secure communications and a flexible architecture. On the PowerShell side, Empire implements the ability to run PowerShell agents without needing powershell.exe, rapidly deployable post-exploitation modules ranging from key loggers to Mimikatz, and adaptable communications to evade network detection, all wrapped up in a usability-focused framework.

- https://github.com/BC-SECURITY/Empire
- https://gitlab.com/parrotsec/packages/powershell-empire

### python-ipwhois

Retrieve and parse whois data for IP addresses (common documentation) This package contains a library to retrieve and parse whois data for IPv4 and IPv6 addresses. * Parses a majority of whois fields in to a standard dictionary * Supports RDAP queries (recommended method, see: https://tools.ietf.org/html/rfc7483) * Proxy support for RDAP queries * Supports legacy whois protocol queries * Referral whois support for legacy whois protocol * Recursive network parsing for IPs with parent/children networks listed * National Internet Registry support for JPNIC and KRNIC * Supports IP to ASN and ASN origin queries * Full CLI for IPWhois with optional ANSI colored console output. This is the common documentation package.

- https://github.com/secynic/ipwhois
- https://gitlab.com/parrotsec/packages/python-ipwhois

### rebind

DNS rebinding tool Rebind is a tool that implements the multiple A record DNS rebinding attack. Although this tool was originally written to target home routers, it can be used to target any public (non RFC1918) IP address. Rebind provides an external attacker access to a target router's internal Web interface. This tool works on routers that implement the weak end system model in their IP stack, have specifically configured firewall rules, and who bind their Web service to the router's WAN interface. Note that remote administration does not need to be enabled for this attack to work. All that is required is that a user inside the target network surf to a Web site that is controlled, or has been compromised, by the attacker.

- https://gitlab.com/parrotsec/packages/rebind

### responder

LLMNR/NBT-NS/mDNS Poisoner This package contains Responder/MultiRelay, an LLMNR, NBT-NS and MDNS poisoner. It will answer to specific NBT-NS (NetBIOS Name Service) queries based on their name suffix (see: http://support.microsoft.com/kb/163409). By default, the tool will only answer to File Server Service request, which is for SMB. The concept behind this is to target your answers, and be stealthier on the network. This also helps to ensure that you don't break legitimate NBT-NS behavior. You can set the -r option via command line if you want to answer to the Workstation Service request name suffix.

- https://github.com/lgandx/Responder
- https://gitlab.com/parrotsec/packages/responder

### routersploit

Exploitation Framework for Embedded Devices This package contains an open-source exploitation framework dedicated to embedded devices. It consists of various modules that aids penetration testing operations: * exploits - modules that take advantage of identified vulnerabilities. * creds - modules designed to test credentials against network services. * scanners - modules that check if target is vulnerable to any exploit. * payloads - modules that are responsible for generating payloads for various architectures and injection points. * generic - modules that perform generic attacks.

- https://github.com/threat9/routersploit
- https://gitlab.com/parrotsec/packages/routersploit

### rtlsdr-scanner

simple spectrum analyser for scanning with a RTL-SDR compatible USB device A cross platform Python frequency scanning GUI for the OsmoSDR rtl-sdr library. The scanner attempts to overcome the tuner's frequency response by averaging scans from both the positive and negative frequency offsets of the baseband data.

- https://github.com/CdeMills/RTLSDR-Scanner
- https://gitlab.com/parrotsec/packages/rtlsdr-scanner

### ruby-cms-scanner

CMS Scanner Framework This package provides a quick and easy way to create a CMS/WebSite Scanner by acting like a Framework and providing classes, formatters etc.

- https://github.com/wpscanteam/CMSScanner
- https://gitlab.com/parrotsec/packages/ruby-cms-scanner

### s3scanner

tool to find open S3 buckets and dump their contents This package contains a tool to find open S3 buckets and dump their contents. The features are: * zap Multi-threaded scanning * telescope Supports tons of S3-compatible APIs * female_detective Scans all bucket permissions to find misconfigurations * floppy_disk Dump bucket contents to a local folder * whale Docker support

- https://github.com/sa7mon/s3scanner
- https://gitlab.com/parrotsec/packages/s3scanner

### sctpscan

SCTP network scanner for discovery and security SCTP network scanner for discovery and security

- https://github.com/philpraxis/sctpscan
- https://gitlab.com/parrotsec/packages/sctpscan

### socat

multipurpose relay for bidirectional data transfer Socat (for SOcket CAT) establishes two bidirectional byte streams and transfers data between them. Data channels may be files, pipes, devices (terminal or modem, etc.), or sockets (Unix, IPv4, IPv6, raw, UDP, TCP, SSL). It provides forking, logging and tracing, different modes for interprocess communication and many more options. It can be used, for example, as a TCP relay (one-shot or daemon), as an external socksifier, as a shell interface to Unix sockets, as an IPv6 relay, as a netcat and rinetd replacement, to redirect TCP-oriented programs to a serial line, or to establish a relatively secure environment (su and chroot) for running client or server shell scripts inside network connections. Socat supports sctp as of 1.7.0.

- https://www.dest-unreach.org/socat/
- https://gitlab.com/parrotsec/packages/socat

### spike

Network protocol fuzzer When you need to analyze a new network protocol for buffer overflows or similar weaknesses, the SPIKE is the tool of choice for professionals. While it requires a strong knowledge of C to use, it produces results second to none in the field.

- http://www.immunitysec.com/resources-freesoftware.shtml
- https://gitlab.com/parrotsec/packages/spike

### sslstrip

SSL/TLS man-in-the-middle attack tool sslstrip is a tool that transparently hijacks HTTP traffic on a network, watch for HTTPS links and redirects, and then map those links into look-alike HTTP links or homograph-similar HTTPS links. It also supports modes for supplying a favicon which looks like a lock icon, selective logging, and session denial.

- https://github.com/L1ghtn1ng/sslstrip
- https://gitlab.com/parrotsec/packages/sslstrip

### tetragon

eBPF-based Security Observability and Runtime Enforcement (tetra CLI) Cilium’s new Tetragon component enables powerful realtime, eBPF-based Security Observability and Runtime Enforcement. Tetragon detects and is able to react to security-significant events, such as: - Process execution events - System call activity - I/O activity including network & file access When used in a Kubernetes environment, Tetragon is Kubernetes-aware - that is, it understands Kubernetes identities such as namespaces, pods and so-on - so that security event detection can be configured in relation to individual workloads. This package contains the tool tetra CLI.

- https://github.com/cilium/tetragon
- https://gitlab.com/parrotsec/packages/tetragon

### tlssled

Evaluates the security of a target SSL/TLS (HTTPS) server TLSSLed is a Linux shell script whose purpose is to evaluate the security of a target SSL/TLS (HTTPS) web server implementation. It is based on sslscan, a thorough SSL/TLS scanner that is based on the openssl library, and on the "openssl s_client" command line tool. The current tests include checking if the target supports the SSLv2 protocol, the NULL cipher, weak ciphers based on their key length (40 or 56 bits), the availability of strong ciphers (like AES), if the digital certificate is MD5 signed, and the current SSL/TLS renegotiation capabilities.

- http://www.taddong.com/en/lab.html
- https://gitlab.com/parrotsec/packages/tlssled

### unicornscan

Userland distributed TCP/IP stack Unicornscan is a new information gathering and correlation engine built for and by members of the security research and testing communities. It was designed to provide an engine that is Scalable, Accurate, Flexible, and Efficient. It is released for the community to use under the terms of the GPL license. Benefits: Unicornscan is an attempt at a User-land Distributed TCP/IP stack. It is intended to provide a researcher a superior interface for introducing a stimulus into and measuring a response from a TCP/IP enabled device or network. Although it currently has hundreds of individual features, a main set of abilities include: - Asynchronous stateless TCP scanning with all variations of TCP Flags. - Asynchronous stateless TCP banner grabbing - Asynchronous protocol specific UDP Scanning (sending enough of a signature to elicit a response). - Active and Passive remote OS, application, and component identification by analyzing responses. - PCAP file logging and filtering - Relational database output - Custom module support - Customized data-set views

- http://www.unicornscan.org/
- https://gitlab.com/parrotsec/packages/unicornscan

### watobo

Semi-automated web application scanner WATOBO is intended to enable security professionals to perform highly efficient (semi-automated) web application security audits. It works like a local web proxy.

- https://sourceforge.net/projects/watobo/
- https://gitlab.com/parrotsec/packages/watobo

### whatmask

helper for network settings This package contains a small C program that will help you with network settings. Whatmask can work in two modes. The first mode is to invoke Whatmask with only a subnet mask as the argument. In this mode Whatmask will echo back the subnet mask in four formats, plus the number of useable addresses in the range. The second mode is to invoke Whatmask with any ip address within the subnet, followed by a slash ('/'), followed by the subnet mask in any format. Whatmask will echo back the following: - The netmask in the following formats: CIDR, Netmask, Netmask (Hex) Wildcard Bits - The Network Address - The Broadcast Address - The number of Usable IP Addresses - The First Usable IP Address - The Last Usable IP Address

- http://www.laffeycomputer.com/whatmask.html
- https://gitlab.com/parrotsec/packages/whatmask

### wifiphisher

Automated phishing attacks against Wi-Fi networks This package contains a security tool that mounts automated phishing attacks against Wi-Fi networks in order to obtain secret passphrases or other credentials. It is a social engineering attack that unlike other methods it does not include any brute forcing. It is an easy way for obtaining credentials from captive portals and third party login pages or WPA/WPA2 secret passphrases.

- https://github.com/sophron/wifiphisher
- https://gitlab.com/parrotsec/packages/wifiphisher


## Open Source Intelligence


### OpenOSINT

AI-powered OSINT agent with interactive REPL, MCP server, and CLI. 16 tools. Works with Claude, GPT-4, or local models. For authorized security research only.

- GitHub: https://github.com/OpenOSINT/OpenOSINT
- Official site: https://openosint.tech
- Documentation: https://github.com/OpenOSINT/OpenOSINT/blob/main/README.md
- Topics: ai-agent, anthropic, claude, cli, cybersecurity, holehe, llm, mcp

### pentest-ai

Offensive-security MCP server with 205 wrapped tools, 17 specialist agents, and 60 SPA-aware probes for OWASP Top 10. CLI + MCP, BYO LLM. No API key needed on MCP path.

- GitHub: https://github.com/0xSteph/pentest-ai
- Official site: https://pentestai.xyz
- Documentation: https://github.com/0xSteph/pentest-ai/blob/main/README.md
- Topics: ai-security, bug-bounty, claude, ctf, cybersecurity, exploit, exploit-chaining, hacking-tools

### autopentest-ai

Agentic pentesting MCP server that automates web application penetration testing using the OWASP Web Security Testing Guide and PortSwigger technique references, with role-specialized agents for discovery, exploitation, and reporting.

- GitHub: https://github.com/bhavsec/autopentest-ai
- Documentation: https://github.com/bhavsec/autopentest-ai/blob/main/README.md
- Topics: ai, cybersecurity, mcp, owasp, pentesting, security-testing, web-security
### OnionClaw

Provide AI agents with full Tor network access and dark web data through a zero-config OpenClaw skill or standalone tool.

- GitHub: https://github.com/christinminor459/OnionClaw
- Documentation: https://github.com/christinminor459/OnionClaw/blob/main/README.md
- Topics: ai-agents, hidden-services, llm, mcp-server, onion, openclaw, openclaw-skill, osint

### web-check

🕵️‍♂️ All-in-one OSINT tool for analysing any website

- GitHub: https://github.com/lissy93/web-check
- Official site: https://web-check.xyz
- Documentation: https://github.com/lissy93/web-check/blob/master/README.md
- Topics: osint, privacy, security, security-tools, sysadmin
### osint-namecheckers-list

A list of tools to search accounts by username

- GitHub: https://github.com/soxoj/osint-namecheckers-list
- Documentation: https://github.com/soxoj/osint-namecheckers-list/blob/master/README.md
- Topics: account-search, awesome-osint, awesome-osint-tools, namechecker, nickname-search, osint, osint-list, osint-resources

### maigret

Collect a dossier on a person by username from 3000+ sites

- GitHub: https://github.com/soxoj/maigret
- Official site: https://maigret.app
- Documentation: https://maigret.readthedocs.io/
- Topics: cli, cybersecurity, identification, information-gathering, infosec, investigation, open-source, osint
- Topics: osint-framework, osint-python, pentesting, python, python3, reconnaissance, redteam, scraping
- Topics: sherlock, social-network, socmint, username

### kitphishr

A tool designed to hunt for Phishing Kit source code

- GitHub: https://github.com/cybercdh/kitphishr
- Documentation: https://github.com/cybercdh/kitphishr/blob/main/README.md
- Topics: blue-team, golang, incident-response, osint, phishing, phishing-kit, security-tools, threat-intelligence

### phishing_catcher

Tool for monitoring certificate transparency logs to spot suspicious domains that may be related to phishing campaigns and brand impersonation.

- GitHub: https://github.com/x0rz/phishing_catcher
- Documentation: https://github.com/x0rz/phishing_catcher/blob/master/README.md
- Topics: certstream, phishing, phishing-detection, security, threat-intelligence

### dnstwist

Domain fuzzing engine that helps detect typo-squatting, phishing, and brand impersonation domains by generating and inspecting lookalike variations.

- GitHub: https://github.com/elceef/dnstwist
- Official site: https://dnstwist.it/
- Documentation: https://github.com/elceef/dnstwist/blob/master/README.md

### Phishing.Database

Community-maintained phishing domain and URL blocklist intended for detection, filtering, and defensive security operations.

- GitHub: https://github.com/mitchellkrogza/Phishing.Database
- Documentation: https://github.com/mitchellkrogza/Phishing.Database/blob/master/README.md
- Topics: blacklist, blocklist, phishing, threat-intelligence, url-blocklist

### mrphish

All In One Social Accounts Phishing With Otp Bypass In Termux.

A phishing toolkit commonly referenced in security research and malware analysis contexts. It is associated with social engineering pages targeting multiple online services and is often used as a sample in phishing-awareness and detection work.

- GitHub: https://github.com/noob-hackers/mrphish
- Documentation: https://github.com/noob-hackers/mrphish/blob/master/README.md
- Topics: blacklist, blocklist, phishing, threat-intelligence, url-blocklist
- threat_type: `phishing-kit`
- use_case: `defensive_analysis`
- tags: `phishing, social-engineering, credential-harvesting, ioc`

Note: 
- This is a dual-use artifact; should be handled strictly for analysis, detection, and security research
- Not intended for deployment, reuse, or operational activity

### haylxon

⚡ Blazing-fast tool to grab screenshots of your domain list right from terminal.

- GitHub: https://github.com/pwnwriter/haylxon
- Official site: https://hxn.pwnwriter.me
- Documentation: https://github.com/pwnwriter/haylxon/blob/main/README.md
- Topics: bug-hunting-tools, hactoberfest, osint, pwnwriter, rust, rustlang, screenshot-utility

### Void-Tools

Python terminal multitool — OSINT, network utilities, Rich TUI dashboard. Educational use only.

- GitHub: https://github.com/v0id4real/Void-Tools
- Documentation: https://github.com/v0id4real/Void-Tools/blob/main/README.md
- Topics: discord-joiner, discord-multi-tool, discord-multitool, discord-multitools, discord-nuke-bot, discord-nuker, discord-nukers, discord-raid
### Void-Tools-v2.0

Python terminal multitool — OSINT, Discord, web & network utilities. Rich TUI, 13 themes, remote updates. Educational use only.

- GitHub: https://github.com/V0id-v2/Void-Tools-v2.0
- Documentation: https://github.com/V0id-v2/Void-Tools-v2.0/blob/main/README.md
- Topics: discord-joiner, discord-multi-tool, discord-multitool, discord-multitools, discord-nuke-bot, discord-nuker, discord-nukers, discord-raid

### The-Pika-s-OSINT-ToolBox

A curated list of free OSINT tools ⚡️

- GitHub: https://github.com/passthesh3ll/The-Pika-s-OSINT-ToolBox
- Official site: https://pikaosint.pages.dev
- Documentation: https://github.com/passthesh3ll/The-Pika-s-OSINT-ToolBox/blob/main/README.md

### OSINT-for-countries-V2.0

OSINT resources and tools by country, structured for fact-checkers and digital profilers

- GitHub: https://github.com/paulpogoda/OSINT-for-countries-V2.0
- Official site: https://t.me/pavelbannikov
- Documentation: https://github.com/paulpogoda/OSINT-for-countries-V2.0/blob/main/README.md
- Topics: fact-checking, open-data, osint, osint-tools, profiling

### dpulse

DPULSE - Tool for complex approach to domain OSINT

- GitHub: https://github.com/OSINT-TECHNOLOGIES/dpulse
- Official site: https://pypi.org/project/dpulse/
- Documentation: https://github.com/OSINT-TECHNOLOGIES/dpulse/blob/main/README.md
- Topics: cybersecurity, cybersecurity-education, cybersecurity-tool, data-gathering, domain-analysis, google-dorking, information-gathering, information-security

### Ransomware-Tool-Matrix

A resource containing all the tools each ransomware gangs uses

- GitHub: https://github.com/BushidoUK/Ransomware-Tool-Matrix
- Official site: https://blog.bushidotoken.net/2024/08/the-ransomware-tool-matrix.html
- Documentation: https://github.com/BushidoUK/Ransomware-Tool-Matrix/blob/main/README.md
- Topics: cti, cybersecurity, detection-engineering, hacking, osint, ransomware, threat-hunting, threat-intelligence

### Awesome-Blackhat-Tools

A curated list of tools officially presented at Black Hat events

- GitHub: https://github.com/UCYBERS/Awesome-Blackhat-Tools
- Official site: https://ucybers.com
- Documentation: https://github.com/UCYBERS/Awesome-Blackhat-Tools/blob/master/README.md
- Topics: appsec, awesome-list, blackhat, blue-teaming, cybersecurity, defensive-security, forensics, hacker-tools

### OSINT-for-countries

Methodology, links, tools for OSINT in different countries

- GitHub: https://github.com/wddadk/OSINT-for-countries
- Documentation: https://github.com/wddadk/OSINT-for-countries/blob/main/README.md

### OSINT-BIBLE

A comprehensive 2026 guide to Open-Source Intelligence (OSINT): tools, methodologies, ethics, and techniques for responsible research and investigation.

- GitHub: https://github.com/frangelbarrera/OSINT-BIBLE
- Documentation: https://github.com/frangelbarrera/OSINT-BIBLE/blob/main/README.md
- Topics: cybersecurity, data-analysis, ethical-hacking, forensics, investigation, open-source-intelligence, osint, privacy

### misp-modules

Modules for expansion services, enrichment, import and export in MISP and other tools.

- GitHub: https://github.com/MISP/misp-modules
- Official site: http://misp.github.io/misp-modules
- Documentation: https://github.com/MISP/misp-modules/blob/main/README.md
- Topics: cti, domaintools, enrichment, expansion, misp, misp-modules, osint, passive-dns

### darkfox

CTI Cyber Threat Intelligence OSINT Dark Web Deep Web Research. Ransomware gang information gathering tool.

- GitHub: https://github.com/aryanguenthner/darkfox
- Documentation: https://github.com/aryanguenthner/darkfox/blob/main/README.md

### The-Black-Tiger

The Black Tiger is all in one OSINT Tool, which has the best methods to collect Information about something or someone just by few mouse clicks.

- GitHub: https://github.com/VirusZzHkP/The-Black-Tiger
- Documentation: https://github.com/VirusZzHkP/The-Black-Tiger/blob/main/README.md
- Topics: cybersecurity, cybersecurity-tools, email-osint, hacking, hacking-tools, information, information-gathering, linux

### E4GL30S1NT

E4GL30S1NT - Simple Information Gathering Tool

- GitHub: https://github.com/C0MPL3XDEV/E4GL30S1NT
- Official site: https://carminedev.it
- Documentation: https://github.com/C0MPL3XDEV/E4GL30S1NT/blob/main/README.md
- Topics: dorker, information-gathering, osint, osint-python, python, reversedns, reverseip, social-media

### Image-Research-OSINT

Learn how to research images and the tools, techniques & tradecraft required.

- GitHub: https://github.com/The-Osint-Toolbox/Image-Research-OSINT
- Documentation: https://github.com/The-Osint-Toolbox/Image-Research-OSINT/blob/main/README.md
- Topics: ai, exif-data-extraction, exif-metadata, face-recognition, image-forensics, photos, reverse-image-search, stock-images
### Social-Media-OSINT

Social Media OSINT collection containing - tools, techniques & tradecraft.

- GitHub: https://github.com/The-Osint-Toolbox/Social-Media-OSINT
- Documentation: https://github.com/The-Osint-Toolbox/Social-Media-OSINT/blob/main/README.md
- Topics: bluesky, dating-app, discord, facebook, instagram, kik, linkedin, mastadon
### People-Search-OSINT

Search tools to help you find people, focused towards UK resources.

- GitHub: https://github.com/The-Osint-Toolbox/People-Search-OSINT
- Documentation: https://github.com/The-Osint-Toolbox/People-Search-OSINT/blob/main/README.md
- Topics: data, data-aggregation, osint, people, privacy, search, searching

### GitSint

🕵️ OSINT Tool (github tracker)

- GitHub: https://github.com/N0rz3/GitSint
- Documentation: https://github.com/N0rz3/GitSint/blob/master/README.md
- Topics: email, github, github-tracker, infosec, open-source-intelligence, organization, osint, osint-python

### SoIG

OSINT Tool gets a range of information from an Instagram account 🛠

- GitHub: https://github.com/yezz123/SoIG
- Documentation: https://github.com/yezz123/SoIG/blob/master/README.md
- Topics: api, caption, information-gathering, instagram, instagram-osint, osint, osint-python, osint-tool

### arjun

HTTP parameter discovery suite This package can find query parameters for URL endpoints. Web applications use parameters (or queries) to accept user input, take the following example into consideration. http://api.example.com/v1/userinfo?id=751634589 This URL seems to load user information for a specific user id, but what if there exists a parameter named admin which when set to True makes the endpoint provide more information about the user? This is what Arjun does, it finds valid HTTP parameters with a huge default dictionary of 25,890 parameter names. It takes less than 10 seconds to go through this huge list while making just 50-60 requests to the target. Some features: - Supports GET/POST/POST-JSON/POST-XML requests; - Automatically handles rate limits and timeouts; - Export results to: BurpSuite, text or JSON file; - Import targets from: BurpSuite, text file or a raw request file; - Can passively extract parameters from JS or 3 external sources. Arjun is useful for penetration testing (PENTEST) and network security analysis, serving as OSINT.

- https://github.com/s0md3v/Arjun
- https://gitlab.com/parrotsec/packages/arjun

### maryam

OWASP Maryam is a modular/optional open source framework bas This package contains the OWASP Maryam, a modular/optional open source framework based on OSINT and data gathering. Maryam is written in Python programming language and it’s designed to provide a powerful environment to harvest data from open sources and search engines and collect data quickly and thoroughly.

- https://github.com/saeeddhqan/Maryam
- https://gitlab.com/parrotsec/packages/maryam


## AI Agent Security and Tooling


### VoltAgent

Open-source TypeScript AI agent framework with built-in support for guardrails, MCP integration, observability, memory, workflows, and evals. While it is broader than cybersecurity alone, it is relevant for secure agent engineering and agent runtime governance.

- GitHub: https://github.com/VoltAgent/voltagent
- Official site: https://voltagent.dev/
- Documentation: https://voltagent.dev/docs/
- LLM guide: https://voltagent.dev/llms.txt

### BoxPwnr

Modular framework for benchmarking LLMs and agentic strategies on security labs and CTF-style challenges across Hack The Box, PortSwigger Labs, picoCTF, TryHackMe, and similar platforms.

- GitHub: https://github.com/0ca/BoxPwnr
- Official site: https://boxpwnr.info/
- Documentation: https://github.com/0ca/BoxPwnr/blob/main/README.md

### taranis-ai

Taranis AI is an advanced Open-Source Intelligence (OSINT) tool, leveraging Artificial Intelligence to revolutionize information gathering and situational analysis.

- GitHub: https://github.com/taranis-ai/taranis-ai
- Official site: https://taranis.ai/
- Documentation: https://github.com/taranis-ai/taranis-ai/blob/master/README.md
- Topics: artificial-intelligence, cybersecurity, nlp, osint, secops

### D4rk_Intel-OSINT-Investigative-Toolkit

A curated toolkit for Open-Source Intelligence (OSINT) investigations. This repository contains a collection of scripts, resources, and methodologies to aid in gathering and analyzing publicly available information. D...

- GitHub: https://github.com/techenthusiast167/D4rk_Intel-OSINT-Investigative-Toolkit
- Documentation: https://github.com/techenthusiast167/D4rk_Intel-OSINT-Investigative-Toolkit/blob/main/README.md

## General Security


### SecToolKit

Cybersecurity tool repository / Wiki 收录常用 / 前沿 的CTF和渗透工具以及其 官方/使用 文档，致力于让每个工具都能发挥作用ww，不管你是萌新还是领域从业者希望你都能在这里找到适合你的工具或者获得一定的启发。

- GitHub: https://github.com/ProbiusOfficial/SecToolKit
- Official site: https://tool.tjsec.cn/
- Documentation: https://github.com/ProbiusOfficial/SecToolKit/blob/main/README.md
- Topics: ctf, ctf-tools, ctf-wiki, cyber-security, cyber-security-tool, cyber-security-wiki

### athena

Athena OS is a Arch/Nix-based distro focused on Cybersecurity. Learn, practice and enjoy with any hacking tool!

- GitHub: https://github.com/Athena-OS/athena
- Official site: https://athenaos.org
- Documentation: https://github.com/Athena-OS/athena/blob/main/README.md
- Topics: archlinux, athenaos, cybersecurity, hacking, infosec, learning, linux, os
### cset

Cybersecurity Evaluation Tool

- GitHub: https://github.com/cisagov/cset
- Documentation: https://github.com/cisagov/cset/blob/develop/README.md
- Topics: cset, security-audit

### raptor

Raptor turns Claude Code into a general-purpose AI offensive/defensive security agent. By using Claude.md and creating rules, sub-agents, and skills, and orchestrating security tool usage, we configure the agent for a...

- GitHub: https://github.com/gadievron/raptor
- Documentation: https://github.com/gadievron/raptor/blob/main/README.md
### Awesome-AI-Security

Curated resources, research, and tools for securing AI systems

- GitHub: https://github.com/TalEliyahu/Awesome-AI-Security
- Official site: https://www.linkedin.com/groups/14545517/
- Documentation: https://github.com/TalEliyahu/Awesome-AI-Security/blob/main/README.md
- Topics: artificial-intelligence, cybersecurity

### tldfinder

A streamlined tool for discovering private TLDs for security research.

- GitHub: https://github.com/projectdiscovery/tldfinder
- Documentation: https://github.com/projectdiscovery/tldfinder/blob/main/README.md
- Topics: hacktoberfest, tld-discovery, tldfinder
### ctf-tools

Some setup scripts for security research tools.

- GitHub: https://github.com/zardus/ctf-tools
- Documentation: https://github.com/zardus/ctf-tools/blob/master/README.md

### Awesome-LLM4Security

This project aims to consolidate and share high-quality resources and tools across the cybersecurity domain.

- GitHub: https://github.com/liu673/Awesome-LLM4Security
- Documentation: https://github.com/liu673/Awesome-LLM4Security/blob/main/README.md
- Topics: cybersecurity, llm, sec, security, security-tools, tools
### strykerapp

Magic tool for pentest from your android device!

- GitHub: https://github.com/zalexdev/strykerapp
- Documentation: https://github.com/zalexdev/strykerapp/blob/main/README.md
### nix-security-box

Tool set for Information security professionals and all others

- GitHub: https://github.com/fabaff/nix-security-box
- Official site: https://fabaff.github.io/nix-security-box/
- Documentation: https://github.com/fabaff/nix-security-box/blob/main/README.md
- Topics: nix, nixos, nixpkgs, offensive, offensive-security, pentest, pentest-tool, pentesting

### i-Haklab

i-Haklab is a hacking laboratory for Termux that contains open source tools for pentesting, scan/find vulnerabilities, explotation and post-explotation recommended by Ivam3 with automation hacking commands and many gu...

- GitHub: https://github.com/ivam3/i-Haklab
- Official site: https://ivam3.github.io
- Documentation: https://github.com/ivam3/i-Haklab/blob/master/README.md
- Topics: hacking, hacking-tools, termux

### attackgen

AttackGen is a cybersecurity incident response testing tool that leverages the power of large language models and the comprehensive MITRE ATT&CK framework. The tool generates tailored incident response scenarios based...

- GitHub: https://github.com/mrwadams/attackgen
- Documentation: https://github.com/mrwadams/attackgen/blob/main/README.md
### ScubaGoggles

SCuBA Secure Configuration Baselines and assessment tool for Google Workspace

- GitHub: https://github.com/cisagov/ScubaGoggles
- Official site: https://www.cisa.gov/resources-tools/services/secure-cloud-business-applications-scuba-project
- Documentation: https://github.com/cisagov/ScubaGoggles/blob/main/README.md
- Topics: cisa, cybersecurity, google, google-workspace, gws, opa, open-policy-agent, open-source

### security-suite

Open-source security suite for OSINT reconnaissance, web security testing, API security assessment, compliance checks, and AI-assisted analysis.

- GitHub: https://github.com/TheSecuredAnalyst/security-suite
- Documentation: https://github.com/TheSecuredAnalyst/security-suite/blob/main/README.md

### GraphQLer

🔍A cutting edge context aware GraphQL API fuzzing tool!

- GitHub: https://github.com/omar2535/GraphQLer
- Documentation: https://github.com/omar2535/GraphQLer/blob/main/README.md
- Topics: api, api-testing-framework, appsec, automated-testing, cybersecurity, fuzzing, graphql, llm-fuzzing

### gram

Gram is Klarna's own threat model diagramming tool

- GitHub: https://github.com/klarna-incubator/gram
- Documentation: https://github.com/klarna-incubator/gram/blob/main/README.md
- Topics: appsec, cybersecurity, infosec, threat-modeling

### automotive-skills-suite

100+ installable Claude skills covering Engineering areas such as, ISO 26262 functional safety, ISO/SAE 21434 cybersecurity, ISO 21448 SOTIF, AIAG-VDA quality (APQP/PPAP/FMEA), Automotive SPICE, and continuous improve...

- GitHub: https://github.com/jherrodthomas/automotive-skills-suite
- Documentation: https://github.com/jherrodthomas/automotive-skills-suite/blob/main/README.md
- Topics: apqp, aspice, automotive, autosar, engineering, fusa, hardware, software-engineering

### pentest-copilot

Pentest Copilot is an AI-powered browser based ethical hacking assistant tool designed to streamline pentesting workflows.

- GitHub: https://github.com/bugbasesecurity/pentest-copilot
- Official site: https://pentest.bugbase.ai
- Documentation: https://github.com/bugbasesecurity/pentest-copilot/blob/main/README.md
- Topics: ai, cybersecurity, cybersecurity-tools, llms, pentesting

### attack-flow

Attack Flow helps executives, SOC managers, and defenders easily understand how attackers compose ATT&CK techniques into attacks by developing a representation of attack flows, modeling attack flows for a small corpus...

- GitHub: https://github.com/center-for-threat-informed-defense/attack-flow
- Official site: https://ctid.io/flow
- Documentation: https://github.com/center-for-threat-informed-defense/attack-flow/blob/main/README.md
- Topics: ctid, cyber-threat-intelligence, cybersecurity, mitre-attack, threat-informed-defense

### Wonka

Wonka is a sweet Windows tool that extracts Kerberos tickets from the Local Security Authority (LSA) cache. Like finding a ticket, but for security research and penetration testing! 🎫

- GitHub: https://github.com/Shac0x/Wonka
- Documentation: https://github.com/Shac0x/Wonka/blob/main/README.md

### rawsec-cybersecurity-inventory

An inventory of tools and resources about CyberSecurity that aims to help people to find everything related to CyberSecurity.

- GitHub: https://github.com/noraj/rawsec-cybersecurity-inventory
- Official site: https://inventory.raw.pm
- Documentation: https://github.com/noraj/rawsec-cybersecurity-inventory/blob/master/README.md
- Topics: cyber, cyber-security, cyberdefense, cybersecurity, hacktoberfest, infosec, inventory, ressources

### Pentest-Tools-Collection

Curated cybersecurity resource discovered by the scheduled GitHub automation.

- GitHub: https://github.com/LuemmelSec/Pentest-Tools-Collection
- Documentation: https://github.com/LuemmelSec/Pentest-Tools-Collection/blob/main/README.md
### adscan

Active Directory pentesting tool for Linux. Automated Kerberoasting, AS-REP Roasting, ADCS/ESC exploitation, DCSync, BloodHound integration, and 40+ AD attack paths. ENS Alto / NIS2 / ISO 27001 compliance reports. No...

- GitHub: https://github.com/ADScanPro/adscan
- Official site: https://www.adscanpro.com/docs
- Topics: active-directory, active-directory-certificate-services, adcs, bloodhound, ctf, dcsync, enumeration, kerberoasting

### deadend-cli

Agentic pentest tooling. Currently achieving 81% (KIMI K2.5) on XBOW's benchmark in full black-box. Completely Self-hosted. Every model available on LiteLLM (Ollama, anthropic, openai...)

- GitHub: https://github.com/straylabs-ai/deadend-cli
- Documentation: https://github.com/straylabs-ai/deadend-cli/blob/main/README.md
- Topics: agentic-ai, ai, cybersecurity, cybersecurity-tools, offensive-security, pentesting, secure-coding

### athena-nix

Athena OS Nix configuration files focused on Cybersecurity. Learn, practice and enjoy with any hacking tool!

- GitHub: https://github.com/Athena-OS/athena-nix
- Official site: https://athenaos.org
- Documentation: https://github.com/Athena-OS/athena-nix/blob/main/README.md
- Topics: athenaos, cybersecurity, hacking, infosec, learning, linux, nix, nixos

### strix

Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.

- GitHub: https://github.com/usestrix/strix
- Official site: https://strix.ai
- Documentation: https://github.com/usestrix/strix/blob/main/README.md
- Topics: agents, ai-hacking, ai-penetration-testing, ai-pentesting, ai-security, artificial-intelligence, bug-bounty, code-quality

### 0trace

traceroute tool that can run within an existing TCP connection The package is traceroute tool that can be run within an existing, open TCP connection, therefore bypassing some types of stateful packet filters with ease.

- https://lcamtuf.coredump.cx
- https://gitlab.com/parrotsec/packages/0trace

### aadict

Auto-Attribute Dict (Python 3) This package contains a Python dict sub-class that allows attribute-style access to dict items, e.g. d.foo is equivalent to d['foo']. aadict also provides a few other helpful methods, such as pick and omit methods. Also, an aadict is more call chaining friendly (e.g. methods such as update return self) and is pickle'able. This package installs the library for Python 3.

- https://github.com/metagriffin/aadict
- https://gitlab.com/parrotsec/packages/aadict

### aardwolf

Asynchronous RDP/VNC client (Python 3) This package contains an Asynchronous RDP/VNC client. The features are: * Supports credssp auth via NTLM/Kerberos. * Built-in proxy client allows SOCKS/HTTP proxy tunneling without 3rd part software * PtH via CredSSP+Restricted admin mode * Scriptable Keyboard, Mouse input and Clipboard input/output * Can run in headless mode, no GUI required (read: no need for Qt) * Support for Duckyscript files to emulate keystrokes This package installs the library for Python 3.

- https://github.com/skelsec/aardwolf
- https://gitlab.com/parrotsec/packages/aardwolf

### aesedb

async parser for JET (Python 3) This package contains an async parser for JET. It mainly aims to provide an async parsing option for NTDS.dit database file for obtaining user secrets. It might also useful for parsing random JET databases. This package installs the library for Python 3.

- https://github.com/skelsec/aesedb
- https://gitlab.com/parrotsec/packages/aesedb

### aiocmd

Asyncio-based automatic CLI creation tool using prompt-toolkit This package contains asyncio-based automatic CLI creation tool using prompt-toolkit. This package installs the library for Python 3.

- https://github.com/KimiNewt/aiocmd
- https://gitlab.com/parrotsec/packages/aiocmd

### aioconsole

Asynchronous console and interfaces for asyncio (common documentation) This package contains an aynchronous console and interfaces for asyncio. It provides: * asynchronous equivalents to input, print, exec and code.interact * an interactive loop running the asynchronous Python console * a way to customize and run command line interface using argparse * stream support to serve interfaces instead of using standard streams * the apython script to access asyncio code at runtime without modifying the sources This is the common documentation package.

- https://github.com/vxgmichel/aioconsole
- https://gitlab.com/parrotsec/packages/aioconsole

### aiohttp-apispec

Package entry imported from the ParrotSec package index.

- https://github.com/maximdanilchenko/aiohttp-apispec
- https://gitlab.com/parrotsec/packages/aiohttp-apispec

### aiomultiprocess

Take a modern Python codebase to the next level of performance (Python 3) This package contains a simple interface, while running a full AsyncIO event loop on each child process, enabling levels of concurrency never before seen in a Python application. Each child process can execute multiple coroutines at once, limited only by the workload and number of cores available. This package installs the library for Python 3.

- https://gitlab.com/parrotsec/packages/aiomultiprocess

### aiosmb

Fully asynchronous SMB library (Python 3) This package contains a fully asynchronous SMB library. This package installs the library for Python 3.

- https://github.com/skelsec/aiosmb
- https://gitlab.com/parrotsec/packages/aiosmb

### aiowinreg

Registry hive parsing the async way (Python 3) This package contains a registry hive reader library implementing both async and regural parsing. This package installs the library for Python 3.

- https://github.com/skelsec/aiowinreg
- https://gitlab.com/parrotsec/packages/aiowinreg

### amap

next-generation scanning tool for pentesters AMAP stands for Application MAPper. It is a next-generation scanning tool for pentesters. It attempts to identify applications even if they are running on a different port than normal. It also identifies non-ascii based applications. This is achieved by sending trigger packets, and looking up the responses in a list of response strings.

- https://www.thc.org
- https://gitlab.com/parrotsec/packages/amap

### apache-users

Enumerate usernames on systems with Apache UserDir module This Perl script will enumerate the usernames on any system that uses Apache with the UserDir module.

- https://labs.portcullis.co.uk/downloads/
- https://gitlab.com/parrotsec/packages/apache-users

### apt

commandline package manager This package provides commandline tools for searching and managing as well as querying information about packages as a low-level access to all features of the libapt-pkg library. These include: * apt-get for retrieval of packages and information about them from authenticated sources and for installation, upgrade and removal of packages together with their dependencies * apt-cache for querying available information about installed as well as installable packages * apt-cdrom to use removable media as a source for packages * apt-config as an interface to the configuration settings * apt-extracttemplates is used by debconf to prompt for configuration questions before installation.

- https://gitlab.com/parrotsec/packages/apt

### ara-icon-theme

Ara icon theme for Parrot OS Ara is a modern freedesktop icon theme whose design is based around the use of bold colours and simple geometric shapes to compose icons. Each icon has been meticulously designed for pixel-perfect viewing. The icon theme has been forked from the Paper icon theme.

- https://github.com/parrotsec/ara-icon-theme
- https://gitlab.com/parrotsec/packages/ara-icon-theme

### arc4

small and insanely fast ARCFOUR (RC4) cipher implementation (Python 3) This package contains a small and insanely fast ARCFOUR (RC4) cipher implementation of Python: - Strongly focused on performance; entire source code is written in C. - Thread-safety; you can improve further performance with multi-threading. - Easily installable; single file with no dependency, pre-built wheels provided. This package installs the library for Python 3.

- https://github.com/manicmaniac/arc4
- https://gitlab.com/parrotsec/packages/arc4

### arkime

Package entry imported from the ParrotSec package index.

- https://arkime.com/
- https://gitlab.com/parrotsec/packages/arkime

### armitage

Cyber attack management for Metasploit Armitage is a scriptable red team collaboration tool for Metasploit that visualizes targets, recommends exploits, and exposes the advanced post- exploitation features in the framework.

- https://github.com/r00t0v3rr1d3/armitage
- https://gitlab.com/parrotsec/packages/armitage

### asn1tools

Package entry imported from the ParrotSec package index.

- https://github.com/eerimoq/asn1tools
- https://gitlab.com/parrotsec/packages/asn1tools

### asyauth

Unified authentication library (Python 3) This package contains an Unified Authentication library. This package installs the library for Python 3.

- https://github.com/skelsec/asyauth
- https://gitlab.com/parrotsec/packages/asyauth

### asysocks

Socks5 / Socks4 client and server library (Python 3) This package contains a Socks5 / Socks4 client and server Python library. This package installs the library for Python 3.

- https://github.com/skelsec/asysocks
- https://gitlab.com/parrotsec/packages/asysocks

### b374k

Package entry imported from the ParrotSec package index.

- https://github.com/b374k/b374k
- https://gitlab.com/parrotsec/packages/b374k

### badauth

Fork of asyauth for bloodyAD Unified authentication library, written in python. This is a fork made for use with bloodyAD This package installs the library for Python 3.

- https://github.com/CravateRouge/badauth
- https://gitlab.com/parrotsec/packages/badauth

### base-files

Parrot base system miscellaneous files This package contains the basic filesystem hierarchy of a Parrot system, and several important miscellaneous files, such as /etc/debian_version, /etc/host.conf, /etc/issue, /etc/motd, /etc/profile, and others, and the text of several common licenses in use on Debian systems.

- https://gitlab.com/parrotsec/packages/base-files

### bddisasm

The BitDefender disassembler The Bitdefender disassembler (bddisasm) is a lightweight, x86/x64 only instruction decoder. It is easy to integrate, easy to work with, it has no external dependencies, it is thread-safe, it allocates no memory at all, it works in virtually any environment (we use it inside user, kernel, hypervisor, on both Windows and Linux environments), and it provides lots of info regarding the decoded instructions, such as: operands (both explicit and implicit), access mode for each operand, CPUID feature flag, flags access, etc.

- https://github.com/bitdefender/bddisasm/
- https://gitlab.com/parrotsec/packages/bddisasm

### bed

Package entry imported from the ParrotSec package index.

- http://www.snake-basket.de
- https://gitlab.com/parrotsec/packages/bed

### berate-ap

Package entry imported from the ParrotSec package index.

- https://github.com/sensepost/berate_ap
- https://gitlab.com/parrotsec/packages/berate-ap

### bettercap-caplets

Bettercap scripts (caplets) and proxy modules This package contains Bettercap scripts (caplets) and proxy modules. The bettercap's interactive sessions can be scripted with .cap files, or caplets.

- https://github.com/bettercap/caplets
- https://gitlab.com/parrotsec/packages/bettercap-caplets

### betterlockscreen

Package entry imported from the ParrotSec package index.

- https://github.com/pavanjadhaw/betterlockscreen
- https://gitlab.com/parrotsec/packages/betterlockscreen

### bing-ip2hosts

Package entry imported from the ParrotSec package index.

- https://www.morningstarsecurity.com/research/bing-ip2hosts
- https://gitlab.com/parrotsec/packages/bing-ip2hosts

### bluelog

Package entry imported from the ParrotSec package index.

- http://www.digifail.com/software/bluelog.shtml
- https://gitlab.com/parrotsec/packages/bluelog

### blueman

Graphical bluetooth manager Blueman is a GTK+ bluetooth management utility for GNOME using bluez D-Bus backend.

- https://github.com/blueman-project/blueman
- https://gitlab.com/parrotsec/packages/blueman

### blueranger

Package entry imported from the ParrotSec package index.

- http://www.hackfromacave.com/projects/blueranger.html
- https://gitlab.com/parrotsec/packages/blueranger

### bluesnarfer

Package entry imported from the ParrotSec package index.

- http://www.alighieri.org/
- https://gitlab.com/parrotsec/packages/bluesnarfer

### bumblebee

NVIDIA Optimus support for Linux Bumblebee is an effort to make NVIDIA Optimus enabled laptops work in GNU/Linux systems. These laptops are built in such a way that the NVIDIA graphics card can be used on demand so that battery life is improved and temperature is kept low. It disables the discrete graphics card if no client is detected, and starts an X server making use of NVIDIA card if requested then let software GL implementations (such as VirtualGL) copy frames to the visible display that runs on the integrated graphics. The ability to use discrete graphics depends on the driver: open source nouveau and proprietary nvidia.

- https://launchpad.net/~bumblebee
- https://gitlab.com/parrotsec/packages/bumblebee

### busybox

Tiny utilities for small and embedded systems BusyBox combines tiny versions of many common UNIX utilities into a single small executable. It provides minimalist replacements for the most common utilities you would usually find on your desktop system (i.e., ls, cp, mv, mount, tar, etc.). The utilities in BusyBox generally have fewer options than their full-featured GNU cousins; however, the options that are included provide the expected functionality and behave very much like their GNU counterparts. This package installs the BusyBox binary but does not install symlinks for any of the supported utilities. Some of the utilities can be used in the system by installing the busybox-syslogd, udhcpc or udhcpd packages.

- http://www.busybox.net
- https://gitlab.com/parrotsec/packages/busybox

### cabby

TAXII client implementation from EclecticIQ (common documentation) This package contains a Python TAXII client implementation from EclecticIQ. This is the common documentation package.

- https://github.com/eclecticiq/cabby
- https://gitlab.com/parrotsec/packages/cabby

### calamares

distribution-independent installer framework Calamares is a distribution-independent installer framework. It provides a graphical installer that can be used with nearly any distribution. This package is suitable for live media on Debian-based systems, and won't be of any particular use on an already installed system. You will likely want to provide your own config files to match your distribution, reading the Calamares documentation will guide you through that process.

- https://github.com/calamares/calamares
- https://gitlab.com/parrotsec/packages/calamares

### calamares-settings-parrot

Parrot theme and settings for the Calamares Installer Calamares is a generic installer framework for Linux distributions. By default, it contains a set of boilerplate wording and images. This package provides the latest Parrot artwork as well as scripts that supports EFI installations.

- https://salsa.debian.org/live-team/calamares-settings-debian
- https://gitlab.com/parrotsec/packages/calamares-settings-parrot

### caldera

Package entry imported from the ParrotSec package index.

- https://github.com/mitre/caldera
- https://gitlab.com/parrotsec/packages/caldera

### cassandra

Package entry imported from the ParrotSec package index.

- https://cassandra.apache.org
- https://gitlab.com/parrotsec/packages/cassandra

### cdrom-detect

Package entry imported from the ParrotSec package index.

- https://gitlab.com/parrotsec/packages/cdrom-detect

### certgraph

tool to crawl the graph of certificate Alternate Names This package contains a tool to crawl the graph of certificate Alternate Names. CertGraph crawls SSL certificates creating a directed graph where each domain is a node and the certificate alternative names for that domain's certificate are the edges to other domain nodes. New domains are printed as they are found. In Detailed mode upon completion the Graph's adjacency list is printed. Crawling defaults to collecting certificate by connecting over TCP, however there are multiple drivers that can search Certificate Transparency logs. This tool was designed to be used for host name enumeration via SSL certificates, but it can also show you a "chain" of trust between domains and the certificates that re-used between them.

- https://github.com/lanrat/certgraph
- https://gitlab.com/parrotsec/packages/certgraph

### choose-mirror

Package entry imported from the ParrotSec package index.

- https://gitlab.com/parrotsec/packages/choose-mirror

### cilium-cli

Package entry imported from the ParrotSec package index.

- https://github.com/cilium/cilium-cli
- https://gitlab.com/parrotsec/packages/cilium-cli

### cisco-auditing-tool

Scans Cisco routers for vulnerabilities Perl script which scans cisco routers for common vulnerabilities.

- http://www.scrypt.net/
- https://gitlab.com/parrotsec/packages/cisco-auditing-tool

### cisco-global-exploiter

Simple and fast Cisco exploitation tool Cisco Global Exploiter (CGE), is an advanced, simple and fast security testing tool.

- http://www.blackangels.it
- https://gitlab.com/parrotsec/packages/cisco-global-exploiter

### cmseek

CMS Detection and Exploitation suite This package contains a CMS Detection and Exploitation suite. It scans WordPress, Joomla, Drupal and over 180 other CMSs. A content management system (CMS) manages the creation and modification of digital content. It typically supports multiple users in a collaborative environment.

- https://github.com/Tuhinshubhra/CMSeeK
- https://gitlab.com/parrotsec/packages/cmseek

### colorful

Package entry imported from the ParrotSec package index.

- https://github.com/timofurrer/colorful
- https://gitlab.com/parrotsec/packages/colorful

### convoc2

Command and Control infrastracture through Microsoft Teams convoC2 is a Command and Control infrastructure that allows Red Teamers to execute system commands on compromised hosts through Microsoft Teams. It infiltrates data into hidden span tags in Microsoft Teams messages and exfiltrates command outputs in Adaptive Cards image URLs, triggering out-of-bound requests to a C2 server.

- https://gitlab.com/parrotsec/packages/convoc2

### copy-router-config

Copies Cisco configs via SNMP This package copies configuration files from Cisco devices running SNMP.

- https://www.offsec.com
- https://gitlab.com/parrotsec/packages/copy-router-config

### cpe

Common Platform Enumeration for Python (common documentation) This package contains a Common Platform Enumeration for Python. CPE is a standardized method of describing and identifying classes of applications, operating systems, and hardware devices present among an enterprise's computing assets. This is the common documentation package.

- https://github.com/nilp0inter/cpe
- https://gitlab.com/parrotsec/packages/cpe

### crackle

Crack and decrypt BLE encryption crackle exploits a flaw in the BLE pairing process that allows an attacker to guess or very quickly brute force the TK (Temporary Key). With the TK and other data collected from the pairing process, the STK (Short Term Key) and later the LTK (Long Term Key) can be collected. With the STK and LTK, all communications between the master and the slave can be decrypted

- https://github.com/mikeryan/crackle
- https://gitlab.com/parrotsec/packages/crackle

### cri-tools

command line tool used for creating OCI images This package contains a series of debugging and validation tools for Kubelet CRI, which includes: - crictl: CLI for kubelet CRI. - critest: validation test suites for kubelet CRI.

- https://github.com/kubernetes-sigs/cri-tools
- https://gitlab.com/parrotsec/packages/cri-tools

### cti-taxii-client

minimal client implementation for the TAXII 2.X server (common documentation) This package contains a minimal client implementation for the TAXII 2.X server. It supports the following TAXII 2.X API services: - Server Discovery - Get API Root Information - Get Status - Get Collections - Get a Collection - Get Objects - Add Objects - Get an Object - Delete an Object (2.1 only) - Get Object Manifests - Get Object Versions (2.1 only) This is the common documentation package.

- https://github.com/oasis-open/cti-taxii-client
- https://gitlab.com/parrotsec/packages/cti-taxii-client

### ctypescrypto

interface to some openssl functions based on ctypes module (Python 3) This package contains a Python interface to some openssl function based on ctypes module. This package installs the library for Python 3.

- https://github.com/vbwagner/ctypescrypto
- https://gitlab.com/parrotsec/packages/ctypescrypto

### cupid-wpa

Package entry imported from the ParrotSec package index.

- https://github.com/lgrangeia/cupid/
- https://gitlab.com/parrotsec/packages/cupid-wpa

### cymothoa

Stealth backdooring tool Cymothoa is a stealth backdooring tool, that inject backdoor's shellcode into an existing process. The tool uses the ptrace library (available on nearly all * nix), to manipulate processes and infect them.

- https://cymothoa.sourceforge.net/
- https://gitlab.com/parrotsec/packages/cymothoa

### dbus

simple interprocess messaging system (system message bus) D-Bus is a message bus, used for sending messages between applications. Conceptually, it fits somewhere in between raw sockets and CORBA in terms of complexity. D-Bus supports broadcast messages, asynchronous messages (thus decreasing latency), authentication, and more. It is designed to be low-overhead; messages are sent using a binary protocol, not using XML. D-Bus also supports a method call mapping for its messages, but it is not required; this makes using the system quite simple. It comes with several bindings, including GLib, Python, Qt and Java. This package provides a fully-functional D-Bus system bus with activation support, used for communication between system services, and depends on most of the other components of the reference implementation of D-Bus. To provide a complete D-Bus session bus, install one of the packages that implement the dbus-session-bus virtual package, such as dbus-user-session. The recommended implementation is indicated by the default-dbus-session-bus virtual package.

- https://dbus.freedesktop.org/
- https://gitlab.com/parrotsec/packages/dbus

### debian-cd

Tools for building (Official) Debian CD set Debian-cd is the official tool for building Debian CD set since the potato release. It was formerly called YACS (for Yet Another CD Script). Its goal is to facilitate the creation of customized Debian CD sets.

- https://gitlab.com/parrotsec/packages/debian-cd

### debian-installer

Debian Installer documentation This package currently only contains some documentation for the Debian installer. We welcome suggestions about what else to put in it.

- https://gitlab.com/parrotsec/packages/debian-installer

### desktop-base

common files for the Parrot Desktop This package contains various miscellaneous files which are used by Debian Desktop installations. Currently, it provides some Debian-related artwork and themes, .desktop files containing links to Debian related material (suitable for placement on a user's desktop), and other common files between the available desktop environments such as GNOME and KDE.

- https://www.debian.org/devel/debian-desktop/
- https://gitlab.com/parrotsec/packages/desktop-base

### device-pharmer

Search Shodan results and test credentials Concurrently open either Shodan search results, a specified IP, IP range, or domain and print the status and title of the page if applicable. Add the -u and -p options to attempt to login to the page first looking for a form login and failing that, attempt HTTP Basic Auth. Use -f SEARCHSTRING to look for a certain string in the html response in order to test if authentication succeeded. Logs all devices that respond using either the Shodan search term or the target IPs/domain + _results.txt. One caveat with searching the response page's HTML is that some form login pages return a JSON object response after an authentication request rather than the post-login page's HTML source. Often you can determine whether or not you were successful by just using -f "success" Default timeout on the requests is 12 seconds. Sends batches of 1000 requests concurrently which can be adjust using the -c option. One should note that Shodan only allows the first page of results (100 hosts) if you are using their free API key. If you have their professional API key you can specify the number of search result pages to test with the -n NUMBER_OF_PAGES argument. By default it will only check page 1.

- https://github.com/DanMcInerney/device_pharmer/
- https://gitlab.com/parrotsec/packages/device-pharmer

### die-engine

A program for determining types of files. "DIE" - Detect-It-Easy, is a cross-platform application that determines the type of file, and then sequentially loads all the signatures, which lie in the corresponding folder. Currently the program defines the following types: - MSDOS executable files MS-DOS - PE executable files Windows - ELF executable files Linux - MACH executable files Mac OS - Binary all other files

- https://horsicq.github.io/
- https://gitlab.com/parrotsec/packages/die-engine

### dissect.cstruct

Dissect module implementing a parser for C-like structures (Python 3) This package contains a Dissect module implementing a parser for C-like structures. Structure parsing in Python made easy. With cstruct, you can write C-like structures and use them to parse binary data, either as file-like objects or bytestrings. Parsing binary data with cstruct feels familiar and easy. No need to learn a new syntax or the quirks of a new parsing library before you can start parsing data. The syntax isn't strict C but it's compatible with most common structure definitions. You can often use structure definitions from open-source C projects and use them out of the box with little to no changes. Need to parse an EXT4 super block? Just copy the structure definition from the Linux kernel source code. Need to parse some custom file format? Write up a simple structure and immediately start parsing data, tweaking the structure as you go. This package installs the library for Python 3.

- https://github.com/fox-it/dissect.cstruct
- https://gitlab.com/parrotsec/packages/dissect.cstruct

### django-fieldsignals

help to tell when the fields on your model have changed (Python 3) This package contains django-fieldsignals: it simply makes it easy to tell when the fields on your model have changed. This package installs the library for Python 3.

- https://github.com/craigds/django-fieldsignals
- https://gitlab.com/parrotsec/packages/django-fieldsignals

### django-ratelimit

Package entry imported from the ParrotSec package index.

- https://github.com/jsocol/django-ratelimit
- https://gitlab.com/parrotsec/packages/django-ratelimit

### django-tagulous

tagging lib for Django built on ForeignKey and ManyToManyField (common documentation) This package contains a tagging library for Django built on ForeignKey and ManyToManyField, giving you all their normal power with a sprinkling of tagging syntactic sugar. - Easy to install - simple requirements, simple syntax, lots of options - Based on ForeignKey and ManyToManyField, so it's easy to query - Autocomplete support built in, if you want it - Supports multiple independent tag fields on a single model - Can be used as a user-customisable CharField with choices - Supports trees of nested tags, for detailed categorisation - Admin support for managing tags and tagged models This is the common documentation package.

- https://github.com/radiac/django-tagulous
- https://gitlab.com/parrotsec/packages/django-tagulous

### django-watson

fast multi-model full-text search plugin for Django (Python 3) This package contains a fast multi-model full-text search plugin for Django. It provides high quality search results. This package installs the library for Python 3.

- https://github.com/etianen/django-watson
- https://gitlab.com/parrotsec/packages/django-watson

### dpkg

Debian package management system This package provides the low-level infrastructure for handling the installation and removal of Debian software packages. For Debian package development tools, install dpkg-dev.

- https://wiki.debian.org/Teams/Dpkg
- https://gitlab.com/parrotsec/packages/dpkg

### dradis

Collaboration tools for penetration testing Dradis is a tool to help in the process of penetration testing. Penetration testing is about information: 1. Information discovery 2. Exploit useful information 3. Report the findings But penetration testing is also about sharing the information you and your teammates gather. Not sharing the information available in an effective way will result in exploitation oportunities lost and the overlapping of efforts.

- https://dradisframework.org
- https://gitlab.com/parrotsec/packages/dradis

### dronekit

helper to create powerful apps for UAVs (Python 3) This package contains the Python language implementation of DroneKit. The API allows developers to create Python apps that communicate with vehicles over MAVLink. It provides programmatic access to a connected vehicle's telemetry, state and parameter information, and enables both mission management and direct control over vehicle movement and operations. The API is primarily intended for use in onboard companion computers (to support advanced use cases including computer vision, path planning, 3D modelling etc). It can also be used for ground station apps, communicating with vehicles over a higher latency RF-link. This package installs the library for Python 3.

- https://github.com/dronekit/dronekit-python
- https://gitlab.com/parrotsec/packages/dronekit

### dscan

wrapper around nmap This package provides a wrapper around nmap, and distribute scans across several hosts. It aggregates / splits address ranges, uses a configuration file where scan configuration can be adjusted, supports resume.

- https://github.com/0x4E0x650x6F/dscan
- https://gitlab.com/parrotsec/packages/dscan

### dsnap

Package entry imported from the ParrotSec package index.

- https://github.com/RhinoSecurityLabs/dsnap
- https://gitlab.com/parrotsec/packages/dsnap

### dumpsterdiver

Package entry imported from the ParrotSec package index.

- https://github.com/securing/DumpsterDiver
- https://gitlab.com/parrotsec/packages/dumpsterdiver

### dwarf2json

Package entry imported from the ParrotSec package index.

- https://github.com/volatilityfoundation/dwarf2json
- https://gitlab.com/parrotsec/packages/dwarf2json

### echo-themes

Echo, the default theme for ParrotOS 7 Available on KDE, it comes bundled with Echo wallpapers.

- https://parrotsec.org
- https://gitlab.com/parrotsec/packages/echo-themes

### edb-debugger

cross platform x86/x86-64 debugger edb is a graphical cross platform x86/x86-64 debugger. It was inspired by Ollydbg, but aims to function on x86 and x86-64 as well as multiple OS's. Linux is the only officially supported platform at the moment, but FreeBSD, OpenBSD, OSX and Windows ports are underway with varying degrees of functionality.

- https://github.com/eteran/edb-debugger
- https://gitlab.com/parrotsec/packages/edb-debugger

### enum4linux-ng

Next generation version of enum4linux A rewrite of Mark Lowe's (former Portcullis Labs now Cisco CX Security Labs) enum4linux.pl, a tool for enumerating information from Windows and Samba systems, aimed for security professionals and CTF players. The tool is mainly a wrapper around the Samba tools nmblookup, net, rpcclient and smbclient

- https://github.com/cddmp/enum4linux-ng
- https://gitlab.com/parrotsec/packages/enum4linux-ng

### exe2hexbat

Convert EXE to bat A Python script to convert a Windows PE executable file to a batch file and vice versa.

- https://github.com/g0tmi1k/exe2hex/
- https://gitlab.com/parrotsec/packages/exe2hexbat

### exploitdb

Searchable Exploit Database archive Searchable archive from The Exploit Database. https://www.exploit-db.com/

- https://www.exploit-db.com
- https://gitlab.com/parrotsec/packages/exploitdb

### exploitdb-bin-sploits

The Exploit Database's archive of binary exploits Searchable binary exploits from The Exploit Database. https://www.exploit-db.com

- https://www.exploit-db.com
- https://gitlab.com/parrotsec/packages/exploitdb-bin-sploits

### exploitdb-papers

The Exploit Database's archive of papers & ezines Searchable papers & ezines archives from The Exploit Database. https://www.exploit-db.com/papers

- https://www.exploit-db.com
- https://gitlab.com/parrotsec/packages/exploitdb-papers

### fake-useragent

Package entry imported from the ParrotSec package index.

- https://github.com/hellysmile/fake-useragent
- https://gitlab.com/parrotsec/packages/fake-useragent

### faraday-agent-dispatcher

Package entry imported from the ParrotSec package index.

- https://github.com/infobyte/faraday_agent_dispatcher
- https://gitlab.com/parrotsec/packages/faraday-agent-dispatcher

### faraday-agent-parameters-types

Set the models of parameters types for the agents (Python 3) This module sets the models of parameters types for the agents: - How to pass them by identifier strings - How to encode/decode them to pass data between the Faraday server and the agents dispatcher This package installs the library for Python 3.

- https://github.com/infobyte/faraday_agent_parameters_types
- https://gitlab.com/parrotsec/packages/faraday-agent-parameters-types

### faraday-cli

Package entry imported from the ParrotSec package index.

- https://github.com/infobyte/faraday-cli
- https://gitlab.com/parrotsec/packages/faraday-cli

### faraday-plugins

Faraday plugins (Python 3) This package contains plugins for the python-faraday package. This package installs the library for Python 3.

- https://github.com/infobyte/faraday_plugins
- https://gitlab.com/parrotsec/packages/faraday-plugins

### fiked

Cisco VPN attack tool FakeIKEd, or fiked for short, is a fake IKE daemon supporting just enough of the standards and Cisco extensions to attack commonly found insecure Cisco VPN PSK+XAUTH based IPsec authentication setups in what could be described as a semi MitM attack. Fiked can impersonate a VPN gateway’s IKE responder in order to capture XAUTH login credentials; it doesn’t currently do the client part of full MitM.

- https://www.roe.ch/FakeIKEd
- https://gitlab.com/parrotsec/packages/fiked

### firmware-mod-kit

Package entry imported from the ParrotSec package index.

- https://github.com/rampageX/firmware-mod-kit
- https://gitlab.com/parrotsec/packages/firmware-mod-kit

### flask-jsglue

helps hook up your Flask application with the front end (Python 3) This package contains a Python module that helps hook up your Flask application nicely with the front end. This package installs the library for Python 3.

- https://github.com/stewartpark/Flask-JSGlue
- https://gitlab.com/parrotsec/packages/flask-jsglue

### fleep

File format determination library (Python 3) This package contains a library that determines file format by file signature (also known as "magic number"). This package installs the library for Python 3.

- https://github.com/floyernick/fleep-py
- https://gitlab.com/parrotsec/packages/fleep

### fpdf

Package entry imported from the ParrotSec package index.

- https://pyfpdf.github.io/fpdf2/
- https://gitlab.com/parrotsec/packages/fpdf

### framework2

Metasploit Framework 2 Version 2 of the Metasploit Framework. No longer updated but still useful, particularly for shellcode.

- https://www.metasploit.com
- https://gitlab.com/parrotsec/packages/framework2

### freeradius-wpe

FreeRadius Wireless Pawn Edition This package is FreeRadius Wireless Pawn Edition. There are supported and tested EAP Types/Inner Authentication Methods (others may also work): * PEAP/PAP (OTP) * PEAP/MSCHAPv2 * EAP-TTLS/PAP (includes OTPs) * EAP-TTLS/MSCHAPv1 * EAP-TTLS/MSCHAPv2 * EAP-MD5

- https://www.freeradius.org/
- https://gitlab.com/parrotsec/packages/freeradius-wpe

### ftester

Tool for testing firewalls and Intrusion Detection System (IDS) The Firewall Tester (FTester) is a tool designed for testing firewall filtering policies and Intrusion Detection System (IDS) capabilities. Features: * firewall testing * IDS testing * simulation of real tcp connections for stateful inspection firewalls and IDS * TCP connection spoofing * IP fragmentation / TCP segmentation * IDS evasion techniques

- https://dev.inversepath.com/ftester/
- https://gitlab.com/parrotsec/packages/ftester

### fxscintilla

Implementation of Scintilla for the FOX GUI Library This package contains the development files of fxscintilla, an implementation of Scintilla for the FOX GUI Library. The FOX GUI toolkit is a platform independent GUI library developed by Jeroen van der Zijp. For more information about FOX, see http://fox-toolkit.org.

- https://savannah.gnu.org/projects/fxscintilla/
- https://gitlab.com/parrotsec/packages/fxscintilla

### gdb-peda

Python Exploit Development Assistance for GDB This package contains a Python GDB script with many handy commands to help speed up exploit development process on Linux/Unix. It is also a framework for writing custom interactive Python GDB commands.

- https://github.com/longld/peda
- https://gitlab.com/parrotsec/packages/gdb-peda

### geany

fast and lightweight IDE Geany is a small and lightweight integrated development environment. It was developed to provide a small and fast IDE, which has only a few dependencies from other packages. It is using only the GTK3 toolkit and therefore you need only the GTK3 runtime libraries to run Geany. The basic features of Geany are: - syntax highlighting - code completion - auto completion of constructs like if, for and while, XML and HTML - call tips - folding - many supported filetypes like C, Java, PHP, HTML, Python, Perl, Pascal - symbol lists - embedded terminal emulation

- http://www.geany.org
- https://gitlab.com/parrotsec/packages/geany

### getallurls

fetch known URLs from AlienVault's Open Threat Exchange (gau) This package contains getallurls (gau). It fetches known URLs from AlienVault's Open Threat Exchange (https://otx.alienvault.com), the Wayback Machine, and Common Crawl for any given domain. Inspired by Tomnomnom's waybackurls.

- https://github.com/lc/gau
- https://gitlab.com/parrotsec/packages/getallurls

### ghidra-data

FID databases for Ghidra This package contains FID databases and data type archives that improve Ghidra.

- https://github.com/NationalSecurityAgency/ghidra-data
- https://gitlab.com/parrotsec/packages/ghidra-data

### gintro

The development files for GTK in Nim language. This package contains modules of GTK binding for developing with GTK framework.

- https://github.com/StefanSalewski/gintro/
- https://gitlab.com/parrotsec/packages/gintro

### globre

Glob-Like Pattern Matching (Python 3) This package contains a module to convert a glob-matching pattern to a regular expression, using Apache Cocoon style rules (with some extensions). This package installs the library for Python 3.

- https://github.com/metagriffin/globre
- https://gitlab.com/parrotsec/packages/globre

### golang-github-akamensky-argparse

Argparse for golang (library) This package contains an Argpars library in Go. The goal of this project is to bring ease of use and flexibility of argparse to Go. Which is where the name of this package comes from.

- https://github.com/akamensky/argparse
- https://gitlab.com/parrotsec/packages/golang-github-akamensky-argparse

### golang-github-antchfx-htmlquery

XPath package for HTML query (library) htmlquery is an XPath query package for HTML, letting you extract data or evaluate from HTML documents by an XPath expression.

- https://github.com/antchfx/htmlquery
- https://gitlab.com/parrotsec/packages/golang-github-antchfx-htmlquery

### golang-github-binject-debug

debug lib with additional functionalities This package is a fork of the debug/ folder from the standard library, to take direct control of the debug/elf, debug/macho, and debug/pe binary format parsers. The ability to also generate executable files from the parsed intermediate data structures has been added to these parsers. This lets load a file with debug parsers, make changes by interacting with the parser structures, and then write those changes back out to a new file.

- https://github.com/Binject/debug
- https://gitlab.com/parrotsec/packages/golang-github-binject-debug

### golang-github-binject-go-donut

Package entry imported from the ParrotSec package index.

- https://github.com/Binject/go-donut
- https://gitlab.com/parrotsec/packages/golang-github-binject-go-donut

### golang-github-cretz-gopaque

Package entry imported from the ParrotSec package index.

- https://github.com/cretz/gopaque
- https://gitlab.com/parrotsec/packages/golang-github-cretz-gopaque

### golang-github-domainr-whois

Package entry imported from the ParrotSec package index.

- https://github.com/domainr/whois
- https://gitlab.com/parrotsec/packages/golang-github-domainr-whois

### golang-github-domainr-whoistest

Package entry imported from the ParrotSec package index.

- https://github.com/domainr/whoistest
- https://gitlab.com/parrotsec/packages/golang-github-domainr-whoistest

### golang-github-go-git-go-git-v5

Package entry imported from the ParrotSec package index.

- https://github.com/go-git/golang-github-go-git-go-git-v5
- https://gitlab.com/parrotsec/packages/golang-github-go-git-go-git-v5

### golang-github-haccer-available

Package entry imported from the ParrotSec package index.

- https://github.com/mgutz/logxi
- https://gitlab.com/parrotsec/packages/golang-github-haccer-available

### golang-github-hako-durafmt

Better time duration formatting in Go! (library) This package contains a tiny Go library that formats time.Duration strings (and types) into a human readable format.

- https://github.com/hako/durafmt
- https://gitlab.com/parrotsec/packages/golang-github-hako-durafmt

### golang-github-jawher-mow.cli

versatile library for building CLI applications in Go (library) This package provides a framework to build command line applications in Go with most of the burden of arguments parsing and validation placed on the framework instead of the user.

- https://github.com/jawher/mow.cli
- https://gitlab.com/parrotsec/packages/golang-github-jawher-mow.cli

### golang-github-jpillora-ansi

Easy to use ANSI control codes (library) This package implements the ANSI VT100 control set.

- https://github.com/jpillora/ansi
- https://gitlab.com/parrotsec/packages/golang-github-jpillora-ansi

### golang-github-jpillora-requestlog

Simple request logging in Go (library) This package contains a simple request logging in Go (Golang).

- https://github.com/jpillora/requestlog
- https://gitlab.com/parrotsec/packages/golang-github-jpillora-requestlog

### golang-github-jpillora-sizestr

Pretty print byte counts in Go (library) This package contains a print byte counts in Go. It converts 231938 into 232KB.

- https://github.com/jpillora/sizestr
- https://gitlab.com/parrotsec/packages/golang-github-jpillora-sizestr

### golang-github-kennygrant-sanitize

functions for sanitizing text in golang strings This package contains functions to sanitize html and paths with go (golang).

- https://github.com/kennygrant/sanitize
- https://gitlab.com/parrotsec/packages/golang-github-kennygrant-sanitize

### golang-github-m-mizutani-urlscan-go

urlscan.io client library in Go (library) The package provides a API client of urlscan.io (https://urlscan.io) in Go.

- https://github.com/m-mizutani/urlscan-go
- https://gitlab.com/parrotsec/packages/golang-github-m-mizutani-urlscan-go

### golang-github-oxffaa-gopher-parse-sitemap

lib for parsing big-sized sitemaps and avoiding high memory usage This package contains a high effective golang library for parsing big-sized sitemaps and avoiding high memory usage.

- https://github.com/oxffaa/gopher-parse-sitemap
- https://gitlab.com/parrotsec/packages/golang-github-oxffaa-gopher-parse-sitemap

### golang-github-projectdiscovery-gologger

simple layer for leveled logging in go (library) gologger is a very simple logger for fast logging in simple command line tools.

- https://github.com/projectdiscovery/gologger
- https://gitlab.com/parrotsec/packages/golang-github-projectdiscovery-gologger

### golang-github-tomasen-realip

get client's real public ip address from http request headers This package can be used to get client's real public IP, which usually useful for logging HTTP server.

- https://github.com/tomasen/realip
- https://gitlab.com/parrotsec/packages/golang-github-tomasen-realip

### golang-github-tomnomnom-linkheader

HTTP Link header parser Package linkheader provides functions for parsing HTTP Link headers.

- https://github.com/tomnomnom/linkheader
- https://gitlab.com/parrotsec/packages/golang-github-tomnomnom-linkheader

### golang-go.dedis-fixbuf

Fixed length binary encoding of arbitrary structures in Go This package contains a fixed length binary encoding of arbitrary structures in Go.

- https://github.com/dedis/fixbuf
- https://gitlab.com/parrotsec/packages/golang-go.dedis-fixbuf

### golang-go.dedis-kyber

Package entry imported from the ParrotSec package index.

- https://github.com/dedis/kyber
- https://gitlab.com/parrotsec/packages/golang-go.dedis-kyber

### golang-go.dedis-protobuf

Reflection-based Protocol Buffers for Go (library) This package implements Protocol Buffers reflectively using Go types to define message formats. This approach provides convenience similar to Gob encoding, but with a widely-used and language-neutral wire format.

- https://github.com/dedis/protobuf
- https://gitlab.com/parrotsec/packages/golang-go.dedis-protobuf

### goofile

Command line filetype search Use this tool to search for a specific file type in a given domain.

- https://github.com/sosukeinu/goofile
- https://gitlab.com/parrotsec/packages/goofile

### google-nexus-tools

ADB and Fastboot for use with Nexus devices Nexus Tools is an installer for the Android debug/development command-line tools ADB (Android Device Bridge) and Fastboot for Mac OS X, Linux, and Google Chrome/Chromium OS.

- https://github.com/corbindavenport/nexus-tools
- https://gitlab.com/parrotsec/packages/google-nexus-tools

### gophish

Open-Source Phishing Toolkit This package contains an open-source phishing toolkit designed for businesses and penetration testers. It provides the ability to quickly and easily setup and execute phishing engagements and security awareness training.

- https://getgophish.com/
- https://gitlab.com/parrotsec/packages/gophish

### gpp-decrypt

Group Policy Preferences decrypter A simple ruby script that will decrypt a given GPP encrypted string.

- http://carnal0wnage.attackresearch.com/2012/10/group-policy-preferences-and-getting.html
- https://gitlab.com/parrotsec/packages/gpp-decrypt

### gps3

GPSD interface (Python 3) This package contains GPSD interface and defaults to host=’127.0.0.1’, port=2947, gpsd_protocol=’json’ in two classes. - GPSDSocket creates a GPSD socket connection & request/retrieve GPSD output. - DataStream unpacks the streamed gpsd data into python dictionaries. These dictionaries are literated from the JSON data packet sent from the GPSD. This package installs the library for Python 3.

- https://github.com/wadda/gps3
- https://gitlab.com/parrotsec/packages/gps3

### grub2

GRand Unified Bootloader, version 2 (dummy package) This is a dummy transitional package to handle GRUB 2 upgrades. It can be safely removed.

- https://www.gnu.org/software/grub/
- https://gitlab.com/parrotsec/packages/grub2

### hak5-wifi-coconut

Userspace driver for the Hak5 Wi-Fi Coconut Userspace drive for USB Wi-Fi NICs and the Hak5 Wi-Fi Coconut

- https://hak5.org
- https://gitlab.com/parrotsec/packages/hak5-wifi-coconut

### hakrawler

Package entry imported from the ParrotSec package index.

- https://github.com/hakluke/hakrawler
- https://gitlab.com/parrotsec/packages/hakrawler

### hamster-sidejack

Sidejacking tool Hamster is tool or "sidejacking". It acts as a proxy server that replaces your cookies with session cookies stolen from somebody else, allowing you to hijack their sessions. Cookies are sniffed using the Ferret program. You need a copy of that as well.

- http://www.erratasec.com/research.html
- https://gitlab.com/parrotsec/packages/hamster-sidejack

### hostapd-mana

featureful rogue access point This package contains a eatureful rogue access point first presented at Defcon 22.

- https://github.com/sensepost/hostapd-mana
- https://gitlab.com/parrotsec/packages/hostapd-mana

### hostsman

cross-platform command line tool for handling hosts files cross-platform command line tool for adding, removing or listing mappings in hosts file.

- https://github.com/qszhuan/hostsman
- https://gitlab.com/parrotsec/packages/hostsman

### hotpatch

Hot patches Linux executables with .so file injection Hotpatch is a library that can be used to dynamically load a shared library (.so) file on Linux from one process into another already running process, without affecting the execution of the target process. The API is a C API, but also supported in C++.

- https://github.com/vikasnkumar/hotpatch
- https://gitlab.com/parrotsec/packages/hotpatch

### httprobe

Take a list of domains and probe for working HTTP and HTTPS servers This package contains a tool to test a domains list. It takes a list of domains and probe for working http and https servers.

- https://github.com/tomnomnom/httprobe
- https://gitlab.com/parrotsec/packages/httprobe

### httpx-toolkit

fast and multi-purpose HTTP toolkit This package contains the httpX toolkit developed by ProjectDiscovery. It's a fast and multi-purpose HTTP toolkit allow to run multiple probers using retryablehttp library, it is designed to maintain the result reliability with increased threads. Features * Simple and modular code base making it easy to contribute. * Fast And fully configurable flags to probe multiple elements. * Supports multiple HTTP based probings. * Smart auto fallback from https to http as default. * Supports hosts, URLs and CIDR as input. * Handles edge cases doing retries, backoffs etc for handling WAFs. This tool is packaged as 'httpx-toolkit' to avoid confusion and conflicts with the package python3-httpx that provides a script /usr/bin/httpx.

- https://github.com/projectdiscovery/httpx
- https://gitlab.com/parrotsec/packages/httpx-toolkit

### humble

HTTP Headers Analyzer This package contains an humble, and fast, security-oriented HTTP headers analyzer.

- https://github.com/rfc-st/humble
- https://gitlab.com/parrotsec/packages/humble

### hurl

Hexadecimal & URL encoder + decoder This package contains a hexadecimal & URL (en/de)coder.

- https://github.com/fnord0/hURL
- https://gitlab.com/parrotsec/packages/hurl

### hyperion

Runtime encrypter for 32-bit portable executables This package contains a runtime encrypter for 32-bit portable executables. It is a reference implementation and bases on the paper "Hyperion: Implementation of a PE-Crypter". The paper describes the implementation details which aren't in the scope of this readme file. The crypter is started via the command line and encrypts an input executable with AES-128. The encrypted file decrypts itself on startup (bruteforcing the AES key which may take a few seconds) and generates a log file for debug purpose.

- http://www.nullsecurity.net/tools/binary.html
- https://gitlab.com/parrotsec/packages/hyperion

### iaxflood

VoIP flooder tool A UDP Inter-Asterisk_eXchange (i.e. IAX) packet was captured from an IAX channel between two Asterisk IP PBX's. The content of that packet is the source of the payload for the attack embodied by this tool. While the IAX protocol header might not match the Asterisk PBX you'll attack with this tool, it may require more processing on the part of the PBX than a simple udpflood without any payload that even resembles an IAX payload.

- http://www.hackingexposedvoip.com/sec_tools.html
- https://gitlab.com/parrotsec/packages/iaxflood

### ibombshell

Dynamic Remote Shell This package contains a tool written in Powershell that allows you to have a prompt at any time with post-exploitation functionalities (and in some cases exploitation). It is a shell that is downloaded directly to memory providing access to a large number of pentesting features. These functionalities can be downloaded directly to memory, in the form of a Powershell function. This form of execution is known as everywhere. In addition, ibombshell provides a second execution mode called Silently, so the pentester can execute an instance of ibombshell (called warrior). The compromised computer will be connected to a C2 panel through HTTP. Therefore, it will be possible to control the warrior and be able to load functions in memory that help the pentester. This is happening whithin the post-exploitation phase.

- https://github.com/Telefonica/ibombshell
- https://gitlab.com/parrotsec/packages/ibombshell

### impacket-scripts

Links to useful impacket scripts examples This package contains links to useful impacket scripts. It's a separate package to keep impacket package from Debian and have the useful scripts in the path for Kali.

- https://gitlab.com/parrotsec/packages/impacket-scripts

### init-system-helpers

helper tools for all init systems This package contains helper tools that are necessary for switching between the various init systems that Debian contains (e. g. sysvinit or systemd). An example is deb-systemd-helper, a script that enables systemd unit files without depending on a running systemd. It also includes the "service", "invoke-rc.d", and "update-rc.d" scripts which provide an abstraction for enabling, disabling, starting, and stopping services for all supported Debian init systems as specified by the policy. While this package is maintained by pkg-systemd-maintainers, it is NOT specific to systemd at all. Maintainers of other init systems are welcome to include their helpers in this package.

- https://gitlab.com/parrotsec/packages/init-system-helpers

### inspy

LinkedIn enumeration tool This package contains a Python based LinkedIn enumeration tool. You will need an API key from HunterIO.

- https://github.com/gojhonny/InSpy
- https://gitlab.com/parrotsec/packages/inspy

### inviteflood

SIP/SDP INVITE message flooding over UDP/IP A tool to perform SIP/SDP INVITE message flooding over UDP/IP. It was tested on a Linux Red Hat Fedora Core 4 platform (Pentium IV, 2.5 GHz), but it is expected this tool will successfully build and execute on a variety of Linux distributions.

- http://www.hackingvoip.com/sec_tools.html
- https://gitlab.com/parrotsec/packages/inviteflood

### ipv6toolkit

IPv6 assessment and troubleshooting tools Included tools: - addr6: An IPv6 address analysis and manipulation tool. - flow6: A tool to perform a security asseessment of the IPv6 Flow Label. - frag6: A tool to perform IPv6 fragmentation-based attacks and to perform a security assessment of a number of fragmentation-related aspects. - icmp6: A tool to perform attacks based on ICMPv6 error messages. - jumbo6: A tool to assess potential flaws in the handling of IPv6 Jumbograms. - na6: A tool to send arbitrary Neighbor Advertisement messages. - ni6: A tool to send arbitrary ICMPv6 Node Information messages, and assess possible flaws in the processing of such packets. - ns6: A tool to send arbitrary Neighbor Solicitation messages. - ra6: A tool to send arbitrary Router Advertisement messages. - rd6: A tool to send arbitrary ICMPv6 Redirect messages. - rs6: A tool to send arbitrary Router Solicitation messages. - scan6: An IPv6 address scanning tool. - tcp6: A tool to send arbitrary TCP segments and perform a variety of TCP- based attacks.

- https://www.si6networks.com/tools/ipv6toolkit/
- https://gitlab.com/parrotsec/packages/ipv6toolkit

### ismtp

SMTP user enumeration and testing tool Test for SMTP user enumeration (RCPT TO and VRFY), internal spoofing, and relay.

- https://github.com/altjx/ipwn/
- https://gitlab.com/parrotsec/packages/ismtp

### javasnoop

Intercept Java applications locally Normally, without access to the original source code, testing the security of a Java client is unpredictable at best and unrealistic at worst. With access the original source, you can run a simple Java program and attach a debugger to it remotely, stepping through code and changing variables where needed. Doing the same with an applet is a little bit more difficult. JavaSnoop attempts to solve this problem by allowing you attach to an existing process (like a debugger) and instantly begin tampering with method calls, run custom code, or just watch what's happening on the system.

- https://gitlab.com/parrotsec/packages/javasnoop

### json-log-formatter

Package entry imported from the ParrotSec package index.

- https://github.com/marselester/json-log-formatter
- https://gitlab.com/parrotsec/packages/json-log-formatter

### jsql

Java tool for automatic database injection jSQL Injection is a lightweight application used to find database information from a distant server. jSQL is free, open source and cross-platform (Windows, Linux, Mac OS X, Solaris).

- https://github.com/ron190/jsql-injection
- https://gitlab.com/parrotsec/packages/jsql

### kbuild

framework for writing simple makefiles for complex tasks The goals of the kBuild framework: - Similar behavior cross all supported platforms. - Flexibility, don't create unnecessary restrictions preventing ad-hoc solutions. - Makefile can very simple to write and maintain. There are four concepts being tried out in the current kBuild incaration: - One configuration file for a subtree automatically included. - Target configuration templates as the primary mechanism for makefile simplification. - Tools and SDKs for helping out the templates with flexibility. - Non-recursive makefile method by using sub-makefiles. kBuild does not provide any facilities for checking compiler/library/header configurations, that's not in its scope. If this is important for your project, check out the autoconf tool in the GNU build system. It is possible to use kBuild together with autoconf if you like, but you might just as well use the full GNU package.

- https://svn.netlabs.org/kbuild
- https://gitlab.com/parrotsec/packages/kbuild

### kerbad

Minikerberos fork for bloodyAD kerbad is fork of minikerberos a kerberos client library written in Python>=3.6. It is the kerberos library used for bloodyAD. It also comes with multiple useful examples for pentesters who wish to perform security audits on the kerberos protocol. This package installs the library for Python 3.

- https://github.com/CravateRouge/kerbad
- https://gitlab.com/parrotsec/packages/kerbad

### kerberoast

tools for attacking MS Kerberos implementations This package contains a series of tools for attacking MS Kerberos implementations: - extract all accounts in use as SPN using built in MS tools - extract the acquired tickets from ram with Mimikatz - crack with tgsrepcrack - request Ticket(s) - etc

- https://github.com/nidem/kerberoast
- https://gitlab.com/parrotsec/packages/kerberoast

### kismet-docs

official kismet-docs This package contains the official documentation for Kismet.

- https://github.com/kismetwireless/kismet-docs
- https://gitlab.com/parrotsec/packages/kismet-docs

### koadic

Windows post-exploitation rootkit This package contains Koadic, or COM Command & Control. It is a Windows post-exploitation rootkit similar to other penetration testing tools such as Meterpreter and Powershell Empire. The major difference is that Koadic does most of its operations using Windows Script Host (a.k.a. JScript/VBScript), with compatibility in the core to support a default installation of Windows 2000 with no service packs (and potentially even versions of NT4) all the way through Windows 10. It is possible to serve payloads completely in memory from stage 0 to beyond, as well as use cryptographically secure communications over SSL and TLS (depending on what the victim OS has enabled).

- https://github.com/zerosum0x0/koadic
- https://gitlab.com/parrotsec/packages/koadic

### kubernetes-helm

tool for managing Charts (helm) This package contains a tool for managing Charts. Charts are packages of pre-configured Kubernetes resources. Use Helm to: * Find and use popular software packaged as Helm Charts to run in Kubernetes * Share your own applications as Helm Charts * Create reproducible builds of your Kubernetes applications * Intelligently manage your Kubernetes manifest files

- https://github.com/helm/helm
- https://gitlab.com/parrotsec/packages/kubernetes-helm

### kustomize

Customization of Kubernetes YAML configurations (program) Kustomize is a standalone binary tool for managing Kubernetes configurations without requiring templates. It allows users to customize resource configurations through overlays, making it easy to reuse and share manifests across environments. Kustomize operates natively with Kubernetes YAML, offering functionality like applying patches, setting images, and managing common labels and annotations.

- https://github.com/kubernetes-sigs/kustomize
- https://gitlab.com/parrotsec/packages/kustomize

### libcreg

library to access Windows 9x/Me Registry files -- development files libcreg is a library to access the Windows 9x/Me Registry File (CREG) format. This package includes the development support files.

- https://github.com/libyal/libcreg
- https://gitlab.com/parrotsec/packages/libcreg

### libcrypt-mcrypt-perl

Perl extension for MCrypt Crypto library This is an perl interface to the MCrypt crypto library, which supports a wide variety of block algorithms such as DES, TripleDES, Blowfish (default), 3-WAY, SAFER-SK64, SAFER-SK128, TWOFISH, TEA, RC2, GOST, LOKI, SERPENT, CAST and RIJNDAEL in CBC, OFB, CFB and ECB cipher modes. Mcrypt can be used to encrypt and decrypt using the above mentioned ciphers. The four important mcrypt commands (mcrypt_cfb(), mcrypt_cbc(), mcrypt_ecb(), and mcrypt_ofb()) can operate in both modes which are named MCRYPT_ENCRYPT and MCRYPT_DECRYPT, respectively. Mcrypt can operate in four block cipher modes (CBC, OFB, CFB, and ECB).

- https://metacpan.org/pod/MCrypt
- https://gitlab.com/parrotsec/packages/libcrypt-mcrypt-perl

### libevtx

Windows XML Event Log format access library -- development files libevtx is a library to access the Windows XML Event Log (EVTX) format. This package includes the development support files.

- https://github.com/libyal/libevtx
- https://gitlab.com/parrotsec/packages/libevtx

### libfindrtp

Library required by multiple VoIP tools This package contains a library used by multiple VoIP tools.

- http://www.hackingvoip.com/sec_tools.html
- https://gitlab.com/parrotsec/packages/libfindrtp

### libfsext

library to access the Extended File System -- development files libfsext is a library to access the Extended File System. This package includes the development support files.

- https://github.com/libyal/libfsext
- https://gitlab.com/parrotsec/packages/libfsext

### libfshfs

library to access the Mac OS Hierarchical File System -- development files libfshfs is a library to access the Mac OS Hierarchical File System (HFS). This package includes the development support files.

- https://github.com/libyal/libfshfs
- https://gitlab.com/parrotsec/packages/libfshfs

### libfsxfs

llibrary to access the SGI X File System -- development files libfsxfs is a library to access the SGI X File System (XFS). This package includes the development support files.

- https://github.com/libyal/libfsxfs
- https://gitlab.com/parrotsec/packages/libfsxfs

### libfwnt

Windows NT data type library -- development files libfwnt is a library for Windows NT data types. This package includes the development support files.

- https://github.com/libyal/libfwnt
- https://gitlab.com/parrotsec/packages/libfwnt

### libmodi

library to access the Mac OS disk image formats -- Utilities libmodi is a library to access the Mac OS disk image formats. This package contains tools to access data ...

- https://github.com/libyal/libmodi
- https://gitlab.com/parrotsec/packages/libmodi

### libnim-winim

Windows API for Nim lang Winim contains Windows API, struct, and constant definitions for Nim. The definitions are translated from MinGW's Windows headers and Windows 10 SDK headers. The module also include some Windows string type utilities and Windows COM support. See winstr.nim and com.nim for details. Furthermore, winim provides ability to interact with Windows .NET Frameworks since version 3.6.0.

- https://github.com/khchen/winim
- https://gitlab.com/parrotsec/packages/libnim-winim

### libsqlite-jdbc-java

SQLite JDBC Driver in Java This package contains a library for accessing and creating SQLite database files in Java. This package contains the bindings.

- https://github.com/xerial/sqlite-jdbc
- https://gitlab.com/parrotsec/packages/libsqlite-jdbc-java

### libstree

Generic suffix tree library libstree is a generic suffix tree implementation, written in C. It can handle arbitrary data structures as elements of a string. Unlike most demo implementations, it is not limited to simple ASCII character strings. Suffix tree generation in libstree is highly efficient and implemented using the algorithm by Ukkonen. This means that libstree builds suffix trees in time linear to the length of the strings, assuming that string element comparisons can be done in constant time.

- http://www.icir.org/christian/libstree/index.html
- https://gitlab.com/parrotsec/packages/libstree

### libvsgpt

library to access the GUID Partition Table volume system -- development files libvsgpt is a library to access the GUID Partition Table (GPT) volume system. This package includes the development support files.

- https://github.com/libyal/libvsgpt
- https://gitlab.com/parrotsec/packages/libvsgpt

### lief

Library to Instrument Executable Formats -- development files LIEF is a library for parsing, modifying ELF, PE, and MachO formats. This package contains the static library, header files, and examples.

- https://lief-project.github.io/
- https://gitlab.com/parrotsec/packages/lief

### limiter

Package entry imported from the ParrotSec package index.

- https://github.com/alexdelorenzo/limiter
- https://gitlab.com/parrotsec/packages/limiter

### linux

Inspection and simple manipulation of BPF programs and maps The bpftool command allows for inspection and simple modification of Berkeley Packet Filter (BPF) objects on the system.

- https://www.kernel.org/
- https://gitlab.com/parrotsec/packages/linux

### linux-exploit-suggester

LES: Linux privilege escalation auditing tool This package contains a Linux privilege escalation auditing tool. It's designed to assist in detecting security deficiencies for given Linux kernel/Linux-based machine. It provides following functionality: - Assessing kernel exposure on publicly known exploits Tool assesses (using heuristics methods discussed in details here) exposure of the given kernel on every publicly known Linux kernel exploit. For each exploit, exposure is calculated - Verifying state of kernel hardening security measures LES can check for most of security settings available by your Linux kernel. It verifies not only the kernel compile-time configurations (CONFIGs) but also verifies run-time settings (sysctl) giving more complete picture of security posture for running kernel. This functionality is modern continuation of --kernel switch from checksec.sh tool by Tobias Klein.

- https://github.com/mzet-/linux-exploit-suggester
- https://gitlab.com/parrotsec/packages/linux-exploit-suggester

### lsassy

Extract credentials from lsass remotely (Python 3) This package contains Python library to remotely extract credentials on a set of hosts. This package installs the library for Python 3.

- https://github.com/Hackndo/lsassy
- https://gitlab.com/parrotsec/packages/lsassy

### lzallright

Package entry imported from the ParrotSec package index.

- https://github.com/vlaci/lzallright
- https://gitlab.com/parrotsec/packages/lzallright

### maltego-teeth

Set of offensive Maltego transforms A set of transforms for Maltego to run nmap, sqlmap, and more against entitites in Maltego.

- https://www.maltego.com
- https://gitlab.com/parrotsec/packages/maltego-teeth

### manuf

Parser library for Wireshark's OUI database (Python 3) This package contains a parser library for Wireshark's OUI database. It converts MAC addresses into a manufacturer using Wireshark's OUI database. It's optimized for quick lookup performance by reading the entire file into memory on initialization. Maps ranges of MAC addresses to manufacturers and comments (descriptions). It contains full support for netmasks and other strange things in the database. This package installs the library for Python 3.

- https://github.com/coolbho3k/manuf
- https://gitlab.com/parrotsec/packages/manuf

### marco

lightweight GTK+ window manager for MATE Marco is a small window manager, using GTK+ to do everything. It is developed mainly for the MATE Desktop. This package contains the marco window manager itself.

- http://www.mate-desktop.org/
- https://gitlab.com/parrotsec/packages/marco

### markdown-it-py

Python port of markdown-it and some its associated plugins High speed Python markdown parser based in markdown-it. markdown-it-py follows the CommonMark spec for baseline parsing. Also, new syntax rules can be added and even replace existing ones. New syntax extensions can be added to extend the parser.

- https://github.com/executablebooks/markdown-it-py
- https://gitlab.com/parrotsec/packages/markdown-it-py

### massdns

high-performance DNS stub resolver This package contains a simple high-performance DNS stub resolver targeting those who seek to resolve a massive amount of domain names in the order of millions or even billions. Without special configuration, MassDNS is capable of resolving over 350,000 names per second using publicly available resolvers.

- https://github.com/blechschmidt/massdns
- https://gitlab.com/parrotsec/packages/massdns

### metagoofil

Tool designed for extracting metadata of public documents Metagoofil is an information gathering tool designed for extracting metadata of public documents (pdf,doc,xls,ppt,docx,pptx,xlsx) belonging to a target company. Metagoofil will perform a search in Google to identify and download the documents to local disk. Metagoofil does no longer extract the metadata. See /usr/share/doc/metagoofil/README.md.gz.

- https://github.com/opsdisk/metagoofil
- https://gitlab.com/parrotsec/packages/metagoofil

### mitmproxy-rs

mitmproxy's Rust bits (Python 3) This package contains mitmproxy's Rust bits, most notably: - WireGuard Mode: The ability to proxy any device that can be configured as a WireGuard client. - Windows OS Proxy Mode: The ability to proxy arbitrary Windows applications by name or pid. This package installs the library for Python 3.

- https://github.com/mitmproxy/mitmproxy_rs
- https://gitlab.com/parrotsec/packages/mitmproxy-rs

### mongodb

Package entry imported from the ParrotSec package index.

- https://www.mongodb.org
- https://gitlab.com/parrotsec/packages/mongodb

### more-termcolor

Pass unlimited number of colors, color-codes, or attributes (Python 3) This package contains a library to pass unlimited number of colors, color-codes, or attributes. Intelligently handles existing colors in the text as to allow adding or combining colors automatically, while ensuring the smallest string size possible This package installs the library for Python 3.

- https://github.com/giladbarnea/more_termcolor
- https://gitlab.com/parrotsec/packages/more-termcolor

### msldap

LDAP library for auditing MS AD (Python 3) This package contains an LDAP library for auditing MS AD. - Comes with a built-in console LDAP client - All parameters can be conrolled via a conveinent URL (see below) - Supports integrated windows authentication - Supports SOCKS5 proxy without the need of extra proxifyer - Minimal footprint - A lot of pre-built queries for convenient information polling This package installs the library for Python 3.

- https://github.com/skelsec/msldap
- https://gitlab.com/parrotsec/packages/msldap

### mypy-boto3-ebs

Type annotations for EBS (Python 3) This package contains type annotations for EBS service compatible with VSCode, PyCharm, Emacs, Sublime Text, mypy, pyright and other tools. This package installs the library for Python 3.

- https://github.com/vemel/mypy_boto3_builder
- https://gitlab.com/parrotsec/packages/mypy-boto3-ebs

### naked

command line application framework (Python 3) This package contains a new Python command line application framework. This package installs the library for Python 3.

- http://naked-py.com
- https://gitlab.com/parrotsec/packages/naked

### nassl

Package entry imported from the ParrotSec package index.

- https://github.com/nabla-c0d3/nassl
- https://gitlab.com/parrotsec/packages/nassl

### neo4j-python-driver

Package entry imported from the ParrotSec package index.

- https://github.com/neo4j/neo4j-python-driver
- https://gitlab.com/parrotsec/packages/neo4j-python-driver

### neotime

Nanosecond-precision temporal types for Python (Python 3) This package contains a neotime module that defines classes for working with temporal data to nanosecond precision. These classes comprise a similar set to that provided by the standard library datetime module. Inspiration has also been drawn from ISO-8601. This package installs the library for Python 3.

- https://github.com/neo4j-drivers/neotime
- https://gitlab.com/parrotsec/packages/neotime

### net-retriever

Package entry imported from the ParrotSec package index.

- https://gitlab.com/parrotsec/packages/net-retriever

### netcfg

Package entry imported from the ParrotSec package index.

- https://gitlab.com/parrotsec/packages/netcfg

### nextnet

pivot point discovery tool in Go This package contains a pivot point discovery tool written in Go.

- https://github.com/hdm/nextnet
- https://gitlab.com/parrotsec/packages/nextnet

### nishang

Collection of PowerShell scripts and payloads Nishang is a framework and collection of scripts and payloads which enables usage of PowerShell for offensive security and post exploitation during Penetration Tests. The scripts are written on the basis of requirement by the author during real Penetration Tests.

- https://github.com/samratashok/nishang
- https://gitlab.com/parrotsec/packages/nishang

### nvidia-graphics-drivers

NVIDIA CUDA Driver Library The Compute Unified Device Architecture (CUDA) enables NVIDIA graphics processing units (GPUs) to be used for massively parallel general purpose computation. This package contains the CUDA Driver API library for low-level CUDA programming. Supported NVIDIA devices include GPUs starting from GeForce 8 and Quadro FX series, as well as the Tesla computing processors. Please see the nvidia-kernel-dkms (nvidia-open-kernel-dkms) or nvidia-kernel-source (nvidia-open-kernel-source) packages for building the kernel module required by this package. This will provide nvidia-kernel-550.163.01 (nvidia-open-kernel-550.163.01).

- https://www.nvidia.com
- https://gitlab.com/parrotsec/packages/nvidia-graphics-drivers

### odpi

Oracle DB Programming Interface for Drivers and Applications (headers) This package contains Oracle Database Programming Interface for C (ODPI-C), an open source library of C code that simplifies access to Oracle Database for applications written in C or C++. It is a wrapper over Oracle Call Interface (OCI) that makes applications and language interfaces easier to develop. ODPI-C supports basic and advanced features of Oracle Database and Oracle Client. This package contains the headers.

- https://github.com/oracle/odpi
- https://gitlab.com/parrotsec/packages/odpi

### ohrwurm

RTP fuzzer ohrwurm is a small and simple RTP fuzzer that has been successfully tested on a small number of SIP phones. Features: - reads SIP messages to get information of the RTP port numbers - reading SIP can be omitted by providing the RTP port numbers, sothat any RTP traffic can be fuzzed - RTCP traffic can be suppressed to avoid that codecs - learn about the "noisy line" - special care is taken to break RTP handling itself - the RTP payload is fuzzed with a constant BER - the BER is configurable - requires arpspoof from dsniff to do the MITM attack - requires both phones to be in a switched LAN (GW operation only works partially)

- http://mazzoo.de/blog/2006/08/25#ohrwurm
- https://gitlab.com/parrotsec/packages/ohrwurm

### ollydbg

32-bit assembler level analysing debugger OllyDbg is a 32-bit assembler level analysing debugger for Microsoft Windows. Emphasis on binary code analysis makes it particularly useful in cases where source is unavailable.

- http://www.ollydbg.de/
- https://gitlab.com/parrotsec/packages/ollydbg

### open-ath9k-htc-firmware

firmware for AR7010 and AR9271 USB wireless adapters The Qualcomm Atheros AR7010 and AR9271 chipsets are used in USB wireless adapters which are 802.11n-capable. This package contains the free firmware they require to function, and which gets loaded onto the devices during use.

- https://github.com/qca/open-ath9k-htc-firmware
- https://gitlab.com/parrotsec/packages/open-ath9k-htc-firmware

### opensnitch

GNU/Linux interactive application firewall Whenever a program makes a connection, it'll prompt the user to allow or deny it. The user can decide if block the outgoing connection based on properties of the connection: by port, by uid, by dst ip, by program or a combination of them. These rules can last forever, until the app restart or just one time. The GUI allows the user to view live outgoing connections, as well as search by process, user, host or port. OpenSnitch can also work as a system-wide domains blocker, by using lists of domains, list of IPs or list of regular expressions.

- https://github.com/evilsocket/opensnitch
- https://gitlab.com/parrotsec/packages/opensnitch

### opentaxii

Package entry imported from the ParrotSec package index.

- https://github.com/eclecticiq/OpenTAXII
- https://gitlab.com/parrotsec/packages/opentaxii

### oracle-instantclient-devel

Oracle Instant Client SDK Devel This package contains SDK, additional header files and an example makefile for developing Oracle applications with Instant Client.

- https://www.oracle.com/technetwork/database/database-technologies/instant-client/overview/index.html
- https://gitlab.com/parrotsec/packages/oracle-instantclient-devel

### oracle-instantclient-sqlplus

Oracle Instant Client SQL*Plus This package contains additional libraries and executable for running SQL*Plus with Instant Client.

- https://www.oracle.com/technetwork/database/database-technologies/instant-client/overview/index.html
- https://gitlab.com/parrotsec/packages/oracle-instantclient-sqlplus

### owl

Package entry imported from the ParrotSec package index.

- https://owlink.org/
- https://gitlab.com/parrotsec/packages/owl

### pack2

Package entry imported from the ParrotSec package index.

- https://github.com/hops/pack2
- https://gitlab.com/parrotsec/packages/pack2

### packageurl-python

library to parse and build Package URLs (common documentation) This package contains a Python library to parse and build "purl" aka. Package URLs. This is the common documentation package.

- https://github.com/package-url/packageurl-python
- https://gitlab.com/parrotsec/packages/packageurl-python

### pacu

Package entry imported from the ParrotSec package index.

- https://rhinosecuritylabs.com/aws/pacu-open-source-aws-exploitation-framework/
- https://gitlab.com/parrotsec/packages/pacu

### padbuster

Script for performing Padding Oracle attacks PadBuster is a Perl script for automating Padding Oracle Attacks. PadBuster provides the capability to decrypt arbitrary ciphertext, encrypt arbitrary plaintext, and perform automated response analysis to determine whether a request is vulnerable to padding oracle attacks.

- https://github.com/GDSSecurity/PadBuster
- https://gitlab.com/parrotsec/packages/padbuster

### parrot-archive-keyring

Parrot GPG Archive Keyring Public keys for the parrot archives digital signature.

- https://gitlab.com/parrotsec/packages/parrot-archive-keyring

### parrot-core

Core package for Parrot OS Core package for the Parrot Debian distribution. . This package provides essential configuration files and base dependencies for the Parrot Security operating system and its flavors.

- https://www.parrotsec.org/
- https://gitlab.com/parrotsec/packages/parrot-core

### parrot-interface

Parrot interface metapackage metapackage that installs the graphic interface

- https://www.parrotsec.org/
- https://gitlab.com/parrotsec/packages/parrot-interface

### parrot-menu

Parrot GNU/Linux custom menu This package provides a custom menu for Parrot GNU/Linux. It is used by any destkop that complies with the Freedesktop menu specification at http://standards.freedesktop.org/menu-spec/menu-spec-1.0.html

- https://gitlab.com/parrotsec/packages/parrot-menu

### parrot-themes

Parrot OS default themes. This package contains the default themes for Parrot OS.

- https://www.parrotsec.org/
- https://gitlab.com/parrotsec/packages/parrot-themes

### parrot-tools

Parrot Encryption Tools This is Parrot Security, a security focused GNU/Linux distribution. This metapackage provides the cryptographic tools.

- https://www.parrotsec.org/
- https://gitlab.com/parrotsec/packages/parrot-tools

### parrot-wallpapers

Default wallpapers for Parrot GNU/Linux This is a collection of desktop wallpapers created for Parrot GNU/Linux

- https://parrotsec.org/
- https://gitlab.com/parrotsec/packages/parrot-wallpapers

### partman-auto

Package entry imported from the ParrotSec package index.

- https://gitlab.com/parrotsec/packages/partman-auto

### partman-basicfilesystems

Package entry imported from the ParrotSec package index.

- https://gitlab.com/parrotsec/packages/partman-basicfilesystems

### pdf-parser

Parses PDF files to identify fundamental elements This tool will parse a PDF document to identify the fundamental elements used in the analyzed file. It will not render a PDF document.

- https://blog.didierstevens.com/programs/pdf-tools/
- https://gitlab.com/parrotsec/packages/pdf-parser

### pdfid

Scans PDF files for certain PDF keywords This tool is not a PDF parser, but it will scan a file to look for certain PDF keywords, allowing you to identify PDF documents that contain (for example) JavaScript or execute an action when opened. PDFiD will also handle name obfuscation.

- https://blog.didierstevens.com/programs/pdf-tools/
- https://gitlab.com/parrotsec/packages/pdfid

### peass-ng

Privilege Escalation Awesome Scripts SUITE Privilege escalation tools for Windows and Linux/Unix* and MacOS. These tools search for possible local privilege escalation paths that you could exploit and print them to you with nice colors so you can recognize the misconfigurations easily.

- https://github.com/carlospolop/PEASS-ng
- https://gitlab.com/parrotsec/packages/peass-ng

### peirates

Package entry imported from the ParrotSec package index.

- https://github.com/inguardians/peirates
- https://gitlab.com/parrotsec/packages/peirates

### perl-cisco-copyconfig

Provides methods for manipulating Cisco devices Cisco::CopyConfig provides methods for manipulating the running-config of Cisco devices running IOS via SNMP directed TFTP. This is handy for making changes or backups on many devices without having to log into each device or write messy expect type scripts that need constant tweaking.

- https://metacpan.org/pod/Cisco::CopyConfig
- https://gitlab.com/parrotsec/packages/perl-cisco-copyconfig

### phpggc

Generate payloads that exploit unsafe object deserialization PHPGGC is a library of payloads exploiting unsafe object deserialization. It also provides a command-line tool to generate them.

- https://github.com/ambionics/phpggc
- https://gitlab.com/parrotsec/packages/phpggc

### pi-bluetooth

Raspberry Pi 3 bluetooth Loads BCM43430A1 firmware on boot

- https://github.com/RPi-Distro/pi-bluetooth
- https://gitlab.com/parrotsec/packages/pi-bluetooth

### pipewire-module-xrdp

audio over xrdp for PipeWire based systems This package provides scripts to automatically load the PipeWire xrdp modules when a xrdp session is started, thus allowing xrdp to generate sound on a pipewire-based system.

- https://github.com/neutrinolabs/pipewire-module-xrdp
- https://gitlab.com/parrotsec/packages/pipewire-module-xrdp

### plaso

super timeline all the things -- metapackage This is a metapackage that depends on the Python 3 package of the Plaso libraries and scripts.

- https://github.com/log2timeline/plaso
- https://gitlab.com/parrotsec/packages/plaso

### plotext

plot directly on terminal (Python 3) This package contains a Python module to plot directly on terminal. * it allows for scatter, line, bar, histogram and date-time plots (including candlestick), * it can also plot error bars, confusion matrices, and add extra text, lines and shapes to the plot, * you could use it to plot images (including GIFs) and stream video with audio (including YouTube), * it can save plots as text or as colored html, * it provides a simple function to color strings, * it comes with a dedicated command line tool, * it has no dependencies (except for optional dependencies for image/video plotting). This package installs the library for Python 3.

- https://github.com/piccolomo/plotext
- https://gitlab.com/parrotsec/packages/plotext

### powersploit

PowerShell Post-Exploitation Framework PowerSploit is a series of Microsoft PowerShell scripts that can be used in post-exploitation scenarios during authorized penetration tests.

- https://github.com/PowerShellMafia/PowerSploit
- https://gitlab.com/parrotsec/packages/powersploit

### protos-sip

SIP test suite The purpose of this test-suite is to evaluate implementation level security and robustness of Session Initiation Protocol (SIP) implementations.

- https://www.ee.oulu.fi/research/ouspg/PROTOS_Test-Suite_c07-sip
- https://gitlab.com/parrotsec/packages/protos-sip

### proxify

Swiss Army knife Proxy tool for HTTP/HTTPS traffic capture, manipulation This package contains a Swiss Army Knife Proxy for rapid deployments. It supports multiple operations such as request/response dump, filtering and manipulation via DSL language, upstream HTTP/Socks5 proxy. Additionally a replay utility allows to import the dumped traffic (request/responses with correct domain name) into burp or any other proxy by simply setting the upstream proxy to proxify. Features * Intercept / Manipulate HTTP/HTTPS & NON-HTTTP traffic * Invisible & Thick clients traffic proxy support * TLS MITM support with client/server certificates * HTTP and SOCKS5 support for upstream proxy * Traffic Match/Filter and Replace DSL support * Full traffic dump to file (request/responses) * Native embedded DNS server * Plugin Support to decode specific protocols (e.g XMPP/SMTP/FTP/SSH/) * Proxify Traffic replay in Burp

- https://github.com/projectdiscovery/proxify
- https://gitlab.com/parrotsec/packages/proxify

### proxmark3

Package entry imported from the ParrotSec package index.

- https://github.com/RfidResearchGroup/proxmark3
- https://gitlab.com/parrotsec/packages/proxmark3

### pulseaudio-module-xrdp

xrdp module for PulseAudio sound server PulseAudio, previously known as Polypaudio, is a sound server for POSIX and WIN32 systems. It is a drop in replacement for the ESD sound server with much better latency, mixing/re-sampling quality and overall architecture. This modules provides xrdp sink / source for PulseAudio. The server to client audio redirection is implemented as per Remote Desktop Protocol: Audio Output Virtual Channel Extension [MS-RDPEA] specs, which means it is interoperable with any RDP client which implements it (most of them including: MS RDP clients, FreeRDP). The client to server audio redirection is implemented as per Remote Desktop Protocol: Audio Input Redirection Virtual Channel Extension [MS-RDPEAI] which means it is interoperable with any RDP client which implements it (most of them including: MS RDP clients, FreeRDP). The module is called module-xrdp.

- https://github.com/neutrinolabs/pulseaudio-module-xrdp
- https://gitlab.com/parrotsec/packages/pulseaudio-module-xrdp

### pwnat

NAT to NAT client-server communication pwnat, pronounced "poe-nat", is a tool that allows any number of clients behind NATs to communicate with a server behind a separate NAT with *no* port forwarding and *no* DMZ setup on any routers in order to directly communicate with each other. The server does not need to know anything about the clients trying to connect.

- http://samy.pl/pwnat/
- https://gitlab.com/parrotsec/packages/pwnat

### py-sneakers

Port of the libnms C library (Python 3) This package contains a port to Python of the libnms C library. It recreates the famous data decryption effect shown in the 1992 film Sneakers. This package installs the library for Python 3.

- https://github.com/aenima-x/py-sneakers
- https://gitlab.com/parrotsec/packages/py-sneakers

### py2neo

client library and toolkit for working with Neo4j (common documentation) This package contains a client library and toolkit for working with Neo4j from within Python applications and from the command line. The core library has no external dependencies and has been carefully designed to be easy and intuitive to use. This is the common documentation package.

- https://py2neo.org
- https://gitlab.com/parrotsec/packages/py2neo

### pyexcel

Package entry imported from the ParrotSec package index.

- https://github.com/pyexcel/pyexcel
- https://gitlab.com/parrotsec/packages/pyexcel

### pyexcel-io

Package entry imported from the ParrotSec package index.

- https://github.com/pyexcel/pyexcel-io
- https://gitlab.com/parrotsec/packages/pyexcel-io

### pyexcel-ods

Package entry imported from the ParrotSec package index.

- https://github.com/pyexcel/pyexcel-ods
- https://gitlab.com/parrotsec/packages/pyexcel-ods

### pyexcel-text

Package entry imported from the ParrotSec package index.

- https://github.com/pyexcel/pyexcel-text
- https://gitlab.com/parrotsec/packages/pyexcel-text

### pyexcel-xls

Package entry imported from the ParrotSec package index.

- https://github.com/pyexcel/pyexcel-xls
- https://gitlab.com/parrotsec/packages/pyexcel-xls

### pyexcel-xlsx

Package entry imported from the ParrotSec package index.

- https://github.com/pyexcel/pyexcel-xlsx
- https://gitlab.com/parrotsec/packages/pyexcel-xlsx

### pyexploitdb

library to fetch the most recent exploit-database (Python 3) This package contains an optimized Python3 library to fetch the most recent exploit-database, create searchable indexes for CVE->EDBID and EDBID -> CVE, and provide methods to perform searches. This package installs the library for Python 3.

- https://github.com/GoVanguard/pyExploitDb
- https://gitlab.com/parrotsec/packages/pyexploitdb

### pygexf

library to generate gexf file format (common documentation) This package contains a Python library to generate gexf file format. This is the common documentation package.

- https://github.com/paulgirard/pygexf
- https://gitlab.com/parrotsec/packages/pygexf

### pygments

documentation for the Pygments Pygments is syntax highlighting package. This package contains the documentation for Pygments in HTML and reStructuredText format.

- https://pygments.org/
- https://gitlab.com/parrotsec/packages/pygments

### pyinstaller

Utility to bundle a Python application into a single package PyInstaller reads a Python script written by you. It analyzes your code to discover every other module and library your script needs in order to execute. Then it collects copies of all those files and puts them with your script in a single folder, or optionally in a single executable file. This package contains the executables. It depends on 'python3-pyinstaller', which contains the Python modules.

- https://pyinstaller.org/en/stable/
- https://gitlab.com/parrotsec/packages/pyinstaller

### pyjsparser

Fast JavaScript parser (Python 3) This package contains a Fast JavaScript parser, a manual translation of esprima.js to Python. It takes 1 second to parse whole angular.js library so parsing speed is about 100k characters per second which makes it the fastest and most comprehensible JavaScript parser for Python out there. It supports whole ECMAScript 5.1 and parts of ECMAScript 6. This package installs the library for Python 3.

- https://github.com/PiotrDabkowski/pyjsparser
- https://gitlab.com/parrotsec/packages/pyjsparser

### pykrb5

Python krb5 API interface (Python 3) This library provides Python functions that wraps the Kerberos 5 C API. This library is merely a wrapper around the Kerberos 5 APIs. The functions under the krb5 namespace match the KRB5 API specification but with the krb5_ prefix removed. This package installs the library for Python 3.

- https://github.com/jborean93/pykrb5
- https://gitlab.com/parrotsec/packages/pykrb5

### pylnk

transitional package This is a transitional package. It can safely be removed.

- https://github.com/strayge/pylnk
- https://gitlab.com/parrotsec/packages/pylnk

### pymetasploit3

full-fledged Metasploit automation library (Python 3) This package contains a full-fledged Python3 Metasploit automation library. It can interact with Metasploit either through msfrpcd or the msgrpc plugin in msfconsole. This package installs the library for Python 3.

- https://github.com/DanMcInerney/pymetasploit3
- https://gitlab.com/parrotsec/packages/pymetasploit3

### pyminifier

Package entry imported from the ParrotSec package index.

- https://github.com/liftoff/pyminifier
- https://gitlab.com/parrotsec/packages/pyminifier

### pymisp

Python Library to access MISP (common documentation) This package contains a Python library to access MISP platforms via their REST API. PyMISP allows you to fetch events, add or update events/attributes, add or update samples or search for attributes. This is the common documentation package.

- https://github.com/MISP/PyMISP
- https://gitlab.com/parrotsec/packages/pymisp

### pypcapfile

Python library for handling libpcap savefiles (Python 3) This package contains a pure Python library for handling libpcap savefiles. This package installs the library for Python 3.

- https://github.com/kisom/pypcapfile
- https://gitlab.com/parrotsec/packages/pypcapfile

### pyperscan

Package entry imported from the ParrotSec package index.

- https://github.com/vlaci/pyperscan
- https://gitlab.com/parrotsec/packages/pyperscan

### pyppeteer

port of puppeteer JavaScript chromium browser automation lib (common doc) This package contains an unofficial Python port of puppeteer javascript (headless) chrome/chromium browser automation library. This is the common documentation package.

- https://github.com/pyppeteer/pyppeteer
- https://gitlab.com/parrotsec/packages/pyppeteer

### pypsrp

PowerShell Remoting Protocol for Python (Python 3) This package contains a Python client for the PowerShell Remoting Protocol (PSRP) and Windows Remove Management (WinRM) service. It allows your to execute commands on a remote Windows host from any machine that can run Python. This library exposes 4 different types of APIs; * A simple client API that can copy files to and from the remote Windows host as well as execute processes and PowerShell scripts * A WSMan interface to execute various WSMan calls like Send, Create, Connect, Disconnect, etc * A Windows Remote Shell (WinRS) layer that executes cmd commands and executables using the base WinRM protocol * A PowerShell Remoting Protocol (PSRP) layer allows you to create remote Runspace Pools and PowerShell pipelines This package installs the library for Python 3.

- https://github.com/jborean93/pypsrp
- https://gitlab.com/parrotsec/packages/pypsrp

### pypykatz

Mimikatz implementation in pure Python (Python 3) This package contains Mimikatz implementation in pure Python. This package installs the library for Python 3.

- https://github.com/skelsec/pypykatz
- https://gitlab.com/parrotsec/packages/pypykatz

### pysecretsocks

Socks server for tunneling connections (Python 3) This package contains a Python SOCKS server for tunneling connections over another channel. This package installs the library for Python 3.

- https://github.com/BC-SECURITY/PySecretSOCKS
- https://gitlab.com/parrotsec/packages/pysecretsocks

### pyshodan

script for interacting with Shodan API (Python 3) This package contains a Python 3 script for interacting with Shodan API. It has three modes of operation: making an API query for a search term, for a single IP address, or for a list of IP addresses in a .txt file. This package installs the library for Python 3.

- https://github.com/GoVanguard/pyShodan
- https://gitlab.com/parrotsec/packages/pyshodan

### pysigma

library that parses and converts Sigma rules into queries (common documentation) This package contains a Python library that parses and converts Sigma rules into queries. It is a replacement for the legacy Sigma toolchain (sigmac) with a much cleaner design and is almost fully tested. This is the common documentation package.

- https://github.com/SigmaHQ/pySigma
- https://gitlab.com/parrotsec/packages/pysigma

### pysmb

SMB/CIFS library (common documentation) This package contains an experimental SMB/CIFS library written in Python. It implements the client-side SMB/CIFS protocol which allows your Python application to access and transfer files to/from SMB/CIFS shared folders like your Windows file sharing and Samba folders. This is the common documentation package.

- https://miketeo.net/wp/index.php/projects/pysmb
- https://gitlab.com/parrotsec/packages/pysmb

### pyspnego

Library to handle SPNEGO authentication (common documentation) This package contains a library to handle SPNEGO (Negotiate, NTLM, Kerberos) authentication. It also includes a packet parser that can be used to decode raw NTLM/SPNEGO/Kerberos tokens into a human readable format. This is the common documentation package.

- https://github.com/jborean93/pyspnego
- https://gitlab.com/parrotsec/packages/pyspnego

### python-adblockparser

parser for Adblock Plus filters (Python 3) This package contains a module for working with Adblock Plus filter rules. It can parse Adblock Plus filters and match URLs against them. This package installs the library for Python 3.

- https://github.com/scrapinghub/adblockparser
- https://gitlab.com/parrotsec/packages/python-adblockparser

### python-adns

Python bindings to the asynchronous DNS resolver library This module provides a Python binding to the adns asynchronous DNS resolver library. The module provides a small wrapper adns that simply returns status codes as does the C library. It also provides a more Python like interface ADNS that wraps status codes in proper exceptions. The package contains working examples in ADNS.py and DNSBL.py.

- https://github.com/trolldbois/python3-adns
- https://gitlab.com/parrotsec/packages/python-adns

### python-apt

Python interface to libapt-pkg (locales) The apt_pkg Python interface will provide full access to the internal libapt-pkg structures allowing Python programs to easily perform a variety of functions. This package contains locales.

- https://gitlab.com/parrotsec/packages/python-apt

### python-bluepy

Python interface to Bluetooth Low Energy on Linux (common documentation) This package contains a Python module to allow Bluetooth Low Energy (a.k.a Bluetooth Smart) peripherals to be controlled from Python. This is the common documentation package.

- https://github.com/IanHarvey/bluepy
- https://gitlab.com/parrotsec/packages/python-bluepy

### python-cffi-py2

Package entry imported from the ParrotSec package index.

- http://cffi.readthedocs.org/
- https://gitlab.com/parrotsec/packages/python-cffi-py2

### python-cherrypy-cors

CORS support for CherryPy (Python 3) CORS handling as a cherrypy tool This package installs the library for Python 3.

- https://github.com/yougov/cherrypy-cors
- https://gitlab.com/parrotsec/packages/python-cherrypy-cors

### python-cstruct

C-style structs for Python (common documentation) This package contains a C-style structs for Python. It Converts C struct/union definitions into Python classes with methods for serializing/deserializing. This is the common documentation package.

- https://github.com/andreax79/python-cstruct
- https://gitlab.com/parrotsec/packages/python-cstruct

### python-extproxy

Extend urllib2's ProxyHandler to support extra proxy types ExtProxy extend urllib2's ProxyHandler to support extra proxy types: HTTPS, SOCKS. It provides a consistent user experience like HTTP proxy for the users.

- https://github.com/SeaHOH/extproxy
- https://gitlab.com/parrotsec/packages/python-extproxy

### python-faraday

Collaborative Penetration Test IDE Faraday introduces a new concept (IPE) Integrated Penetration-Test Environment a multiuser Penetration test IDE. Designed for distribution, indexation and analysis of the generated data during the process of a security audit. The main purpose of Faraday is to re-use the available tools in the community to take advantage of them in a multiuser way. This package is a transitional package. It can be remove safely.

- https://faradaysec.com
- https://gitlab.com/parrotsec/packages/python-faraday

### python-filebytes

Library to read and edit files in ELF, PE, MachO and OAT (Python 3) This package contains a library to read and edit files in the following formats: Executable and Linking Format (ELF), Portable Executable (PE), MachO and OAT (Android Runtime). This package installs the library for Python 3.

- https://github.com/sashs/filebytes
- https://gitlab.com/parrotsec/packages/python-filebytes

### python-flask-classful

Class based views for Flask (common documentation) This package contains an extension that adds class based view to Flask. This is the common documentation package.

- https://github.com/teracyhq/flask-classful
- https://gitlab.com/parrotsec/packages/python-flask-classful

### python-googlesearch

Google search engine (Python 3) This package contains Python bindings for the Google search engine. This package installs the library for Python 3.

- https://breakingcode.wordpress.com/
- https://gitlab.com/parrotsec/packages/python-googlesearch

### python-grequests

Package entry imported from the ParrotSec package index.

- https://github.com/spyoungtech/grequests
- https://gitlab.com/parrotsec/packages/python-grequests

### python-httpagentparser

Python HTTP Agent Parser (Python 3) Extracts OS Browser etc information from http user agent string This package installs the library for Python 3.

- https://github.com/shon/httpagentparser
- https://gitlab.com/parrotsec/packages/python-httpagentparser

### python-imapclient

Easy-to-use Python IMAP client library (documentation) IMAPClient is a high-level Python library to access mailboxes via the IMAP protocol. It relieves the user of many low-level tasks like parsing server responses, encoding of unicode strings used as folder names, optional translation of timestamps into local time of the client and more. The information is delivered in handy Python data structures that can be easily used for further processing. To help with code development or for quick inspections IMAPClient also offers easy-to-use interactive sessions. This is the documentation package.

- https://github.com/mjs/imapclient
- https://gitlab.com/parrotsec/packages/python-imapclient

### python-jq

lightweight and flexible JSON processor (Python3 version) A lightweight and flexible JSON processor that provides Python bindings for jq. This package contains the Python 3 version of the library.

- https://github.com/mwilliamson/jq.py
- https://gitlab.com/parrotsec/packages/python-jq

### python-kismet-external

External tool Python API library for Kismet (Python 3) This package contains the Kismet external tool Python API library. This package installs the library for Python 3.

- https://github.com/kismetwireless/python-kismet-external
- https://gitlab.com/parrotsec/packages/python-kismet-external

### python-lml

Load me later, a lazy plugin management system (common documentation) This package contains a lazy plugin management system. It seamlessly finds the lml based plugins from the current Python environment but loads the plugins on demand. It is designed to support plugins that have external dependencies, especially bulky and/or memory hungry ones. lml provides the plugin management system only and the plugin interface is on your shoulder. This is the common documentation package.

- https://github.com/chfw/lml
- https://gitlab.com/parrotsec/packages/python-lml

### python-lsassy

Package entry imported from the ParrotSec package index.

- https://github.com/Hackndo/lsassy
- https://gitlab.com/parrotsec/packages/python-lsassy

### python-magic-ahupp

interface to the libmagic file type identification library (Python 3) This package contains a Python interface to the libmagic file type identification library. libmagic identifies file types by checking their headers according to a predefined list of file types. This functionality is exposed to the command line by the Unix command `file` This package installs the library for Python 3.

- https://github.com/ahupp/python-magic
- https://gitlab.com/parrotsec/packages/python-magic-ahupp

### python-mbedtls

Cryptographic library with Mbed TLS back end (Python 3) This package contains a free cryptographic library for Python that uses mbed TLS for back end. This package installs the library for Python 3.

- https://github.com/Synss/python-mbedtls
- https://gitlab.com/parrotsec/packages/python-mbedtls

### python-minidump

library to parse and read Microsoft minidump file format (Python 3) This package contains a Python library to parse and read Microsoft minidump file format. It can create minidumps on Windows machines using the windows API (implemented with ctypes). This package installs the library for Python 3.

- https://github.com/skelsec/minidump
- https://gitlab.com/parrotsec/packages/python-minidump

### python-minikerberos

Kerberos manipulation library in pure Python (Python 3) This package contains Kerberos manipulation library. This package installs the library for Python 3.

- https://github.com/skelsec/minikerberos
- https://gitlab.com/parrotsec/packages/python-minikerberos

### python-nplusone

Auto-detecting the n+1 queries problem in Python (common documentation) This package contains a library for detecting the n+1 queries problem in Python ORMs, including SQLAlchemy, Peewee, and the Django ORM. This is the common documentation package.

- https://github.com/jmcarp/nplusone
- https://gitlab.com/parrotsec/packages/python-nplusone

### python-owasp-zap-v2.4

implementation to access the OWASP ZAP API (Python 3) This package contains the Python implementation to access the OWASP ZAP API. This package installs the library for Python 3.

- https://github.com/zaproxy/zap-api-python
- https://gitlab.com/parrotsec/packages/python-owasp-zap-v2.4

### python-pptx

Package entry imported from the ParrotSec package index.

- https://github.com/scanny/python-pptx
- https://gitlab.com/parrotsec/packages/python-pptx

### python-publicsuffixlist

Public Suffix List parser implementation (Python 3) Public Suffix List parser implementation This package installs the library for Python 3.

- https://github.com/ko-zu/psl
- https://gitlab.com/parrotsec/packages/python-publicsuffixlist

### python-python-anticaptcha

Documentation for the Python library python_anticaptcha HTML documentation for the python_anticaptcha Python client library

- https://github.com/ad-m/python-anticaptcha
- https://gitlab.com/parrotsec/packages/python-python-anticaptcha

### python-roguehostapd

Hostapd fork with Wi-Fi attacks and Python bindings with ctypes (Python 3) This package contains a fork of hostapd, the famous user space software access point. It provides Python ctypes bindings and a number of additional attack features. It was primarily developed for use in the Wifiphisher project. This package installs the library for Python 3.

- https://github.com/wifiphisher/roguehostapd
- https://gitlab.com/parrotsec/packages/python-roguehostapd

### python-rtlsdr

Python wrapper for librtlsdr (Python3 package) pyrtlsdr is a simple Python interface to devices supported by the RTL-SDR project, which turns certain USB DVB-T dongles employing the Realtek RTL2832U chipset into low-cost, general purpose software-defined radio receivers. It wraps all the functions in the librtlsdr library (including asynchronous read support), and also provides a more Pythonic API. This package installs the library for Python 3.

- https://github.com/roger-/pyrtlsdr
- https://gitlab.com/parrotsec/packages/python-rtlsdr

### python-simple-rest-client

Simple REST client (Python 3) This package contains Simple REST client for Python 3.7+. This package installs the library for Python 3.

- https://github.com/allisson/python-simple-rest-client
- https://gitlab.com/parrotsec/packages/python-simple-rest-client

### python-sqlalchemy-schemadisplay

Turn SQLAlchemy DB Model into a graph (Python 3) This package contains a module to turn SQLAlchemy DB Model into a graph. This package installs the library for Python 3.

- https://github.com/fschulze/sqlalchemy_schemadisplay
- https://gitlab.com/parrotsec/packages/python-sqlalchemy-schemadisplay

### python-status

HTTP Status for Humans (Python 3) This package contains very simple Python library which provides human understandable HTTP status codes and improves readability of your code. You don't have to use those ugly HTTP status numbers, but use easily understandable status names. This package installs the library for Python 3.

- https://pypi.org/project/python-status
- https://gitlab.com/parrotsec/packages/python-status

### python-syslog-rfc5424-formatter

Python logging formatter for emitting RFC5424 Syslog messages (common doc) This module implements a Python logging formatter which produces well-formed RFC5424-compatible Syslog messages to a given socket. This is the common documentation package.

- https://github.com/EasyPost/syslog-rfc5424-formatter
- https://gitlab.com/parrotsec/packages/python-syslog-rfc5424-formatter

### python-titlecase

changes a given text to Title Caps This package filter changes a given text to Title Caps, and attempts to be clever about SMALL words like a/an/the in the input. The list of "SMALL words" which are not capped comes from the New York Times Manual of Style, plus some others like 'vs' and 'v'. The filter employs some heuristics to guess abbreviations that don't need conversion. This is a port of John Gruber's titlecase.pl.

- https://github.com/ppannuto/python-titlecase
- https://gitlab.com/parrotsec/packages/python-titlecase

### python-unidns

Rudimentary async DNS client in Python(Python 3) A basic async DNS library made by skelsec. This package installs the library for Python 3.

- https://github.com/skelsec/unidns
- https://gitlab.com/parrotsec/packages/python-unidns

### python-visvis

object oriented approach to visualization (Python 3) This package contains a pure Python library for visualization of 1D to 4D data in an object oriented way. Essentially, visvis is an object oriented layer of Python on top of OpenGl, thereby combining the power of OpenGl with the usability of Python. A Matlab/Matplotlib-like interface in the form of a set of functions allows easy creation of objects (e.g. plot(), imshow(), volshow(), surf()). This package installs the library for Python 3.

- https://github.com/almarklein/visvis
- https://gitlab.com/parrotsec/packages/python-visvis

### python-zlib-wrapper

Wrapper around zlib with custom header crc32 (Python 3) This package contains a very small library for building crc32 header on top of zlib. Zlib performance on the highest compression is decent for the benchmark, while not as optimized as 7z it was roughly half the time for all in memory test. This package installs the library for Python 3.

- https://github.com/killswitch-GUI/zlib_wrapper
- https://gitlab.com/parrotsec/packages/python-zlib-wrapper

### pytsk

Python Bindings for The Sleuth Kit This package contains Python 3 bindings to libtsk3, the shared library that provides all the functionality of The Sleuth Kit.

- https://github.com/py4n6/pytsk/
- https://gitlab.com/parrotsec/packages/pytsk

### pyuserinput

Simple, cross-platform module for mouse and keyboard control (Python 3) This package contains a module for cross-platform control of the mouse and keyboard in Python that is simple to use. This package installs the library for Python 3.

- https://github.com/PyUserInput/PyUserInput
- https://gitlab.com/parrotsec/packages/pyuserinput

### pyvnc

client library for interacting with a VNC session (Python 3) This package contains a client library for interacting programmatically (and physically) with a VNC session. pyVNC Client that is built with Twisted-Python and PyGame. The client supports the following encodings: Hextile, CoRRE, RRE, RAW, CopyRect. This package installs the library for Python 3.

- https://github.com/cair/pyVNC
- https://gitlab.com/parrotsec/packages/pyvnc

### pywinrm

Python 3 library for Windows Remote Management pywinrm is a Python client for Windows Remote Management (WinRM). This allows you to invoke commands on target Windows machines from any machine that can run Python. WinRM allows you to call native objects in Windows. These include, but are not limited to, running batch scripts, powershell scripts and fetching WMI variables.

- https://github.com/diyan/pywinrm
- https://gitlab.com/parrotsec/packages/pywinrm

### qsslcaudit

Package entry imported from the ParrotSec package index.

- https://github.com/gremwell/qsslcaudit
- https://gitlab.com/parrotsec/packages/qsslcaudit

### quark-engine

Package entry imported from the ParrotSec package index.

- https://github.com/quark-engine/quark-engine
- https://gitlab.com/parrotsec/packages/quark-engine

### radiotap-library

Radiotp parser C library This package is a Radiotap parser C library. Radiotap is a de facto standard for 802.11 frame injection and reception.

- https://github.com/radiotap/radiotap-library
- https://gitlab.com/parrotsec/packages/radiotap-library

### rawtherapee

raw image converter and digital photo processor RawTherapee is an advanced program for developing raw photos and for processing non-raw photos. It is non-destructive, makes use of OpenMP, supports all the cameras supported by dcraw and carries out its calculations in a high precision 32bit floating point engine. RawTherapee supports JPEG, PNG, and TIFF as output format for processed photos.

- https://www.rawtherapee.com
- https://gitlab.com/parrotsec/packages/rawtherapee

### rcracki-mt

Version of rcrack that supports hybrid and indexed tables rcracki_mt is our modified version of rcrack which supports hybrid and indexed tables. In addition to that, it also adds multi-core support

- https://freerainbowtables.com/
- https://gitlab.com/parrotsec/packages/rcracki-mt

### recstudio

Package entry imported from the ParrotSec package index.

- http://www.backerstreet.com/rec/rec.htm
- https://gitlab.com/parrotsec/packages/recstudio

### redeye

tool to help you manage your data during a pentest operation This package contains a tool intended to help you manage your data during a pentest operation in the most efficient and organized way.

- https://github.com/redeye-framework/Redeye
- https://gitlab.com/parrotsec/packages/redeye

### redfang

Locates non-discoverable bluetooth devices fang is a small proof-of-concept application to find non discoveredable bluetooth devices. This is done by brute forcing the last six (6) bytes of the bluetooth address of the device and doing a read_remote_name().

- https://gitlab.com/parrotsec/packages/redfang

### rich

render rich text, tables, progress bars, syntax highlighting, markdown and more Rich is a Python library for rich text and beautiful formatting in the terminal. The Rich API makes it easy to add color and style to terminal output. Rich can also render pretty tables, progress bars, markdown, syntax highlighted source code, tracebacks, and more — out of the box. Here's a list of the core functionalities of rich: * to effortlessly add rich output to your application, you can import the rich print method, which has the same signature as the builtin Python function * Rich can be installed in the Python REPL, so that any data structures will be pretty printed and highlighted * for more control over rich terminal content, import and construct a Console object. The Console object has a print method which has an intentionally similar interface to the builtin print function * to insert an emoji in to console output place the name between two colons * Rich can render flexible tables with unicode box characters. There is a large variety of formatting options for borders, styles, cell alignment etc * Rich can render multiple flicker-free progress bars to track long-running tasks. * Rich can render content in neat columns with equal or optimal width. * Rich can render markdown and does a reasonable job of translating the formatting to the terminal * Rich can render beautiful tracebacks which are easier to read and show more code than standard Python tracebacks. You can set Rich as the default traceback handler so all uncaught exceptions will be rendered by Rich.

- https://github.com/Textualize/rich
- https://gitlab.com/parrotsec/packages/rich

### rizin-ghidra-plugin

A fork of Ghidra's decompiler for Rizin and Cutter This is an integration of the Ghidra decompiler and Sleigh Disassembler for Rizin. It is solely based on the decompiler part of Ghidra, which is written entirely in C++, so Ghidra itself is not required at all and the plugin can be built self-contained.

- https://github.com/rizinorg/rz-ghidra/
- https://gitlab.com/parrotsec/packages/rizin-ghidra-plugin

### rizin-libyara

Rizin libyara wrapper for creating Yara rules Rizin libyara wrapper for creating, parsing and applying YARA rules and Cutter native plugin. This package is a plugin for Rizin.

- https://github.com/rizinorg/rz-libyara/
- https://gitlab.com/parrotsec/packages/rizin-libyara

### robotstxt

robots.txt exclusion protocol implementation for Go language This package contains a robots.txt exclusion protocol implementation for Go language (golang).

- https://github.com/temoto/robotstxt
- https://gitlab.com/parrotsec/packages/robotstxt

### rootskel-gtk

Package entry imported from the ParrotSec package index.

- https://gitlab.com/parrotsec/packages/rootskel-gtk

### ropper

rop gadget finder and binary information tool This package contains scripts that display info about files in different formats and find gadgets to build ROPs chains for different architectures (x86/x86_64, ARM/ARM64, MIPS, PowerPC). For disassembly ropper uses the Capstone Framework.

- https://scoding.de/ropper/
- https://gitlab.com/parrotsec/packages/ropper

### rsmangler

Wordlist mangling tool RSMangler will take a wordlist and perform various manipulations on it similar to those done by John the Ripper the main difference being that it will first take the input words and generate all permutations and the acronym of the words (in order they appear in the file) before it applies the rest of the mangles.

- https://digi.ninja/projects/rsmangler.php
- https://gitlab.com/parrotsec/packages/rsmangler

### rtpflood

Tool to flood any RTP device A command line tool used to flood any device that is processing RTP.

- http://www.hackingvoip.com/sec_tools.html
- https://gitlab.com/parrotsec/packages/rtpflood

### rtpinsertsound

Inserts audio into a specified stream A tool to insert audio into a specified audio (i.e. RTP) stream was created in the August - September 2006 timeframe. The tool is named rtpinsertsound. It was tested on a Linux Red Hat Fedora Core 4 platform (Pentium IV, 2.5 GHz), but it is expected this tool will successfully build and execute on a variety of Linux distributions.

- http://www.hackingvoip.com/sec_tools.html
- https://gitlab.com/parrotsec/packages/rtpinsertsound

### rtpmixsound

Mixes pre-recorded audio in real-time A tool to mix pre-recorded audio in real-time with the audio (i.e. RTP) in the specified target audio stream.

- http://www.hackingvoip.com/sec_tools.html
- https://gitlab.com/parrotsec/packages/rtpmixsound

### ruby-async-dns

easy to use DNS client resolver and server for Ruby Async::DNS provides a high-performance DNS client resolver and server which can be easily integrated into other projects or used as a stand-alone daemon.

- https://github.com/socketry/async-dns
- https://gitlab.com/parrotsec/packages/ruby-async-dns

### ruby-ecdsa

ECDSA implementation almost entirely in pure Ruby This package contains the Elliptic Curve Digital Signature Algorithm (ECDSA) almost entirely in pure Ruby. This gem does use OpenSSL but it only uses it to decode and encode ASN1 strings for ECDSA signatures. All cryptographic calculations are done in pure Ruby.

- https://github.com/DavidEGrayson/ruby_ecdsa
- https://gitlab.com/parrotsec/packages/ruby-ecdsa

### ruby-ffi

load dynamic libraries, bind functions from within ruby code Ruby-FFI is a ruby extension for programmatically loading dynamic libraries, binding functions within them, and calling those functions from Ruby code. Moreover, a Ruby-FFI extension works without changes on Ruby and JRuby. Discover why should you write your next extension using Ruby-FFI at https://github.com/ffi/ffi/wiki/Why-use-FFI.

- https://github.com/ffi/ffi/wiki
- https://gitlab.com/parrotsec/packages/ruby-ffi

### ruby-fxruby

Package entry imported from the ParrotSec package index.

- https://github.com/larskanis/fxruby
- https://gitlab.com/parrotsec/packages/ruby-fxruby

### ruby-glu

Glu bindings for ruby This package contains Glu bindings for ruby. It works in tandem with opengl.

- https://github.com/larskanis/glu
- https://gitlab.com/parrotsec/packages/ruby-glu

### ruby-glut

Glut bindings for OpenGL This package contains Glut bindings for OpenGL. It is to be used with the {opengl}[https://github.com/larskanis/opengl] gem.

- https://github.com/larskanis/glut
- https://gitlab.com/parrotsec/packages/ruby-glut

### ruby-iostruct

Struct that can read/write itself from/to IO-like objects This package contains a gem to manage a struct that can read/write itself from/to IO-like objects.

- http://github.com/zed-0xff/iostruct
- https://gitlab.com/parrotsec/packages/ruby-iostruct

### ruby-opengl

Ruby OpenGl wrapper This package contains an OpenGL wrapper for Ruby. opengl contains bindings for OpenGL.

- https://github.com/larskanis/opengl
- https://gitlab.com/parrotsec/packages/ruby-opengl

### ruby-pedump

Package entry imported from the ParrotSec package index.

- http://github.com/zed-0xff/pedump
- https://gitlab.com/parrotsec/packages/ruby-pedump

### ruby-salsa20

Salsa20 stream cipher algorithm This package provides a simple Ruby wrapper for Salsa20, a stream cipher algorithm.

- https://github.com/dubek/salsa20-ruby
- https://gitlab.com/parrotsec/packages/ruby-salsa20

### ruby-winrm

Ruby library for Windows Remote Management This package contains a SOAP library that uses the functionality in Windows Remote Management(WinRM) to call native object in Windows. This includes, but is not limited to, running batch scripts, powershell scripts and fetching WMI variables.

- https://github.com/WinRb/WinRM
- https://gitlab.com/parrotsec/packages/ruby-winrm

### ruby-winrm-fs

WinRM File System This package contains a Ruby library for file system operations via Windows Remote Management.

- http://github.com/WinRb/winrm-fs
- https://gitlab.com/parrotsec/packages/ruby-winrm-fs

### ruby-zhexdump

highly flexible hexdump implementation This package contains a highly flexible hexdump implementation in Ruby.

- https://github.com/zed-0xff/zhexdump
- https://gitlab.com/parrotsec/packages/ruby-zhexdump

### rule-engine

library for creating general purpose “Rule” objects (common documentation) This package contains a library for creating general purpose “Rule” objects from a logical expression which can then be applied to arbitrary objects to evaluate whether or not they match. This is the common documentation package.

- https://github.com/zeroSteiner/rule-engine
- https://gitlab.com/parrotsec/packages/rule-engine

### rz-ghidra

Package entry imported from the ParrotSec package index.

- https://github.com/rizinorg/rz-ghidra
- https://gitlab.com/parrotsec/packages/rz-ghidra

### rzpipe

Pipe interface for rizin Interact with rizin using the `#!pipe` command or in standalone scripts that communicate with local or remote rizin via pipe, tcp or http.

- https://rizin.re
- https://gitlab.com/parrotsec/packages/rzpipe

### sarge

library to interact with exteranl programs (Python 3) This package contains Sarge, a library which is intended to make your life easier than using the subprocess module in Python’s standard library. Sarge is, of course, short for sergeant – and like any good non-commissioned officer, sarge works to issue commands on your behalf and to inform you about the results of running those commands. This is the common documentation package.

- https://docs.red-dove.com/sarge/
- https://gitlab.com/parrotsec/packages/sarge

### sasquatch

Tool to extract vendor specific SquashFS images This package contains a tool to extract vendor specific SquashFS images.

- https://github.com/onekey-sec/sasquatch
- https://gitlab.com/parrotsec/packages/sasquatch

### seclists-lite

Minimal collection of multiple types of security lists seclists-lite is a collection of multiple types of lists used during security assessments. List types included are a small subset of the larger SecLists in order to provide common lists while saving disk space (approximately half the size of the full seclists package). The goal is to enable a security tester to pull this repo onto a new testing box and have access to a minimal collection of common lists that may be needed.

- https://www.owasp.org/index.php/Projects/OWASP_SecLists_Project
- https://gitlab.com/parrotsec/packages/seclists-lite

### secure-socket-funneling

Package entry imported from the ParrotSec package index.

- https://github.com/securesocketfunneling/ssf
- https://gitlab.com/parrotsec/packages/secure-socket-funneling

### set

Social-Engineer Toolkit The Social-Engineer Toolkit (SET) is an open-source Python-driven tool aimed at penetration testing around Social-Engineering.

- https://www.trustedsec.com/downloads/social-engineer-toolkit/
- https://gitlab.com/parrotsec/packages/set

### sfuzz

Black Box testing utilities In the same vein as the Generic Protocol Framework, sfuzz is a really simple to use black box testing suite called Simple Fuzzer (what else would you expect?). The goal is to provide a simple to use, but fairly powerful and flexible black box testing utility.

- http://aconole.brad-x.com/programs/sfuzz.html
- https://gitlab.com/parrotsec/packages/sfuzz

### shellfire

exploiting LFI, RFI, and command injection vulnerabilities This package contains an exploitation shell which focuses on exploiting LFI, RFI, and command injection vulnerabilities.

- https://github.com/unix-ninja/shellfire
- https://gitlab.com/parrotsec/packages/shellfire

### sidguesser

Guesses sids against an Oracle database Guesses sids/instances against an Oracle database according to a predefined dictionary file. The speed is slow (80-100 guesses per second) but it does the job.

- http://www.cqure.net/wp/tools/database/sidguesser/
- https://gitlab.com/parrotsec/packages/sidguesser

### sigma-cli

Sigma command line interface This package contains the Sigma command line interface using the pySigma library to manage, list and convert Sigma rules into query languages.

- https://github.com/SigmaHQ/sigma-cli
- https://gitlab.com/parrotsec/packages/sigma-cli

### siparmyknife

SIP fuzzing tool SIP Army Knife is a fuzzer that searches for cross site scripting, SQL injection, log injection, format strings, buffer overflows, and more.

- https://packetstormsecurity.com/files/107301/SIP-Army-Knife-Fuzzer-11232011.html
- https://gitlab.com/parrotsec/packages/siparmyknife

### slim

desktop-independent graphical login manager for X11 SLiM aims to be light, simple and independent from the various desktop environments. Although completely configurable through themes and an option file. It is particularly suitable for machines that don't require remote logins.

- http://sourceforge.net/projects/slim-fork/
- https://gitlab.com/parrotsec/packages/slim

### slimtoolkit

optimization of your containers This package contains Slim(toolkit). It was called DockerSlim, and it is now just Slim (SlimToolkit). It is a tool for developers with a number of different commands (build, xray, lint, debug and others) to simplify and optimize your developer experience with containers. It makes your containers better, smaller and more secure while providing advanced visibility and improved usability working with the

- https://github.com/slimtoolkit/slim
- https://gitlab.com/parrotsec/packages/slimtoolkit

### sliver

Implant framework This package contains a general purpose cross-platform implant framework that supports C2 over Mutual-TLS, HTTP(S), and DNS. Implants are dynamically compiled with unique X.509 certificates signed by a per-instance certificate authority generated when you first run the binary.

- https://github.com/BishopFox/sliver
- https://gitlab.com/parrotsec/packages/sliver

### slowapi

Rate limiting library for Starlette and FastAPI (Python 3) This package contains a rate limiting library for Starlette and FastAPI adapted from flask-limiter. This package installs the library for Python 3.

- https://github.com/laurentS/slowapi
- https://gitlab.com/parrotsec/packages/slowapi

### smtp-user-enum

Username guessing tool for the SMTP service Username guessing tool primarily for use against the default Solaris SMTP service. Can use either EXPN, VRFY or RCPT TO.

- http://pentestmonkey.net/tools/user-enumeration/smtp-user-enum
- https://gitlab.com/parrotsec/packages/smtp-user-enum

### sniffjoke

Transparent TCP connection scrambler SniffJoke is an application for Linux that handle transparently your TCP connection, delaying, modifyng and inject fake packets inside your transmission, make them almost impossible to be correctly readed by a passive wiretapping technology (IDS or sniffer).

- https://github.com/vecna/sniffjoke
- https://gitlab.com/parrotsec/packages/sniffjoke

### snmpenum

SNMP tabledump This package contains a simple Perl script to enumerate information on Machines that are running SNMP.

- https://packetstormsecurity.com/files/download/31079/snmpenum.zip
- https://gitlab.com/parrotsec/packages/snmpenum

### sparrow-wifi

Graphical Wi-Fi Analyzer for Linux This package contains a gaphical Wi-Fi analyser for Linux. It provides a more comprehensive GUI-based replacement for tools like inSSIDer and linssid that runs specifically on Linux. In its most comprehensive use cases, sparrow-wifi integrates Wi-Fi, software-defined radio (hackrf), advanced bluetooth tools (traditional and Ubertooth), traditional GPS (via gpsd), and drone/rover GPS via mavlink in one solution.

- https://github.com/ghostop14/sparrow-wifi
- https://gitlab.com/parrotsec/packages/sparrow-wifi

### sparta-scripts

Additional Sparta Scripts for Legion This package contains optional scripts to use with Legion, a Sparta's fork. These scripts come from the initial Sparta project.

- https://github.com/GoVanguard/sparta-scripts
- https://gitlab.com/parrotsec/packages/sparta-scripts

### spiderfoot

Package entry imported from the ParrotSec package index.

- https://www.spiderfoot.net
- https://gitlab.com/parrotsec/packages/spiderfoot

### spooftooph

Automates spoofing or cloning Bluetooth devices Spooftooph is designed to automate spoofing or cloning Bluetooth device Name, Class, and Address. Cloning this information effectively allows Bluetooth device to hide in plain site. Bluetooth scanning software will only list one of the devices if more than one device in range shares the same device information when the devices are in Discoverable Mode (specificaly the same Address).

- http://www.hackfromacave.com/projects/spooftooph.html
- https://gitlab.com/parrotsec/packages/spooftooph

### spyse-python

Package entry imported from the ParrotSec package index.

- https://github.com/spyse-com/spyse-python
- https://gitlab.com/parrotsec/packages/spyse-python

### sqldict

Dictionary attack tool for SQL Server SQLdict is a dictionary attack tool for SQL Server.

- https://ntsecurity.nu/toolbox/sqldict/
- https://gitlab.com/parrotsec/packages/sqldict

### sqlninja

SQL server injection and takeover tool Fancy going from a SQL Injection on Microsoft SQL Server to a full GUI access on the DB? Take a few new SQL Injection tricks, add a couple of remote shots in the registry to disable Data Execution Prevention, mix with a little Perl that automatically generates a debug script, put all this in a shaker with a Metasploit wrapper, shake well and you have just one of the attack modules of sqlninja!

- https://sqlninja.sourceforge.net/
- https://gitlab.com/parrotsec/packages/sqlninja

### sslcrypto

fast and simple library for AES, ECIES and ECDSA (Python 3) This package contains a fast and simple library for AES, ECIES and ECDSA for Python. sslcrypto can use OpenSSL in case it's available in your system for speedup, but pure-Python code is also available and is heavily optimized. This package installs the library for Python 3.

- https://github.com/imachug/sslcrypto
- https://gitlab.com/parrotsec/packages/sslcrypto

### sslscan

Tests SSL/TLS enabled services to discover supported cipher suites This tool allow queries SSL/TLS services (such as HTTPS) and reports the protocol versions, cipher suites, key exchanges, signature algorithms, and certificates in use. This helps the user understand which parameters are weak from a security standpoint. sslscan can also output results into an XML file for easy consumption by external programs.

- https://github.com/rbsec/sslscan
- https://gitlab.com/parrotsec/packages/sslscan

### sslyze

Package entry imported from the ParrotSec package index.

- https://github.com/nabla-c0d3/sslyze
- https://gitlab.com/parrotsec/packages/sslyze

### starkiller

Frontend for Powershell Empire This package contains a Frontend for Powershell Empire.

- https://github.com/BC-SECURITY/Starkiller
- https://gitlab.com/parrotsec/packages/starkiller

### stix2

Package entry imported from the ParrotSec package index.

- https://github.com/oasis-open/cti-python-stix2
- https://gitlab.com/parrotsec/packages/stix2

### subjack

Package entry imported from the ParrotSec package index.

- https://github.com/haccer/subjack
- https://gitlab.com/parrotsec/packages/subjack

### syncer

async-to-sync converter for Python (common documentation) This package contains an async-to-sync converter for Python. Sometimes (mainly in test) we need to convert asynchronous functions to normal, synchronous functions and run them synchronously. It can be done by ayncio.get_event_loop().run_until_complete(), but it's quite long... Syncer makes this conversion easy. This is the common documentation package.

- https://github.com/miyakogi/syncer
- https://gitlab.com/parrotsec/packages/syncer

### tasksel

tool for selecting tasks for installation on Debian systems This package provides 'tasksel', a simple interface for users who want to configure their system to perform a specific task.

- https://gitlab.com/parrotsec/packages/tasksel

### teamsploit

Tools for group based penetration testing TeamSploit makes group-based penetration testing fun and easy, providing real-time collaboration and automation. TeamSploit is a suite of tools for the Metasploit Framework. TeamSploit should work with any MSF product (including OpenSource, Express, or Pro). Features include: * Exploitation Automation * Automated Post-Exploitation * Information and Data Gathering * Session Sharing * Trojans and Trollware TeamSploit's primary goal is to automate common penetration testing tasks, and provide access and information to fellow team members.

- http://www.teamsploit.com
- https://gitlab.com/parrotsec/packages/teamsploit

### thc-ssl-dos

Stress tester for the SSL handshake THC-SSL-DOS is a tool to verify the performance of SSL. Establishing a secure SSL connection requires 15x more processing power on the server than on the client. THC-SSL-DOS exploits this asymmetric property by overloading the server and knocking it off the Internet. This problem affects all SSL implementations today. The vendors are aware of this problem since 2003 and the topic has been widely discussed. This attack further exploits the SSL secure Renegotiation feature to trigger thousands of renegotiations via single TCP connection.

- http://www.thc.org/thc-ssl-dos/
- https://gitlab.com/parrotsec/packages/thc-ssl-dos

### thehive

Package entry imported from the ParrotSec package index.

- https://github.com/TheHive-Project/TheHive
- https://gitlab.com/parrotsec/packages/thehive

### tls-parser

Small library to parse TLS records (Python 3) This package contains a small library to parse TLS records, used by SSLyze. This package installs the library for Python 3.

- https://github.com/nabla-c0d3/tls_parser
- https://gitlab.com/parrotsec/packages/tls-parser

### tnscmd10g

Tool to prod the oracle tnslsnr process A tool to prod the oracle tnslsnr process on port 1521/tcp.

- http://www.red-database-security.com/
- https://gitlab.com/parrotsec/packages/tnscmd10g

### trufflehogregexes

regexes power truffleHog (Python 3) This package contains regexes power truffleHog. This package installs the library for Python 3.

- https://github.com/dxa4481/truffleHogRegexes
- https://gitlab.com/parrotsec/packages/trufflehogregexes

### tundeep

Layer 2 VPN/injection tool The tool resides [almost] entirely in user space on the victim aside from the pcap requirement.

- https://www.adampalmer.me/iodigitalsec/tundeep/
- https://gitlab.com/parrotsec/packages/tundeep

### ubertooth

2.4 GHz wireless development platform for Bluetooth experimentation Project Ubertooth is an open source wireless development platform suitable for Bluetooth experimentation. This package contains everything necessary to use the hardware dongle. Ubertooth is capable of sniffing BLE (Bluetooth Smart) connections and it also has some ability to sniff some data from Basic Rate (BR) Bluetooth Classic connections. In addition to the Bluetooth specific capabilities, there is also a simple spectrum analyzer for the 2.4 GHz band included (ubertooth-specan-ui) which can be used to also observe other things in this frequency band.

- https://github.com/greatscottgadgets/ubertooth/
- https://gitlab.com/parrotsec/packages/ubertooth

### ubi-reader

scripts capable of extracting the contents of UBI and UBIFS images (Python 3) This package contains a ollection of scripts capable of extracting the contents of UBI and UBIFS images, along with analyzing these images to determine the parameter settings to recreate them using the mtd-utils tools. This package installs the library for Python 3.

- https://github.com/onekey-sec/ubi_reader
- https://gitlab.com/parrotsec/packages/ubi-reader

### uhd-images

Various UHD Images Various UHD Images

- https://www.ettus.com
- https://gitlab.com/parrotsec/packages/uhd-images

### unblob

Package entry imported from the ParrotSec package index.

- https://unblob.org/
- https://gitlab.com/parrotsec/packages/unblob

### unblob-native

performance-critical components of Unblob (Python 3) This package holds performance-critical components of Unblob, an accurate, fast, and easy-to-use extraction suite. It parses unknown binary blobs for more than 30 different archive, compression, and file-system formats, extracts their content recursively, and carves out unknown chunks that have not been accounted for. This package installs the library for Python 3.

- https://github.com/onekey-sec/unblob-native
- https://gitlab.com/parrotsec/packages/unblob-native

### unicorn-magic

Tool for a PowerShell downgrade attack and inject shellcode This package contains a simple tool for using a PowerShell downgrade attack and inject shellcode straight into memory. Based on Matthew Graeber's powershell attacks and the powershell bypass technique presented by David Kennedy (TrustedSec) and Josh Kelly at Defcon 18. Usage is simple, just run Magic Unicorn (ensure Metasploit is installed and in the right path) and magic unicorn will automatically generate a powershell command that you need to simply cut and paste the powershell code into a command line window or through a payload delivery system.

- https://github.com/trustedsec/unicorn
- https://gitlab.com/parrotsec/packages/unicorn-magic

### unicrypto

Unified interface for some crypto algos (Python 3) This package contains a Python module: an unified interface for some crypto algos. This package installs the library for Python 3.

- https://github.com/skelsec/unicrypto
- https://gitlab.com/parrotsec/packages/unicrypto

### unsafeopenssl

Secure Sockets Layer toolkit - development files - UNSAFE VERSION This package is part of the OpenSSL project's implementation of the SSL and TLS cryptographic protocols for secure communication over the Internet. It contains development libraries, header files, and manpages for libssl and libcrypto.

- https://github.com/gremwell/unsafeopenssl-pkg-deb
- https://gitlab.com/parrotsec/packages/unsafeopenssl

### vadersentiment

lexicon and rule-based sentiment analysis tool (Python 3) This package contains VADER (Valence Aware Dictionary and sEntiment Reasoner). It is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. This package installs the library for Python 3.

- https://github.com/cjhutto/vaderSentiment
- https://gitlab.com/parrotsec/packages/vadersentiment

### veil

Generates payloads to bypass anti-virus solutions Veil is a tool designed to generate metasploit payloads that bypass common anti-virus solutions. It replaces the package veil-evasion.

- https://github.com/Veil-Framework/Veil
- https://gitlab.com/parrotsec/packages/veil

### voiphopper

Runs a VLAN hop security test VoIP Hopper is a GPLv3 licensed security tool, written in C that rapidly runs a VLAN Hop security test. VoIP Hopper is a VoIP infrastructure security testing tool but also a tool that can be used to test the (in)security of VLANs.

- https://sourceforge.net/projects/voiphopper
- https://gitlab.com/parrotsec/packages/voiphopper

### volatility3

The volatile memory extraction framework Volatility is the world's most widely used framework for extracting digital artifacts from volatile memory (RAM) samples. The extraction techniques are performed completely independent of the system being investigated but offer visibility into the runtime state of the system. The framework is intended to introduce people to the techniques and complexities associated with extracting digital artifacts from volatile memory samples and provide a platform for further work into this exciting area of research.

- https://github.com/volatilityfoundation/volatility3
- https://gitlab.com/parrotsec/packages/volatility3

### wgetpaste

Command-line interface to various online pastebin services This package contains a script that automates pasting to a number of pastebin services.

- http://wgetpaste.zlin.dk/
- https://gitlab.com/parrotsec/packages/wgetpaste

### wig-ng

utility for Wi-Fi device fingerprinting This package contains WIG (Wi-Fi Information Gathering), a utility for Wi-Fi device fingerprinting. Supported protocols and standards: * Apple Wireless Direct Link (AWDL) * Cisco Client Extension (CCX) * HP Printers Custom Information Element * Wi-Fi Direct (P2P) * Wi-Fi Protected Setup (WPS) This tool doesn't perform channel hopping, use tools such as chopping or airodump-ng.

- https://github.com/6e726d/wig-ng
- https://gitlab.com/parrotsec/packages/wig-ng

### windows-binaries

Various pentesting Windows binaries A collection of Windows executables for use on penetration tests.

- https://www.kali.org
- https://gitlab.com/parrotsec/packages/windows-binaries

### wmi

DCOM/WMI client implementation This DCOM/WMI client implementation is based on Samba4 sources. It uses RPC/DCOM mechanisms to interact with WMI services on Windows 2000/XP/2003 machines. This package contains the command line client to perform remote command execution on Windows systems.

- https://gitlab.com/parrotsec/packages/wmi

### wmis

Linux native WMIC client Linux native WMIC client

- https://gitlab.com/parrotsec/packages/wmis

### woeusb-ng

Create Windows Installer on Linux A simple tool that enable you to create your own usb stick windows installer from an iso image or a real DVD. This is a rewrite of original WoeUSB.

- https://github.com/WoeUSB/WoeUSB-ng
- https://gitlab.com/parrotsec/packages/woeusb-ng

### wordlists

Contains the rockyou wordlist This package contains the rockyou.txt wordlist and has an installation size of 134 MB.

- https://www.kali.org
- https://gitlab.com/parrotsec/packages/wordlists

### xlutils

Utilities for working with Excel files (common documentation) This package provides a collection of utilities for working with Excel files. Since these utilities may require either or both of the xlrd and xlwt packages, they are collected together here, separate from either package. This is the common documentation package.

- http://www.python-excel.org/
- https://gitlab.com/parrotsec/packages/xlutils

### xspy

X server sniffer Sniffs keystrokes on remote or local X-Windows servers.

- https://www.kali.org
- https://gitlab.com/parrotsec/packages/xspy

### zsh-autocomplete

Real time type-ahead completion for ZSH This package is a plugin of ZSH that suggest file/folder name.

- https://github.com/marlonrichert/zsh-autocomplete
- https://gitlab.com/parrotsec/packages/zsh-autocomplete


## Web Security


### ToolHunt

This is a local search engine to search for cybersecurity tools. It has 3000+ tools in it's database.

- GitHub: https://github.com/cyberytti/ToolHunt
- Documentation: https://github.com/cyberytti/ToolHunt/blob/main/README.md
- Topics: cyber-security, cyberpunkui, cybersecurity, dockerfile, ethical-hacking, ethical-hacking-tools, ethicalhacking, hacking-tool

### toolbox-pentest-web

Docker toolbox for pentest of web based application.

- GitHub: https://github.com/righettod/toolbox-pentest-web
- Official site: https://github.com/righettod/toolbox-pentest-web/pkgs/container/toolbox-pentest-web
- Documentation: https://github.com/righettod/toolbox-pentest-web/blob/master/README.md
- Topics: docker, pentesting, web

### bettercap-ui

bettercap's web UI This package contains the bettercap's web UI. Web UI - the easiest method, good if you never used bettercap before.

- https://github.com/bettercap/ui
- https://gitlab.com/parrotsec/packages/bettercap-ui

### burpsuite

Toolkit for security testing of web applications Burp Suite is an integrated platform for performing security testing of web applications. Its various tools work seamlessly together to support the entire testing process, from initial mapping and analysis of an application's attack surface, through to finding and exploiting security vulnerabilities. Burp gives you full control, letting you combine advanced manual techniques with state-of-the-art automation, to make your work faster, more effective, and more fun.

- https://portswigger.net
- https://gitlab.com/parrotsec/packages/burpsuite

### cloudflare-scrape

Python module to bypass Cloudflare's anti-bot page (Python 3) This package contains a simple Python module to bypass Cloudflare's anti-bot page (also known as "I'm Under Attack Mode", or IUAM), implemented with Requests. Due to Cloudflare continually changing and hardening their protection page, cloudflare-scrape requires Node.js to solve Javascript challenges. This allows the script to easily impersonate a regular web browser without explicitly deobfuscating and parsing Cloudflare's Javascript. This package installs the library for Python 3.

- https://github.com/Anorov/cloudflare-scrape
- https://gitlab.com/parrotsec/packages/cloudflare-scrape

### colly

Elegant Scraper and Crawler Framework for Golang (program) This package contains a Colly Lightning Fast and Elegant Scraping Framework for Gophers. Colly provides a clean interface to write any kind of crawler/scraper/spider. With Colly you can easily extract structured data from websites, which can be used for a wide range of applications, like data mining, data processing or archiving.

- https://github.com/gocolly/colly
- https://gitlab.com/parrotsec/packages/colly

### davtest

Testing tool for WebDAV servers DAVTest tests WebDAV enabled servers by uploading test executable files, and then (optionally) uploading files which allow for command execution or other actions directly on the target. It is meant for penetration testers to quickly and easily determine if enabled DAV services are exploitable.

- https://github.com/cldrn/davtest
- https://gitlab.com/parrotsec/packages/davtest

### dvwa

Damn Vulnerable Web Application This package contains a PHP/MySQL web application that is damn vulnerable. Its main goal is to be an aid for security professionals to test their skills and tools in a legal environment, help web developers better understand the processes of securing web applications and to aid both students & teachers to learn about web application security in a controlled class room environment. The aim of DVWA is to practice some of the most common web vulnerabilities, with various levels of difficulty, with a simple straightforward interface. Please note, there are both documented and undocumented vulnerabilities with this software. This is intentional. You are encouraged to try and discover as many issues as possible. WARNING: Do not upload it to your hosting provider's public html folder or any Internet facing servers, as they will be compromised.

- https://github.com/digininja/DVWA
- https://gitlab.com/parrotsec/packages/dvwa

### emailharvester

Email addresses harvester This package contains EmailHarvester, a tool to retrieve Domain email addresses from Search Engines. Features: * Retrieve Domain email addresses from popular Search engines (Google, Bing, Yahoo, ASK, Baidu, Dogpile, Exalead) * Export results to txt and xml files * Limit search results * Define your own User-Agent string * Use proxy server * Plugins system * Search in popular web sites using Search engines (Twitter, LinkedIn, Google+, Github, Instagram, Reddit, Youtube)

- https://github.com/maldevel/EmailHarvester
- https://gitlab.com/parrotsec/packages/emailharvester

### eyewitness

Rapid web application triage tool EyeWitness is designed to take screenshots of websites, provide some server header info, and identify default credentials if possible. Inspiration came from Tim Tomes's PeepingTom Script. EyeWitness is designed to run on Kali Linux. It will auto detect the file you give it with the -f flag as either being a text file with URLs on each new line, nmap xml output, or nessus xml output. The -t (timeout) flag is completely optional, and lets you provice the max time to wait when trying to render and screenshot a web page. The --open flag, which is optional, will open the URL in a new tab within Firefox.

- https://www.christophertruncer.com/eyewitness-triage-tool/
- https://gitlab.com/parrotsec/packages/eyewitness

### goshs

Simple, yet feature-rich web server Replacement for Python's SimpleHTTPServer. It allows uploading and downloading via HTTP/S with either self-signed certificate or user provided certificate and you can use HTTP basic auth.

- https://github.com/patrickhener/goshs
- https://gitlab.com/parrotsec/packages/goshs

### gospider

Fast web spider written in Go Fast web spider written in Go supports multiple purposes

- https://github.com/jaeles-project/gospider
- https://gitlab.com/parrotsec/packages/gospider

### gradle

Powerful build system for the JVM Gradle is a build tool with a focus on build automation and support for multi-language development. If you are building, testing, publishing, and deploying software on any platform, Gradle offers a flexible model that can support the entire development lifecycle from compiling and packaging code to publishing web sites. Gradle has been designed to support build automation across multiple languages and platforms including Java, Scala, Android, C/C++, and Groovy, and is closely integrated with development tools and continuous integration servers including Eclipse, IntelliJ, and Jenkins.

- https://gradle.org
- https://gitlab.com/parrotsec/packages/gradle

### httprint

Web server fingerprinting tool httprint is a web server fingerprinting tool. It relies on web server characteristics to accurately identify web servers, despite the fact that they may have been obfuscated by changing the server banner strings, or by plug-ins such as mod_security or servermask. httprint can also be used to detect web enabled devices which do not have a server banner string, such as wireless access points, routers, switches, cable modems, etc. httprint uses text signature strings and it is very easy to add signatures to the signature database.

- https://www.net-square.com/httprint.html
- https://gitlab.com/parrotsec/packages/httprint

### isr-evilgrade

Evilgrade framework Evilgrade is a modular framework that allows the user to take advantage of poor upgrade implementations by injecting fake updates. It comes with pre-made binaries (agents), a working default configuration for fast pentests, and has it's own WebServer and DNSServer modules. Easy to set up new settings, and has an autoconfiguration when new binary agents are set.

- https://github.com/infobyte/evilgrade
- https://gitlab.com/parrotsec/packages/isr-evilgrade

### juice-shop

insecure web application This package contains a modern and sophisticated insecure web application! It can be used in security trainings, awareness demos, CTFs and as a guinea pig for security tools! Juice Shop encompasses vulnerabilities from the entire OWASP Top Ten along with many other security flaws found in real-world applications! WARNING: Do not upload it to your hosting provider's public html folder or any Internet facing servers, as they will be compromised.

- https://github.com/juice-shop/juice-shop
- https://gitlab.com/parrotsec/packages/juice-shop

### laudanum

Collection of injectable web files Laudanum is a collection of injectable files, designed to be used in a pentest when SQL injection flaws are found and are in multiple languages for different environments.They provide functionality such as shell, DNS query, LDAP retrieval and others.

- https://sourceforge.net/projects/laudanum/
- https://gitlab.com/parrotsec/packages/laudanum

### neo4j

Graph database Neo4j Community Edition This package contains Neo4j Community Edition. It's a highly scalable, native graph database purpose-built to leverage not only data but also its relationships. Neo4j runs as a server application, exposing a Web-based management interface and RESTful endpoints for data access.

- https://neo4j.com/
- https://gitlab.com/parrotsec/packages/neo4j

### osrframework

Open Sources Research Framework This package contains a set of libraries developed by i3visio to perform Open Source Intelligence tasks. They include references to a bunch of different applications related to username checking, DNS lookups, information leaks research, deep web search, regular expressions extraction and many others.

- https://github.com/i3visio/osrframework
- https://gitlab.com/parrotsec/packages/osrframework

### owasp-mantra-ff

Web application security testing framework built on top of Firefox Mantra is a browser especially designed for web application security testing. By having such a product, more people will come to know the easiness and flexibility of being able to follow basic testing procedures within the browser. Mantra believes that having such a portable, easy to use and yet powerful platform can be helpful for the industry. Mantra has many built in tools to modify headers, manipulate input strings, replay GET/POST requests, edit cookies, quickly switch between multiple proxies, control forced redirects etc. This makes it a good software for performing basic security checks and sometimes, exploitation. Thus, Mantra can be used to solve basic levels of various web based CTFs, showcase security issues in vulnerable web applications etc.

- https://www.owasp.org/index.php/OWASP_Mantra_-_Security_Framework
- https://gitlab.com/parrotsec/packages/owasp-mantra-ff

### paros

Web application proxy Lightweight web application testing proxy

- http://www.parosproxy.org/index.shtml
- https://gitlab.com/parrotsec/packages/paros

### payloadsallthethings

Collection of useful payloads and bypasses A list of useful payloads and bypasses for Web Application Security and Pentest/CTF.

- https://github.com/swisskyrepo/PayloadsAllTheThings
- https://gitlab.com/parrotsec/packages/payloadsallthethings

### phpsploit

Stealth post-exploitation framework This package contains a remote control framework, aiming to provide a stealth interactive shell-like connection over HTTP between client and web server. It is a post-exploitation tool capable to maintain access to a compromised web server for privilege escalation purposes.

- https://github.com/nil0x42/phpsploit
- https://gitlab.com/parrotsec/packages/phpsploit

### python-advancedhttpserver

Standalone web server built on Python's BaseHTTPServer (Python 3) AdvancedHTTPServer builds on top of Python's included BaseHTTPServer and provides out of the box support for additional commonly needed features such as: - Threading - SSL - Registering handler functions to HTTP resources - A default robots.txt file - Forking the server process - Basic Authentication - The HTTP verbs GET HEAD POST and OPTIONS - RPC over HTTP This package installs the library for Python 3.

- https://github.com/zeroSteiner/AdvancedHTTPServer/
- https://gitlab.com/parrotsec/packages/python-advancedhttpserver

### python-filteralchemy

Declarative query builder for SQLAlchemy (common documentation) This package contains a declarative query builder for SQLAlchemy. It uses marshmallow-sqlalchemy to auto-generate filter fields and webargs to parse field parameters from the request. Use it to filter data with minimal boilerplate. This is the common documentation package.

- https://github.com/infobyte/filteralchemy
- https://gitlab.com/parrotsec/packages/python-filteralchemy

### python-secure

Secure lock headers and cookies for Python web frameworks (Python 3) This package contains is a lightweight package that adds optional security headers and cookie attributes for Python web frameworks. This package installs the library for Python 3.

- https://github.com/TypeError/secure.py
- https://gitlab.com/parrotsec/packages/python-secure

### python-selenium

Python3 bindings for Selenium (Documentation) Python3 language bindings for Selenium WebDriver. The `selenium` package is used automate web browser interaction from Python. Several browsers/drivers are supported (Chrome, Chromium, Edge, Firefox, Internet Explorer and Safari), as well as the Remote protocol. This package installs the documentation for the library.

- https://github.com/SeleniumHQ/selenium/
- https://gitlab.com/parrotsec/packages/python-selenium

### routerkeygenpc

Router Keygen generate default WPA/WEP keys This package generates default WPA/WEP keys for the several routers: * Thomson based routers ( this includes Thomson, SpeedTouch, Orange, Infinitum, BBox, DMax, BigPond, O2Wireless, Otenet, Cyta , TN_private, Blink ) * DLink ( only some models ) * Pirelli Discus * Eircom * Verizon FiOS ( only some routers supported) * Alice AGPF * FASTWEB Pirelli and Telsey * Huawei (some InfinitumXXXX) * Wlan_XXXX or Jazztel_XXXX * Wlan_XX ( only some are supported) * Ono ( P1XXXXXX0000X ) * WlanXXXXXX, YacomXXXXXX and WifiXXXXXX * Sky V1 routers * Clubinternet.box v1 and v2 ( TECOM-AH4XXXX ) * InfostradaWifi * CONN-X * Megared * EasyBox, Arcor and Vodafone * PBS (Austria) * MAXCOM * PTV * TeleTu/Tele2 * Axtel, Axtel-xtremo * Intercable * OTE * Cabovisao Sagem * Alice in Germany * Speedport

- https://github.com/routerkeygen/routerkeygenPC
- https://gitlab.com/parrotsec/packages/routerkeygenpc

### ruby-webrick

HTTP server toolkit in Ruby WEBrick is an HTTP server toolkit that can be configured as an HTTPS server, a proxy server, and a virtual-host server. It used to be provided with the standard library of the Ruby interpreter, and has been available only as a standalone gem since ruby3.0.

- https://github.com/ruby/webrick
- https://gitlab.com/parrotsec/packages/ruby-webrick

### splinter

Python test framework for web applications (common documentation) This package contains an open source tool for testing web applications using Python. It lets you automate browser actions, such as visiting URLs and interacting with their items. This is the common documentation package.

- https://github.com/cobrateam/splinter
- https://gitlab.com/parrotsec/packages/splinter

### token-bucket

Token Bucket Implementation for Python Web Apps (Python 3) This package contains an implementation of the token bucket algorithm suitable for use in web applications for shaping or policing request rates. This implementation does not require the use of an independent timer thread to manage the bucket state. Compared to other rate-limiting algorithms that use a simple counter, the token bucket algorithm provides the following advantages: The thundering herd problem is avoided since bucket capacity is replenished gradually, rather than being immediately refilled at the beginning of each epoch as is common with simple fixed window counters. Burst duration can be explicitly controlled. Moving window algorithms are resistant to bursting, but at the cost of additional processing and memory overhead vs. the token bucket algorithm which uses a simple, fast counter per key. The latter approach does allow for bursting, but only for a controlled duration. This package installs the library for Python 3.

- https://github.com/falconry/token-bucket
- https://gitlab.com/parrotsec/packages/token-bucket

### webacoo

Web backdoor cookie script kit Scripts for creating Web backdoors using cookies, with module support

- https://github.com/anestisb/WeBaCoo
- https://gitlab.com/parrotsec/packages/webacoo

### webscarab

Web application review tool WebScarab is designed to be a tool for anyone who needs to expose the workings of an HTTP(S) based application, whether to allow the developer to debug otherwise difficult problems, or to allow a security specialist to identify vulnerabilities in the way that the application has been designed or implemented.

- https://github.com/OWASP/OWASP-WebScarab
- https://gitlab.com/parrotsec/packages/webscarab

### webshells

Collection of webshells A collection of webshells for ASP, ASPX, CFM, JSP, Perl, and PHP servers.

- https://www.kali.org
- https://gitlab.com/parrotsec/packages/webshells

### weevely

Stealth tiny web shell Weevely is a stealth PHP web shell that simulate telnet-like connection. It is an essential tool for web application post exploitation, and can be used as stealth backdoor or as a web shell to manage legit web accounts, even free hosted ones.

- https://github.com/epinna/weevely3/
- https://gitlab.com/parrotsec/packages/weevely

### wotmate

reimplement the defunct PGP pathfinder with only your own keyring This package contains a reimplementation the defunct PGP pathfinder without needing anything other than your own keyring. Currently, the following tools are available: * graph-paths.py: Draws the shortest path between each key you have personally signed and the target key. For simpler setups, it exactly mirrors the web of trust, but the resulting graph is not necessarily one-to-one (because you can assign ownertrust to a key you did not directly sign). * graph-to-full.py: Very similar, but finds shortest paths to each fully-trusted key in your keyring. Handy for open-source projects where someone maintains a "web of trust."

- https://github.com/mricon/wotmate
- https://gitlab.com/parrotsec/packages/wotmate

### wsgidav

generic and extendable WebDAV server (common documentation) This package contains a generic and extendable WebDAV server written in Python and based on WSGI. This is the common documentation package.

- https://github.com/mar10/wsgidav
- https://gitlab.com/parrotsec/packages/wsgidav

### xsser

XSS testing framework Cross Site "Scripter" (aka XSSer) is an automatic -framework- to detect, exploit and report XSS vulnerabilities in web-based applications. It contains several options to try to bypass certain filters, and various special techniques of code injection.

- https://xsser.03c8.net/
- https://gitlab.com/parrotsec/packages/xsser

### zaproxy

Testing tool for finding vulnerabilities in web applications The OWASP Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding vulnerabilities in web applications. It is designed to be used by people with a wide range of security experience and as such is ideal for developers and functional testers who are new to penetration testing as well as being a useful addition to an experienced pen testers toolbox. https://www.owasp.org/index.php/ZAP

- https://github.com/zaproxy/zaproxy
- https://gitlab.com/parrotsec/packages/zaproxy


## Forensics


### LockKnife

LockKnife: The Ultimate Android Security Research Tool. A unified TUI workspace and headless CLI for deep Android security research, built for researchers and hackers. Powered by Python orchestration and a Rust-accele...

- GitHub: https://github.com/ImKKingshuk/LockKnife
- Official site: https://lockknife.vercel.app
- Documentation: https://github.com/ImKKingshuk/LockKnife/blob/main/README.md
- Topics: adb, ai-agents, ai-assisted-hacking, ai-hacking, android-forensics, android-hacking, android-reverse-engineering, android-security

### RecoverPy

Interactively find and recover deleted or :point_right: overwritten :point_left: files from your terminal

- GitHub: https://github.com/PabloLec/RecoverPy
- Documentation: https://github.com/PabloLec/RecoverPy/blob/main/README.md
- Topics: cli, console, cybersecurity, data, data-recovery, files, forensics, hacking

### autopsy

graphical interface to SleuthKit The Autopsy Forensic Browser is a graphical interface to the command line digital forensic analysis tools in The Sleuth Kit. Together, The Sleuth Kit and Autopsy provide many of the same features as commercial digital forensics tools for the analysis of Windows and UNIX file systems (NTFS, FAT, FFS, EXT2FS, and EXT3FS).

- https://www.sleuthkit.org/autopsy/
- https://gitlab.com/parrotsec/packages/autopsy

### dfdatetime

Digital Forensics date and time library for Python 3 dfDateTime, or Digital Forensics date and time, provides date and time objects to preserve accuracy and precision.

- https://github.com/log2timeline/dfdatetime
- https://gitlab.com/parrotsec/packages/dfdatetime

### dfwinreg

Digital Forensics Windows Registry library for Python 3 dfWinReg, or Digital Forensics Windows Registry, provides read-only access to Windows Registry objects. The goal of dfWinReg is to provide a generic interface for accessing Windows Registry objects that resembles the Registry key hierarchy as seen on a live Windows system.

- https://github.com/log2timeline/dfwinreg
- https://gitlab.com/parrotsec/packages/dfwinreg

### dumpzilla

Mozilla browser forensic tool Dumpzilla application is developed in Python 3.x and has as purpose extract all forensic interesting information of Firefox, Iceweasel and Seamonkey browsers to be analyzed. Due to its Python 3.x development, might not work properly in old Python versions, mainly with certain characters. Works under Unix and Windows 32/64 bits systems. Works in command line interface, so information dumps could be redirected by pipes with tools such as grep, awk, cut, sed... Dumpzilla allows one to visualize following sections, search customization and extract certain content.

- http://www.dumpzilla.org/
- https://gitlab.com/parrotsec/packages/dumpzilla

### maltego

Open source intelligence and graphical link analysis tool Maltego is an open source intelligence and forensics application. It will offer you timous mining and gathering of information as well as the representation of this information in a easy to understand format. Coupled with its graphing libraries, Maltego allows you to identify key relationships between information and identify previously unknown relationships between them.

- https://www.maltego.com/
- https://gitlab.com/parrotsec/packages/maltego

### xplico

Network Forensic Analysis Tool (NFAT) The goal of Xplico is extract from an internet traffic capture the applications data contained. For example, from a pcap file Xplico extracts each email (POP, IMAP, and SMTP protocols), all HTTP contents, each VoIP call (SIP, MGCP, H323), FTP, TFTP, and so on. Xplico is not a network protocol analyzer.

- https://www.xplico.org
- https://gitlab.com/parrotsec/packages/xplico


## Reverse Engineering


### awesome-canbus

:articulated_lorry: Awesome CAN bus tools, hardware and resources for Cyber Security Researchers, Reverse Engineers, and Automotive Electronics Enthusiasts.

- GitHub: https://github.com/iDoka/awesome-canbus
- Documentation: https://github.com/iDoka/awesome-canbus/blob/main/README.md
- Topics: automotive, automotive-security, awesome, awesome-list, bus-monitoring, can, can-bus, can-fd

### ipatool

Command-line tool that allows searching and downloading app packages (known as ipa files) from the iOS App Store

- GitHub: https://github.com/majd/ipatool
- Documentation: https://github.com/majd/ipatool/blob/main/README.md
- Topics: apple, appstore, cli, command-line, command-line-tool, go, golang, golang-library

### jboss-autopwn

JBoss script for obtaining remote shell access This JBoss script deploys a JSP shell on the target JBoss AS server. Once deployed, the script uses its upload and command execution capability to provide an interactive session. Features include: - Multiplatform support - tested on Windows, Linux and Mac targets - Support for bind and reverse bind shells - Meterpreter shells and VNC support for Windows targets

- https://github.com/SpiderLabs/jboss-autopwn
- https://gitlab.com/parrotsec/packages/jboss-autopwn

### mitmproxy

SSL-capable man-in-the-middle HTTP proxy mitmproxy is an interactive man-in-the-middle proxy for HTTP and HTTPS. It provides a console interface that allows traffic flows to be inspected and edited on the fly. Also shipped is mitmdump, the command-line version of mitmproxy, with the same functionality but without the frills. Think tcpdump for HTTP. Features: - intercept and modify HTTP and HTTPS requests and responses and modify them on the fly - save HTTP conversations for later replay and analysis - replay the client-side of an HTTP conversation - reverse proxy mode to forward traffic to a specified server - transparent proxy mode on OSX and Linux - make scripted changes to HTTP traffic using Python - SSL/TLS certificates for interception are generated on the fly - ... This package contains the python-pathod module (previously provided by other source package). The python-netlib module was also included but it has been dropped by upstream in version 1.0.

- https://mitmproxy.org
- https://gitlab.com/parrotsec/packages/mitmproxy

### odat

Oracle Database Attacking Tool This package contains the ODAT (Oracle Database Attacking Tool), an open source penetration testing tool that tests the security of Oracle Databases remotely. Usage examples of ODAT: * You have an Oracle database listening remotely and want to find valid SIDs and credentials in order to connect to the database * You have a valid Oracle account on a database and want to escalate your privileges to become DBA or SYSDBA * You have a Oracle account and you want to execute system commands (e.g. reverse shell) in order to move forward on the operating system hosting the database

- https://github.com/quentinhardy/odat
- https://gitlab.com/parrotsec/packages/odat

### pwncat

netcat on steroids This package contains Netcat on steroids with Firewall, IDS/IPS evasion, bind and reverse shell, self-injecting shell and port forwarding magic - and its fully scriptable with Python (PSE).

- https://github.com/cytopia/pwncat
- https://gitlab.com/parrotsec/packages/pwncat

### rev-proxy-grapher

Reverse proxy grapher This package contains a useful little tool that will generate a nice graphviz graph illustrating your reverse proxy flow. It takes a manually curated YAML file describing the topology of your network, proxy definitions, and optionally a collection of nmap output files for additional port/service information and output a graph in any format supported by graphviz.

- https://github.com/mricon/rev-proxy-grapher
- https://gitlab.com/parrotsec/packages/rev-proxy-grapher

### rfcat

Swiss army knife of sub-GHz radio Rfcat is a sub GHz analysis tool. The goals of the project are to reduce the time for security researchers to create needed tools for analyzing unknown targets, to aid in reverse-engineering of hardware.

- https://github.com/atlas0fd00m/rfcat
- https://gitlab.com/parrotsec/packages/rfcat

### rizin-cutter

GUI for rizin reverse engineering framework Cutter is a Qt based GUI for reverse engineering binaries, which makes use of the rizin framework. Advanced users are expected to use the rizin CLI tools instead, which are much more powerful.

- https://rizin.re/
- https://gitlab.com/parrotsec/packages/rizin-cutter

### villain

High level C2 framework Villain is a C2 framework that can handle multiple TCP socket & HoaxShell-based reverse shells, enhance their functionality with additional features and share them among connected sibling servers.

- https://github.com/t3l3machus/Villain
- https://gitlab.com/parrotsec/packages/villain

### wifipumpkin3

Powerful framework for rogue access point attack This package contains a powerful framework for rogue access point attack, written in Python, that allow and offer to security researchers, red teamers and reverse engineers to mount a wireless network to conduct a man-in-the-middle attack.

- https://github.com/P0cL4bs/wifipumpkin3
- https://gitlab.com/parrotsec/packages/wifipumpkin3


## Vulnerability Research


### vuls

Agent-less vulnerability scanner for Linux, FreeBSD, Container, WordPress, Programming language libraries, Network devices

- GitHub: https://github.com/future-architect/vuls
- Official site: https://vuls.io/
- Documentation: https://github.com/future-architect/vuls/blob/master/README.md
- Topics: administrator, cybersecurity, freebsd, go, golang, linux, security, security-audit

### jok3r

Jok3r v3 BETA 2 - Network and Web Pentest Automation Framework

- GitHub: https://github.com/koutto/jok3r
- Official site: https://www.jok3r-framework.com
- Documentation: https://github.com/koutto/jok3r/blob/master/README.md
- Topics: automation, automation-framework, docker, exploiting-vulnerabilities, framework, hacking, hacking-tool, network

### mutillidae

OWASP Mutillidae II is a free, open-source, deliberately vulnerable web application providing a target for web-security training. This is an easy-to-use web hacking environment designed for labs, security enthusiasts,...

- GitHub: https://github.com/webpwnized/mutillidae
- Documentation: https://github.com/webpwnized/mutillidae/blob/main/README.md
- Topics: 10, application, appsec, cybersecurity, owasp, owasp-top-10, penetration-testing, security

### cve-mcp-server

Production-grade MCP server giving Claude 27 security intelligence tools across 21 APIs — CVE lookup, EPSS scoring, CISA KEV, MITRE ATT&CK, Shodan, VirusTotal, and more.

- GitHub: https://github.com/mukul975/cve-mcp-server
- Official site: https://www.mahipal.engineer/CVE-MCP-Server/
- Documentation: https://github.com/mukul975/cve-mcp-server/blob/main/README.md
- Topics: cisa-kev, claude-ai, cve, cybersecurity, devsecops, epss, fastmcp, mcp

### Hacking-Tools

A curated list of penetration testing and ethical hacking tools, organized by category. This compilation includes tools from Kali Linux and other notable sources.

- GitHub: https://github.com/yogsec/Hacking-Tools
- Official site: https://linktr.ee/abhinavsingwal
- Documentation: https://github.com/yogsec/Hacking-Tools/blob/main/README.md
- Topics: abhinav-singwal, blue-team, bugbounty, cybersecurity, ethical-hacking-tools, hackers, hacking, hacking-tools

### commix

Automated All-in-One OS Command Injection and Exploitation Tool This package contains Commix (short for [comm]and [i]njection e[x]ploiter). It has a simple environment and it can be used, from web developers, penetration testers or even security researchers to test web applications with the view to find bugs, errors or vulnerabilities related to command injection attacks. By using this tool, it is very easy to find and exploit a command injection vulnerability in a certain vulnerable parameter or string. Commix is written in Python programming language.

- https://commixproject.com
- https://gitlab.com/parrotsec/packages/commix

### defectdojo

security orchestration and vulnerability management platform This package contains a security orchestration and vulnerability management platform. DefectDojo allows you to manage your application security program, maintain product and application information, triage vulnerabilities and push findings to systems like JIRA and Slack. DefectDojo enriches and refines vulnerability data using a number of heuristic algorithms that improve with the more you use the platform.

- https://github.com/DefectDojo/django-DefectDojo
- https://gitlab.com/parrotsec/packages/defectdojo

### gvm-tools

Remote control the Greenbone Vulnerability Manager The Greenbone Vulnerability Management Tools or gvm-tools in short are a collection of tools that help with remote controlling a Greenbone Security Manager (GSM) appliance and its underlying Greenbone Vulnerability Manager (GVM). The tools essentially aid accessing the communication protocols GMP (Greenbone Management Protocol) and OSP (Open Scanner Protocol). This module is comprised of interactive and non-interactive clients. The programming language Python is supported directly for interactive scripting. But it is also possible to issue remote GMP/OSP commands without programming in Python.

- https://www.greenbone.net/
- https://gitlab.com/parrotsec/packages/gvm-tools

### joomscan

OWASP Joomla Vulnerability Scanner Project This package contains JoomScan, short for [Joom]la Vulnerability [Scan]ner. It's a project in perl programming language to detect Joomla CMS vulnerabilities and analysis them.

- https://www.owasp.org/index.php/Category:OWASP_Joomla_Vulnerability_Scanner_Project
- https://gitlab.com/parrotsec/packages/joomscan

### metasploit-framework

Framework for exploit development and vulnerability research The Metasploit Framework is an open source platform that supports vulnerability research, exploit development, and the creation of custom security tools.

- https://www.metasploit.com/
- https://gitlab.com/parrotsec/packages/metasploit-framework

### notus-scanner

vulnerable products detection (Python 3) Notus Scanner detects vulnerable products in a system environment. The scanning method is to evaluate internal system information. It does this very fast and even detects currently inactive products because it does not need to interact with each of the products. To report about vulnerabilities, Notus Scanner receives collected system information on the one hand and accesses the vulnerability information from the feed service on the other. Both input elements are in table form: the system information is specific to each environment and the vulnerability information is specific to each system type. This is a component of the Greenbone Vulnerability Management framework.

- https://github.com/greenbone/notus-scanner
- https://gitlab.com/parrotsec/packages/notus-scanner

### pocsuite3

Open-sourced remote vulnerability testing framework Pocsuite3 is an open-sourced remote vulnerability testing and proof-of-concept development framework developed by the Knownsec 404 Team. It comes with a powerful proof-of-concept engine, many nice features for the ultimate penetration testers and security researchers.

- https://pocsuite.org
- https://gitlab.com/parrotsec/packages/pocsuite3

### python-gvm

Greenbone Vulnerability Management Python Library (common documentation) This module gvm contains the Greenbone Vulnerability Management Python API library. It's a collection of APIs that help with remote controlling a Greenbone Security Manager (GSM) appliance and its underlying Greenbone Vulnerability Manager (GVM). The library essentially abstracts accessing the communication protocols Greenbone Management Protocol (GMP) and Open Scanner Protocol (OSP). This is the common documentation package.

- https://github.com/greenbone/python-gvm
- https://gitlab.com/parrotsec/packages/python-gvm

### syft

CLI tool for generating a SBOM from container images and filesystems This package contains a CLI tool and Go library for generating a Software Bill of Materials (SBOM) from container images and filesystems. Exceptional for vulnerability detection when used with a scanner like Grype. * Generates SBOMs for container images, filesystems, archives, and more to discover packages and libraries * Supports OCI, Docker and Singularity image formats * Linux distribution identification * Works seamlessly with Grype (a fast, modern vulnerability scanner) * Able to create signed SBOM attestations using the in-toto specification * Convert between SBOM formats, such as CycloneDX, SPDX, and Syft's own format.

- https://github.com/anchore/syft
- https://gitlab.com/parrotsec/packages/syft

### uniscan

LFI, RFI, and RCE vulnerability scanner Uniscan is a simple Remote File Include, Local File Include and Remote Command Execution vulnerability scanner.

- https://sourceforge.net/projects/uniscan/
- https://gitlab.com/parrotsec/packages/uniscan

### wpscan

Black box WordPress vulnerability scanner WPScan scans remote WordPress installations to find security issues.

- https://wpscan.com/wordpress-security-scanner
- https://gitlab.com/parrotsec/packages/wpscan


## Malware Analysis


### turbo-scanner

A port scanner and service detection tool that uses 1000 goroutines at once to scan any hosts IP or FQDN with the sole purpose of testing your own network to ensure there are no malicious services running.

- GitHub: https://github.com/mytechnotalent/turbo-scanner
- Documentation: https://github.com/mytechnotalent/turbo-scanner/blob/main/README.md
- Topics: blue-team, blue-teams, cyber, cybersecurity, defensive-security, go, golang, malware

### clamav

ClamAV is an open source antivirus engine for detecting trojans, viruses, malware, and other malicious threats. It is commonly used for on-demand file scanning, mail gateway inspection, and automated signature updates in defensive workflows.

- GitHub: https://github.com/Cisco-Talos/clamav
- Official site: https://www.clamav.net/
- Documentation: https://docs.clamav.net/

### YARA

YARA is a pattern-matching toolkit widely used in malware research and threat hunting to identify suspicious files and behaviors with reusable detection rules. It is a foundational building block for signature-based malware triage and detection engineering.

- GitHub: https://github.com/VirusTotal/yara
- Documentation: https://yara.readthedocs.io/

### Loki

Loki is a simple IOC and YARA scanner designed for host-based threat detection. It is useful for incident response and compromise assessment where defenders want to scan endpoints against known indicators and rule sets.

- GitHub: https://github.com/Neo23x0/Loki
- Documentation: https://github.com/Neo23x0/Loki/blob/master/README.md

### signature-base

signature-base is a curated YARA signature and IOC database used by malware scanners and threat hunting tools such as Loki. It is a practical companion resource when building or maintaining detection content for malware analysis workflows.

- GitHub: https://github.com/Neo23x0/signature-base
- Documentation: https://github.com/Neo23x0/signature-base/blob/master/README.md

### malwoverview

Malwoverview is a first response tool for threat hunting across VirusTotal, Hybrid Analysis, URLHaus, Polyswarm, Malshare, Alien Vault, Malpedia, Malware Bazaar, ThreatFox, Triage, IPInfo, Shodan, AbuseIPDB, GreyNoise...

- GitHub: https://github.com/alexandreborges/malwoverview
- Official site: https://github.com/alexandreborges/malwoverview
- Documentation: https://github.com/alexandreborges/malwoverview/blob/master/README.md
- Topics: alienvault, cve, cve-search, cybersecurity, malpedia, malshare, malware, malware-analysis

### njrat-config-analyzer

Best RAT Builder Analysis Tool 2026 for Cybersecurity Education & Malware Detection

- GitHub: https://github.com/fintanpyren-coder/njrat-config-analyzer
- Documentation: https://github.com/fintanpyren-coder/njrat-config-analyzer/blob/main/README.md
- Topics: njrat, njrat-attacker, njrat-download

### dnschef

DNS proxy for penetration testers DNSChef is a highly configurable DNS proxy for Penetration Testers and Malware Analysts. A DNS proxy (aka "Fake DNS") is a tool used for application network traffic analysis among other uses. For example, a DNS proxy can be used to fake requests for "badguy.com" to point to a local machine for termination or interception instead of a real host somewhere on the Internet.

- https://github.com/iphelix/dnschef
- https://gitlab.com/parrotsec/packages/dnschef


## Cloud Security


### DevSecOps

Ultimate DevSecOps library

- GitHub: https://github.com/sottlmarek/DevSecOps
- Documentation: https://github.com/sottlmarek/DevSecOps/blob/master/README.md
- Topics: automation, awesome, awesome-list, aws, azure, ci-cd, cloud, containers

### cloudbrute

Package entry imported from the ParrotSec package index.

- https://github.com/0xsha/cloudbrute
- https://gitlab.com/parrotsec/packages/cloudbrute

### cloudscraper

Package entry imported from the ParrotSec package index.

- https://github.com/VeNoMouS/cloudscraper
- https://gitlab.com/parrotsec/packages/cloudscraper

### eksctl

official CLI for Amazon EKS (program) eksctl is a simple CLI tool for creating clusters on EKS - Amazon's new managed Kubernetes service for EC2. It is written in Go, and uses CloudFormation. You can create a cluster in minutes with just one command – **eksctl create cluster**!

- https://github.com/weaveworks/eksctl
- https://gitlab.com/parrotsec/packages/eksctl

### godoh

DNS-over-HTTPS Command & Control Proof of Concept This package contains a proof of concept Command and Control framework, written in Golang, that uses DNS-over-HTTPS as a transport medium. Currently supported providers include Google, Cloudflare but also contains the ability to use traditional DNS.

- https://github.com/sensepost/goDoH
- https://gitlab.com/parrotsec/packages/godoh


## Privacy and Anonymity


### anonsurf

Anonymization toolkit for Parrot Security OS AnonSurf is an anonymization toolkit that helps prevent tracking and surveillance of the end-user. AnonSurf creates a Tor transparent proxy using iptables to forward all traffic through the Tor network. It also disables IPv6 and clears application caches to prevent data leaks.

- https://www.parrotsec.org/
- https://gitlab.com/parrotsec/packages/anonsurf

### apispec-webframeworks

Web framework plugins for apispec (Python 3) This package contains apispec plugins for integrating with various web frameworks. The included plugins are: - apispec_webframeworks.bottle - apispec_webframeworks.flask - apispec_webframeworks.tornado This package installs the library for Python 3.

- https://github.com/marshmallow-code/apispec-webframeworks
- https://gitlab.com/parrotsec/packages/apispec-webframeworks

### apple-bleee

scripts to show what an attacker get from Apple devices This package contains experimental scripts. They are PoCs that show what an attacker get from Apple devices if they sniff Bluetooth traffic. To use these scripts you will need a Bluetooth adapter for sending BLE messages and Wi-Fi card supporting active monitor mode with frame injection for communication using AWDL (AirDrop).

- https://github.com/hexway/apple_bleee
- https://gitlab.com/parrotsec/packages/apple-bleee

### backintime

simple backup/snapshot system (common files) Back In Time is a framework for rsync and cron for the purpose of taking snapshots and backups of specified folders. It minimizes disk space use by taking a snapshot only if the directory has been changed, and hard links for unmodified files if it has. The user can schedule regular backups using cron. This is the common framework for Back In Time. For a graphical interface, install backintime-qt. To back up to SSH or encrypted filesystems, install the additional sshfs or encfs packages.

- https://github.com/bit-team/backintime
- https://gitlab.com/parrotsec/packages/backintime

### badldap

Fork of msldap for bloodyAD LDAP library for Microsoft Active Directory. This is a fork of the original msldap for use with bloodyAD.

- https://github.com/CravateRouge/badldap
- https://gitlab.com/parrotsec/packages/badldap

### beef-xss

Browser Exploitation Framework (BeEF) BeEF is short for The Browser Exploitation Framework. It is a penetration testing tool that focuses on the web browser. Amid growing concerns about web-born attacks against clients, including mobile clients, BeEF allows the professional penetration tester to assess the actual security posture of a target environment by using client-side attack vectors. Unlike other security frameworks, BeEF looks past the hardened network perimeter and client system, and examines exploitability within the context of the one open door: the web browser. BeEF will hook one or more web browsers and use them as beachheads for launching directed command modules and further attacks against the system from within the browser context.

- https://beefproject.com/
- https://gitlab.com/parrotsec/packages/beef-xss

### bloodhound

Six Degrees of Domain Admin, BloodHound CE This package contains BloodHound Community Edition, a single page Javascript web application. BloodHound uses graph theory to reveal the hidden and often unintended relationships within an Active Directory environment. Attackers can use BloodHound to easily identify highly complex attack paths that would otherwise be impossible to quickly identify. Defenders can use BloodHound to identify and eliminate those same attack paths. Both blue and red teams can use BloodHound to easily gain a deeper understanding of privilege relationships in an Active Directory environment.

- https://github.com/SpecterOps/BloodHound
- https://gitlab.com/parrotsec/packages/bloodhound

### bloodhound.py

ingestor for BloodHound, based on Impacket (Python 3) This package contains a Python based ingestor for BloodHound, based on Impacket. BloodHound.py currently has the following limitations: * Supports most, but not all BloodHound (SharpHound) features. Primary missing features are GPO local groups and some differences in session resolution between BloodHound and SharpHound. * Kerberos authentication support is not yet complete, but can be used from the updatedkerberos branch. This package installs the library for Python 3.

- https://github.com/dirkjanm/bloodhound.py
- https://gitlab.com/parrotsec/packages/bloodhound.py

### bloodyad

Active Directory Privilege Escalation Framework This tool can perform specific LDAP calls to a domain controller in order to perform AD privesc. bloodyAD supports authentication using cleartext passwords, pass-the-hash, pass-the-ticket or certificates and binds to LDAP services of a domain controller to perform AD privesc.

- https://github.com/CravateRouge/bloodyAD
- https://gitlab.com/parrotsec/packages/bloodyad

### bulk-extractor

Package entry imported from the ParrotSec package index.

- https://github.com/simsong/bulk_extractor
- https://gitlab.com/parrotsec/packages/bulk-extractor

### bytecode-viewer

Java 8+ Jar & Android APK Reverse Engineering Suite This package contains Bytecode Viewer (BCV). It is an Advanced Lightweight Java Bytecode Viewer, GUI Java Decompiler, GUI Bytecode Editor, GUI Smali, GUI Baksmali, GUI APK Editor, GUI Dex Editor, GUI APK Decompiler, GUI DEX Decompiler, GUI Procyon Java Decompiler, GUI Krakatau, GUI CFR Java Decompiler, GUI FernFlower Java Decompiler, GUI DEX2Jar, GUI Jar2DEX, GUI Jar-Jar, Hex Viewer, Code Searcher, Debugger and more. There is also a plugin system that will allow you to interact with the loaded classfiles, for example you can write a String deobfuscator, a malicious code searcher, or something else you can think of. You can either use one of the pre-written plugins, or write your own. It supports groovy scripting. Once a plugin is activated, it will execute the plugin with a ClassNode ArrayList of every single class loaded in BCV, this allows the user to handle it completely using ASM. It's currently being maintained and developed by Konloch.

- https://github.com/Konloch/bytecode-viewer
- https://gitlab.com/parrotsec/packages/bytecode-viewer

### certipy-ad

Tool for attacking AD Certificate Services Offensive tool for enumerating and abusing Active Directory Certificate Services (AD CS).

- https://github.com/ly4k/Certipy
- https://gitlab.com/parrotsec/packages/certipy-ad

### cisco-torch

Cisco device scanner The main feature that makes cisco-torch different from similar tools is the extensive use of forking to launch multiple scanning processes on the background for maximum scanning efficiency. Also, it uses several methods of application layer fingerprinting simultaneoulsy, if needed. We wanted something fast to discover remote Cisco hosts running Telnet, SSH, Web, NTP, TFTP and SNMP services and launch dicitionary attacks against the services discovered, including SNMP community attack (you would like the community.txt list :-) and TFTP servers (configuration file name bruteforcing with following config leeching). The tool can also get device configurationfiles automatically if SNMP RW community is found.

- https://gitlab.com/parrotsec/packages/cisco-torch

### cloud-enum

Multi-cloud open source intelligence tool cloud_enum enumerates public resources matching user requested keywords in public clouds: Amazon Web Services: Open S3 Buckets Protected S3 Buckets Microsoft Azure: Storage Accounts Open Blob Storage Containers Hosted Databases Virtual Machines Web Apps Google Cloud Platform: Open GCP Buckets Protected GCP Buckets Google App Engine sites This program is useful for penetration testing (PENTEST) and network security analysis serving as OSINT.

- https://github.com/initstring/cloud_enum
- https://gitlab.com/parrotsec/packages/cloud-enum

### cmospwd

decrypt BIOS passwords from CMOS CmosPwd is a cross-platform tool to decrypt password stored in CMOS used to access a computer's BIOS setup. This application should work out of the box on most modern systems, but some more esoteric BIOSes may not be supported or may require additional steps.

- https://www.cgsecurity.org/wiki/CmosPwd
- https://gitlab.com/parrotsec/packages/cmospwd

### code-oss

Open Source package of vscode This package contains code-oss, a code editor with what developers need for their core edit-build-debug cycle. It provides comprehensive code editing, navigation, and understanding support along with lightweight debugging, a rich extensibility model, and lightweight integration with existing tools. This package is built from Microsoft open source code named code-oss.

- https://github.com/microsoft/vscode
- https://gitlab.com/parrotsec/packages/code-oss

### cosign

Code signing/transparency for containers and binaries (program) Signing OCI containers (and other artifacts) using Sigstore Cosign supports: * "Keyless signing" with the Sigstore public good Fulcio certificate authority and Rekor transparency log (default) * Hardware and KMS signing * Signing with a cosign generated encrypted private/public keypair * Container Signing, Verification and Storage in an OCI registry. * Bring-your-own PKI This package contains the command-line tool cosign.

- https://github.com/sigstore/cosign
- https://gitlab.com/parrotsec/packages/cosign

### crackmapexec

Swiss army knife for pentesting networks This package is a swiss army knife for pentesting Windows/Active Directory environments. From enumerating logged on users and spidering SMB shares to executing psexec style attacks, auto-injecting Mimikatz/Shellcode/DLL's into memory using Powershell, dumping the NTDS.dit and more. The biggest improvements over the above tools are: - Pure Python script, no external tools required - Fully concurrent threading - Uses **ONLY** native WinAPI calls for discovering sessions, users, dumping SAM hashes etc... - Opsec safe (no binaries are uploaded to dump clear-text credentials, inject shellcode etc...) Additionally, a database is used to store used/dumped credentals. It also automatically correlates Admin credentials to hosts and vice-versa allowing you to easily keep track of credential sets and gain additional situational awareness in large environments.

- https://github.com/byt3bl33d3r/CrackMapExec
- https://gitlab.com/parrotsec/packages/crackmapexec

### cryptsetup

disk encryption support - startup scripts Cryptsetup provides an interface for configuring encryption on block devices (such as /home or swap partitions), using the Linux kernel device mapper target dm-crypt. It features integrated Linux Unified Key Setup (LUKS) support. Cryptsetup is backwards compatible with the on-disk format of cryptoloop, but also supports more secure formats. This package includes support for automatically configuring encrypted devices at boot time via the config file /etc/crypttab. Additional features are cryptoroot support through initramfs-tools and several supported ways to read a passphrase or key. This package provides the cryptdisks_start and _stop wrappers, as well as luksformat.

- https://gitlab.com/cryptsetup/cryptsetup
- https://gitlab.com/parrotsec/packages/cryptsetup

### cvss

CVSS v2 and v3 computation utilities (Python 3) This package contains CVSS v2 and v3 computation utilities and interactive calculator. This package installs the library for Python 3.

- https://github.com/skontar/cvss
- https://gitlab.com/parrotsec/packages/cvss

### dbeaver

Universal Database Manager and SQL Client This package contains DBeaver Community Edition. It's Free multi-platform database tool for developers, SQL programmers, database administrators and analysts. Supports all popular databases: MySQL, PostgreSQL, SQLite, Oracle, DB2, SQL Server, Sybase, Teradata, Cassandra.

- http://dbeaver.jkiss.org/
- https://gitlab.com/parrotsec/packages/dbeaver

### debootstrap

Bootstrap a basic Debian system debootstrap is used to create a Debian base system from scratch, without requiring the availability of dpkg or apt. It does this by downloading .deb files from a mirror site, and carefully unpacking them into a directory which can eventually be chrooted into.

- https://gitlab.com/parrotsec/packages/debootstrap

### dex2jar

Tools to work with android .dex and java .class files dex2jar contains 4 compments: dex-reader is designed to read the Dalvik Executable (.dex/.odex) format. It has a light weight API similar with ASM. An example here dex-translator is designed to do the convert job. It reads the dex instruction to dex-ir format, after some optimize, convert to ASM format. dex-ir used by dex-translator, is designed to represent the dex instruction dex-tools tools to work with .class files.

- https://github.com/pxb1988/dex2jar/tree/2.x
- https://gitlab.com/parrotsec/packages/dex2jar

### dfvfs

Digital Forensics Virtual File System The Digital Forensics Virtual File System, provides read-only access to file-system objects from various storage media types and file formats. The goal of dfVFS is to provide a generic interface for accessing file-system objects, for which it uses several back-ends that provide the actual implementation of the various storage media types, volume systems and file systems.

- https://github.com/log2timeline/dfvfs
- https://gitlab.com/parrotsec/packages/dfvfs

### dirbuster

Web server directory brute-forcer DirBuster is a multi threaded java application designed to brute force directories and files names on web/application servers. Often is the case now of what looks like a web server in a state of default installation is actually not, and has pages and applications hidden within. DirBuster attempts to find these. However tools of this nature are often as only good as the directory and file list they come with. A different approach was taken to generating this. The list was generated from scratch, by crawling the Internet and collecting the directory and files that are actually used by developers! DirBuster comes a total of 9 different lists, this makes DirBuster extremely effective at finding those hidden files and directories. And if that was not enough DirBuster also has the option to perform a pure brute force, which leaves the hidden directories and files nowhere to hide.

- https://www.owasp.org/index.php/Category:OWASP_DirBuster_Project
- https://gitlab.com/parrotsec/packages/dirbuster

### dirsearch

Web path scanner This package contains is a command-line tool designed to brute force directories and files in webservers. As a feature-rich tool, dirsearch gives users the opportunity to perform a complex web content discovering, with many vectors for the wordlist, high accuracy, impressive performance, advanced connection/request settings, modern brute-force techniques and nice output.

- https://github.com/maurosoria/dirsearch
- https://gitlab.com/parrotsec/packages/dirsearch

### django-auditlog

Library for logging changes to Django models This library records modifications to Django model instances along with the user responsible for the change. It offers more flexibility compared to Django's default admin log and provides a JSON summary of modifications, allowing easy tracking of changes across models. Designed to be simple and efficient, it minimizes storage use by avoiding full version control, instead focusing on logging key attributes and actions for each change. It communicates directly with Django models to capture and store these logs, integrating seamlessly into Django-based applications.

- https://github.com/jazzband/django-auditlog
- https://gitlab.com/parrotsec/packages/django-auditlog

### django-crum

captures the current request and user in thread local storage (common documentation) This package contains Django-CRUM: Current Request User Middleware. It captures the current request and user in thread local storage. It enables apps to check permissions, capture audit trails or otherwise access the current request and user without requiring the request object to be passed directly. It also offers a context manager to allow for temporarily impersonating another user. It provides a signal to extend the built-in function for getting the current user, which could be helpful when using custom authentication methods or user models. This is the common documentation package.

- https://github.com/ninemoreminutes/django-crum/
- https://gitlab.com/parrotsec/packages/django-crum

### django-dbbackup

management commands to help backup and restore DB (common documentation) This package contains a Django application which provides management commands to help backup and restore your project database and media files with various storages such as Amazon S3, Dropbox, local file storage or any Django storage. This is the common documentation package.

- https://github.com/django-dbbackup/django-dbbackup
- https://gitlab.com/parrotsec/packages/django-dbbackup

### django-multiselectfield

new model field and form field (Python 3) This package contains a new model field and form field. With this you can get a multiple select from a choice. It stores to the database as a CharField of comma-separated values. This package installs the library for Python 3.

- https://github.com/goinnn/django-multiselectfield
- https://gitlab.com/parrotsec/packages/django-multiselectfield

### dnsgen

DNS generator This package provides a generator of a combination of domain names from the provided input. Combinations are created based on wordlist. Custom words are extracted per execution.

- https://github.com/ProjectAnte/dnsgen
- https://gitlab.com/parrotsec/packages/dnsgen

### donut-shellcode

Donut documentation Donut is a position-independent code that enables in-memory execution of VBScript, JScript, EXE, DLL files and dotNET assemblies. A module created by Donut can either be staged from a HTTP server or embedded directly in the loader itself. The module is optionally encrypted using the Chaskey block cipher and a 128-bit randomly generated key. After the file is loaded and executed in memory, the original reference is erased to deter memory scanners. The generator and loader support the following features: - Compression of input files with aPLib and LZNT1, Xpress, Xpress Huffman via RtlCompressBuffer. - Using entropy for API hashes and generation of strings. - 128-bit symmetric encryption of files. - Patching Antimalware Scan Interface (AMSI) and Windows Lockdown Policy (WLDP). - Patching command line for EXE files. - Patching exit-related API to avoid termination of host process. - Multiple output formats: C, Ruby, Python, PowerShell, Base64, C#, Hexadecimal. This is the common documentation package.

- https://github.com/TheWover/donut
- https://gitlab.com/parrotsec/packages/donut-shellcode

### dotdotpwn

Directory Traversal Fuzzer. DotDotPwn is a very flexible intelligent fuzzer to discover traversal directory vulnerabilities in software such as HTTP/FTP/TFTP servers, Web platforms such as CMSs, ERPs, Blogs, etc.

- https://dotdotpwn.blogspot.ca
- https://gitlab.com/parrotsec/packages/dotdotpwn

### dufflebag

Search exposed EBS volumes for secrets (program) Dufflebag is a tool that searches through public Elastic Block Storage (EBS) snapshots for secrets that may have been accidentally left in. The tool is organized as an Elastic Beanstalk ("EB", not to be confused with EBS) application, and definitely won't work if you try to run it on your own machine. Dufflebag has a lot of moving pieces because it's fairly nontrivial to actually read EBS volumes in practice. You have to be in an AWS environment, clone the snapshot, make a volume from the snapshot, attach the volume, mount the volume, etc... This is why it's made as an Elastic Beanstalk app, so it can automagically scale up or down however much you like, and so that the whole thing can be easily torn down when you're done with it.

- https://github.com/BishopFox/dufflebag
- https://gitlab.com/parrotsec/packages/dufflebag

### eapmd5pass

Tool for extracting and cracking EAP-MD5 EAP-MD5 is a legacy authentication mechanism that does not provide sufficient protection for user authentication credentials. Users who authenticate using EAP-MD5 subject themselves to an offline dictionary attack vulnerability. This tool reads from a live network interface in monitor-mode, or from a stored libpcap capture file, and extracts the portions of the EAP-MD5 authentication exchange. Once the challenge and response portions have been collected from this exchange, eapmd5pass will mount an offline dictionary attack against the user's password.

- https://www.willhackforsushi.com/?page_id=67
- https://gitlab.com/parrotsec/packages/eapmd5pass

### encryptpad

Text editor for password protecting and encrypting files Minimalist secure text editor and binary encryptor that implements RFC 4880 Open PGP format: symmetrically encrypted, compressed and integrity protected. The editor can protect files with passwords, key files or both.

- https://github.com/evpo/EncryptPad
- https://gitlab.com/parrotsec/packages/encryptpad

### endesive

library for digital signing and verification of signatures in docs Endesive is a Python module that has the ability to add and check digital signatures on PDF documents, emails and XMLs. This is useful for guarantee the protection and integrity of documents, making it difficult tamper with your content. Supports PDF digital signature standards defined in standards such as PAdES and CAdES. These standards are widely recognized for digital signatures on PDF documents. This library implements CAdES-B handler for signing and verifying PDF documents in Adobe.PPKLite/adbe.pkcs7.detached form. It can sign documents during generation using a modified version of pyfpdf which is included in this library. It can also sign documents generated by external programs. For ASN.1 implementation, pocote depends on the asn1crypto and cryptography libraries. Just like for certificate verification, the package recommends "CertValidator" as a dependency. Also implements S/MIME handler which can encrypt and decrypt S/MIME messages using a public RSA key, in AES-128/192/256 CBC/OFB modes. It can also sign and verify S/MIME messages. Still, the package is capable of implementing XADES BES/T with an enveloped and enveloping format, creating signed XML files. In addition to all the implementations, the package is also capable of implementing CMS, enabling the signing and verification of simple text files with separate signature files. This package installs the library for Python 3.

- https://github.com/m32/endesive
- https://gitlab.com/parrotsec/packages/endesive

### enum4linux

Enumerates info from Windows and Samba systems Enum4linux is a tool for enumerating information from Windows and Samba systems. It attempts to offer similar functionality to enum.exe formerly available from www.bindview.com. It is written in PERL and is basically a wrapper around the Samba tools smbclient, rpclient, net and nmblookup. The samba package is therefore a dependency. Features include: RID Cycling (When RestrictAnonymous is set to 1 on Windows 2000) User Listing (When RestrictAnonymous is set to 0 on Windows 2000) Listing of Group Membership Information Share Enumeration Detecting if host is in a Workgroup or a Domain Identifying the remote Operating System Password Policy Retrieval (using polenum)

- https://labs.portcullis.co.uk/application/enum4linux/
- https://gitlab.com/parrotsec/packages/enum4linux

### enumiax

IAX protocol username enumerator enumIAX is an Inter Asterisk Exchange protocol username brute-force enumerator. enumIAX may operate in two distinct modes; Sequential Username Guessing or Dictionary Attack.

- https://enumiax.sourceforge.net/
- https://gitlab.com/parrotsec/packages/enumiax

### evil-winrm

ultimate WinRM shell for hacking/pentesting This package contains the ultimate WinRM shell for hacking/pentesting. WinRM (Windows Remote Management) is the Microsoft implementation of WS-Management Protocol. A standard SOAP based protocol that allows hardware and operating systems from different vendors to interoperate. Microsoft included it in their Operating Systems in order to make life easier to system administrators. This program can be used on any Microsoft Windows Servers with this feature enabled (usually at port 5985), of course only if you have credentials and permissions to use it. So it could be used in a post-exploitation hacking/pentesting phase. The purpose of this program is to provide nice and easy-to-use features for hacking. It can be used with legitimate purposes by system administrators as well but the most of its features are focused on hacking/pentesting stuff. It is using PSRP (Powershell Remoting Protocol) for initializing runspace pools as well as creating and processing pipelines.

- https://github.com/Hackplayers/evil-winrm
- https://gitlab.com/parrotsec/packages/evil-winrm

### evil-winrm-py

Execute commands interactively on remote Windows machines using WinRM evil-winrm-py is a python-based tool for executing commands on remote Windows machines using the WinRM (Windows Remote Management) protocol. It provides an interactive shell with enhanced features like file upload/download, command history, and colorized output. It supports various authentication methods including NTLM, Pass-the-Hash, Certificate, and Kerberos.

- https://github.com/adityatelange/evil-winrm-py
- https://gitlab.com/parrotsec/packages/evil-winrm-py

### evilginx2

man-in-the-middle attack framework This package contains a man-in-the-middle attack framework used for phishing login credentials along with session cookies, which in turn allows to bypass 2-factor authentication protection. This tool is a successor to Evilginx, released in 2017, which used a custom version of nginx HTTP server to provide man-in-the-middle functionality to act as a proxy between a browser and phished website. Present version is fully written in GO as a standalone application, which implements its own HTTP and DNS server, making it extremely easy to set up and use.

- https://github.com/kgretzky/evilginx2
- https://gitlab.com/parrotsec/packages/evilginx2

### fastapi

modern, fast, web framework for building APIs, based on type hints FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. The key features are: * Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette * and Pydantic). One of the fastest Python frameworks available. * Fast to code: Increase the speed to develop features by about 200% to 300%. * (note1) * Fewer bugs: Reduce about 40% of human (developer) induced errors. (note1) * Intuitive: Great editor support. Completion everywhere. Less time debugging. * Easy: Designed to be easy to use and learn. Less time reading docs. * Short: Minimize code duplication. Multiple features from each parameter * declaration. Fewer bugs. * Robust: Get production-ready code. With automatic interactive documentation. * Standards-based: Based on (and fully compatible with) the open standards for * APIs: OpenAPI (previously known as Swagger) and JSON Schema. (note1) estimation based on tests on an internal development team, building production applications.

- https://github.com/tiangolo/fastapi
- https://gitlab.com/parrotsec/packages/fastapi

### feroxbuster

fast, simple, recursive content discovery tool written in Rust feroxbuster is a tool designed to perform Forced Browsing. Forced browsing is an attack where the aim is to enumerate and access resources that are not referenced by the web application, but are still accessible by an attacker. feroxbuster uses brute force combined with a wordlist to search for unlinked content in target directories. These resources may store sensitive information about web applications and operational systems, such as source code, credentials, internal network addressing, etc... This attack is also known as Predictable Resource Location, File Enumeration, Directory Enumeration, and Resource Enumeration.

- https://github.com/epi052/feroxbuster
- https://gitlab.com/parrotsec/packages/feroxbuster

### ferret-sidejack

Monitors data and extracts interesting data This tool extracts interesting bits from network traffic. One use is to feed the "hamster" tool. Another use is to dump the output intoa text file, then use indexers and grep programs to analyze it.

- https://github.com/robertdavidgraham/ferret
- https://gitlab.com/parrotsec/packages/ferret-sidejack

### ffuf

Fast web fuzzer written in Go (program) ffuf is a fast web fuzzer written in Go that allows typical directory discovery, virtual host discovery (without DNS records) and GET and POST parameter fuzzing. This program is useful for pentesters, ethical hackers and forensics experts. It also can be used for security tests.

- https://github.com/ffuf/ffuf
- https://gitlab.com/parrotsec/packages/ffuf

### flask-kvsession

Flask's session handling using server-side sessions (common documentation) This package contains server-side session replacement for Flask's signed client-based session management. Instead of storing data on the client, only a securely generated ID is stored on the client, while the actual session data resides on the server. This has two major advantages: - Clients no longer see the session information - It is possible to securely destroy sessions to protect against replay attacks. Other things are possible with server side session that are impossible with clients side sessions, like inspecting and manipulating data in absence of the client. This is the common documentation package.

- https://pypi.org/project/Flask-KVSession-fork
- https://gitlab.com/parrotsec/packages/flask-kvsession

### gnupg2

GNU privacy guard - a free PGP replacement (dummy transitional package) GnuPG is GNU's tool for secure communication and data storage. It can be used to encrypt data and to create digital signatures. It includes an advanced key management facility and is compliant with the proposed OpenPGP Internet standard as described in RFC4880. This is a dummy transitional package that provides symlinks from gpg2 to gpg.

- https://www.gnupg.org/
- https://gitlab.com/parrotsec/packages/gnupg2

### gobuster

Directory/file & DNS busting tool written in Go Gobuster is a tool used to brute-force: URIs (directories and files) in web sites, DNS subdomains (with wildcard support), Virtual Host names on target web servers, Open Amazon S3 buckets, Open Google Cloud buckets and TFTP servers. Gobuster is useful for pentesters, ethical hackers and forensics experts. It also can be used for security tests.

- https://github.com/OJ/gobuster
- https://gitlab.com/parrotsec/packages/gobuster

### golang-github-go-git-go-billy-v5

Missing interface filesystem abstraction for Go (library) This package implements an interface based on the os standard library, allowing to develop applications without dependency on the underlying storage. It makes it virtually free to implement mocks and testing over filesystem operations.

- https://github.com/go-git/go-billy
- https://gitlab.com/parrotsec/packages/golang-github-go-git-go-billy-v5

### golang-github-go-git-go-git-fixtures-v4

Several git fixtures to run go-git tests (library) This package contains git repository fixtures used by go-git.

- https://github.com/go-git/go-git-fixtures
- https://gitlab.com/parrotsec/packages/golang-github-go-git-go-git-fixtures-v4

### golang-github-ipinfo-go-ipinfo

Go library for IPInfo API This package contains the official Go client library for the IPinfo.io (https://ipinfo.io). IP address API, allowing you to lookup your own IP address, or get any of the following details for other IP addresses: * IP to Geolocation (https://ipinfo.io/ip-geolocation-api) (city, region, country, postal code, latitude and longitude) * IP to ASN (https://ipinfo.io/asn-api) (ISP or network operator, associated domain name, and type, such as business, hosting or company) * IP to Company (https://ipinfo.io/ip-company-api) (the name and domain of the business that uses the IP address) * IP to Carrier (https://ipinfo.io/ip-carrier-api) (the name of the mobile carrier and MNC and MCC for that carrier if the IP is used exclusively for mobile traffic)

- https://github.com/ipinfo/go
- https://gitlab.com/parrotsec/packages/golang-github-ipinfo-go-ipinfo

### golang-github-saintfish-chardet

Charset detector library for golang derived from ICU This package contains a library to automatically detect charset (http://en.wikipedia.org/wiki/Character_encoding) of texts for Go programming language (http://golang.org/). It's based on the algorithm and data in ICU (http://icu-project.org/)'s implementation.

- https://github.com/saintfish/chardet
- https://gitlab.com/parrotsec/packages/golang-github-saintfish-chardet

### gsad

remote network security auditor - web interface The Greenbone Security Assistant HTTP Server connects to the Greebone Vulnerability Manager "gvmd" to provide a full-featured user interface for vulnerability management. This tools was initially provided by the package greenbone-security-assistant.

- https://www.greenbone.net
- https://gitlab.com/parrotsec/packages/gsad

### gvm

remote network security auditor - metapackage and useful scripts The Greenbone Vulnerability Manager is a modular security auditing tool, used for testing remote systems for vulnerabilities that should be fixed. This package installs all the required packages. It provides scripts to setup, start and stop the GVM services. The tool was previously named OpenVAS.

- https://www.greenbone.net/
- https://gitlab.com/parrotsec/packages/gvm

### gvm-libs

remote network security auditor - static libraries and headers The Open Vulnerability Assessment System is a modular security auditing tool, used for testing remote systems for vulnerabilities that should be fixed. It is made up of two parts: a server, and a client. The server/daemon, gvmd, is in charge of the attacks, whereas the client, gvm-tools, provides an X11/GTK+ user interface. This package contains the required static libraries and headers.

- https://www.greenbone.net/
- https://gitlab.com/parrotsec/packages/gvm-libs

### gvmd

Manager Module of Greenbone Vulnerability Manager The Greenbone Vulnerability Manager is the central management service between security scanners and the user clients. It manages the storage of any vulnerability management configurations and of the scan results. Access to data, control commands and workflows is offered via the XML-based Greenbone Management Protocol (GMP). The primary scanner, openVAS Scanner is controlled directly via protocol OTP while any other remote scanner is coupled with the Open Scanner Protocol (OSP). This package contains the gvmd files architecture dependent.

- https://www.greenbone.net/
- https://gitlab.com/parrotsec/packages/gvmd

### heartleech

Scanner detecting systems vulnerable to the heartbleed OpenSSL bug This is a typical "heartbleed" tool. It can scan for systems vulnerable to the bug, and then be used to download them. Some important features: * conclusive/inconclusive verdicts as to whether the target is vulnerable * bulk/fast download of heartbleed data into a large files for offline processing using many threads * automatic retrieval of private keys with no additional steps * some limited IDS evasion * STARTTLS support * IPv6 support * Tor/Socks5n proxy support * extensive connection diagnostic information

- https://github.com/robertdavidgraham/heartleech
- https://gitlab.com/parrotsec/packages/heartleech

### hexinject

Versatile packet injector and sniffer HexInject is a very versatile packet injector and sniffer, that provide a command-line framework for raw network access. It's designed to work together with others command-line utilities, and for this reason it facilitates the creation of powerful shell scripts capable of reading, intercepting and modifying network traffic in a transparent manner.

- https://hexinject.sourceforge.net/
- https://gitlab.com/parrotsec/packages/hexinject

### hostapd-wpe

Modified hostapd to facilitate AP impersonation attacks This package contains hostapd modified with hostapd-wpe.patch. It implements IEEE 802.1x Authenticator and Authentication Server impersonation attacks to obtain client credentials, establish connectivity to the client, and launch other attacks where applicable. hostapd-wpe supports the following EAP types for impersonation: 1. EAP-FAST/MSCHAPv2 (Phase 0) 2. PEAP/MSCHAPv2 3. EAP-TTLS/MSCHAPv2 4. EAP-TTLS/MSCHAP 5. EAP-TTLS/CHAP 6. EAP-TTLS/PAP Once impersonation is underway, hostapd-wpe will return an EAP-Success message so that the client believes they are connected to their legitimate authenticator. For 802.11 clients, hostapd-wpe also implements Karma-style gratuitous probe responses. Inspiration for this was provided by JoMo-Kun's patch for older versions of hostapd. http://www.foofus.net/?page_id=115 hostapd-wpe also implements CVE-2014-0160 (Heartbleed) attacks against vulnerable clients. Inspiration for this was provided by the Cupid PoC: https://github.com/lgrangeia/cupid hostapd-wpe logs all data to stdout and hostapd-wpe.log

- https://github.com/aircrack-ng/aircrack-ng/tree/master/patches/wpe
- https://gitlab.com/parrotsec/packages/hostapd-wpe

### htshells

Self contained htaccess shells and attacks htshells is a series of web based attacks based around the .htaccess files. Most of the attacks are centered around two attack categories. Remote code/ command execution and information disclosure. These attacks are intended for use during penetration tests or security assessments. It was created to get shell in a CMS that restricted uploads based on extension and placed each uploaded file in it's own directory.

- https://github.com/wireghoul/htshells
- https://gitlab.com/parrotsec/packages/htshells

### imhex

Hex Editor for Reverse Engineers, Programmers This package contains a Hex Editor for Reverse Engineers, Programmers and people who value their retinas when working at 3 AM.

- https://github.com/WerWolv/ImHex
- https://gitlab.com/parrotsec/packages/imhex

### imhex-patterns

ImHex Database This package contains a database for files to use with the ImHex Hex Editor. It currently contains: * Patterns - Binary Format definitions for the Pattern Language * Pattern Libraries - Libraries that make using the Pattern Language easier * Magic Files - Custom magic file definitions for the use with libmagic * Encodings - Custom encodings in the .tbl format * Data Processor Nodes - Custom nodes made for ImHex's Data Processor * Themes - Custom themes for ImHex * Constants - Constants definition files * Scripts - Various scripts to generate code or automate some tasks * Yara - Custom Yara rules

- https://github.com/WerWolv/ImHex-Patterns
- https://gitlab.com/parrotsec/packages/imhex-patterns

### instaloader

Instagram automatic photo downloader Instaloader downloads photos from Instagram, including public and private profiles, hashtags, user stories, feeds and saved media. How as well as comments, geotags and captions for each post. It automatically detects profile name changes and renames the target directory accordingly. It also allows for refined customization of filters and where to store downloaded media be able to detect automatically stop previously interrupted download interactions.

- https://github.com/instaloader/instaloader
- https://gitlab.com/parrotsec/packages/instaloader

### jadx

Dex to Java decompiler This package contains a Dex to Java decompiler. It contains a command line and GUI tools for produce Java source code from Android Dex and Apk files. Main features: - decompile Dalvik bytecode to java classes from APK, dex, aar and zip files - decode AndroidManifest.xml and other resources from resources.arsc - deobfuscator included jadx-gui features: - view decompiled code with highlighted syntax - jump to declaration - find usage - full text search

- https://github.com/skylot/jadx
- https://gitlab.com/parrotsec/packages/jadx

### jefferson

JFFS2 filesystem extraction tool (Python 3) This package contains a JFFS2 filesystem extraction tool. The main features are: * big-endian and little-endian support with auto-detection * zlib, rtime, LZMA, and LZO compression support * CRC checks - for now only enforced on hdr_crc * extraction of symlinks, directories, files, and device nodes * detection/handling of duplicate inode numbers. Occurs if multiple JFFS2 filesystems are found in one file and causes jefferson to treat segments as separate filesystems This package installs the library for Python 3.

- https://github.com/onekey-sec/jefferson
- https://gitlab.com/parrotsec/packages/jefferson

### john

active password cracking tool John the Ripper is a tool designed to help systems administrators to find weak (easy to guess or crack through brute force) passwords, and even automatically mail users warning them about it, if it is desired. Besides several crypt(3) password hash types most commonly found on various Unix flavors, supported out of the box are Kerberos AFS and Windows NT/2000/XP/2003 LM hashes, plus several more with contributed patches.

- https://github.com/magnumripper/JohnTheRipper
- https://gitlab.com/parrotsec/packages/john

### joplin

open source note taking and to-do application This package contains a free, open source note taking and to-do application, which can handle a large number of notes organised into notebooks. The notes are searchable, can be copied, tagged and modified either from the applications directly or from your own text editor. The notes are in Markdown format. Notes exported from Evernote via .enex files can be imported into Joplin, including the formatted content (which is converted to Markdown), resources (images, attachments, etc.) and complete metadata (geolocation, updated time, created time, etc.). Plain Markdown files can also be imported. The notes can be synchronised with various cloud services including Nextcloud, Dropbox, OneDrive, WebDAV or the file system (for example with a network directory). When synchronising the notes, notebooks, tags and other metadata are saved to plain text files which can be easily inspected, backed up and moved around.

- https://github.com/laurent22/joplin
- https://gitlab.com/parrotsec/packages/joplin

### js2py

Pure Python JavaScript Translator/Interpreter (Python 3) This package contains a Pure Python JavaScript Translator/Interpreter. It translates JavaScript to Python code. Js2Py is able to translate and execute virtually any JavaScript code. This package installs the library for Python 3.

- https://github.com/PiotrDabkowski/Js2Py
- https://gitlab.com/parrotsec/packages/js2py

### jsp-file-browser

File browser java server page This package contains an easy to use and easy to install file browser java server page. This JSP program allows remote web-based file access and manipulation. Features: - Create, copy, move, rename and delete files and directories - Shortkeys - View Files (pictures, movies, pdf, html,...) - Javascript filename filter - Edit textfiles - Upload files to the server (Status via Upload monitor) - Download files from the server - Download groups of files and folders as a single zip file that is created on the fly - Execute native commands on the server (e.g ls, tar, chmod,...) - View entries and unpack zip, jar, war and gz files on the server - Just one file, very easy to install (in fact, just copy it to the server) - Customizable layout via css file - Restrict file access via black or whitelist - Changeable to a read-only (with or without upload) solution Jsp file browser should work on any JSP1.1 compatible server (e.g. Tomcat>=3.0). It has been tested on Tomcat 4.0 and 5.5, Resin 2.1.7 and Jetty.

- https://www.vonloesch.de/filebrowser.html
- https://gitlab.com/parrotsec/packages/jsp-file-browser

### lbd

Load balancer detector Checks if a given domain uses load-balancing.

- http://ge.mine.nu/code/
- https://gitlab.com/parrotsec/packages/lbd

### libnet-pcaputils-perl

Utility routines for Net::Pcap module Net::PcapUtils is a module to sit in front of Net::Pcap in order to hide some of the pcap(3) initialisation by providing sensible defaults. This enables a programmer to easily write small, specific scripts for a particular purpose without having to worry about too many details. The functions implemented in Net::PcapUtils are named after those in Net::Pcap. The loop function sits in a loop and executes a callback for each packet received, while next retrieves the next packet from the network device, and open returns an opened packet descriptor suitable for use with other Net::Pcap routines.

- https://metacpan.org/release/Net-PcapUtils
- https://gitlab.com/parrotsec/packages/libnet-pcaputils-perl

### libtaxii

library for handling Trusted Automated eXchange of Indicator Information (common documentation) The package contains a Python library for handling Trusted Automated eXchange of Indicator Information (TAXII™) v1.x Messages and invoking TAXII Services. This is the common documentation package.

- https://github.com/TAXIIProject/libtaxii
- https://gitlab.com/parrotsec/packages/libtaxii

### live-build

Live System Build Components The Debian Live project maintains the components to build Debian based Live systems and the official Debian Live images themselves. live-build contains the components to build a live system from a configuration directory.

- https://wiki.debian.org/DebianLive
- https://gitlab.com/parrotsec/packages/live-build

### masky

library to remotely dump domain users' credentials thanks to an ADCS (Python 3) This package contains a library providing an alternative way to remotely dump domain users' credentials thanks to an ADCS. A command line tool has been built on top of this library in order to easily gather PFX, NT hashes and TGT on a larger scope. This tool does not exploit any new vulnerability and does not work by dumping the LSASS process memory. Indeed, it only takes advantage of legitimate Windows and Active Directory features (token impersonation, certificate authentication via kerberos & NT hashes retrieval via PKINIT). This package installs the library for Python 3.

- https://github.com/Z4kSec/Masky
- https://gitlab.com/parrotsec/packages/masky

### mfterm

Terminal for working with Mifare Classic 1-4k Tags mfterm is a terminal interface for working with Mifare Classic tags. Tab completion on commands is available. Also, commands that have file name arguments provide tab completion on files. There is also a command history, like in most normal shells.

- https://github.com/4ZM/mfterm
- https://gitlab.com/parrotsec/packages/mfterm

### msfpc

MSFvenom Payload Creator (MSFPC) A quick way to generate various "basic" Meterpreter payloads using msfvenom which is part of the Metasploit framework.

- https://github.com/g0tmi1k/msfpc
- https://gitlab.com/parrotsec/packages/msfpc

### multimac

Create multiple MACs on an adapter Multimac is a linux virtual ethernet tap allocator to emulate and use multiple virtual interfaces (with different MAC addresses) on a LAN using a single network adapter.

- https://sourceforge.net/projects/multimac/
- https://gitlab.com/parrotsec/packages/multimac

### mutter

Example window manager using GNOME's window manager library Mutter is a Wayland display server and X11 window manager and compositor library. It contains functionality related to, among other things, window management, window compositing, focus tracking, workspace management, keybindings and monitor configuration. Internally it uses a fork of Cogl, a hardware acceleration abstraction library used to simplify usage of OpenGL pipelines, as well as a fork of Clutter, a scene graph and user interface toolkit. This package contains the mutter executable. It can be used as a standalone window manager, but is primarily intended for debugging.

- https://mutter.gnome.org/
- https://gitlab.com/parrotsec/packages/mutter

### neobolt

Neo4j Bolt Connector for Python 3 This package contains a Bolt connector library for Python. It is generally intended for use by a higher level driver. This package installs the library for Python 3.

- https://github.com/neo4j-drivers/neobolt
- https://gitlab.com/parrotsec/packages/neobolt

### openvas-scanner

remote network security auditor - scanner The Open Vulnerability Assessment System is a modular security auditing tool, used for testing remote systems for vulnerabilities that should be fixed. It is made up of two parts: a scan server, and a client. The scanner/daemon, openvassd, is in charge of the attacks, whereas the client, gvm-tools, provides an X11/GTK+ user interface. This package provides the scanner.

- https://www.greenbone.net/
- https://gitlab.com/parrotsec/packages/openvas-scanner

### ospd-openvas

OSP server implementation to allow GVM to remotely control an OpenVAS Scanner This package contains an OSP server implementation to allow GVM to remotely control OpenVAS. It is a command line tool with parameters to start a daemon which keeps waiting for instructions to update the feed of vulnerability tests and to start a scan. The second part of the interface is the redis store where the parameters about a scan task need to be placed and from where the results can be retrieved, being the unique communication channel between OSPD-OpenVAS and OpenVAS. Once running, you need to configure OpenVAS for the Greenbone Vulnerability Manager, for example via the web interface Greenbone Security Assistant. Then you can create scan tasks to use OpenVAS.

- https://www.greenbone.net/
- https://gitlab.com/parrotsec/packages/ospd-openvas

### parrot-updater

Parrot Updater - system update manager Parrot Updater is a tool designed to handle system updates via a graphical interface and provide periodical update reminders. Its main goal is to manage updates while respecting privacy and network opsec. This behavior avoids unwanted network noise when the system is used in critical monitored networks or during security audits, preventing third parties from identifying the OS through repository polling.

- http://www.parrotsec.org/
- https://gitlab.com/parrotsec/packages/parrot-updater

### parsero

Robots.txt audit tool Parsero is a free script written in Python which reads the Robots.txt file of a web server and looks at the Disallow entries. The Disallow entries tell the search engines what directories or files hosted on a web server mustn't be indexed. For example, "Disallow: /portal/login" means that the content on www.example.com/portal/login it's not allowed to be indexed by crawlers like Google, Bing, Yahoo... This is the way the administrator have to not share sensitive or private information with the search engines.

- https://github.com/behindthefirewalls/Parsero
- https://gitlab.com/parrotsec/packages/parsero

### pg-gvm

functionality for ical object manipulation The Greenbone Vulnerability Manager is the central management service between security scanners and the user clients. It manages the storage of any vulnerability management configurations and of the scan results. Access to data, control commands and workflows is offered via the XML-based Greenbone Management Protocol (GMP). The primary scanner, openVAS Scanner is controlled directly via protocol OTP while any other remote scanner is coupled with the Open Scanner Protocol (OSP). pg-gvm contains functionality for ical object manipulation for PostgreSQL.

- https://github.com/greenbone/pg-gvm
- https://gitlab.com/parrotsec/packages/pg-gvm

### phishery

Basic Auth Credential Harvester with Word Doc Template Injector This package contains a Simple SSL Enabled HTTP server with the primary purpose of phishing credentials via Basic Authentication. The power of phishery is best demonstrated by setting a Word document's template to a phishery URL. This causes Microsoft Word to make a request to the URL, resulting in an Authentication Dialog being shown to the end-user. The ability to inject any .docx file with a URL is possible using phishery's -i [in docx], -o [out docx], and -u [url] options.

- https://github.com/ryhanson/phishery
- https://gitlab.com/parrotsec/packages/phishery

### policykit-1

GObject introspection data for polkit polkit is a toolkit for defining and handling the policy that allows unprivileged processes to speak to privileged processes. It was previously named PolicyKit. This package contains introspection data for polkit. It can be used by packages using the GIRepository format to generate dynamic bindings.

- https://github.com/polkit-org/polkit/
- https://gitlab.com/parrotsec/packages/policykit-1

### poshc2

proxy aware C2 framework This package contains a proxy aware C2 framework used to aid penetration testers with red teaming, post-exploitation and lateral movement. PoshC2 is primarily written in Python3 and follows a modular format to enable users to add their own modules and tools, allowing an extendible and flexible C2 framework. Out-of-the-box PoshC2 comes PowerShell/C# and Python3 implants with payloads written in PowerShell v2 and v4, C++ and C# source code, a variety of executables, DLLs and raw shellcode in addition to a Python3 payload. These enable C2 functionality on a wide range of devices and operating systems, including Windows, *nix and OSX. Other notable features of PoshC2 include: - Consistent and Cross-Platform support using Docker. - Highly configurable payloads, including default beacon times, jitter, kill dates, user agents and more. - A large number of payloads generated out-of-the-box which are frequently updated and maintained to bypass common Anti-Virus products. - Auto-generated Apache Rewrite rules for use in a C2 proxy, protecting your C2 infrastructure and maintaining good operational security. - A modular format allowing users to create or edit C#, PowerShell or Python3 modules which can be run in-memory by the Implants. - Notifications on receiving a successful Implant, such as via text message or Pushover. - A comprehensive and maintained contextual help and an intelligent prompt with contextual auto-completion, history and suggestions. - Fully encrypted communications, protecting the confidentiality and integrity of the C2 traffic even when communicating over HTTP. - Client/Server format allowing multiple team members to utilise a single C2 server. - Extensive logging. Every action and response is timestamped and stored in a database with all relevant information such as user, host, implant number etc. In addition to this the C2 server output is directly logged to a separate file. - PowerShell-less implants that do not use System.Management.Automation.dll using C# or Python. - A free and open-source SOCKS Proxy by integrating with SharpSocks

- https://github.com/nettitude/PoshC2
- https://gitlab.com/parrotsec/packages/poshc2

### pskracker

collection of WPA/WPA2/WPS default keys generators/pingens This package contains a collection of WPA/WPA2/WPS default algorithms/password generators/pingens written in C. This is useful for testing/auditing wireless networks and contains bleeding edge algorithms.

- https://github.com/soxrok2212/PSKracker
- https://gitlab.com/parrotsec/packages/pskracker

### pymavlink

Python implementation of the MAVLink protocol (Python 3) This package contains Python implementation of the MAVLink protocol. It includes a source code generator (generator/mavgen.py) to create MAVLink protocol implementations for other programming languages as well. Also contains tools for analyzing flight logs. This package installs the library for Python 3.

- https://github.com/ArduPilot/pymavlink
- https://gitlab.com/parrotsec/packages/pymavlink

### pytest-factoryboy

factory_boy integration the pytest runner (common documentation) This package contains a factory_boy integration with the pytest runner. It makes it easy to combine factory approach to the test setup with the dependency injection, heart of the pytest fixtures. This is the common documentation package.

- https://github.com/pytest-dev/pytest-factoryboy
- https://gitlab.com/parrotsec/packages/pytest-factoryboy

### python-asset

Generalized Package Asset Loader (Python 3) This package contains a Generalized Package Asset Loader. It can load resources and symbols from a Python package, whether installed as a directory, an egg, or in source form. Also provides some other package-related helper methods, including asset.version(), asset.caller(), and asset.chunks(). This package installs the library for Python 3.

- https://github.com/metagriffin/asset
- https://gitlab.com/parrotsec/packages/python-asset

### python-dsinternals

Library to interact with Windows AD A Python native library containing necessary classes, functions and structures to interact with Windows Active Directory.

- https://github.com/p0dalirius/pydsinternals
- https://gitlab.com/parrotsec/packages/python-dsinternals

### python-emailahoy3

Utility to verify existence of an email address (Python 3) This package contains a Python email utility that verifies existence of an email address. This package is based on the un33k/python-emailahoy Python module which only run in Python 2. It has been refactored to work in Python 3. This package installs the library for Python 3.

- https://github.com/febrezo/python-emailahoy-3
- https://gitlab.com/parrotsec/packages/python-emailahoy3

### python-filedepot

file storage made easy for the Web World (common documentation) This package contains DEPOT, a framework for easily storing and serving files in web applications. This is the common documentation package.

- https://github.com/amol-/depot
- https://gitlab.com/parrotsec/packages/python-filedepot

### python-obfuscator

Module to obfuscate code (Python 3) This package contains Python obfuscator. This package installs the library for Python 3.

- https://github.com/davidteather/python-obfuscator
- https://gitlab.com/parrotsec/packages/python-obfuscator

### python-pyric

Wireless library for Linux (common documentation) This package contains a Linux only library providing wireless developers and pentesters the ability to identify, enumerate and manipulate their system's wireless cards programmatically in Python. Pentesting applications and scripts written in Python have increased dramatically in recent years. However, these tools still rely on Linux command lines tools to setup and prepare and restore the system for use. Until now. PyRIC is: - Pythonic: no ctypes, SWIG etc. PyRIC redefines C header files as Python and uses sockets to communicate with the kernel. - Self-sufficient: No third-party files used. PyRIC is completely self-contained. - Fast: (relatively speaking) PyRIC is faster than using command line tools through subprocess.Popen - Parseless: Get the output you want without parsing output from command line tools. Never worry about newer iw versions and having to rewrite your parsers. - Easy: If you can use iw, you can use PyRIC. At it's heart, PyRIC is a Python port of (a subset of) iw and by extension, a Python port of Netlink w.r.t nl80211 functionality. PyRIC puts iw, ifconfig, rfkill, udevadm, airmon-ng and macchanger in your hands (or your program). This is the common documentation package.

- http://github.com/sophron/pyric
- https://gitlab.com/parrotsec/packages/python-pyric

### python-simplekv

simple key-value store for binary data (Python 3) This package contains an API for very basic key-value stores used for small, frequently accessed data or large binary blobs. Its basic interface is easy to implement and it supports a number of backends, including the filesystem, SQLAlchemy, MongoDB, Redis and Amazon S3/Google Storage. This package installs the library for Python 3.

- https://github.com/mbr/simplekv
- https://gitlab.com/parrotsec/packages/python-simplekv

### pywebcopy

Python websites and webpages cloning at ease (Python 3) This package contains a Python library to clone websites and webpages: * Python websites and webpages cloning at ease * Web Scraping or Saving Complete webpages and websites * Web scraping and archiving tool: Archive any online website and its assets, css, js and images for offilne reading, storage or whatever reasons This package installs the library for Python 3.

- https://github.com/rajatomar788/pywebcopy
- https://gitlab.com/parrotsec/packages/pywebcopy

### pywerview

(partial) Python rewriting of PowerSploit's PowerView (Python 3) This package contains a (partial) Python rewriting of PowerSploit's PowerView. PowerView makes it so easy to find vulnerable machines, or list what domain users were added to the local Administrators group of a machine, and much more. This package installs the library for Python 3.

- https://github.com/the-useless-one/pywerview
- https://gitlab.com/parrotsec/packages/pywerview

### realtek-rtl8188eus-dkms

Realtek RTL8188EUS driver in DKMS format This package provides the source code for RTL8188EUS Linux driver (with monitor mode and frame injection) to be build with dkms. Kernel sources or headers are required to compile this module.

- https://github.com/gglluukk/rtl8188eus
- https://gitlab.com/parrotsec/packages/realtek-rtl8188eus-dkms

### realtek-rtl8814au-dkms

Realtek RTL8814AU driver in DKMS format for kernel < 6.15 This package provides the source code for RTL8814AU Linux driver (with monitor mode and frame injection) to be build with dkms. Kernel sources or headers are required to compile this module. This package is only required for kernel < 6.15

- https://github.com/morrownr/8814au
- https://gitlab.com/parrotsec/packages/realtek-rtl8814au-dkms

### realtek-rtl88xxau-dkms

Realtek RTL88xxAU driver in DKMS format This package provides the source code for RTL8812AU/21AU Linux driver (with monitor mode and frame injection) to be build with dkms. Kernel sources or headers are required to compile this module.

- https://github.com/aircrack-ng/rtl8812au
- https://gitlab.com/parrotsec/packages/realtek-rtl88xxau-dkms

### redsnarf

Pentesting tool for retrieving credentials from Windows workstations This package contains a pentesting / redteaming tool by Ed Williams for retrieving hashes and credentials from Windows workstations, servers and domain controllers using OpSec Safe Techniques. RedSnarf functionality includes: * Retrieval of local SAM hashes * Enumeration of user/s running with elevated system privileges and their corresponding lsa secrets password; * Retrieval of MS cached credentials; * Pass-the-hash; * Quickly identify weak and guessable username/password combinations (default of administrator/Password01); * The ability to retrieve hashes across a range; * Hash spraying

- https://github.com/nccgroup/redsnarf
- https://gitlab.com/parrotsec/packages/redsnarf

### rizin

A fork of the radare2 reverse engineering framework Rizin is portable and it can be used to analyze binaries, disassemble code, debug programs, as a forensics tool, as a scriptable command-line hexadecimal editor able to open disk files, and much more!

- https://rizin.re/
- https://gitlab.com/parrotsec/packages/rizin

### ruby-em-websocket

EventMachine based, async, Ruby WebSocket server It is an async Ruby based Websocket server which is based on EventMachine which supports all websocket protocols This library is a dependency of Jekyll; a simple, blog aware, static site generator.

- https://github.com/igrigorik/em-websocket
- https://gitlab.com/parrotsec/packages/ruby-em-websocket

### ruby-ethon

libcurl wrapper using ffi Very lightweight libcurl wrapper. In Greek mythology, Ethon, the son of Typhoeus and Echidna, is a gigantic eagle. So much for the history. In the modern world, Ethon is a very basic libcurl wrapper using ffi

- https://github.com/typhoeus/ethon
- https://gitlab.com/parrotsec/packages/ruby-ethon

### ruby-maxmind-db

Gem for reading MaxMind DB files This package contains a gem for reading MaxMind DB files. MaxMind DB is a binary file format that stores data indexed by IP address subnets (IPv4 or IPv6).

- https://github.com/maxmind/MaxMind-DB-Reader-ruby
- https://gitlab.com/parrotsec/packages/ruby-maxmind-db

### ruby-nokogiri

HTML, XML, SAX, and Reader parser for Ruby Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser. It is able to search documents via XPath or CSS3 selectors, and is a drop-in replacement for Hpricot (though not bug for bug).

- https://nokogiri.org
- https://gitlab.com/parrotsec/packages/ruby-nokogiri

### ruby-opt-parse-validator

Ruby OptionParser Validators This package contains an implementation of validators for the ruby OptionParser lib. It's mainly used in the CMSScanner gem to define the cli options available.

- https://github.com/wpscanteam/OptParseValidator
- https://gitlab.com/parrotsec/packages/ruby-opt-parse-validator

### sakis3g

Tool for establishing 3G connections Sakis3G is a tweaked shell script which is supposed to work out-of-the-box for establishing a 3G connection with any combination of modem or operator. It automagically setups your USB or Bluetooth™ modem, and may even detect operator settings. You should try it when anything else fails.

- http://www.sakis3g.org
- https://gitlab.com/parrotsec/packages/sakis3g

### sentrypeer

SIP peer to peer honeypot for VoIP SentryPeer is a distributed list of bad IP addresses and phone numbers collected via a SIP Honeypot. SentryPeer is a fraud detection tool. It lets bad actors try to make phone calls and saves the IP address they came from and number they tried to call. Those details can then be used to raise notifications at the service providers network and the next time a user/customer tries to call a collected number, you can act anyway you see fit. Traditionally this data is shipped to a central place, so you don't own the data you've collected. This project is all about Peer to Peer sharing of that data. The user owning the data and various Service Provider / Network Provider related feeds of the data is the key bit for me. I'm sick of all the services out there that keep it and sell it. If you've collected it, you should have the choice to keep it and/or opt in to share it with other SentryPeer community members via p2p methods.

- https://sentrypeer.org
- https://gitlab.com/parrotsec/packages/sentrypeer

### shellnoob

Shellcode writing toolkit Features: * convert shellcode between different formats and sources. Formats currently supported: asm, bin, hex, obj, exe, C, Python, ruby, pretty, safeasm, completec, shellstorm. (All details in the "Formats description" section.) * interactive asm-to-opcode conversion (and viceversa) mode. This is useful when you cannot use specific bytes in the shellcode and you want to figure out if a specific assembly instruction will cause problems. * support for both ATT & Intel syntax. Check the --intel switch. * support for 32 and 64 bits (when playing on x86_64 machine). Check the --64 switch. * resolve syscall numbers, constants, and error numbers * portable and easily deployable (it only relies on gcc/as/objdump and Python) And it just one self-contained Python script! * in-place development: you run ShellNoob directly on the target architecture * built-in support for Linux/x86, Linux/x86_64, Linux/ARM, FreeBSD/x86, FreeBSD/x86_64. * "*prepend breakpoint*" option. Check the -c switch. * read from stdin / write to stdout support (use "-" as filename) * uber cheap debugging: check the --to-strace and --to-gdb option! * Use ShellNoob as a Python module in your scripts! Check the "ShellNoob as a library" section. * Verbose mode shows the low-level steps of the conversion: useful to debug / understand / learn * Extra plugins: binary patching made easy with the --file-patch, --vm-patch, --fork-nopper options

- https://github.com/reyammer/shellnoob
- https://gitlab.com/parrotsec/packages/shellnoob

### shellter

Dynamic shellcode injection tool and dynamic PE infector Shellter is a dynamic shellcode injection tool aka dynamic PE infector. It can be used in order to inject shellcode into native Windows applications (currently 32-bit apps only). The shellcode can be something yours or something generated through a framework, such as Metasploit. Shellter takes advantage of the original structure of the PE file and doesn't apply any modification such as changing memory access permissions in sections (unless the user wants to), adding an extra section with RWE access, and whatever would look dodgy under an AV scan.

- https://www.shellterproject.com/
- https://gitlab.com/parrotsec/packages/shellter

### sherlock

Find usernames across social networks Sherlock relies on the site's designers providing a unique URL for a registered username. To determine if a username is available, Sherlock queries that URL, and uses to response to understand if there is a claimed username already there. Currently, the tool is capable of locating users on more than 300 social networks: Apple Developer, Arduino, Docker Hub, GitHub, GitLab, Facebook, BitCoinForum, CNET, IFTTT, Instagram, PlayStore PyPI, Scribd, Telegram, TikTok, Tinder etc.

- https://github.com/sherlock-project/sherlock
- https://gitlab.com/parrotsec/packages/sherlock

### silenttrinity

asynchronous, collaborative post-exploitation agent This package contains a modern, asynchronous, multiplayer & multiserver C2/post-exploitation framework powered by Python 3 and .NETs DLR. It's the culmination of an extensive amount of research into using embedded third-party .NET scripting languages to dynamically call .NET API's, a technique the author coined as BYOI (Bring Your Own Interpreter). The aim of this tool and the BYOI concept is to shift the paradigm back to PowerShell style like attacks (as it offers much more flexibility over traditional C# tradecraft) only without using PowerShell in anyway. Some of the main features that distinguish SILENTTRINITY are: - Multi-User & Multi-Server - Supports multi-user collaboration. Additionally, the client can connect to and control multiple Teamservers. - Client and Teamserver Built in Python 3.7 - Latest and greatest features of the Python language are used, heavy use of Asyncio provides ludicrous speeds. - Real-time Updates and Communication - Use of Websockets allow for real-time communication and updates between the Client and Teamserver. - Focus on Usability with an Extremely Modern CLI - Powered by prompt-toolkit. - Dynamic Evaluation/Compilation Using .NET Scripting Languages - The SILENTTRINITY implant Naga, is somewhat unique as it uses embedded third-party .NET scripting languages (e.g. Boolang) to dynamically compile/evaluate tasks, this removes the need to compile tasks server side, allows for real-time editing of modules, provides greater flexibilty and stealth over traditional C# based payloads and makes everything much more light-weight. - ECDHE Encrypted C2 Communication - SILENTTRINITY uses Ephemeral Elliptic Curve Diffie-Hellman Key Exchange to encrypt all C2 traffic between the Teamserver and its implant. - Fully Modular - Listeners, Modules, Stagers and C2 Channels are fully modular allowing operators to easily build their own. - Extensive logging - Every action is logged to a file. - Future proof - HTTPS/HTTP listeners are built on Quart & Hypercorn which also support HTTP2 & Websockets.

- https://github.com/byt3bl33d3r/SILENTTRINITY
- https://gitlab.com/parrotsec/packages/silenttrinity

### sipp

Traffic generator for the SIP protocol SIPp is a free Open Source test tool / traffic generator for the SIP protocol. It includes a few basic SipStone user agent scenarios (UAC and UAS) and establishes and releases multiple calls with the INVITE and BYE methods. It can also reads custom XML scenario files describing from very simple to complex call flows. It features the dynamic display of statistics about running tests (call rate, round trip delay, and message statistics), periodic CSV statistics dumps, TCP and UDP over multiple sockets or multiplexed with retransmission management and dynamically adjustable call rates.

- https://sipp.sourceforge.net/
- https://gitlab.com/parrotsec/packages/sipp

### snmpcheck

SNMP service enumeration tool Like to snmpwalk, snmpcheck allows you to enumerate the SNMP devices and places the output in a very human readable friendly format. It could be useful for penetration testing or systems monitoring.

- http://www.nothink.org/codes/snmpcheck/index.php
- https://gitlab.com/parrotsec/packages/snmpcheck

### spray

Password Spraying tool for Active Directory Credentials This package contains a Password Spraying tool for Active Directory Credentials. The script will password spray a target over a period of time. It requires password policy as input so accounts are not locked out. The package also provides a series of hand crafted password files for multiple languages. These have been crafted from the most common active directory passwords in various languages and all fit in the complex (1 Upper, 1 lower, 1 digit) category.

- https://github.com/Greenwolf/Spray
- https://gitlab.com/parrotsec/packages/spray

### spraykatz

tool able to retrieve credentials on Windows machines This package contains a tool without any pretention able to retrieve credentials on Windows machines and large Active Directory environments. It simply tries to procdump machines and parse dumps remotely in order to avoid detections by antivirus software as much as possible.

- https://github.com/aas-n/spraykatz
- https://gitlab.com/parrotsec/packages/spraykatz

### sqlsus

MySQL injection tool sqlsus is an open source MySQL injection and takeover tool, written in perl. Via a command line interface, you can retrieve the database(s) structure, inject your own SQL queries (even complex ones), download files from the web server, crawl the website for writable directories, upload and control a backdoor, clone the database(s), and much more... Whenever relevant, sqlsus will mimic a MySQL console output.

- https://sqlsus.sourceforge.net/
- https://gitlab.com/parrotsec/packages/sqlsus

### stix2-patterns

tool to check the syntax of the CTI STIX Pattern expressions (common documentation) This package contains software tool for checking the syntax of the Cyber Threat Intelligence (CTI) STIX Pattern expressions, which are used within STIX to express conditions (prepresented with the Cyber Observable data model) that indicate particular cyber threat activity. The repository contains source code, an ANTLR grammar, automated tests and associated documentation for the tool. The validator can be used as a command-line tool or as a Python library which can be included in other applications. This is the common documentation package.

- https://github.com/oasis-open/cti-pattern-validator
- https://gitlab.com/parrotsec/packages/stix2-patterns

### terraform

tool for building, changing, and versioning infrastructure This package contains a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions. Terraform enables you to safely and predictably create, change, and improve infrastructure. It is an open source tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned. The key features of Terraform are: * Infrastructure as Code: Infrastructure is described using a high- level configuration syntax. This allows a blueprint of your datacenter to be versioned and treated as you would any other code. Additionally, infrastructure can be shared and re-used. * Execution Plans: Terraform has a "planning" step where it generates an execution plan. The execution plan shows what Terraform will do when you call apply. This lets you avoid any surprises when Terraform manipulates infrastructure. * Resource Graph: Terraform builds a graph of all your resources, and parallelizes the creation and modification of any non-dependent resources. Because of this, Terraform builds infrastructure as efficiently as possible, and operators get insight into dependencies in their infrastructure. * Change Automation: Complex changesets can be applied to your infrastructure with minimal human interaction. With the previously mentioned execution plan and resource graph, you know exactly what Terraform will change and in what order, avoiding many possible human errors.

- https://github.com/hashicorp/terraform
- https://gitlab.com/parrotsec/packages/terraform

### tftpd32

Open source ipv6-ready TFTP server for Windows Tftpd32 is a free, opensource IPv6 ready application which includes DHCP, TFTP, DNS, SNTP and Syslog servers as well as a TFTP client. The TFTP client and server are fully compatible with TFTP option support (tsize, blocksize and timeout), which allow the maximum performance when transferring the data. Some extended features such as directory facility, security tuning, interface filtering; progress bars and early acknowledgments enhance usefulness and throughput of the TFTP protocol for both client and server. The included DHCP server provides unlimited automatic or static IP address assignment.

- https://tftpd32.jounin.net/tftpd32.html
- https://gitlab.com/parrotsec/packages/tftpd32

### torbrowser-launcher

helps download and run the Tor Browser Bundle Tor Browser Launcher is intended to make the Tor Browser Bundle (TBB) easier to maintain and use for GNU/Linux users. torbrowser-launcher handles downloading the most recent version of TBB for you, in your language and for your architecture. It also adds a "Tor Browser" application launcher to your operating system's menu. When you first launch Tor Browser Launcher, it will download TBB from https://www.torproject.org/ and extract it to ~/.local/share/torbrowser, and then execute it. Cache and configuration files will be stored in ~/.cache/torbrowser and ~/.config/torbrowser. Each subsequent execution after installation will simply launch the most recent TBB, which is updated using Tor Browser's own update feature.

- https://github.com/micahflee/torbrowser-launcher
- https://gitlab.com/parrotsec/packages/torbrowser-launcher

### trivy

comprehensive and versatile security scanner This package contains a comprehensive and versatile security scanner. Trivy has scanners that look for security issues, and targets where it can find those issues. It can find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more. Targets (what Trivy can scan): * Container Image * Filesystem * Git Repository (remote) * Virtual Machine Image * Kubernetes * AWS Scanners (what Trivy can find there): * OS packages and software dependencies in use (SBOM) * Known vulnerabilities (CVEs) * IaC issues and misconfigurations * Sensitive information and secrets * Software licenses

- https://github.com/aquasecurity/trivy
- https://gitlab.com/parrotsec/packages/trivy

### trufflehog

Searches through git repositories for secrets This package contains a utitlity to search through git repositories for secrets, digging deep into commit history and branches. This is effective at finding secrets accidentally committed.

- https://github.com/trufflesecurity/truffleHog
- https://gitlab.com/parrotsec/packages/trufflehog

### unix-privesc-check

Script to check for simple privilege escalation vectors Unix-privesc-checker is a script that runs on Unix systems (tested on Solaris 9, HPUX 11, Various Linuxes, FreeBSD 6.2). It tries to find misconfigurations that could allow local unprivileged users to escalate privileges to other users or to access local apps (e.g. databases). It is written as a single shell script so it can be easily uploaded and run (as opposed to un-tarred, compiled and installed). It can run either as a normal user or as root (obviously it does a better job when running as root because it can read more files).

- http://pentestmonkey.net/tools/audit/unix-privesc-check
- https://gitlab.com/parrotsec/packages/unix-privesc-check

### urlcrazy

Domain typo generator Generate and test domain typos and variations to detect and perform typo squatting, URL hijacking, phishing, and corporate espionage.

- https://www.morningstarsecurity.com/research/urlcrazy
- https://gitlab.com/parrotsec/packages/urlcrazy

### wce

Windows Credentials Editor Windows Credentials Editor (WCE) v1.3beta allows you to: NTLM authentication: * List logon sessions and add, change, list and delete associated credentials (e.g.: LM/NT hashes) * Perform pass-the-hash on Windows natively * Obtain NT/LM hashes from memory (from interactive logons, services, remote desktop connections, etc.) which can be used to authenticate to other systems. WCE can perform this task without injecting code, just by reading and decrypting information stored in Windows internal memory structures. It also has the capability to automatically switch to code injection when the aforementioned method cannot be performed.

- http://www.ampliasecurity.com/research.html
- https://gitlab.com/parrotsec/packages/wce

### wifi-honey

Wi-Fi honeypot In the case of WPA/WPA2, by running airodump-ng along side this you also end up capturing the first two packets of the four way handshake and so can attempt to crack the key with either aircrack-ng or coWPAtty. What this script does is to automate the setup process, it creates five monitor mode interfaces, four are used as APs and the fifth is used for airodump-ng. To make things easier, rather than having five windows all this is done in a screen session which allows you to switch between screens to see what is going on. All sessions are labelled so you know which is which.

- https://www.digininja.org/projects/wifi_honey.php
- https://gitlab.com/parrotsec/packages/wifi-honey

### winacl

Platform independent lib for interfacing windows security descriptors This package contains a platform independent library for interfacing windows security descriptors. This package installs the library for Python 3.

- https://github.com/skelsec/winacl
- https://gitlab.com/parrotsec/packages/winacl

### windows-privesc-check

Windows privilege escalation checking tool Windows-privesc-check is standalone executable that runs on Windows systems (tested on XP, Windows 7 only so far). It tries to find misconfigurations that could allow local unprivileged users to escalate privileges to other users or to access local apps (e.g. databases). It is written in python and converted to an executable using pyinstaller so it can be easily uploaded and run (as opposed to unzipping python + other dependencies). It can run either as a normal user or as Administrator (obviously it does a better job when running as Administrator because it can read more files).

- https://pentestmonkey.net/tools/windows-privesc-check
- https://gitlab.com/parrotsec/packages/windows-privesc-check

### winexe

Remote Windows-command executor Winexe remotely executes commands on Windows NT/2000/XP/2003 systems from GNU/Linux (and possibly also from other Unices capable of building the Samba 4 software package).

- https://sourceforge.net/projects/winexe
- https://gitlab.com/parrotsec/packages/winexe

### witnessme

Web Inventory tool This package contains a Web Inventory tool inspired by Eyewitness, its also written to be extensible allowing you to create custom functionality that can take advantage of the headless browser it drives in the back-end.

- https://github.com/byt3bl33d3r/WitnessMe
- https://gitlab.com/parrotsec/packages/witnessme

### zeek

passive network traffic analyzer Zeek is primarily a security monitor that inspects all traffic on a link in depth for signs of suspicious activity. More generally, however, Zeek supports a wide range of traffic analysis tasks even outside of the security domain, including performance measurements and helping with trouble-shooting. Zeek comes with built-in functionality for a range of analysis and detection tasks, including detecting malware by interfacing to external registries, reporting vulnerable versions of software seen on the network, identifying popular web applications, detecting SSH brute-forcing, validating SSL certificate chains, among others.

- http://www.zeek.org/
- https://gitlab.com/parrotsec/packages/zeek
