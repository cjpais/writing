# [Hashicorp Go Plugin Architecture](https://www.youtube.com/watch?v=SRvm3zQQc1Q)
  * See: <https://github.com/hashicorp/go-plugin>
  * Want multiprocess architecture to have stability
  * Should be as easy as implementing an interface
  * No weird building
  * Use rpc to communicate between processes.
  * "host" and "plugin" names, probably use this in general
  * **v1**
    * launch plugin
      * host tells plugin which ports it can use
      * host starts subproccess
      * waits for tcp
        * notes that stdout/stderr are only guaranteed streams (what bout sockets?)
          * i dont know anything about them
    * talk between the systems
      * plugin outputs address over stdout
      * host see it and tries to connect
        * after the first connection established the plugin closes its listener so no one else can connect
    * establish rpc connection
      * use stdlib `net/rpc`
    * data streams
      * cant stream data over rpc
      * basically creates new tcp connection then to `io.Reader`
        * need to come back 17:00
    * misc
      * basically rpc is nice because it doesnt really mean any dependency
      * can just implement interface and now boom you have a communication channel
      * dont need to understand what is going on underneath
      * can establish more rpc channels if needed
        * host broadcasts where to connect for the plugin then the plugin goes and talks
        * creates data stream etc...
      * uses stdout/stderr as control and log channels
  * **v2**
    * address problem in v1
      * basically opening ports was an issue (firewalls fucked you up)
        * send full address instead of just port
        * use unix domain socket instead of tcp (if you can *cough* windows.. ok fine wsl)
      * how to allow for interfaces to change
        * protocol versioning
          * if protocol doesn't match host then make error
          * can even change phys layer (wire)
  * **v3**
    * issues with v2
      * new connections are being created all the time, but closed relatively fast
        * people was running out of file handles in userspace
      * multiplexed connections (on tcp?)
        * single connection between host and plugins, all communications on top (multiplex on top)
          * random weird thought, we multiplex a lot OTA (over the air), can similar things be done 'on the wire'
            * maybe something stupid like having a 'file' where 'lines' of the file are actually independent data streams. and you can control the 'bandwidth' dynamically
  * **v4**
    * issues with v3
      * muxconn crashes randomly hahahahahaha
        * replaced by Yamux
      * also needed
        * one plugin host to serve multiple instances of itself
          * initial connection is a dispenser
            * host would ask plugin to dispense an instance of a plugin
              * ex: aws plugin, but different regions and different configs independently
        * installation of plugins could be easier
          * "plugin auto discovery"
            * Look in home dir, binary dir, curr dir
            * if matched 'glob' then try to execute, if can communicate then set it up
  * **v5**
    * issues with v4 
      * tty not preserved
        * launch plugin with file handle (not quite there with this part, i dont know enough)
        * creates a multiplexed stream for stdout and stderr
      * stdout and stderr couldn't be used because it was hijacked to establish connection
      * lots of plugins were shipped in the release, so releases were huge
        * plugin flattening
          * didnt quite get this
        * ship one binary, but subcommands would go get binary??
  * **v6**
    * needs moving forward
      * crypto secure plugins
        * vault sounds cool
          * didnt support plugins due to attack surface
        * *sign binaries*
        * very small window where binary can be 'swapped'
          * read everything into memory then verify signature and write to secure location
        * could encrypt all the data through (via tls), but since going through unix socket it implies root access
      * user versioning
        * basically look at node