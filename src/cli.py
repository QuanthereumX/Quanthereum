# cli.py - Command Line Interface for QuanthereumX
# Author: Przemek Buczek

import argparse
from services import fetch_data, process_data
from auth import generate_token, verify_token
import sys

def main():
    parser = argparse.ArgumentParser(description="QuanthereumX CLI - Manage your system from terminal")

    parser.add_argument("--users", action="store_true", help="Fetch all users from database")
    parser.add_argument("--token", type=int, help="Generate a JWT token for a user with given ID")
    parser.add_argument("--verify", type=str, help="Verify a given JWT token")

    args = parser.parse_args()

    if args.users:
        print("🔍 Fetching users...")
        data = fetch_data("SELECT * FROM users;")
        if data:
            processed = process_data(data)
            print("👥 Users:", processed)
        else:
            print("❌ No users found.")

    elif args.token:
        print(f"🔑 Generating token for user ID {args.token}...")
        token = generate_token(user_id=args.token)
        print("🎫 JWT Token:", token)

    elif args.verify:
        print("🔍 Verifying token...")
        result = verify_token(args.verify)
        if result:
            print("✅ Token is valid:", result)
        else:
            print("❌ Invalid or expired token.")

    else:
        print("❌ No valid command provided. Use --help for available options.")

if __name__ == "__main__":
    main()
