## Paper

### Foothold
This box took a while to complete because I misread the /etc/hosts file. After running nikto on the host you realize that you need to add the right domain<br>
To get a wordpress site. Once you access the wordpress site you have to tamper with the url to view hidden comments.

## Exploitation 
http://office.paper?/static=1&order=date will reveal a chat site. After using the chat site and enumerating the bot you can type "file ../hubot/.env"<br>
After you exploit the bots lfi you can use the password and the bot creators first name to login via ssh and grab the user flag. 
<br>From there the author created a polkit
exploit. This can be found by using linpeas<br> Run the exploit and login/switch to the new user.
