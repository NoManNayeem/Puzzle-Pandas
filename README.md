# Puzzle-Pandas

Welcome to **Puzzle-Pandas**, a quiz platform where you can play exciting quizzes and win amazing gifts! Dive into a variety of topics, challenge your knowledge, and get rewarded.

## Getting Started

Start playing by visiting our platform: [Puzzle-Pandas](https://github.com/NoManNayeem/Puzzle-Pandas.git)

### How to Play

1. **Sign Up/Login**: Create a new account or log in.
2. **Choose a Quiz**: Select from a variety of topics you're interested in.
3. **Play & Score**: Answer questions correctly to score points.
4. **Win Gifts**: High scores can win you exciting gifts.

### Features

- A wide range of topics
- Timed quizzes
- Leaderboards to see how you rank against others
- Rewards for top scorers

### Contributing

We welcome contributions to make Puzzle-Pandas even better. Feel free to fork the repository and submit pull requests.

### Support

For support, you can open an issue on the GitHub repository or contact us directly at support@puzzle-pandas.com.

Join **Puzzle-Pandas** today and start playing your way to fantastic prizes!




# Deployment Instructions

This document outlines the steps necessary to deploy the Django project both in a development environment and on a production server.

## Development Setup

### Step 1: Clone the Repository
Clone the repository from GitHub to get the project's code on your local machine.

```bash
git clone https://github.com/NoManNayeem/Puzzle-Pandas.git
cd Puzzle-Pandas
```

### Step 2: Install Required Software
Install Python, pip, and other necessary software including Nginx, and Gunicorn.

```bash
sudo apt install python3-pip python3-dev libpq-dev nginx curl
```

### Step 3: Set Up the Project
Repeat Steps 1 to 3 from the Development Setup on your production server.

### Step 4: Collect Static Files
Collect static files into a single directory for Nginx to serve.

```bash
python manage.py collectstatic
```

### Step 5: Gunicorn Configuration
Start the Gunicorn application server to serve the Django app.
```bash
gunicorn --workers 3 --bind unix:/home/yourusername/Puzzle-Pandas/puzzlepandas.sock PuzzlePandas.wsgi:application
```

### Step 6: Configure Nginx to Proxy Pass to Gunicorn
Create an Nginx server block configuration:
```bash
sudo nano /etc/nginx/sites-available/puzzlepandas
```

Insert the following configuration:
```bash
server {
    listen 80;
    server_name yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/yourusername/Puzzle-Pandas;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/yourusername/Puzzle-Pandas/puzzlepandas.sock;
    }
}
```
Link the file to the sites-enabled directory:

```bash
sudo ln -s /etc/nginx/sites-available/puzzlepandas /etc/nginx/sites-enabled
```

### Step 7: Restart Nginx
Restart Nginx to apply the changes:
```bash
sudo systemctl restart nginx
```
### Step 8: Secure the Server
Consider securing your application with SSL/TLS using Let's Encrypt.
```bash
sudo apt install python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

## Additional Configuration
Remember to adjust ALLOWED_HOSTS in your Django settings.py and manage your database settings as per your environment specifications.
```bash
ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']
```
These steps should help you to deploy and run your Django application both in development and in production environments.

## Note:
You can adjust the domain names, paths, and specific settings according to your project's requirements. Follow the link below for more:
```bash
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu
```
