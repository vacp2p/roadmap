# TODO

### . KademliaDHT `vac:p2p:ift:2025q2-kademlia-dht`
Implement Kademlia Distributed Hash Table in nim-libp2p, based on the [libp2p specification](https://github.com/libp2p/specs/blob/master/kad-dht/) as an additional discovery mechanism.
This commitment involves two main objectives: implementing nim-kademlia-dht, and integrating this in nim-libp2p
- Routing table and RPC Protocol
`vac:p2p:ift:2025q2-nimlibp2p-kad-dht:routing-and-rpc`
- Bootstrapping & Lookup: join, lookup, key-value storage
 `vac:p2p:ift:2025q2-kad-dht:bootstraping-and-lookup`
- Network maintenance: ping, node eviction, bucket refresh
 `vac:p2p:ift:2025q2-kad-dht:network-maintenance`
- Bootstrap process to keep routing tables filled
 `vac:p2p:ift:2025q2-kad-dht:bootstrap`
- nim-libp2p integration
 `vac:p2p:ift:2025q2-kad-dht:nim-libp2p`