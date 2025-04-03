## Permision for pem file
icacls C:\External-projects\WinVinaya\powerautomate\training_powerautomate.pem /grant light:(F)

icacls.exe training_powerautomate.pem /reset
whoami
icacls.exe training_powerautomate.pem /grant:r dharanidaran\daran:(R)
icacls.exe training_powerautomate.pem /inheritance:r

### step-1
sudo apt update
sudo apt upgrade -y

### step-2 Install postgres sql
sudo apt install postgresql postgresql-contrib -y
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo systemctl status postgresql

#### create user in postgres
sudo -i -u postgres
psql
ALTER USER postgres WITH PASSWORD '12345';
\q
exit

#### create new database 
sudo -u postgres createdb employee_db

### push from git to server
git clone https://github.com/daran6255/powerautomate.git


### Install dependency
sudo apt install python3-pip
sudo apt install python3.12-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### Pm2 config
sudo apt install -y nodejs npm
sudo npm install -g pm2
cd ~/powerautomate
source venv/bin/activate
pm2 start "venv/bin/python3 main.py" --name powerautomate
pm2 save
pm2 startup
pm2 list
pm2 logs powerautomate

pm2 restart powerautomate - ## for restart
pm2 stop powerautomate - ## for stop


## Making It Available on Port 80 (NGINX)

### Install Nginx
sudo apt install nginx -y

### Nginx Configuration
sudo nano /etc/nginx/sites-available/default

server {
	listen 80;
	server_name training.winvinaya.com www.training.winvinaya.com;

	location / {
		proxy_pass http://127.0.0.1:5000;
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	}
}


sudo systemctl restart nginx

sudo certbot --nginx -d training.winvinaya.com -d www.training.winvinaya.com

ubuntu@ip-172-31-1-245:~$ sudo certbot --nginx -d training.winvinaya.com -d www.training.winvinaya.com
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Enter email address (used for urgent renewal and security notices)
 (Enter 'c' to cancel): dharanidaran.a@winvinaya.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.5-February-24-2025.pdf. You must
agree in order to register with the ACME server. Do you agree?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: y

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Would you be willing, once your first certificate is successfully issued, to
share your email address with the Electronic Frontier Foundation, a founding
partner of the Let's Encrypt project and the non-profit organization that
develops Certbot? We'd like to send you email about our work encrypting the web,
EFF news, campaigns, and ways to support digital freedom.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: y
Account registered.
Requesting a certificate for training.winvinaya.com and www.training.winvinaya.com

Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/training.winvinaya.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/training.winvinaya.com/privkey.pem
This certificate expires on 2025-07-02.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.

Deploying certificate
Successfully deployed certificate for training.winvinaya.com to /etc/nginx/sites-enabled/default
Successfully deployed certificate for www.training.winvinaya.com to /etc/nginx/sites-enabled/default
Congratulations! You have successfully enabled HTTPS on https://training.winvinaya.com and https://www.training.winvinaya.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
If you like Certbot, please consider supporting our work by:
 * Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
 * Donating to EFF:                    https://eff.org/donate-le
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

-------------------------------
\c employee_db;
\dt;
SELECT * FROM employee;
