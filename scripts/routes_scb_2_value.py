#!/usr/bin/env python3
"""Route Blueprint: Seoul · Cheonan · Busan (Smart Value & Authentic Neighborhood Living)."""

from scripts.generate_all_itineraries import make_day
from scripts.itinerary_builder_scb import (
    get_scb_common_bases,
    get_scb_common_transfers,
    get_scb_budget_scenarios,
    get_scb_booking_priorities
)

def get_scb_value():
    days = [
        # Day 1: Nov 1
        make_day(0, "Seoul", "Arrival", "Seoul · Myeongdong / Seoul Station edge",
            "ICN arrival at 21:00 → late transfer → budget-smart convenience store reset → sleep",
            "Smart Arrival & Value-Conscious Night Check-in",
            [
                {"time": "21:00–22:15", "title": "ICN Arrival & Budget Connectivity", "detail": "Clear customs and activate value eSIM and rechargeable T-Money transport card.", "logistics": "Terminal 1 or 2."},
                {"time": "22:30–23:45", "title": "Direct Limousine Bus to Seoul Base", "detail": "Take the airport limousine bus directly to Myeongdong / Seoul Station hotel.", "logistics": "Direct bus saves taxi surcharges."},
                {"time": "23:45–00:30", "title": "Convenience Store Warm Snack & Rest", "detail": "Pick up warm barley tea and samgak kimbap at CU/GS25; get restful sleep.", "logistics": "Notify hotel of late check-in."}
            ],
            [
                {"label": "Value Posture", "text": "Starting with high-value transport cards and local convenience snacks sets a sustainable budget pace."},
                {"label": "Rest Priority", "text": "Save energy for tomorrow's free panoramic city wall hike."}
            ],
            "Light convenience store snack (banana milk & tuna kimbap ~₩3,500).",
            "Confirm late check-in with hotel in writing.",
            "Limousine Bus ~₩17,000 / Snacks ~₩3,500.",
            "Late night jetlag; keep bedtime calm.",
            "Convenience store adjacent to hotel provides warm teas."
        ),
        # Day 2: Nov 2
        make_day(1, "Seoul", "Fortress Vistas & Mural Alleys", "Seoul · Myeongdong / Seoul Station edge",
            "Naksan Mountain Seoul City Wall Sunset Walk → Ihwa Mural Village → Dongdaemun Gate",
            "Free Panoramic Fortress Ramparts & Historic Mural Villages",
            [
                {"time": "10:00–12:30", "title": "Ihwa Mural Village & Marronnier Park", "detail": "Explore the vibrant outdoor street murals, retro cafes, and theatrical street sculptures in Daehak-ro.", "logistics": "Hyehwa Station Line 4 Exit 2."},
                {"time": "12:45–14:00", "title": "Daehak-ro Student Alley Lunch", "detail": "Enjoy generous, affordable portions of stone-pot bibimbap or handmade katsu.", "logistics": "Daehak-ro student dining lane."},
                {"time": "14:30–17:30", "title": "Seoul City Wall (Hanyangdoseong) Naksan Trail", "detail": "Walk along 600-year-old stone fortress ramparts from Naksan mountain park down to Dongdaemun, capturing free 360-degree panoramic views over Seoul at sunset.", "logistics": "Naksan Park trail down to Heunginjimun Gate."},
                {"time": "18:00–19:30", "title": "Dongdaemun Design Plaza Exterior Night Lighting", "detail": "Admire Zaha Hadid's futuristic curved architecture glowing under evening LED lights.", "logistics": "Dongdaemun History & Culture Park Station."},
                {"time": "20:00–21:30", "title": "Dongdaemun Grilled Fish Alley Dinner", "detail": "Savor crispy briquette-grilled mackerel with unlimited side dishes, warm rice, and doenjang soup.", "logistics": "Dongdaemun Fish Alley (Line 1/4 Exit 9)."}
            ],
            [
                {"label": "Zero-Cost Panoramic Views", "text": "Naksan fortress wall offers panoramic city skyline vistas rivaling paid observation decks for zero entrance fee."},
                {"label": "Generous Local Feasts", "text": "Dongdaemun fish alley delivers incredible nutritional value with unlimited side dishes."}
            ],
            "Lunch: Daehak-ro student bibimbap set. Dinner: Dongdaemun briquette-grilled mackerel set with soybean stew (~₩12,000).",
            "City wall trail and DDP exterior are 100% free and open 24/7.",
            "Daily sightseeing cost: ₩0; Meals ~₩22,000 per person.",
            "Wear comfortable walking shoes with good grip for stone wall stairs.",
            "DDP design interior and underground malls provide indoor shelter."
        ),
        # Day 3: Nov 3
        make_day(2, "Seoul", "Brass Coins & Free Royal Museums", "Seoul · Myeongdong / Seoul Station edge",
            "National Palace Museum (Free Admission) → Tongin Market Brass Coin Lunchbox → Seochon Alleys",
            "Free Royal Palace Treasures & Traditional Brass Coin Feasts",
            [
                {"time": "09:30–11:30", "title": "National Palace Museum of Korea", "detail": "Examine royal Joseon dynasty seals, imperial carriages, astronomical water clocks, and court costumes in a magnificent free-admission museum.", "logistics": "Gyeongbokgung Station Line 3 Exit 5 (free entry)."},
                {"time": "11:45–13:30", "title": "Tongin Market Brass Coin Lunchbox Cafe (Dosirak Cafe)", "detail": "Exchange cash for a string of traditional brass coins (Yeopjeon) and fill a customized lunchbox tray from market stalls with oil tteokbokki, rolled omelets, and dumplings.", "logistics": "Tongin Market central customer center (Line 3 Gyeongbokgung Exit 2)."},
                {"time": "14:00–16:30", "title": "Seochon Village Hanok Alleys & Cheongun Library", "detail": "Stroll peaceful artist residential lanes and read poetry in the Hanok pavilion library with indoor waterfall.", "logistics": "Seochon pedestrian walking lane."},
                {"time": "17:00–18:30", "title": "Gwanghwamun Square & King Sejong Memorial", "detail": "Visit the giant golden statue of King Sejong and explore the free underground Hangeul and Admiral Yi Sun-sin museum.", "logistics": "Gwanghwamun Station Line 5 Exit 9."},
                {"time": "19:00–21:00", "title": "Jongno Traditional Kalguksu & Mandu Dinner", "detail": "Warm up with rich handmade knife-cut noodle soup and steamed dumplings.", "logistics": "Jongno dining quarter."}
            ],
            [
                {"label": "Interactive Coin Economy", "text": "Tongin Market's Yeopjeon lunchbox is one of Seoul's most engaging and economical food experiences."},
                {"label": "Free High-Culture", "text": "National Palace Museum and King Sejong underground hall offer world-class curation at zero cost."}
            ],
            "Lunch: Tongin Market Yeopjeon brass coin lunchbox (custom selection ~₩8,000). Dinner: Jongno handmade kalguksu and steamed mandu (~₩9,000).",
            "Tongin Dosirak cafe operates 11:00–16:00 (closed Mondays).",
            "Museums free; Dosirak lunch ~₩8,000; Dinner ~₩9,000 per person.",
            "Arrive at Tongin Market by 11:30 AM before popular side dishes run out.",
            "National Palace Museum and Sejong underground museum are fully indoor."
        ),
        # Day 4: Nov 4
        make_day(3, "Seoul", "Vintage Markets & Stream Walks", "Seoul · Myeongdong / Seoul Station edge",
            "Dongmyo Vintage Flea Market → Hwanghak Kitchenware Street → Cheonggyecheon Stream Walk",
            "Retro Treasure Hunting & Peaceful Waterway Strolls",
            [
                {"time": "10:00–12:30", "title": "Dongmyo Vintage Flea Market", "detail": "Hunt for retro treasures across thousands of open-air stalls: vintage cameras, vinyl records, classic denim jackets, and antique books.", "logistics": "Dongmyo Station Line 1/6 Exit 3."},
                {"time": "12:45–14:00", "title": "Dongmyo Market Toast & Soy Noodle Lunch", "detail": "Enjoy ultra-affordable market street toast, warm soybean noodles (kongguksu), or bibimbap.", "logistics": "Dongmyo food stalls."},
                {"time": "14:15–16:00", "title": "Seoul Folk Flea Market (Indoor Arcade)", "detail": "Browse two floors of curated Korean folk antiques, brassware, retro toys, and traditional musical instruments.", "logistics": "Sinseol-dong Station Line 1/2 Exit 9."},
                {"time": "16:30–18:30", "title": "Cheonggyecheon Stream Walk to Gwangjang Market", "detail": "Follow the sunken pedestrian eco-stream under leafy bridges to Gwangjang Market.", "logistics": "Cheonggyecheon pedestrian path."},
                {"time": "19:00–21:00", "title": "Gwangjang Market Crispy Bindaetteok Feast", "detail": "Dine on giant freshly fried mung bean pancakes and mayak gimbap with draft makgeolli.", "logistics": "Jongno 5-ga Station Line 1 Exit 8."}
            ],
            [
                {"label": "Authentic Local Economy", "text": "Dongmyo and Seoul Folk Flea Market show everyday thrift and reuse culture beloved by Seoul vintage hunters."},
                {"label": "Low-Cost Iconic Market", "text": "Bindaetteok at Gwangjang is one of the most delicious, filling, and affordable dinners in Seoul."}
            ],
            "Lunch: Dongmyo market street toast and noodles (~₩5,000). Dinner: Gwangjang Market crispy bindaetteok and mayak gimbap (~₩12,000).",
            "Dongmyo flea market stalls are cash or T-money only.",
            "Market items ~₩5,000–₩15,000; Dinner ~₩12,000 per person.",
            "Keep bags zipped in crowded market aisles.",
            "Seoul Folk Flea Market is an indoor two-story covered building."
        ),
        # Day 5: Nov 5
        make_day(4, "Seoul", "Urban Forests & River Picnics", "Seoul · Myeongdong / Seoul Station edge",
            "Seoul Forest Park (Free Ginkgo Forest) → Ttukseom Hangang Riverbank → Mangwon Market",
            "Free Forest Sanctuaries & Riverside Automated Ramen",
            [
                {"time": "10:00–12:30", "title": "Seoul Forest Park Metasequoia Canopy", "detail": "Stroll under golden ginkgo groves and towering metasequoias, visiting the deer corral and outdoor sculpture garden (all free admission).", "logistics": "Seoul Forest Station Suin-Bundang Line Exit 4."},
                {"time": "12:45–14:00", "title": "Seongsu Neighborhood Rice Bowl Lunch", "detail": "Enjoy affordable dolsot bibimbap or handmade dumplings near the park.", "logistics": "Seongsu dining lane."},
                {"time": "14:30–17:00", "title": "Mangwon Traditional Neighborhood Market", "detail": "Browse Seoul's favorite authentic neighborhood market for crispy dakgangjeong (sweet fried chicken), handmade croquettes, and hotteok.", "logistics": "Mangwon Station Line 6 Exit 2."},
                {"time": "17:30–19:30", "title": "Mangwon Hangang Park Sunset & Automated Ramen", "detail": "Cook instant ramen on an automated induction boiler by the Han River bank, watching sunset over the water.", "logistics": "Mangwon Hangang Park."},
                {"time": "20:00–21:30", "title": "Mapo Charcoal Pork Galbi Feast", "detail": "Feast on tender marinated pork ribs grilled over charcoal.", "logistics": "Mapo Station Line 5 BBQ Alley."}
            ],
            [
                {"label": "Urban Green Oases", "text": "Seoul Forest and Hangang parks offer hundreds of acres of natural beauty with zero admission fees."},
                {"label": "Beloved Local Snack Culture", "text": "Mangwon Market provides superior prices and freshness compared to tourist-heavy commercial zones."}
            ],
            "Lunch: Seongsu stone-pot bibimbap. Afternoon: Mangwon dakgangjeong chicken bites & croquettes (~₩6,000). Dinner: Mapo charcoal-grilled pork ribs (~₩18,000).",
            "Seoul Forest and Hangang parks are open 24/7 for free.",
            "Parks free; Mangwon snacks ~₩6,000; Dinner ~₩18,000 per person.",
            "Carry a small picnic mat or jacket to sit comfortably on Hangang grassy banks.",
            "Mangwon Market is a covered arcade; Insect Garden inside Seoul Forest is indoor."
        ),
        # Day 6: Nov 6
        make_day(5, "Seoul", "Artisan Industrial Villages", "Seoul · Myeongdong / Seoul Station edge",
            "Mullae-dong Creative Arts Village → Yeongdeungpo Traditional Market → Hongdae Evening",
            "Metal Workshop Art Lofts & Thriving Youth Streets",
            [
                {"time": "10:30–13:00", "title": "Mullae-dong Creative Arts Village", "detail": "Walk through living steel-cutting metal workshops juxtaposed with independent art studios, rooftop murals, and indie cafes.", "logistics": "Mullae Station Line 2 Exit 7."},
                {"time": "13:00–14:30", "title": "Mullae Creative Village Lunch", "detail": "Enjoy handmade pasta, smashburgers, or Korean rice sets in converted industrial spaces.", "logistics": "Mullae arts street."},
                {"time": "15:00–17:00", "title": "Yeongdeungpo Traditional Market Walk", "detail": "Browse one of southwestern Seoul's largest local wholesale markets selling fresh fruits, sundae, and seasoned banchan.", "logistics": "Yeongdeungpo Market Station Line 5 Exit 3."},
                {"time": "17:30–19:30", "title": "Hongdae Street Busking Walk", "detail": "Watch free synchronized K-pop dance and acoustic music busking on the pedestrian strip.", "logistics": "Hongik Univ. Station Line 2 Exit 8/9."},
                {"time": "20:00–21:30", "title": "Hongdae Korean BBQ Dinner", "detail": "Enjoy thick pork belly and kimchi stew.", "logistics": "Hongdae dining street."}
            ],
            [
                {"label": "Raw Industrial Authenticity", "text": "Mullae preserves working metal craftspeople while fostering grassroots artist studios."},
                {"label": "Free Street Entertainment", "text": "Hongdae busking offers world-class live performance completely free."}
            ],
            "Lunch: Mullae creative cafe lunch. Dinner: Hongdae charcoal-grilled pork belly with steamed egg and soybean stew.",
            "Mullae metal workshops operate on weekdays; be courteous of working machinery.",
            "Free neighborhood walking; Lunch ~₩14,000; Dinner ~₩22,000 per person.",
            "Stick to designated pedestrian pathways in Mullae.",
            "Yeongdeungpo Times Square mega-mall provides indoor shelter."
        ),
        # Day 7: Nov 7
        make_day(6, "Seoul", "Stonewall Strolls & KTX Prep", "Seoul · Myeongdong / Seoul Station edge",
            "Deoksugung Stonewall Walkway → Jeongdong Observatory (Free City View) → KTX Prep",
            "Romantic Autumn Walkways, Free Sky Views & Rail Prep",
            [
                {"time": "10:00–12:30", "title": "Deoksugung Stonewall Walkway & Jeongdong Heritage", "detail": "Walk Korea's most romantic ginkgo-shaded stonewall path and take the elevator to the 13th-floor Jeongdong Observatory for free panoramic views of Deoksugung Palace.", "logistics": "City Hall Station Line 1/2 Exit 2 (Observatory inside City Hall Seosomun Annex)."},
                {"time": "12:45–14:00", "title": "Myeongdong Kyoja Kalguksu Lunch", "detail": "Enjoy Michelin Bib Gourmand handmade noodles and steamed mandu dumplings.", "logistics": "Myeongdong 2-ga."},
                {"time": "14:30–16:30", "title": "Seoul Station Lotte Mart Food Reconnaissance", "detail": "Preview Korean food gifts and pick up snacks for tomorrow's KTX train.", "logistics": "Seoul Station 2F."},
                {"time": "17:00–18:30", "title": "Luggage Packing & KTX Ticket Check", "detail": "Pack primary luggage for Sunday morning KTX to Cheonan-Asan (only 35 mins!).", "logistics": "Seoul Station hotel."},
                {"time": "19:00–21:00", "title": "Warm Budae Jjigae (Army Stew) Dinner", "detail": "Savor hearty stew simmered with spam, sausage, ramen noodles, tofu, and kimchi.", "logistics": "Seoul Station dining lane."}
            ],
            [
                {"label": "Free High-Altitude Palace View", "text": "Jeongdong Observatory provides the finest aerial view over Deoksugung Palace courtyards for zero fee."},
                {"label": "Rail Preparation", "text": "Packing early ensures an effortless Sunday morning 35-minute rail leap to Cheonan."}
            ],
            "Lunch: Myeongdong Kyoja (kalguksu & mandu ~₩11,000). Dinner: Hearty tabletop Budae Jjigae army stew with ramen (~₩12,000).",
            "Jeongdong Observatory open weekends 09:00–18:00 (free admission).",
            "Observatory free; Lunch ~₩11,000; Dinner ~₩12,000 per person.",
            "Deoksugung Stonewall path is flat and easily walkable.",
            "City Hall Seosomun Annex and Seoul Station concourse are completely indoor."
        ),
        # Day 8: Nov 8
        make_day(7, "Cheonan", "City Transition & Market Value", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Morning KTX to Cheonan-Asan (35 mins) → Cheonan Namsan Central Market Crawl → 1934 Hodu-gwaja",
            "Fast 35-Min Rail Leap, Authentic Markets & Walnut Cakes",
            [
                {"time": "09:45–10:20", "title": "KTX High-Speed Rail Seoul to Cheonan-Asan", "detail": "Lightning 35-minute smooth high-speed transit from Seoul Station to Cheonan-Asan Station (value fare ₩14,100).", "logistics": "Direct Gyeongbu line."},
                {"time": "10:30–12:00", "title": "Hotel Check-in & Base Setup", "detail": "Check into value base (e.g. Shilla Stay Cheonan or Ramada Encore Cheonan-Asan) and drop bags.", "logistics": "Station area / Shinbu-dong."},
                {"time": "12:30–15:00", "title": "Cheonan Namsan Central Market Feast", "detail": "Browse Cheonan's oldest covered market for knife-cut noodles (kalguksu for ₩4,000!), giant handmade pork dumplings, and vegetable hotteok.", "logistics": "Sajik-dong (walk from Cheonan Station)."},
                {"time": "15:30–17:00", "title": "1934 Original Hakhwa Hodu-gwaja Bakery", "detail": "Taste steaming hot walnut pastries filled with whole crunchy walnuts and red/white bean paste freshly baked from the oven.", "logistics": "Cheonan Station / Shinbu-dong branch."},
                {"time": "17:30–19:00", "title": "Arario Open-Air Sculpture Park Walk", "detail": "Walk the public plaza to see monumental works by Damien Hirst and Keith Haring for free.", "logistics": "Shinbu-dong Arario Plaza."},
                {"time": "19:30–21:30", "title": "Cheonan Sizzling Bulgogi Dinner", "detail": "Feast on tender beef bulgogi with fresh seasonal banchan side dishes.", "logistics": "Central Cheonan dining lane."}
            ],
            [
                {"label": "Extreme Rail Value", "text": "At just 35 minutes and ₩14,100, Cheonan offers unbeatable transit speed and lower accommodation costs."},
                {"label": "Authentic Market Value", "text": "Namsan Central Market serves authentic knife-cut noodles at unbeatable traditional pricing."}
            ],
            "Lunch: Namsan Central Market hand-pulled kalguksu & giant mandu (~₩7,000). Afternoon: 1934 Hakhwa hot walnut pastries. Dinner: Cheonan sizzling beef bulgogi with rice (~₩18,000).",
            "Book KTX Seoul→Cheonan-Asan on Korail app 30 days prior.",
            "KTX ticket ~₩14,100; Namsan market food ~₩7,000; Hodu-gwaja box ~₩6,000.",
            "Namsan market kalguksu stalls accept cash or T-Money.",
            "Namsan Central Market is a fully covered weather-proof arcade."
        ),
        # Day 9: Nov 9
        make_day(8, "Cheonan", "Free National Monument & Maple Tunnel", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Independence Hall of Korea (Free Admission, 7 Vast Halls) → 3.2km Maple Tree Tunnel Walk",
            "Monumental National Exhibits & Radiant Autumn Foliage",
            [
                {"time": "09:30–13:30", "title": "Independence Hall of Korea (Exhibition Halls 1–6)", "detail": "Tour Korea's foremost patriotic national monument: the colossal Grand Hall of the Nation and vast multimedia galleries (all 100% free admission).", "logistics": "City Bus 381/382/383 from Cheonan Station or 20-min taxi."},
                {"time": "13:30–14:45", "title": "Mokcheon Traditional Country Lunch", "detail": "Enjoy hearty country soybean paste stew (doenjang jjigae), acorn jelly, and grilled fish.", "logistics": "Independence Hall restaurant plaza."},
                {"time": "15:00–17:30", "title": "Independence Hall Autumn Maple Tree Tunnel Walk", "detail": "Walk the spectacular 3.2km paved pedestrian path shaded by thousands of crimson and golden maple trees encircling the complex.", "logistics": "Circling trail around Independence Hall (free)."},
                {"time": "18:00–19:30", "title": "Return to Cheonan & Cafe Rest", "detail": "Relax at hotel or explore local cafes in Shinbu-dong.", "logistics": "Short taxi or bus return."},
                {"time": "20:00–21:30", "title": "Cheonan Charcoal Pork BBQ Dinner", "detail": "Feast on thick pork neck and steaming kimchi stew.", "logistics": "Shinbu-dong dining lane."}
            ],
            [
                {"label": "Zero Admission Monument", "text": "Independence Hall provides world-class museum facilities and 7 exhibition halls completely free of charge."},
                {"label": "Peak Foliage Spectacle", "text": "The 3.2km Maple Tree Tunnel is one of Korea's premier autumn foliage walks."}
            ],
            "Lunch: Mokcheon traditional country doenjang stew and grilled mackerel (~₩10,000). Dinner: Shinbu-dong charcoal pork BBQ with soybean stew (~₩20,000).",
            "Independence Hall of Korea is free admission; closed on Mondays (outdoor park grounds remain open).",
            "Independence Hall is free; Taxi ~₩15,000 each way; Meals ~₩30,000 per person.",
            "Wear comfortable walking shoes for the 3.2km maple loop.",
            "All 7 exhibition halls are fully indoor and climate-controlled."
        ),
        # Day 10: Nov 10
        make_day(9, "Cheonan", "Willow Pavilions & City Culture", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Cheonan Samgeori Park Willow Pavilions → Cheonan City Museum (Free Admission)",
            "Historic Crossroads Pavilions & Folk Relics",
            [
                {"time": "10:00–12:30", "title": "Cheonan Samgeori Park Heritage Walk", "detail": "Walk around the scenic willow-lined lake and traditional pavilions where the historic Gyeongbu and Honam royal highways intersected (immortalized in the folk song Cheonan Heungtaryeong).", "logistics": "Dongnam-gu Samnyong-dong; Bus 24/12 or 10-min taxi."},
                {"time": "12:45–14:00", "title": "Samnyong-dong Local Noodle Lunch", "detail": "Enjoy buckwheat cold noodles or bibimbap near the park.", "logistics": "Park entrance restaurant row."},
                {"time": "14:15–16:30", "title": "Cheonan Museum of Folk & History", "detail": "Explore traditional royal carriage exhibits, Joseon lifestyle dioramas, and ancient relics (free admission).", "logistics": "Located directly adjacent to Samgeori Park."},
                {"time": "17:00–18:30", "title": "Shinbu Cultural Street Walk", "detail": "Stroll central Cheonan's lively youth shopping street.", "logistics": "Shinbu-dong."},
                {"time": "19:00–21:00", "title": "Cheonan Sliced Pork Suyuk & Kimchi Feast", "detail": "Enjoy tender boiled pork belly wrapped in fresh salted cabbage with spicy radish salad.", "logistics": "Shinbu-dong dining lane."}
            ],
            [
                {"label": "Free Folk Heritage", "text": "Samgeori Park and Cheonan Museum celebrate the city's historic role as Korea's central crossroads with zero admission fees."},
                {"label": "Unrushed Rhythm", "text": "A relaxing, flat walking day between mountain excursions."}
            ],
            "Lunch: Samnyong-dong buckwheat makguksu and potato pancake. Dinner: Cheonan tender pork suyuk bossam with fresh oyster kimchi.",
            "Cheonan Museum is closed on Mondays; free admission.",
            "Park and Museum are free; Meals ~₩25,000 per person.",
            "Samgeori Park lake pavilion provides scenic photo backdrops.",
            "Cheonan Museum is completely enclosed and heated."
        ),
        # Day 11: Nov 11
        make_day(10, "Cheonan", "Lake Boardwalks & Birdwatching", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Seongseong Lake Park Eco-Boardwalk Loop → Lakefront Cafe Rest",
            "Wooden Wetland Boardwalks & Sunset Water Vistas",
            [
                {"time": "10:00–13:00", "title": "Seongseong Lake Park & Eco-Boardwalk", "detail": "Walk the scenic wooden boardwalk loop around Seongseong Lake, visiting the bird observatory, reed fields, and modern waterfront cafes.", "logistics": "Seobuk-gu Seongseong-dong; City Bus 5 or 15-min taxi."},
                {"time": "13:15–14:45", "title": "Seongseong Lakefront Cafe Lunch", "detail": "Enjoy affordable artisanal brunch, pasta, or Korean rice sets overlooking the sparkling water.", "logistics": "Seongseong cafe road."},
                {"time": "15:15–17:30", "title": "Seongseong Waterfront Sunset Walk", "detail": "Watch sunset reflections on the lake and photograph autumn reeds.", "logistics": "Wooden boardwalk loop."},
                {"time": "18:00–19:30", "title": "Shinbu-dong Specialty Dessert & Coffee", "detail": "Taste Korean shaved ice (bingsu) or pour-over coffee.", "logistics": "Shinbu-dong."},
                {"time": "20:00–21:30", "title": "Cheonan Mushroom Shabu-Shabu Hot Pot Dinner", "detail": "Cook fresh mushrooms and thinly sliced beef in savory broth.", "logistics": "Station area dining room."}
            ],
            [
                {"label": "Modern Wetland Oasis", "text": "Seongseong Lake Park is Cheonan's newest urban wetland park with pristine wooden boardwalks."},
                {"label": "Scenic Relaxation", "text": "A calm, picturesque lakeside day with minimal commercial stress."}
            ],
            "Lunch: Seongseong lakefront cafe brunch (~₩14,000). Dinner: Beef and mushroom shabu-shabu hot pot (~₩18,000).",
            "Seongseong Lake Park is open 24/7; admission is free.",
            "Park is free; Lunch ~₩14,000; Dinner ~₩18,000 per person.",
            "Bring binoculars for birdwatching migratory ducks on the lake.",
            "Lakefront multi-story cafes provide heated indoor water views."
        ),
        # Day 12: Nov 12
        make_day(11, "Cheonan", "Colossal Buddha & Rail Prep", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Gakwonsa Temple (Grand 15-Meter Bronze Buddha) → Taejosan Trail → KTX to Busan Prep",
            "Monumental Bronze Statues & Pre-Busan Rail Prep",
            [
                {"time": "09:30–12:30", "title": "Gakwonsa Temple & Grand Bronze Buddha", "detail": "Climb stone stairs to behold the colossal 15-meter seated Bronze Amita Buddha overlooking Taejosan Mountain (free admission).", "logistics": "Dongnam-gu Anseo-dong; City Bus 24 or 15-min taxi."},
                {"time": "12:45–14:15", "title": "Anseo-dong Mountain Village Lunch", "detail": "Enjoy buckwheat cold noodles, potato pancakes, and wild herb bibimbap near the temple lake.", "logistics": "Gakwonsa lake restaurant row."},
                {"time": "14:30–17:00", "title": "Taejosan Mountain Forest Walk", "detail": "Walk the pine-shaded trails and visit the mountain reservoir.", "logistics": "Taejosan park trails."},
                {"time": "17:30–19:30", "title": "Hotel Packing & KTX Ticket Verification", "detail": "Pack primary luggage for Friday morning KTX to Busan and confirm seat assignments.", "logistics": "Hotel room."},
                {"time": "20:00–21:30", "title": "Cheonan Farewell Korean Feast", "detail": "Celebrate 5 nights in Cheonan with rich pork galbi barbecue.", "logistics": "Shinbu-dong dining lane."}
            ],
            [
                {"label": "Free Monumental Icon", "text": "Gakwonsa's 60-ton Bronze Buddha is one of Asia's most majestic outdoor bronze statues with free entry."},
                {"label": "Transit Preparation", "text": "Packing early ensures a relaxed Friday morning high-speed train directly to Busan."}
            ],
            "Lunch: Anseo-dong buckwheat makguksu and potato pancake. Dinner: Charcoal-grilled pork galbi with cold noodles.",
            "Gakwonsa Temple is free admission; open year-round from dawn to dusk.",
            "Temple is free; Lunch ~₩12,000; Dinner ~₩22,000 per person.",
            "Pack primary bags tonight for Friday morning KTX to Busan.",
            "Daeungbojeon prayer hall provides covered shelter."
        ),
        # Day 13: Nov 13
        make_day(12, "Busan", "Coastward Rail & Beach Arrival", "Busan · Haeundae Beachfront",
            "KTX Cheonan-Asan to Busan (1h45m) → Haeundae Check-in → Sunset Beach Walk",
            "Direct High-Speed Coastal Rail to the Southern Sea",
            [
                {"time": "10:00–11:45", "title": "KTX High-Speed Rail to Busan", "detail": "Smooth 1-hour 45-minute direct journey from Cheonan-Asan to Busan Station.", "logistics": "Direct Gyeongbu high-speed line."},
                {"time": "12:00–13:15", "title": "Busan Station Choryang Milmyeon Lunch", "detail": "Savor authentic cold wheat noodles and steamed dumplings.", "logistics": "Opposite Busan Station."},
                {"time": "13:45–15:00", "title": "Transfer to Haeundae Beach Base", "detail": "Check into Haeundae hotel (e.g. Felix by STX or L7 Haeundae).", "logistics": "Metro Line 2 or taxi across harbor bridge."},
                {"time": "15:30–18:00", "title": "Haeundae Beachfront Promenade Walk", "detail": "Stroll white sands of Haeundae Beach and follow the free Dongbaek Island wooden boardwalk to APEC House.", "logistics": "Paved oceanside walkway."},
                {"time": "18:30–21:00", "title": "Haeundae Traditional Market Feast", "detail": "Sample grilled seafood, tteokbokki, and famous seed hotteok.", "logistics": "Haeundae Traditional Market."}
            ],
            [
                {"label": "Direct Rail Speed", "text": "Direct KTX arrives in Busan by noon, maximizing afternoon coastal leisure."},
                {"label": "Haeundae Value Base", "text": "Haeundae provides seven nights of walkable beach access without moving hotels."}
            ],
            "Lunch: Choryang Milmyeon (cold wheat noodles & dumplings ~₩8,500). Dinner: Haeundae Market grilled seafood & ssiat hotteok (~₩18,000).",
            "Book KTX Cheonan-Asan→Busan on Korail app 30 days in advance.",
            "KTX ticket ~₩46,500; Beach and Dongbaek trail are free.",
            "Dongbaek Island trail is paved and lighted; Nurimaru APEC House closes at 17:00.",
            "SEA LIFE Busan Aquarium on Haeundae beachfront provides indoor shelter."
        ),
        # Day 14: Nov 14
        make_day(13, "Busan", "Free Hillside Stair Lifts & Old Alleys", "Busan · Haeundae Beachfront",
            "Choryang 168 Stairs & Haneul-gil Elevator (Free Public Lift) → Sanbokdoro Panoramic Bus → Saturday Drones",
            "Historic Hillside Stair Elevator & Saturday Night Drones",
            [
                {"time": "09:30–12:30", "title": "Choryang 168 Stairs & Haneul-gil Inclined Elevator & Observation Deck", "detail": "Ride the free 12-person inclined elevator (opened March 2025, replacing the old monorail retired in 2023) alongside the 168 Stairs into the historic hillside village, enjoying sweeping panoramic views across Busan Port from the Kim Min-bu observatory.", "logistics": "Busan Station Line 1 Exit 7, 10-min walk."},
                {"time": "12:45–14:00", "title": "Choryang Bulgogi Alley Lunch", "detail": "Savor sweet soy-marinated beef bulgogi with fresh leafy greens.", "logistics": "Choryang dining lane."},
                {"time": "14:30–16:30", "title": "Sanbokdoro (Mountain-Side Road) Scenic Bus Route", "detail": "Ride local city bus #86 along the mountain-hugging highway, gazing out over Busan harbor and shipyards for regular bus fare.", "logistics": "Bus 86 from Choryang."},
                {"time": "17:00–18:30", "title": "Gwangalli Beach Sunset Walk", "detail": "Watch sunset illuminate Gwangan Suspension Bridge.", "logistics": "Gwangan Station Line 2."},
                {"time": "19:00–21:30", "title": "Gwangalli Saturday Night 500-Drone Show & Chimaek", "detail": "Watch 500+ synchronized LED drones dance above Gwangan Bridge from the sand, enjoying Korean fried chicken.", "logistics": "Gwangalli Beach (drones at 19:00 & 21:00)."}
            ],
            [
                {"label": "Free Public Transit Marvel", "text": "The 168 Stairs inclined elevator and Bus 86 provide spectacular city panoramas for free or ordinary public transit fares."},
                {"label": "Saturday Night Drone Wonder", "text": "Timed specifically for Saturday evening to experience Gwangalli's free weekly drone spectacle."}
            ],
            "Lunch: Choryang marinated beef bulgogi (~₩10,000). Dinner: Gwangalli beachfront Korean fried chicken and draft beer (~₩18,000).",
            "Choryang 168 Stairs are open at all times; the free inclined elevator runs daytime hours — the former monorail was removed in 2023 and replaced by this elevator in March 2025.",
            "Elevator free; Bus 86 ₩1,550; Drone show free public viewing on the sand.",
            "Arrive at Gwangalli Beach 20 mins early for good sand seating.",
            "Gwangalli beachfront cafes provide heated indoor viewing."
        ),
        # Day 15: Nov 15
        make_day(14, "Busan", "Hillside Murals & Seafood Markets", "Busan · Haeundae Beachfront",
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
        make_day(15, "Busan", "Cliffside Alleys & Night Feasts", "Busan · Haeundae Beachfront",
            "Huinnyeoul Culture Village (Cliffside Sea Walk) → Bupyeong Night Market Feasting",
            "Dramatic Coastal Cliff Alleys & Vibrant Night Market Feasts",
            [
                {"time": "10:00–13:00", "title": "Huinnyeoul Culture Village & Coastal Sea Tunnel", "detail": "Walk the narrow cliffside pathways on Yeongdo Island overlooking crashing waves, exploring the illuminated coastal rock tunnel (all free access).", "logistics": "Bus 7/71/508 from Nampo Station Exit 6."},
                {"time": "13:15–14:45", "title": "Huinnyeoul Ocean-View Cafe Lunch", "detail": "Dine on fresh seafood ramyeon or toasted sandwiches overlooking the Korea Strait.", "logistics": "Huinnyeoul cliff cafe road."},
                {"time": "15:15–17:30", "title": "Lotte Department Store Gwangbok Sky Garden (Free Harbor View)", "detail": "Take the express elevator to the 13th-floor rooftop sky park for free 360-degree views of Busan Port and Yeongdo Bridge.", "logistics": "Nampo Station Line 1 direct basement connection."},
                {"time": "18:00–19:30", "title": "Yeongdo Bridge Sunset Walk", "detail": "Stroll across the historic bridge connecting mainland Busan to Yeongdo.", "logistics": "Nampo / Yeongdo bridge."},
                {"time": "20:00–22:00", "title": "Bupyeong Kkangtong Night Market Street Feast", "detail": "Sample iconic budget street dishes: Bibim Dangmyeon (spicy glass noodles), giant fried Busan fishcakes, skewered grilled pork, and rolled egg omelets.", "logistics": "Bupyeong Market (stalls open from 19:30)."}
            ],
            [
                {"label": "Free High-Altitude Views", "text": "Lotte Gwangbok Sky Garden provides free panoramic harbor views equal to paid observation towers."},
                {"label": "Affordable Night Gastronomy", "text": "Bupyeong Kkangtong Night Market allows you to sample a dozen unique dishes for minimal cost."}
            ],
            "Lunch: Huinnyeoul coastal ramyeon with seafood (~₩7,000). Dinner: Bupyeong Kkangtong Night Market assorted street dishes (~₩15,000).",
            "Huinnyeoul village and Lotte rooftop sky garden are 100% free.",
            "Free attractions; Lunch ~₩7,000; Night market ~₩15,000 per person.",
            "Huinnyeoul cliff paths have steep stairs; hold handrails.",
            "Lotte Department Store and Bupyeong covered arcade are fully indoor."
        ),
        # Day 17: Nov 17
        make_day(16, "Busan", "Estuary Wetlands & Fiery Sunsets", "Busan · Haeundae Beachfront",
            "Dadaepo Beach & Wetlands Boardwalk → Sunset Coastal Walk → Seomyeon BBQ",
            "Vast Coastal Reed Fields & Breathtaking Estuary Sunsets",
            [
                {"time": "11:00–13:30", "title": "Dadaepo Beach & Coastal Eco-Boardwalk", "detail": "Walk the wooden boardwalk across vast coastal tidal wetlands and golden autumn reed fields where the Nakdong River meets the South Sea (100% free admission).", "logistics": "Dadaepo Beach Station Line 1 Exit 4."},
                {"time": "13:45–15:00", "title": "Dadaepo Clam Kalguksu Lunch", "detail": "Enjoy hearty hand-cut clam noodle soup in an earthenware pot.", "logistics": "Dadaepo beach dining row."},
                {"time": "15:30–17:30", "title": "Dadaepo Sunset Dune Walk", "detail": "Watch the fiery sunset blaze across the ocean horizon, illuminating the vast sandy flats.", "logistics": "Dadaepo coastal dune path."},
                {"time": "18:00–19:30", "title": "Metro to Seomyeon & Youth Shopping Walk", "detail": "Explore Seomyeon underground mall and youth street.", "logistics": "Metro Line 1."},
                {"time": "20:00–21:30", "title": "Seomyeon Korean Charcoal BBQ Dinner", "detail": "Feast on tender charcoal-grilled pork neck and kimchi stew.", "logistics": "Seomyeon dining lane."}
            ],
            [
                {"label": "Busan's Greatest Sunset Horizon", "text": "Dadaepo provides the most expansive and dramatic sunset horizon in southern Korea for zero cost."},
                {"label": "Pristine Estuary Ecology", "text": "Nakdong estuary reed boardwalks offer peaceful, uncrowded nature walks."}
            ],
            "Lunch: Dadaepo fresh clam kalguksu (~₩9,000). Dinner: Seomyeon charcoal pork BBQ with steamed egg and soybean stew (~₩20,000).",
            "Dadaepo Beach and boardwalk trails are open 24/7 for free.",
            "Free park; Lunch ~₩9,000; Dinner ~₩20,000 per person.",
            "Coastal winds can be brisk at sunset; wear a windbreaker jacket.",
            "Seomyeon underground shopping city is 100% indoor and heated."
        ),
        # Day 18: Nov 18
        make_day(17, "Busan", "Free Tea Heritage & Silla Temples", "Busan · Haeundae Beachfront",
            "Busan Museum (Free Admission & Tea Ceremony) → UN Memorial Cemetery → Beomeosa Temple",
            "Free Traditional Tea Ceremonies & 1,300-Year Mountain Temples",
            [
                {"time": "09:30–12:00", "title": "Busan Museum & Free Darye Tea Ceremony", "detail": "Explore Busan's archaeological treasures and participate in a traditional Korean tea ceremony (Darye) wearing hanbok in the cultural hall (100% free experience).", "logistics": "Daeyeon Station Line 2 Exit 3."},
                {"time": "12:15–13:30", "title": "Daeyeon Ssangdungi Dwaeji Gukbap Lunch", "detail": "Savor famous boiled pork slices (suyuk baekban) served with warm pork broth and rice.", "logistics": "5-minute walk from museum."},
                {"time": "13:45–15:30", "title": "UN Memorial Cemetery in Korea", "detail": "Walk the peaceful, beautifully landscaped botanical memorial grounds (free admission).", "logistics": "Adjacent to Busan Museum."},
                {"time": "16:00–18:30", "title": "Beomeosa Ancient Mountain Temple Stroll", "detail": "Ascend Mount Geumjeong to tour the 678 AD Silla Buddhist headquarters surrounded by peaceful bamboo groves (free entry).", "logistics": "Beomeosa Station Line 1 Exit 5 + Bus 90."},
                {"time": "19:00–21:00", "title": "Dongnae Halmae Pajeon Dinner", "detail": "Enjoy royal scallion seafood pancake with Geumjeongsanseong makgeolli.", "logistics": "Dongnae dining street."}
            ],
            [
                {"label": "Free High-Touch Cultural Activity", "text": "Busan Museum provides authentic traditional tea ceremony and Hanbok wearing experiences at zero cost."},
                {"label": "Spiritual Mountain Beauty", "text": "Beomeosa Temple is one of Korea's greatest ancient Buddhist complexes with free public entry."}
            ],
            "Lunch: Daeyeon Ssangdungi Dwaeji Gukbap (~₩9,500). Dinner: Dongnae scallion seafood pancake and makgeolli (~₩22,000).",
            "Busan Museum tea ceremony registration is free at 1F counter upon arrival.",
            "Museum free; Cemetery free; Temple free; Meals ~₩32,000 per person.",
            "Respectful silence requested on temple and memorial grounds.",
            "Busan Museum is completely indoor and heated."
        ),
        # Day 19: Nov 19
        make_day(18, "Busan", "Low-Stakes Coastal Stroll (CSAT Day)", "Busan · Haeundae Beachfront",
            "Songjeong Beach Gentle Stroll → Haedong Yonggungsa Temple (CSAT Day)",
            "Peaceful Waves, Seaside Temples & Gentle Pace (CSAT / Suneung Day)",
            [
                {"time": "10:00–12:30", "title": "Songjeong Beach Scenic Coastal Stroll", "detail": "Walk the quiet sands of Songjeong Beach, watching surfers catch autumn waves and exploring Jukdo Park pine pavilion.", "logistics": "Bus 100/181 from Haeundae."},
                {"time": "12:45–14:00", "title": "Songjeong Beachfront Lunch", "detail": "Enjoy fresh seafood noodle soup or bibimbap overlooking the sea.", "logistics": "Songjeong restaurant row."},
                {"time": "14:15–16:30", "title": "Haedong Yonggungsa Temple (Temple by the Sea)", "detail": "Visit the 1376 Buddhist cliffside sanctuary listening to rhythmic ocean waves crashing on granite rocks below (free entry).", "logistics": "Short bus or taxi from Songjeong."},
                {"time": "17:00–19:00", "title": "Haeundae Sunset Beach Stroll", "detail": "Relax along Haeundae sands reflecting on 7 unforgettable Busan nights.", "logistics": "Haeundae beachfront."},
                {"time": "19:30–21:30", "title": "Busan Farewell Feast: Hanwoo Beef Barbecue", "detail": "Celebrate final night in Busan with premium charcoal-grilled Korean Hanwoo beef tenderloin.", "logistics": "Haeundae Somunnan Amso Galbi."}
            ],
            [
                {"label": "CSAT Low-Stakes Alignment", "text": "Nov 19 national CSAT exam day is kept localized along the eastern coast to avoid urban transit hold zones."},
                {"label": "Free Coastal Sanctuaries", "text": "Haedong Yonggungsa and Songjeong offer world-class ocean scenery with zero entrance fees."}
            ],
            "Lunch: Songjeong seafood noodle soup. Dinner: Haeundae Somunnan Amso Galbi (marinated beef short ribs with potato noodles).",
            "Haedong Yonggungsa Temple is free entry; open year-round.",
            "Temple is free; Farewell Hanwoo dinner ~₩45,000–₩55,000 per person.",
            "Pack primary bags tonight for Friday morning KTX to Seoul.",
            "Haeundae beachfront indoor cafes offer heated panoramic sea views."
        ),
        # Day 20: Nov 20
        make_day(19, "Seoul", "Capital Return & Sky Garden", "Seoul · Seoul Station / Myeongdong",
            "Morning KTX Busan to Seoul → Seoullo 7017 Sky Garden → Namdaemun Kalguksu Alley",
            "Capital Return, Free Elevated Sky Garden & Kalguksu Feasts",
            [
                {"time": "09:30–10:15", "title": "Busan Station Departure", "detail": "Check out of Haeundae hotel, take metro or taxi to Busan Station, and board direct KTX.", "logistics": "Board train 10 minutes prior to departure."},
                {"time": "10:30–12:45", "title": "KTX High-Speed Rail to Seoul", "detail": "Comfortable 2-hour 15-minute high-speed journey back to Seoul Station.", "logistics": "Direct arrival inside Seoul Station concourse."},
                {"time": "13:00–14:30", "title": "Seoul Station Hotel Check-in & Lunch", "detail": "Check into hotel directly at Seoul Station and drop bags.", "logistics": "Direct hotel connection."},
                {"time": "15:00–17:30", "title": "Seoullo 7017 Sky Garden Walk to Namdaemun", "detail": "Walk the 1km elevated highway overpass garden lined with 24,000 Korean trees and flowers directly into Namdaemun Market (free).", "logistics": "Direct elevated bridge from Seoul Station."},
                {"time": "18:00–20:30", "title": "Namdaemun Market Kalguksu Alley Dinner", "detail": "Dine in famous Kalguksu Alley where ordering warm hand-pulled noodles includes a free cold spicy bibim naengmyeon bowl and soybean soup!", "logistics": "Hoehyeon Station Line 4 Exit 5."}
            ],
            [
                {"label": "Strategic Departure Security", "text": "Arriving in Seoul on Friday eliminates all risk of KTX weekend disruption before Sunday flight."},
                {"label": "Double-Noodle Value", "text": "Namdaemun Kalguksu Alley offers the famous 2-for-1 noodle deal beloved by budget-conscious locals."}
            ],
            "Lunch: Seoul Station bibimbap. Dinner: Namdaemun Kalguksu Alley (hand-pulled noodle soup + free bibim naengmyeon ~₩8,000).",
            "Book KTX Busan→Seoul on Korail app 30 days in advance.",
            "KTX ticket ~₩59,800; Seoullo 7017 free; Dinner ~₩8,000 per person.",
            "Friday afternoon KTX trains fill up quickly; secure reserved seats early.",
            "Lotte Mart and Seoul Station concourse are completely enclosed."
        ),
        # Day 21: Nov 21
        make_day(20, "Seoul", "Smart Souvenirs & Farewell Banquet", "Seoul · Seoul Station / Myeongdong",
            "Namdaemun Market Craft Alleys → Seoul Station Lotte Mart (Instant Tax Refund) → Grand Farewell Feast",
            "Tax-Free Pantry Curation & Celebration Feast",
            [
                {"time": "09:30–12:30", "title": "Namdaemun Market Kitchenware & Snack Alleys", "detail": "Curate traditional wooden tea trays, Korean stainless steel chopsticks, and dried seaweed (gim).", "logistics": "Hoehyeon Station Line 4 Exit 5."},
                {"time": "13:00–15:30", "title": "Seoul Station Lotte Mart Mega-Store Curation", "detail": "Fill luggage with value food gifts: multi-pack seasoned seaweed, market snack boxes, gochujang, and instant noodles with instant tax refund.", "logistics": "Immediate tax refund counter on 2F with passport."},
                {"time": "16:00–18:00", "title": "Afternoon Packing & Luggage Weighing", "detail": "Return to hotel room, organize souvenirs, check luggage weight against airline allowance, and complete online flight check-in.", "logistics": "Hotel front desk provides digital scale."},
                {"time": "18:30–21:00", "title": "Grand Farewell Korean BBQ Feast", "detail": "Celebrate the 21-night journey with premium Korean Hanwoo beef barbecue and aged kimchi stew in central Seoul.", "logistics": "Myeongdong / Gwanghwamun dining room."}
            ],
            [
                {"label": "Smart Tax-Free Savings", "text": "Handling instant tax refunds at Lotte Mart saves 30+ minutes and lines at airport customs."},
                {"label": "Zero Departure Stress", "text": "All shopping and packing completed by Saturday night ensures Sunday morning is 100% serene."}
            ],
            "Lunch: Namdaemun Market japchae vegetable hotteok and dumplings (~₩6,000). Dinner: Premium Hanwoo charcoal BBQ banquet (~₩45,000).",
            "Complete online airline check-in 24 hours prior; select seats and enter passport numbers.",
            "Souvenirs ~₩40,000–₩80,000; Farewell dinner ~₩45,000 per person.",
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
                {"time": "12:30–13:00", "title": "Boarding & Takeoff", "detail": "Board aircraft for the return flight home with unforgettable memories of authentic Korean living and smart value travel.", "logistics": "Gates close 15 minutes before scheduled departure."}
            ],
            [
                {"label": "Logistics Perfection", "text": "Direct AREX express from hotel doorstep guarantees predictable 43-minute airport transit."},
                {"label": "Zero Rush", "text": "Arriving at 10:15 leaves ample time for customs, tax refunds, and a relaxed pre-flight meal."}
            ],
            "Breakfast: Hotel café or airport lounge / Korean Food Street at ICN Terminal (bibimbap/soup).",
            "Verify terminal (T1 vs T2) based on airline ticket before boarding AREX.",
            "AREX Express ticket ₩13,000 per person (fare raised from ₩11,000; verified 2026).",
            "Terminal 2 is 8 minutes further on the AREX line than Terminal 1; check your terminal code.",
            "If AREX express sells out, AREX All-Stop commuter train departs every 6–10 minutes."
        )
    ]

    scorecard = [
        {"label": "Budget Optimization", "value": "5/5", "tone": "good"},
        {"label": "Local Market Depth", "value": "5/5", "tone": "good"},
        {"label": "Free Cultural Sights", "value": "5/5", "tone": "good"},
        {"label": "Rail Speed & Value", "value": "5/5", "tone": "good"}
    ]

    return {
        "id": "seoul-cheonan-busan-value",
        "shortTitle": "Seoul · Cheonan · Busan (Value & Local Living)",
        "title": "Smart Value & Authentic Neighborhood Living (Value & Local Living)",
        "routeLabel": "Seoul (7N) → Cheonan (5N) → Busan (7N) → Seoul (2N)",
        "badge": "Smart Value & Authentic Local Markets",
        "bestFor": "Budget-conscious travelers, backpackers, solo explorers, and savvy planners who love authentic traditional markets, free panoramic city wall trails, neighborhood food alleys, and maximum transit value.",
        "decisionSummary": "A brilliantly cost-effective 21-night itinerary leveraging Korea's incredible free public treasures (Seoul City Wall, National Palace Museum, Independence Hall, Choryang 168 Stairs hillside elevator, Dadaepo reed trails) alongside authentic market feasts and budget-smart Cheonan hotel pricing.",
        "recommendation": "Choose this route if you want to stretch your travel budget further while experiencing genuine Korean everyday neighborhood life, street snacks, and panoramic public parks.",
        "tradeoff": "More meals taken at traditional market stalls and casual neighborhood eateries rather than luxury hotel dining rooms.",
        "scorecard": scorecard,
        "bases": get_scb_common_bases(),
        "transfers": get_scb_common_transfers(),
        "budgetScenarios": get_scb_budget_scenarios(),
        "bookingPriorities": get_scb_booking_priorities(),
        "days": days
    }
