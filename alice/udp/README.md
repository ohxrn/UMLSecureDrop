UDP examples — simple echo + broadcast demos

This folder contains three small Python examples that demonstrate basic UDP (Datagram) networking.

Files

- `udp_server.py` — a minimal UDP echo server. It binds to port 9999 (by default) on `0.0.0.0` and echoes back any datagrams it receives.

- `udp_client.py` — a minimal UDP client that sends a single message to the server (`server_ip` / `server_port`) and waits for the echoed reply. Update the `server_ip` variable in the file to point at the server (or set it to `127.0.0.1` to test locally).

- `udp_broadcast.py` — a small script that sends a UDP broadcast on the local network (and typically listens for responses). Use it to discover services or send a message to all hosts on the subnet. Make sure your network allows broadcasts.

Quick examples

Run the server (terminal A):

```bash
cd udp
python3 udp_server.py
```

Run the client (terminal B) — edit `server_ip` first if needed:

```bash
cd udp
python3 udp_client.py
# then type a message and press Enter
```

Run the broadcast script (terminal C):

```bash
cd udp
python3 udp_broadcast.py
```

Notes

- All scripts use UDP (socket.AF_INET + socket.SOCK_DGRAM). UDP is connectionless and messages may be lost or arrive out of order.
- If testing on a single machine, set `server_ip` to `127.0.0.1`. If testing across machines, ensure devices are on the same subnet and that firewalls permit UDP on port 9999.
- Broadcast behavior depends on your network: some routers block subnet or global broadcasts. If the broadcast script uses a specific broadcast address, adjust it to your subnet (for example `192.168.1.255`).

That's all — small, focused examples for learning UDP send/receive and simple broadcast patterns.
