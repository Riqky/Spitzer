#used script: (that are not included in Kali)
#aquatone
#gobuster
#securityheaders.py
#testssl.sh
#interlace?

#aquatone
wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip
unzip -j aquatone_linux_amd64_1.7.0.zip aquatone /usr/local/bin/
rm aquatone_linux_amd64_1.7.0.zip

#gobuster
wget https://github.com/OJ/gobuster/releases/download/v3.0.1/gobuster-linux-amd64.7z
unzip -j gobuster-linux-amd64.7z gobuster-linux-amd64/gobuster /usr/local/bin/
rm gobuster-linux-amd64.7z

#securityheaders.py
wget https://raw.githubusercontent.com/juerkkil/securityheaders/master/securityheaders.py -P /opt/spitzer/

#testssl.sh
wget https://raw.githubusercontent.com/drwetter/testssl.sh/3.0/testssl.sh -P /opt/splitzer/

#TODO maybe reinstall masscan, to make sure it is the latest version
#or ask this

#TODO maybe first check for pip and python version
pip install .

