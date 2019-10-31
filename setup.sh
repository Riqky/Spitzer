#used script: (that are not included in Kali)
#aquatone
#gobuster
#securityheaders.py
#testssl.sh
#interlace?


#TODO maybe first check for pip and python version
pip install . > /dev/null

#aquatone
mkdir /tmp/spitzer > /dev/null

wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip -P /tmp/spitzer/ > /dev/null
unzip /tmp/spitzer/aquatone_linux_amd64_1.7.0.zip -d /tmp/spitzer > /dev/null
mv /tmp/spitzer/aquatone /usr/local/bin/ > /dev/null

#gobuster
wget https://github.com/OJ/gobuster/releases/download/v3.0.1/gobuster-linux-amd64.7z -P /tmp/spitzer/
7z x /tmp/spitzer/gobuster-linux-amd64.7z -o/tmp/spitzer/
mv /tmp/spitzer/gobuster-linux-amd64/gobuster /usr/local/bin/
chmod +x /usr/local/bin/gobuster

rm -r /tmp/spitzer

#securityheaders.py
wget https://raw.githubusercontent.com/juerkkil/securityheaders/master/securityheaders.py -P /opt/spitzer/ > /dev/null

#testssl.sh
wget https://raw.githubusercontent.com/drwetter/testssl.sh/3.0/testssl.sh -P /opt/spitzer/ > /dev/null

#TODO maybe reinstall masscan, to make sure it is the latest version
#or ask this

