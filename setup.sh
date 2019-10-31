#used script: (that are not included in Kali)
#aquatone
#gobuster
#securityheaders.py
#testssl.sh
#interlace?


#TODO maybe first check for pip and python version
pip install .

#aquatone
mkdir /tmp/spitzer

wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip -P /tmp/spitzer/
unzip /tmp/spitzer/aquatone_linux_amd64_1.7.0.zip -d /tmp/spitzer
mv /tmp/spitzer/aquatone /usr/local/bin/

#gobuster
wget https://github.com/OJ/gobuster/releases/download/v3.0.1/gobuster-linux-amd64.7z -P /tmp/spitzer/
7z x /tmp/spitzer/gobuster-linux-amd64.7z -o /tmp/spitzer/
mv /tmp/spitzer/gobuster-linux-amd64/gobuster /usr/local/bin/

#rm -r /tmp/spitzer

#securityheaders.py
wget https://raw.githubusercontent.com/juerkkil/securityheaders/master/securityheaders.py -P /opt/spitzer/

#testssl.sh
wget https://raw.githubusercontent.com/drwetter/testssl.sh/3.0/testssl.sh -P /opt/spitzer/

#TODO maybe reinstall masscan, to make sure it is the latest version
#or ask this

