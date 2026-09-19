# 🚩 Hands-On CTF Lab: Where's The Flag?

Welcome to the hands-on lab. In Capture The Flag (CTF) competitions, your objective is to uncover hidden tokens known as **Flags**, formatted as `FLAG{...}`.

---

## ⚡ Quick Start

Clone this repository to your Kali VM or local machine:

```bash
git clone [https://github.com/LOWGUANHOONG/PEKOM-Linux-Workshop.git](https://github.com/LOWGUANHOONG/PEKOM-Linux-Workshop.git)
cd PEKOM-Linux-Workshop
```

---

## 🗺️ Challenge Map

| # | Category | Challenge Name | Target File / Location | Core Skills & Tools |
|---|---|---|---|---|
| **01** | **Web Exploitation** | *Secret Agent Only* | `challenges/01-web/` | HTTP request headers, `curl` / Burp Suite |
| **02** | **Cryptography** | *Caesar's Ciphertext* | `challenges/02-crypto/secret.txt` | Base64 decoding, ROT13, [CyberChef](https://gchq.github.io/CyberChef/) |
| **03** | **Forensics** | *The Ghost in the Pixels* | `challenges/03-forensics/evidence.png` | File signatures, artifact extraction, `strings` |
| **04** | **Reverse Engineering** | *Vault Password Checker* | `challenges/04-rev/vault` | Static binary analysis, `strings`, `ltrace` |
| **05** | **Pwn (Binary Exploitation)** | *Buffer Overwrite 101* | `challenges/05-pwn/bof` | Stack layout, buffer overflows, Python CLI piping |
| **06** | **OSINT** | *The Leaked Commit* | This GitHub Repository | Public commit diffs, `git log -p` |
| **07** | **Misc** | *Lost in Transmission* | `challenges/07-misc/traffic.pcap` | Network capture inspection, Wireshark filters |

---

### 1. Web Exploitation: *Secret Agent Only*

* **Scenario:** An internal verification endpoint has been deployed, but access is restricted to a proprietary internal client.
* **Objective:** Send a request with the expected user identity to reveal the flag.

#### Instructions:
1. Move to `challenges/01-web/` and launch the local test server:
   ```bash
   cd challenges/01-web
   python3 app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:8080`. You will receive an **Access Denied** notice.
3. Modify your HTTP request header so that your `User-Agent` identifies as `FlagBrowser`.

<details>
<summary>💡 Need a Hint?</summary>

Servers use the `User-Agent` header to identify incoming clients. You can forge this header instantly in your terminal without setting up a browser proxy:
```bash
curl -H "User-Agent: FlagBrowser" [http://127.0.0.1:8080](http://127.0.0.1:8080)
```
</details>

<details>
<summary>🔓 Solution</summary>

Running the following command retrieves the flag directly from the response body:
```bash
curl -H "User-Agent: FlagBrowser" [http://127.0.0.1:8080](http://127.0.0.1:8080)
```
**Flag:** `FLAG{http_h3ad3rs_t3ll_all}`
</details>

---

### 2. Cryptography: *Caesar's Ciphertext*

* **Scenario:** A scrambled transmission was intercepted over an unsecured channel.
* **Target File:** `challenges/02-crypto/secret.txt`
* **Ciphertext:**
  ```text
  U1laR3twNDNzNHJfdzB1bGRfYjNfcHIwdWR9
  ```

#### Instructions:
1. Identify the encoding format (look at character set and length).
2. Load [CyberChef](https://gchq.github.io/CyberChef/) in your browser.
3. Decode the representation, then apply the correct classical shift cipher.

<details>
<summary>💡 Need a Hint?</summary>

The string contains standard alphanumeric characters and is Base64-encoded. After decoding Base64, the output starts with `SYZG`, which corresponds to `FLAG` shifted by 13 alphabet positions.
</details>

<details>
<summary>🔓 Solution</summary>

1. CyberChef Recipe: **From Base64** $\rightarrow$ produces `SYZG{p43s4r_w0uld_b3_pr0ud}`.
2. CyberChef Recipe: Add **ROT13** (Amount = 13) $\rightarrow$ decodes to plain text.

**Flag:** `FLAG{c43s4r_w0uld_b3_pr0ud}`
</details>

---

### 3. Forensics: *The Ghost in the Pixels*

* **Scenario:** A PNG image was recovered from an abandoned USB drive. The visual data appears normal, but investigators believe additional data was appended outside the pixel raster.
* **Target File:** `challenges/03-forensics/evidence.png`

#### Instructions:
1. Verify the file integrity using terminal utilities:
   ```bash
   file evidence.png
   ```
2. Scan the file for embedded human-readable ASCII strings.

<details>
<summary>💡 Need a Hint?</summary>

Binary files often contain raw ASCII text embedded by tools or attackers. Use `strings` piped into `grep`:
```bash
strings evidence.png | grep -i "FLAG"
```
</details>

<details>
<summary>🔓 Solution</summary>

Running:
```bash
strings evidence.png | grep "FLAG"
```
Extracts the trailing appended string:
**Flag:** `FLAG{str1ngs_n3v3r_l13}`
</details>

---

### 4. Reverse Engineering: *Vault Password Checker*

* **Scenario:** You have recovered a compiled authentication binary (`vault`). Source code is unavailable, but validation is handled locally.
* **Target File:** `challenges/04-rev/vault`

#### Instructions:
1. Grant execution rights and run the executable:
   ```bash
   chmod +x vault
   ./vault
   ```
2. Intercept or view the string comparison routine to find the expected input.

<details>
<summary>💡 Need a Hint?</summary>

You can trace dynamic library calls to see what string `strcmp` checks against:
```bash
ltrace ./vault
```
Enter any text when prompted to observe the comparison argument.
</details>

<details>
<summary>🔓 Solution</summary>

Running `ltrace ./vault` and typing `test` prints:
```text
strcmp("test", "open_sesame_2026")
```
Re-running `./vault` and supplying `open_sesame_2026` prints:
**Flag:** `FLAG{r3v3rs3_th3_v4ult}`
</details>

---

### 5. Pwn (Binary Exploitation): *Buffer Overwrite 101*

* **Scenario:** A compiled C binary allocates 16 bytes for user input. A target integer variable sits directly adjacent on the stack.
* **Target File:** `challenges/05-pwn/bof` (Source code is available in `bof.c` for inspection)

#### Instructions:
1. Mark the binary as executable and test normal execution:
   ```bash
   chmod +x bof
   ./bof
   ```
2. Supply an input longer than 16 bytes to overwrite the adjacent stack memory and trigger the success branch.

<details>
<summary>💡 Need a Hint?</summary>

Because memory allocations align contiguously, feeding 24 characters (e.g., 24 `A`s) forces the excess bytes past the end of `buffer` into `modified`:
```bash
python3 -c 'print("A" * 24)' | ./bof
```
</details>

<details>
<summary>🔓 Solution</summary>

Piping an overflowing string into standard input:
```bash
python3 -c 'print("A" * 24)' | ./bof
```
Overwrites `modified != 0` and unlocks:
**Flag:** `FLAG{st4ck_0v3rfl0w_b4s1cs}`
</details>

---

### 6. OSINT: *The Leaked Commit*

* **Scenario:** An engineer accidentally pushed hardcoded API keys to this repository, then submitted a commit stating *"Cleaned up sensitive config"*.
* **Target Location:** This Git repository's commit history.

#### Instructions:
1. View historical commit metadata on your local clone:
   ```bash
   git log --oneline
   ```
2. Review the diff of previous commits to find the deleted secret.

<details>
<summary>💡 Need a Hint?</summary>

Use `git log -p` to inspect the full textual diff of past revisions, or browse the commit history directly on the GitHub web interface.
</details>

<details>
<summary>🔓 Solution</summary>

Running:
```bash
git log -p
```
Reveals the deleted credentials line:
```diff
- API_KEY=FLAG{g1t_h1st0ry_n3v3r_f0rg3ts}
```
**Flag:** `FLAG{g1t_h1st0ry_n3v3r_f0rg3ts}`
</details>

---

### 7. Misc: *Lost in Transmission*

* **Scenario:** Network traffic was captured on a local subnet while a user submitted authentication parameters over plain HTTP.
* **Target File:** `challenges/07-misc/traffic.pcap`

#### Instructions:
1. Open the packet capture file in Wireshark:
   ```bash
   wireshark traffic.pcap &
   ```
2. Apply a display filter for HTTP traffic.
3. Locate the `POST` request and follow its TCP stream to reconstruct the conversation.

<details>
<summary>💡 Need a Hint?</summary>

Type `http.request.method == "POST"` in the display filter bar at the top, right-click the packet, and select **Follow > TCP Stream**.
</details>

<details>
<summary>🔓 Solution</summary>

Inspecting the TCP stream of the HTTP POST packet reveals the submitted payload in clear text:
```text
POST /login HTTP/1.1
...
user=admin&flag=FLAG{p4ck3t_sn1ff1ng_succ3ss}
```
**Flag:** `FLAG{p4ck3t_sn1ff1ng_succ3ss}`
</details>