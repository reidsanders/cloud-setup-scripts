#! bash
## From https://docs.markhh.com/pages/dev/linux-mount-gdrive/
sudo add-apt-repository ppa:alessandro-strada/ppa
sudo apt-get update && sudo apt-get install google-drive-ocamlfuse
echo $'#!/bin/sh\necho $* > /dev/stderr' > xdg-open
chmod 755 xdg-open
echo "Go to url and give access:"
env PATH=`pwd`:$PATH google-drive-ocamlfuse
mkdir ~/G_DRIVE
google-drive-ocamlfuse ~/G_DRIVE
