#used script: (that are not included in Kali)
#aquatone
#gobuster
#securityheaders.py
#testssl.sh


if [ ! -z `which pip3` ]; then
    pip3 install . 
else
    echo -e '\033[1;31m[!] ERROR: No pip3 installed!\033[0;0m'
    exit 1
fi
#if /tmp/spitzer exsists, stop the script
if [ -d "/opt/spitzer/" ]; then
    exit 0
fi
mkdir /tmp/spitzer

#aquatone"
if [ -z `which aquatone` ]; then
    wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip -P /tmp/spitzer/ 
    unzip /tmp/spitzer/aquatone_linux_amd64_1.7.0.zip -d /tmp/spitzer 
    mv /tmp/spitzer/aquatone /usr/local/bin/ 
fi

#gobuster
if [ -z `which gobuster` ]; then
    wget https://github.com/OJ/gobuster/releases/download/v3.0.1/gobuster-linux-amd64.7z -P /tmp/spitzer/
    7z x /tmp/spitzer/gobuster-linux-amd64.7z -o/tmp/spitzer/
    mv /tmp/spitzer/gobuster-linux-amd64/gobuster /usr/local/bin/
    chmod +x /usr/local/bin/gobuster
fi

#securityheaders.py
wget https://raw.githubusercontent.com/juerkkil/securityheaders/master/securityheaders.py -P /opt/spitzer/ 

#testssl.sh
git clone  https://github.com/drwetter/testssl.sh /opt/spitzer/testssl

chmod +x /opt/spitzer/*

#masscan
mass=`masscan --version`
massversion=${mass:16:6}
massnum=`echo "$massversion" | tr -d .`
if [ $massnum -lt 106 ]; then
    read -p "Masscan appears to be outdated, do you want to reinstall it? y/n [y] " yn
    case $yn in
        [Nn]* ) rm -r /tmp/spitzer; exit;;
        * )
            #remove current version
            loc=`which masscan`
            rm $loc
            git clone https://github.com/robertdavidgraham/masscan /tmp/spitzer/masscan
            cd /tmp/spitzer/masscan; make -j
            mv /tmp/spitzer/masscan/bin/masscan /usr/local/bin/;;
    esac
fi

rm -r /tmp/spitzer