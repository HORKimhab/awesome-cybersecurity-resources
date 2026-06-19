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

## AI Agent Security and Tooling


### VoltAgent

Open-source TypeScript AI agent framework with built-in support for guardrails, MCP integration, observability, memory, workflows, and evals. While it is broader than cybersecurity alone, it is relevant for secure agent engineering and agent runtime governance.

- GitHub: https://github.com/VoltAgent/voltagent
- Official site: https://voltagent.dev/
- Documentation: https://voltagent.dev/docs/
- LLM guide: https://voltagent.dev/llms.txt

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
