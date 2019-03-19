Title: Whispering Pictures - Beware
Date: 2017-01-01
Category: Free Software
Tags: privacy, code, free software, tech, web
Slug: privacy-pictures
Author: Prasanna Venkadesh

*This is the english version of the [tamil post](https://fsftn.org/blog/pesum-pugaipadangal-gavanam/) that I wrote for [FSFTN's blog](https://fsftn.org/blog).*

We come across a lot of new people throughout our life. There is a reason we call them strangers. Not everyone wins our trust and vice-versa. We don't reveal much about ourselves to those strangers. We try to be more cautious about what information we reveal to them. This is what we call our **Privacy**.

> Privacy is the ability of an individual or group to seclude themselves, or information about themselves, and thereby express themselves selectively. - [Wikipedia](https://en.wikipedia.org/wiki/Privacy)

Whenever we talk about privacy, many people tend to think it in terms of *secrecy*. While secrecy is more about the information whereas privacy is more about the ability of one's control over that information. Though they both are different, they both go hand in hand with each other most of the time.

There goes a song in Tamil cinema which is quite popular,

> Let's take a selfie pulla...

In this selfie cultured digital world around us, the need to take privacy seriously arises naturally. Usage of smartphones, laptops and DSR/DSLR camera have become quite common these days. We also know that all these devices are controlled by the software that are already inside those devices. It can be the firmware (or) the operating system (or) the application itself. One such module of these software is called [EXIF](https://en.wikipedia.org/wiki/Exif) which stands for **EX**changeable **I**mage file **F**ormat. 

The EXIF defines a lot of properties like the size of the image, dimension, name and model of the device used, date and time of the picture taken, location where this picture was taken (if GPS is enabled and the application has the ability to get location from GPS), whether flash was fired or not when the picture was taken, etc., believe me, there are [a lot of such data](http://exiv2.org/tags.html) that can be embeded along with that awesome selfie / photograph that we shoot everyday.

We think, we are just taking pictures, but most of us aren't aware of the fact that all these so called *smart devices* also collect and embed a lot of other sensitive information with our pictures. You don't have to even believe what I am saying. You can try it yourself with this page that I built for demonstrating the same [here](https://prashere.gitlab.io/exifdata/)

In the above demonstration, the more *undefined* you see, the more happy you can be, because those informations are not present with your pictures. Here is one example that I tried myself.

![image of a fan](https://fsftn.org/blog/content/images/2016/12/20161228_162446.jpg)

What information can you extract from the above image? Yes, you are right. It's a ceiling fan and the fan is functioning. What else can you know?

![screenshot of fan with exif metadata](https://fsftn.org/blog/content/images/2016/12/with_geolocation.png)

Oh crap! This photograph seems to reveal a lot than what we thought! The location of where this picture was taken, the deivce used, date and time, whether flash used or not is also visible. Using these information we can also know that the person who shoot this photograph was using this particular device and this fan and the person was at that particular location on that particular date and time! and yeah the flash did not fire ;) 

Now what happens when I upload this to social networks (umm, I'll be specific, yeah facbeook)

![screenshot of the same image uploaded to facebook](https://fsftn.org/blog/content/images/2016/12/facebook_exif.png)

Look at this. Facebook retrieves the location and date from these pictures. A lot of such services on the web are waiting for us upload our data and build a profile around us and then sell it to third-party agencies for their profit. Even if we remove (or) edit, there is no way for us to make sure that those informations are actually removed from fb's server. This is how our privacy is compromised at a lot of stage. Remember, our intention was just to share a selfie or photograph that we just took, not any other information.

Imagine how much selfies and photograph of our family and friends we shoot and share it in Web! Most liberal minded people would easily say, *hey! you are ignorant and it's your mistake that you are not aware of such things*, well I would rather say *No. It's not our mistake*, because the software is proprietary in most of the case, we do not even know what the software does in the background and there is no way to know what else the software does when the source code is not available. Moreover, you and I didn't ask for such a feature and also we don't have the freedom to modify the source code under a proprietary regime. That is why we as a movement (Free Software movement) call for the adoption and usagae of [Free(dom) Software](https://www.gnu.org/philosophy/free-sw.en.html)

> When the proprietary software controls the device, it means the creator of the proprietary software is in indirect control of your device. It also means your device is not in your control.

So, what can we do about this?

  - re-configure your smartphone and other smart devices that has camera in it, so that they don't embed these information.
  - remove sensitive metadata from your pictures before uploading or sharing it with others.
  - GNU/Linux users can install a tool named [MAT - Metadata Anonymisation Toolkit](http://mat.boum.org/) which is also a *free software*. This software cleans our image of any such harmful metadata.
  - I don't find any such free software EXIF removers for Windows (may be because, I don't use windows and so I don't find a need to search for it).
  - There are some EXIF editors and removers for Android at Play Store. (again they are proprietary and I don't recommend them, for they can be harmful too).
  - There are no such EXIF editors / removers for Android in F-droid. (as far as I have searched).
  - don't use the **take picture** option directly from the social network and instant messengers app on your smartphone.
  - avoid using proprietary softwares and apps. free yourself by using a free software operating system like GNU/Linux.

I am not arguing against EXIF metadata, I am arguing for the case of user's privacy. The application and the ecosystem should be designed in such a way that a user has the control over their digital activity, for it is their data that this ecosystem is making use of.

*Note: By the end of January 2017 (26, 27, 28 & 29) the 2nd National Conference and Convention of Free Software Movement of India is set to happen at Chennai, Tamilnadu, India. This conference and convention will be discussion topics ranging from privacy, software freedom, commons, community networks, programming, etc., The confernce is named as [4CCon](https://4ccon.fsmi.in). Students, academicians, researchers, software experts, Internet activists, free software hacktivists, social activists are participating. You are also invited. Do visit the site and register yourself if you are interested.*
