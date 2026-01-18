import asyncio
import os, sys
import sys

from dotenv import load_dotenv
from csfloat_api.csfloat_client import Client


if getattr(sys, 'frozen', False):
    # is running as exe
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # if running as script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(BASE_DIR)


load_dotenv()

api_key = os.getenv("CSFLOAT_KEY")
description = os.getenv("DESCRIPTION")

#Verifying if .env exists, if not creating a new one with key and description
if not api_key:
    api_key = input("CSFLOAT_API_KEY: ").strip()
    description = input("DESCRIPTION: ").strip()
    with open(".env", "w") as f:
        f.write(f"CSFLOAT_KEY={api_key}\n")
        f.write(f"DESCRIPTION={description}\n")





async def retry_async(func, *args, retries=3, delay=0.5, **kwargs):
    for attempt in range(1, retries + 1):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] {func.__name__} failed (attempt {attempt}/{retries}): {e}")
            if attempt < retries:
                await asyncio.sleep(delay)
            else:
                raise

async def relist_items(client, listing, description):
    print(f"--> Relisting: {listing.item.item_name}")

    # 1. Deleting with retry
    await retry_async(
        client.delete_listing,
        listing_id=int(listing.id),
        retries=5,
        delay=1
    )
    print(f"Deleted listing {listing.item.item_name}")

    await asyncio.sleep(0.2)

    # 2. Creting with retry
    await retry_async(
        client.create_listing,
        asset_id=listing.item.asset_id,
        price=listing.price,
        description=description,
        retries=5,
        delay=1
    )
    print(f"Recreated listing for asset {listing.item.asset_id}")



async def main():
    async with Client(api_key=api_key) as client:
        me = await client.get_me()
        x = me.user
        #print(x.steam_id)

        stall_listings = await client.get_stall(x.steam_id)
        #print(listings)

        for listing in stall_listings.listings:
            try:
                await relist_items(client,listing,description)
            except Exception as e:
                print(f"[FATAL] Listing {listing.id} could not be restored: {e}")


asyncio.run(main())