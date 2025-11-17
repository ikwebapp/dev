#!/bin/bash

NGINX_CONF="/etc/nginx/sites-available/ikweb"
GUNICORN_SERVICE="/etc/systemd/system/gunicorn.service"

# Create cloudflare folder
sudo mkdir -p /etc/ssl/cloudflare
sudo cp ~/ikweb/conf/origin.* /etc/ssl/cloudflare

sudo mkdir -p /var/www/ikweb
sudo cp -r ~/ikweb/static /var/www/ikweb/

# Create Nginx configuration
echo "Creating Nginx configuration..."

sudo bash -c "cat > $NGINX_CONF" << 'EOF'
server {
    listen 443 ssl;
    server_name iksaan.com www.iksaan.com;

    ssl_certificate /etc/ssl/cloudflare/origin.pem;
    ssl_certificate_key /etc/ssl/cloudflare/origin.key;

    location / {
        proxy_pass http://127.0.0.1:8001;
    }

    location /static/ {
        alias /var/www/ikweb/static/;
    }
}

EOF

# Enable Nginx site
sudo ln -sf "$NGINX_CONF" /etc/nginx/sites-enabled/ikweb
sudo rm -f /etc/nginx/sites-enabled/default

# Test and reload Nginx
echo "Testing Nginx..."
sudo nginx -t && sudo systemctl restart nginx


# Create Gunicorn service file
echo "Creating Gunicorn service..."

sudo bash -c "cat > $GUNICORN_SERVICE" << 'EOF'
[Unit]
Description=Gunicorn for Django (ikweb)
After=network.target

[Service]
User=webadmin
Group=www-data
WorkingDirectory=/home/webadmin/ikweb
ExecStart=/home/webadmin/ikweb/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8001 ikweb.wsgi:application

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd and start Gunicorn
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl restart gunicorn

echo "Nginx and Gunicorn setup completed successfully!"

