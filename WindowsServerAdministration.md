## Windows Server Administration
## On OS: Windows Server 2012 R2

**Contents**

- DHCP
- DNS
- ADDS
- IIS

### Dynamic Host Configration Protocol (DHCP)

- Dynamic Host Configuration Protocol (DHCP) is a client/server protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mak and default gateway. RFCs 2131 and 2132 define DHCP as an Internet Engineering Task Force (IETF) standard based on Bootstrap Protocol (BOOTP), is a protocol with which DHCP shares many implementation details. DHCP allows host to obtain required TCP/IP configuration from a DHCP server.

- The DHCP server maintains a pool of IP addresses and leases an address to any DHCP-enables client when it starts up on the network. Becuase the IP addresses are dynamic (leased) rather than static (permanently assigned), addresses no longer in use are automatically returned to the pool for reallocation.

- The network administrator establishes DHCP servers that maintain TCP/IP configuration information and provide address configuration to DHCP-enables clients in the form of a lease offer. The DHCP server stores the configuration information in a database that includes:
	- Valid TCP/IP configration parameters for all clients on the network.
	- Valid IP addresses, maintained in a pool for assignment to clients, as well as excluded addresses.
	- Reserved IP addresses associated with particular DHCP clients. This allows consistent assignment of a single IP address to a single DHCP client.
	- The lease duration, ot the length of time for which the IP address can be used before a lease renewal is required.

- A DHCP-enabled client, upon accepting a lease offer, recieves:
	- A valid IP address for the subnet to which it is connecting.
	- Requested DHCP options, which are additional parameters that a DHCP server is configured to assign to clients. Some example of DHCP options are Router (default gateway), DNS Servers, and DNS Domain Name.

### Benefits of DHCP

DHCP provides the following benefits.

- **Reliable IP address configuration**. DHCP minimizes configuration error caused by manual IP address configuration, such as typographical error, or address conflicts caused by the assignment of an IP address to more than one computer at the same time.

- **Reduced network administration**. DHCP includes the following features to reduce network administration:
	- Centralized and automated TCP/IP configuration.
	- The ability to define TCP/IP configuration from a central location.
	- The ability to assign a fill range of additional TCP/IP configuration values by means of DHCP options.
	- The efficient handling of IP address change for clients that must be updated frequently, such as those for portable devices that move to different location on a wireless network.
	- The forwarding of initial DHCP messages by using a DHCP relay agent, which eliminated the need for a DHCP server on every subnet.


