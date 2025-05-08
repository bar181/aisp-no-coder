from app.db import client
print("Seeding example rows…")
client().table("vehicle").insert({"id": 1, "name": "SeederTruck"}).execute()
print("✓ done")