set -x
echo -e "\n"
cat /etc/bash.bashrc
echo -e "\n"
cat /etc/environment
echo -e "\n"
cat /etc/apt/apt.conf
echo -e "\n"
set | egrep "prox|PROX"
echo -e "\n"
gsettings list-recursively org.gnome.system.proxy
echo -e "\n"

