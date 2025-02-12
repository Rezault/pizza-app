import os
import subprocess

print("🚀 Setting up Django project...")

# Run migrations
print("📦 Applying database migrations...")
subprocess.run(["python", "manage.py", "migrate"])

# Populate the database
print("🍕 Populating default pizza data...")
subprocess.run(["python", "manage.py", "populate_db"])

# Collect static files
print("🎨 Collecting static files...")
subprocess.run(["python", "manage.py", "collectstatic", "--noinput"])

print("✅ Setup complete! You can now run the server with: python manage.py runserver")
