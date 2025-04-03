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