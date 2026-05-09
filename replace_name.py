import os
import re

directories_to_check = ['templates', 'static', '.']

replacements = [
    (re.compile(r'Stocker\b(?!\.(png|jpg|css|js))', re.IGNORECASE), lambda m: 'Trading Dashboard' if m.group(0).istitle() else ('TRADING DASHBOARD' if m.group(0).isupper() else 'trading dashboard'))
]

# Specifically we want to avoid replacing:
# - 'stocker_users'
# - 'logo stocker.png'
# - 'stocker-theme'
# - 'stocker_secret'
# We can do this safely by only replacing text in HTML nodes, or using a safer regex.

# Let's refine the script to only replace specific known strings:
exact_replacements = [
    ("Stocker", "Trading Dashboard"),
    ("STOCKER", "TRADING DASHBOARD"),
]

# Files to process
def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    # Replace in title tags
    new_content = re.sub(r'<title>(.*?)Stocker(.*?)</title>', r'<title>\1Trading Dashboard\2</title>', new_content)
    
    # Replace in sitename
    new_content = new_content.replace('>STOCKER<', '>TRADING DASHBOARD<')
    new_content = new_content.replace('>Stocker<', '>Trading Dashboard<')
    
    # Replace in plain text like "Stocker Assistant"
    new_content = new_content.replace('Stocker Assistant', 'Trading Dashboard Assistant')
    
    # "Stocker, based in Hyderabad"
    new_content = new_content.replace('Stocker, based', 'Trading Dashboard, based')
    
    # "Admin Dashboard - Stocker" is handled by title regex
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('templates'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

# Check app.py for any user-facing messages or titles
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()
new_content = content.replace('Stocker', 'Trading Dashboard')
# revert any table names if they were affected
new_content = new_content.replace('Trading Dashboard_users', 'stocker_users')
new_content = new_content.replace('Trading Dashboard_stocks', 'stocker_stocks')
new_content = new_content.replace('Trading Dashboard_transactions', 'stocker_transactions')
new_content = new_content.replace('Trading Dashboard_portfolio', 'stocker_portfolio')
new_content = new_content.replace('Trading Dashboard_watchlist', 'stocker_watchlist')
new_content = new_content.replace('Trading Dashboard_secret', 'stocker_secret')

if new_content != content:
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated app.py")

