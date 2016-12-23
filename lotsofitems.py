from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalog_database import User, Categories, Items, Base

engine = create_engine('sqlite:///catalogproject.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#create user
User1 = User(name = "Chuck Norris", email = "ChuckNorris@whitehouse.gov", picture = "http://nymag.com/images/2/daily/entertainment/07/05/18_chucknorris_lgl.jpg")
session.add(User1)
session.commit()


categories = {"Electronics","Auto & Tires", "Sports, Fitness & Outdoors", "Movies & Music", "Books",
            "Toys & Games", "Office Suppliers", "Clothing"}




category_items1 = ["Nikon Digital Camera", "Nikon D3300 Digital SLR Camera & 18-55mm VR DX II AF-S Lens (Black) ",
"https://us-i5.tb.wal.co/asr/a1e2e13e-a876-4286-9771-d0f5073506c1_1.e0d19ab7236856bd30674c8379e59d72.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$374.00", "Electronics"]


category_items2 = ["Samsung smart TV", 'SAMSUNG 50" 5200 Series- Full HD Smart LED TV - 1080p 60MR',
"https://us-i5.tb.wal.co/asr/5584c003-5487-4e40-9eac-d82a3529720a_1.25c7bd72115b71ce00c670dcb1ba4134.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$477.00", "Electronics"]


category_items3 = ["Android cellphone", 'AT&T Alcatel Onetouch Allura Prepaid GoPhone',
"https://us-i5.tb.wal.co/asr/d939497c-99bb-4520-a18c-adb253fe0378_1.7570b0d181e169cfb9ee7d0cbab2038f.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$89.00", "Electronics"]

category_items4 = ["Google Chromecast", 'Chromecast is a media streaming device that plugs into the HDMI port on your TV',
"https://us-i5.tb.wal.co/asr/8289d1b0-b630-46bc-a33e-f0e5b347ff70_1.c6e10cbefa0cd58296f32c2f54e0e45f.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$35.00", "Electronics"]

category_items5 = ["Bushnell PowerView Binoculars", 'Bushnell PowerView 10 x 50mm Porro Prism Instafocus Binoculars, Realtree AP. Instafocus binoculars with 10x magnification and 50mm objective lenses',
"https://static.bhphoto.com/images/images500x500/bushnell_131055_10x50_porro_prism_1358444718000_911024.jpg",
"$62.57", "Electronics"]


category_items6 = ["Duracell Ultra Battery", "2009 Chrysler PT Cruiser L4 2.4L 510CCA Car and Truck battery",
"https://www.batteriesplus.com/content/images/product/large/33832.jpg",
"$107.99", "Auto & Tires"]

category_items7 = ["Carpet Floor Mats", "Genuine Toyota floor mat designed to protect the floor of a vehicle from dirt, wear and salt corrosion.",
"https://s3.amazonaws.com/rp-part-images/assets/9d069868a60c04f4e4fc3c5357ea9199.gif",
"$59.99", "Auto & Tires"]

category_items8 = ["Motor Oil", "Valvoline SynPower Full Synthetic 5W-30 Motor Oil, 5 Quarts. Provides superior engine cleanliness through sludge and varnish protection",
"https://us-i5.tb.wal.co/asr/7d3b2f64-2b45-48a1-97d8-ec0464f00441_3.5babe0506c10e2aa4964bca006190f4d.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$22.47", "Auto & Tires"]

category_items9 = ["Goodyear Wrangler Tire", "The Goodyear Wrangler Radial Tire (P235/75R15 105S) is designed for drivers of light and pickup trucks who are looking for performance and style.",
"https://us-i5.tb.wal.co/asr/fa4023f5-f869-4484-8227-1fecfc214f9d_1.9b592886eb1f73e2f83b267f359efa2f.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$82.00", "Auto & Tires"]


category_items10 = ["Wilson NFL Football", "The Wilson NFL Super Grip Football is made of composite leather. It makes for a thoughtful gift for up-and-coming young prospects or savvy backyard veterans",
"https://us-i5.tb.wal.co/asr/712d585e-603c-4537-8683-d43aa9e36f68_1.1f1c1e42daeabf4a98831c0b8a28c80f.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$14.97", "Sports, Fitness & Outdoors"]

category_items11 = ["Callaway Men's Golf Club set", "The Strata 16-Piece Men's Golf Club Set is designed for maximum performance right out of the box",
"https://us-i5.tb.wal.co/asr/72f4a62a-2443-4cb9-82dc-c0f55b37dcb0_1.07387d47c50ab33b4ba1d985a340a1c5.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$315.99", "Sports, Fitness & Outdoors"]


category_items12 = ["Dumbell", "CAP's Rubber Hex Dumbbells are premium club-quality weights that are built to last. Comes in sets of 2",
"https://us-i5.tb.wal.co/asr/d617c0b6-3e96-4112-ba76-d94fc5abd803_1.b78d4356163bff13db381694022c1e25.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$29.99", "Sports, Fitness & Outdoors"]


category_items13 = ["Archery bow", 'Samick Sage Takedown Recurve Bow. The 62" AMO length allows for stable, smooth shooting for almost any draw length',
"http://www.3riversarchery.com/mm5/graphics/00000001/2490x_130x500.jpg",
"$139.99", "Sports, Fitness & Outdoors"]


category_items14 = ["Avatar", "Avatar, the story of an ex-Marine who finds himself thrust into hostilities on an alien planet filled with exotic life forms",
"http://www.astronomytrek.com/wp-content/uploads/2014/04/avatar-oridginal1.jpg",
"$12.99", "Movies & Music"]

category_items15 = ["The Dark Knight", "The Dark Knight reunites Christian Bale with director Christopher Nolan and takes Batman across the world in his quest to fight a growing criminal threat known as The Joker ",
"http://www.movieash.in/wp-content/uploads/2015/12/The-Dark-Knight-Full-Movie-Download-HD-Free.jpg",
"$9.99", "Movies & Music"]


category_items16 = ["NO MAN'S LAND", "Special Agent John Puller, combat veteran and the army's most tenacious investigator, is back in this action-packed thriller from worldwide #1 bestselling author David Baldacci.",
"https://books.google.com/books/content/images/frontcover/z7MsDAAAQBAJ?fife=w300-rw",
"$9.99", "Books"]

category_items17 = ["GILLIAN FLYNN GONE GIRL", "In Carthage, Mo., former New York-based writer Nick Dunne (Ben Affleck) and his glamorous wife Amy (Rosamund Pike) present a portrait of a blissful marriage to the public. However, when Amy goes missing on the couple's fifth wedding anniversary, Nick becomes the prime suspect in her disappearance",
"https://books.google.com/books/content/images/frontcover/L25K1tY5WyoC?fife=w300-rw",
"$8.99", "Books"]


category_items18 = ["Alexander Hamilton", "With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent",
"https://books.google.com/books/content/images/frontcover/L25K1tY5WyoC?fife=w300-rw",
"$8.99", "Books"]


category_items19 = ["Grant Theft Auto", "Grand Theft Auto V is an open world action-adventure video game developed by Rockstar North and published by Rockstar Games. It was released on 17 September 2013 for the PlayStation 3 and Xbox 360, on 18 November 2014 for the PlayStation 4 and Xbox One, and on 14 April 2015 for Microsoft Windows",
"http://media.rockstargames.com/rockstargames/img/global/news/upload/actual_1364906194.jpg",
"$40.99", "Toys & Games"]

category_items20 = ["Call of Duty 4: Modern Warfare", "Call of Duty 4: Modern Warfare is a 2007 first-person shooter video game developed by Infinity Ward and published by Activision for Microsoft Windows, OS X, PlayStation 3, Xbox 360, and Wii. A handheld game was made for the Nintendo DS",
"http://www.mobygames.com/images/covers/l/97335-call-of-duty-4-modern-warfare-windows-front-cover.jpg",
"$39.99", "Toys & Games"]


category_items21 = ["Pokemon Sun and Moon", "Pokemon Sun and Pokemon Moon are role-playing video games developed by Game Freak and published by Nintendo for the Nintendo 3DS. They are the first installments in the seventh generation of Pokemon games",
"http://im.ziffdavisinternational.com/ign_pl/screenshot/default/b47656ed7e409e8da4100557a24a9ae67e63f774c63b9736870c38cefd81_he2t.png",
"$39.99", "Toys & Games"]


category_items22 = ["EA SPORTS FIFA 17", "Innovates across the entire pitch to deliver a balanced, authentic, and exciting football experience that lets you play your way, and compete at a higher level. And with all new ways to play! ",
"https://us-i5.tb.wal.co/asr/651e5cba-fef0-4283-bd07-d904760234f1_1.d37acaa206a017241016840f6e76c64d.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$51.38", "Toys & Games"]


category_items23 = ["Super Mario Galaxy 2", "Super Mario Galaxy 2 is a platforming video game developed and published by Nintendo for the Wii. It was first announced at E3 2009 and is the sequel to Super Mario Galaxy.",
"http://firsthour.net/screenshots/super-mario-galaxy-2/super-mario-galaxy-2-cover.jpg",
"$19.99", "Toys & Games"]


category_items24 = ["The Last of Us Remastered", "The Last of Us Remastered is an action-adventure survival horror video game developed by Naughty Dog and published by Sony Computer Entertainment",
"http://3.bp.blogspot.com/-iIWPA0ZIpfQ/VTEUqIj_AEI/AAAAAAAABhQ/J55WGpa75So/s1600/the-last-of-us-remastered-ps4-3d.png",
"$19.99", "Toys & Games"]


category_items25 = ["EA SPORTS MADDEN 17", "Madden NFL 17 is an American football sports video game based on the National Football League and published by EA Sports for the PlayStation 4, PlayStation 3, Xbox One and Xbox 360",
"https://i5.walmartimages.com/asr/8c1a930d-03ab-4541-9619-69840ffb6024_1.9c5c500ca6b12efbc4341a07da8d26f2.jpeg",
"$49.99", "Toys & Games"]


category_items26 = ["Texas Instruments TI-84 Plus Calculator", "TI-84 Plus is a graphing calculator with 8 display lines, displaying 16 characters, included USB computer cable, fully compatible with TI-83 Plus",
"https://us-i5.tb.wal.co/asr/4b2eea27-548c-4f1c-847c-b5043a5711b4_1.eea649dd8a9c254c7251657d0d0747e1.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$115.00", "Office Suppliers"]


category_items27 = ["Canon Printer", "Canon MF212w Mono MFP Wireless Laser Multifunctional Printer/Copier/Scanner",
"https://us-i5.tb.wal.co/asr/7e572bbb-098d-4d17-b754-fb813addab09_1.2fdcb678fe61d884d68c83b028ec6dcf.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$213.75", "Office Suppliers"]


category_items28 = ["Duracell Batteries", "Duracell Coppertop AA Household Batteries, 24 Count",
"https://us-i5.tb.wal.co/asr/5c8741cd-9551-4c5f-9f77-7f0b90f400a7_1.91805e3d8e9639bc62bc3a2edd5405d0.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$13.97", "Office Suppliers"]


category_items29 = ["Flash Drive", "SanDisk CZ60 64GB USB 2.0 Flash Drive",
"https://us-i5.tb.wal.co/asr/e7d53e4f-4e7f-44ee-80a9-42801614a6c7_1.8d3e563bd64f84ea78eca6bd3c85024f.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$19.95", "Office Suppliers"]



category_items30 = ["Women's Jeans", "Signature by Levi & Co. Women's curvy BOOT Cut Jeans",
"https://us-i5.tb.wal.co/asr/cf049fd5-0498-4b38-940c-81269e316cad_1.705201ad16fad4de073d8555574ff2b6.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$19.94", "Clothing"]

category_items31 = ["Athletic Shoe", "Men's Belmar Athletic Shoe",
"https://us-i5.tb.wal.co/asr/766f6e74-95d6-4889-a5d8-f4f0e8cbf138_1.2ec53fa910b6266127439b8d23c4136f.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$10.00", "Clothing"]


category_items32 = ["Toddler Dress", "Healthtex Baby Toddler Girl Short Sleeve 2-Fer Dress",
"https://us-i5.tb.wal.co/asr/5501ae34-e181-4c26-b2c8-f56879e4fb0e_1.a1b07cf68c8a8924031829a66b8739b0.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$5.97", "Clothing"]


category_items33 = ["Socks", "Fruit of the Loom Mens No Show Socks 6 Pack",
"https://us-i5.tb.wal.co/asr/aef3ff89-7d92-485c-98a1-1b9eca4386bc_1.a2dcf09817f738310908b8993d7f3f0b.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$6.97", "Clothing"]


category_items34 = ["Suit Jacket", "George - Big Men's Suit Jacket",
"https://us-i5.tb.wal.co/asr/f42a02a3-dcb5-41dc-9823-1f20c96d74ba_1.4fbd2ce318d01b2b5167a1e0d6b1211e.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$47.00", "Clothing"]


category_items35 = ["Shirt", "George - Men's Long-Sleeve Oxford Shirt",
"https://us-i5.tb.wal.co/asr/a21519b9-2f21-4ab8-8e4e-8a9bcda2ceb8_1.32c07c362c76ee509bdccf472fc2f379.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
"$13.98", "Clothing"]


category_list = []


# Function to add individual category-items
def add_item(item):
    category_list.append(item)


# Function to add multiple category-items
def add_multiItems(*items):
    for item in items:
        category_list.append(item)

# Function to remove individual category-items
def remove_item(item):
    if item in category_list:
        category_list.remove(item)
    else:
        print item + " not in the category_list"


add_multiItems(category_items1, category_items2, category_items3, category_items4, category_items5,
    category_items6, category_items7, category_items8, category_items9, category_items10, category_items11,
    category_items12, category_items13, category_items14, category_items15, category_items16,
    category_items17, category_items18, category_items19, category_items20, category_items21,
    category_items22, category_items23, category_items24, category_items25, category_items26,
    category_items27, category_items28, category_items29, category_items30, category_items31,
    category_items32, category_items33, category_items34, category_items35)



# Add and commit all the categories and items.
for category in categories:
    cat = Categories(user_id = 1, name=category)
    session.add(cat)
    session.commit()
    for i in category_list:
        if category == i[4]:
            item = Items(user_id = 1,
                         name=i[0],
                         description=i[1],
                         picture = i[2],
                         price=i[3],
                         category=cat)
            session.add(item)
            session.commit()





print "added category & items!!!"
