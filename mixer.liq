#!/usr/bin/liquidsoap

# Put the log file in some directory where
# you have permission to write.
set("log.file.path","/tmp/<script>.log")
# Print log messages to the console,
# can also be done by passing the -v option to liquidsoap.
set("log.stdout", true)

localstream = (input.alsa(id="liquidsoap"):source(2,0,0))

stereo.left(source1)
stereo.right(source2)

# Server settings
set("harbor.bind_addr","192.168.1.1")

# An emergency file
emergency = single("/path/to/emergency/single.ogg")

# A playlist
#playlist = playlist("/path/to/playlist")

# A live source
remotestream = input.harbor("remotestream",port=8080,password="hackme")

# fallback
radio = fallback(track_sensitive=false,
                 [live,emergency])

# Stream it out
output.icecast(%vorbis,
  host = "localhost", port = 8000,
  password = "hackme", mount = "soap.ogg",
  radio)
