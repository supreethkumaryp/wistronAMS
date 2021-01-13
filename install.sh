#!/bin/sh

echo ╭╮╭╮╭╮╱╱╱╭╮╱╱╱╱╱╱╱╱╱╭━━━┳━╮╭━┳━━━╮
echo ┃┃┃┃┃┃╱╱╭╯╰╮╱╱╱╱╱╱╱╱┃╭━╮┃┃╰╯┃┃╭━╮┃
echo ┃┃┃┃┃┣┳━┻╮╭╋━┳━━┳━╮╱┃┃╱┃┃╭╮╭╮┃╰━━╮
echo ┃╰╯╰╯┣┫━━┫┃┃╭┫╭╮┃╭╮╮┃╰━╯┃┃┃┃┃┣━━╮┃
echo ╰╮╭╮╭┫┣━━┃╰┫┃┃╰╯┃┃┃┃┃╭━╮┃┃┃┃┃┃╰━╯┃
echo ╱╰╯╰╯╰┻━━┻━┻╯╰━━┻╯╰╯╰╯╱╰┻╯╰╯╰┻━━━╯
echo ""

echo "Creating Sites Dir"
mkdir ~/Sites

echo "Creating Dir Wistron-AMS inside Sites Dir"
mkdir ~/Sites/Wistron-AMS

echo "Copying Application to Wistron-AMS"
cp -r ./* ~/Sites/Wistron-AMS

echo "Installing Dependencies"
sudo pip3 install -r ~/Sites/Wistron-AMS/requirements.txt

echo "Installing mod_wsgi"
sudo pip3 install mod_wsgi

echo "Creating wsgi file"
cat > ~/Sites/Wistron-AMS/app.wsgi << EOL
import sys
from app import create_app
from config import config_dict

sys.path.insert(0, '/Users/$(basename $HOME)/Sites/Wistron-AMS')

app_config = config_dict['Production']

application = create_app(app_config)
EOL

echo "Creating backup of httpd.conf as httpd.conf.bak"
sudo cp -v /etc/apache2/httpd.conf /etc/apache2/httpd.conf.bak

echo "Configuring Apache for Wistron AMS"
sudo cat >> /etc/apache2/httpd.conf << EOL


LoadModule wsgi_module "/opt/anaconda3/lib/python3.8/site-packages/mod_wsgi/server/mod_wsgi-py38.cpython-38-darwin.so"
WSGIPythonHome "/opt/anaconda3"

<Directory "/Users/$(basename $HOME)/Sites/Wistron-AMS">
  Options Indexes MultiViews FollowSymLinks
  AllowOverride None
  Require all granted
</Directory>
WSGIScriptAlias /wistron-ams /Users/$(basename $HOME)/Sites/Wistron-AMS/app.wsgi
EOL

echo "Restarting Apache"
sudo apachectl restart

echo "Deployment Successful"
echo "Open <mac_mini_ip_address>/wistron-ams in your laptop"
