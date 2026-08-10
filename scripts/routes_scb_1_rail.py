#!/usr/bin/env python3
"""Route Blueprint: Seoul · Cheonan · Busan (Scenic Rail Corridor & Independence Heritage)."""

from scripts.generate_all_itineraries import make_day
from scripts.itinerary_builder_scb import (
    get_scb_common_bases,
    get_scb_common_transfers,
    get_scb_budget_scenarios,
    get_scb_booking_priorities
)

def get_scb_rail():
    days = [
        # Day 1: Nov 1
        make_day(0, "Seoul", "Arrival", "Seoul · Myeongdong / Seoul Station edge",
            "ICN arrival at 21:00 → late transfer → hotel check-in → restful sleep",
            "Smooth Late Arrival & Station-Adjacent Base Check-in",
            [
                {"time": "21:00–22:15", "title": "ICN Arrival & Border Clearance", "detail": "Clear immigration smoothly, collect checked luggage, and pick up pre-arranged transportation card and eSIM.", "logistics": "Terminal 1 or 2."},
                {"time": "22:30–23:45", "title": "Direct Transfer to Seoul Station Area", "detail": "Board Airport Limousine Bus or official taxi directly to Myeongdong / Seoul Station hotel.", "logistics": "Direct drop-off minimizes late-night subway transfers."},
                {"time": "23:45–00:30", "title": "Hotel Check-in & Rest", "detail": "Check into hotel room, unpack essentials, hydrate, and get deep sleep.", "logistics": "Notify hotel in advance of late arrival."}
            ],
            [
                {"label": "Rail Anchor", "text": "Positioning at Seoul Station guarantees seamless train departures throughout the trip."},
                {"label": "Arrival Protocol", "text": "Save energy for the comprehensive royal palace itinerary starting tomorrow morning."}
            ],
            "Light convenience store snack (CU / GS25 warm samgak kimbap or banana milk).",
            "Confirm late check-in with hotel in writing.",
            "Limousine Bus ~₩17,000.",
            "Late night jetlag; keep bedtime calm without heavy alcohol.",
            "Official airport taxi stands are available outside terminal arrivals hall."
        ),
        # Day 2: Nov 2
        make_day(1, "Seoul", "Royal Heritage", "Seoul · Myeongdong / Seoul Station edge",
            "Gyeongbokgung Palace Guard Changing → Bukchon Hanok Village → Insadong Teahouses",
            "Imperial Grandeur & Traditional Hanok Quarters",
            [
                {"time": "09:30–11:30", "title": "Gyeongbokgung Royal Palace", "detail": "Witness the Royal Guard Changing Ceremony at Gwanghwamun Gate (10:00 AM) and tour Geunjeongjeon throne hall and Gyeonghoeru Pavilion.", "logistics": "Gyeongbokgung Station Line 3 Exit 5."},
                {"time": "11:45–13:15", "title": "Samcheong-dong Traditional Lunch", "detail": "Savor handmade potato-dough sujebi or bulgogi along leafy Samcheong-dong.", "logistics": "Short walk east from palace."},
                {"time": "13:30–15:30", "title": "Bukchon Hanok Village Walk", "detail": "Wander preserved Joseon residential stone alleys with traditional tile roofs overlooking modern Seoul.", "logistics": "Quiet residential zone etiquette."},
                {"time": "15:45–18:00", "title": "Insadong Antique Street & Ssamzigil", "detail": "Browse traditional calligraphy, celadon crafts, and sip roasted jujube tea in a wooden hanok teahouse.", "logistics": "Anguk Station Line 3 Exit 6."},
                {"time": "18:30–20:30", "title": "Welcome Korean BBQ Dinner", "detail": "Feast on charcoal-grilled pork belly with fresh lettuce wraps and doenjang stew.", "logistics": "Jongno dining quarter."}
            ],
            [
                {"label": "Clustered Heritage", "text": "Gyeongbokgung, Bukchon, and Insadong are contiguous northern districts requiring zero subway hops during the day."},
                {"label": "Autumn Ambience", "text": "Early November offers golden ginkgo foliage along Samcheong-dong and palace stone walls."}
            ],
            "Lunch: Samcheong-dong Sujebi (Michelin Bib Gourmand). Dinner: Jongno charcoal-grilled pork belly with soybean stew.",
            "Palace closed on Tuesdays; entry ₩3,000 (free if wearing hanbok).",
            "Palace entry ₩3,000; meals ~₩35,000 per person.",
            "Bukchon is a quiet residential area; quiet hours strictly enforced after 17:00.",
            "National Folk Museum of Korea inside palace grounds provides covered indoor shelter."
        ),
        # Day 3: Nov 3
        make_day(2, "Seoul", "UNESCO Gardens & Markets", "Seoul · Myeongdong / Seoul Station edge",
            "Changdeokgung Secret Garden (Huwon) → Ikseon-dong Hanok Cafes → Gwangjang Market",
            "Secret Royal Landscapes & Street Food Feasts",
            [
                {"time": "09:30–12:00", "title": "Changdeokgung Palace & Secret Garden (Huwon)", "detail": "Explore UNESCO World Heritage Changdeokgung and take a guided walking tour through the serene autumn Secret Garden pavilions.", "logistics": "Anguk Station Line 3 Exit 3."},
                {"time": "12:15–14:00", "title": "Ikseon-dong Hanok Alleys & Lunch", "detail": "Discover retro-modern hanok alleys filled with artisanal bakeries and fusion cafes.", "logistics": "Jongno 3-ga Station Exit 4."},
                {"time": "14:30–17:00", "title": "Jongmyo Royal Ancestral Shrine & Cheonggyecheon", "detail": "Walk the solemn grounds of Jongmyo Shrine and follow the tranquil Cheonggyecheon Stream pedestrian path.", "logistics": "Walk east from Ikseon-dong."},
                {"time": "17:30–20:30", "title": "Gwangjang Traditional Food Market", "detail": "Experience Korea's oldest market feast: crispy bindaetteok (mung bean pancake), mayak gimbap, and beef tartare (yukhoe).", "logistics": "Jongno 5-ga Station Line 1 Exit 8."}
            ],
            [
                {"label": "Secret Garden Timing", "text": "Huwon requires advance timed reservation; early November autumn foliage here is world-famous."},
                {"label": "Seamless Pedestrian Path", "text": "Connecting Changdeokgung through Ikseon-dong to Gwangjang Market is a straight, flat walk."}
            ],
            "Lunch: Ikseon-dong hanok cafe dining. Dinner: Gwangjang Market bindaetteok, mayak gimbap, and makgeolli.",
            "Book Changdeokgung Huwon Secret Garden ticket online 6 days in advance at 10:00 AM KST.",
            "Palace + Garden entry ₩8,000; Market food ~₩20,000 per person.",
            "Gwangjang market food stalls are cash/T-money preferred.",
            "Gwangjang covered market roof shields from any autumn rain."
        ),
        # Day 4: Nov 4
        make_day(3, "Seoul", "National Treasures & Heights", "Seoul · Myeongdong / Seoul Station edge",
            "National Museum of Korea → War Memorial of Korea → N Seoul Tower Sunset",
            "Masterpiece Artifacts & Mountain Skyline Panoramas",
            [
                {"time": "09:30–12:30", "title": "National Museum of Korea", "detail": "Marvel at Korean national treasures including the Pensive Bodhisattva in the Room of Quiet Contemplation and Ten-Story Gyeongcheonsa Pagoda.", "logistics": "Ichon Station Line 4 direct underground walkway."},
                {"time": "12:45–14:15", "title": "Ichon-dong Gourmet Lunch", "detail": "Enjoy lunch in Little Tokyo Ichon-dong or museum garden cafe.", "logistics": "Short walk from museum park."},
                {"time": "14:30–16:00", "title": "War Memorial of Korea", "detail": "Tour expansive outdoor military aircraft exhibitions and solemn indoor memorial halls.", "logistics": "Samgakji Station Line 4/6 Exit 12."},
                {"time": "16:30–19:30", "title": "N Seoul Tower & Namsan Sunset", "detail": "Ascend Namsan via scenic cable car or shuttle bus to enjoy 360-degree sunset views over Seoul.", "logistics": "Myeongdong Namsan Cable Car or Yellow Shuttle Bus #01."},
                {"time": "20:00–21:30", "title": "Myeongdong Kyoja Dumpling Dinner", "detail": "Savor Michelin Bib Gourmand handmade pork dumplings and rich chicken broth kalguksu with spicy garlic kimchi.", "logistics": "Myeongdong Station Line 4 Exit 8."}
            ],
            [
                {"label": "Cultural Depth", "text": "National Museum provides essential historical context before traveling to regional Joseon and Silla cities."},
                {"label": "Sunset Alignment", "text": "Reaching N Seoul Tower by 16:30 captures day, golden hour, and shimmering city lights."}
            ],
            "Lunch: Ichon Japanese katsu or Museum Garden Cafe. Dinner: Myeongdong Kyoja (handmade kalguksu and steamed mandu).",
            "National Museum permanent galleries are free admission.",
            "N Seoul Tower observatory ₩21,000; Cable car round-trip ₩15,000.",
            "Cable car queue can be busy on clear evenings; shuttle bus 01 is faster alternative.",
            "National Museum of Korea is fully indoor and heated."
        ),
        # Day 5: Nov 5
        make_day(4, "Seoul", "Historic Rail Excursion to Suwon", "Seoul · Myeongdong / Seoul Station edge",
            "Suwon Hwaseong Fortress Rail Excursion (KTX / Line 1) → Suwon King Galbi Lunch",
            "UNESCO Fortress Walls, Archery & King Galbi",
            [
                {"time": "09:00–09:45", "title": "Rail Excursion: Seoul Station to Suwon Station", "detail": "Board direct KTX (30 mins) or rapid commuter train down the historic Gyeongbu line to Suwon.", "logistics": "Seoul Station Platform."},
                {"time": "10:00–13:00", "title": "Suwon Hwaseong Fortress (UNESCO World Heritage)", "detail": "Walk the 5.7km stone fortress battlements, secret gates (Ammun), and watchtowers built in 1796 by King Jeongjo, trying traditional Korean archery (Gukgung) at Yeonmudae.", "logistics": "Suwon Station + Bus 11/13 to Paldalmun or Hwaseomun."},
                {"time": "13:15–15:00", "title": "Famous Suwon Wang Galbi (King's Beef Ribs) Feast", "detail": "Feast on Suwon's legendary massive marinated beef short ribs grilled over charcoal.", "logistics": "Yeonpodang / Bonsuwon Galbi near fortress."},
                {"time": "15:30–17:00", "title": "Hwaseong Haenggung Temporary Palace", "detail": "Tour the royal detached palace where King Jeongjo stayed during ancestral visits.", "logistics": "Central fortress plaza."},
                {"time": "17:30–18:15", "title": "Return Rail to Seoul Station", "detail": "Smooth 30-minute train ride back to central Seoul.", "logistics": "Suwon Station to Seoul Station."},
                {"time": "19:00–21:00", "title": "Seoul Station Rest & Dinner", "detail": "Relax and dine near Seoul Station base.", "logistics": "Seoul Station concourse."}
            ],
            [
                {"label": "Rail Mastery Excursion", "text": "Demonstrates the power of Korea's rail network to explore a premier UNESCO World Heritage fortress just 30 minutes from Seoul."},
                {"label": "Epicurean Suwon Beef", "text": "Suwon Wang Galbi is internationally renowned for its colossal size and sweet fruit-and-garlic marinade."}
            ],
            "Lunch: Suwon Wang Galbi (King beef short ribs grilled over charcoal). Dinner: Seoul Station warm bibimbap or noodle soup.",
            "Suwon Hwaseong fortress open year-round; archery experience ₩2,000.",
            "Train round-trip ~₩16,000; Suwon Wang Galbi lunch ~₩45,000 per person.",
            "Wear walking shoes for walking fortress stone slopes.",
            "Hwaseong Haenggung exhibition halls and Suwon Museum provide indoor shelter."
        ),
        # Day 6: Nov 6
        make_day(5, "Seoul", "Indie Culture & Youth Hubs", "Seoul · Myeongdong / Seoul Station edge",
            "Hongdae Shopping & Indie Culture → Gyeongui Line Forest Park → Mapo Charcoal BBQ",
            "Creative Greenways, Street Buskers & Charcoal Galbi",
            [
                {"time": "10:00–12:30", "title": "Gyeongui Line Forest Park Stroll", "detail": "Walk the transformed former railway corridor lined with boutique shops, craft bakeries, and autumn trees.", "logistics": "Hongik Univ. Station Line 2 / AREX Exit 3."},
                {"time": "12:30–14:00", "title": "Yeonnam-dong Trendy Dining Lunch", "detail": "Enjoy artisanal handmade pasta, Korean rice bowls, or fresh bakery treats in trendy Yeonnam-dong.", "logistics": "Yeonnam cafe street."},
                {"time": "14:15–17:00", "title": "Hongdae Shopping & Indie Arts Street", "detail": "Browse unique Korean streetwear, stationary shops (Object, KT&G Sangsangmadang), and photo studios.", "logistics": "Hongdae Pedestrian Walking Street."},
                {"time": "17:15–19:00", "title": "Hongdae Live Street Busking", "detail": "Watch talented young K-pop dancers, acoustic musicians, and indie performers on Hongdae busking street.", "logistics": "Hongik Univ. Station Exit 8/9 area."},
                {"time": "19:30–21:30", "title": "Mapo Charcoal Galbi Barbecue Feast", "detail": "Feast on marinated pork ribs grilled over charcoal accompanied by refreshing cold dongchimi broth.", "logistics": "Mapo Station Line 5 BBQ Alley."}
            ],
            [
                {"label": "Youth Energy", "text": "Hongdae comes alive in the afternoon and evening with creative youth culture and music."},
                {"label": "Walkable Greenway", "text": "Forest park provides a calming pedestrian buffer between bustling commercial streets."}
            ],
            "Lunch: Yeonnam-dong Korean fusion bibimbap or burger. Dinner: Mapo Original Galbi pork ribs.",
            "Most retail and indie shops in Hongdae open around 11:00 AM.",
            "Budget ~₩40,000 per person for dining and dessert cafes.",
            "Evening crowds in Hongdae get dense; keep valuables secure.",
            "KT&G Sangsangmadang offers multi-floor indoor art gallery, cinema, and design shop."
        ),
        # Day 7: Nov 7
        make_day(6, "Seoul", "Gangnam & Rail Departure Prep", "Seoul · Myeongdong / Seoul Station edge",
            "Starfield COEX Library → Bongeunsa Millennium Temple → Sunday KTX to Cheonan Prep",
            "Towering Libraries, Ancient Temples & Rail Preparation",
            [
                {"time": "10:00–12:30", "title": "Starfield COEX Library & Mega Mall", "detail": "Photograph the magnificent 13-meter tall book towers at Starfield Library and browse Asia's largest underground shopping complex.", "logistics": "Samseong Station Line 2 Exit 6 or Bongeunsa Station Line 9 Exit 7."},
                {"time": "12:30–14:00", "title": "Parnas Mall Gourmet Lunch", "detail": "Enjoy Korean modern beef soup (gomtang) or royal hot pot in the lower level gourmet arcade.", "logistics": "Directly connected to COEX Mall."},
                {"time": "14:15–16:00", "title": "Bongeunsa Buddhist Temple", "detail": "Step across the street into an ancient peaceful temple founded in 794 AD, home to a majestic 23-meter stone Maitreya Buddha.", "logistics": "Bongeunsa Station Line 9 Exit 1."},
                {"time": "16:30–18:30", "title": "Seoul Station Packing & Train Check", "detail": "Return to Seoul Station base, pack luggage for Sunday morning KTX to Cheonan-Asan, and verify seat reservations.", "logistics": "Seoul Station hotel."},
                {"time": "19:00–21:00", "title": "Seoul Station Farewell Korean Stew Dinner", "detail": "Enjoy boiling army base stew (budae jjigae) or bibimbap.", "logistics": "Seoul Station dining lane."}
            ],
            [
                {"label": "Temple & Modernity", "text": "Bongeunsa's ancient wood stands in stunning contrast to Gangnam's glass skyscrapers."},
                {"label": "Lightning Rail Leap Prep", "text": "Packing early ensures a relaxed Sunday morning 35-minute KTX train to Cheonan."}
            ],
            "Lunch: Hadongkwan 80-year Gomtang beef soup at COEX. Dinner: Seoul Station hearty budae jjigae hot pot.",
            "Bongeunsa Temple is free entry; open until 22:00.",
            "Free entry to COEX library and temple; Dinner ~₩20,000 per person.",
            "COEX underground mall is vast; follow overhead color-coded floor lines.",
            "COEX mall is 100% weather-proof and indoor."
        ),
        # Day 8: Nov 8
        make_day(7, "Cheonan", "City Transition & Modern Sculpture", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Morning KTX Seoul to Cheonan-Asan (35 mins) → Arario Sculpture Park (Damien Hirst, Keith Haring) → 1934 Hakhwa Hodu-gwaja",
            "Lightning High-Speed Rail Leap & World-Class Sculpture Plaza",
            [
                {"time": "09:45–10:20", "title": "KTX High-Speed Rail Seoul to Cheonan-Asan", "detail": "Ultra-fast 35-minute high-speed journey from Seoul Station to Cheonan-Asan Station.", "logistics": "Board train at Seoul Station; arrives before you finish a coffee!"},
                {"time": "10:30–12:00", "title": "Hotel Check-in & Base Setup", "detail": "Check into hotel (e.g. Shilla Stay Cheonan or Ramada Encore Cheonan-Asan) and drop bags.", "logistics": "Cheonan-Asan Station / Shinbu-dong base."},
                {"time": "12:15–13:30", "title": "Shinbu-dong Gourmet Lunch", "detail": "Enjoy Korean hand-cut noodles or stone-pot rice in central Cheonan.", "logistics": "Shinbu-dong dining district."},
                {"time": "13:45–16:00", "title": "Arario Sculpture Park Cheonan", "detail": "Walk the world-famous open-air sculpture park featuring colossal original masterpieces: Damien Hirst's 6-meter 'Hymn' and 'Charity', Keith Haring's vibrant bronzes, and Arman's tower of 99 car axles.", "logistics": "Shinbu-dong Arario Plaza."},
                {"time": "16:15–17:30", "title": "1934 Original Hakhwa Hodu-gwaja Bakery", "detail": "Visit Korea's most historic walnut pastry bakery (founded 1934 by Grandmother Sim Bok-sun) to taste freshly baked, steaming hot walnut cakes filled with whole walnut chunks and smooth white/red bean paste.", "logistics": "Cheonan Station / Shinbu-dong branch."},
                {"time": "18:30–21:00", "title": "Cheonan Sizzling Bulgogi & Suyuk Dinner", "detail": "Feast on tender seasoned beef bulgogi with fresh side dishes.", "logistics": "Cheonan central restaurant quarter."}
            ],
            [
                {"label": "Lightning Rail Leap", "text": "At just 35 minutes on the KTX, Cheonan is the most rail-efficient transit stop in South Korea."},
                {"label": "World Art Landmark", "text": "Arario Sculpture Park is one of the few places in Asia exhibiting monumental works by Damien Hirst and Keith Haring in a public urban plaza."}
            ],
            "Lunch: Shinsegae Cheonan gourmet dining. Afternoon: 1934 Hakhwa freshly baked warm Hodu-gwaja walnut pastries. Dinner: Cheonan charcoal-grilled Hanwoo beef bulgogi.",
            "Book KTX Seoul→Cheonan-Asan on Korail app 30 days in advance.",
            "KTX ticket ~₩14,100; Arario sculpture park is free open-air plaza; Hodu-gwaja box ~₩6,000.",
            "Eat Hakhwa Hodu-gwaja while warm from the bakery oven for peak crispness.",
            "Arario Gallery Cheonan and Shinsegae Department Store provide full indoor comfort."
        ),
        # Day 9: Nov 9
        make_day(8, "Cheonan", "National Independence Heritage", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Independence Hall of Korea (Grand Complex & Maple Tree Tunnel) → Autumn Foliage Walk",
            "Vast Monumental Exhibits & Korea's Longest Autumn Maple Tunnel",
            [
                {"time": "09:30–13:30", "title": "Independence Hall of Korea (Exhibition Halls 1–6)", "detail": "Tour Korea's foremost patriotic national monument: the colossal Grand Hall of the Nation (roof tiled with 40,000 copper tiles), the Monument to the Nation, and expansive multimedia exhibits documenting Korean resistance against colonial rule.", "logistics": "Dongnam-gu Mokcheon-eup; City Bus 381/382/383 from Cheonan Station or 20-min taxi."},
                {"time": "13:30–14:45", "title": "Mokcheon Traditional Country Lunch", "detail": "Enjoy hearty country soybean paste stew (doenjang jjigae), acorn jelly, and grilled fish.", "logistics": "Independence Hall restaurant plaza."},
                {"time": "15:00–17:30", "title": "Independence Hall Autumn Maple Tree Tunnel Walk", "detail": "Walk the spectacular 3.2km paved pedestrian path shaded by thousands of crimson and golden maple trees encircling the complex.", "logistics": "Circling trail around Independence Hall."},
                {"time": "18:00–19:30", "title": "Return to Cheonan & Rest", "detail": "Relax at hotel or explore local cafes in Shinbu-dong.", "logistics": "Short taxi or bus return."},
                {"time": "20:00–21:30", "title": "Cheonan Charcoal Pork BBQ Dinner", "detail": "Feast on thick pork neck and steaming kimchi stew.", "logistics": "Shinbu-dong dining lane."}
            ],
            [
                {"label": "National Heritage Monument", "text": "Independence Hall is the emotional and historical epicenter of modern Korean national identity."},
                {"label": "Peak Maple Tunnel", "text": "The 3.2km Maple Tree Tunnel is widely celebrated as one of Korea's most magnificent autumn foliage walks in mid-November."}
            ],
            "Lunch: Mokcheon traditional soybean stew and grilled mackerel. Dinner: Shinbu-dong charcoal-grilled pork barbecue with soybean paste stew.",
            "Independence Hall of Korea is free admission; closed on Mondays (outdoor park grounds remain open).",
            "Independence Hall is free; Taxi ~₩15,000 each way; Dinner ~₩25,000 per person.",
            "The complex is vast (over 1 million pyeong); wear comfortable walking shoes.",
            "All 7 massive exhibition halls are fully indoor and climate-controlled."
        ),
        # Day 10: Nov 10
        make_day(9, "Cheonan", "Patriots & Heritage Blood Sausage", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Yu Gwan-sun Memorial Hall & Aunae Market → Byeongcheon Soondae Street Feast",
            "National Heroes & 50-Year Heritage Blood Sausage Alley",
            [
                {"time": "09:30–12:30", "title": "Yu Gwan-sun Memorial Hall & Historic Shrine", "detail": "Honor 16-year-old independence hero Yu Gwan-sun at her memorial hall, birthplace, and beacon fire site on Maebongsan Mountain, where the March 1st 1919 independence demonstration was ignited.", "logistics": "Dongnam-gu Byeongcheon-myeon; City Bus 400/402 or 25-min taxi."},
                {"time": "12:45–14:30", "title": "Byeongcheon Soondae Alley (Korea's Famous Blood Sausage Capital)", "detail": "Feast on authentic Byeongcheon Soondae Gukbap: tender small intestine stuffed with cellophane noodles, fresh vegetables, and pork blood simmered in rich bone broth, served with steaming sliced soondae and pork cuts.", "logistics": "Byeongcheon Soondae Street (over 20 heritage restaurants)."},
                {"time": "14:45–16:30", "title": "Aunae Traditional Marketplace Walk", "detail": "Stroll the historic marketplace where thousands gathered in 1919 waving national flags, sampling traditional candy and rice crisps.", "logistics": "Byeongcheon marketplace."},
                {"time": "17:00–18:30", "title": "Cheonan Samgeori Park Heritage Walk", "detail": "Walk the scenic willow-lined lake and classical pavilions where Korea's historic Gyeongbu and Honam royal highways intersected.", "logistics": "Cheonan Samgeori Park."},
                {"time": "19:00–21:00", "title": "Cheonan Hanwoo Beef Feast", "detail": "Savor grilled Korean Hanwoo beef tenderloin.", "logistics": "Cheonan central dining district."}
            ],
            [
                {"label": "Sacred Patriotism", "text": "Yu Gwan-sun is often called the Joan of Arc of Korea, inspiring generations with her fearless courage."},
                {"label": "Culinary Heritage Alley", "text": "Byeongcheon Soondae is nationally distinct for its heavy vegetable content and delicate, non-greasy flavor."}
            ],
            "Lunch: Famous Byeongcheon Soondae Gukbap (authentic pork blood sausage soup with assorted meats). Dinner: Cheonan charcoal-grilled Hanwoo beef with doenjang stew.",
            "Yu Gwan-sun Memorial Hall is free admission; open daily.",
            "Memorial Hall free; Soondae lunch ~₩10,000; Dinner ~₩35,000 per person.",
            "Soondae soup is seasoned to taste with salted shrimp (saeujeot) and red pepper paste (dadeagi).",
            "Yu Gwan-sun Memorial Hall and Byeongcheon restaurants are fully indoor."
        ),
        # Day 11: Nov 10
        make_day(10, "Cheonan", "Colossal Buddha & Mountain Forest", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Gakwonsa Temple (Colossal 15-Meter Bronze Buddha) → Taejosan Mountain Trail",
            "Monumental Bronze Statues & Pine Mountain Forests",
            [
                {"time": "09:30–12:30", "title": "Gakwonsa Temple & Grand Bronze Buddha", "detail": "Climb the 203 stone stairs to behold the colossal 15-meter-tall, 60-ton seated Bronze Amita Buddha overlooking Taejosan Mountain, exploring the massive wooden main prayer hall (Daeungbojeon).", "logistics": "Dongnam-gu Anseo-dong; City Bus 24 or 15-min taxi from station."},
                {"time": "12:45–14:15", "title": "Anseo-dong Mountain Village Lunch", "detail": "Enjoy buckwheat cold noodles (makguksu), potato pancakes, and wild mountain herb bibimbap near the temple lake.", "logistics": "Gakwonsa lake restaurant row."},
                {"time": "14:30–17:00", "title": "Taejosan Mountain Pine Forest Walk", "detail": "Walk the shaded pine paths and visit the Taejosan Park sculpture garden and mountain reservoir.", "logistics": "Taejosan park trails."},
                {"time": "17:30–19:00", "title": "Shinbu-dong Shopping & Coffee", "detail": "Relax at a specialty cafe in central Cheonan.", "logistics": "Shinbu-dong."},
                {"time": "19:30–21:30", "title": "Cheonan Charcoal Pork Galbi BBQ Dinner", "detail": "Enjoy sweet soy-marinated pork ribs grilled over hardwood charcoal.", "logistics": "Cheonan dining quarter."}
            ],
            [
                {"label": "Colossal Buddhist Monument", "text": "Gakwonsa's Bronze Buddha is one of the largest outdoor bronze statues in Asia, second only to the Buddha at Todaiji in Japan."},
                {"label": "Autumn Mountain Vista", "text": "Taejosan provides tranquil pine forest trails and panoramic views across the Cheonan valley."}
            ],
            "Lunch: Anseo-dong buckwheat makguksu and potato pancake. Dinner: Charcoal-grilled pork galbi with cold noodles.",
            "Gakwonsa Temple is free admission; open year-round from dawn to dusk.",
            "Temple free; Makguksu lunch ~₩12,000; Dinner ~₩25,000 per person.",
            "Climbing the 203 stairs to the Buddha statue is paved; ramp access also available.",
            "Daeungbojeon hall and temple tea rooms provide indoor shelter."
        ),
        # Day 12: Nov 12
        make_day(11, "Cheonan", "Lake Boardwalks & Rail Departure Prep", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Seongseong Lake Park Boardwalk Sunset → Cheonan Namsan Central Market → KTX to Busan Prep",
            "Wooden Lake Boardwalks, Market Snacks & Rail Preparation",
            [
                {"time": "10:00–12:30", "title": "Seongseong Lake Park & Eco-Boardwalk", "detail": "Walk the scenic wooden boardwalk loop around Seongseong Lake, visiting the bird observatory, reed fields, and modern waterfront cafes.", "logistics": "Seobuk-gu Seongseong-dong; City Bus 5 or 15-min taxi."},
                {"time": "12:45–14:15", "title": "Seongseong Lakefront Cafe & Lunch", "detail": "Enjoy artisanal brunch, pasta, or Korean rice sets overlooking the water.", "logistics": "Seongseong cafe road."},
                {"time": "14:45–17:00", "title": "Cheonan Namsan Central Market Crawl", "detail": "Browse Cheonan's largest traditional covered market, tasting handmade dumplings, knife-cut noodles, hotteok, and picking up regional walnut snacks.", "logistics": "Sajik-dong (walk from Cheonan Station)."},
                {"time": "17:30–19:30", "title": "Hotel Packing & KTX Ticket Verification", "detail": "Pack luggage for Friday morning KTX to coastal Busan and confirm seat assignments.", "logistics": "Hotel room."},
                {"time": "20:00–21:30", "title": "Cheonan Farewell Korean Feast", "detail": "Celebrate 5 nights in Cheonan with rich mushroom beef hot pot (shabu-shabu).", "logistics": "Shinbu-dong / Station area."}
            ],
            [
                {"label": "Lakeside Tranquility", "text": "Seongseong Lake Park provides a modern, serene boardwalk promenade to cap your Cheonan stay."},
                {"label": "Pre-Coastal Preparation", "text": "Packing early guarantees a stress-free Friday morning KTX train directly to Busan."}
            ],
            "Lunch: Seongseong lakefront cafe brunch. Afternoon: Namsan Market handmade dumplings & hotteok. Dinner: Cheonan beef and mushroom hot pot shabu-shabu.",
            "Seongseong Lake Park is open 24/7; admission is free.",
            "Park free; Market snacks ~₩8,000; Dinner ~₩25,000 per person.",
            "Pack primary bags tonight for Friday morning KTX to Busan.",
            "Namsan Central Market is a fully covered weather-proof arcade."
        ),
        # Day 13: Nov 13
        make_day(12, "Busan", "Coastward Rail & Maritime Arrival", "Busan · Haeundae Beachfront",
            "KTX Cheonan-Asan to Busan (1h45m) → Haeundae Check-in → Sunset Beach Walk",
            "Coastward Bound: Direct High-Speed Rail to the Southern Sea",
            [
                {"time": "10:00–11:45", "title": "KTX High-Speed Rail to Busan", "detail": "Smooth 1-hour 45-minute direct high-speed journey from Cheonan-Asan Station to Busan Station on the southern sea.", "logistics": "Direct Gyeongbu high-speed line."},
                {"time": "12:00–13:15", "title": "Busan Station Choryang Milmyeon Lunch", "detail": "Savor authentic cold wheat noodles and steamed king dumplings.", "logistics": "Opposite Busan Station."},
                {"time": "13:45–15:00", "title": "Transfer to Haeundae Beachfront Base", "detail": "Check into Haeundae hotel (e.g. L7 Haeundae or Felix by STX).", "logistics": "Metro Line 2 or taxi across harbor bridge."},
                {"time": "15:30–18:00", "title": "Haeundae Beach Promenade & Dongbaek Island Walk", "detail": "Stroll white sands of Haeundae Beach and follow the wooden coastal boardwalk around pine-forested Dongbaek Island to APEC Nurimaru House.", "logistics": "Paved oceanside walkway."},
                {"time": "18:30–21:00", "title": "Haeundae Traditional Market Seafood Dinner", "detail": "Walk Haeundae market street and feast on fresh grilled seafood hot pot, sea eel, and seed hotteok (ssiat hotteok).", "logistics": "Haeundae Traditional Market."}
            ],
            [
                {"label": "Direct Rail Efficiency", "text": "Direct KTX from Cheonan-Asan arrives in Busan before noon, leaving the full afternoon for coastal exploration."},
                {"label": "Haeundae Anchor", "text": "Staying in Haeundae provides seven nights of oceanfront serenity without hotel moves."}
            ],
            "Lunch: Choryang Milmyeon (cold wheat noodles & giant dumplings). Dinner: Haeundae Market grilled seafood hot pot & ssiat hotteok.",
            "Book KTX Cheonan-Asan→Busan on Korail app 30 days in advance.",
            "KTX ticket ~₩39,200 per person.",
            "Dongbaek Island trail is paved and lighted; Nurimaru APEC House closes at 17:00.",
            "SEA LIFE Busan Aquarium on Haeundae beachfront provides indoor shelter."
        ),
        # Day 14: Nov 14
        make_day(13, "Busan", "Coastal Rails & Seaside Temple", "Busan · Haeundae Beachfront",
            "Haeundae Blueline Sky Capsule to Cheongsapo → Haedong Yonggungsa Temple → Saturday Drones",
            "Scenic Coastal Railway, Seaside Cliff Sanctuaries & Saturday Lights",
            [
                {"time": "09:30–11:30", "title": "Haeundae Blueline Park Sky Capsule (Mipo to Cheongsapo)", "detail": "Ride a private colorful Sky Capsule cabin suspended 10 meters above the sea along coastal cliff tracks.", "logistics": "Mipo Station; book tickets 2 weeks in advance."},
                {"time": "11:30–13:00", "title": "Cheongsapo Twin Lighthouses & Grilled Clam Lunch", "detail": "Photograph red and white lighthouses, walk Daritdol Skywalk, and enjoy fresh grilled clams with butter and cheese.", "logistics": "Cheongsapo restaurant row."},
                {"time": "13:30–16:00", "title": "Haedong Yonggungsa Temple (Temple by the Sea)", "detail": "Visit Korea's dramatic Buddhist temple built directly onto coastal granite rocks above crashing waves.", "logistics": "Bus 181 from Cheongsapo or 15-min taxi."},
                {"time": "16:30–18:30", "title": "Ananti Cove & Coastal Walk", "detail": "Explore luxury ocean promenade and seaside cafes in Gijang.", "logistics": "Short taxi from Yonggungsa."},
                {"time": "19:00–21:30", "title": "Gwangalli Beach & Saturday Drone Light Show", "detail": "Watch 500+ synchronized LED drones dance above Gwangan Bridge from the sand.", "logistics": "Gwangalli Beach (drones at 19:00 & 21:00)."}
            ],
            [
                {"label": "Eastern Coastal Synergy", "text": "Blueline Park, Cheongsapo, Yonggungsa, and Gwangalli form a natural eastern coastline day."},
                {"label": "Saturday Drone Spectacular", "text": "Timed specifically for Saturday evening to witness Gwangalli's world-renowned drone performance."}
            ],
            "Lunch: Cheongsapo seaside grilled clams (jogae-gui) with butter and cheese. Dinner: Gwangalli beachfront raw yellowtail sashimi or Korean craft beer and fried chicken.",
            "Book Blueline Sky Capsule 14 days in advance on official website.",
            "Sky Capsule 2-person cabin ₩35,000; Yonggungsa Temple is free entry.",
            "Haedong Yonggungsa has stone steps down to the cliffs; wear non-slip shoes.",
            "Eternal Journey Bookstore at Ananti and Centum City provide indoor alternatives."
        ),
        # Day 15: Nov 15
        make_day(14, "Busan", "Hillside Alleys & Marine Markets", "Busan · Haeundae Beachfront",
            "Gamcheon Culture Village → Jagalchi Fish Market → BIFF Square",
            "Pastel Terraced Alleys & Korea's Largest Marine Market",
            [
                {"time": "09:30–12:30", "title": "Gamcheon Culture Village Walk", "detail": "Wander terraced hillside alleys painted in pastel hues and photograph the famous Little Prince statue overlooking the harbor.", "logistics": "Toseong Station Line 1 Exit 6 + local bus Saha 1-1."},
                {"time": "13:00–15:00", "title": "Jagalchi Fish Market Feast", "detail": "Explore Korea's biggest seafood market, dining on fresh seasonal sashimi and spicy fish stew in the second-floor market hall.", "logistics": "Jagalchi Station Line 1 Exit 10."},
                {"time": "15:15–17:30", "title": "BIFF Square & Bupyeong Kkangtong Market", "detail": "Walk the film festival handprint square, taste famous seed hotteok, and browse traditional retro market alleys.", "logistics": "Nampo-dong pedestrian zone."},
                {"time": "18:00–19:30", "title": "Yongdusan Park & Busan Tower Night View", "detail": "Ride outdoor escalator up to Yongdusan Park to view twinkling harbor lights.", "logistics": "Nampo Station Exit 1/7."},
                {"time": "20:00–21:30", "title": "Nampo-dong Dwaeji Gukbap Dinner", "detail": "Enjoy boiling pork bone soup with tender pork slices and chives.", "logistics": "Nampo soup alley."}
            ],
            [
                {"label": "Old Busan Heritage", "text": "Reveals the resilient history of wartime refugees in Gamcheon and the maritime spirit of Jagalchi."},
                {"label": "Market Immersion", "text": "Jagalchi and BIFF street snacks showcase essential Busan culinary culture."}
            ],
            "Lunch: Jagalchi Market fresh flounder sashimi & spicy fish soup. Dinner: Traditional Busan Dwaeji Gukbap (pork bone soup).",
            "Gamcheon village maps available at tourist center for ₩2,000.",
            "Gamcheon entry free; Busan Tower observation deck ₩12,000.",
            "Gamcheon is a living residential village; keep noise low.",
            "Jagalchi 7-story indoor market building provides complete shelter."
        ),
        # Day 16: Nov 16
        make_day(15, "Busan", "Hillside Monorails & Mountain Fortress", "Busan · Haeundae Beachfront",
            "Choryang 168 Monorail & Sanbokdoro Scenic Road → Beomeosa Mountain Temple",
            "Free Hillside Public Monorails & 1,300-Year Silla Sanctuaries",
            [
                {"time": "09:30–12:00", "title": "Choryang 168 Monorail & Sanbokdoro (Mountain Road)", "detail": "Ride the unique free public monorail climbing steeply up 168 stairs into the historic hillside village, enjoying sweeping panoramic views across Busan Port from the observation deck.", "logistics": "Busan Station Line 1 Exit 7, 10-min walk."},
                {"time": "12:15–13:30", "title": "Choryang Bulgogi Alley Lunch", "detail": "Savor sweet soy-marinated beef bulgogi with fresh ssam greens.", "logistics": "Choryang dining lane."},
                {"time": "14:00–17:00", "title": "Beomeosa Mountain Temple & Forest Trail", "detail": "Ascend Mount Geumjeong to tour one of Korea's premier Buddhist headquarters founded in 678 AD, surrounded by tranquil bamboo groves.", "logistics": "Beomeosa Station Line 1 Exit 5 + Bus 90."},
                {"time": "17:30–19:30", "title": "Oncheonjang Natural Hot Spring Bath", "detail": "Soak in historic mineral hot springs to soothe legs.", "logistics": "Oncheonjang Station Line 1."},
                {"time": "20:00–21:30", "title": "Dongnae Scallion Pajeon & Makgeolli Dinner", "detail": "Enjoy 80-year-old royal scallion seafood pancake with Geumjeongsanseong rice wine.", "logistics": "Dongnae dining street."}
            ],
            [
                {"label": "Authentic Hillside Rail", "text": "The 168 Monorail is a real public transit marvel providing free mobility to hillside residents."},
                {"label": "Mountain Sanctuary", "text": "Beomeosa offers deep Buddhist serenity on the slopes of Mount Geumjeong."}
            ],
            "Lunch: Choryang marinated beef bulgogi. Dinner: Dongnae Halmae Pajeon (royal scallion seafood pancake) with mountain makgeolli.",
            "Choryang 168 Monorail is free public transit; open daily 06:00–21:00.",
            "Monorail free; Beomeosa free; Pajeon dinner ~₩25,000 per person.",
            "Monorail has limited capacity (8 passengers per car); short wait during morning peak.",
            "Beomeosa museum and Oncheonjang spa are completely indoor."
        ),
        # Day 17: Nov 17
        make_day(16, "Busan", "Marine Cable Cars & Thermal Spas", "Busan · Haeundae Beachfront",
            "Songdo Marine Cable Car & Skywalk → Centum City Spa Land Thermal Saunas",
            "Over-Water Gondolas & World-Class Hydrotherapy Saunas",
            [
                {"time": "09:30–12:30", "title": "Songdo Marine Cable Car (Air Cruise) & Cloud Trails", "detail": "Glide across the open sea in a glass-bottom Crystal Cabin gondola between Songdo Beach and Amnam Park, walking the curved Songdo Cloud Trails skywalk.", "logistics": "Songdo Bay Station; bus or taxi from Haeundae."},
                {"time": "12:30–14:00", "title": "Songdo Beachfront Seafood Lunch", "detail": "Enjoy fresh grilled mackerel or abalone porridge overlooking the bay.", "logistics": "Songdo waterfront."},
                {"time": "14:30–18:30", "title": "Spa Land Centum City Luxury Thermal Bathhouse", "detail": "Spend 4 hours immersed in 18 natural mineral pools and 13 themed aesthetic saunas with heated loungers.", "logistics": "Centum City Station Line 2 direct basement connection."},
                {"time": "19:00–21:30", "title": "Shinsegae Sky Lounge Modern Korean Dinner", "detail": "Dine overlooking Suyeong River.", "logistics": "Shinsegae Centum City 9F."}
            ],
            [
                {"label": "Aerial Ocean Perspective", "text": "Songdo Cable Car provides sweeping aerial views of incoming container vessels and rocky islands."},
                {"label": "Mid-Trip Rejuvenation", "text": "Spa Land hydrotherapy completely restores muscles before the final leg of the journey."}
            ],
            "Lunch: Songdo seaside abalone porridge or grilled fish. Dinner: Modern Korean tasting menu at Shinsegae Centum City 9F.",
            "Songdo Cable Car Crystal Cabin ₩22,000 round-trip; Spa Land 4-hr pass ~₩23,000.",
            "Cable Car ₩22,000; Spa Land ₩23,000; Dinner ~₩30,000 per person.",
            "Spa Land does not admit children under 7; maintains quiet adult relaxation.",
            "Spa Land and Shinsegae Mall are 100% indoor and weatherproof."
        ),
        # Day 18: Nov 18
        make_day(17, "Busan", "Arts Complex & Night Skyline", "Busan · Haeundae Beachfront",
            "F1963 Wire Factory Cultural Complex → Busan Cinema Center → The Bay 101 Skyline",
            "Post-Industrial Art Spaces & Sparkling Skyscraper Panoramas",
            [
                {"time": "10:00–12:30", "title": "F1963 Cultural Arts Complex (Former Factory)", "detail": "Explore the visionary industrial architecture of a 1963 wire rope factory converted into an eco-arts complex, featuring Yes24 giant book store and bamboo gardens.", "logistics": "Mangmi Station Line 3 or 15-min taxi from Haeundae."},
                {"time": "12:30–14:00", "title": "Terarosa Specialty Coffee & Bakery Lunch", "detail": "Enjoy pour-over specialty coffee and artisan sourdough in the dramatic factory interior.", "logistics": "Inside F1963."},
                {"time": "14:30–17:00", "title": "Busan Cinema Center (BIFF Venue)", "detail": "Admire the Guinness World Record cantilevered LED roof structure and explore cinema exhibits.", "logistics": "Centum City Station Line 2."},
                {"time": "17:30–19:30", "title": "The Bay 101 & Marine City Sunset", "detail": "Photograph glittering glass skyscrapers reflecting across the harbor.", "logistics": "Dongbaek Station Exit 1."},
                {"time": "20:00–21:30", "title": "Haeundae Korean Fried Chicken & Draft Beer", "detail": "Crispy golden chicken on Haeundae avenue.", "logistics": "Gunam-ro."}
            ],
            [
                {"label": "Adaptive Reuse", "text": "F1963 is a masterclass in post-industrial architectural revitalization."},
                {"label": "Iconic Nightscape", "text": "Marine City skyline reflections at The Bay 101 are internationally celebrated."}
            ],
            "Lunch: Terarosa F1963 artisan sourdough sandwich and coffee. Dinner: Haeundae gourmet Korean fried chicken and draft beer.",
            "F1963 exhibitions and bookstore are free admission; open daily 10:00–20:00.",
            "F1963 free; Cinema Center free exterior; Dinner ~₩22,000 per person.",
            "Terarosa coffee beans can be purchased as fresh souvenirs.",
            "F1963 is completely indoor and weatherproof."
        ),
        # Day 19: Nov 19
        make_day(18, "Busan", "Low-Stakes Coastal Stroll (CSAT Day)", "Busan · Haeundae Beachfront",
            "Igidae Coastal Cliff Walkway → Oryukdo Skywalk → Sunset Cafe (CSAT Day)",
            "Peaceful Waves, Skywalks & Gentle Rhythm (CSAT / Suneung Day)",
            [
                {"time": "10:00–12:30", "title": "Igidae Coastal Cliff Walkway", "detail": "Walk the scenic coastal trail cut into volcanic cliff faces, offering pristine ocean views.", "logistics": "Kyungsung Univ. Station Line 2 + Bus 20/22/39."},
                {"time": "12:45–14:00", "title": "Oryukdo Island View Lunch", "detail": "Enjoy warm seafood noodle soup (haemul kalguksu) overlooking the rocky islets.", "logistics": "Oryukdo tourist plaza."},
                {"time": "14:15–16:00", "title": "Oryukdo Glass Skywalk", "detail": "Step onto the transparent glass skywalk suspended 35 meters above roaring waves.", "logistics": "Free admission (shoe covers provided)."},
                {"time": "16:30–19:00", "title": "Haeundae Sunset Cafe & Rest", "detail": "Relax at an ocean-view cafe on Haeundae beachfront, reflecting on 7 wonderful Busan nights.", "logistics": "Haeundae beachfront."},
                {"time": "19:30–21:30", "title": "Busan Farewell Feast: Hanwoo Beef Barbecue", "detail": "Celebrate final night in Busan with premium charcoal-grilled Korean Hanwoo beef tenderloin.", "logistics": "Haeundae Somunnan Amso Galbi."}
            ],
            [
                {"label": "CSAT Low-Stakes Alignment", "text": "Nov 19 national CSAT exam day is kept localized along the coast to avoid urban traffic hold zones."},
                {"label": "Farewell Coastal Ridge", "text": "Igidae-to-Oryukdo ridge provides one of Korea's most breathtaking coastal walking memories."}
            ],
            "Lunch: Oryukdo Haemul Kalguksu (rich seafood noodle soup). Dinner: Haeundae Somunnan Amso Galbi (marinated beef short ribs with potato noodles).",
            "Oryukdo Skywalk open 09:00–18:00; admission is free.",
            "Skywalk free; Farewell Hanwoo BBQ dinner ~₩45,000–₩60,000 per person.",
            "Oryukdo Skywalk closes temporarily during strong winds or rain for safety.",
            "Haeundae beachfront indoor cafes offer heated panoramic sea views."
        ),
        # Day 20: Nov 20
        make_day(19, "Seoul", "Capital Return & Retro Alleys", "Seoul · Seoul Station / Myeongdong",
            "Morning KTX Busan to Seoul (2h15m) → Seoul Station Check-in → Euljiro Retro Alleys",
            "Capital Return: High-Speed Rail & Departure Buffer",
            [
                {"time": "09:30–10:15", "title": "Busan Station Departure", "detail": "Check out of Haeundae hotel, take taxi or metro to Busan Station, and board direct KTX.", "logistics": "Board train 10 minutes prior to departure."},
                {"time": "10:30–12:45", "title": "KTX High-Speed Rail to Seoul", "detail": "Comfortable 2-hour 15-minute high-speed journey back to Seoul Station.", "logistics": "Direct arrival inside Seoul Station concourse."},
                {"time": "13:00–14:30", "title": "Seoul Station Hotel Check-in & Lunch", "detail": "Check into hotel directly at Seoul Station and enjoy warm bibimbap or beef soup.", "logistics": "Drop bags; zero long subway commute."},
                {"time": "15:00–18:00", "title": "Euljiro 'Hipjiro' Lighting & Print Alleys", "detail": "Explore the vibrant collision of traditional industrial workshops and secret third-floor coffee lofts.", "logistics": "Euljiro 3-ga Station Line 2/3."},
                {"time": "18:30–21:00", "title": "Euljiro Nogari Alley & Korean Draft Beer", "detail": "Experience Korea's iconic outdoor beer alley tradition with grilled dried pollack, garlic chicken, and draft beer.", "logistics": "Euljiro 3-ga Station Exit 3/4."}
            ],
            [
                {"label": "Departure Buffer", "text": "Returning to Seoul on Friday eliminates all risk of KTX weekend disruption before Sunday flight."},
                {"label": "Seoul Station Anchor", "text": "Direct doorstep proximity to the AREX airport express line guarantees effortless Sunday transit."}
            ],
            "Lunch: Seoul Station concourse dining. Dinner: Euljiro Nogari alley garlic fried chicken and grilled pollack.",
            "Book KTX Busan→Seoul on Korail app 30 days in advance.",
            "KTX ticket ~₩59,800 per person.",
            "Friday afternoon KTX trains fill up quickly; secure reserved seats early.",
            "Lotte Mart at Seoul Station offers covered shopping right at your doorstep."
        ),
        # Day 21: Nov 21
        make_day(20, "Seoul", "Souvenirs & Farewell Feast", "Seoul · Seoul Station / Myeongdong",
            "Namdaemun Market → Seoul Station Lotte Mart (Tax-Free Food Shopping) → Grand Farewell Banquet",
            "Final Souvenir Curations & Celebration Feast",
            [
                {"time": "09:30–12:30", "title": "Namdaemun Market & Kalguksu Alley", "detail": "Browse Korea's oldest traditional market for ceramics, tea accessories, dried seaweed, and handmade kitchenware, enjoying hot kalguksu.", "logistics": "Hoehyeon Station Line 4 Exit 5."},
                {"time": "13:00–15:30", "title": "Seoul Station Lotte Mart Mega-Store", "detail": "Curate gourmet food gifts: premium Korean seaweed (gim), market snacks, red pepper paste (gochujang), and instant noodles with instant tax refund.", "logistics": "Immediate tax refund counter on 2F with passport."},
                {"time": "16:00–18:00", "title": "Afternoon Packing & Luggage Weighing", "detail": "Return to hotel room, organize souvenirs, check luggage weight against airline allowance, and complete online flight check-in.", "logistics": "Hotel front desk provides digital scale."},
                {"time": "18:30–21:00", "title": "Grand Farewell Korean BBQ Feast", "detail": "Celebrate the 21-night journey with premium Korean Hanwoo beef barbecue and aged kimchi stew in central Seoul.", "logistics": "Myeongdong / Gwanghwamun dining room."}
            ],
            [
                {"label": "Departure Prep", "text": "All shopping and packing completed by Saturday night ensures Sunday morning is 100% calm and stress-free."},
                {"label": "Immediate Tax Refund", "text": "Handling tax refunds at Lotte Mart saves 30+ minutes at airport customs lines."}
            ],
            "Lunch: Namdaemun Kalguksu Alley (includes free cold bibim naengmyeon bowl). Dinner: Premium Hanwoo charcoal BBQ banquet.",
            "Complete online airline check-in 24 hours prior; select seats and enter passport numbers.",
            "Souvenirs ~₩50,000–₩100,000; Farewell dinner ~₩45,000 per person.",
            "Keep tax refund receipts, passport, and critical items in carry-on bag.",
            "Shinsegae Main Department Store underground tunnels connect Namdaemun to Myeongdong."
        ),
        # Day 22: Nov 22
        make_day(21, "Seoul", "Departure", "Departure · Incheon International Airport",
            "AREX Non-Stop Express to ICN (43 mins) → Check-in & Security → Flight at 13:00",
            "Calm & Seamless Flight Departure",
            [
                {"time": "08:30–09:15", "title": "Hotel Checkout & City Airport Check-in (Optional)", "detail": "Check out of Seoul Station hotel. If flying Korean Air/Asiana, check in bags at Seoul Station City Airport Terminal.", "logistics": "B2 of Seoul Station."},
                {"time": "09:30–10:15", "title": "AREX Non-Stop Express Train to ICN", "detail": "Board direct express train to Incheon Airport Terminal 1 (43 mins) or Terminal 2 (51 mins).", "logistics": "Reserved seats with dedicated luggage racks."},
                {"time": "10:15–12:15", "title": "Airport Customs, Security & Tax Refund", "detail": "Drop remaining bags, clear security, process airport tax refunds, and reach departure gate by 12:20.", "logistics": "Target 3 hours prior to 13:00 international departure."},
                {"time": "12:30–13:00", "title": "Boarding & Takeoff", "detail": "Board aircraft for the return flight home with unforgettable memories of Korea.", "logistics": "Gates close 15 minutes before scheduled departure."}
            ],
            [
                {"label": "Logistics Perfection", "text": "Direct AREX express from hotel doorstep guarantees predictable 43-minute airport transit."},
                {"label": "Zero Rush", "text": "Arriving at 10:15 leaves ample time for customs, tax refunds, and a relaxed pre-flight meal."}
            ],
            "Breakfast: Hotel café or airport lounge / Korean Food Street at ICN Terminal (bibimbap/soup).",
            "Verify terminal (T1 vs T2) based on airline ticket before boarding AREX.",
            "AREX Express ticket ₩11,000 per person.",
            "Terminal 2 is 8 minutes further on the AREX line than Terminal 1; check your terminal code.",
            "If AREX express sells out, AREX All-Stop commuter train departs every 6–10 minutes."
        )
    ]

    scorecard = [
        {"label": "Rail Efficiency", "value": "5/5", "tone": "good"},
        {"label": "Independence Heritage", "value": "5/5", "tone": "good"},
        {"label": "Coastal Scenery", "value": "5/5", "tone": "good"},
        {"label": "Monumental Art", "value": "5/5", "tone": "good"}
    ]

    return {
        "id": "seoul-cheonan-busan-rail",
        "shortTitle": "Seoul · Cheonan · Busan (Rail Classic Explorer)",
        "title": "Scenic Rail Corridor & Independence Heritage (Rail Classic Explorer)",
        "routeLabel": "Seoul (7N) → Cheonan (5N) → Busan (7N) → Seoul (2N)",
        "badge": "Maximum Rail Speed & Patriotic Heritage",
        "bestFor": "Train lovers, history buffs, and practical travelers who appreciate ultra-fast 35-minute KTX rail transfers, majestic patriotic monuments, colossal bronze Buddhas, and scenic coastal railways.",
        "decisionSummary": "An exceptionally efficient high-speed rail corridor connecting Seoul's imperial palaces and Suwon fortress with Cheonan's monumental Independence Hall and Damien Hirst sculpture park, concluding with Busan's beach trains and coastal cliffs.",
        "recommendation": "Choose this route if you want maximum rail speed between cities (just 35 minutes Seoul to Cheonan), profound national independence heritage, and seamless transit logistics.",
        "tradeoff": "Cheonan is a more compact, focused regional city with shorter transit times than Daejeon.",
        "scorecard": scorecard,
        "bases": get_scb_common_bases(),
        "transfers": get_scb_common_transfers(),
        "budgetScenarios": get_scb_budget_scenarios(),
        "bookingPriorities": get_scb_booking_priorities(),
        "days": days
    }
