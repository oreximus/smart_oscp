# Introduction to Web Applications (Notes From: HTB Academy)

## Introduction

- **Web Applications** are interactive applications that run on web browsers. Web applications usually adopt a **client-server architecture** to run and handle interactions.

- They typically have front end components (i.e., the website interface, or "what the user sees") that run on the client (browser) and other back end components (web application source code) that run on the the server-side (back end server/databases).

- This allows organizations to host powerful applications with near-complete real-time control over their design and functionality while being accessible worldwide. Some examples of typical web applications include online email services like **Gmail**, online retailers like **Amazon**, online word processors like **Google Docs**.

- Web applications are not exclusive to giant providers like Google or Microsoft but can be developed by any web developer and hosted online in any of the common hosting services, to be used by anyone on the internet.

- This is why today we have millions of web applications all over the internet, with billions of users interacting with them every day.

## Web Applications vs. Websites

- In the past, we interacted with websites that are static and cannot be changed in real-time. This means that traditional websites were statically created to represent specific information, and this information would not change with our interaction.

- To change website's content, the corresponding page has to be edited by the developers manually. These type of static pages do not contain functions and, therefore, do not produce real-time changes. That type of website is also known as **Web 1.0**.

![img01](imgs/img01.png)

- On the other hand, most website run web applications, or **Web 2.0** presenting dynamic content based on user interaction.

- Another significant difference is that web applications are fully functional and can perform various functionalities for the end-user, while sites lack this type of functionality.

- Other key differences between traditional websites and web applications include:
  - Being modular
  - Running on any display size
  - Running on any platform without being opimized

## Web Applications vs. Native Operating System Applications
  
- Unlike native operating system (native OS) applications, web-applications are platform-independent and can run in a browser on any operating system.

- These web applications do not have to be installed on a user's system because these web applications and their functionality are executed remotely on the remote server and hence do not consume any space on the end user's hard drive.

- Another advantage of web applications over native OS applications is version unity. All users accessing a web application use the same version and the same web application, which can be continuously updated and modified without pushing updates to each user.

- Web applications can be updated in a single location (webserver) without developing different builds for each platform, which dramatically reduces maintenance and support costs removing the need to communicate changes to all users individually.

- On the other hand, native OS applications have certain advantages over web applications, mainly their operation speed and the ability to utilize native operating system libraries and local hardware.

- As native applications are built to utilize native OS libraries, they are much faster to load and interact with.

- Furthermore, native applications are usually more capable than web applications, as they have a deeper integration to the operating system and are not limited to the browser's capabilities only.

- More recently, however, hybrid and progressive web applications are becoming more common. They utilize modern frameworks to run web applications using native OS capabilities and resources, making them faster than regular web applications and more capable.

## Web Application Distribution

- There are many open-soure web applications used by organizations worlwide that can be customized to meet each organization's needs. Some common open source web applications include:
  - Wordpress
  - OpenCart
  - Joomla

- There are also proprietary 'closed source' web applications, which are usually developed by a certain organization and then sold to another organization or used by organizations through a subscription plan model.
  - Wix
  - Shopify
  - DotNetNuke

## Security Risks of Web Applications

- Web application attacks are prevalent and present a challenge for most organizations with a web presence, regardless of their size.

- After all, they are usually accessible fron any country by everyone with an internet connection and a web browser and usually offer a vast attack surface.

- There are many automated tools for scanning and attacking web applications that, in the wrong hands, can cause significant damage.

- As web applications become more complicated and advanced, so does the possiblity of critical vulnerabilities being incorporated into thier design.

- A successful web application attack can lead to significant losses and massive business interruptions. Since web applications are run on servers that may host other sensitive information and are often also linked to databases containing sensitive user or corpotate data, all of this data could be compromized if a web site is successfully attacked.

- This is why it is critical for any business that utilizes web applications to properly test these applications for vulnerabilities and patch them promptly while testing that the patch fixes the flaw and does not inadvertently introduce any new flaws.

- Web application penetration testing is an increasingly critical skill to learn. Any organization looking to secure their internet-facing (and internal) web applications should undergo frequent web application tests and implement secure coding practices at every development life cycle stage.

- To properly pentest web applications, we need to understand how they work, how they are developed, and what kind of risk lies at each layer and component of the application depending on the technologies in use.

- We will always come across various web applications that are designed and configured differently. One of the most current and widely used methods for testing web applications is the **OWASP Web Security Testing Guide**.

- One of the most common procedures is to start by reviewing a web application's front end components, such as **HTML**, **CSS** and **Javascript** (also known as the front end trinity), and attempt to find vulnerabilities such as **Sensitive Data Exposure** and **Cross Site Scripting (XSS)**.

- Once all front end components are thoroughly tested, we would typically review the web application's core functionality and the interaction between the browser and the webserver to enumerate the technologies the webserver uses and look for exploitable flaws.

- We typically assess web applications from both an unauthenticated and authenticated perspective (if the application has login functionality) to maximize coverage and review every possible attack scenario.

## Attacking Web Applications

- Nowadays every corporation no matter how big it is, they will definitely have one or more web applications within their external perimeter.

- These applications can be everything from simple static websites to blogs powered by Content Management Systems (CMS) such **WordPress** to complicated applications with sign-up/login functionality supporting various user roles from basic users to super admins. Nowadays, it is not very common to find an externally facing host directly exploitable via a know public exploit (such as a vulnerable service or Windows remote code execution (RCE) vulnerability), though it does happen.

- Web applications provide a vast attack surface, and their dynamic nature means that they are constantly changing (and overlooked!).

- A relatively simple code change may introduce a catastrophic vulnerability or a series of vulnerabilities that can be chained together to gain access to sensitive data or remote code execution on the webserver or other hosts in the environment, such as database servers.

- It is not uncommon to find flaws that can lead directly to code execution, such as a file upload form that allows for the upload of malicious code or a file inclusion vulnerability that can be leveraged to obtain remote code execution.

- A well-known vulnerability that is still quite prevalent in various type of web applications is SQL injection. This type of vulnerability arises from the unsafe handling of user-supplied input. It can result in access to sensitive data, reading/writing files on the database server, and even remote code execution.

- We often find SQL injection vulnerabilities on web applications that use Active Directory for authentication. While we can usually not leverage this to extract password (since Active Directory administraters them), we can often pull most or all Active Directory user email addresses, which are ofen the same as their usernames.

- This data can then be used to perform a **password spraying** attack against web portals that use Active Directory for authentication such as VPN or Microsoft Outlook Web Access/Microsoft O365.

- A successful password spray can often result in access to sensitive data such as email or even a foothold directly into the corpotate network environment.

- This example shows the damage that can arise from a single web application vulnerability, especially when "chained" to extract data from one application that can be used to attack other portions of a company's external infrastruction.

- **A well-rounded infosec professional should have a deep understanding of web applications and be as comfortable attacking web applications as performing network penetration and Active Directory attacks.**

- A penetration tester with a strong a foundation in web applications can often set themselves apart from their peers and find flaws that orders may overlook.

- A few more real-world example of web-application attacks and the impact are as follows:

| **Flaw** | **Real-world Scenario** |
|----------|-------------------------|
| SQL injection | Obtaining Active Directory usernames and performing a password spraying attack against a VPN or email portal. |
| File Inclusion | Reading source code to find a hidden page or directory which exposes additional functionality that can be used to gain remote code execution. |
| Unresticted File Upload | A web application that allows a user to upload a profile picture that allows any file type to be uploaded (not just images). This can be leveraged to gain full control of the web application server by uploading malicious code. |
| Insecure Direct Object Referencing (IDOR) | When combined with a flaw such as broken access control, this can often be used to access another user's files or functionality. An example would be editing your user profile browsing to a page such as /user/701/edit-profile. If we can change the **701** to **702**, we may edit another user's profile!. |
| Broken Access Control | Another example is an application that allows a user to register a new account. If the account registration functionality is designed poorly, a user may perform privilege escalation when registering. Consider the **POST** request when registering a new user, which submits the data **username=bjones&password=Welcome1&email=bjones@inlanefreight.local&roleid=3**. What if we can manipulate the **roleid** parameter and change it to **0** or **1**. We have seen real-world applications where this was the case, and it was possible to quickly register an admin user and access many unitended features of the web application. |

## Web Application Layout

- Web Application layouts consists of many different layers that can be summarized with the following three main categories:

|**Category** | **Description**|
|-------------|----------------|
| Web Application Infrastructure | Describes the structure of required componenets, such as the database, needed for the web application to function as intended. Since the web application can be set up to run on a separate server, it is essential to know which database server it needs to access. |
| Web Application Components | The components that make up a web application represent all the components that the web application interacts with. These are divided into the following three areas: **UI/UX**,**Clients**, and **Server** components. |
| Web Application Architecture | Architecture comprises all the relationships between the various web application components. |

## Web Application Infrastructure

- Web applications can use many different infrastructure setups. These are also called **models**. The most common ones can be grouped into the following four types:
  - Client-Server
  - One Server
  - Many Server - One Database
  - Many Server - Many Database

## Client-Server

- Web applications often adopt the **client-server** model. A server hosts the web applications in a client server model and distributes it to any clients trying to access it.

![img05](imgs/img05.png)

- In this model, web applications have two types of components, those in the front end, which are usually interpreted and executed on the client-side (browser), and components in the back end, usually compiled, interpreted, and executed by the hosting server.

- When a client visits the web applications's URL (web address, i.e. https://www.acme.local), the server uses the main 


