
#!/usr/bin/env bash
set -euo pipefail

# delete existing
rm -rf ca* server* 

# (1) generate CA key (will prompt for passphrase if -esa256 used)
openssl genpkey -algorithm RSA -out ca.key -aes256

# (2)create CA cert with CA extensions using openssl.cnf
openssl req -x509 -new -key ca.key -sha256 -days 3650 -out ca.crt \
  -subj "/CN=My Test CA" \
  -config openssl.cnf -extensions v3_ca

# (3) generate server key and CSR
openssl genpkey -algorithm RSA -out server.key
openssl req -new -key server.key -out server.csr -subj "/CN=server"

# sign server CSR with CA and include server_cert extensions from openssl.cnf
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
  -out server.pem -days 825 -sha256 -extfile openssl.cnf -extensions server_cert