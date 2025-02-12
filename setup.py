import sys
import subprocess

def run_command(command):
    result = subprocess.run(command)
    if result.returncode != 0:
        print(f"❌ Error running {command}: {result.stderr}")
        print("\n⚠️ This error could've been caused if pip is out of date. Try updating pip: `python -m pip install --upgrade pip`\n")
        print("\n⚠️ Alternatively, try updating to the newest version of python.")
        exit(1)

# Check current pip version
pip_version = subprocess.run(
    [sys.executable, "-m", "pip", "--version"],
    capture_output=True,
    text=True
).stdout.strip()

print(f"🔍 Current pip version: {pip_version}")

# Suggest upgrade if pip is outdated
print("\n⚠️ If you run into issues, consider upgrading pip manually: `python -m pip install --upgrade pip`\n")

print("🚀 Setting up Django project...")

# Install requirements
print("\n⬆️ Installing requirements (could take a few minutes)...")
run_command(f"{sys.executable} -m pip install -r requirements.txt")

# Run migrations
print("\n📦 Applying database migrations...")
run_command(f"{sys.executable} manage.py migrate")

# Populate the database
print("\n🍕 Populating default pizza data...")
run_command(f"{sys.executable} manage.py populate_db")

# Collect static files
print("\n🎨 Collecting static files...")
run_command(f"{sys.executable} manage.py collectstatic --noinput")

print("\n✅ Setup complete! You can now run the server with: python manage.py runserver")
