set -x
echo -e "\n"
update-alternatives --query java | grep 'Value: ' | sed 's/Value: \(.*\)\/bin\/java/\1\/lib\/net.properties/' | xargs cat | egrep -i "prox"
echo -e "\n"
cat /etc/bash.bashrc | egrep -i "prox"
echo -e "\n"
cat /etc/environment | egrep -i "prox"
echo -e "\n"
cat /etc/apt/apt.conf | egrep -i "prox"
echo -e "\n"
set | egrep -i "prox"
echo -e "\n"
gsettings list-recursively org.gnome.system.proxy
echo -e "\n"
