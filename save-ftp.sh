#!/bin/sh
cd /home/pi/save-survie
mkdir `date +%Y%m%d`
cd `date +%Y%m%d`
wget -r ftp://user:mdp@host/minecraft_Paperspigot\ -\ Survie
