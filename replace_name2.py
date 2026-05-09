import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    # Titles
    new_content = new_content.replace('<title>Trader Dashboard - Stocker</title>', '<title>Trader Dashboard - Trading Dashboard</title>')
    new_content = new_content.replace('<title>Admin Dashboard - Stocker</title>', '<title>Admin Dashboard - Trading Dashboard</title>')
    new_content = new_content.replace('<title>Stocker</title>', '<title>Trading Dashboard</title>')
    new_content = new_content.replace('<title>Stocker - Cloud-Based Stock Trading Platform</title>', '<title>Trading Dashboard - Cloud-Based Stock Trading Platform</title>')
    new_content = new_content.replace('<title>Our Services - Stocker</title>', '<title>Our Services - Trading Dashboard</title>')
    new_content = new_content.replace('<title>All Transactions - Stocker</title>', '<title>All Transactions - Trading Dashboard</title>')
    
    # sitename headers
    new_content = new_content.replace('>STOCKER<', '>TRADING DASHBOARD<')
    new_content = new_content.replace('class="sitename">STOCKER</h1>', 'class="sitename">TRADING DASHBOARD</h1>')
    new_content = new_content.replace('class="sitename text-primary mb-0">STOCKER<span', 'class="sitename text-primary mb-0">TRADING DASHBOARD<span')
    
    # other mentions
    new_content = new_content.replace('Stocker Assistant', 'Trading Dashboard Assistant')
    new_content = new_content.replace('Stocker, based in Hyderabad', 'Trading Dashboard, based in Hyderabad')
    new_content = new_content.replace('<span class="sitename">Stocker</span>', '<span class="sitename">Trading Dashboard</span>')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('templates'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

# Update app.py
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()
new_content = content.replace('Stocker Assistant', 'Trading Dashboard Assistant')
if new_content != content:
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated app.py")

