#!/usr/bin/env python3
"""Route Blueprint: Seoul · Daejeon · Busan (K-Innovation, High-Tech & Pop Culture Odyssey)."""

from scripts.generate_all_itineraries import make_day
from scripts.itinerary_builder_sdb import (
    get_sdb_common_bases,
    get_sdb_common_transfers,
    get_sdb_budget_scenarios,
    get_sdb_booking_priorities
)

def get_sdb_modern():
    days = [
        # Day 1: Nov 1
        make_day(0, "Seoul", "Arrival", "Seoul · Myeongdong / Seoul Station edge",
            "ICN arrival at 21:00 → high-tech eSIM/connectivity activation → hotel check-in → sleep",
            "Late Landing & High-Tech Connectivity Activation",
            [
                {"time": "21:00–22:15", "title": "ICN Arrival & Digital Prep", "detail": "Clear immigration and activate high-speed 5G eSIM / pocket Wi-Fi and T-Money digital transit apps.", "logistics": "Terminal 1 or 2."},
                {"time": "22:30–23:45", "title": "Direct Transfer to Central Seoul Base", "detail": "Airport Limousine Bus or official taxi directly to Myeongdong / Seoul Station hotel.", "logistics": "Door-to-door transit."},
                {"time": "23:45–00:30", "title": "Hotel Check-in & Rest", "detail": "Check into hotel room, charge all mobile devices and power banks, and get restful sleep.", "logistics": "Notify hotel of late arrival."}
            ],
            [
                {"label": "Digital Setup", "text": "Activating seamless connectivity on arrival powers navigation across high-tech hubs and esports venues."},
                {"label": "Arrival Rest", "text": "Save energy for tomorrow's futuristic architectural exploration."}
            ],
            "Late-night convenience store snacks (ramyun, banana milk, samgak kimbap).",
            "Confirm late check-in with hotel in writing.",
            "Limousine Bus ~₩17,000.",
            "Charge power banks overnight; camera and phone battery use will be high.",
            "Hotel front desk provides 24-hour service."
        ),
        # Day 2: Nov 2
        make_day(1, "Seoul", "Futuristic Architecture & Design", "Seoul · Myeongdong / Seoul Station edge",
            "Dongdaemun Design Plaza (DDP) Architecture → DDP Design Labs → Cheonggyecheon Stream Night Lights",
            "Zaha Hadid Curves, Design Showrooms & Urban Stream Lights",
            [
                {"time": "09:30–12:30", "title": "Dongdaemun Design Plaza (DDP)", "detail": "Explore Zaha Hadid's neo-futuristic architectural masterpiece, studying the 45,133 curved aluminum panels, D-Light design labs, and Seoul Smart City exhibitions.", "logistics": "Dongdaemun History & Culture Park Station Line 2/4/5 Exit 1."},
                {"time": "12:45–14:15", "title": "DDP Gourmet Arcade Lunch", "detail": "Enjoy Korean modern fusion dining or artisan rice bowls in DDP lower concourse.", "logistics": "DDP B2 design pathway."},
                {"time": "14:30–17:00", "title": "Dongdaemun Fashion Town & K-Fashion Malls", "detail": "Browse multi-story fashion towers (DOOTA, apM Place) featuring emerging Korean indie streetwear designers.", "logistics": "Dongdaemun fashion district."},
                {"time": "17:30–19:30", "title": "Cheonggyecheon Stream Evening LED Stroll", "detail": "Walk along the sunken urban stream as night lighting and digital art projections illuminate the water.", "logistics": "Walk west along Cheonggyecheon toward Gwanghwamun."},
                {"time": "20:00–21:30", "title": "Sindang-dong Tteokbokki Town Feasting", "detail": "Dine on bubbling tabletop spicy rice cakes with ramen and dumplings.", "logistics": "Sindang Station Line 2/6 Exit 8."}
            ],
            [
                {"label": "Architectural Landmark", "text": "DDP is the global centerpiece of Seoul's World Design Capital heritage."},
                {"label": "Urban Renewal", "text": "Cheonggyecheon illustrates how highway infrastructure was transformed into a green eco-stream."}
            ],
            "Lunch: DDP modern Korean dining. Dinner: Sindang-dong bubbling tabletop tteokbokki hot pot with cheese.",
            "DDP exterior open 24/7; design labs open 10:00–20:00.",
            "DDP exterior free; Exhibits ~₩15,000; Dinner ~₩14,000 per person.",
            "DDP curved pathways can be disorienting; use digital floor maps.",
            "DDP interior and connected underground malls provide complete weather shelter."
        ),
        # Day 3: Nov 3
        make_day(2, "Seoul", "Trend Capital & Concept Lofts", "Seoul · Myeongdong / Seoul Station edge",
            "Seongsu Industrial Concept Lofts (Tamburins, Gentle Monster) → Seoul Forest Walk",
            "Transformed Red-Brick Lofts, Pop-Up Flagships & Scent Architecture",
            [
                {"time": "10:00–13:00", "title": "Seongsu-dong Flagship Boutiques (Yeonmujang-gil)", "detail": "Experience mind-bending kinetic art and multi-sensory concept stores: Gentle Monster / Tamburins Haus Nowhere, Daelim Warehouse, and Musinsa Standard.", "logistics": "Seongsu Station Line 2 Exit 3."},
                {"time": "13:15–14:45", "title": "Seongsu Industrial Loft Dining Lunch", "detail": "Dine in converted shoe factory cafes on artisan pasta, gourmet smashburgers, or modern Korean bowls.", "logistics": "Yeonmujang-gil lane."},
                {"time": "15:00–17:00", "title": "K-Beauty Flagships & Scent Labs", "detail": "Test customized skincare and create personalized fragrance blends in boutique Seongsu perfume ateliers.", "logistics": "Seongsu fragrance corridor."},
                {"time": "17:30–19:30", "title": "Seoul Forest Autumn Canopy Walk", "detail": "Stroll golden ginkgo groves and enjoy the outdoor art sculptures.", "logistics": "Seoul Forest Station Suin-Bundang Line Exit 4."},
                {"time": "20:00–22:00", "title": "Seongsu Modern Craft Makgeolli Pub", "detail": "Pair bubbly artisanal rice wine with crispy truffle potato pancakes.", "logistics": "Seongsu dining quarter."}
            ],
            [
                {"label": "Brooklyn of Seoul", "text": "Seongsu is the global epicentre of Korean youth fashion, luxury pop-ups, and experiential retail."},
                {"label": "Sensory Retail Architecture", "text": "Gentle Monster and Tamburins redefine physical retail as immersive art galleries."}
            ],
            "Lunch: Seongsu Daelim Warehouse cafe lunch. Dinner: Seongsu modern craft pub (crispy truffle gamjajeon and sparkling makgeolli).",
            "Seongsu flagship boutiques open at 11:00 AM; free entry.",
            "Free boutique visits; Lunch ~₩18,000; Dinner ~₩28,000 per person.",
            "Popular pop-ups may have tablet queue reservations; register phone number on arrival.",
            "Seongsu multi-story loft cafes and galleries are completely indoor."
        ),
        # Day 4: Nov 4
        make_day(3, "Seoul", "K-Pop Busking & Indie Culture", "Seoul · Myeongdong / Seoul Station edge",
            "Hongdae K-Pop Busking Streets → KT&G Sangsangmadang → Gyeongui Line Forest Park",
            "Youth Street Buskers, Indie Art Hubs & K-Pop Beats",
            [
                {"time": "10:30–13:00", "title": "Gyeongui Line Forest Park & Yeonnam-dong", "detail": "Walk the transformed green railway line, browse boutique stationery stores (Object), and sample salt bread.", "logistics": "Hongik Univ. Station Line 2/AREX Exit 3."},
                {"time": "13:00–14:30", "title": "Yeonnam-dong Fusion Dining Lunch", "detail": "Enjoy Japanese-Korean katsu or handmade burger bowls.", "logistics": "Yeonnam cafe road."},
                {"time": "14:45–17:00", "title": "KT&G Sangsangmadang & Hongdae Design Shops", "detail": "Explore the 7-floor independent cultural complex featuring indie design goods, photo galleries, and music halls.", "logistics": "Hongdae main pedestrian street."},
                {"time": "17:30–19:30", "title": "Hongdae Live Street Busking Spectacular", "detail": "Watch talented young dance crews perform synchronized K-pop choreographies and live acoustic sets on the illuminated pedestrian strip.", "logistics": "Hongdae Busking Zone (Eoulmadang-ro)."},
                {"time": "20:00–22:00", "title": "Mapo Charcoal Pork Ribs (Galbi) Barbecue", "detail": "Feast on marinated pork ribs grilled over real charcoal.", "logistics": "Mapo BBQ alley."}
            ],
            [
                {"label": "Living K-Pop Street Culture", "text": "Hongdae busking is where future K-pop stars and underground indie musicians hone their stagecraft in front of enthusiastic crowds."},
                {"label": "Creative Energy", "text": "Vibrant, creative energy that defines modern Korean Gen-Z lifestyle."}
            ],
            "Lunch: Yeonnam-dong handmade katsu or burger. Dinner: Mapo charcoal-grilled pork galbi with cold dongchimi noodles.",
            "Busking performances peak between 17:00 and 21:00 daily (weather permitting).",
            "Sangsangmadang entry free; Dinner ~₩25,000 per person.",
            "Keep personal belongings zipped in crowded busking street circles.",
            "KT&G Sangsangmadang and Hongdae underground arcades provide indoor shelter."
        ),
        # Day 5: Nov 5
        make_day(4, "Seoul", "K-Star Road & Mega Libraries", "Seoul · Myeongdong / Seoul Station edge",
            "Starfield COEX Library → SM KWANGYA Flagship → K-Star Road Gangnam",
            "Mega Book Towers, K-Pop Metaverse & Futuristic Malls",
            [
                {"time": "10:00–12:30", "title": "Starfield Library COEX Mall", "detail": "Photograph the monumental 13-meter tall open book towers and explore Asia's largest underground shopping and digital lifestyle mall.", "logistics": "Samseong Station Line 2 Exit 6 or Bongeunsa Station Line 9 Exit 7."},
                {"time": "12:30–14:00", "title": "COEX Parnas Gourmet Mall Lunch", "detail": "Dine on modern Korean beef gomtang or royal bibimbap.", "logistics": "Directly connected to COEX."},
                {"time": "14:15–16:00", "title": "SM Entertainment KWANGYA Seoul Flagship", "detail": "Experience the high-tech immersive K-pop merchandise and multimedia metaverse showroom in Seoul Forest / Seongsu.", "logistics": "Seoul Forest Station Exit 4 (Acro Seoul Forest B1)."},
                {"time": "16:30–18:30", "title": "Gangnam K-Star Road & Apgujeong Rodeo", "detail": "Walk the glamorous avenue lined with artistic K-pop GangnamDol bear statues (BTS, EXO, Blackpink).", "logistics": "Apgujeong Rodeo Station Exit 2."},
                {"time": "19:00–21:30", "title": "Gangnam Korean Fried Chicken & Craft Beer", "detail": "Enjoy crispy golden chicken and craft IPAs in Gangnam.", "logistics": "Gangnam Station Line 2/Shinbundang Line Exit 11."}
            ],
            [
                {"label": "Global Pop Culture Hub", "text": "Connects international K-pop metaverse spaces with Gangnam's world-famous luxury districts."},
                {"label": "Iconic Book Architecture", "text": "Starfield Library is an international triumph of public architectural design."}
            ],
            "Lunch: Hadongkwan 80-year Gomtang beef soup at COEX. Dinner: Gangnam artisan Korean fried chicken and craft beer.",
            "Starfield Library and SM KWANGYA are free admission; open daily.",
            "Free library and K-Star road; Lunch ~₩16,000; Dinner ~₩22,000 per person.",
            "COEX mall is vast; look for floor navigation screens.",
            "COEX mall is 100% enclosed, heated, and weatherproof."
        ),
        # Day 6: Nov 6
        make_day(5, "Seoul", "Esports Arena & Gaming Culture", "Seoul · Myeongdong / Seoul Station edge",
            "LoL Park LCK Esports Arena → T1 Base Camp & VR Gaming Hub → Insadong Retro",
            "Global Esports Colosseums & Next-Gen PC Bangs",
            [
                {"time": "10:30–13:00", "title": "LoL Park LCK Arena (League of Legends Korea HQ)", "detail": "Tour the futuristic circular esports arena, viewing championship trophies, life-sized champion statues, player handprints, and Riot Store merchandise.", "logistics": "Jonggak Station Line 1 Exit 1 (Gran Seoul 3F)."},
                {"time": "13:15–14:30", "title": "Gran Seoul Gourmet Hall Lunch", "detail": "Enjoy modern Korean spicy pork or chicken cutlet in the tech tower concourse.", "logistics": "Gran Seoul 1F/B1."},
                {"time": "14:45–17:00", "title": "T1 Base Camp & Premium Next-Gen PC Bang Experience", "detail": "Experience Korea's world-famous high-spec gaming cafe culture at the official T1 team cafe with RTX graphics cards, mechanical keyboards, and table-delivered snacks.", "logistics": "Hongdae or Gangnam T1 facility."},
                {"time": "17:30–19:30", "title": "Insadong Ssamzigil & Craft Alleys", "detail": "Contrast high-tech gaming with traditional spiral courtyard crafts.", "logistics": "Anguk Station Line 3."},
                {"time": "20:00–21:30", "title": "Jongno Korean Charcoal BBQ Dinner", "detail": "Feast on thick pork neck and kimchi stew.", "logistics": "Jongno dining lane."}
            ],
            [
                {"label": "Global Esports Capital", "text": "Seoul is the undisputed capital of global competitive gaming; LoL Park is the cathedral of League of Legends."},
                {"label": "PC Bang Culture", "text": "Korean PC bangs offer world-class gaming hardware and instant chef-cooked food delivery to your desk."}
            ],
            "Lunch: Gran Seoul gourmet katsu or spicy pork rice bowl. Afternoon: PC Bang gourmet snacks (tteokbokki, hot dogs, iced coffee). Dinner: Jongno charcoal-grilled pork barbecue.",
            "LoL Park exhibition hall is free entry; match tickets sold separately on Interpark if in-season.",
            "LoL Park free; PC Bang 2 hours ~₩4,000; Dinner ~₩25,000 per person.",
            "PC Bangs accept cash and cards; English language interface available.",
            "Gran Seoul and LoL Park are modern indoor high-tech towers."
        ),
        # Day 7: Nov 7
        make_day(6, "Seoul", "Futuristic Atriums & Riverside Ramen", "Seoul · Myeongdong / Seoul Station edge",
            "Yeouido The Hyundai Seoul Indoor Garden Atrium → Han River Automated Ramen → Sunday KTX Prep",
            "Indoor Forest Architecture, Automated Ramen & Rail Prep",
            [
                {"time": "10:30–13:30", "title": "The Hyundai Seoul (Sounds Forest Atrium)", "detail": "Tour Seoul's most progressive department store, featuring a 5th-floor indoor forest garden under natural skylights, robotic barista arms, and cutting-edge design pop-ups.", "logistics": "Yeouido Station Line 5/9 direct underground walkway."},
                {"time": "13:30–15:00", "title": "Tasty Seoul Gourmet Food Hall Lunch", "detail": "Sample gourmet delicacies from Korea's hottest food trucks and bakery pop-ups.", "logistics": "The Hyundai Seoul B1."},
                {"time": "15:30–17:30", "title": "Yeouido Hangang Park & Automated Ramen Cooking", "detail": "Experience the beloved Seoul ritual: purchasing instant ramen at a riverside convenience store and cooking it in an automated induction boiler on the Han River bank.", "logistics": "Yeouinaru Station Line 5 Exit 2."},
                {"time": "18:00–19:30", "title": "Seoul Station Hotel Packing & KTX Verification", "detail": "Pack luggage for Sunday morning KTX to Daejeon and check reserved seats.", "logistics": "Seoul Station hotel."},
                {"time": "20:00–21:30", "title": "Myeongdong Korean Dakgalbi Feast", "detail": "Savor spicy stir-fried chicken with mozzarella cheese and fried rice.", "logistics": "Myeongdong dining area."}
            ],
            [
                {"label": "Retail Architecture of the Future", "text": "The Hyundai Seoul replaces traditional department store layouts with open green spaces and public art."},
                {"label": "Automated Riverbank Culture", "text": "Hangang automated ramen is an iconic everyday Seoul cultural experience."}
            ],
            "Lunch: The Hyundai Seoul gourmet food hall. Afternoon: Han River convenience store automated boiling ramen. Dinner: Myeongdong spicy chicken dakgalbi with cheese.",
            "The Hyundai Seoul is open daily 10:30–20:00 (extended to 20:30 on weekends).",
            "Hyundai Seoul free entry; Hangang ramen ~₩4,000; Dinner ~₩20,000 per person.",
            "Follow the numbered buttons on automated ramen machines for automatic water dispensing.",
            "The Hyundai Seoul is completely enclosed and weatherproof."
        ),
        # Day 8: Nov 8
        make_day(7, "Daejeon", "City Transition & Science Sunset", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Morning KTX to Daejeon → Expo Science Park Hanbit Tower Media Facade → Expo Bridge Lights",
            "High-Speed Rail into Korea's Silicon Valley",
            [
                {"time": "09:30–10:30", "title": "KTX High-Speed Rail Seoul to Daejeon", "detail": "55-minute smooth high-speed transit from Seoul Station to Daejeon Station.", "logistics": "Direct Gyeongbu line."},
                {"time": "11:00–13:00", "title": "Sung Sim Dang 1956 Bakery & Downtown Walk", "detail": "Sample legendary Twigim Soboro (fried streusel pastry) and browse Jungang Market.", "logistics": "Jungangno Station Line 1 Exit 2."},
                {"time": "13:30–15:30", "title": "Hotel Check-in & Base Setup", "detail": "Check into Daejeon hotel (e.g. Hotel Onoma or Ramada Yuseong) and refresh.", "logistics": "Metro Line 1."},
                {"time": "16:00–18:30", "title": "Expo Science Park & Hanbit Tower Media Facade", "detail": "Visit the 1993 Daejeon Expo site, ascend the 93-meter Hanbit Tower for panoramic city sunset views, and watch digital media projections.", "logistics": "Near Shinsegae Complex."},
                {"time": "19:00–21:00", "title": "Expo Bridge Night LED Light Show & Dubu Duruchigi Dinner", "detail": "Photograph the dual red and blue illuminated arches of Expo Bridge reflecting in the Gapcheon River, then enjoy Daejeon's famous spicy braised tofu with noodles.", "logistics": "Gapcheon River / Daeheung-dong."}
            ],
            [
                {"label": "Science City Heritage", "text": "Daejeon is Korea's recognized science capital, hosting the nation's premier research institutes."},
                {"label": "Media Facade Spectacle", "text": "Hanbit Tower and Expo Bridge create a futuristic light show across the river."}
            ],
            "Lunch: Sung Sim Dang fresh pastries and bakery brunch. Dinner: Famous Daejeon spicy Dubu Duruchigi (braised tofu stir-fry with noodles).",
            "Book KTX train 30 days prior on Korail app.",
            "KTX ticket ~₩23,700; Hanbit Tower observatory free/minimal; Dinner ~₩18,000 per person.",
            "Expo Bridge light show illuminates at dusk; great photo spot from Gapcheon south bank.",
            "Daejeon Shinsegae complex and Hanbit Tower provide indoor warmth."
        ),
        # Day 9: Nov 9
        make_day(8, "Daejeon", "Science Supercluster & KAIST", "Daejeon · Yuseong Hot Springs / Dunsan",
            "National Science Museum Interactive Labs → KAIST Innovation Campus Tour → Yuseong Foot Bath",
            "National Science Labs, Robotics & Thermal Spring Relief",
            [
                {"time": "09:30–12:30", "title": "National Science Museum (Hall of Science & Technology)", "detail": "Experience hands-on physics simulators, aerospace simulators, robotics demonstrations, and interactive natural history exhibits.", "logistics": "Yuseong-gu Daedeok Science Town; City Bus 104/121."},
                {"time": "12:45–14:00", "title": "Daedeok Innopolis Research Valley Lunch", "detail": "Dine on Korean stone-pot bibimbap or gourmet katsu near KAIST campus.", "logistics": "Eoeun-dong / Gung-dong student village."},
                {"time": "14:15–16:30", "title": "KAIST (Korea Advanced Institute of Science & Tech) Campus", "detail": "Walk the landscaped campus of Korea's premier MIT equivalent, visiting student innovation labs, the scenic duck pond, and tech incubators.", "logistics": "KAIST Main Campus."},
                {"time": "17:00–18:30", "title": "Yuseong Hot Springs Outdoor Foot Bath Park", "detail": "Soak feet in 42°C natural alkaline hot spring waters in the landscaped public thermal park.", "logistics": "Yuseong Spa Station Line 1 Exit 7 (free entry)."},
                {"time": "19:00–21:00", "title": "Yuseong Herbal Duck Stew (Oritang) Dinner", "detail": "Feast on rich duck stew simmered with toasted perilla seeds and seasonal greens.", "logistics": "Yuseong Hot Springs alley."}
            ],
            [
                {"label": "Silicon Valley of Korea", "text": "Daedeok Innopolis hosts over 20,000 PhD researchers and 26 national research institutes."},
                {"label": "Campus Innovation", "text": "KAIST is the cradle of Korean robotics (HUBO) and artificial intelligence advancements."}
            ],
            "Lunch: KAIST student boulevard stone-pot bibimbap. Dinner: Yuseong rich Oritang duck stew with toasted perilla seeds.",
            "National Science Museum Hall of Science is free; planetarium is ₩2,000.",
            "Museum free; Foot bath free; Dinner ~₩25,000 per person.",
            "Bring a small towel for drying feet after Yuseong outdoor foot bath.",
            "National Science Museum is fully enclosed and heated."
        ),
        # Day 10: Nov 10
        make_day(9, "Daejeon", "Robotic Bakeries & Sky Lounges", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Sung Sim Dang DCC Robotic Bakery Lab → Shinsegae 38F Sky Terrace → Modern Art Walk",
            "Automated Bakery Showrooms & 38th-Floor River Vistas",
            [
                {"time": "10:00–12:30", "title": "Sung Sim Dang DCC Robotic Bakery Lab", "detail": "Witness robotic tray delivery systems and sample freshly pulled artisanal pastries, walnut pies, and brioches.", "logistics": "Daejeon Convention Center (DCC) 1F."},
                {"time": "13:00–15:00", "title": "Shinsegae Art & Science Gourmet Market Lunch", "detail": "Enjoy gourmet Korean noodles or modern bibimbap in the upscale food hall.", "logistics": "Hotel Onoma / Shinsegae Complex B1."},
                {"time": "15:15–17:00", "title": "Shinsegae 38F Sky Terrace & Starbucks", "detail": "Ride the express elevator to the 38th-floor observation lounge overlooking the Gapcheon River and Daejeon valley.", "logistics": "Shinsegae Tower 38F."},
                {"time": "17:30–19:30", "title": "Lee Ungno Museum & Modern Sculpture Park", "detail": "Explore the award-winning white stone architecture and abstract modern calligraphy paintings of Lee Ungno.", "logistics": "Expo Park cultural grounds."},
                {"time": "20:00–21:30", "title": "Daejeon Hand-Cut Clam Kalguksu & Pork Suyuk", "detail": "Enjoy rich clam broth noodles and tender boiled pork belly.", "logistics": "Dunsan dining street."}
            ],
            [
                {"label": "Pastry Innovation", "text": "DCC branch combines Sung Sim Dang's 70-year pastry mastery with modern robotic logistics."},
                {"label": "Panoramic River View", "text": "38F Sky Terrace offers the highest public vista in central Korea."}
            ],
            "Lunch: Shinsegae gourmet food hall. Afternoon: Sky lounge coffee & bakery treat. Dinner: Famous Daejeon clam kalguksu with pork suyuk.",
            "Lee Ungno Museum closed on Mondays; entry ₩1,000.",
            "Museum ₩1,000; Sky terrace free access; Dinner ~₩20,000 per person.",
            "Dress warmly for rooftop sky terrace in November evening breezes.",
            "DCC and Shinsegae complexes are 100% indoor and weatherproof."
        ),
        # Day 11: Nov 11
        make_day(10, "Daejeon", "Giant LED Canopy & Retro Gaming", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Daejeon Skyroad 214-Meter LED Canopy → Jung-gu Retro Arcades → Thermal Bath",
            "Monumental LED Canopies & Urban Retro Arcades",
            [
                {"time": "10:30–13:00", "title": "Hanbat Arboretum Autumn Stroll", "detail": "Walk through golden metasequoias and outdoor botanical trails.", "logistics": "Govt Complex Station Line 1."},
                {"time": "13:15–14:30", "title": "Dunsan Cafe Boulevard Lunch", "detail": "Enjoy fresh tonkatsu or Korean rice bowls.", "logistics": "Dunsan central avenue."},
                {"time": "15:00–17:30", "title": "Yuseong Mineral Hot Springs Thermal Bath", "detail": "Relax and recharge in natural mineral waters.", "logistics": "Yuseong Onsen bathhouse."},
                {"time": "18:00–20:00", "title": "Daejeon Skyroad (214-Meter Mega LED Canopy)", "detail": "Walk beneath the colossal 214-meter-long overhead LED arcade screen showcasing digital media art, interactive games, and smartphone video feeds above Jung-gu shopping street.", "logistics": "Jungangno Station Line 1 Exit 1."},
                {"time": "20:30–22:00", "title": "Daejeon Charcoal Pork Galbi BBQ Feast", "detail": "Enjoy sweet soy-marinated pork ribs grilled over real charcoal.", "logistics": "Jungangno / Daeheung-dong."}
            ],
            [
                {"label": "High-Tech Street Canopy", "text": "Daejeon Skyroad is one of Asia's largest overhead public digital LED screens."},
                {"label": "Retro Youth Hub", "text": "Jungangno combines modern digital spectacles with lively youth shopping streets."}
            ],
            "Lunch: Dunsan tonkatsu or rice bowl. Dinner: Jungangno charcoal-grilled pork galbi with cold noodles.",
            "Skyroad LED media shows operate in the evenings starting from 18:00 (free).",
            "Skyroad free; Hot spring ~₩10,000; Dinner ~₩25,000 per person.",
            "Skyroad screen shows interactive smartphone messages from visitors via QR code.",
            "Jungangno underground shopping mall provides 1km of covered retail."
        ),
        # Day 12: Nov 12
        make_day(11, "Daejeon", "Aerospace Research & Lake Views", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Korea Aerospace & Astronomy Exhibits → Daecheongho Lake Sunset Stroll",
            "Satellite Innovation, Space Exploration & Scenic Lakes",
            [
                {"time": "09:30–12:30", "title": "National Science Museum Space & Astronomical Pavilion", "detail": "Explore Korea's Nuri rocket launch vehicle models, lunar orbiter Danuri exhibits, and planetarium dome cinema.", "logistics": "Daedeok Science Town; City Bus 104."},
                {"time": "12:45–14:15", "title": "Lakeside Mountain Mushroom Stew Lunch", "detail": "Enjoy fresh mushroom casserole and acorn pancakes near Daecheong Dam.", "logistics": "Daecheong Dam restaurant row."},
                {"time": "14:45–17:00", "title": "Daecheongho Lake Waterfront Boardwalk", "detail": "Walk the wooden boardwalks along serene Daecheongho Lake, capturing shimmering water reflections and autumn reed fields.", "logistics": "Water Culture Center."},
                {"time": "17:30–19:30", "title": "Daejeon Hotel Packing & Train Verification", "detail": "Return to hotel, organize bags for Friday KTX to Busan, and check seat reservations.", "logistics": "Yuseong hotel base."},
                {"time": "20:00–21:30", "title": "Daejeon Farewell Hanwoo Bulgogi Dinner", "detail": "Celebrate 5 nights in Daejeon with sizzling Hanwoo beef bulgogi.", "logistics": "Yuseong / Dunsan."}
            ],
            [
                {"label": "Space Tech Milestones", "text": "Highlights Korea's rapid emergence as an independent global spacefaring nation."},
                {"label": "Daejeon Completion", "text": "Concludes Daejeon's science chapter before Friday's coastal rail trip to Busan."}
            ],
            "Lunch: Daecheong Dam wild mushroom stew and potato pancake. Dinner: Sizzling Hanwoo beef bulgogi with seasonal mountain side dishes.",
            "Planetarium show tickets ₩2,000 (book at museum counter).",
            "Planetarium ₩2,000; Lunch ~₩16,000; Dinner ~₩25,000 per person.",
            "Pack primary bags tonight for Friday morning KTX to Busan.",
            "Water Culture Center and Space Pavilion are completely indoor."
        ),
        # Day 13: Nov 13
        make_day(12, "Busan", "Coastward Rail & Skyscraper Skyline", "Busan · Haeundae Beachfront",
            "KTX Daejeon to Busan (1h30m) → Haeundae Beach Check-in → The Bay 101 Marine City Reflection",
            "High-Speed Coastal Transit & Gleaming Cyberpunk Skylines",
            [
                {"time": "10:00–11:30", "title": "KTX High-Speed Rail to Busan", "detail": "90-minute smooth high-speed transit arriving at Busan Station on the southern sea.", "logistics": "Board train at Daejeon Station."},
                {"time": "11:45–13:15", "title": "Busan Station Choryang Milmyeon Lunch", "detail": "Taste authentic cold wheat noodles and giant steamed mandu.", "logistics": "Opposite Busan Station."},
                {"time": "13:45–15:00", "title": "Transfer to Haeundae Beach Base", "detail": "Check into Haeundae hotel (e.g. L7 Haeundae or Signiel Busan).", "logistics": "Metro Line 2 or taxi across harbor bridge."},
                {"time": "15:30–18:00", "title": "Haeundae Beachfront & Gunam-ro Avenue Walk", "detail": "Explore the pedestrian boulevard filled with digital photo booths, street musicians, and cafes.", "logistics": "Gunam-ro pedestrian avenue."},
                {"time": "18:30–21:30", "title": "The Bay 101 & Marine City Skyscraper Reflections", "detail": "Capture world-famous water-reflection photographs of Marine City's glittering glass skyscrapers and enjoy fish & chips on the open-air deck.", "logistics": "Dongbaek Station Line 2 Exit 1."}
            ],
            [
                {"label": "Cyberpunk Coastal Skyline", "text": "Marine City's soaring glass residential towers create Korea's most futuristic coastal skyline."},
                {"label": "Iconic Photography", "text": "The Bay 101 reflection photography spot is an international social media sensation."}
            ],
            "Lunch: Choryang Milmyeon (cold wheat noodles & mandu). Dinner: The Bay 101 fish & chips / Haeundae market grilled seafood.",
            "Book KTX Daejeon→Busan on Korail app 30 days prior.",
            "KTX ticket ~₩36,200; The Bay 101 access is free.",
            "To capture the puddle reflection photo at The Bay 101, bring a small water bottle to create a clean surface reflection.",
            "SEA LIFE Busan Aquarium and indoor mall lounges provide shelter if stormy."
        ),
        # Day 14: Nov 14
        make_day(13, "Busan", "Ocean Rails & 500-Drone Spectacular", "Busan · Haeundae Beachfront",
            "Haeundae Blueline Sky Capsule → Cheongsapo → Gwangalli Saturday Night Drone Show",
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
        make_day(14, "Busan", "Cinema Mega-Structures & Spa Land", "Busan · Haeundae Beachfront",
            "Busan Cinema Center (BIFF Mega-Structure) → Centum City Spa Land Thermal Saunas",
            "Guinness Cantilever LED Roofs & Luxury Bathhouses",
            [
                {"time": "10:00–12:30", "title": "Busan Cinema Center (BIFF Venue)", "detail": "Marvel at the Guinness World Record cantilevered roof spanning 85 meters without support columns, covered with 42,600 dynamic LED ceiling lights, touring the cinema museum.", "logistics": "Centum City Station Line 2 Exit 6 or 12."},
                {"time": "12:30–14:00", "title": "Shinsegae Centum Gourmet Hall Lunch", "detail": "Dine in the world's largest department store food emporium on gourmet bibimbap or handmade noodles.", "logistics": "Shinsegae B1."},
                {"time": "14:15–18:30", "title": "Spa Land Centum City Luxury Thermal Bathhouse", "detail": "Experience 18 natural mineral pools and 13 aesthetic themed saunas (Himalayan salt, Roman steam, Finnish sauna) with heated ergonomic loungers.", "logistics": "Direct Shinsegae Mall connection."},
                {"time": "19:00–21:30", "title": "Shinsegae Sky Lounge Modern Korean Dinner", "detail": "Enjoy contemporary Korean dining overlooking Suyeong River.", "logistics": "Shinsegae 9F dining room."}
            ],
            [
                {"label": "Guinness Record Architecture", "text": "The Busan Cinema Center is an international engineering marvel, designed by Coop Himmelb(l)au."},
                {"label": "Ultimate Urban Spa", "text": "Spa Land Centum City delivers the world's most luxurious urban jjimjilbang experience."}
            ],
            "Lunch: Shinsegae Centum City gourmet food hall. Dinner: Modern Korean seasonal tasting dinner at Shinsegae 9F.",
            "Spa Land 4-hour pass ~₩20,000–₩23,000 at entrance.",
            "Cinema Center exterior free; Spa Land ~₩23,000; Dinner ~₩32,000 per person.",
            "Spa Land does not admit children under 7; maintains serene adult relaxation atmosphere.",
            "This entire day is 100% enclosed, heated, and weatherproof."
        ),
        # Day 16: Nov 16
        make_day(15, "Busan", "Immersive Digital Media Art", "Busan · Haeundae Beachfront",
            "Arte Museum Busan (Immersive Digital Art) → Huinnyeoul Coastal Tunnel",
            "Sensory Digital Waterfalls, Light Forests & Cliff Tunnels",
            [
                {"time": "10:00–13:00", "title": "Arte Museum Busan (Immersive Digital Media)", "detail": "Step into monumental multi-sensory digital art spaces: infinite mirrored waterfalls, bioluminescent ocean waves, surreal flower gardens, and interactive aroma soundscapes on Yeongdo.", "logistics": "Yeongdo-gu; bus from Nampo Station or 25-min taxi from Haeundae."},
                {"time": "13:15–14:45", "title": "P.ARK Yeongdo Architectural Cafe Lunch", "detail": "Dine in the striking multi-level stepped amphitheater cafe overlooking Busan harbor shipyards.", "logistics": "Inside P.ARK complex."},
                {"time": "15:15–17:30", "title": "Huinnyeoul Culture Village & Coastal Sea Tunnel", "detail": "Walk the narrow cliffside paths overlooking the ocean and photograph the illuminated coastal rock tunnel.", "logistics": "Yeongdo coastal bus."},
                {"time": "18:00–19:30", "title": "Nampo-dong BIFF Square Street Snacks", "detail": "Sample famous seed hotteok and spicy rice cakes.", "logistics": "Jagalchi / Nampo Station."},
                {"time": "20:00–21:30", "title": "Traditional Busan Dwaeji Gukbap Dinner", "detail": "Enjoy 24-hour simmered pork bone soup with boiled pork suyuk.", "logistics": "Nampo soup alley."}
            ],
            [
                {"label": "Next-Gen Immersive Art", "text": "Arte Museum Busan is Korea's newest and largest digital media art destination, created by d'strict."},
                {"label": "Post-Industrial Harbor Vistas", "text": "P.ARK transforms commercial shipyard docks into an avant-garde cultural amphitheater."}
            ],
            "Lunch: P.ARK Yeongdo artisan bakery pizza and pour-over coffee. Dinner: Traditional Nampo-dong Dwaeji Gukbap with suyuk.",
            "Book Arte Museum Busan timed tickets online or purchase at door (₩19,000).",
            "Arte Museum ₩19,000; Huinnyeoul free; Dinner ~₩15,000 per person.",
            "Arte Museum is dark with mirrored floors; lockers available for large bags.",
            "Arte Museum and P.ARK complex are completely indoor."
        ),
        # Day 17: Nov 17
        make_day(16, "Busan", "Esports Arena & Youth Innovation", "Busan · Haeundae Beachfront",
            "Busan Esports Arena (BRENA) → Jeonpo Transformed Cafe Streets → Seomyeon Night",
            "Competitive Gaming Arenas & Transformed Tool Workshop Cafes",
            [
                {"time": "10:30–12:30", "title": "Busan e-Sports Arena (BRENA)", "detail": "Tour Korea's foremost municipal esports stadium in Seomyeon, exploring the main stage, pro-gamer broadcast booths, and gaming history gallery.", "logistics": "Seomyeon Station Line 1/2 Exit 1 (Busan e-Sports Arena 15F/16F)."},
                {"time": "13:00–14:30", "title": "Jeonpo Tool-Street Gourmet Lunch", "detail": "Dine on handmade Japanese curry, pasta, or Korean rice bowls in transformed industrial workshop alleys.", "logistics": "Jeonpo Station Line 2 Exit 7."},
                {"time": "14:45–17:30", "title": "Jeonpo Cafe Street & Vintage Boutiques", "detail": "Discover artisanal matcha lounges, specialty espresso bars, and indie thrift boutiques recognized by NYT as a top global destination.", "logistics": "Jeonpo-dong."},
                {"time": "18:00–20:00", "title": "Seomyeon Underground Shopping City", "detail": "Browse thousands of K-fashion, beauty, and accessory stores in Korea's largest interconnected underground mall.", "logistics": "Seomyeon Station underground."},
                {"time": "20:30–22:30", "title": "Seomyeon Charcoal BBQ & Pojangmacha Tents", "detail": "Feast on sizzling pork belly and visit iconic orange street food tents.", "logistics": "Seomyeon dining lane."}
            ],
            [
                {"label": "Regional Esports Capital", "text": "BRENA positions Busan as the gaming heartland of southern Korea, hosting major international tournaments."},
                {"label": "Industrial Revival", "text": "Jeonpo successfully repurposed metal hardware shops into vibrant youth coffee ateliers."}
            ],
            "Lunch: Jeonpo handmade curry or pasta. Afternoon: Artisanal espresso & canelé. Dinner: Seomyeon charcoal pork belly BBQ and street tent snacks.",
            "BRENA arena tour is free when non-ticketed events are in progress.",
            "BRENA free; Lunch ~₩14,000; Dinner ~₩25,000 per person.",
            "Jeonpo cafe street has winding alleys; follow digital map markers.",
            "Seomyeon Underground Mall and BRENA are 100% indoor and heated."
        ),
        # Day 18: Nov 18
        make_day(17, "Busan", "Digital Contemporary Art & Craft Beer", "Busan · Haeundae Beachfront",
            "Museum 1 (Digital Art Museum) → Centum Film Archives → Millak Craft Beer",
            "Interactive Media Art, Film Heritage & Waterfront Brews",
            [
                {"time": "10:30–13:00", "title": "Museum 1 (Centum Digital Media Art Museum)", "detail": "Immerse in dynamic LED floors and ceiling projections combining contemporary painting with digital motion graphics.", "logistics": "Centum City Station Line 2 Exit 6."},
                {"time": "13:15–14:45", "title": "Centum City Fusion Lunch", "detail": "Enjoy Korean modern rice bowls or handmade pizza.", "logistics": "Centum dining lane."},
                {"time": "15:00–17:00", "title": "Korean Film Archive Busan Center", "detail": "Browse historic cinema posters, director scripts, and vintage film cameras inside the Busan Cinema Center.", "logistics": "Busan Cinema Center 2F."},
                {"time": "17:30–19:30", "title": "Millak Waterfront Park Sunset Walk", "detail": "Stroll along the waterfront promenade as Gwangan Bridge lights up.", "logistics": "Millak waterfront."},
                {"time": "20:00–22:00", "title": "Busan Craft Beer Brewery & Chimaek Feast", "detail": "Sample local Busan craft IPAs and lagers (Gorilla Brewing / Galmegi Brewing) with crispy Korean fried chicken.", "logistics": "Gwangalli craft beer strip."}
            ],
            [
                {"label": "Cutting-Edge Media Art", "text": "Museum 1 showcases cutting-edge domestic contemporary media artists."},
                {"label": "Craft Beer Innovation", "text": "Busan is celebrated as Korea's craft beer brewing capital."}
            ],
            "Lunch: Centum City modern Korean dining. Dinner: Gwangalli craft beer tasting and garlic-soy Korean fried chicken.",
            "Museum 1 tickets ~₩18,000 at door or online.",
            "Museum 1 ₩18,000; Film Archive free; Dinner ~₩28,000 per person.",
            "Take care walking on Museum 1 mirrored glass floors.",
            "Museum 1 and Cinema Center are fully indoor."
        ),
        # Day 19: Nov 19
        make_day(18, "Busan", "Low-Stakes Photography & Sunset (CSAT Day)", "Busan · Haeundae Beachfront",
            "Haeundae High-Tech Photo Ateliers → Dalmaji Sea-View Cafe (CSAT Day)",
            "Creative Photo Studios & Sunset Ocean Lounges (CSAT / Suneung Day)",
            [
                {"time": "10:30–12:30", "title": "Haeundae Beachfront High-Tech Self-Photo Studio", "detail": "Experience Korea's trendiest high-tech automated self-portrait photo booths (Haru Film, Photoism) with professional lighting and K-pop filters.", "logistics": "Gunam-ro pedestrian avenue."},
                {"time": "12:45–14:15", "title": "Haeundae Gourmet Burger & Fries Lunch", "detail": "Enjoy artisan smashburgers or Korean fusion bowls.", "logistics": "Haeundae dining lane."},
                {"time": "14:30–17:30", "title": "Dalmaji Hill Panoramic Sea-View Cafe Lounge", "detail": "Relax on a heated ocean-view terrace overlooking the sea, sipping Einspänner coffee or artisanal herbal tea.", "logistics": "Dalmaji-gil cafe road."},
                {"time": "18:00–19:30", "title": "Sunset Beach Contemplation", "detail": "Watch the golden sun dip below the horizon on Haeundae sand, reflecting on 7 unforgettable Busan nights.", "logistics": "Haeundae beachfront."},
                {"time": "20:00–22:00", "title": "Busan Farewell Feast: Hanwoo Beef Barbecue", "detail": "Celebrate final night in Busan with premium charcoal-grilled Korean Hanwoo beef tenderloin.", "logistics": "Haeundae Somunnan Amso Galbi."}
            ],
            [
                {"label": "CSAT Low-Stakes Alignment", "text": "Nov 19 national CSAT exam day is kept 100% localized in Haeundae and Dalmaji to avoid city transit hold zones."},
                {"label": "Creative Self-Photo Culture", "text": "Korean automated self-photo booths offer fun, high-quality personalized physical souvenir prints."}
            ],
            "Lunch: Haeundae gourmet burger and truffle fries. Afternoon: Dalmaji sea-view Einspänner coffee. Dinner: Haeundae Somunnan Amso Galbi marinated beef short ribs with potato noodles.",
            "Self-photo booths cost ~₩4,000–₩5,000 for 2 photo strips (instant cash/card).",
            "Photo booths ~₩5,000; Farewell Hanwoo dinner ~₩48,000 per person.",
            "Pack primary bags tonight for Friday morning KTX to Seoul.",
            "Haeundae indoor photo studios and ocean cafes provide comfortable shelter."
        ),
        # Day 20: Nov 20
        make_day(19, "Seoul", "Capital Return & Cyberpunk Alleys", "Seoul · Seoul Station / Myeongdong",
            "Morning KTX Busan to Seoul → Euljiro Hipjiro Neon Alleys & Hidden Cocktail Bars",
            "Capital Return & Cyberpunk Industrial Alleys",
            [
                {"time": "09:30–10:15", "title": "Busan Station Departure", "detail": "Check out of Haeundae hotel, take taxi or metro to Busan Station, and board direct KTX.", "logistics": "Board train 10 minutes prior to departure."},
                {"time": "10:30–12:45", "title": "KTX High-Speed Rail to Seoul", "detail": "Comfortable 2-hour 15-minute smooth journey back to Seoul Station.", "logistics": "Direct arrival in central Seoul."},
                {"time": "13:00–14:30", "title": "Seoul Station Hotel Check-in & Lunch", "detail": "Check into Seoul Station hotel base and enjoy warm bibimbap or beef soup.", "logistics": "Drop bags at hotel doorstep."},
                {"time": "15:00–18:00", "title": "Euljiro 'Hipjiro' Lighting & Print Workshop Alleys", "detail": "Explore the vibrant collision of traditional industrial acrylic workshops and hidden third-floor speakeasies and coffee lofts.", "logistics": "Euljiro 3-ga Station Line 2/3."},
                {"time": "18:30–21:30", "title": "Euljiro Retro Nogari Alley & Neon Rooftop Bar", "detail": "Enjoy draft beer, grilled dried pollack, and Korean fried chicken under retro neon signs.", "logistics": "Euljiro 3-ga Station Exit 3/4."}
            ],
            [
                {"label": "Friday Departure Security", "text": "Arriving in Seoul on Friday eliminates all risk of KTX travel disruption before Sunday international flight."},
                {"label": "Cyberpunk Atmosphere", "text": "Euljiro's neon signs and gritty industrial stairs represent modern Seoul's most thrilling retro-futuristic aesthetic."}
            ],
            "Lunch: Seoul Station gourmet dining. Dinner: Euljiro Nogari alley garlic fried chicken and grilled pollack.",
            "Book KTX Busan→Seoul 30 days in advance on Korail app.",
            "KTX ticket ~₩59,800; Euljiro night ~₩25,000 per person.",
            "Friday afternoon KTX trains sell out fast; reserve morning seat.",
            "Lotte Mart and Seoul Station concourse are completely enclosed."
        ),
        # Day 21: Nov 21
        make_day(20, "Seoul", "Flagship Tech & Farewell BBQ", "Seoul · Seoul Station / Myeongdong",
            "Samsung & Apple Gangnam Flagships → Seoul Station Lotte Mart Gifts → Grand Farewell Feast",
            "High-Tech Flagships & Grand Celebration Banquet",
            [
                {"time": "10:00–12:30", "title": "Samsung Gangnam & Apple Gangnam Interactive Flagships", "detail": "Experience high-tech interactive tech demo zones, customized phone case printing, and digital gaming lounges in Gangnam.", "logistics": "Gangnam Station Line 2 Exit 10."},
                {"time": "13:00–15:30", "title": "Seoul Station Lotte Mart Mega-Store Curation", "detail": "Curate Korean food and pop-culture gifts: K-pop snack boxes, honey butter chips, sheet masks, ramen sets, and tech accessories with instant tax refund.", "logistics": "Lotte Mart 2F immediate tax refund counter."},
                {"time": "16:00–18:00", "title": "Luggage Packing & Scale Check", "detail": "Pack items safely into luggage, weigh bags at hotel front desk, and complete airline online check-in.", "logistics": "Hotel room."},
                {"time": "18:30–21:30", "title": "Grand Modern Farewell Feast: Premium Hanwoo Barbecue", "detail": "Celebrate 21 nights of high-tech and pop-culture discovery with premium charcoal-grilled Korean Hanwoo beef tenderloin, cold naengmyeon, and craft plum wine.", "logistics": "Central Seoul premier Hanwoo dining room."}
            ],
            [
                {"label": "Flagship Tech Demonstrations", "text": "Samsung Gangnam showcases the absolute bleeding edge of mobile AI and interactive gaming."},
                {"label": "Flawless Departure Prep", "text": "All packing, gift shopping, and online check-in completed by Saturday night ensures Sunday morning is 100% serene."}
            ],
            "Lunch: Gangnam gourmet katsu or Korean noodle bowl. Dinner: Grand Hanwoo charcoal beef banquet with Pyongyang cold noodles and maesil wine.",
            "Complete online airline check-in 24 hours prior to flight.",
            "Souvenirs ~₩50,000–₩120,000; Grand Farewell Dinner ~₩50,000 per person.",
            "Keep tax refund receipts, passport, and critical items in carry-on bag.",
            "Underground department store arcades connect Namdaemun to Myeongdong."
        ),
        # Day 22: Nov 22
        make_day(21, "Seoul", "Departure", "Departure · Incheon International Airport",
            "AREX Non-Stop Express to ICN → Customs & Tax Refunds → Flight at 13:00",
            "Seamless Airport Rail & Triumphant Flight Departure",
            [
                {"time": "08:30–09:15", "title": "Hotel Checkout & AREX Express Boarding", "detail": "Check out of Seoul Station hotel and board direct AREX Non-Stop Express Train to Incheon Airport (43 mins).", "logistics": "B2 Seoul Station."},
                {"time": "09:30–10:15", "title": "AREX Express to ICN Terminal 1 / 2", "detail": "Fast, direct airport train ride with reserved seating and dedicated luggage racks.", "logistics": "43 min to T1 / 51 min to T2."},
                {"time": "10:15–12:15", "title": "Airport Customs, Tax Refunds & Departure Gate", "detail": "Drop luggage, clear security, collect tax refund cash, and reach departure gate by 12:20.", "logistics": "Target arriving 3 hours prior to 13:00 international flight."},
                {"time": "12:30–13:00", "title": "Boarding & Flight Departure at 13:00", "detail": "Board aircraft for the return flight home with unforgettable memories of K-pop, cutting-edge science, esports, and modern Korean culture.", "logistics": "Flight departs at 13:00 local time."}
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
        {"label": "K-Pop & Youth Culture", "value": "5/5", "tone": "good"},
        {"label": "High-Tech & Esports", "value": "5/5", "tone": "good"},
        {"label": "Modern Architecture", "value": "5/5", "tone": "good"},
        {"label": "Digital Nightscapes", "value": "5/5", "tone": "good"}
    ]

    return {
        "id": "seoul-daejeon-busan-modern",
        "shortTitle": "Seoul · Daejeon · Busan (Modern & Pop Culture)",
        "title": "K-Innovation, High-Tech & Pop Culture Odyssey (Modern & Pop Culture)",
        "routeLabel": "Seoul (7N) → Daejeon (5N) → Busan (7N) → Seoul (2N)",
        "badge": "K-Pop, Esports & Modern Innovation",
        "bestFor": "Fans of K-pop, esports gamers, tech enthusiasts, urban architecture admirers, and travelers energized by trendy concept stores, futuristic media facades, and buzzing youth nightlife.",
        "decisionSummary": "A dynamic, trendsetting itinerary exploring Seoul's iconic esports arenas, K-pop busking streets, and Seongsu concept stores, alongside Daejeon's robotics superclusters and KAIST innovation labs, culminating in Busan's world-record cantilevered Cinema Center, drone spectacles, and immersive digital art museums.",
        "recommendation": "Choose this route if you want to experience South Korea at the cutting edge of global pop culture, technology, interactive digital art, and futuristic urban design.",
        "tradeoff": "More focus on bustling commercial districts, high-tech venues, and nightlife than quiet countryside temples.",
        "scorecard": scorecard,
        "bases": get_sdb_common_bases(),
        "transfers": get_sdb_common_transfers(),
        "budgetScenarios": get_sdb_budget_scenarios(),
        "bookingPriorities": get_sdb_booking_priorities(),
        "days": days
    }
