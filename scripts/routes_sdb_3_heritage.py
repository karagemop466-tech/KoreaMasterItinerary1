#!/usr/bin/env python3
"""Route Blueprint: Seoul · Daejeon · Busan (Joseon Dynasty, Hanok Living & Fine Arts)."""

from scripts.generate_all_itineraries import make_day
from scripts.itinerary_builder_sdb import (
    get_sdb_common_bases,
    get_sdb_common_transfers,
    get_sdb_budget_scenarios,
    get_sdb_booking_priorities
)

def get_sdb_heritage():
    days = [
        # Day 1: Nov 1
        make_day(0, "Seoul", "Arrival", "Seoul · Myeongdong / Seoul Station edge",
            "ICN arrival at 21:00 → late transfer → peaceful hotel check-in → restorative rest",
            "Serene Landing & Heritage Haven Check-in",
            [
                {"time": "21:00–22:15", "title": "ICN Arrival & Welcome", "detail": "Clear immigration and collect luggage; pick up pre-arranged transportation cards.", "logistics": "Terminal 1 or 2."},
                {"time": "22:30–23:45", "title": "Direct Transfer to Central Seoul Heritage Base", "detail": "Direct Airport Limousine Bus or official taxi to Myeongdong / Seoul Station hotel.", "logistics": "Comfortable door-to-door transfer."},
                {"time": "23:45–00:30", "title": "Hotel Check-in & Peaceful Rest", "detail": "Settle into hotel room with warm herbal tea; rest deeply before Joseon palace exploration.", "logistics": "Notify hotel of late arrival."}
            ],
            [
                {"label": "Gentle Start", "text": "Preserve energy for extensive walking through historic palace courtyards and stone pathways."},
                {"label": "Historic Base", "text": "Base provides effortless walking access to Deoksugung and Royal Palaces."}
            ],
            "Light herbal tea and convenience store snack near hotel.",
            "Confirm late check-in with hotel in writing.",
            "Limousine Bus ~₩17,000.",
            "Get deep sleep to prepare for morning palace ceremonies.",
            "Hotel front desk provides 24-hour assistance."
        ),
        # Day 2: Nov 2
        make_day(1, "Seoul", "Imperial Joseon & Hanok Arts", "Seoul · Myeongdong / Seoul Station edge",
            "Gyeongbokgung Palace Guard Changing → National Palace Museum → Bukchon Hanok Craft Workshops",
            "Royal Court Architecture & Traditional Hanok Living",
            [
                {"time": "09:30–11:30", "title": "Gyeongbokgung Royal Palace & Guard Ceremony", "detail": "Observe the colorful Royal Guard Changing Ceremony at Gwanghwamun Gate (10:00 AM) and study the intricate dancheong woodwork of Geunjeongjeon throne hall and Hyangwonjeong island pavilion.", "logistics": "Gyeongbokgung Station Line 3 Exit 5."},
                {"time": "11:45–13:00", "title": "National Palace Museum of Korea", "detail": "Examine royal Joseon seals, astronomical water clocks (Jagyeongnu), court attire, and imperial palanquins.", "logistics": "Located directly inside palace south gate (free admission)."},
                {"time": "13:15–14:30", "title": "Samcheong-dong Royal Court Lunch", "detail": "Enjoy refined dolsot bibimbap or handmade dumplings in a quiet Samcheong-dong courtyard.", "logistics": "Short walk east of palace."},
                {"time": "14:45–17:00", "title": "Bukchon Hanok Village & Traditional Craft Centers", "detail": "Explore centuries-old wooden hanok architecture and visit artisanal workshops for Korean knotting (maedeup) and mother-of-pearl lacquerware (najeonchilgi).", "logistics": "Anguk Station Line 3 Exit 2."},
                {"time": "17:30–19:30", "title": "Insadong Antique Gallery & Traditional Teahouse", "detail": "Browse Joseon celadon ceramics, calligraphy brushes, and sip hot omija tea in a 100-year-old wooden hanok teahouse.", "logistics": "Insadong Ssamzigil lane."},
                {"time": "20:00–21:30", "title": "Traditional Hanjeongsik (Korean Full-Course) Dinner", "detail": "Savor a multi-course royal court dinner with braised short ribs, grilled fish, seasoned mountain herbs, and steamed rice.", "logistics": "Insadong / Jongno dining hall."}
            ],
            [
                {"label": "Royal Court Immersion", "text": "Combines primary Joseon seat of power with living royal museum artifacts and artisan workshops."},
                {"label": "Preserved Aesthetics", "text": "Bukchon and Insadong showcase traditional Korean architectural balance with nature (Pungsu-jiri)."}
            ],
            "Lunch: Samcheong-dong handmade dumplings and bibimbap. Afternoon: Traditional pine needle tea and yakgwa. Dinner: Insadong Royal Hanjeongsik multi-course banquet.",
            "Palace admission ₩3,000 (free if wearing traditional hanbok).",
            "Palace entry ₩3,000; Hanjeongsik dinner ~₩38,000 per person.",
            "Bukchon is a quiet residential area; speak in low tones and observe residential privacy.",
            "National Palace Museum is fully indoor and climate-controlled."
        ),
        # Day 3: Nov 3
        make_day(2, "Seoul", "UNESCO Sanctuaries & Ancestral Rites", "Seoul · Myeongdong / Seoul Station edge",
            "Changdeokgung Secret Garden (UNESCO) → Jongmyo Royal Ancestral Shrine → Ikseon Hanok Alleys",
            "Sacred Royal Groves & Ancestral Ceremonial Shrines",
            [
                {"time": "09:30–12:00", "title": "Changdeokgung Palace & Secret Garden (Huwon)", "detail": "Tour the UNESCO World Heritage palace, designed in complete harmony with surrounding natural topography, and walk the private royal autumn garden.", "logistics": "Anguk Station Line 3 Exit 3."},
                {"time": "12:15–13:30", "title": "Ikseon-dong Hanok Brunch", "detail": "Dine on handmade pasta or Korean rice sets in a restored 1920s hanok courtyard.", "logistics": "Jongno 3-ga Station Exit 4."},
                {"time": "14:00–16:00", "title": "Jongmyo Royal Ancestral Shrine (UNESCO)", "detail": "Walk the world's longest wooden structure (Jeongjeon), dedicated to memorial services for Joseon kings and queens and home to the 600-year-old Jongmyo Jeryeak ritual music tradition.", "logistics": "Jongno 3-ga Station Exit 11."},
                {"time": "16:30–18:30", "title": "Changgyeonggung Palace & Grand Greenhouse", "detail": "Stroll the picturesque autumn gardens and Korea's first Western-style royal greenhouse built in 1909.", "logistics": "Walk north from Jongmyo."},
                {"time": "19:00–21:00", "title": "Jongno Traditional Braised Beef (Galbijjim) Dinner", "detail": "Savor slow-braised beef short ribs tenderly cooked in sweet soy sauce with chestnuts, gingko nuts, and carrots.", "logistics": "Jongno 3-ga dining quarter."}
            ],
            [
                {"label": "Double UNESCO Heritage", "text": "Changdeokgung and Jongmyo represent the spiritual and architectural zenith of the Joseon Dynasty."},
                {"label": "Autumn Forest Foliage", "text": "The Secret Garden and Changgyeonggung forest offer some of Seoul's most breathtaking autumn maple colors."}
            ],
            "Lunch: Ikseon-dong hanok courtyard dining. Dinner: Jongno slow-cooked Hanwoo Galbijjim (braised beef short ribs) with warm rice.",
            "Book Changdeokgung Secret Garden timed tour online 6 days in advance at 10:00 AM KST.",
            "Changdeokgung + Huwon ₩8,000; Jongmyo ₩1,000; Changgyeonggung ₩1,000.",
            "Jongmyo stone pathways (Sindo) are sacred for ancestral spirits; walk on side stones rather than center.",
            "Palace exhibition halls and greenhouse provide shelter."
        ),
        # Day 4: Nov 4
        make_day(3, "Seoul", "Modern Aesthetics & Stonewall Walk", "Seoul · Myeongdong / Seoul Station edge",
            "MMCA Seoul (Contemporary Art) → Deoksugung Palace & Stonewall Walkway → Jeongdong Heritage",
            "Fine Contemporary Visions & Romantic Stonewall Alleys",
            [
                {"time": "09:30–12:30", "title": "MMCA Seoul (National Museum of Modern & Contemporary Art)", "detail": "Explore groundbreaking exhibitions of contemporary Korean artists, monumental sculpture installations, and the historic Jongchinbu royal genealogy office on museum grounds.", "logistics": "Anguk Station Line 3 Exit 1."},
                {"time": "12:45–14:00", "title": "Samcheong-dong Fine Dining Lunch", "detail": "Enjoy refined seasonal Korean dining or garden cafe lunch.", "logistics": "Directly opposite MMCA."},
                {"time": "14:30–16:30", "title": "Deoksugung Palace & MMCA Deoksugung Branch", "detail": "Tour the unique palace blending Joseon wooden pavilions with neoclassical Western stone architecture (Seokjojeon).", "logistics": "City Hall Station Line 1/2 Exit 2."},
                {"time": "16:45–18:30", "title": "Deoksugung Stonewall Walkway & Jeongdong Heritage Trail", "detail": "Walk Korea's most romantic tree-lined stonewall road, viewing historic 19th-century diplomatic legations, and take the elevator up to Jeongdong Observatory for sunset views.", "logistics": "Deoksugung stonewall path."},
                {"time": "19:00–21:00", "title": "Gwanghwamun Hanwoo Bulgogi Dinner", "detail": "Enjoy seasoned Korean beef bulgogi with glass noodles and organic mushrooms in a quiet private dining room.", "logistics": "Gwanghwamun dining area."}
            ],
            [
                {"label": "Art & History Synergy", "text": "Connects Korea's foremost contemporary museum (MMCA Seoul) with 20th-century modernization history at Deoksugung."},
                {"label": "Romantic Urban Walk", "text": "Deoksugung Stonewall Walkway is draped in golden autumn ginkgo leaves throughout November."}
            ],
            "Lunch: Samcheong-dong artisan Korean dining. Afternoon: Jeongdong Observatory Darak cafe. Dinner: Gwanghwamun Hanwoo beef bulgogi hot pot.",
            "MMCA Seoul admission ₩5,000; Deoksugung Palace ₩1,000; Jeongdong Observatory is free.",
            "Museums ~₩6,000; Dinner ~₩32,000 per person.",
            "MMCA Seoul and MMCA Deoksugung have separate ticket desks; verify current special exhibitions.",
            "MMCA and Seokjojeon are fully indoor fine art facilities."
        ),
        # Day 5: Nov 5
        make_day(4, "Seoul", "National Treasures & Contemplation", "Seoul · Myeongdong / Seoul Station edge",
            "National Museum of Korea → Room of Quiet Contemplation → Yongsan Park",
            "Masterpiece Treasures & 5,000 Years of Artifacts",
            [
                {"time": "09:30–13:00", "title": "National Museum of Korea (Permanent Masterpieces)", "detail": "Contemplate the two National Treasure Pensive Bodhisattva statues in the award-winning Room of Quiet Contemplation; marvel at the Ten-Story Gyeongcheonsa Pagoda, Silla golden crowns, and Goryeo celadon masterpieces.", "logistics": "Ichon Station Line 4 direct underground museum walkway."},
                {"time": "13:15–14:30", "title": "Museum Mirror Pond Restaurant Lunch", "detail": "Dine overlooking the traditional pavilion and scenic reflection pond.", "logistics": "Museum 1F dining hall."},
                {"time": "14:45–16:30", "title": "National Hangeul Museum", "detail": "Explore the scientific genius and cultural evolution of King Sejong's Korean alphabet (Hangeul) created in 1443.", "logistics": "Located adjacent to National Museum (free admission)."},
                {"time": "17:00–19:00", "title": "Yongsan Family Park Autumn Stroll", "detail": "Relax along scenic tree-lined walking tracks and tranquil lotus ponds.", "logistics": "Directly connected to museum grounds."},
                {"time": "19:30–21:30", "title": "Samgakji Charcoal Hanwoo Ribs (Chadolbagi) Dinner", "detail": "Enjoy thinly sliced beef brisket and aged kimchi stew at historic Bongsan-jip.", "logistics": "Samgakji Station Line 4/6 Exit 13."}
            ],
            [
                {"label": "Philosophical Wonder", "text": "The Room of Quiet Contemplation offers one of the world's most serene and transcendent museum spaces."},
                {"label": "Hangeul Innovation", "text": "The Hangeul Museum illustrates how Korea's written language was designed for democratic literacy."}
            ],
            "Lunch: National Museum Mirror Pond Korean set. Dinner: Samgakji Bongsan-jip Hanwoo beef brisket (chadolbagi) with spicy fermented cabbage stew.",
            "National Museum of Korea permanent galleries are free admission.",
            "Museum entry is free; Dinner ~₩35,000 per person.",
            "Photography inside Room of Quiet Contemplation is permitted without flash; maintain silence.",
            "National Museum of Korea is vast, heated, and completely indoor."
        ),
        # Day 6: Nov 6
        make_day(5, "Seoul", "Fine Art Masterpieces & Antiques", "Seoul · Myeongdong / Seoul Station edge",
            "Leeum Museum of Art → Itaewon Antique Furniture Street → Namsan Scenic Overlook",
            "Celadon Antiquities, World Fine Masters & Antique Alleys",
            [
                {"time": "10:00–13:00", "title": "Leeum Museum of Art (Traditional & Modern)", "detail": "Admire museum architecture designed by Mario Botta, Jean Nouvel, and Rem Koolhaas; marvel at Korea's finest private collection of Joseon white porcelain, Goryeo celadon, and international modern masterworks (Rothko, Warhol, Giacometti).", "logistics": "Hangangjin Station Line 6 Exit 1."},
                {"time": "13:15–14:45", "title": "Hannam-dong Gourmet Lunch", "detail": "Dine in chic Hannam-dong on artisan French dining, gourmet pasta, or modern Korean cuisine.", "logistics": "Hannam cafe street."},
                {"time": "15:00–17:00", "title": "Itaewon Antique Furniture Street", "detail": "Browse European and Asian antique furniture, vintage clocks, and decorative art curations across 100+ boutique shops.", "logistics": "Itaewon Station Line 6 Exit 3/4."},
                {"time": "17:30–19:30", "title": "Namsan Outdoor Sculpture Park & Sunset", "detail": "Walk through pine-scented sculpture gardens overlooking central Seoul.", "logistics": "Namsan park trail."},
                {"time": "20:00–21:30", "title": "Traditional Ginseng Chicken Soup (Samgyetang) Dinner", "detail": "Warm up with whole young chicken stuffed with sticky rice, ginseng root, garlic, and jujubes simmered in rich herbal broth at Tosokchon.", "logistics": "Tosokchon Samgyetang (Gyeongbokgung Station)."}
            ],
            [
                {"label": "Private Art Pinnacle", "text": "Leeum Museum offers Korea's most prestigious private art collection and stunning rotunda architecture."},
                {"label": "Restorative Herbal Cuisine", "text": "Samgyetang restores warmth and vitality after a day of aesthetic discovery."}
            ],
            "Lunch: Hannam-dong artisanal Italian or modern Korean bistro. Dinner: Tosokchon Samgyetang (historic ginseng chicken soup).",
            "Book Leeum Museum of Art tickets online 14 days in advance (free permanent collection, timed entry).",
            "Leeum Museum free permanent entry; Samgyetang dinner ~₩20,000 per person.",
            "Leeum audio guide is available in English (highly recommended, powered by smartphone device).",
            "Leeum Museum is fully indoor with world-class climate control."
        ),
        # Day 7: Nov 7
        make_day(6, "Seoul", "Fortress Walls & Historic Alleys", "Seoul · Myeongdong / Seoul Station edge",
            "Seoul City Wall (Hanyangdoseong) Naksan Trail → Dongmyo Flea Market → KTX Prep",
            "Ancient Stone Ramparts & Vintage Artifact Markets",
            [
                {"time": "09:30–12:30", "title": "Seoul City Wall (Hanyangdoseong) Naksan Trail", "detail": "Hike along 600-year-old stone fortress walls built in 1396 from Hyehwamun Gate to Naksan peak and down to Dongdaemun (Heunginjimun Gate), enjoying panoramic city views.", "logistics": "Hanseong Univ. Station Line 4 Exit 4 to Dongdaemun Station Line 1/4."},
                {"time": "12:45–14:00", "title": "Dongdaemun Traditional Noodle Lunch", "detail": "Enjoy warm handmade kalguksu or dumpling soup near the historic East Gate.", "logistics": "Dongdaemun Market area."},
                {"time": "14:15–16:30", "title": "Dongmyo Vintage Flea Market & Seoul Folk Flea Market", "detail": "Browse thousands of vintage artifacts, retro electronics, traditional ceramics, vinyl records, and historic trinkets.", "logistics": "Dongmyo Station Line 1/6 Exit 3."},
                {"time": "17:00–18:30", "title": "Seoul Station Packing & Train Verification", "detail": "Return to Seoul hotel base, organize bags for Sunday morning KTX to Daejeon, and verify seat reservations.", "logistics": "Seoul Station hotel."},
                {"time": "19:00–21:00", "title": "Myeongdong Traditional Dumpling & Hot Pot Feast", "detail": "Enjoy steaming mandu hot pot (mandu jeongol) in central Seoul.", "logistics": "Myeongdong dining lane."}
            ],
            [
                {"label": "Fortress Wall Heritage", "text": "Hanyangdoseong is the world's longest continuously surviving stone city wall (18.6km total)."},
                {"label": "Vintage Discovery", "text": "Dongmyo offers authentic retro treasure hunting and fascinating everyday historical objects."}
            ],
            "Lunch: Dongdaemun market handmade dumpling soup. Dinner: Myeongdong steaming mandu jeongol (dumpling hot pot) with beef broth.",
            "City wall trail is open 24/7; admission is free.",
            "Free wall trail and market; Dinner ~₩22,000 per person.",
            "Wear sturdy walking shoes for stone steps along the fortress wall trail.",
            "Dongdaemun Design Plaza and indoor markets provide shelter if raining."
        ),
        # Day 8: Nov 8
        make_day(7, "Daejeon", "City Transition & Scholar Estates", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Morning KTX to Daejeon → Dongchundang Historic Scholar House → Daejeon Modern History Museum",
            "High-Speed Rail into Central Joseon Scholar Landscapes",
            [
                {"time": "09:30–10:30", "title": "KTX High-Speed Rail Seoul to Daejeon", "detail": "55-minute comfortable high-speed journey from Seoul Station to Daejeon Station.", "logistics": "Direct Gyeongbu line."},
                {"time": "11:00–13:00", "title": "Dongchundang Historic Joseon House & Park", "detail": "Tour the designated National Treasure #209 wooden residence and scholar pavilion of Song Jun-gil, representing understated Joseon Confucian residential elegance.", "logistics": "Daedeok-gu Songchon-dong; short bus/taxi from station."},
                {"time": "13:15–14:30", "title": "Daedeok Traditional Hanjeongsik Lunch", "detail": "Savor seasonal side dishes, grilled fish, and stone-pot rice.", "logistics": "Songchon-dong restaurant area."},
                {"time": "15:00–16:30", "title": "Daejeon Modern History Museum (Former Chungnam Provincial Office)", "detail": "Explore the striking 1932 early-modern brick architectural landmark, featured in historical cinema, detailing Daejeon's transition from railway crossroads to metropolitan hub.", "logistics": "Jungangno Station Line 1 Exit 4."},
                {"time": "17:00–18:30", "title": "Hotel Check-in in Yuseong / Dunsan & Hot Spring Walk", "detail": "Check into Daejeon hotel base and take a gentle stroll through Yuseong Hot Springs park.", "logistics": "Metro Line 1."},
                {"time": "19:00–21:00", "title": "Daejeon Traditional Bulgogi & Mountain Herbs Dinner", "detail": "Enjoy slow-marinated beef bulgogi with fresh wild mountain herbs and doenjang stew.", "logistics": "Yuseong dining quarter."}
            ],
            [
                {"label": "Scholar Architecture", "text": "Dongchundang embodies the austere beauty and proportion of Joseon neo-Confucian thought."},
                {"label": "Modernist Preservation", "text": "The former Provincial Office is one of Korea's finest preserved 1930s architectural treasures."}
            ],
            "Lunch: Daedeok traditional stone-pot rice with seasoned mountain roots and grilled croaker. Dinner: Yuseong marinated Hanwoo beef bulgogi with perilla salad.",
            "Book KTX Seoul→Daejeon 30 days prior on Korail app.",
            "KTX ticket ~₩23,700; Dongchundang is free; Modern History Museum is free.",
            "Dongchundang requires removing shoes when stepping onto wooden verandas (maru).",
            "Daejeon Modern History Museum is fully indoor."
        ),
        # Day 9: Nov 9
        make_day(8, "Daejeon", "Modern Art Masters & Calligraphy", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Lee Ungno Museum of Art → Daejeon Museum of Art → Hanbat Botanical Pavilion",
            "Modernist Abstract Calligraphy & Architectural Light",
            [
                {"time": "09:30–12:00", "title": "Lee Ungno Museum of Art", "detail": "Marvel at the abstract calligraphy paintings, tapestries, and woodcuts of master artist Lee Ungno, housed in an architectural marvel of light and white stone designed by French architect Laurent Beaudouin.", "logistics": "Govt Complex Daejeon Station Line 1 or Bus 604."},
                {"time": "12:15–13:30", "title": "Museum Cafe & Gourmet Lunch", "detail": "Enjoy handmade sandwiches or Korean pasta overlooking the museum reflecting pool.", "logistics": "Lee Ungno Museum courtyard."},
                {"time": "13:45–16:00", "title": "Daejeon Museum of Art & Outdoor Sculpture Park", "detail": "Tour permanent contemporary art galleries and outdoor monumental bronze and steel sculptures.", "logistics": "Adjacent to Lee Ungno Museum."},
                {"time": "16:15–18:00", "title": "Hanbat Arboretum Tropical Botanical Glasshouse", "detail": "Stroll the lush indoor tropical greenhouse and golden autumn pine arboretum paths.", "logistics": "Hanbat Arboretum East Garden."},
                {"time": "18:30–21:00", "title": "Daejeon Hand-Cut Clam Kalguksu & Boiled Suyuk Dinner", "detail": "Feast on tender slices of boiled pork belly and rich hand-cut noodle soup.", "logistics": "Dunsan dining street."}
            ],
            [
                {"label": "World-Class Monographic Museum", "text": "Lee Ungno Museum is internationally acclaimed for the seamless dialogue between architecture, natural light, and abstract art."},
                {"label": "Botanical Artistry", "text": "Hanbat Arboretum showcases Korea's finest urban botanical garden design."}
            ],
            "Lunch: Lee Ungno Museum cafe light dining. Dinner: Dunsan handmade clam kalguksu with tender pork suyuk.",
            "Lee Ungno Museum closed on Mondays; entry ₩1,000.",
            "Museum tickets ~₩2,000 total; Arboretum free; Dinner ~₩20,000 per person.",
            "No flash photography inside art exhibition galleries.",
            "Both museums and the tropical greenhouse are completely enclosed and heated."
        ),
        # Day 10: Nov 10
        make_day(9, "Daejeon", "Classical Pavilion Gardens", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Uam Historic Park (Namganjeongsa Pavilion) → Daecheong Dam Cultural Heritage Walk",
            "Classical Joseon Water Pavilions & Scholar Philosophy",
            [
                {"time": "09:30–12:30", "title": "Uam Historic Park & Namganjeongsa Pavilion", "detail": "Explore the tranquil country estate and wooden study hall of renowned Joseon philosopher Song Si-yeol (Uam), built over a natural crystal stream with lotus ponds and centuries-old zelkova trees.", "logistics": "Dong-gu Gayang-dong; City Bus 311 or 20-min taxi."},
                {"time": "12:45–14:15", "title": "Rustic Mountain Village Lunch", "detail": "Taste country-style acorn jelly (dotorimuk) and fresh wild mountain herb bibimbap.", "logistics": "Gayang-dong village restaurant."},
                {"time": "14:45–17:00", "title": "Daecheong Dam Water Culture Center & Heritage Overlook", "detail": "Walk the scenic lakeside trails and visit the cultural exhibition hall explaining the history of the Geum River basin.", "logistics": "Daecheong Dam park."},
                {"time": "17:30–19:30", "title": "Yuseong Thermal Foot Bath Stroll", "detail": "Dip feet into soothing mineral waters in Yuseong park.", "logistics": "Yuseong Spa Station."},
                {"time": "20:00–21:30", "title": "Daejeon Clay Pot Duck Stew (Oritang) Dinner", "detail": "Enjoy bubbling duck stew with wild perilla and leeks.", "logistics": "Yuseong Hot Springs alley."}
            ],
            [
                {"label": "Namganjeongsa Masterpiece", "text": "Namganjeongsa is designated Tangible Cultural Asset #4, renowned for channeling mountain spring water directly under the wooden pavilion floor."},
                {"label": "Philosophical Tranquility", "text": "Offers an unhurried, meditative glimpse into classical Joseon scholar life."}
            ],
            "Lunch: Rustic dotorimuk acorn jelly salad and wild herb bibimbap. Dinner: Yuseong rich Oritang duck stew with toasted perilla seeds.",
            "Uam Historic Park is open daily; admission is free.",
            "Park entry free; Taxi transfers ~₩20,000; Dinner ~₩25,000 per person.",
            "Stone steps around the water pavilion can be damp; step carefully.",
            "Water Culture Center and park pavilions provide covered shelters."
        ),
        # Day 11: Nov 11
        make_day(10, "Daejeon", "Genealogy, Roots & Natural Healing", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Ppuri Park (Genealogy & Family Heritage Park) → Korea Jokbo Museum",
            "Ancestral Lineages, Clan Sculptures & Forest Sanctuaries",
            [
                {"time": "09:30–12:30", "title": "Ppuri Park (Ancestry & Family Heritage Park)", "detail": "Walk across the scenic Manseonggyo suspension bridge into the world's only family lineage park, discovering 240+ monumental sculptures representing Korean family clan names and family trees.", "logistics": "Jung-gu Sanseong-dong; Bus 313/513 or taxi."},
                {"time": "12:30–13:30", "title": "Korea Jokbo Museum (Genealogy Museum)", "detail": "Tour the unique museum preserving centuries of clan genealogy books (jokbo) and royal lineage records.", "logistics": "Located inside Ppuri Park (free admission)."},
                {"time": "13:45–15:00", "title": "Riverside Traditional Duck & Rice Lunch", "detail": "Dine on grilled duck slices and savory soybean stew overlooking the Yudeungcheon River.", "logistics": "Sanseong-dong restaurant row."},
                {"time": "15:30–17:30", "title": "Yuseong Mineral Hot Spring Onsen Soak", "detail": "Full mineral bath to rejuvenate legs and body.", "logistics": "Yuseong Onsen bathhouse."},
                {"time": "18:30–20:30", "title": "Sung Sim Dang Heritage Bakery Evening Crawl", "detail": "Explore the historic 1956 flagship bakery in Jungangno and pick up artisanal pastries.", "logistics": "Jungangno Station Line 1 Exit 2."}
            ],
            [
                {"label": "Unique Cultural Institution", "text": "Ppuri Park offers deep insight into Korean Confucian family values and lineage documentation."},
                {"label": "Artistic Monuments", "text": "Each clan sculpture was designed by a prominent Korean contemporary sculptor."}
            ],
            "Lunch: Riverside grilled duck breast with fresh ssam greens. Dinner: Jungangno historic Korean beef soup or grilled pork belly.",
            "Ppuri Park and Jokbo Museum are free admission.",
            "Free park entry; Hot spring soak ~₩10,000; Dinner ~₩22,000 per person.",
            "Manseonggyo suspension bridge offers sweeping river photos.",
            "Korea Jokbo Museum is fully enclosed and climate-controlled."
        ),
        # Day 12: Nov 12
        make_day(11, "Daejeon", "Traditional Crafts & Tea Culture", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Daejeon Traditional Culture Center & Craft Studio → Gapcheon Sunset Stroll",
            "Living Folk Arts, Tea Ceremonies & Pre-Busan Preparation",
            [
                {"time": "10:00–12:30", "title": "Daejeon Intangible Cultural Heritage Center", "detail": "Observe traditional artisans demonstrating Korean woodwork, lacquer, and court music instruments (Gayageum/Geomungo).", "logistics": "Daedeok-gu Songchon-dong."},
                {"time": "12:45–14:15", "title": "Traditional Tea & Lotus Leaf Rice Lunch", "detail": "Enjoy fragrant lotus leaf wrapped sticky rice (yeonipbap) served with 12 medicinal mountain side dishes.", "logistics": "Songchon cultural district."},
                {"time": "14:30–16:30", "title": "Hanbat Arboretum Autumn Metasequoia Farewell Walk", "detail": "Final peaceful stroll under soaring golden metasequoias.", "logistics": "Hanbat West Garden."},
                {"time": "17:00–18:30", "title": "Daejeon Shinsegae Art Gallery & Sky Terrace", "detail": "Browse contemporary art installations and watch the sun set over the Gapcheon River.", "logistics": "Hotel Onoma complex."},
                {"time": "19:00–21:00", "title": "Daejeon Farewell Hanwoo BBQ Feast", "detail": "Celebrate 5 rich days in Daejeon with charcoal-grilled Hanwoo beef.", "logistics": "Dunsan / Yuseong district."}
            ],
            [
                {"label": "Living Heritage", "text": "The Heritage Center connects centuries-old craft lineages with living master demonstrations."},
                {"label": "Daejeon Completion", "text": "Prepares for Friday high-speed rail transit to coastal Busan."}
            ],
            "Lunch: Traditional steamed lotus leaf rice (yeonipbap) banquet. Dinner: Daejeon charcoal Hanwoo beef barbecue.",
            "Cultural Center admission is free; verify workshop demonstration times upon entry.",
            "Craft Center free; Hanwoo dinner ~₩45,000 per person.",
            "Pack primary luggage tonight for Friday morning KTX to Busan.",
            "Shinsegae Art Gallery and Cultural Center are indoor venues."
        ),
        # Day 13: Nov 13
        make_day(12, "Busan", "Coastward Rail & Maritime Scholar Heritage", "Busan · Haeundae Beachfront",
            "KTX Daejeon to Busan (1h30m) → Haeundae Check-in → Dongbaekseok Choe Chi-won Heritage Walk",
            "Coastal Rail Transit & Ancient Scholar Inscriptions",
            [
                {"time": "10:00–11:30", "title": "KTX High-Speed Rail to Busan", "detail": "90-minute smooth train transit down the Gyeongbu rail line to Busan Station.", "logistics": "Board train at Daejeon Station."},
                {"time": "11:45–13:15", "title": "Busan Station Choryang Milmyeon Lunch", "detail": "Enjoy authentic cold wheat noodles and steamed mandu dumplings.", "logistics": "Opposite Busan Station."},
                {"time": "13:45–15:00", "title": "Transfer to Haeundae Beachfront Base", "detail": "Check into Haeundae hotel (e.g. L7 Haeundae or Felix by STX).", "logistics": "Metro Line 2 or taxi along harbor bridge."},
                {"time": "15:30–18:00", "title": "Dongbaekseok Island & Choe Chi-won Memorial Walk", "detail": "Walk the pine-covered island trails to find the 9th-century rock carvings by Silla dynasty scholar-poet Choe Chi-won (who named 'Haeundae' after his pen name Haeun), visiting the APEC Nurimaru House.", "logistics": "Oceanside boardwalk."},
                {"time": "18:30–21:00", "title": "Haeundae Grilled Seafood & Pajeon Dinner", "detail": "Feast on fresh coastal seafood and green onion pancakes.", "logistics": "Haeundae Traditional Market."}
            ],
            [
                {"label": "Literary Roots of Haeundae", "text": "Dongbaek Island preserves the origin story of Busan's most famous coast named by Silla master poet Choe Chi-won."},
                {"label": "Coastal Harmony", "text": "APEC House exemplifies traditional Korean architectural lines integrated into a modern glass pavilion."}
            ],
            "Lunch: Choryang Milmyeon (Busan wheat noodles & dumplings). Dinner: Haeundae fresh grilled seafood hot pot and green onion pancake.",
            "Book KTX Daejeon→Busan on Korail app 30 days prior.",
            "KTX ticket ~₩36,200; Dongbaekseok walk is free.",
            "APEC Nurimaru House closes at 17:00 (last entry 16:30).",
            "SEA LIFE Busan Aquarium and Dongbaek Nurimaru provide indoor shelter."
        ),
        # Day 14: Nov 14
        make_day(13, "Busan", "Seaside Cliff Temples & Coastal Fishing", "Busan · Haeundae Beachfront",
            "Haedong Yonggungsa Seaside Temple (1376 AD) → Cheongsapo Fishing Village → Gwangalli Drones",
            "Buddhist Cliffside Sanctuaries & Saturday Night Lights",
            [
                {"time": "09:00–11:30", "title": "Haedong Yonggungsa Temple (Temple by the Sea)", "detail": "Visit the 1376 Goryeo-era Buddhist sanctuary built on jagged coastal granite cliffs, honoring the Haesu Gwaneum Daebul (Sea Goddess of Compassion) listening to roaring waves.", "logistics": "Bus 181 from Haeundae or 20-min taxi."},
                {"time": "12:00–13:30", "title": "Cheongsapo Fishing Village Grilled Clam Lunch", "detail": "Enjoy live scallops and abalone grilled over briquettes with butter and cheese at an oceanfront terrace.", "logistics": "Cheongsapo harbor lane."},
                {"time": "14:00–16:30", "title": "Haeundae Blueline Park Beach Train Stroll", "detail": "Ride the retro coastal train from Cheongsapo back along the coastal cliffs to Mipo.", "logistics": "Cheongsapo Station."},
                {"time": "17:00–18:30", "title": "Gwangalli Beach Twilight Stroll", "detail": "Watch the sunset illuminate Gwangan Suspension Bridge.", "logistics": "Gwangan Station Line 2."},
                {"time": "19:00–21:30", "title": "Millak Raw Fish Feast & Saturday Drone Show", "detail": "Savor sliced seasonal sashimi with ocean views and watch 500+ synchronized LED drones dance above Gwangan Bridge.", "logistics": "Millak Raw Fish Tower (drones at 19:00 & 21:00)."}
            ],
            [
                {"label": "Rare Coastal Temple", "text": "While most Korean temples sit deep in mountains, Haedong Yonggungsa commands a dramatic open sea vista."},
                {"label": "Saturday Spectacle", "text": "Timed for Saturday evening to witness Gwangalli's illuminated drone performance."}
            ],
            "Lunch: Cheongsapo seaside grilled clams (jogae-gui). Dinner: Millak Raw Fish Town fresh yellowtail sashimi, abalone, and spicy maeuntang.",
            "Haedong Yonggungsa is open year-round from 05:00 to sunset; free admission.",
            "Temple free; Beach train ₩7,000; Clam lunch ~₩35,000; Sashimi ~₩40,000 per person.",
            "Granite stone stairs down to Yonggungsa temple can be slippery; hold handrails.",
            "Millak indoor restaurants offer panoramic glass views of Gwangan Bridge."
        ),
        # Day 15: Nov 15
        make_day(14, "Busan", "Wartime Heritage & Cliff Villages", "Busan · Haeundae Beachfront",
            "Provisional Capital Memorial Hall → Gamcheon Culture Village → Jagalchi Marine Market",
            "Korean War Sanctuary & Vibrant Pastel Alleys",
            [
                {"time": "09:30–11:30", "title": "Provisional Capital Memorial Hall", "detail": "Tour the preserved 1950s presidential residence used by President Syngman Rhee when Busan served as Korea's wartime provisional capital during the Korean War.", "logistics": "Dongdaesin Station Line 1 Exit 2; free admission."},
                {"time": "12:00–14:30", "title": "Gamcheon Culture Village History & Art Walk", "detail": "Discover how 1950s wartime refugee shanties were transformed through community art into a vibrant hillside terraced cultural landmark.", "logistics": "Toseong Station Line 1 Exit 6 + local bus Saha 1-1."},
                {"time": "15:00–17:30", "title": "Jagalchi Fish Market & Nampo Heritage", "detail": "Explore Korea's biggest marine market and walk BIFF Square.", "logistics": "Jagalchi Station Line 1 Exit 10."},
                {"time": "18:00–20:30", "title": "Traditional Busan Dwaeji Gukbap Dinner", "detail": "Taste historic rich pork bone soup simmered for 24 hours.", "logistics": "Nampo / Choryang soup alley."}
            ],
            [
                {"label": "Wartime Resilience", "text": "Provisional Capital Memorial Hall reveals Busan's pivotal role as the last democratic refuge during 1950–1953."},
                {"label": "Community Art Transformation", "text": "Gamcheon illustrates how art preserved historical memory while rejuvenating the neighborhood."}
            ],
            "Lunch: Gamcheon hillside cafe artisan sandwich or bibimbap. Dinner: Traditional Nampo-dong Dwaeji Gukbap (pork bone soup) with boiled suyuk.",
            "Provisional Capital Memorial Hall closed on Mondays; free admission.",
            "Memorial Hall free; Gamcheon map ₩2,000; Dinner ~₩15,000 per person.",
            "Gamcheon paths involve uphill stairs; comfortable walking shoes essential.",
            "Memorial Hall and Jagalchi 7-story building provide indoor shelter."
        ),
        # Day 16: Nov 16
        make_day(15, "Busan", "Ancient Silla Mountain Temple & Fortress", "Busan · Haeundae Beachfront",
            "Beomeosa Head Temple (678 AD) → Geumjeongsanseong Mountain Fortress North Gate",
            "1,300-Year Buddhist Head Sanctuary & Mountain Bastions",
            [
                {"time": "09:30–12:30", "title": "Beomeosa Temple (Temple of the Nirvana Fish)", "detail": "Explore one of Korea's greatest Buddhist head temples, founded by Master Uisang in 678 AD during the Silla Kingdom, viewing the Three-Story Stone Pagoda (National Treasure) and Daeungjeon Main Hall.", "logistics": "Beomeosa Station Line 1 Exit 5, then Bus 90 up mountain."},
                {"time": "12:45–14:15", "title": "Dongnae Halmae Pajeon (Busan Cultural Asset #1) Lunch", "detail": "Feast on 80-year-old royal scallion seafood pancake with Geumjeongsanseong traditional makgeolli.", "logistics": "Dongnae-gu Myeongnyun-dong."},
                {"time": "14:45–17:00", "title": "Geumjeongsanseong Fortress North Gate Trail", "detail": "Walk the reconstructed granite battlements of Korea's largest mountain fortress (17km perimeter) built in 1703 against coastal invasions.", "logistics": "Hike from Beomeosa or take Geumgang Park cable car."},
                {"time": "17:30–19:30", "title": "Oncheonjang Natural Hot Spring Bath", "detail": "Dip into historic Oncheonjang hot spring waters used since Silla times.", "logistics": "Oncheonjang Station Line 1."},
                {"time": "20:00–21:30", "title": "Dongnae Sliced Pork Suyuk & Kimchi Feast", "detail": "Enjoy tender steamed pork slices with fresh oyster kimchi.", "logistics": "Dongnae dining street."}
            ],
            [
                {"label": "Silla Buddhist Masterpiece", "text": "Beomeosa is among the most revered and spiritually intact temple complexes in East Asia."},
                {"label": "Historic Stone Bastion", "text": "Geumjeongsanseong offers panoramic views over Busan harbor and mountain ridges."}
            ],
            "Lunch: Dongnae Halmae Pajeon (heritage scallion pancake) with Geumjeongsanseong makgeolli. Dinner: Dongnae pork suyuk and seasoned mountain roots.",
            "Beomeosa Temple is free admission; open daily.",
            "Temple free; Pajeon lunch ~₩25,000; Hot spring ~₩10,000 per person.",
            "Mountain paths have uneven stone steps; hold handrails.",
            "Beomeosa temple museum and Oncheonjang spa are fully indoor."
        ),
        # Day 17: Nov 17
        make_day(16, "Busan", "Industrial Transformation & Modern Art", "Busan · Haeundae Beachfront",
            "F1963 Cultural Complex (Wire Factory to Arts Hub) → Kukje Gallery Busan → Kiswire Museum",
            "Post-Industrial Art Spaces & Visionary Architecture",
            [
                {"time": "10:00–12:30", "title": "F1963 Cultural Complex (Former Kiswire Factory)", "detail": "Tour the visionary industrial architecture of a 1963 wire rope factory converted into an eco-arts complex, featuring Yes24 massive bookstore, bamboo gardens, and the Hyundai Motorstudio Busan design pavilion.", "logistics": "Mangmi Station Line 3 or 15-min taxi from Haeundae."},
                {"time": "12:30–14:00", "title": "Terarosa Specialty Coffee & Bakery Lunch", "detail": "Enjoy pour-over specialty coffee and artisan sourdough in the dramatic factory interior preserved with original wire spools and steel trusses.", "logistics": "Inside F1963."},
                {"time": "14:15–16:00", "title": "Kukje Gallery Busan & Kiswire Museum", "detail": "Examine avant-garde contemporary art exhibits at premier Kukje Gallery and learn about architectural suspension cables at Kiswire Museum.", "logistics": "Inside F1963 complex."},
                {"time": "16:30–18:30", "title": "Busan Cinema Center Architecture Walk", "detail": "Visit the world-record LED cantilever roof at the Centum City film center.", "logistics": "Centum City Station Line 2."},
                {"time": "19:00–21:00", "title": "Centum City Korean Fine Dining", "detail": "Enjoy modern Korean seasonal tasting menu.", "logistics": "Shinsegae Centum City 9F."}
            ],
            [
                {"label": "Industrial Adaptive Reuse", "text": "F1963 is Korea's most celebrated industrial-to-cultural architecture transformation."},
                {"label": "Leading Contemporary Galleries", "text": "Kukje Gallery brings premier international and Korean contemporary masters to Busan."}
            ],
            "Lunch: Terarosa F1963 artisan sourdough sandwich and pour-over coffee. Dinner: Centum City modern Korean tasting course with seasonal seafood.",
            "F1963 exhibitions and bookstore open daily 10:00–20:00; admission is free.",
            "F1963 is free; Cinema Center free exterior; Dinner ~₩35,000 per person.",
            "Hyundai Motorstudio Busan design exhibits are free entry.",
            "F1963 is 100% enclosed, heated, and weatherproof."
        ),
        # Day 18: Nov 18
        make_day(17, "Busan", "Eco-Art & Marine Nature", "Busan · Haeundae Beachfront",
            "MoCA Busan (Museum of Contemporary Art on Eulsukdo) → Dadaepo Sunset",
            "Eco-Architecture, Vertical Gardens & Estuary Art",
            [
                {"time": "10:00–13:00", "title": "Museum of Contemporary Art Busan (MoCA Busan)", "detail": "Explore the striking eco-art museum on Eulsukdo Island featuring the monumental living vertical garden facade by French botanist Patrick Blanc and cutting-edge media art installations.", "logistics": "Hadan Station Line 1 Exit 3, then Bus 168/3/55 or 30-min taxi."},
                {"time": "13:15–14:30", "title": "Eulsukdo Eco-Park Riverside Lunch", "detail": "Enjoy fresh clam noodle soup or Korean rice bowl overlooking Nakdong River wetlands.", "logistics": "Eulsukdo cultural center cafe."},
                {"time": "15:00–17:30", "title": "Dadaepo Beach & Coastal Boardwalk", "detail": "Walk the wooden boardwalk across vast coastal tidal wetlands and reed fields where the Nakdong River meets the South Sea, capturing fiery coastal sunsets.", "logistics": "Dadaepo Beach Station Line 1 Exit 4."},
                {"time": "18:00–19:30", "title": "Dadaepo Sunset Beach Promenade", "detail": "Relax along the illuminated dune boardwalk.", "logistics": "Dadaepo coastal park."},
                {"time": "20:00–21:30", "title": "Seomyeon Korean Charcoal BBQ Dinner", "detail": "Feast on tender charcoal-grilled pork neck and kimchi stew.", "logistics": "Seomyeon Station Line 1/2."}
            ],
            [
                {"label": "Eco-Artistic Vision", "text": "MoCA Busan seamlessly blends ecological conservation on migratory bird island Eulsukdo with world-class contemporary art."},
                {"label": "Spectacular Estuary Sunset", "text": "Dadaepo offers the most expansive and dramatic sunset horizon in Busan."}
            ],
            "Lunch: Eulsukdo fresh clam soup and vegetable bibimbap. Dinner: Seomyeon charcoal-grilled pork barbecue with soybean stew.",
            "MoCA Busan closed on Mondays; free admission to permanent exhibitions.",
            "Museum is free; Meals ~₩30,000 per person.",
            "Dadaepo coastal breezes can be brisk at sunset; wear a warm outer layer.",
            "MoCA Busan is fully indoor with spacious galleries."
        ),
        # Day 19: Nov 19
        make_day(18, "Busan", "Solemn Peace & Tea Heritage (CSAT Day)", "Busan · Haeundae Beachfront",
            "UN Memorial Cemetery in Korea → Busan Museum & Traditional Tea Experience (CSAT Day)",
            "Solemn Peace Gardens & Ancient Tea Ceremonies (CSAT / Suneung Day)",
            [
                {"time": "10:00–12:30", "title": "UN Memorial Cemetery in Korea", "detail": "Walk the solemn, beautifully manicured botanical memorial grounds—the world's only United Nations cemetery, honoring soldiers from 16 nations who defended Korea during the 1950–1953 war.", "logistics": "Daeyeon Station Line 2 Exit 3, 10-min walk."},
                {"time": "12:45–14:00", "title": "Daeyeon Ssangdungi Dwaeji Gukbap Lunch", "detail": "Savor famous boiled pork slices (suyuk baekban) served with warm pork broth and rice.", "logistics": "5-minute walk from UN Memorial."},
                {"time": "14:15–16:30", "title": "Busan Museum & Traditional Tea Ceremony Experience", "detail": "Tour Busan's archaeological artifacts and participate in a serene, traditional Korean tea ceremony (Darye) wearing hanbok in the museum cultural hall.", "logistics": "Adjacent to UN Memorial Cemetery."},
                {"time": "17:00–19:00", "title": "Haeundae Sunset Beach Stroll", "detail": "Tranquil evening beach walk reflecting on 7 unforgettable Busan nights.", "logistics": "Haeundae beachfront."},
                {"time": "19:30–21:30", "title": "Busan Farewell Hanwoo Beef Short Ribs Feast", "detail": "Celebrate final night in Busan with premium charcoal-grilled Korean Hanwoo beef.", "logistics": "Haeundae Somunnan Amso Galbi."}
            ],
            [
                {"label": "CSAT Low-Stakes Alignment", "text": "Nov 19 national CSAT exam day is spent peacefully in quiet botanical memorial parks and cultural tea rooms, avoiding urban traffic stress."},
                {"label": "Darye Tea Contemplation", "text": "The traditional tea ceremony provides a mindful, contemplative cultural memory."}
            ],
            "Lunch: Daeyeon Ssangdungi Dwaeji Gukbap (boiled pork belly set with rich broth). Afternoon: Traditional Korean green tea and rice cake. Dinner: Haeundae Hanwoo beef short ribs with potato noodles.",
            "UN Memorial Cemetery open 09:00–17:00 (free entry; respectful attire required). Tea ceremony at Busan Museum is free (register at 1F counter).",
            "Cemetery free; Museum free; Tea ceremony free; Farewell Hanwoo dinner ~₩48,000 per person.",
            "No loud voices or casual sports inside UN Memorial grounds.",
            "Busan Museum is completely indoor and heated."
        ),
        # Day 20: Nov 20
        make_day(19, "Seoul", "Capital Return & Gate Architecture", "Seoul · Seoul Station / Myeongdong",
            "Morning KTX Busan to Seoul → Sungnyemun (Namdaemun Gate) → Insadong Heritage Craft Alleys",
            "Capital Return & National Treasure Architecture",
            [
                {"time": "09:30–10:15", "title": "Busan Station Departure", "detail": "Check out of Haeundae hotel, take taxi or metro to Busan Station, and board direct KTX.", "logistics": "Board train 10 minutes prior to departure."},
                {"time": "10:30–12:45", "title": "KTX High-Speed Rail to Seoul", "detail": "Comfortable 2-hour 15-minute smooth journey back to Seoul Station.", "logistics": "Direct arrival in central Seoul."},
                {"time": "13:00–14:30", "title": "Seoul Station Hotel Check-in & Lunch", "detail": "Check into Seoul Station hotel base and enjoy warm Korean beef stew.", "logistics": "Direct hotel connection."},
                {"time": "15:00–17:00", "title": "Sungnyemun (Namdaemun Gate National Treasure #1)", "detail": "Examine the majestic 1398 fortress gate, the oldest wooden building in Seoul and ceremonial southern entrance of the capital.", "logistics": "Hoehyeon Station Line 4 Exit 5."},
                {"time": "17:30–19:30", "title": "Insadong Heritage Craft Alleys & Teahouse", "detail": "Pick up authentic handcrafted Korean paper (Hanji), calligraphy seals, and celadon gifts.", "logistics": "Anguk Station Line 3."},
                {"time": "20:00–21:30", "title": "Gwanghwamun Traditional Royal Stew Dinner", "detail": "Savor royal hot pot (Sinseollo) or tender braised beef short ribs.", "logistics": "Gwanghwamun dining room."}
            ],
            [
                {"label": "Friday Departure Security", "text": "Returning to Seoul on Friday eliminates all risk of KTX travel delays before Sunday international flight."},
                {"label": "National Treasure #1", "text": "Sungnyemun represents the definitive architectural monument of Joseon dynasty craftsmanship."}
            ],
            "Lunch: Seoul Station traditional beef gomtang soup. Dinner: Gwanghwamun royal Hanjeongsik or galbijjim braised ribs.",
            "Book KTX Busan→Seoul 30 days prior on Korail app.",
            "KTX ticket ~₩59,800; Sungnyemun is free; Dinner ~₩35,000 per person.",
            "Friday afternoon KTX trains sell out fast; reserve early.",
            "Lotte Mart and Seoul Station concourse are completely enclosed."
        ),
        # Day 21: Nov 21
        make_day(20, "Seoul", "Folk Crafts & Royal Court Farewell", "Seoul · Seoul Station / Myeongdong",
            "Namdaemun Artisan Markets → Seoul Station Lotte Mart Gifts → Grand Hanjeongsik Farewell Feast",
            "Folk Craft Curation & Royal Court Farewell Banquet",
            [
                {"time": "09:30–12:30", "title": "Namdaemun Market Craft & Kitchenware Alleys", "detail": "Curate traditional brass cutlery (Bangjja Yugi), wooden tea trays, Korean ceramics, and handmade textiles.", "logistics": "Hoehyeon Station Line 4 Exit 5."},
                {"time": "13:00–15:30", "title": "Seoul Station Lotte Mart Gourmet Curation", "detail": "Curate fine green tea from Boseong, red ginseng extract (Hongsam), seasoned seaweed, and confectionery with instant tax refund.", "logistics": "Lotte Mart 2F immediate tax refund counter."},
                {"time": "16:00–18:00", "title": "Packing & Online Airline Check-in", "detail": "Pack delicate ceramics and crafts carefully with protective bubble wrap; complete online flight check-in for Sunday departure.", "logistics": "Hotel room."},
                {"time": "18:30–21:30", "title": "Grand Royal Court Farewell Banquet (Hanjeongsik)", "detail": "Celebrate 21 nights of Korean heritage with a 15-dish royal court dinner featuring grilled abalone, pine nut porridge, royal Sinseollo hot pot, and aged plum wine.", "logistics": "Central Seoul traditional Hanok dining estate."}
            ],
            [
                {"label": "Artisan Craftsmanship", "text": "Bangjja Yugi bronzeware and Korean ceramics are timeless heirloom souvenirs."},
                {"label": "Pristine Departure Readiness", "text": "All packing and check-in finished by Saturday night ensures Sunday morning is 100% serene."}
            ],
            "Lunch: Namdaemun hand-made kalguksu noodle soup. Dinner: Grand Royal Court Hanjeongsik 15-dish banquet with aged Korean maesil plum wine.",
            "Complete online airline check-in 24 hours prior to flight.",
            "Craft souvenirs ~₩50,000–₩150,000; Grand Farewell Dinner ~₩55,000 per person.",
            "Pack fragile ceramic pieces inside clothing in checked bags.",
            "Underground department store passages connect Namdaemun to Myeongdong."
        ),
        # Day 22: Nov 22
        make_day(21, "Seoul", "Departure", "Departure · Incheon International Airport",
            "AREX Non-Stop Express to ICN → Customs & Tax Refunds → Flight at 13:00",
            "Seamless Airport Rail & Calm Flight Departure",
            [
                {"time": "08:30–09:15", "title": "Hotel Checkout & AREX Express Boarding", "detail": "Check out of Seoul Station hotel and board direct AREX Non-Stop Express Train to Incheon Airport (43 mins).", "logistics": "B2 Seoul Station."},
                {"time": "09:30–10:15", "title": "AREX Express to ICN Terminal 1 / 2", "detail": "Fast, direct airport train ride with reserved seating and dedicated luggage racks.", "logistics": "43 min to T1 / 51 min to T2."},
                {"time": "10:15–12:15", "title": "Airport Customs, Tax Refunds & Departure Gate", "detail": "Drop luggage, clear security, collect tax refund cash, and reach departure gate by 12:20.", "logistics": "Target arriving 3 hours prior to 13:00 international flight."},
                {"time": "12:30–13:00", "title": "Boarding & Flight Departure at 13:00", "detail": "Board aircraft for the return flight home with rich memories of Korean heritage and fine arts.", "logistics": "Flight departs at 13:00 local time."}
            ],
            [
                {"label": "Zero Departure Stress", "text": "Direct AREX express guarantees exact 43-minute transit to Incheon Airport."},
                {"label": "Ample Buffer", "text": "Arriving at 10:15 leaves ample time for customs, tax refunds, and duty-free before boarding."}
            ],
            "Breakfast: Hotel café or airport lounge / Korean Food Street at ICN Terminal (warm abalone porridge or beef soup).",
            "Verify airline departure terminal (T1 vs T2) before boarding AREX.",
            "AREX Express ticket ₩13,000 per person (fare raised from ₩11,000; verified 2026).",
            "Terminal 2 is 8 minutes further on the AREX line than Terminal 1.",
            "If AREX express sells out, AREX all-stop commuter train departs every 8 minutes."
        )
    ]

    scorecard = [
        {"label": "Joseon Heritage", "value": "5/5", "tone": "good"},
        {"label": "Fine Arts & Architecture", "value": "5/5", "tone": "good"},
        {"label": "Temple Sanctuaries", "value": "5/5", "tone": "good"},
        {"label": "Craftsmanship", "value": "5/5", "tone": "good"}
    ]

    return {
        "id": "seoul-daejeon-busan-heritage",
        "shortTitle": "Seoul · Daejeon · Busan (Heritage & Fine Arts)",
        "title": "Joseon Dynasty, Hanok Living & Fine Arts (Heritage & Aesthetics)",
        "routeLabel": "Seoul (7N) → Daejeon (5N) → Busan (7N) → Seoul (2N)",
        "badge": "UNESCO Treasures & Fine Art Masters",
        "bestFor": "History enthusiasts, art lovers, architects, and travelers who appreciate UNESCO World Heritage palaces, serene Buddhist temple architecture, modernist galleries, and classical Confucian gardens.",
        "decisionSummary": "A contemplative, culturally rich route focusing on imperial Joseon palaces, the sublime Room of Quiet Contemplation, Daejeon's Lee Ungno modernist museum, and Busan's 1,300-year-old mountain temples and post-industrial art hubs.",
        "recommendation": "Choose this route if you want to explore the deepest layers of Korea's 5,000-year artistic and architectural legacy with unhurried, aesthetic pacing.",
        "tradeoff": "More time devoted to museums, traditional craft workshops, and temple contemplation rather than high-intensity nightlife or theme parks.",
        "scorecard": scorecard,
        "bases": get_sdb_common_bases(),
        "transfers": get_sdb_common_transfers(),
        "budgetScenarios": get_sdb_budget_scenarios(),
        "bookingPriorities": get_sdb_booking_priorities(),
        "days": days
    }
