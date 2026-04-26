## CA Certificate

Generate the CA private key

```bash
$ openssl genpkey -algorithm RSA -out ca.key -aes256
..+.........+.+............+..+...+.........+.+..............+++++++++++++++++++++++++++++++++++++++*.........+......+.+...+..+....+........+...+...+.......+..+......+.......+..+++++++++++++++++++++++++++++++++++++++*.....+................+.....+......+....+.................+...+.+...+..+.........+.+.........+..+.......+..+.+............+.....+.+.........+...+..+.............+........+.+..............+...............+....+..+................+.....+....+.....+......+..................+.........+.+...........+.+..+......+............+.........+.+.....+.......++++++
.+......+.............+..+....+..+....+........+...+...+.+......+..+...+.......+............+........+......+......+.+..+...+....+.....+......+...+.......+..+...+.......+++++++++++++++++++++++++++++++++++++++*...+....+.....+.+............+.....+...+++++++++++++++++++++++++++++++++++++++*...+...............+....+...+..+.......+.........+..+....+........+...+.......+......+.....+.+........+..................+....+...+........+...+......+...............+.........+.+......+........+....+..................+.........+.....+.+..+...+...............+............+.+..+.......+..+......+...+.+...+...+........+.....................+.+.........+...+...+........+......+.+...+.....+....+..+.+..++++++
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
```

Generate the CA certificate
```bash
$ openssl req -new -x509 -key ca.key -sha256 -days 3650 -out ca.crt
Enter pass phrase for ca.key:
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:MA
Locality Name (eg, city) []:Lowell
Organization Name (eg, company) [Internet Widgits Pty Ltd]:UMass Lowell
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:ca
Email Address []:
```

## Server Certificate

Generate the server private key

```bash
$ openssl genpkey -algorithm RSA -out server.key
.........+.+.........+...+........+++++++++++++++++++++++++++++++++++++++*....+......+...+.......+..............+....+..+...+..........+.....+.+..+..........+..+......+.+......+..+.+............+..+++++++++++++++++++++++++++++++++++++++*....+.....+...............+.+..+............+.+..+...+.......+.........++++++
...+............+...+...............+.........+.................+...+++++++++++++++++++++++++++++++++++++++*.+.......+...+++++++++++++++++++++++++++++++++++++++*...+....+......+.........+..+.......+.....+......+......+.............+.....+..................+...+...................+..+....+......+.....+.+..............+.+...............+...+..+..........+..+.+..+....+.....+...+...............+.+..............+.+............+.....+....+...+...........+....+..+....+...............+......+...+.....+...+...+...............+.+.....+.+..+.......+...............+...+.....+...+.............+.................+.........+......+.......+...+...+......+...+...+........+......+......+...+.+........+...+...+....+...........++++++
```

Generate the server csr file

```bash
$ openssl req -new -key server.key -out server.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:MA
Locality Name (eg, city) []:Lowell
Organization Name (eg, company) [Internet Widgits Pty Ltd]:UMass Lowell
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:server
Email Address []:

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```

Generate the server certificate

```bash
$ openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.pem -days 3650 -sha256
Certificate request self-signature ok
subject=C = US, ST = MA, L = Lowell, O = UMass Lowell, CN = server
Enter pass phrase for ca.key:
```