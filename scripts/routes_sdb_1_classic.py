#!/usr/bin/env python3
"""Route Blueprint: Seoul · Daejeon · Busan (Classic Explorer)."""

from scripts.generate_all_itineraries import make_day
from scripts.itinerary_builder_sdb import (
    get_sdb_common_bases,
    get_sdb_common_transfers,
    get_sdb_budget_scenarios,
    get_sdb_booking_priorities
)

def get_sdb_classic():
    days = [
        # Day 1: Nov 1
        make_day(0, "Seoul", "Arrival", "Seoul · Myeongdong / Seoul Station edge",
            "ICN arrival at 21:00 → late transfer → hotel check-in → sleep",
            "Land softly; do not turn arrival night into sightseeing",
            [
                {"time": "21:00–22:15", "title": "ICN Arrival & Border Clearance", "detail": "Clear immigration, collect checked luggage, and pick up pre-booked eSIM / T-Money transport card at terminal arrivals hall.", "logistics": "Terminal 1 or 2 depending on flight carrier."},
                {"time": "22:30–23:45", "title": "Airport Transfer to Central Seoul", "detail": "Board Airport Limousine Bus (6001/6015) or official airport taxi queue directly to hotel in Myeongdong / Seoul Station.", "logistics": "Direct drop-off minimizes late-night stair transfers with heavy bags."},
                {"time": "23:45–00:30", "title": "Hotel Check-in & Rest", "detail": "Check into hotel room, unpack essentials, grab warm water or tea, and get restorative sleep.", "logistics": "Notify hotel front desk of late check-in in advance."}
            ],
            [
                {"label": "Arrival Protocol", "text": "Preserve physical energy after international transit; do not schedule dining reservations."},
                {"label": "Direct Transport", "text": "Airport bus or taxi eliminates confusing subway line transfers at midnight."}
            ],
            "Light convenience store snack (CU / GS25 warm samgak kimbap or banana milk) or room service.",
            "Confirm late check-in with hotel in writing 48 hours prior.",
            "Airport Limousine bus ~₩17,000 / Deluxe Taxi ~₩85,000.",
            "Late night jetlag; keep bedtime calm without heavy alcohol.",
            "If flight is delayed past 23:00, use official International Taxi counter at ICN Hall 4C/8C."
        ),
        # Day 2: Nov 2
        make_day(1, "Seoul", "Royal Heritage", "Seoul · Myeongdong / Seoul Station edge",
            "Gyeongbokgung Palace Guard Changing → Bukchon Hanok Village → Insadong Tea Alley",
            "Imperial Grandeur & Traditional Hanok Quarters",
            [
                {"time": "09:30–11:30", "title": "Gyeongbokgung Royal Palace", "detail": "Witness the vibrant Royal Guard Changing Ceremony at Gwanghwamun Gate (10:00 AM) and explore the majestic Geunjeongjeon throne hall and Gyeonghoeru Pavilion.", "logistics": "Subway Line 3 to Gyeongbokgung Station Exit 5."},
                {"time": "11:45–13:15", "title": "Samcheong-dong Traditional Lunch", "detail": "Stroll leafy Samcheong-dong street and savor handmade sujebi (potato-dough pasta soup) or bulgogi.", "logistics": "10-minute gentle walk from palace east gate."},
                {"time": "13:30–15:30", "title": "Bukchon Hanok Village Walk", "detail": "Wander preserved Joseon-era residential alleys with traditional tiled roofs overlooking modern Seoul skyline.", "logistics": "Uphill stone pathways; please respect quiet residential zone rules."},
                {"time": "15:45–18:00", "title": "Insadong Antique Street & Ssamzigil", "detail": "Browse calligraphy shops, artisan crafts, and sip roasted traditional jujube or omija tea in a wooden hanok teahouse.", "logistics": "Anguk Station Line 3 Exit 6."},
                {"time": "18:30–20:30", "title": "Welcome Korean BBQ Dinner", "detail": "Enjoy aged pork belly (samgyeopsal) grilled over charcoal with fresh ssam lettuce wraps and doenjang stew.", "logistics": "Jongno / Euljiro dining quarter."}
            ],
            [
                {"label": "Clustered Geography", "text": "Gyeongbokgung, Bukchon, and Insadong are contiguous northern heritage districts, requiring zero subway hops during the day."},
                {"label": "Autumn Ambience", "text": "Early November offers golden ginkgo foliage along Samcheong-dong and palace walls."}
            ],
            "Lunch: Samcheong-dong Sujebi (Michelin Bib Gourmand). Dinner: Jongno charcoal-grilled pork belly with soybean stew.",
            "Palace closed on Tuesdays; entry ₩3,000 (free if wearing hanbok).",
            "Sightseeing entry ₩3,000; meals ~₩35,000 per person.",
            "Bukchon is a quiet residential area; quiet hours strictly enforced after 17:00.",
            "National Folk Museum of Korea located inside palace grounds if weather turns rainy."
        ),
        # Day 3: Nov 3
        make_day(2, "Seoul", "UNESCO Gardens & Markets", "Seoul · Myeongdong / Seoul Station edge",
            "Changdeokgung Huwon Secret Garden → Ikseon-dong Hanok Cafes → Gwangjang Market",
            "Secret Royal Landscapes & Street Food Feasts",
            [
                {"time": "09:30–12:00", "title": "Changdeokgung Palace & Secret Garden (Huwon)", "detail": "Explore UNESCO World Heritage Changdeokgung and take a guided walking tour through the serene autumn Secret Garden pavilions and lotus ponds.", "logistics": "Anguk Station Line 3 Exit 3."},
                {"time": "12:15–14:00", "title": "Ikseon-dong Hanok Alleys & Lunch", "detail": "Discover retro-modern hanok alleys filled with artisanal bakeries, fusion cafes, and craft boutiques.", "logistics": "Jongno 3-ga Station Line 1/3/5 Exit 4."},
                {"time": "14:30–17:00", "title": "Jongmyo Royal Ancestral Shrine & Cheonggyecheon", "detail": "Walk the solemn grounds of Jongmyo Shrine and follow the tranquil Cheonggyecheon Stream pedestrian walkway.", "logistics": "Walk east from Ikseon-dong."},
                {"time": "17:30–20:30", "title": "Gwangjang Traditional Food Market", "detail": "Experience Korea's oldest market feast: crispy mung bean pancakes (bindaetteok), mayak gimbap, and beef tartare (yukhoe).", "logistics": "Jongno 5-ga Station Line 1 Exit 8."}
            ],
            [
                {"label": "Secret Garden Timing", "text": "Huwon requires advance timed reservation; early November autumn foliage here is world-famous."},
                {"label": "Seamless Walkway", "text": "Connecting Changdeokgung through Ikseon-dong to Gwangjang Market is a straight, flat pedestrian route."}
            ],
            "Lunch: Ikseon-dong hanok cafe (steamed egg toast or kalguksu). Dinner: Gwangjang Market bindaetteok, mayak gimbap, and makgeolli.",
            "Book Changdeokgung Huwon Secret Garden ticket online 6 days in advance at 10:00 AM KST.",
            "Palace + Garden entry ₩8,000; Market food ~₩20,000 per person.",
            "Gwangjang market food stalls are cash/T-money preferred; evening crowds can be dense.",
            "If heavy rain occurs, explore underground Jongno arcades and Gwangjang covered market."
        ),
        # Day 4: Nov 4
        make_day(3, "Seoul", "National Treasures & Heights", "Seoul · Myeongdong / Seoul Station edge",
            "National Museum of Korea → Yongsan Family Park → N Seoul Tower Sunset",
            "Masterpiece Artifacts & Mountain Skyline Views",
            [
                {"time": "09:30–12:30", "title": "National Museum of Korea", "detail": "Marvel at Korean national treasures including the Pensive Bodhisattva statues in the Room of Quiet Contemplation and Ten-Story Gyeongcheonsa Pagoda.", "logistics": "Ichon Station Line 4 / Gyeongui-Jungang Line direct underground connection."},
                {"time": "12:45–14:15", "title": "Ichon-dong Japanese Dining / Fusion Lunch", "detail": "Enjoy lunch in Little Tokyo Ichon-dong or museum garden lakeside restaurant.", "logistics": "Short walk from museum park."},
                {"time": "14:30–16:00", "title": "War Memorial of Korea", "detail": "Tour the expansive outdoor aircraft and naval exhibitions and solemn indoor memorial halls.", "logistics": "Samgakji Station Line 4/6 Exit 12."},
                {"time": "16:30–19:30", "title": "N Seoul Tower & Namsan Sunset", "detail": "Ascend Namsan via scenic cable car or shuttle bus to enjoy 360-degree sunset views over the entire Seoul metropolitan basin.", "logistics": "Myeongdong Namsan Cable Car or Yellow Shuttle Bus #01."},
                {"time": "20:00–21:30", "title": "Myeongdong Kyoja Dumpling Dinner", "detail": "Savor Michelin Bib Gourmand handmade pork dumplings (mandu) and rich chicken broth kalguksu with spicy garlic kimchi.", "logistics": "Myeongdong Station Line 4 Exit 8."}
            ],
            [
                {"label": "Cultural Depth", "text": "National Museum provides essential historical context before traveling to regional Joseon and Silla cities."},
                {"label": "Sunset Alignment", "text": "Reaching N Seoul Tower by 16:30 captures day, golden hour, and shimmering city nightscape in one visit."}
            ],
            "Lunch: Ichon Japanese katsu / Udon or Museum Garden Cafe. Dinner: Myeongdong Kyoja (handmade kalguksu and steamed mandu).",
            "National Museum permanent galleries are free; special exhibitions may require ticket.",
            "N Seoul Tower observatory ₩21,000; Cable car round-trip ₩15,000.",
            "Cable car queue can be 30–45 mins on clear evenings; shuttle bus 01 is faster alternative.",
            "National Museum of Korea is fully climate-controlled with vast indoor galleries."
        ),
        # Day 5: Nov 5
        make_day(4, "Seoul", "Youth Culture & Arts", "Seoul · Myeongdong / Seoul Station edge",
            "Hongdae Indie Culture → Gyeongui Line Forest Park → Yeonnam-dong Boutique Cafes",
            "Creative Hubs, Urban Greenways & Coffee Culture",
            [
                {"time": "10:00–12:30", "title": "Gyeongui Line Forest Park Stroll", "detail": "Walk the transformed former railway corridor lined with boutique shops, craft bakeries, and autumn trees.", "logistics": "Hongik Univ. Station Line 2 / AREX Exit 3."},
                {"time": "12:30–14:00", "title": "Yeonnam-dong Trendy Dining Lunch", "detail": "Enjoy artisanal handmade pasta, Korean rice bowls, or fresh bakery treats in trendy Yeonnam-dong.", "logistics": "Walk along Yeonnam cafe street."},
                {"time": "14:15–17:00", "title": "Hongdae Shopping & Indie Arts Street", "detail": "Browse unique Korean streetwear, stationary shops (Object, KT&G Sangsangmadang), and photo studios.", "logistics": "Hongdae Pedestrian Walking Street."},
                {"time": "17:15–19:00", "title": "Hongdae Live Street Busking", "detail": "Watch talented young K-pop dancers, acoustic musicians, and indie performers on Hongdae busking street.", "logistics": "Hongik Univ. Station Exit 8/9 area."},
                {"time": "19:30–21:30", "title": "Mapo Charcoal Galbi Barbecue Feast", "detail": "Feast on marinated pork ribs grilled over charcoal accompanied by refreshing cold dongchimi broth.", "logistics": "Mapo Station Line 5 BBQ Alley."}
            ],
            [
                {"label": "Youth Energy", "text": "Hongdae comes alive in the afternoon and evening with creative youth culture and music."},
                {"label": "Walkable Greenway", "text": "Forest park provides a calming pedestrian buffer between bustling commercial streets."}
            ],
            "Lunch: Yeonnam-dong Korean fusion bibimbap or handmade burger. Dinner: Mapo Original Galbi pork ribs.",
            "Most retail and indie shops in Hongdae open around 11:00 AM.",
            "Budget ~₩40,000 per person for dining and dessert cafes.",
            "Evening crowds in Hongdae on Friday/weekend get dense; keep valuables secure.",
            "KT&G Sangsangmadang offers multi-floor indoor art gallery, cinema, and design shop."
        ),
        # Day 6: Nov 6
        make_day(5, "Seoul", "Futuristic Architecture & Design", "Seoul · Myeongdong / Seoul Station edge",
            "Dongdaemun Design Plaza (DDP) → Seongsu-dong Concept Lofts → Han River Sunset Cruise",
            "Cutting-Edge Design & Brooklyn of Seoul",
            [
                {"time": "09:30–12:00", "title": "Dongdaemun Design Plaza (DDP)", "detail": "Explore Zaha Hadid's futuristic architectural masterpiece, design museums, innovation showrooms, and rooftop gardens.", "logistics": "Dongdaemun History & Culture Park Station Line 2/4/5 Exit 1."},
                {"time": "12:30–14:00", "title": "Seongsu-dong Industrial Loft Lunch", "detail": "Experience transformed red-brick shoe factory cafes and dining spaces in trendy Seongsu-dong.", "logistics": "Seongsu Station Line 2 Exit 3."},
                {"time": "14:15–16:30", "title": "Seongsu Flagship Boutiques (Tamburins, Gentle Monster, Daelim)", "detail": "Visit experiential architecture and multi-sensory concept stores across Seongsu Yeonmujang-gil.", "logistics": "Walkable fashion/design corridor."},
                {"time": "17:00–19:00", "title": "Ttukseom Hangang Park & Sunset View", "detail": "Relax along the Han River bank, enjoy automated Han River convenience store instant ramen, and watch the sunset.", "logistics": "Jayang (Ttukseom Resort) Station Line 7 Exit 2."},
                {"time": "19:30–21:30", "title": "Sindang-dong Tteokbokki Town Supper", "detail": "Enjoy famous bubbling tabletop spicy rice cakes cooked with ramen, dumplings, fishcakes, and eggs.", "logistics": "Sindang Station Line 2/6 Exit 7."}
            ],
            [
                {"label": "Modern Contrasts", "text": "Balances Seoul's futuristic architecture with industrial revitalization in Seongsu."},
                {"label": "Riverside Relaxation", "text": "Hangang park break prevents city fatigue and showcases everyday local Seoul life."}
            ],
            "Lunch: Seongsu Daelim Warehouse cafe dining. Dinner: Sindang-dong Tteokbokki Town shared boiling pot.",
            "DDP design store opens at 10:00; architecture exterior accessible 24/7.",
            "DDP exhibits ~₩15,000; Tteokbokki dinner ~₩12,000 per person.",
            "Seongsu popular flagship stores may have short digital queue wait times on weekends.",
            "DDP indoor design labs and Seongsu Daelim Warehouse provide covered indoor shelter."
        ),
        # Day 7: Nov 7
        make_day(6, "Seoul", "Gangnam & Temple Oasis", "Seoul · Myeongdong / Seoul Station edge",
            "Starfield COEX Library → Bongeunsa Millennium Temple → Han River Park Walk",
            "Glamour, Grand Libraries & Ancient Urban Sanctuary",
            [
                {"time": "10:00–12:30", "title": "Starfield COEX Library & Mega Mall", "detail": "Photograph the magnificent 13-meter tall book towers at Starfield Library and browse Asian largest underground shopping complex.", "logistics": "Samseong Station Line 2 Exit 6 or Bongeunsa Station Line 9 Exit 7."},
                {"time": "12:30–14:00", "title": "Parnas Mall Gourmet Lunch", "detail": "Enjoy Korean modern beef soup (gomtang) or royal hot pot in the lower level gourmet arcade.", "logistics": "Directly connected to COEX Mall."},
                {"time": "14:15–16:00", "title": "Bongeunsa Buddhist Temple", "detail": "Step across the street into an ancient peaceful temple founded in 794 AD, home to a majestic 23-meter stone Maitreya Buddha.", "logistics": "Bongeunsa Station Line 9 Exit 1."},
                {"time": "16:30–18:30", "title": "Apgujeong Rodeo & K-Star Road", "detail": "Walk Gangnam upscale fashion district, K-Star Road art bear statues, and Dosan Park cafes.", "logistics": "Apgujeong Rodeo Station Suin-Bundang Line Exit 2."},
                {"time": "19:00–21:00", "title": "Seoul Station Prep & Early Sleep", "detail": "Return to Myeongdong / Seoul Station base, pack primary luggage for Sunday KTX transit, and enjoy dinner.", "logistics": "Subway Line 4 return to Seoul Station."}
            ],
            [
                {"label": "Temple & Tower Harmony", "text": "Bongeunsa's serene incense and ancient wood sits in mesmerizing contrast to Gangnam glass skyscrapers."},
                {"label": "Transit Prep", "text": "Finishing early on Saturday night guarantees relaxed packing before Sunday morning KTX to Daejeon."}
            ],
            "Lunch: Hadongkwan 80-year Gomtang beef soup at COEX. Dinner: Myeongdong Dakgalbi spicy stir-fried chicken.",
            "Bongeunsa Temple is free entry; open until 22:00.",
            "Free entry to COEX library and temple; meals ~₩30,000 per person.",
            "COEX underground mall is vast; follow overhead color-coded floor navigation lines.",
            "COEX mall and Aquarium provide 100% weather-proof indoor environment."
        ),
        # Day 8: Nov 8
        make_day(7, "Daejeon", "City Transition", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Morning KTX Seoul to Daejeon (55 mins) → Sung Sim Dang Main Bakery → Expo Hanbit Tower Sunset",
            "High-Speed Rail into Korea's Science & Bakery Capital",
            [
                {"time": "09:30–10:15", "title": "Seoul Station Departure", "detail": "Walk to Seoul Station from hotel, grab morning coffee, and board direct KTX high-speed train.", "logistics": "Board train 10 minutes before departure; assigned carriage and seats."},
                {"time": "10:30–11:25", "title": "KTX to Daejeon Station", "detail": "Smooth 55-minute high-speed transit through central South Korea plains.", "logistics": "Daejeon Station is a major hub on Gyeongbu Line."},
                {"time": "11:45–13:30", "title": "Sung Sim Dang Legendary Bakery & Eunhaeng-dong", "detail": "Visit Korea's most celebrated historic bakery (since 1956) for warm Twigim Soboro (fried streusel pastry) and Panna Cotta; stroll Jungang Market.", "logistics": "Jungangno Station Line 1 Exit 2."},
                {"time": "14:00–15:30", "title": "Hotel Check-in & Settle in Yuseong / Dunsan", "detail": "Check into Daejeon base hotel (e.g. Hotel Onoma or Ramada Yuseong) and refresh.", "logistics": "Daejeon Metro Line 1 or short taxi."},
                {"time": "16:00–18:30", "title": "Expo Science Park & Hanbit Tower Media Facade", "detail": "Visit the 1993 Daejeon Expo site, ascend Hanbit Tower observatory for sunset, and witness Expo Bridge light reflections.", "logistics": "Near Shinsegae Art & Science Complex."},
                {"time": "19:00–21:00", "title": "Daejeon Spicy Dubu Duruchigi Dinner", "detail": "Savor Daejeon authentic specialty: spicy braised tofu stir-fry with knife-cut noodles (kalguksu sari).", "logistics": "Famous local spots in Daeheung-dong or Dunsan-dong."}
            ],
            [
                {"label": "Mid-Morning Transit", "text": "Leaving Seoul at 10:30 allows a relaxed breakfast without rush-hour luggage congestion."},
                {"label": "Bakery Legend", "text": "Visiting Sung Sim Dang on arrival day introduces Daejeon beloved food icon."}
            ],
            "Lunch: Sung Sim Dang fresh bakery delights & Jungang Market street snacks. Dinner: Gwangcheon Sikdang spicy Dubu Duruchigi tofu.",
            "Book KTX Seoul→Daejeon on Korail app 30 days prior.",
            "KTX ticket ~₩23,700 per person.",
            "Sung Sim Dang can have lines, but queues move swiftly (under 15 mins).",
            "Daejeon Shinsegae Art & Science offers multi-level indoor complex and observatory if rainy."
        ),
        # Day 9: Nov 9
        make_day(8, "Daejeon", "Innovation & Space", "Daejeon · Yuseong Hot Springs / Dunsan",
            "National Science Museum → KAIST Campus → Yuseong Outdoor Hot Spring Foot Bath",
            "Pioneering Science, Robotics & Thermal Spring Relief",
            [
                {"time": "09:30–12:30", "title": "National Science Museum & Science Center", "detail": "Tour Korea's foremost science museum featuring the Hall of Science & Technology, Natural History, and dynamic interactive physics pavilions.", "logistics": "Yuseong-gu Daedeok Science Town; City Bus 104/121."},
                {"time": "12:45–14:00", "title": "Daedeok Innopolis Research Valley Lunch", "detail": "Enjoy lunch at university faculty dining or local dolsot bibimbap restaurant.", "logistics": "Near KAIST main campus."},
                {"time": "14:15–16:00", "title": "KAIST Campus & Innovation Walk", "detail": "Explore the peaceful grounds of Korea's premier science institute (duck pond, high-tech labs, and student innovation center).", "logistics": "KAIST Main Campus."},
                {"time": "16:30–18:30", "title": "Yuseong Hot Springs Outdoor Foot Bath Park", "detail": "Dip tired feet into 100% natural 42°C alkaline mineral thermal waters in the landscaped public outdoor hot spring park.", "logistics": "Yuseong Spa Station Line 1 Exit 7; free public facility, bring a small towel."},
                {"time": "19:00–21:00", "title": "Yuseong Traditional Duck Stew (Oritang) Dinner", "detail": "Warm up with a hearty clay pot of simmered duck with wild perilla seeds and seasonal greens.", "logistics": "Yuseong Hot Spring dining alley."}
            ],
            [
                {"label": "Science & Relaxation", "text": "Pairs intellectual discovery at KAIST with therapeutic thermal foot bathing in Yuseong."},
                {"label": "Neighborhood Flow", "text": "All sites are clustered inside western Daejeon / Yuseong-gu, eliminating cross-city commutes."}
            ],
            "Lunch: KAIST student boulevard stone-pot bibimbap. Dinner: Yuseong mineral water duck stew or Hanwoo beef bulgogi.",
            "National Science Museum Hall of Science is free; planetarium requires small fee (₩2,000).",
            "Museum free; Foot bath free; Dinner ~₩25,000 per person.",
            "Bring a hand towel for drying feet after Yuseong outdoor foot bath.",
            "National Science Museum is completely indoor and vast."
        ),
        # Day 10: Nov 10
        make_day(9, "Daejeon", "Arboretum & Fine Arts", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Hanbat Arboretum Autumn Metasequoia → Lee Ungno Museum → Dunsan Dining Quarter",
            "Urban Botanical Oases & Modern Fine Art",
            [
                {"time": "09:30–12:00", "title": "Hanbat Arboretum (West & East Gardens)", "detail": "Walk through Korea's largest artificial urban arboretum, featuring golden metasequoia walkways, pine forests, and wetland lotus ponds.", "logistics": "Govt Complex Daejeon Station Line 1 or City Bus 604/911."},
                {"time": "12:15–13:30", "title": "Dunsan Cafe Boulevard Lunch", "detail": "Enjoy lunch near Dunsan government center (hand-rolled mandu or tonkatsu).", "logistics": "5-minute walk from arboretum south gate."},
                {"time": "13:45–15:30", "title": "Lee Ungno Museum of Art & Daejeon Museum of Art", "detail": "Admire the modernist white stone architecture by Laurent Beaudouin and explore the abstract calligraphy paintings of master artist Lee Ungno.", "logistics": "Located inside Expo park cultural grounds."},
                {"time": "16:00–18:00", "title": "Daejeon Shinsegae Art & Science Sky Park", "detail": "Take the high-speed elevator to the 38th floor Starbucks and rooftop sculpture terrace overlooking the Gapcheon River.", "logistics": "Hotel Onoma / Shinsegae Complex."},
                {"time": "18:30–20:30", "title": "Daejeon Kalguksu & Suyuk Dinner", "detail": "Feast on rich clam-broth hand-cut noodles and tender steamed pork belly slices (suyuk).", "logistics": "Dunsan culinary street."}
            ],
            [
                {"label": "Aesthetic Balance", "text": "Combines natural autumn landscape with world-class fine art and panoramic city river views."},
                {"label": "Central Positioning", "text": "All destinations surround the Gapcheon River cultural corridor."}
            ],
            "Lunch: Dunsan handmade dumpling soup. Dinner: Famous Daejeon hand-cut clam kalguksu with suyuk boiled pork.",
            "Lee Ungno Museum closed on Mondays; entry ₩1,000.",
            "Hanbat Arboretum is free; Museum entry ₩1,000; Shinsegae sky lounge free.",
            "Dress warmly for rooftop sky garden terrace in November breezes.",
            "Daejeon Museum of Art and Shinsegae Art Center are fully indoor."
        ),
        # Day 11: Nov 11
        make_day(10, "Daejeon", "Nature Trekking", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Gyejoksan Mountain Barefoot Red Clay Trail → Dongchundang Historic Hanok",
            "Healing Earth Trails & Scholar Heritage",
            [
                {"time": "09:00–13:00", "title": "Gyejoksan Red Clay Trail Walk", "detail": "Experience Korea's famous 14.5km natural red clay mountain trail (earthing therapy) through crisp autumn pine forests up to Gyejoksanseong Stone Fortress.", "logistics": "City Bus 74 from Daejeon Station or 25-minute taxi to Jangdong forest entrance."},
                {"time": "13:15–14:30", "title": "Jangdong Local Farmer Lunch", "detail": "Enjoy country-style acorn jelly salad (dotorimuk), potato pancakes (gamjajeon), and fresh wild greens bibimbap.", "logistics": "Base village restaurants at trail entrance."},
                {"time": "15:00–17:00", "title": "Dongchundang Historic House (Joseon Scholar Residence)", "detail": "Tour the 17th-century wooden estate and serene scholar pavilion of Song Jun-gil, showcasing Joseon aristocratic architecture.", "logistics": "Daedeok-gu Songchon-dong; short bus/taxi."},
                {"time": "17:30–19:30", "title": "Yuseong Thermal Spa Mineral Bath Reset", "detail": "Soak in a traditional indoor mineral hot spring bathhouse to relax leg muscles after mountain hiking.", "logistics": "Yuseong Hotel / Onsen public baths."},
                {"time": "20:00–21:30", "title": "Grilled Eel (Jangeo-gui) Feast", "detail": "Replenish stamina with charcoal-grilled freshwater eel seasoned with sweet ginger soy glaze.", "logistics": "Yuseong Hot Springs dining quarter."}
            ],
            [
                {"label": "Earthing & Wellness", "text": "Gyejoksan's soft clay trail is a signature Daejeon natural wellness experience."},
                {"label": "Thermal Recovery", "text": "Ending the hiking day with a Yuseong hot spring soak completely relieves physical fatigue."}
            ],
            "Lunch: Jangdong forest village dotorimuk and potato pancake. Dinner: Yuseong charcoal-grilled freshwater eel with seasoned rice.",
            "Wash stations with clean water are available along Gyejoksan clay trail.",
            "Trail and Dongchundang are free; Thermal bath ~₩10,000; Dinner ~₩35,000 per person.",
            "Wear comfortable walking shoes with socks easy to remove if walking barefoot on red clay.",
            "If rainy, replace hiking with the Daejeon Modern History Museum and indoor spa day."
        ),
        # Day 12: Nov 12
        make_day(11, "Daejeon", "Forest Canopy & Lake Vistas", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Jangtaesan Metasequoia Forest Canopy Skywalk → Daecheongho Lake Eco Walk",
            "Soaring Metasequoia Canopies & Serene Lakeside Panoramas",
            [
                {"time": "09:15–12:30", "title": "Jangtaesan Recreational Metasequoia Forest", "detail": "Walk among towering 30-meter autumn metasequoia trees, traverse the elevated canopy skywalk bridge, and climb the wooden sky tower.", "logistics": "City Bus 20 or 35-minute taxi to Jangan-dong."},
                {"time": "12:45–14:15", "title": "Lakeside Country Duck Stew Lunch", "detail": "Enjoy country chicken stew (dakbokkeumtang) or grilled mountain mushrooms at a rustic lakeside cottage.", "logistics": "Seo-gu Jangan-dong dining cabins."},
                {"time": "14:45–17:00", "title": "Daecheongho Lake Waterfront Eco Trail", "detail": "Stroll the wooden boardwalks around vast Daecheongho Lake, capturing shimmering water reflections and autumn reed fields.", "logistics": "Daecheong Dam Water Culture Center."},
                {"time": "17:30–19:30", "title": "Sung Sim Dang DCC Branch & Farewell Daejeon Stroll", "detail": "Pick up fresh baked goods for tomorrow train ride at the DCC branch and walk the Gapcheon riverside promenade.", "logistics": "Daejeon Convention Center area."},
                {"time": "20:00–21:30", "title": "Daejeon Galbi BBQ Dinner", "detail": "Enjoy sweet soy-marinated pork galbi grilled over real wood charcoal.", "logistics": "Dunsan / Yuseong district."}
            ],
            [
                {"label": "Spectacular Autumn Foliage", "text": "Jangtaesan's metasequoias reach peak rust-orange coloring in early-to-mid November."},
                {"label": "Daejeon Completion", "text": "Concludes 5 memorable nights in Daejeon with pristine forest and lake scenery."}
            ],
            "Lunch: Jangtaesan rustic spicy chicken stew (dakbokkeumtang). Dinner: Dunsan charcoal pork galbi with cold noodles.",
            "Jangtaesan skywalk open 09:00–17:00; admission is free.",
            "Free park entry; Taxi transfers ~₩25,000 each way; Dinner ~₩28,000 per person.",
            "Canopy suspension bridge can sway gently in high winds; hold railings.",
            "Daecheong Dam Water Culture Center and indoor cafes provide covered lake viewing."
        ),
        # Day 13: Nov 13
        make_day(12, "Busan", "City Transition", "Busan · Haeundae Beachfront",
            "Morning KTX Daejeon to Busan (1h30m) → Haeundae Beach Hotel Check-in → Sunset Beach Walk",
            "Coastward Bound: High-Speed Rail to the Maritime Capital",
            [
                {"time": "10:00–10:45", "title": "Daejeon Station Departure", "detail": "Check out of Daejeon hotel, take Metro Line 1 to Daejeon KTX Station, and board high-speed train to Busan.", "logistics": "Luggage storage in train vestibules."},
                {"time": "11:00–12:30", "title": "KTX High-Speed Rail to Busan", "detail": "Scenic 90-minute high-speed journey down the Gyeongbu rail corridor to Busan Station on the southern sea.", "logistics": "Arrive at Busan Station central concourse."},
                {"time": "12:45–14:00", "title": "Busan Station Choryang Milmyeon Lunch", "detail": "Step outside Busan Station to savor famous cold wheat noodles (milmyeon) and steamed king dumplings.", "logistics": "Choryang-dong dining street directly opposite station."},
                {"time": "14:15–15:15", "title": "Metro / Taxi to Haeundae Beachfront", "detail": "Travel to Haeundae hotel base (Metro Line 2 to Haeundae Station or 35-min taxi along Busan Harbor Bridge).", "logistics": "Check into hotel (e.g. L7 Haeundae or Felix by STX)."},
                {"time": "15:30–18:00", "title": "Haeundae Beach Promenade & Dongbaekseok Island Walk", "detail": "Stroll white sands of Haeundae Beach and follow the wooden coastal boardwalk around pine-scented Dongbaek Island to APEC Nurimaru House.", "logistics": "Flat, illuminated oceanside pedestrian path."},
                {"time": "18:30–21:00", "title": "Haeundae Traditional Market Seafood Dinner", "detail": "Walk Haeundae market street and feast on grilled sea eel (godeulbaegi), fresh seafood hot pot, and famous seed hotteok (ssiat hotteok).", "logistics": "Haeundae Traditional Market (Gunam-ro street)."}
            ],
            [
                {"label": "Painless Transit", "text": "Direct 90-minute KTX arrives in Busan by noon, leaving the full afternoon for coastal air and beach walking."},
                {"label": "Haeundae Anchor", "text": "Staying in Haeundae provides seven nights of oceanfront serenity without changing hotels."}
            ],
            "Lunch: Choryang Milmyeon (Busan wheat cold noodles & giant dumplings). Dinner: Haeundae Traditional Market grilled seafood hot pot & ssiat hotteok.",
            "Book KTX Daejeon→Busan on Korail app 30 days in advance.",
            "KTX ticket ~₩28,500 per person.",
            "Dongbaek Island trail is paved and lighted; Nurimaru APEC House closes at 17:00.",
            "SEA LIFE Busan Aquarium on Haeundae beachfront offers indoor marine exhibits if stormy."
        ),
        # Day 14: Nov 14
        make_day(13, "Busan", "Coastal Panoramas & Temple", "Busan · Haeundae Beachfront",
            "Haeundae Blueline Park Beach Train to Cheongsapo → Haedong Yonggungsa Seaside Temple",
            "Ocean Rails, Sky Capsules & Coastal Cliff Sanctuaries",
            [
                {"time": "09:30–11:30", "title": "Haeundae Blueline Park Sky Capsule (Mipo to Cheongsapo)", "detail": "Ride a private colorful Sky Capsule cabin 10 meters above the sea along picturesque coastal cliffs to Cheongsapo fishing village.", "logistics": "Mipo Station; book tickets 2 weeks in advance online."},
                {"time": "11:30–13:00", "title": "Cheongsapo Twin Lighthouses & Grilled Clam Lunch", "detail": "Photograph the red and white twin lighthouses, walk the Daritdol Ocean Skywalk, and enjoy fresh grilled clams (jogae-gui).", "logistics": "Cheongsapo seaside restaurant row."},
                {"time": "13:30–16:00", "title": "Haedong Yonggungsa Temple (Temple by the Sea)", "detail": "Visit Korea's most dramatic Buddhist temple built directly onto coastal granite rocks, listening to crashing waves below.", "logistics": "Bus 181 from Cheongsapo or 15-minute taxi."},
                {"time": "16:30–18:30", "title": "Ananti Cove & Coastal Promenade Stroll", "detail": "Explore the luxury coastal promenade, oceanfront bookstore (Eternal Journey), and seaside cafe terrace in Gijang.", "logistics": "Short taxi from Yonggungsa."},
                {"time": "19:00–21:30", "title": "Gwangalli Beach & Saturday Drone Light Show", "detail": "Watch 500+ synchronized LED drones dance over Gwangan Diamond Suspension Bridge from the sandy beachfront.", "logistics": "Gwangalli Beach; Saturday shows at 19:00 & 21:00 (winter schedule)."}
            ],
            [
                {"label": "Eastern Coastal Synergy", "text": "Blueline Park, Cheongsapo, Yonggungsa, and Gwangalli form a natural eastern coastline day."},
                {"label": "Saturday Drone Spectacular", "text": "Timed specifically for Saturday evening to witness Gwangalli's world-renowned drone performance."}
            ],
            "Lunch: Cheongsapo seaside grilled clams (jogae-gui) with butter and cheese. Dinner: Gwangalli beachfront raw fish / Korean craft beer and fried chicken.",
            "Book Blueline Park Sky Capsule 14 days in advance on official website (sells out fast).",
            "Sky Capsule 2-person cabin ₩35,000; Yonggungsa Temple is free entry.",
            "Haedong Yonggungsa has stone steps down to the cliffs; wear non-slip shoes.",
            "Eternal Journey Bookstore at Ananti and Centum City provide covered coastal alternatives."
        ),
        # Day 15: Nov 15
        make_day(14, "Busan", "Hillside Heritage & Fish Markets", "Busan · Haeundae Beachfront",
            "Gamcheon Culture Village → Jagalchi Fish Market → Nampo-dong & BIFF Square",
            "Pastel Hillside Alleys & Korea's Largest Marine Market",
            [
                {"time": "09:30–12:30", "title": "Gamcheon Culture Village Walk", "detail": "Wander terraced hillside alleys painted in pastel hues, find quirky art installations, and photograph the famous Little Prince and Desert Fox statue overlooking the sea.", "logistics": "Toseong Station Line 1 Exit 6, then Local Bus Saha 1-1 or taxi up hill."},
                {"time": "13:00–15:00", "title": "Jagalchi Fish Market Feast", "detail": "Explore Korea's biggest seafood market; select fresh seasonal sashimi, snow crab, or grilled fish and dine in the second-floor market hall.", "logistics": "Jagalchi Station Line 1 Exit 10."},
                {"time": "15:15–17:30", "title": "BIFF Square & Bupyeong Kkangtong Market", "detail": "Walk the Busan International Film Festival handprint square, taste famous seed hotteok, and browse traditional retro market alleys.", "logistics": "Jagalchi / Nampo Station walking street."},
                {"time": "18:00–19:30", "title": "Yongdusan Park & Busan Tower Night View", "detail": "Ride the outdoor covered escalator up to Yongdusan Park to view twinkling harbor lights from Busan Diamond Tower.", "logistics": "Nampo Station Exit 1 / 7."},
                {"time": "20:00–21:30", "title": "Nampo-dong Dwaeji Gukbap Dinner", "detail": "Enjoy boiling pork bone soup with tender pork slices, chives, salted shrimp, and rice.", "logistics": "Nampo-dong / Choryang soup alley."}
            ],
            [
                {"label": "Old Busan Heritage", "text": "Reveals the resilient history of wartime refugees in Gamcheon and the vibrant maritime spirit of Jagalchi."},
                {"label": "Food Immersion", "text": "Tasting Jagalchi fresh fish and BIFF street snacks is essential Busan culinary culture."}
            ],
            "Lunch: Jagalchi Market 2F fresh flounder sashimi & spicy maeuntang fish soup. Dinner: Traditional Busan Dwaeji Gukbap (rich pork soup).",
            "Gamcheon village maps available at tourist center for ₩2,000 (includes stamp rally).",
            "Gamcheon entry free; Busan Tower observation deck ₩12,000.",
            "Gamcheon is a living residential village; keep noise low and do not enter private courtyards.",
            "Jagalchi 7-story indoor market building and Nampo Lotte Department store offer full indoor comfort."
        ),
        # Day 16: Nov 16
        make_day(15, "Busan", "Marine Cliffs & Cable Cars", "Busan · Haeundae Beachfront",
            "Taejongdae Ocean Cliff Park → Songdo Marine Cable Car & Skywalk",
            "Dramatic Coastal Headlands & Over-Water Gondolas",
            [
                {"time": "09:30–12:30", "title": "Taejongdae Resort Park & Danubi Train", "detail": "Ride the Danubi park train through dense evergreen forests out to Yeongdo lighthouse and sheer sea cliffs overlooking the Korea Strait.", "logistics": "Bus 88/101 from Busan Station or 30-min taxi from hotel."},
                {"time": "12:45–14:15", "title": "Yeongdo Coastal Seafood Lunch", "detail": "Enjoy fresh sea squirt bibimbap, abalone porridge, or grilled mackerel near Taejongdae pier.", "logistics": "Taejongdae entrance restaurant village."},
                {"time": "14:45–17:30", "title": "Songdo Marine Cable Car (Air Cruise) & Cloud Trails", "detail": "Glide across the open sea in a glass-bottom Crystal Cabin gondola between Songdo Beach and Amnam Park, then walk the curved Songdo Cloud Trails skywalk over the ocean.", "logistics": "Songdo Bay Station; bus or taxi from Yeongdo."},
                {"time": "18:00–19:30", "title": "Huinnyeoul Culture Village Sunset", "detail": "Stroll the narrow coastal cliffside walkway on Yeongdo, enjoying illuminated sea tunnels and cafes with panoramic ocean views.", "logistics": "Yeongdo coastal bus."},
                {"time": "20:00–21:30", "title": "Choryang Bulgogi / Seafood Feast", "detail": "Savor marinated beef bulgogi or spicy octopus stir-fry (nakji bokkeum) in central Busan.", "logistics": "Choryang / Seomyeon dining district."}
            ],
            [
                {"label": "Dramatic Geological Wonders", "text": "Taejongdae and Songdo showcase Busan's most impressive coastal cliff and wave topography."},
                {"label": "Ocean Gondola Experience", "text": "The glass-bottom cable car gives breathtaking aerial perspectives of incoming cargo ships and islands."}
            ],
            "Lunch: Taejongdae fresh abalone porridge (jeonbok-juk). Dinner: Gaemijip spicy octopus, pork, and tripe stir-fry (Nakgobsai).",
            "Taejongdae Danubi train runs every 20 mins (₩4,000); closed if extreme heavy rain.",
            "Songdo Cable Car Crystal Cabin ₩22,000 round-trip.",
            "Wind can be brisk on ocean cliffs; windbreaker jacket strongly recommended.",
            "Songdo Marine Cable Car operates in normal rain; Amnam Park indoor cafes provide shelter."
        ),
        # Day 17: Nov 17
        make_day(16, "Busan", "Thermal Relaxation & Modern Cinema", "Busan · Haeundae Beachfront",
            "Centum City Spa Land Thermal Baths → Busan Cinema Center → Shinsegae Department Store",
            "World-Class Jjimjilbang Saunas & Architectural Icons",
            [
                {"time": "09:30–13:30", "title": "Spa Land Centum City (Luxury Korean Bathhouse)", "detail": "Immerse in 18 natural thermal spring pools drawn from 1,000m underground, explore 13 themed aesthetic sauna rooms (Himalayan salt, Roman steam, Finnish sauna), and relax in ergonomic heated loungers.", "logistics": "Centum City Station Line 2 direct mall basement connection."},
                {"time": "13:30–15:00", "title": "Shinsegae Centum City Gourmet Food Hall Lunch", "detail": "Dine in the world's largest department store food emporium, sampling gourmet Korean delicacies, artisan noodles, and dessert.", "logistics": "Shinsegae Centum City B1."},
                {"time": "15:15–17:30", "title": "Busan Cinema Center (BIFF Venue)", "detail": "Admire the Guinness World Record cantilevered LED roof structure, home to the prestigious Busan International Film Festival, and visit cinema exhibitions.", "logistics": "5-minute walk from Shinsegae Mall."},
                {"time": "18:00–20:00", "title": "Marine City Sunset Walk & The Bay 101", "detail": "Photograph the gleaming glass skyscraper reflections of Marine City and relax at The Bay 101 open-air deck.", "logistics": "Dongbaek Station Line 2 Exit 1."},
                {"time": "20:30–22:00", "title": "Gourmet Korean Fried Chicken & Draft Beer (Chimaek)", "detail": "Celebrate with crispy golden Korean fried chicken, sweet garlic glaze, and local Busan craft beer.", "logistics": "Haeundae Gunam-ro avenue."}
            ],
            [
                {"label": "Mid-Trip Physical Rejuvenation", "text": "A full 4-hour wellness soak at Spa Land relieves all accumulated travel fatigue."},
                {"label": "Weather-Proof Comfort", "text": "All major daytime facilities are connected indoors at Centum City."}
            ],
            "Lunch: Shinsegae Centum City Food Hall (gourmet cold noodles or Hanwoo bibimbap). Dinner: The Bay 101 fish & chips / Haeundae artisanal Korean fried chicken.",
            "Spa Land standard pass includes 4 hours of access (approx. ₩20,000–₩23,000).",
            "Spa Land entry ~₩23,000; Cinema Center free exterior.",
            "Spa Land does not admit children under age 7; quiet relaxation etiquette expected.",
            "This entire day is 100% weather-proof with indoor air-conditioned connections."
        ),
        # Day 18: Nov 18
        make_day(17, "Busan", "Mountain Sanctuaries & Craft", "Busan · Haeundae Beachfront",
            "Beomeosa Mountain Temple → Geumjeongsanseong Fortress → F1963 Cultural Hub",
            "Ancient Buddhist Sanctuaries & Industrial Art Spaces",
            [
                {"time": "09:30–12:30", "title": "Beomeosa Temple (Temple of the Nirvana Fish)", "detail": "Ascend Mount Geumjeong to tour one of Korea's premier Buddhist headquarters, founded in 678 AD, surrounded by tranquil bamboo and wisteria groves.", "logistics": "Beomeosa Station Line 1 Exit 5, then Bus 90 up mountain."},
                {"time": "12:45–14:15", "title": "Dongnae Mountain Pajeon Lunch", "detail": "Savor authentic Dongnae Pajeon: thick scallion pancakes loaded with fresh squid, clams, oysters, and beef, paired with local Geumjeongsanseong Makgeolli.", "logistics": "Sanseong village / Dongnae district."},
                {"time": "14:45–17:30", "title": "F1963 Cultural Arts Complex & Terarosa Coffee", "detail": "Explore a visionary former steel wire factory transformed into an eco-friendly cultural space with Yes24 giant book store, Kukje Gallery art exhibits, and bamboo garden.", "logistics": "Mangmi Station Line 3 or 15-min taxi from Centum City."},
                {"time": "18:00–20:30", "title": "Millak Waterfront Raw Fish Feast", "detail": "Enjoy sliced flounder and yellowtail sashimi overlooking the illuminated Gwangan Bridge from high-floor waterfront restaurants.", "logistics": "Millak Raw Fish Town."}
            ],
            [
                {"label": "Mountain & Industrial Heritage", "text": "Contrasts a 1,300-year-old Buddhist mountain haven with 21st-century industrial art revitalization."},
                {"label": "Artisanal Cuisine", "text": "Dongnae Pajeon is historically registered as Busan Local Intangible Cultural Asset #1."}
            ],
            "Lunch: Dongnae Halmae Pajeon (historic scallion pancake with rice wine). Dinner: Millak Waterfront raw seasonal sashimi and spicy maeuntang.",
            "Beomeosa Temple entry is free; open year-round.",
            "Temple free; Makgeolli + Pajeon lunch ~₩20,000 per person.",
            "Bus 90 road winds up the mountain; hold handrails if standing.",
            "F1963 indoor exhibitions, Yes24 bookstore, and Terarosa coffee lounge are completely covered."
        ),
        # Day 19: Nov 19
        make_day(18, "Busan", "Low-Stakes Autumn Coastal Stroll (CSAT Day)", "Busan · Haeundae Beachfront",
            "Igidae Coastal Cliff Walkway → Oryukdo Skywalk → Relaxed Evening Cafe",
            "Peaceful Waves, Skywalks & Gentle Rhythm (CSAT / Suneung Day)",
            [
                {"time": "10:00–12:30", "title": "Igidae Coastal Cliff Walkway", "detail": "Walk the scenic coastal trail cut into volcanic cliff faces, offering pristine ocean views with the modern Busan skyline across the bay.", "logistics": "Kyungsung Univ./Pukyong Univ. Station Line 2, then Bus 20/22/39 or taxi."},
                {"time": "12:45–14:00", "title": "Oryukdo Island View Lunch", "detail": "Enjoy warm seafood noodle soup (haemul kalguksu) or grilled fish set at Oryukdo cliffside pavilion.", "logistics": "Oryukdo Skywalk tourist plaza."},
                {"time": "14:15–16:00", "title": "Oryukdo Glass Skywalk", "detail": "Step out onto the U-shaped transparent glass skywalk suspended 35 meters above roaring ocean waves dividing the East and South Seas.", "logistics": "Free admission; shoe covers provided at gate."},
                {"time": "16:30–19:00", "title": "Haeundae Sunset Cafe & Rest", "detail": "Relax at an ocean-view cafe on Dalmaji Hill or Haeundae beachfront, reflecting on 7 wonderful Busan nights.", "logistics": "Dalmaji-gil cafe road."},
                {"time": "19:30–21:30", "title": "Busan Farewell Feast: Hanwoo Beef Barbecue", "detail": "Celebrate the final night in Busan with premium charcoal-grilled Korean Hanwoo beef tenderloin.", "logistics": "Haeundae Somunnan Amso Galbi-jip or premier local steakhouse."}
            ],
            [
                {"label": "CSAT Low-Stakes Alignment", "text": "Nov 19 is Korea's national CSAT exam day. Keeping this day localized along the coast avoids urban traffic hold zones."},
                {"label": "Farewell Coastal Panorama", "text": "The Igidae-to-Oryukdo ridge provides one of Korea's most breathtaking coastal walking memories."}
            ],
            [
                "Lunch: Oryukdo Haemul Kalguksu (seafood noodle soup). Dinner: Haeundae Somunnan Amso Galbi (marinated beef short ribs with potato noodles).",
            ],
            "Oryukdo Skywalk open 09:00–18:00; admission is free.",
            "Skywalk is free; Final Busan Hanwoo BBQ dinner ~₩45,000–₩60,000 per person.",
            "Oryukdo Skywalk closes temporarily during strong winds or rain for visitor safety.",
            "Centum City and Haeundae indoor cafes offer relaxing sea-view indoor alternatives."
        ),
        # Day 20: Nov 20
        make_day(19, "Seoul", "Return Transit", "Seoul · Seoul Station / Myeongdong",
            "Morning KTX Busan to Seoul (2h15m) → Seoul Station Check-in → Euljiro Retro Alleys",
            "Capital Return: Seamless Rail Travel & Departure Buffer",
            [
                {"time": "09:30–10:15", "title": "Busan Station Departure", "detail": "Check out of Haeundae hotel, take taxi or Metro Line 2/1 to Busan Station, and board direct KTX train.", "logistics": "Board train 10 minutes prior to departure."},
                {"time": "10:30–12:45", "title": "KTX High-Speed Rail to Seoul", "detail": "Comfortable 2-hour 15-minute high-speed journey back to the capital.", "logistics": "Direct arrival inside Seoul Station concourse."},
                {"time": "13:00–14:30", "title": "Seoul Station Check-in & Lunch", "detail": "Check into hotel directly at Seoul Station (e.g. Four Points Josun or Nine Tree Myeongdong) and enjoy warm bibimbap or beef soup.", "logistics": "Drop bags; zero long subway commute needed."},
                {"time": "15:00–18:00", "title": "Euljiro 'Hipjiro' Lighting & Print Alleys", "detail": "Explore the vibrant collision of traditional industrial workshops and secret third-floor coffee lofts and wine bars.", "logistics": "Euljiro 3-ga Station Line 2/3."},
                {"time": "18:30–21:00", "title": "Euljiro Nogari Alley & Korean Draft Beer", "detail": "Experience Korea's iconic outdoor beer alley tradition with grilled dried pollack (nogari), garlic fried chicken, and ice-cold draft beer.", "logistics": "Euljiro 3-ga Station Exit 3/4."}
            ],
            [
                {"label": "Strategic Departure Buffer", "text": "Returning to Seoul on Friday eliminates all risk of KTX weekend disruption before Sunday flight."},
                {"label": "Seoul Station Anchor", "text": "Direct doorstep proximity to the AREX airport express line guarantees effortless Sunday transit."}
            ],
            "Lunch: Seoul Station concourse gourmet dining or KTX Dosirak bento. Dinner: Euljiro Nogari alley garlic fried chicken and grilled pollack.",
            "Book KTX Busan→Seoul on Korail app 30 days in advance.",
            "KTX ticket ~₩59,800 per person.",
            "Friday afternoon KTX trains fill up quickly; secure reserved seats early.",
            "Lotte Mart at Seoul Station offers covered shopping right at your doorstep."
        ),
        # Day 21: Nov 21
        make_day(20, "Seoul", "Souvenirs & Farewell", "Seoul · Seoul Station / Myeongdong",
            "Namdaemun Market → Seoul Station Lotte Mart (Tax-Free Food Gifts) → Grand Farewell Banquet",
            "Final Souvenir Curations & Celebration Feast",
            [
                {"time": "09:30–12:30", "title": "Namdaemun Market & Kalguksu Alley", "detail": "Browse Korea's oldest traditional market for ceramics, tea accessories, dried seaweed, and handmade kitchenware, enjoying hot kalguksu.", "logistics": "Hoehyeon Station Line 4 Exit 5."},
                {"time": "13:00–15:30", "title": "Seoul Station Lotte Mart Mega-Store", "detail": "Curate gourmet food gifts: premium Korean seaweed (gim), market snacks, red pepper paste (gochujang), and instant noodles with instant tax refund.", "logistics": "Immediate tax refund counter on 2F with passport."},
                {"time": "16:00–18:00", "title": "Afternoon Packing & Luggage Weighing", "detail": "Return to hotel room, organize souvenirs, check luggage weight against airline baggage allowance, and complete airline online check-in.", "logistics": "Hotel front desk provides digital luggage scale."},
                {"time": "18:30–21:00", "title": "Grand Farewell Korean BBQ Feast", "detail": "Celebrate the 21-night journey with premium Korean Hanwoo beef barbecue and aged kimchi stew in central Seoul.", "logistics": "Myeongdong / Gwanghwamun dining room."}
            ],
            [
                {"label": "Departure Prep", "text": "All shopping and packing completed by Saturday night ensures Sunday morning is 100% calm and stress-free."},
                {"label": "Immediate Tax Refund", "text": "Handling tax refunds at Lotte Mart saves 30+ minutes at airport customs lines."}
            ],
            "Lunch: Namdaemun Kalguksu Alley (includes free cold bibim naengmyeon bowl). Dinner: Premium Hanwoo charcoal BBQ banquet.",
            "Complete online airline check-in 24 hours prior; select seats and enter passport numbers.",
            "Souvenirs budget ~₩50,000–₩100,000; Farewell dinner ~₩45,000 per person.",
            "Keep tax refund receipts, passport, and critical items in carry-on bag.",
            "Shinsegae Main Department Store underground tunnels connect Namdaemun to Myeongdong."
        ),
        # Day 22: Nov 22
        make_day(21, "Seoul", "Departure", "Departure · Incheon International Airport",
            "AREX Non-Stop Express to ICN (43 mins) → Check-in & Security → Flight at 13:00",
            "Calm & Seamless Flight Departure",
            [
                {"time": "08:30–09:15", "title": "Hotel Checkout & City Airport Check-in (Optional)", "detail": "Check out of Seoul Station hotel. If flying Korean Air/Asiana, check in bags at Seoul Station City Airport Terminal.", "logistics": "B2 of Seoul Station."},
                {"time": "09:30–10:15", "title": "AREX Non-Stop Express Train to ICN", "detail": "Board the direct express train to Incheon Airport Terminal 1 (43 mins) or Terminal 2 (51 mins).", "logistics": "Reserved seats with dedicated luggage racks."},
                {"time": "10:15–12:15", "title": "Airport Customs, Security & Tax Refund", "detail": "Drop remaining bags, clear security, process any airport tax-refund machines, and reach departure gate by 12:20.", "logistics": "Target 3 hours prior to 13:00 international departure."},
                {"time": "12:30–13:00", "title": "Boarding & Takeoff", "detail": "Board aircraft for the return flight home with unforgettable memories of Korea.", "logistics": "Gates close 15 minutes before scheduled departure."}
            ],
            [
                {"label": "Logistics Perfection", "text": "Direct AREX express from hotel doorstep guarantees predictable 43-minute airport transit."},
                {"label": "Zero Rush", "text": "Arriving at 10:15 leaves ample time for customs, tax refunds, duty-free pickup, and a relaxed pre-flight meal."}
            ],
            "Breakfast: Hotel café or airport lounge / Korean Food Street at ICN Terminal (bibimbap/soup).",
            "Verify terminal (T1 vs T2) based on airline ticket before boarding AREX.",
            "AREX Express ticket ₩11,000 per person.",
            "Terminal 2 is 8 minutes further on the AREX line than Terminal 1; check your terminal code.",
            "If AREX express sells out, AREX All-Stop commuter train departs every 6–10 minutes."
        )
    ]

    scorecard = [
        {"label": "Heritage Depth", "value": "5/5", "tone": "good"},
        {"label": "Transit Simplicity", "value": "4/5", "tone": "good"},
        {"label": "Bakery & Science", "value": "5/5", "tone": "good"},
        {"label": "Coastal Scenery", "value": "5/5", "tone": "good"}
    ]

    return {
        "id": "seoul-daejeon-busan-classic",
        "shortTitle": "Seoul · Daejeon · Busan (Classic Explorer)",
        "title": "Capital, Science Hub & Coastal Panoramas (Classic Explorer)",
        "routeLabel": "Seoul (7N) → Daejeon (5N) → Busan (7N) → Seoul (2N)",
        "badge": "Balanced Heritage & City Depth",
        "bestFor": "First-time travelers seeking a balanced, comprehensive introduction to Korea's imperial palaces, cutting-edge science and bakery culture in Daejeon, and dynamic coastal Busan highlights.",
        "decisionSummary": "The quintessential three-city route balancing royal history, high-tech research hubs, and marine scenery with beginner-friendly pacing.",
        "recommendation": "Choose this route if you want the classic South Korea experience with a smooth, structured pace and rich regional variety.",
        "tradeoff": "Daejeon requires a bit more transit time between attractions than Cheonan, and you cover substantial walking daily across three distinct major cities.",
        "scorecard": scorecard,
        "bases": get_sdb_common_bases(),
        "transfers": get_sdb_common_transfers(),
        "budgetScenarios": get_sdb_budget_scenarios(),
        "bookingPriorities": get_sdb_booking_priorities(),
        "days": days
    }
