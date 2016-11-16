![PID1 for the sake!](http://maciej.lasyk.info/images/pid1.png)

# systemd-workshop

The main goal of this workshop is to introduce various aspects of systemd to
all of you who haven't used it extensively yet.

## Requirements

Our main requirement is having Linux distribution with systemd version at least
**229**. It might be installed on some virtual machine on your laptop. Just
make sure it works and running following command returns required systemd
version:

```
$ systemctl --version
systemd 229
```

You may install [Fedora 24](https://getfedora.org/) (server or workstation
edition) - it already has systemd 229 installed.

## How to register?

We're still working on that. Follow **#systemdkrkworkshops** Twitter tag

## Who's the organizer?

That's actually community event. Organizer would be [Anonymous Admins
group](https://www.meetup.com/AnonimowiAdmini/)

## Venue?

That will be Lumesse office in Kraków. Details will be posted together with
registration.

## When?

Probably 26th November 2016

## Who's gonna be the teacher?

[Marcin Skarbek](https://www.linkedin.com/in/marcinskarbek) and [Maciej Lasyk](https://www.linkedin.com/in/maciej-lasyk-04819942)

## Agenda

### systemd-bin (1h)

During this part we'll discover various binaries provided by systemd and use
some ot those:

```
systemd-path                  
systemd-detect-virt             systemd-resolve               
systemctl                       systemd-escape                  systemd-run                   
systemd-analyze                 systemd-firstboot
systemd-ask-password
systemd-sysusers              
systemd-bus-proxy               systemd-inhibit
systemd-timesync              
systemd-cat                     systemd-machine-id-setup
systemd-tmpfiles              
systemd-cgls                    systemd-network
systemd-cgtop                   systemd-notify                                                
systemd-coredump                systemd-nspawn                                                
```

### unit files (2h)

Unit files are a basic configuration tools in systemd which define behaviour for the whole system.
We'll learn what types of unit files systemd provides, what is the purpose of them
and how to correctly write a new one. Thanks to that knowledge both creating quick ad hoc `service`
and fairly complicated chain of `services` in separate `target` shouldn't be a problem. 

### journald (1h)

Here be dragons. We'll dive into specifics of managing logs with journald.
Starting with reading logs and finishing on creating very specific queries. If
there's enough time maybe we'll try to push logs to central repository?

### systemd-nspawn (2h)

We don't need Docker to play with containers, systemd-nspawn will let you run
both system and aplication containers providing stable workflow and predictable behaviour.
We'll learn how to create containers, restrict their capabiliteis and resources
and write custom unit files for them. We'll also try to run Docker container under
systemd-nspawn supervision to understand difrences and srong/weak points in both sollutions. 

### developing systemd-aware apps (until you die)

We'll learn how to integrate Python (and maybe C and Java?) applications with 
systemd making systemd aware of applications' state. Thanks to that application 
operational aspects like automated failover, restart and others will be done 
without manual intervention and in a clear, and proper way.
