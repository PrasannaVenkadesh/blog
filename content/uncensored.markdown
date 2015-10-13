Title: Uncensored - Circumventing Censorship
Date: 2015-10-12
Category: Network
Tags: tor, tech, free software, proxy, internet, web, politics
Slug: uncensored
Author: Prasanna Venkadesh

It's been 2 months since I have enrolled myself for the post graduate course in Networks & Internet Engineering (NIE) at Pondicherry University. The campus is a beautiful place to be and has rich bio-diversity preserved inside. It is also a Wi-Fi enabled campus scaling to various schools from engineering to management, Life Sciences to Performing Arts, Social Sciences to Medical Sciences, etc.,

I belong to Department of Computer Science which comes under School of Engineering & Technology and the funny part is our department receives very poor Wi-Fi signal at class rooms, sometimes not even that. As a student of NIE, I feel the classroom is powerless without even access to wireless networks (at times, we do form ad-hoc networks).

### The Problem (Status Quo)

Ok, let's focus on the censorship part from here on. Even if one can get a strong wi-fi signal or access to the wired network, not all the websites over the internet are accessible through the network. Social networks like Facebook, Video streaming platforms like Youtube, etc., are blocked in a temporal manner (i.e these sites cannot be accessed during class hours). The problem here is, not everyone have uniform class hours. So if one set of people are inside classrooms, some other set of people at some other department will be idle and they won't be able to access websites that are blocked. These rules are applicable even on weekends when the university is not functioning.

There are also other issues like,

 - torrent downloads are blocked.
 - downloading files more than a specific size are blocked (for eg, when the free software users group were preparing to organize a GNU/Linux installation fest inside the campus and we wanted to download the latest / stable iso images of distributions like Ubuntu, Fedora, Trisquel, Mint, etc., we were not allowed to download since the file size were large).
 - a GNU/Linux user could not use the package management tools like **apt-get** (or) **dnf** to update or download tools from the distributions repository which is really irritating, since this is the most preferred way of installing a package (or) software in gnu/linux distributions.

### The Solution (Moving Forward)

With technology, there are always ways to circumvent blockades. I would like to remind you incidents like [this](http://mashable.com/2011/01/27/bypass-twitter-facebook-block-egypt/) and [this](http://www.wired.com/2014/10/firechat-hong-kong-usage/). Using web proxy seems to be a easy option for most of them to access sites that are blocked. But proxy sites will soon hit it's limitations, in our scenario described above, using web proxy one cannot download large files, web proxy sites has no connection with respect to torrent downloads & solving apt-get or package download problem. Also if certain sites are blocked in the country that the web proxy site is located, then that would be the dead end.

Our university uses a proxy server that sits in between the local networks (i.e the campus network) and the rest of the Internet and this proxy server is powered by a software named **[squid](http://www.squid-cache.org/)** which is a [free software](http://www.gnu.org/philosophy/free-sw.html). Every request made from a computer connected to a university network will have to pass or go through the proxy server. The proxy server would inspect the packets header and match it against with the rules written to allow / drop the packets by the network administrator. They could write complex rules combining multiple parameters like the url pattern, response size & type, etc.,

Like everyone else in the campus, I was also confronted with these problems, so I decided to share what works for me, so that you people could use it to circumvent it, especially gnu/linux users.

I have seen most of the people inside the campus are using an application in their android phones called **[Psiphon](https://psiphon.ca/)** which also is a free software. But Psiphon is limited to only Android and Windows currently and so other platforms are left out especially gnu/linux users. Since Psiphon is free software, we can attempt to build our own client for the platforms that are left out.

I use **[Tor](https://torproject.org)** network to bypass the censorship. Tor is a [free software](http://www.gnu.org/philosophy/free-sw.html) project aimed to provide anonymity for users, journalists, activists, etc., around the world and also used to bypass the censorship. This [video](https://www.youtube.com/watch?v=JWII85UlzKw) will better explain the idea behind tor.

Both Psiphon and Tor's objective are completely different. Psiphon's objective is to `bypass censorhip` while Tor's objective is to provide `anonymity` and the fact that tor can also bypass censorship is just a **side-effect of it's network architecture**. So with tor one can stay anonymous while circumventing censorship too. Moreover Tor is cross-platform. It has clients for GNU/Linux, Windows, Mac & Android. Tor also has got a `Tor browser` for desktops which is a fork of Firefox browser and tweaked to be compatible for Tor and released.

I am using Fedora 22 in my laptop and I have installed Tor daemon and have configured my existing firefox browers to use socks proxy. To install Tor in gnu/linux distributions we need access to uncensored internet at the first place, since apt-get (or) dnf yum won't be able to download through the censored network here. So if you visit your friends house with Internet access (or) if you have other means of connecting to internet like mobile data, you can use that to install tor.

Instructions to,

 - install Tor in [Fedora / CentOS](https://www.torproject.org/docs/rpms.html.en).
 - install Tor in [Debian / Ubuntu / LinuxMint](https://www.torproject.org/docs/debian.html.en)

Once you have installed tor successfully, also install another tool named `proxychains` (usage is explained below).

Instructions to install proxychains,

 - fedora:
  > sudo dnf -C install proxychains
 - debian / ubuntu / mint:
  > sudo apt-get install proxychains

Follow these instructions to set it up and start tor.

 - search for `terminal` in applications and open it.
 - if your network is behind a proxy server, we need to enter the proxy location in torrc file. In our university we are sitting behind a squid proxy server and the location is `http://10.10.80.11:3128` and `https://10.10.80.11:3128`
 - copy both (http and https) url and enter the following in terminal which will open the torrc file in nano text editor
 > sudo nano /etc/tor/torrc
 - scroll down to the end of the file and type the following

 > HTTPProxy 10.10.80.11:3128

 > HTTPSProxy 10.10.80.11:3128

 press `ctrl+x` then `Y` and press `Enter` to save and quit. The edited file should look like the image below
 
 <img src="https://ipfs.io/ipfs/QmYdULp2HnNir4d9EUnr2pcQYLAiinZEdRKN4VTDn3RLJe"/>

Now that we have successfully configured `tor` to use the network proxy, let's start using tor.

 1. `tor` will be started automatically in the background for ubuntu / debian / mint. Let's stop it first through terminal.
 > sudo service tor stop
 2. Now let's start the `tor` again. This is a common step for both fedora and debian based distributions.
 > tor
 3. You should be seeing some outputs in number of lines like Bootstrapped 0% (refer the image below). When tor reaches `Bootstrapped 100%: done` it means our computer can now participate in the tor network.
 4. `tor` is pre-configured to run on port 9050 in your computer.

 <img src="https://ipfs.io/ipfs/QmcJf5qhgDf9DMHU7N4qhJ5vYPyxum6AHKc5YWyiDrcqsD"/>

Note: The reason why stopped and started tor is that, by default tor will be running in the background if started automatically, when we invoke `tor` via command line manually, we will be able to see the logs and can check if tor is successfully establishing the connection or struck somewhere so that we can try to debug.

Just leave the terminal open with tor running and let's open `firefox` browser to use tor.

 - in firefox, go to `Edit` > `preferences` > `Advanced` > `Network` > `Settings` > `Manual Proxy configuration`
 - find `SOCKS Host` and enter `localhost` in the first field and `9050` in the port field.
 - click on `ok` and now you should be able to visit websites that are blocked previously.

Website censorship is solved, now let's focus on package manager. Remember we installed `proxychains`? This is where we will make use of it.

 - Open `/etc/proxychains.conf` file using `nano` editor like how we opened the `/etc/tor/torrc` file.
 - scroll down to the end of the file and you could find `#socks4 127.0.0.1 9050`.
 - if there is a `#` like above, just delete that character alone, save and quit the editor.

With `tor` running in the background, now if we invoke any program from the `terminal` using `proxychains` we can make that program to redirect the traffic through `tor`. For example,

> sudo proxychains apt-get install uget

will install uget download manager and install it in your debian based machines. I hope you got the key point here. If you want to redirect any application to use tor, you will have to set `SOCKS proxy` for the application. the proxy address would be `localhost:9050` or `127.0.0.1:3128` where `localhost` or `127.0.0.1` is the address and `3128` is the port number. For applications which doesn't support SOCKS proxy yet, you can use `proxychains`.

Also you can use **[uGet Download Manager](http://ugetdm.com/)** to download files (uget has support for SOCKS proxy, so remember to start tor and set socks 4 proxy in uget preferences before starting your download).

The above chain of solutions solves the following problems that I already mentoned above:

 - bypassing website censorship.
 - downloading and installing software (or) package management in gnu/linux distributions.
 - downloading large files.

The only problem that relies unanswered is `torrent downloads`. Using `torrent` downloads via `tor` traffic is a [bad idea](https://blog.torproject.org/blog/bittorrent-over-tor-isnt-good-idea).

### Endnote

> While the State exists there can be no freedom; when there is freedom there will be no State - V.I. Lenin

Right from the beginning we have been encountering names of software like `squid`, `psiphon`, `tor`, `proxychains`, `uget`, `fedora`, `debian`, `ubuntu`, etc., all of them are **Free Software**. Amidst the fact that `free software` stresses the freedom of user, it doesn't completely libreate or free the masses from oppression.

Here we are seeing two classes of people, one is the `oppressing` class and the other is the `oppressed` class both are using Free Software for their purposes. In our case `squid`, a free softwrae is used to enforce censorship and `psiphon`, `tor`, `proxychains`, etc., which are free softwrae too, are used to fight back. But not everyone are liberated. `You and I` can be exceptions, but exceptions cannot become mainstream.

**Science & Technology** can be used as tools and catalyst while fighting for freedom, but they alone cannot bring about freedom or revolution. We also need to be **politically aware**.
