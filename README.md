## Programming Question 3 - HackIM NullCon 2017

The given file is a repeatedly archived file in various formats. This can be found by successively running the 'file' UNIX command on it and unarchiving it based on the file command's output for the archive type.

After manually running 'file' and unarchive commands based on the archival type of the file obtained for a few times, I made a list of all the archival types used, as follows:
LZMA, XZ, gzip, ZPAQ, lzip, POSIX tar, bzip2 compressed data, NuFile, Zip, ARJ, 7-zip and Zoo

A few of them could be unarchived using existing archival commands in UNIx. Some others like those for XZ, ZPAQ, lzip, Zoo, 7-zip and ARJ could be installed using 'brew'. The following single *brew install* was capable of unarchiving Zip, ARJ, 7-zip and Zoo.
```
brew install unar
```

The NuFile archival format needed installation of 'nulib2' and 'nufxlib' which can be downloaded and installed from here: http://www.nulib.com/

Then I wrote the following python code to unarchive successively based on file type till an unarchived file was obtained after 254 iterations.

[Python Code](https://github.com/unique-nms/nullcon-2017-hackim-prog3/blob/master/p3.py)

The final file obtained was an *ASCII text* file which looked like shown below:

```
total 120
drwx------ 2 root     root     28672 Dec 23 21:01 apt-dpkg-install-kKBLWj
-rw-r--r-- 1 root     root     71259 Dec 23 19:50 apt-fast.list
-rw-r--r-- 1 root     root         0 Dec 23 19:50 apt-fast.lock
-rw-r--r-- 1 root     root         0 Dec 23 21:03 secr
drwx------ 3 root     root      4096 Dec 23 19:30 systemd-private-20af98806288452f91376e836938dc35-colord.service-hbUpEj
drwx------ 3 root     flag      4096 Dec 23 19:30 63336C756448746861486C35634442684C565A686353467566513D3D
```

Found flag string **63336C756448746861486C35634442684C565A686353467566513D3D**.

This was not the flag; so I tried 'hex' decoding the string which gave the following string that looked like it was base-64 encoded:
**c3ludHthaHl5cDBhLVZhcSFufQ==**

Base-64 decoding the above string gave this, **synt{ahyyp0a-Vaq!n}**.
This looked like the cipher text for the flag. On inspection, I predicted that the first 4 letters could be 'flag' and the substring 'ahyyp0a' could be 'nullc0n'. It was a Ceasar cipher with shift=13. Hence, the plain text and flag was:

:sparkles::sparkles:**flag{nullc0n-Ind!a}**:sparkles::sparkles:
