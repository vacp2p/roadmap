# TODO

4. AutoTLS

Implement a process that automates the issuance of Let’s Encrypt wilcard TLS certificates for nim-libp2p nodes. This would enable reliable browser-based clients to connect to libp2p nodes, regardless of the network topology which improves resilience and opens up a window to more capable browser clients. This task is limited to the client functionality; Server functionality could be implemented on a separate task
5.1. Request certificate and authenticate against registration.libp2p.direct
5.2. Notify DNS-01 challenge completion
5.3. Install generated certificate and use it in TCP/WS/WSSS/Quic/Webtransport


2. TLS secure transport vac:p2p:ift:2025q2-tls-transport

Implement TLS secure protocol /tls/1.0.0 to provide encryption and authentication for transports that lack built-in security mechanisms.

    2.1 Implement TLS secure transport
    vac:p2p:ift:2025q2-tls-transport:tls
    Implement the logic for TLS secure transport according to libp2p specification
