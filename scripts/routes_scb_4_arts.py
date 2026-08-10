#!/usr/bin/env python3
"""Route Blueprint: Seoul · Cheonan · Busan (World Sculpture Parks, Urban Design & Creative Hubs)."""

from scripts.generate_all_itineraries import make_day
from scripts.itinerary_builder_scb import (
    get_scb_common_bases,
    get_scb_common_transfers,
    get_scb_budget_scenarios,
    get_scb_booking_priorities
)

def get_scb_arts():
    days = [
        # Day 1: Nov 1
        make_day(0, "Seoul", "Arrival", "Seoul · Myeongdong / Seoul Station edge",
            "ICN arrival at 21:00 → late transfer → hotel check-in → restorative rest",
            "Late Landing & Design Base Check-in",
            [
                {"time": "21:00–22:15", "title": "ICN Arrival & Border Clearance", "detail": "Clear immigration smoothly, collect checked luggage, and pick up pre-arranged transportation cards.", "logistics": "Terminal 1 or 2."},
                {"time": "22:30–23:45", "title": "Direct Transfer to Central Seoul", "detail": "Board Airport Limousine Bus or official taxi directly to Myeongdong / Seoul Station hotel.", "logistics": "Minimizes late-night luggage handling."},
                {"time": "23:45–00:30", "title": "Hotel Check-in & Rest", "detail": "Settle into hotel room, unpack essentials, and rest before starting the architecture and art journey.", "logistics": "Notify hotel of late arrival."}
            ],
            [
                {"label": "Aesthetic Focus", "text": "Preserve energy for extensive gallery walking and architectural exploration starting tomorrow."},
                {"label": "Central Base", "text": "Provides easy walking access to historic and contemporary design landmarks."}
            ],
            "Light herbal tea or convenience store snack.",
            "Confirm late check-in with hotel in writing.",
            "Limousine Bus ~₩17,000.",
            "Rest deeply to prepare for visual and artistic discovery.",
            "Hotel front desk provides 24-hour service."
        ),
        # Day 2: Nov 2
        make_day(1, "Seoul", "Brutalist Space & Contemporary Masters", "Seoul · Myeongdong / Seoul Station edge",
            "Arario Museum in SPACE (Kim Swoo-geun Architecture) → MMCA Seoul → Samcheong Galleries",
            "Brutalist Brick Architecture & Premier Contemporary Galleries",
            [
                {"time": "09:30–12:30", "title": "Arario Museum in SPACE", "detail": "Explore master architect Kim Swoo-geun's 1971 ivy-covered black brick masterpiece (former SPACE Group building), featuring intricate split-level rooms housing monumental contemporary artworks by Marc Quinn, Subodh Gupta, and Nam June Paik.", "logistics": "Anguk Station Line 3 Exit 3."},
                {"time": "12:45–14:00", "title": "Samcheong-dong Artisan Cafe Lunch", "detail": "Enjoy gourmet pasta, salads, or Korean rice sets overlooking the traditional tiled roofs.", "logistics": "Samcheong cafe street."},
                {"time": "14:15–17:00", "title": "MMCA Seoul & Kukje Gallery", "detail": "Tour the National Museum of Modern & Contemporary Art and premier commercial galleries (Kukje, Gallery Hyundai, PKM) in Samcheong-dong.", "logistics": "Anguk Station Line 3 Exit 1."},
                {"time": "17:30–19:30", "title": "Bukchon Hanok Architecture Walk", "detail": "Stroll traditional wooden residential alleys studying Joseon architectural proportions.", "logistics": "Bukchon main ridge."},
                {"time": "20:00–21:30", "title": "Jongno Korean Charcoal BBQ Dinner", "detail": "Feast on tender pork belly and savory soybean stew.", "logistics": "Jongno dining lane."}
            ],
            [
                {"label": "Architectural Icon", "text": "SPACE Building is widely recognized as one of Korea's most important 20th-century architectural masterworks."},
                {"label": "Gallery Concentration", "text": "Samcheong-dong represents the highest density of world-class contemporary art galleries in East Asia."}
            ],
            "Lunch: Samcheong-dong artisan cafe dining. Dinner: Jongno charcoal-grilled pork barbecue with soybean stew.",
            "Arario Museum in SPACE entry ₩15,000; MMCA Seoul ₩5,000 (closed Mondays).",
            "Museums ~₩20,000; Dinner ~₩28,000 per person.",
            "Arario Museum contains narrow spiral staircases; large bags must be stored in lockers.",
            "Both Arario Museum and MMCA are fully enclosed and climate-controlled."
        ),
        # Day 3: Nov 3
        make_day(2, "Seoul", "Neo-Futurism & Industrial Lofts", "Seoul · Myeongdong / Seoul Station edge",
            "Dongdaemun Design Plaza (DDP) Architecture → Seongsu Industrial Design Lofts",
            "Zaha Hadid Parametric Curves & Converted Industrial Lofts",
            [
                {"time": "09:30–12:30", "title": "Dongdaemun Design Plaza (DDP)", "detail": "Examine Zaha Hadid's parametric curves, seamless aluminum facade, and design museum labs.", "logistics": "Dongdaemun History & Culture Park Station Line 2/4/5 Exit 1."},
                {"time": "12:45–14:15", "title": "Seongsu Converted Warehouse Dining Lunch", "detail": "Dine in a red-brick former shoe factory on artisan pasta or Korean fusion bowls.", "logistics": "Seongsu Station Line 2 Exit 3."},
                {"time": "14:30–17:30", "title": "Seongsu Experimental Flagships (Tamburins, Gentle Monster, Daelim)", "detail": "Explore multi-sensory concept stores and kinetic art installations across Seongsu Yeonmujang-gil.", "logistics": "Seongsu design corridor."},
                {"time": "18:00–19:30", "title": "Seoul Forest Outdoor Sculpture Park Sunset", "detail": "Walk among monumental bronze sculptures and golden ginkgo trees.", "logistics": "Seoul Forest Station Exit 4."},
                {"time": "20:00–21:30", "title": "Seongsu Craft Makgeolli Pub Dinner", "detail": "Pair artisanal bubbly rice wine with crispy truffle potato pancakes.", "logistics": "Seongsu dining quarter."}
            ],
            [
                {"label": "Parametric Design", "text": "DDP represents the global pinnacle of digital parametric architecture."},
                {"label": "Industrial Adaptive Reuse", "text": "Seongsu demonstrates how post-industrial factories can become visionary design incubators."}
            ],
            "Lunch: Seongsu Daelim Warehouse cafe lunch. Dinner: Seongsu craft makgeolli and crispy truffle gamjajeon.",
            "DDP exterior open 24/7; Seongsu flagships open at 11:00 AM.",
            "DDP exhibits ~₩15,000; Dinner ~₩28,000 per person.",
            "Popular Seongsu pop-ups may have short digital queue wait times on weekends.",
            "DDP design interior and Seongsu loft cafes provide complete weather shelter."
        ),
        # Day 4: Nov 4
        make_day(3, "Seoul", "Pritzker Architecture & Fine Art", "Seoul · Myeongdong / Seoul Station edge",
            "Leeum Museum of Art (Botta, Nouvel, Koolhaas) → Itaewon Antique Street",
            "Pritzker Trio Architecture & Celadon Masterpieces",
            [
                {"time": "10:00–13:00", "title": "Leeum Museum of Art Architecture & Curations", "detail": "Admire the three distinct museum structures designed by Pritzker Prize laureates Mario Botta (terracotta rotunda), Jean Nouvel (oxidized steel), and Rem Koolhaas (black concrete), housing Korea's finest white porcelain, celadon, and modern masterpieces (Giacometti, Rothko, Warhol).", "logistics": "Hangangjin Station Line 6 Exit 1."},
                {"time": "13:15–14:45", "title": "Hannam-dong Gourmet Lunch", "detail": "Dine in chic Hannam-dong on artisan French dining, gourmet pasta, or modern Korean cuisine.", "logistics": "Hannam cafe street."},
                {"time": "15:00–17:00", "title": "Itaewon Antique Furniture Street", "detail": "Browse European and Asian antique furniture, vintage clocks, and decorative art curations across 100+ boutique shops.", "logistics": "Itaewon Station Line 6 Exit 3/4."},
                {"time": "17:30–19:30", "title": "Namsan Outdoor Sculpture Park & Sunset", "detail": "Walk through pine-scented sculpture gardens overlooking central Seoul.", "logistics": "Namsan park trail."},
                {"time": "20:00–21:30", "title": "Traditional Ginseng Chicken Soup (Samgyetang) Dinner", "detail": "Warm up with whole young chicken stuffed with sticky rice, ginseng root, garlic, and jujubes at Tosokchon.", "logistics": "Tosokchon (Gyeongbokgung Station Line 3)."}
            ],
            [
                {"label": "Pritzker Architectural Harmony", "text": "Leeum is unique globally for bringing Botta, Nouvel, and Koolhaas into a single cohesive campus."},
                {"label": "Masterpiece Rotunda", "text": "Mario Botta's terracotta inverted cone rotunda is one of the world's most photographed museum stairwells."}
            ],
            "Lunch: Hannam-dong artisanal Italian or modern bistro. Dinner: Tosokchon Samgyetang (ginseng chicken soup).",
            "Book Leeum Museum of Art timed tickets online 14 days in advance (free permanent collection).",
            "Leeum Museum free permanent entry; Dinner ~₩22,000 per person.",
            "English audio guide included with smartphone device.",
            "Leeum Museum is fully indoor with world-class climate control."
        ),
        # Day 5: Nov 5
        make_day(4, "Seoul", "Oil Depots & Modern Cultural Parks", "Seoul · Myeongdong / Seoul Station edge",
            "Oil Tank Culture Park (Mapo Industrial Transformation) → Hongdae Indie Street",
            "Massive Steel Oil Tanks Transformed into Cultural Glass Pavilions",
            [
                {"time": "10:00–12:30", "title": "Oil Tank Culture Park (Mapo)", "detail": "Explore five colossal 1970s steel oil storage tanks converted into dramatic glass exhibition pavilions, open-air amphitheaters, and community eco-spaces.", "logistics": "World Cup Stadium Station Line 6 Exit 2."},
                {"time": "12:45–14:15", "title": "Mapo Gourmet Lunch", "detail": "Enjoy buckwheat cold noodles or handmade dumplings.", "logistics": "World Cup Stadium / Mapo dining area."},
                {"time": "14:45–17:00", "title": "KT&G Sangsangmadang & Hongdae Design District", "detail": "Browse independent designer stationery, graphic prints, and photo galleries in Hongdae.", "logistics": "Hongik Univ. Station Line 2 Exit 9."},
                {"time": "17:30–19:30", "title": "Gyeongui Line Forest Park Walk", "detail": "Walk the transformed green railway line shaded by autumn trees.", "logistics": "Yeonnam-dong forest park."},
                {"time": "20:00–21:30", "title": "Mapo Charcoal Pork Galbi Barbecue Feast", "detail": "Feast on marinated pork ribs grilled over hardwood charcoal.", "logistics": "Mapo Station Line 5 BBQ Alley."}
            ],
            [
                {"label": "Ecological Architecture", "text": "Oil Tank Culture Park is a globally celebrated example of industrial heritage reclaimed as public green space."},
                {"label": "Creative Contrast", "text": "Links monumental industrial spaces with Hongdae's vibrant indie design culture."}
            ],
            "Lunch: Mapo buckwheat noodles and dumplings. Dinner: Mapo charcoal-grilled pork galbi with cold dongchimi noodles.",
            "Oil Tank Culture Park is open 24/7; exhibition pavilions open 10:00–18:00 (free admission).",
            "Park free; Sangsangmadang free; Dinner ~₩25,000 per person.",
            "Walk inside Tank 6 to experience the soaring steel and glass circular community lounge.",
            "Tank 6 cafe and glass pavilions provide indoor shelter."
        ),
        # Day 6: Nov 6
        make_day(5, "Seoul", "Monolithic Space & Modern Art", "Seoul · Myeongdong / Seoul Station edge",
            "National Museum of Korea (Pensive Bodhisattva) → Deoksugung Stonewall & MMCA Deoksugung",
            "Transcendent Contemplative Spaces & Neoclassical Stone Palaces",
            [
                {"time": "09:30–12:30", "title": "National Museum of Korea Room of Quiet Contemplation", "detail": "Experience the minimalist architectural space designed by Choi Wook (One O One Architects), housing two National Treasure Pensive Bodhisattvas in serene, meditative lighting.", "logistics": "Ichon Station Line 4 direct underground walkway."},
                {"time": "12:45–14:00", "title": "Museum Mirror Pond Dining Lunch", "detail": "Enjoy refined Korean dining overlooking the traditional pavilion and reflection pond.", "logistics": "Museum 1F dining hall."},
                {"time": "14:30–16:30", "title": "Deoksugung Palace & MMCA Deoksugung Branch", "detail": "Tour the unique palace blending Joseon wooden pavilions with neoclassical Western stone architecture (Seokjojeon).", "logistics": "City Hall Station Line 1/2 Exit 2."},
                {"time": "16:45–18:30", "title": "Deoksugung Stonewall Walkway & Jeongdong Heritage", "detail": "Walk Korea's most romantic tree-lined stonewall road, viewing 19th-century diplomatic legations.", "logistics": "Deoksugung stonewall path."},
                {"time": "19:00–21:00", "title": "Gwanghwamun Hanwoo Bulgogi Dinner", "detail": "Enjoy seasoned Korean beef bulgogi with glass noodles in a private dining room.", "logistics": "Gwanghwamun dining area."}
            ],
            [
                {"label": "Spiritual Minimalism", "text": "Room of Quiet Contemplation creates an architectural environment of profound tranquility and shadow."},
                {"label": "Modernist Dialogue", "text": "Deoksugung Seokjojeon illustrates Korea's early 20th-century architectural modernization."}
            ],
            "Lunch: National Museum Mirror Pond dining. Dinner: Gwanghwamun Hanwoo beef bulgogi hot pot.",
            "National Museum permanent galleries are free; MMCA Deoksugung ₩2,000.",
            "Museums ~₩3,000; Dinner ~₩28,000 per person.",
            "Maintain quiet contemplation in Bodhisattva room.",
            "Both museums are completely indoor and heated."
        ),
        # Day 7: Nov 7
        make_day(6, "Seoul", "Sculpture Parks & KTX Prep", "Seoul · Myeongdong / Seoul Station edge",
            "Olympic Park Monumental Sculpture Walk → Starfield COEX Library → Sunday KTX to Cheonan Prep",
            "World Monumental Sculptures, Giant Book Towers & Rail Prep",
            [
                {"time": "10:00–12:30", "title": "Olympic Park World Sculpture Garden", "detail": "Walk among 200+ monumental sculptures created by world-renowned artists (César, Denis Oppenheim, Dani Karavan) across open autumn lawns.", "logistics": "Olympic Park Station Line 5/9 Exit 3."},
                {"time": "12:30–14:00", "title": "Jamsil Gourmet Lunch", "detail": "Enjoy fresh Korean bibimbap or light noodles near the park lake.", "logistics": "Jamsil / Bangi-dong food alley."},
                {"time": "14:30–16:30", "title": "Starfield Library COEX Mall", "detail": "Photograph the 13-meter tall open book towers and explore the mega design mall.", "logistics": "Samseong Station Line 2 or Bongeunsa Station Line 9."},
                {"time": "17:00–18:30", "title": "Seoul Station Packing & Train Verification", "detail": "Pack luggage for Sunday morning KTX to Cheonan-Asan (only 35 mins!).", "logistics": "Seoul Station hotel."},
                {"time": "19:00–21:00", "title": "Seoul Station Korean Stew Dinner", "detail": "Enjoy mild beef bulgogi or hot pot near hotel doorstep.", "logistics": "Seoul Station dining lane."}
            ],
            [
                {"label": "Top 5 Global Sculpture Park", "text": "Seoul Olympic Sculpture Park is recognized as one of the world's five largest open-air sculpture museums."},
                {"label": "Rail Preparation", "text": "Packing early ensures an effortless Sunday morning 35-minute rail leap to Cheonan."}
            ],
            "Lunch: Jamsil fresh bibimbap. Dinner: Seoul Station sizzling beef bulgogi hot pot.",
            "Olympic Sculpture Park and COEX Starfield Library are 100% free admission.",
            "Free attractions; Lunch ~₩15,000; Dinner ~₩25,000 per person.",
            "Olympic Park is vast; rent a 4-wheel pedal carriage or take park tram if preferred.",
            "COEX complex is 100% enclosed, heated, and weatherproof."
        ),
        # Day 8: Nov 8
        make_day(7, "Cheonan", "City Transition & World Sculpture Hub", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Morning KTX to Cheonan-Asan (35 mins) → Arario Sculpture Park (Damien Hirst, Keith Haring) → Arario Gallery",
            "World Monumental Contemporary Art in an Urban Plaza",
            [
                {"time": "09:45–10:20", "title": "KTX High-Speed Rail Seoul to Cheonan-Asan", "detail": "Lightning 35-minute smooth high-speed transit from Seoul Station to Cheonan-Asan Station.", "logistics": "Direct Gyeongbu line."},
                {"time": "10:30–12:00", "title": "Hotel Check-in & Base Setup", "detail": "Check into hotel (e.g. Shilla Stay Cheonan or Ramada Encore Cheonan-Asan) and drop bags.", "logistics": "Station area / Shinbu-dong."},
                {"time": "12:15–13:30", "title": "Shinbu-dong Gourmet Lunch", "detail": "Enjoy Korean hand-cut noodles or stone-pot bibimbap in central Cheonan.", "logistics": "Shinbu-dong dining district."},
                {"time": "13:45–16:30", "title": "Arario Sculpture Park Cheonan & Arario Gallery", "detail": "Walk the world-famous open-air sculpture plaza featuring colossal original masterpieces: Damien Hirst's 6-meter 'Hymn' and 'Charity', Keith Haring's vibrant bronzes, Arman's tower of 99 car axles, and CI KIM's dynamic contemporary installations.", "logistics": "Shinbu-dong Arario Plaza (free open-air plaza)."},
                {"time": "16:45–17:45", "title": "1934 Original Hakhwa Hodu-gwaja Bakery", "detail": "Taste steaming hot walnut pastries filled with whole crunchy walnuts and smooth red/white bean paste freshly baked from the oven.", "logistics": "Cheonan Station / Shinbu-dong branch."},
                {"time": "18:30–21:00", "title": "Cheonan Sizzling Bulgogi & Suyuk Dinner", "detail": "Feast on tender seasoned beef bulgogi with fresh side dishes.", "logistics": "Central Cheonan restaurant quarter."}
            ],
            [
                {"label": "Asia's Premier Private Sculpture Plaza", "text": "Founded by collector CI KIM, Arario Sculpture Park is one of the only public plazas in Asia displaying monumental works by Damien Hirst and Keith Haring."},
                {"label": "Extreme Rail Speed", "text": "At just 35 minutes on the KTX, Cheonan is the most efficient arts detour in South Korea."}
            ],
            "Lunch: Shinsegae Cheonan gourmet dining. Afternoon: 1934 Hakhwa freshly baked warm walnut pastries. Dinner: Cheonan charcoal-grilled Hanwoo beef bulgogi.",
            "Book KTX Seoul→Cheonan-Asan on Korail app 30 days in advance.",
            "KTX ticket ~₩14,100; Arario sculpture park is free open-air plaza; Hodu-gwaja box ~₩6,000.",
            "Photograph Damien Hirst's 'Hymn' from the elevated pedestrian terrace for prime angles.",
            "Arario Gallery Cheonan and Shinsegae Department Store provide full indoor comfort."
        ),
        # Day 9: Nov 9
        make_day(8, "Cheonan", "Monumental Architecture & Autumn Canopy", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Independence Hall Monumental Architecture (Grand Hall of Nation) → 3.2km Maple Tunnel",
            "Monumental Copper-Tiled Roofs & Korea's Longest Autumn Maple Tunnel",
            [
                {"time": "09:30–13:30", "title": "Independence Hall of Korea Architecture Tour", "detail": "Study the monumental architecture of the Grand Hall of the Nation (Korea's largest roof tiled with 40,000 copper plates), the soaring Monument to the Nation, and expansive multimedia exhibition halls.", "logistics": "City Bus 381/382/383 from Cheonan Station or 20-min taxi."},
                {"time": "13:30–14:45", "title": "Mokcheon Traditional Country Lunch", "detail": "Enjoy hearty country soybean paste stew (doenjang jjigae), acorn jelly, and grilled fish.", "logistics": "Independence Hall restaurant plaza."},
                {"time": "15:00–17:30", "title": "Independence Hall Autumn Maple Tree Tunnel Walk", "detail": "Walk the spectacular 3.2km paved pedestrian path shaded by thousands of crimson and golden maple trees encircling the complex.", "logistics": "Circling trail around Independence Hall."},
                {"time": "18:00–19:30", "title": "Return to Cheonan & Cafe Rest", "detail": "Relax at hotel or explore local cafes in Shinbu-dong.", "logistics": "Short taxi or bus return."},
                {"time": "20:00–21:30", "title": "Cheonan Charcoal Pork BBQ Dinner", "detail": "Feast on thick pork neck and steaming kimchi stew.", "logistics": "Shinbu-dong dining lane."}
            ],
            [
                {"label": "Monumental Architecture", "text": "The Grand Hall of the Nation is one of the largest traditional-style roof structures in the world."},
                {"label": "Peak Foliage", "text": "The 3.2km Maple Tree Tunnel is widely celebrated as one of Korea's most magnificent autumn foliage walks."}
            ],
            "Lunch: Mokcheon traditional country doenjang stew and grilled mackerel. Dinner: Shinbu-dong charcoal pork BBQ with soybean stew.",
            "Independence Hall of Korea is free admission; closed on Mondays (outdoor park grounds remain open).",
            "Independence Hall is free; Taxi ~₩15,000 each way; Dinner ~₩25,000 per person.",
            "The complex is vast; wear comfortable walking shoes.",
            "All 7 massive exhibition halls are fully indoor and climate-controlled."
        ),
        # Day 10: Nov 10
        make_day(9, "Cheonan", "Fine Arts & Classical Pavilions", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Cheonan Arts Center & Museum of Fine Arts → Cheonan Samgeori Classical Pavilions",
            "Contemporary Fine Art Galleries & Historic Willow Pavilions",
            [
                {"time": "10:00–12:30", "title": "Cheonan Arts Center & Museum of Fine Arts", "detail": "Explore contemporary painting, sculpture, and media art exhibitions in Cheonan's premier civic arts complex.", "logistics": "Dongnam-gu Seongnam-myeon; 20-min taxi or Bus 381."},
                {"time": "12:45–14:00", "title": "Arts Center Cafe Lunch", "detail": "Enjoy artisan sandwiches, pasta, or Korean rice bowls overlooking the sculpture terrace.", "logistics": "Arts Center 1F."},
                {"time": "14:30–16:30", "title": "Cheonan Samgeori Park Heritage Walk", "detail": "Walk around the scenic willow-lined lake and traditional pavilions where the historic Gyeongbu and Honam royal highways intersected.", "logistics": "Dongnam-gu Samnyong-dong."},
                {"time": "17:00–18:30", "title": "Shinbu Cultural Street Design Boutiques", "detail": "Browse youth fashion shops, stationery, and dessert cafes.", "logistics": "Shinbu-dong."},
                {"time": "19:00–21:00", "title": "Cheonan Sliced Pork Suyuk & Kimchi Feast", "detail": "Enjoy tender boiled pork belly wrapped in fresh salted cabbage with spicy radish salad.", "logistics": "Shinbu-dong dining lane."}
            ],
            [
                {"label": "Civic Art Architecture", "text": "Cheonan Arts Center showcases modern glass-and-steel civic design."},
                {"label": "Historical Crossroad Serenity", "text": "Samgeori Park provides flat, peaceful willow-shaded walks."}
            ],
            "Lunch: Arts center cafe dining. Dinner: Cheonan tender pork suyuk bossam with fresh oyster kimchi.",
            "Cheonan Arts Center closed on Mondays; free admission to permanent galleries.",
            "Arts Center free; Samgeori Park free; Dinner ~₩25,000 per person.",
            "Samgeori Park lake pavilion provides scenic photo backdrops.",
            "Arts Center and Cheonan Museum are completely enclosed and heated."
        ),
        # Day 11: Nov 11
        make_day(10, "Cheonan", "Colossal Statues & Modern Lake Pavilions", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Gakwonsa Temple (Colossal 15-Meter Bronze Buddha) → Seongseong Lake Modern Pavilion",
            "Monumental Bronze Sculpture & Modernist Lakefront Architecture",
            [
                {"time": "09:30–12:30", "title": "Gakwonsa Temple & Grand Bronze Buddha", "detail": "Climb stone stairs to behold the colossal 15-meter seated Bronze Amita Buddha overlooking Taejosan Mountain, studying the craftsmanship of Asia's largest seated outdoor bronze statue.", "logistics": "Dongnam-gu Anseo-dong; City Bus 24 or 15-min taxi."},
                {"time": "12:45–14:15", "title": "Anseo Lake Village Lunch", "detail": "Enjoy buckwheat cold noodles, potato pancakes, and wild herb bibimbap near the temple lake.", "logistics": "Gakwonsa lake restaurant row."},
                {"time": "14:45–17:30", "title": "Seongseong Lake Park & Modern Architectural Cafes", "detail": "Walk the wooden boardwalk loop around Seongseong Lake, visiting multi-story glass-and-concrete architectural cafes overlooking the water.", "logistics": "Seobuk-gu Seongseong-dong; Bus 5 or 15-min taxi."},
                {"time": "18:00–19:30", "title": "Lakefront Sunset Contemplation", "detail": "Watch sunset reflections across the lake and reed beds.", "logistics": "Wooden boardwalk terrace."},
                {"time": "20:00–21:30", "title": "Cheonan Mushroom Shabu-Shabu Hot Pot Dinner", "detail": "Cook fresh mushrooms and thinly sliced beef in savory broth.", "logistics": "Station area dining room."}
            ],
            [
                {"label": "Scale & Monumentality", "text": "Gakwonsa's 60-ton Bronze Buddha is an unforgettable masterwork of 20th-century Buddhist casting."},
                {"label": "Lakeside Architectural Cafes", "text": "Seongseong Lake features striking modern minimalist cafes with floor-to-ceiling glass."}
            ],
            "Lunch: Anseo-dong buckwheat noodles and potato pancake. Dinner: Beef and mushroom shabu-shabu hot pot with hand-pulled noodles.",
            "Gakwonsa Temple is free admission; open year-round from dawn to dusk.",
            "Temple is free; Lunch ~₩12,000; Dinner ~₩22,000 per person.",
            "Photograph the Bronze Buddha from below to capture its monumental scale against Taejosan pine slopes.",
            "Daeungbojeon hall and lakefront cafes provide indoor comfort."
        ),
        # Day 12: Nov 12
        make_day(11, "Cheonan", "Astronomical Architecture & KTX Prep", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Hong Dae-yong Science Museum Architecture → Cheonan Central Market → KTX to Busan Prep",
            "Astronomical Memorial Architecture & Pre-Busan Rail Prep",
            [
                {"time": "10:00–12:30", "title": "Hong Dae-yong Memorial & Observatory Architecture", "detail": "Explore the astronomical pavilion and dome architecture honoring Joseon astronomer Hong Dae-yong.", "logistics": "Dongnam-gu Susan-myeon; 25-min taxi."},
                {"time": "13:00–14:30", "title": "Cheonan Namsan Central Market Lunch", "detail": "Enjoy hand-pulled knife-cut noodle soup (kalguksu) and handmade dumplings in the covered market.", "logistics": "Sajik-dong (walk from Cheonan Station)."},
                {"time": "15:00–17:00", "title": "Arario Sculpture Park Farewell Walk", "detail": "Final walk past Damien Hirst's 'Hymn' and Keith Haring sculptures.", "logistics": "Shinbu-dong Arario Plaza."},
                {"time": "17:30–19:30", "title": "Hotel Packing & KTX Ticket Check", "detail": "Pack primary luggage for Friday morning KTX to coastal Busan and verify seat assignments.", "logistics": "Hotel room."},
                {"time": "20:00–21:30", "title": "Cheonan Farewell Korean Feast", "detail": "Celebrate 5 nights in Cheonan with rich pork galbi barbecue.", "logistics": "Shinbu-dong dining lane."}
            ],
            [
                {"label": "Astronomical Heritage", "text": "Celebrates Korea's 18th-century scientific enlightenment and architectural observatories."},
                {"label": "Pre-Busan Preparation", "text": "Packing early ensures a relaxed Friday morning high-speed train directly to Busan."}
            ],
            "Lunch: Namsan Central Market handmade kalguksu and dumplings. Dinner: Charcoal-grilled pork galbi with cold noodles.",
            "Hong Dae-yong Science Museum closed on Mondays; entry ₩3,000.",
            "Museum ₩3,000; Lunch ~₩8,000; Dinner ~₩22,000 per person.",
            "Pack primary bags tonight for Friday morning KTX to Busan.",
            "Science Museum and Namsan Central Market are fully indoor."
        ),
        # Day 13: Nov 13
        make_day(12, "Busan", "Coastward Rail & Skyscraper Architecture", "Busan · Haeundae Beachfront",
            "KTX Cheonan-Asan to Busan (1h45m) → Haeundae Check-in → Marine City & The Bay 101",
            "Direct High-Speed Coastal Rail & Cyberpunk Skyscraper Reflections",
            [
                {"time": "10:00–11:45", "title": "KTX High-Speed Rail to Busan", "detail": "Smooth 1-hour 45-minute direct journey from Cheonan-Asan to Busan Station.", "logistics": "Direct Gyeongbu high-speed line."},
                {"time": "12:00–13:15", "title": "Busan Station Choryang Milmyeon Lunch", "detail": "Savor authentic cold wheat noodles and steamed dumplings.", "logistics": "Opposite Busan Station."},
                {"time": "13:45–15:00", "title": "Transfer to Haeundae Beach Base", "detail": "Check into Haeundae hotel (e.g. Felix by STX or L7 Haeundae).", "logistics": "Metro Line 2 or taxi across harbor bridge."},
                {"time": "15:30–18:00", "title": "Dongbaekseok Island & APEC Nurimaru House", "detail": "Walk the pine-forested island path to view APEC Nurimaru House, studying how traditional Korean pavilion design was integrated into modern glass architecture.", "logistics": "Paved oceanside walkway."},
                {"time": "18:30–21:30", "title": "The Bay 101 & Marine City Skyscraper Reflections", "detail": "Capture water-reflection photographs of Marine City's glittering glass skyscrapers and enjoy fish & chips on the open-air deck.", "logistics": "Dongbaek Station Line 2 Exit 1."}
            ],
            [
                {"label": "Direct Rail Speed", "text": "Direct KTX arrives in Busan by noon, maximizing afternoon coastal exploration."},
                {"label": "Skyscraper Architecture", "text": "Marine City's soaring glass residential towers create Korea's most futuristic coastal skyline."}
            ],
            "Lunch: Choryang Milmyeon (cold wheat noodles & dumplings). Dinner: The Bay 101 fish & chips / Haeundae market grilled seafood.",
            "Book KTX Cheonan-Asan→Busan on Korail app 30 days in advance.",
            "KTX ticket ~₩39,200; The Bay 101 access is free.",
            "Dongbaek Island trail is lighted at night; Nurimaru APEC House closes at 17:00.",
            "SEA LIFE Busan Aquarium on Haeundae beachfront provides indoor shelter."
        ),
        # Day 14: Nov 14
        make_day(13, "Busan", "Ocean Rails & 500-Drone Spectacular", "Busan · Haeundae Beachfront",
            "Haeundae Blueline Sky Capsule → Cheongsapo Harbor → Gwangalli Saturday Drone Show",
            "Retro-Futuristic Ocean Pods & 500-Drone Sky Ballet",
            [
                {"time": "09:30–11:30", "title": "Haeundae Blueline Park Sky Capsule (Mipo to Cheongsapo)", "detail": "Ride a private colorful Sky Capsule cabin suspended 10 meters above the sea along coastal cliff tracks.", "logistics": "Mipo Station; book tickets 2 weeks in advance."},
                {"time": "11:30–13:30", "title": "Cheongsapo Seaside Grilled Clam Feast", "detail": "Dine on live scallops, abalone, and clams grilled over briquettes with butter and cheese overlooking the twin lighthouses.", "logistics": "Cheongsapo harbor row."},
                {"time": "14:00–16:30", "title": "Cheongsapo Ocean Skywalk & Cafe Street", "detail": "Walk Daritdol Skywalk over breaking ocean waves and sip artisan coffee.", "logistics": "Cheongsapo waterfront."},
                {"time": "17:00–18:30", "title": "Gwangalli Beach Twilight Stroll", "detail": "Watch the sunset illuminate Gwangan Suspension Bridge.", "logistics": "Gwangan Station Line 2 Exit 3/5."},
                {"time": "19:00–21:30", "title": "Gwangalli Saturday Night 500-Drone Light Show & Craft Beer", "detail": "Witness 500+ synchronized LED drones paint 3D animated figures across the night sky above Gwangan Bridge, accompanied by Korean craft beer and fried chicken.", "logistics": "Gwangalli Beachfront (shows at 19:00 & 21:00)."}
            ],
            [
                {"label": "Ocean Sky Capsule Pods", "text": "Blueline Park seamlessly merges retro railway heritage with futuristic private cabin pods."},
                {"label": "Saturday Night Drone Miracle", "text": "Gwangalli M Drone Show is Korea's first permanent weekly synchronized drone spectacle."}
            ],
            "Lunch: Cheongsapo seaside grilled clams (jogae-gui) with butter and melted cheese. Dinner: Gwangalli beachfront Korean fried chicken and craft IPA / raw yellowtail sashimi.",
            "Book Blueline Sky Capsule 14 days in advance on official website (sells out rapidly).",
            "Sky Capsule 2-person pod ₩35,000; Drone show is free public viewing on the sand.",
            "Arrive on Gwangalli Beach 20 minutes before drone show for prime sand seating.",
            "Gwangalli beachfront cafes with floor-to-ceiling glass provide heated indoor viewing."
        ),
        # Day 15: Nov 15
        make_day(14, "Busan", "Hillside Murals & Marine Markets", "Busan · Haeundae Beachfront",
            "Gamcheon Culture Village → Jagalchi Marine Market → BIFF Square",
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
        make_day(15, "Busan", "Shipyard Amphitheaters & Coastal Tunnels", "Busan · Haeundae Beachfront",
            "P.ARK Yeongdo Culture Complex → Huinnyeoul Coastal Tunnel → Arte Museum",
            "Stepped Architectural Amphitheaters & Immersive Digital Media",
            [
                {"time": "10:00–12:30", "title": "P.ARK Culture Complex Yeongdo", "detail": "Tour the striking architectural masterpiece overlooking Busan harbor shipyards, featuring multi-tiered indoor and outdoor stepped amphitheaters, design exhibitions, and ocean lounges.", "logistics": "Yeongdo-gu; bus from Nampo Station or 25-min taxi from Haeundae."},
                {"time": "12:30–14:00", "title": "P.ARK Artisan Bakery & Cafe Lunch", "detail": "Enjoy artisan sourdough pizza, gourmet sandwiches, and specialty coffee overlooking the harbor.", "logistics": "Inside P.ARK complex."},
                {"time": "14:15–16:30", "title": "Arte Museum Busan (Immersive Digital Art)", "detail": "Experience monumental multi-sensory digital art spaces: infinite mirrored waterfalls, bioluminescent ocean waves, and interactive soundscapes.", "logistics": "Yeongdo Arte Museum."},
                {"time": "17:00–18:30", "title": "Huinnyeoul Coastal Sea Tunnel Sunset", "detail": "Walk the narrow cliffside pathways overlooking the sea and photograph the illuminated coastal rock tunnel.", "logistics": "Yeongdo coastal bus."},
                {"time": "19:30–21:30", "title": "Traditional Busan Dwaeji Gukbap Dinner", "detail": "Enjoy 24-hour simmered pork bone soup with boiled pork suyuk.", "logistics": "Nampo soup alley."}
            ],
            [
                {"label": "Avant-Garde Shipyard Architecture", "text": "P.ARK transforms commercial shipyard docks into an avant-garde cultural amphitheater."},
                {"label": "Immersive Art Innovation", "text": "Arte Museum Busan is Korea's largest digital media art destination, created by d'strict."}
            ],
            "Lunch: P.ARK Yeongdo artisan bakery pizza and pour-over coffee. Dinner: Traditional Nampo-dong Dwaeji Gukbap with suyuk.",
            "Arte Museum Busan tickets ₩19,000; P.ARK is free entry.",
            "Arte Museum ₩19,000; Huinnyeoul free; Dinner ~₩15,000 per person.",
            "Arte Museum has mirrored floors; lockers available for bags.",
            "P.ARK and Arte Museum are completely indoor and weatherproof."
        ),
        # Day 17: Nov 17
        make_day(16, "Busan", "Eco-Art & Vertical Gardens", "Busan · Haeundae Beachfront",
            "MoCA Busan (Museum of Contemporary Art Eulsukdo) → Patrick Blanc Vertical Garden → Centum Cinema Center",
            "Patrick Blanc Vertical Gardens & Cantilevered LED Roofs",
            [
                {"time": "10:00–13:00", "title": "Museum of Contemporary Art Busan (MoCA Busan)", "detail": "Explore the striking eco-art museum on Eulsukdo Island featuring the monumental living vertical garden facade by French botanist Patrick Blanc and cutting-edge media art installations.", "logistics": "Hadan Station Line 1 Exit 3 + Bus 168/3/55 or 30-min taxi."},
                {"time": "13:15–14:30", "title": "Eulsukdo Eco-Park Riverside Lunch", "detail": "Enjoy fresh clam noodle soup or Korean rice bowl overlooking Nakdong River wetlands.", "logistics": "Eulsukdo cultural center cafe."},
                {"time": "15:15–17:30", "title": "Busan Cinema Center (BIFF Venue)", "detail": "Marvel at the Guinness World Record cantilevered roof spanning 85 meters without support columns, covered with 42,600 dynamic LED ceiling lights.", "logistics": "Centum City Station Line 2 Exit 6 or 12."},
                {"time": "18:00–19:30", "title": "Centum City Modern Architecture Walk", "detail": "Stroll Suyeong River promenade viewing modern bridge architecture.", "logistics": "Centum City."},
                {"time": "20:00–21:30", "title": "Shinsegae Sky Lounge Modern Korean Dinner", "detail": "Enjoy contemporary Korean dining overlooking Suyeong River.", "logistics": "Shinsegae Centum City 9F."}
            ],
            [
                {"label": "Botanical Living Facade", "text": "Patrick Blanc's vertical garden on MoCA Busan is one of the largest living plant installations in Asia."},
                {"label": "Guinness Record Architecture", "text": "The Busan Cinema Center is an international engineering marvel designed by Coop Himmelb(l)au."}
            ],
            "Lunch: Eulsukdo fresh clam soup and vegetable bibimbap. Dinner: Modern Korean seasonal tasting dinner at Shinsegae Centum City 9F.",
            "MoCA Busan closed on Mondays; free admission to permanent exhibitions.",
            "Museum is free; Cinema Center exterior free; Dinner ~₩32,000 per person.",
            "MoCA Busan is fully indoor with spacious galleries.",
            "Shinsegae complex and Cinema Center are weatherproof."
        ),
        # Day 18: Nov 18
        make_day(17, "Busan", "Wire Factory Revival & Thermal Spas", "Busan · Haeundae Beachfront",
            "F1963 Cultural Complex (Wire Factory to Arts Hub) → Centum City Spa Land Thermal Saunas",
            "Industrial Factory Transformation & Luxury Thermal Hydrotherapy",
            [
                {"time": "10:00–12:30", "title": "F1963 Cultural Complex (Former Factory)", "detail": "Explore the visionary industrial architecture of a 1963 wire rope factory converted into an eco-arts complex, featuring Yes24 giant book store, Kukje Gallery, and bamboo gardens.", "logistics": "Mangmi Station Line 3 or 15-min taxi from Haeundae."},
                {"time": "12:30–14:00", "title": "Terarosa Specialty Coffee & Bakery Lunch", "detail": "Enjoy pour-over specialty coffee and artisan sourdough in the dramatic factory interior preserved with original wire spools and steel trusses.", "logistics": "Inside F1963."},
                {"time": "14:30–18:30", "title": "Spa Land Centum City Luxury Thermal Bathhouse", "detail": "Spend 4 hours immersed in 18 natural mineral pools and 13 aesthetic themed saunas with heated ergonomic loungers.", "logistics": "Centum City Station Line 2 direct basement connection."},
                {"time": "19:00–21:00", "title": "Gourmet Korean Fried Chicken & Draft Beer", "detail": "Crispy golden chicken on Haeundae avenue.", "logistics": "Haeundae Gunam-ro."}
            ],
            [
                {"label": "Industrial Adaptive Reuse", "text": "F1963 is a masterclass in post-industrial architectural revitalization."},
                {"label": "Ultimate Urban Spa", "text": "Spa Land Centum City delivers the world's most luxurious urban jjimjilbang experience."}
            ],
            "Lunch: Terarosa F1963 artisan sourdough sandwich and coffee. Dinner: Haeundae gourmet Korean fried chicken and draft beer.",
            "F1963 exhibitions and bookstore are free admission; Spa Land 4-hr pass ~₩23,000.",
            "F1963 free; Spa Land ₩23,000; Dinner ~₩22,000 per person.",
            "Spa Land does not admit children under 7; maintains serene adult relaxation atmosphere.",
            "This entire day is 100% enclosed, heated, and weatherproof."
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
                {"time": "12:30–13:00", "title": "Boarding & Takeoff", "detail": "Board aircraft for the return flight home with unforgettable memories of world-class architecture, contemporary art, and urban design across Korea.", "logistics": "Gates close 15 minutes before scheduled departure."}
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
        {"label": "Contemporary Art", "value": "5/5", "tone": "good"},
        {"label": "Pritzker Architecture", "value": "5/5", "tone": "good"},
        {"label": "World Sculpture Parks", "value": "5/5", "tone": "good"},
        {"label": "Post-Industrial Reuse", "value": "5/5", "tone": "good"}
    ]

    return {
        "id": "seoul-cheonan-busan-arts",
        "shortTitle": "Seoul · Cheonan · Busan (Contemporary Art & Architecture)",
        "title": "World Sculpture Parks, Urban Design & Creative Hubs (Contemporary Art & Architecture)",
        "routeLabel": "Seoul (7N) → Cheonan (5N) → Busan (7N) → Seoul (2N)",
        "badge": "World Sculpture Parks & Avant-Garde Architecture",
        "bestFor": "Architects, designers, contemporary art curators, sculptors, and creative travelers captivated by Pritzker Prize architecture, monumental public sculpture plazas (Damien Hirst, Keith Haring), adaptive reuse lofts, and cutting-edge digital media art.",
        "decisionSummary": "A visionary aesthetic journey spanning Kim Swoo-geun's brutalist SPACE building, Zaha Hadid's DDP, and the Leeum Pritzker trio in Seoul, Cheonan's world-renowned Arario Sculpture Park (Damien Hirst, Keith Haring), and Busan's Patrick Blanc vertical garden at MoCA, P.ARK shipyard amphitheater, and F1963 wire factory arts space.",
        "recommendation": "Choose this route if your travel passion is world-class contemporary art, innovative urban architecture, and post-industrial creative transformations.",
        "tradeoff": "More time dedicated to galleries, architectural masterworks, and sculpture parks than traditional outdoor sports.",
        "scorecard": scorecard,
        "bases": get_scb_common_bases(),
        "transfers": get_scb_common_transfers(),
        "budgetScenarios": get_scb_budget_scenarios(),
        "bookingPriorities": get_scb_booking_priorities(),
        "days": days
    }
