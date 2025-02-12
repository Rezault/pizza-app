import os
import subprocess

def run_command(command):
    result = subprocess.run(command)
    if result.returncode != 0:
        print(f"❌ Error running {command}: {result.stderr}")
        exit(1)

print("🚀 Setting up Django project...")

# Install requirements
print("\n⬆️ Installing requirements (could take a few minutes)...")
run_command("pip install -r requirements.txt")

# Run migrations
print("\n📦 Applying database migrations...")
run_command("python manage.py migrate")

# Populate the database
print("\n🍕 Populating default pizza data...")
run_command("python manage.py populate_db")

# Collect static files
print("\n🎨 Collecting static files...")
run_command("python manage.py collectstatic --noinput")

print("\n✅ Setup complete! You can now run the server with: python manage.py runserver")
