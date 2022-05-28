# Relevant - WIP

## Recon

This box may be vulnerable to blue testing that is no fun.


```
nmap -sV IP
80/tcp   open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
3389/tcp open  ms-wbt-server Microsoft Terminal Services
```

nmap -sV -p 0-65353 10.10.82.109


gobuster dir -u http://10.10.82.109/ -w common.txt = No results


enum4linux 10.10.82.109

```
nmap --script smb-os-discovery.nse -p445 10.10.82.109:
Host script results:
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)
|   Computer name: Relevant
|   NetBIOS computer name: RELEVANT\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-05-27T22:06:35-07:00
```
```
nmap --script smb-enum-domains.nse,smb-enum-groups.nse,smb-enum-processes.nse,smb-enum-services.nse,smb-enum-sessions.nse,smb-enum-shares.nse,smb-enum-users.nse -p445 10.10.82.109
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
```

smbmap -u nt4wrksv -H 10.10.82.109


smbmap -u nt4wrksv -H 10.10.82.109 -r nt4wrksv


https://www.nopsec.com/blog/smbmap-wield-it-like-the-creator/


smbmap -u nt4wrksv -H 10.10.82.109 -r nt4wrksv -A 'pass'
	
Credentials: 

Bob - REDACTED
	

After trying the passwords with RDP the connection did not work. Now we are going to go focus on SMB and see if that yields any results.
