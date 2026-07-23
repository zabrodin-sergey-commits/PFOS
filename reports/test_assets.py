from database.assets import (
    get_assets,
    total_assets
)



print("="*50)
print("PFOS ASSETS")
print("="*50)



for asset in get_assets():

    print(asset)



print()

print(
    "TOTAL:",
    total_assets(),
    "RUB"
)