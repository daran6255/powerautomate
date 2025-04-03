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

git clone https://github.com/daran6255/backend.git


### Install dependency
sudo apt install python3-pip
sudo apt install python3.12-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt