Title: Self Hosting Guide - Part 1
Date: 2017-02-11
Category: Network
Tags: networks, Internet, data
Slug: self-hosting-guide
Author: Prasanna Venkadesh

Quoting my own words from my [very first post](hello-world.html).

> I can always move the site to other providers / host my own, if I at some point needed to abandon github (it's already a proprietary platform).

Here I am, self-hosting my blog and [code](https://code.purambokku.me) as well. When I use the word **self-hosting**, I mean it. The server is sitting in a room at the place where I live currently connected to an ADSL Modem + Router which is in turn connected to Internet via my Internet Service Provider (**ISP**).

![image of orangepi pc](http://files.linuxgizmos.com/orangepipc_angle.jpg)

----

#### Requirements

1. A **computer with GNU/Linux operating system** that has to run 24x7. When it has to run 24x7 think about power consumption. You don't need a GUI component to run a server, therefore get rid of Monitors or external displays. You can use it to setup, but beyond that avoind using a display. A SoC (System on Chip) like **Raspberry Pi** (or) **Beaglebone Black** (or) **Orange Pi PC**, etc., can do well. I have mine setup using Orange Pi PC.
2. A **Web Server** (or) a reverse proxy like **Nginx** or **Apache** or **httpd** to serve the applications on the Web through Internet.
3. A **DSL/ADSL modem** with support for **port forwarding**, **DHCP IP Reservation for LAN**.
4. **Dynanic DNS client** like **ddclient** to install in the server so as to update the **DNS** records everytime your public IP address changes. Our home connections often do not get static IP address instead our IP addresses are dynamic, which means there is no guarentee that I will get the same IP address tomorrow. IP address are required to reach any computer on Interent, if my IP address keeps on changing everyday or after every few hours, how would my friends or others on the Internet knows that it has changed to new address? This is where DDNS comes in.
5. An **account on DDNS service** like [nsupdate](https://nsupdate.info) (or) [freeDNS](https://freedns.afraid.org). nsupdate is completely free to use, while freeDNS has a free plan as well.
6. **Domain Name** (optional). A name for your site can be purchased from domain registrars like bigrock or godaddy or namecheap etc., This is completely optional. If you can't afford to buy a domain name (or) if you decide you don't need a domain name, both nsupdate and freeDNS provides subdomains. It is like some people would have purchased a domain name and then added it to freeDNS or nsupdate like how I have added **purambokku.me** to freeDNS and also allow others to create a subdomain using this domain for them. Like for example, you can create yourname.purambokku.me or using any public domain name. This is more or less a gift economy.

----

#### Cost of Self-Hosting (approx.)

Am not including the cost of modem + Internet connection here.

1. [Orange Pi PC](https://www.crazypi.com/single-board-computers-india/orange-pi-india/orange-pi-pc-india) - Rs. 2000/-
2. RJ45 Ehternet Cable 1 - usually around Rs.70-100/-
3. Class 10 32Gb MicroSD card 1 - Rs. 600-800/-
4. Domain Name (optional) - starting from Rs. 70/-

Apart from optional domain name, the above are one time cost, not something like paying monthly rent to someone. In the next part, I will be writing about preparing your computer for self-hosting.
