# raspberrypi_face_recognition
Set up system for Raspberry Pi</br>
</br>
Need:</br>
MicroSD card (recommend 32G, larger than 32G will lead some problems when doing
formatting).
Download:</br>
https://www.raspberrypi.org/downloads/raspbian/</br>
Download “Raspbian Buster with desktop”</br>
Burning the image on the Mico SD card.</br>
https://www.balena.io/etcher/</br>
</br>
Tips: If the card already include an old system image or the card is larger than 32GB, you
need SD card format tool. Any SD card larger than 32GB is an SDXC card and will be default
formatted with the exFAT filesystem. Need reformat it as FAT32 form to support Raspbian
bootloader.</br>
</br>
SD card formatter:</br>
https://www.sdcard.org/downloads/formatter/</br>
</br>
Setting:</br>
Connect to wifi, set time zone</br>
Enable SSH and VNC (GUI: Open Application Menu => Preferences => Raspberry Pi</br>
Configuration => interfaces => enable SSH & VNC)</br>
</br>
Reboot</br>
Connect pi by SSH: ssh pi@10.0.0.240</br>
Password: raspberry </br>
</br>
</br>
https://zhuanlan.zhihu.com/p/59027897
