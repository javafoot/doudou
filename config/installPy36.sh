## Code in the Name of LORD JESUS CHRIST
cat << EOF > installPy36.sh
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python36u python36u-pip
ln -s /usr/bin/python3.6 /usr/bin/python3
ln -s /usr/bin/pip3.6 /usr/bin/pip3
pip3 install --upgrade pip
##pip3 install pysftp
EOF
chmod 755 installPy36.sh
./installPy36.sh  ## Need to be run under the root account

## Glory to GOD
