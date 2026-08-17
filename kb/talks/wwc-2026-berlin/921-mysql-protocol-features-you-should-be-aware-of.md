---
id: 921
title: "MySQL Protocol Features You Should Be Aware Of"
slug: mysql-protocol-features-you-should-be-aware-of
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Data & Databases"
type: "Lightning Talk"
stage: "Airstream 1"
tags: ["Databases", "MySQL", "Networking", "SQL"]
speakers: ["Daniël van Eeden"]
speaker_companies: ["PingCAP"]
day: 2
starts_at: 2026-07-10T10:35:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=PqrERF7rmkM
video_id: PqrERF7rmkM
session_page: https://app.wearedevelopers.com/events/16/session/921
transcript: true
---

# MySQL Protocol Features You Should Be Aware Of

**Daniël van Eeden (Technical Support Engineer — PingCAP)**

`Track: Data & Databases` · `Type: Lightning Talk` · `Stage: Airstream 1`

`#Databases` `#MySQL` `#Networking` `#SQL`

[Watch the recording](https://www.youtube.com/watch?v=PqrERF7rmkM) · [Session page](https://app.wearedevelopers.com/events/16/session/921)

## Abstract

This talk goes over some less used protocol features like Connection Attributes, Query Attributes, Session Tracking and zstd compression.

These features can help you to create better integrations and applications.

Connection Attributes are somewhat more known, but many people don't know that applications can (and should) add their own information.

And where Connection Attributes are connection based, Query attributes are query based. These are useful today, but they also have the potential to help with future improvements.

And Session Tracking can really help in cases where you write to a primary and then read from a replica. This can give you the GTID from the commit so you can wait for that when reading from the replica. This could replace cases where you would now directly read from the primary to get the read-after-write behavior that you need.

And compression has been in the protocol for a long time, but this was always based on zlib. Now zstandard has entered the picture.

## Speakers

### Daniël van Eeden

*Technical Support Engineer — PingCAP*

Daniël has been working on TiDB and related projects. Before that he worked on scaling MySQL for a large company that sells hotel rooms. One of the side projects he has been working in is the MySQL protocol dissector in Wireshark.

## Transcript

*1,606 words · source: yt (en)*

**[0:02](https://www.youtube.com/watch?v=PqrERF7rmkM&t=2s)** Hello. So, I'm Daniel. I'm from the Netherlands and I work for TiDB. Um and today I'm going to tell you about like some of the the features in the MySQL protocol. I'm not going over the full MySQL protocol. The MySQL protocol is the protocol that's being used between MySQL clients, different MySQL servers, but also it's a protocol used by MariaDB, uh Vitess, uh and also with TiDB, like the company I work for. Um so, why I'm interested in the protocol is that like I've been working on a few open source projects uh including Wireshark, which is uh a tool that can help you to actually look into what communication is going on between different systems including MySQL. It

**[0:51](https://www.youtube.com/watch?v=PqrERF7rmkM&t=51s)** can completely decode the whole protocol. So, if you don't know Wireshark, um it's really a useful tool if you're working with MySQL um and the MySQL protocol. I've also been working on uh Go MySQL, which is a uh a Go library for working with the MySQL protocol including replication and all the other uh tidbits that come with the MySQL protocol. Um so, like I had to re-implement a lot of things that normally might be used uh by like the the C library that MySQL provides. And I don't want to use that library in Go, so that's why I had to re-implement things. I work for TiDB, a MySQL um compatible database. I did some work on MySQL and I'm also still maintaining the Perl driver for

**[1:38](https://www.youtube.com/watch?v=PqrERF7rmkM&t=98s)** MySQL, which does use the the C library that Oracle uh provides for MySQL. So, the very first uh feature of the MySQL protocol that I think you should be aware of is session tracking. So, session tracking means that like you send a query, you get an okay packet back. Uh yes, I have slides, but it's not showing on the monitor. It does show on my monitor. Yes, there we are. Um so the By the way, the slides have a lot of information on there. Uh so if you later like download the slides, that should allow you to like get the whole whole story even if for the slides that I might not be able to cover in this time frame.

**[2:26](https://www.youtube.com/watch?v=PqrERF7rmkM&t=146s)** So in this okay packet, you you can get a lot more information. Um information about like the default schema changing, um user-defined variables, uh prepared statements, and and many other things. Um this is something you have to turn on in MySQL, same for MariaDB, and same for other databases. And then you can get a lot of information in the okay packet. And then you're like, okay, why would I uh want to do this? You can get like a statement ID that you can then use to like look up data in the performance schema to get more information about that specific statement. Uh that's a very useful thing. And the most important thing here is to get the GTID information. So you're like inserting a new record, and you get back

**[3:12](https://www.youtube.com/watch?v=PqrERF7rmkM&t=192s)** the transaction ID of that specific record, and then you can use that to do like a lot of nifty things. Um one of those things um is actually um write the record to to the to the primary, get back the GTID, and then before you're reading from a read replica for maybe your next query, you can tell the database to wait until that specific record has arrived on the on the replica, and then you can do more consistent reads uh more easily. And that's a very useful thing, and that's uh something not many people are actually using, and I think they should. So here um uh uh a quick demonstration. So you just uh

**[4:00](https://www.youtube.com/watch?v=PqrERF7rmkM&t=240s)** uh first uh creating a a new record and then you do doing a a select on the replica and then you get like back the 840 number. Well, you inserted a uh uh more records, so you should get back a higher number. And then actually you're waiting until the new record has arrived. You see that you now get exact same result as you get from the primary. So if you want to have more consistent reads, this really works. Um and for demonstration purposes, I enabled delayed replication, which makes it a more visible, but this might also happen if you're running like schema changes or other things. Next feature, compression. So this has been in the MySQL protocol for many years. Not many people use it.

**[4:48](https://www.youtube.com/watch?v=PqrERF7rmkM&t=288s)** Wasn't very useful feature. Um there's not a lot of instrumentation. There's not a lot of documentation. Some people just enable it and hope for the best, which I don't think is a the best strategy. Um but it can be really useful um even today. Like it was meant for like slow links and things. But now with uh clouds, bandwidth can be quite ex- expensive. And then it can actually reduce the bandwidth you're using with your cloud provider. Um so that can be a uh really useful. And originally it was only the Zlib uh protocol that they were supporting. They recently added Zstandard, which does way better compression. And one of the thing many people don't really um recognize is that like it only compresses things that are larger than

**[5:37](https://www.youtube.com/watch?v=PqrERF7rmkM&t=337s)** like 50 bytes. Uh so like small things, like small queries, are not uh compressed. So that helps to make things more efficient CPU-wise. Um And with Zstandard, you can actually now set the compression level, so you have even more control. Uh still not a lot of information in the server itself. Uh but you can get some information um if you're actually using um like uh Wireshark or other tools. Just skipping over a few things here. Yeah, so like one of the things is that um with compression, if you actually look in the the network particle and see like what package are being sent back and forth and look at this into great detail with like the compression header, how

**[6:26](https://www.youtube.com/watch?v=PqrERF7rmkM&t=386s)** many bytes it takes, and these things, um eventually you find out that like um some like example uh payload uh took like three packets. You see three different packets being sent um like 50 uh kilobytes in total. Um but this is being limited by the net buffer length, and it's actually something you can fix by just increasing it a little bit, and then you only get one packet. So, with a little bit of tuning you and looking at the protocol itself, you can get way better uh performance because every packet has some overhead, um and limiting this uh really helps. Uh I'll just skip over a few things.

**[7:13](https://www.youtube.com/watch?v=PqrERF7rmkM&t=433s)** Connection attributes. Like if you're a DBA and you're looking at your process list, it's really useful to get some more ex- information from the client uh about what the connection is being used for. Like in this example, you can see that uh this is uh just a a program called MySQL, which is the MySQL client. You can see the version, you can see like uh the process ID. This is the process ID that it had on the client. Um this is just being sent by the uh uh client when setting up the connection. Um, but this can be used for many other things. It can have like version information, but it could also be like, well, is it a production connection? Or is it like a critical connection? Or is it um, anything else that may be relevant for your

**[8:01](https://www.youtube.com/watch?v=PqrERF7rmkM&t=481s)** environment. So, that's very uh very useful. And this is actually one of the things you can just easily set up by just When you set up a connection, you can provide connection attributes, just key values. Um, and that's a very useful thing. Um, especially when you look at the the database side and maybe the database gets overloaded or you see weird queries. You want to know if this is from the the recent release or maybe a another host that has an older version of of the application. Um, really useful feature and not used very much. Uh Besides connection attributes, which are connection based, there are also query attributes, which allow you to do a

**[8:48](https://www.youtube.com/watch?v=PqrERF7rmkM&t=528s)** similar thing, but on a query per query basis. Um, less useful, I I would say, um, but can be used for a few different things. Um, so here for example, I'm using uh a simple select query and I'm setting a few uh parameters. These can be things that are normally only like valid on a um per query basis. Maybe like a proxy server and you want to know like for which uh client the the connection was being used. Uh Secu- secure connections. I think we're almost out of time. Um, but secure connections is also one of the things that's now actually being

**[9:36](https://www.youtube.com/watch?v=PqrERF7rmkM&t=576s)** used a lot more. But, uh a lot of people are not looking into all the details of this. And there's so much uh specifics for MySQL where you should be looking at like make sure that you have your your right CA set up and not just expect it to be exactly the same as like a web server because web servers and databases are different. And uh TLS is a really important thing uh for security. I'll just Oh. I don't think we have time for questions, but uh >> Thank you very much, Daniel. And give it up.
