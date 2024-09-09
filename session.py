try:
    from pyrogram import Client, __version__ as pyrogram_version
except ImportError:
    print("Pyrogram is not installed. Please install it using:\n\npip3 install pyrogram tgcrypto")
    exit(1)

# Ensure the Pyrogram version is 2.0 or greater
if pyrogram_version.split(".")[0] < "2":
    print(f"Your Pyrogram version ({pyrogram_version}) is not supported. Please upgrade to Pyrogram V2 or greater:\n\npip3 install --upgrade pyrogram")
    exit(1)

print("Required Pyrogram V2 or greater.")
try:
    API_KEY = int(input("Enter API KEY: "))
    API_HASH = input("Enter API HASH: ")
except ValueError:
    print("Invalid API KEY. It should be a number.")
    exit(1)

with Client(name="USS", api_id=API_KEY, api_hash=API_HASH, in_memory=True) as app:
    session_string = app.export_session_string()
    print(f"Your session string is:\n{session_string}")
