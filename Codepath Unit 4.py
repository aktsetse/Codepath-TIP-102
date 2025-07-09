# def extract_nft_names(nft_collection):
#     nft_names = []
#     for nft in nft_collection:
#         nft_names += nft["name"]
#     return nft_names


# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
# ]

# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# nft_collection_3 = []

# print(extract_nft_names(nft_collection))
# print(extract_nft_names(nft_collection_2))
# print(extract_nft_names(nft_collection_3))

def identify_popular_creators(nft_collection):
    nft_creator = {}
    for nft in nft_collection:
       creator = nft["creator"]
       if creator in nft_creator:
           nft_creator[creator] += 1 
       else:
            nft_creator[creator] = 1
    
    popular_creators = []
    for creator, count in nft_creator.items():
        if count > 1:
            popular_creators.append(creator)

    return popular_creators

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))