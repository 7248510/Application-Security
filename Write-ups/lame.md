## Lame
1. Spawn the machine

2. Running an NMAP scan revealed that ftp,ssh,netbois and microsoft-ds were open[see output below](nmap IP -Pn)
21/tcp  open  ftp                                                                                                                                                                                                                          
22/tcp  open  ssh                                                                                                                                                                                                                          
139/tcp open  netbios-ssn                                                                                                                                                                                                                  
445/tcp open  microsoft-ds 

3. Running another more details nmap scan revealed that vsftpd is active on the box and anonymous ftp login is allowed.
From doing metasploitable2. A backdoor is in vsftpd.
The exploit did not work. But we have an anonymous ftp login that should work.
username: Anonymous Password: Anonymous
While vsftpd did not work(assumings its been patched we find another exploit that works(usermap_script))

4. After re-running an nmap scan to get more information(nmap -A -sV -Pn IP)

5. Lame has a Samba service running on port 139 with the version number 3.0.20

6. Searching "Samba 3" in searchsploit reveals that the service has an exploit written in metasploit.

7. Running the exploit gets us root! After that find the flag in the users' home directory and the root's home directory.
