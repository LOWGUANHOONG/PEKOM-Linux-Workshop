# 🚩 Learn to Hack: Where's The Flag?

An introductory cybersecurity workshop for university students — no prior experience required. By the end of this session you'll understand what cybersecurity actually is, how the field is organized, what a CTF (Capture The Flag) competition is, and you'll have solved your first flags using real industry tools.

---

## 📋 Workshop Agenda

| # | Segment | Duration |
|---|---------|----------|
| 1 | Welcome & Registration | 10 min |
| 2 | Cybersecurity Introduction & Fields / Career Paths | 20 min |
| 3 | Intro to CTF Competitions & Categories | 30 min |
| 4 | Kali Linux Overview (setup done pre-workshop) | 10 min |
| 5 | Tool Walkthrough: Nmap, Wireshark, Burp Suite, Metasploit | 30 min |
| 6 | ☕ Break | 10 min |
| 7 | Hands-On Lab (guided) | 60 min |
| 8 | Wrap-up, Resources & Certificates | 10 min |
Total: 3 hours

> ⚠️ **Please complete the [Pre-Workshop Setup](#-pre-workshop-setup-do-this-before-you-arrive) before attending.**

---

## 🧭 What is Cybersecurity? (Fields & Career Paths)

Cybersecurity isn't one job — it's an umbrella covering many specializations:

| Field | What they do |
|---|---|
| **Offensive Security / Pentesting** | Simulate attacks to find vulnerabilities before real attackers do |
| **Blue Team / SOC Analyst** | Monitor, detect, and respond to active threats |
| **Digital Forensics & Incident Response (DFIR)** | Investigate breaches, recover evidence, trace attacker activity |
| **Application Security (AppSec)** | Secure software during development (secure coding, code review) |
| **Cloud Security** | Secure AWS/Azure/GCP environments and configurations |
| **GRC (Governance, Risk & Compliance)** | Policies, audits, regulatory compliance (ISO 27001, PCI-DSS) |
| **Security Research** | Discover new vulnerabilities, publish CVEs, build tools |
| **Red Team** | Long-term, stealthy simulated adversary engagements |

CTF competitions are a great entry point because they let you sample offense, forensics, crypto, and web security all in one event — helping you figure out what you enjoy before committing to a specialization.

---

## 🏁 Introduction to CTF (Capture The Flag)

A CTF is a gamified cybersecurity competition where you solve challenges to find a hidden **flag** — a string like `flag{wkw4u837a@!d}` — proving you exploited or solved the challenge correctly.

### Common CTF Categories

| Category | What you do | Example |
|---|---|---|
| **Web Exploitation** | Find flaws in websites (SQLi, XSS, auth bypass) | Bypass a login form to reveal a flag |
| **Cryptography** | Decode/break ciphers and weak encryption | Decode a Base64 → Caesar cipher chain |
| **Forensics** | Analyze files, images, memory dumps, network captures | Extract a flag hidden in image metadata |
| **Reverse Engineering** | Analyze compiled binaries to understand their logic | Find a hardcoded password in a binary |
| **Pwn / Binary Exploitation** | Exploit memory corruption bugs | Buffer overflow to get shell access |
| **OSINT** | Find information from public sources | Locate a flag from a social media post |
| **Misc** | Anything that doesn't fit elsewhere | Steganography, esoteric puzzles |

### Practice Platforms (keep learning after today)
- [picoCTF](https://picoctf.org/) — beginner-friendly, always available
- [TryHackMe](https://tryhackme.com/) — guided rooms, browser-based
- [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/) — Linux/command-line fundamentals
- [HackTheBox](https://www.hackthebox.com/) — more advanced, real-world style
- [CTFtime](https://ctftime.org/) — calendar of live CTF competitions worldwide

---

## 🐉 Pre-Workshop Setup (do this BEFORE you arrive)

### Requirements
- Laptop with **8GB+ RAM** (4GB minimum, 8GB+ strongly recommended)
- **20GB+ free disk space**
- Virtualization enabled in BIOS (**Intel VT-x** / **AMD-V**)
- Admin/root rights on your own laptop
- [VirtualBox](https://www.virtualbox.org/) or [VMware Workstation Player](https://www.vmware.com/products/workstation-player.html) installed

### Step-by-Step: Installing Kali Linux (VM method)

1. **Download Kali Linux VM image**
   Go to [kali.org/get-kali](https://www.kali.org/get-kali/) → select **Virtual Machines** → download the VirtualBox or VMware image (pre-built, easier than installing from ISO).

2. **Install VirtualBox/VMware** if you haven't already.

3. **Import the VM**
   - VirtualBox: `File > Import Appliance` → select the downloaded `.ova` file
   - VMware: `File > Open` → select the `.vmx` file

4. **Allocate resources**
   Recommended: 4GB+ RAM, 2 CPU cores, adjust in VM settings before first boot.

5. **Boot the VM**
   Default credentials for the pre-built image: `kali / kali`
   *(Change this password immediately: `passwd`)*

6. **Update the system**
   ```bash
   sudo apt update && sudo apt full-upgrade -y
   ```

7. **Verify the 4 core tools are installed** (they come pre-installed on Kali, but confirm):
   ```bash
   nmap --version
   wireshark --version
   burpsuite --help
   msfconsole --version
   ```

> 💡 **Stuck?** Post in the workshop group chat / Discord *before* the day so we can troubleshoot ahead of time — install issues eat the most time on-site.

---

## 🛠️ Tool Cheat Sheet

### Nmap — Network Scanning
```bash
nmap -sV <target-ip>          # Scan for open ports & service versions
nmap -A <target-ip>           # Aggressive scan (OS detection, scripts)
nmap -p- <target-ip>          # Scan all 65535 ports
```

### Wireshark — Packet Analysis
- Capture live traffic on an interface, or open a provided `.pcap` file
- Use the filter bar: `http`, `tcp.port == 80`, `ftp`
- Right-click a packet → **Follow → TCP Stream** to reconstruct a conversation (great for finding flags in cleartext traffic)

### Burp Suite — Web App Testing
- Configure your browser to proxy through `127.0.0.1:8080`
- Use **Proxy → Intercept** to view/modify requests in-flight
- Use **Repeater** to resend and tweak individual requests

### Metasploit — Exploitation Framework
```bash
msfconsole
search <vulnerability-name>
use <module-path>
set RHOSTS <target-ip>
run
```
*(Today's session uses Metasploit primarily as a guided demo — try it hands-on afterward against intentionally vulnerable VMs like Metasploitable2.)*

---

## 📚 Resources to Keep Learning

- [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) — command-line fundamentals
- [picoCTF](https://picoctf.org/) — beginner CTF practice
- [TryHackMe: Pre Security Path](https://tryhackme.com/path/outline/presecurity)
- [Metasploitable2](https://sourceforge.net/projects/metasploitable/) — safe target VM to practice on
- [CTFtime.org](https://ctftime.org/) — find live CTFs to join with your new team

---

## 🙋 Questions?

Reach out to the organizing team before or during the workshop or contact +60 16-438 5690.
