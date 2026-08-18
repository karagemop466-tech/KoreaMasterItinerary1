#!/usr/bin/env python3
"""Route Blueprint: Seoul · Cheonan · Busan (Family Comfort, Gentle Parks & Relaxed Leisure)."""

from scripts.generate_all_itineraries import make_day
from scripts.itinerary_builder_scb import (
    get_scb_common_bases,
    get_scb_common_transfers,
    get_scb_budget_scenarios,
    get_scb_booking_priorities
)

def get_scb_leisure():
    days = [
        # Day 1: Nov 1
        make_day(0, "Seoul", "Arrival", "Seoul · Myeongdong / Seoul Station edge",
            "ICN arrival at 21:00 → smooth direct transfer → comfortable hotel check-in → late sleep",
            "Unhurried Landing & Family Comfort Base Check-in",
            [
                {"time": "21:00–22:15", "title": "ICN Arrival & Border Clearance", "detail": "Clear immigration smoothly, collect checked luggage, and pick up pre-arranged family connectivity tools.", "logistics": "Terminal 1 or 2."},
                {"time": "22:30–23:45", "title": "Direct Transfer to Hotel Base", "detail": "Direct Airport Limousine Bus or official taxi directly to Myeongdong / Seoul Station hotel.", "logistics": "Minimizes luggage handling and late-night stairs."},
                {"time": "23:45–00:30", "title": "Hotel Check-in & Rest", "detail": "Settle into spacious hotel room, unpack essentials, and enjoy deep, unhurried sleep.", "logistics": "Late morning wakeup planned tomorrow (10:00 AM start)."}
            ],
            [
                {"label": "Gentle Schedule Rule", "text": "All days feature relaxed 10:00 AM starts and zero morning rushing."},
                {"label": "Family Comfort", "text": "Hotel bases provide elevators, wide doorways, and direct transit access."}
            ],
            "Light convenience store snack or hotel room service.",
            "Confirm late check-in with hotel in writing.",
            "Limousine Bus ~₩17,000 / Deluxe Taxi ~₩85,000.",
            "Sleep late tomorrow; first sightseeing starts at 10:00 AM.",
            "Hotel front desk provides 24-hour service."
        ),
        # Day 2: Nov 2
        make_day(1, "Seoul", "Gentle Palaces & Folk Gardens", "Seoul · Myeongdong / Seoul Station edge",
            "10:00 AM start: Gyeongbokgung Palace Gentle Stroll → Children's Folk Museum → Samcheong Cafe",
            "Royal Courtyards, Folk Tale Exhibits & Relaxed Tea Patios",
            [
                {"time": "10:00–12:30", "title": "Gyeongbokgung Royal Palace & Folk Museum", "detail": "Watch the colorful Royal Guard ceremony and stroll wide, flat palace courtyards to the National Folk Museum's interactive outdoor folk village and Children's Museum.", "logistics": "Gyeongbokgung Station Line 3 Exit 5."},
                {"time": "12:45–14:15", "title": "Samcheong-dong Garden Cafe Lunch", "detail": "Enjoy mild beef bulgogi, handmade dumplings, or stone-pot bibimbap in a peaceful Samcheong garden courtyard.", "logistics": "Short flat walk from palace east gate."},
                {"time": "14:30–16:30", "title": "Bukchon Hanok Main Promenade Walk", "detail": "Gentle stroll along the wide, paved main ridge of Bukchon Hanok Village, visiting traditional craft ateliers.", "logistics": "Anguk Station Line 3."},
                {"time": "17:00–18:30", "title": "Insadong Ssamzigil & Sweet Red Bean Treats", "detail": "Browse spiral courtyard craft stalls and enjoy warm sweet red bean pastries and roasted tea.", "logistics": "Insadong pedestrian zone."},
                {"time": "19:00–21:00", "title": "Comforting Korean Beef Barbecue Dinner", "detail": "Savor sweet soy-marinated beef bulgogi and mild egg custard.", "logistics": "Jongno / Myeongdong dining hall."}
            ],
            [
                {"label": "10:00 AM Morning Start", "text": "Allows families and leisure travelers to wake up naturally and enjoy a relaxed hotel breakfast."},
                {"label": "Flat Accessible Walkways", "text": "Paved courtyards and ramped museum pathways avoid steep, exhausting climbs."}
            ],
            "Lunch: Samcheong-dong mild beef bulgogi and handmade dumplings. Dinner: Mild charcoal-grilled beef galbi with steamed egg custard.",
            "Palace entry ₩3,000 (free for children under 6 and seniors over 65).",
            "Palace entry ₩3,000; Dinner ~₩30,000 per person.",
            "Stroller and wheelchair rentals available free at palace ticket gate.",
            "National Folk Museum is fully indoor, heated, and family-friendly."
        ),
        # Day 3: Nov 3
        make_day(2, "Seoul", "Tower Observatories & Marine Aquariums", "Seoul · Myeongdong / Seoul Station edge",
            "10:00 AM start: Lotte World Tower Seoul Sky (123F) → Lotte World Aquarium → Seokchon Lake",
            "Sky-High Glass Observatories, Beluga Whales & Lakeside Strolls",
            [
                {"time": "10:00–12:30", "title": "Lotte World Tower Seoul Sky (123rd Floor)", "detail": "Take the world's fastest double-deck elevator (Sky Shuttle) to the 500-meter-high glass-floor observation deck for breathtaking panoramic views of the entire Seoul metropolitan area.", "logistics": "Jamsil Station Line 2/8 direct basement connection."},
                {"time": "12:30–14:00", "title": "Lotte World Mall Gourmet Avenue Lunch", "detail": "Dine in the sprawling family-friendly dining pavilion on Korean noodles, tonkatsu, or gourmet bibimbap.", "logistics": "Lotte World Mall 5F/6F."},
                {"time": "14:15–16:45", "title": "Lotte World Aquarium", "detail": "Explore Korea's largest ocean ecology tunnel, viewing beluga whales, sea otters, penguins, and 650 marine species across 13 themed zones.", "logistics": "Lotte World Mall B1."},
                {"time": "17:00–18:30", "title": "Seokchon Lake Autumn Stroll", "detail": "Walk the flat, scenic 2.5km paved path around the lake shaded by autumn trees, capturing Lotte Tower reflections.", "logistics": "Adjacent to Lotte Mall."},
                {"time": "19:00–21:00", "title": "Jamsil Korean Beef & Mushroom Hot Pot Dinner", "detail": "Enjoy mild beef shabu-shabu hot pot with hand-pulled noodles.", "logistics": "Jamsil dining arcade."}
            ],
            [
                {"label": "All-in-One Indoor Entertainment", "text": "Seoul Sky, Aquarium, and Mall are directly interconnected with zero weather exposure."},
                {"label": "Sensory Delight for All Ages", "text": "Combines soaring skyward views with captivating underwater marine exhibits."}
            ],
            "Lunch: Lotte World Mall gourmet food avenue. Dinner: Mild beef and fresh mushroom shabu-shabu hot pot.",
            "Book Seoul Sky & Aquarium combo ticket online in advance for family savings.",
            "Seoul Sky + Aquarium combo ~₩45,000; Dinner ~₩25,000 per person.",
            "Strollers permitted throughout Seoul Sky and Aquarium facilities.",
            "Lotte World complex is 100% enclosed, heated, and weatherproof."
        ),
        # Day 4: Nov 4
        make_day(3, "Seoul", "Children's Parks & Botanical Conservatories", "Seoul · Myeongdong / Seoul Station edge",
            "10:00 AM start: Seoul Children's Grand Park → Tropical Conservatory → Animal Village Walk",
            "Golden Park Foliage, Free Animal Sanctuaries & Greenhouses",
            [
                {"time": "10:00–13:00", "title": "Children's Grand Park & Animal Village", "detail": "Walk through 530,000 square meters of flat autumn parkland, visiting the free outdoor animal village (elephants, red pandas, meerkats) and scenic duck ponds.", "logistics": "Children's Grand Park Station Line 7 Exit 1 or Achasan Station Line 5 Exit 4."},
                {"time": "13:15–14:30", "title": "Park Pavilion Family Lunch", "detail": "Enjoy Korean dolsot bibimbap, handmade noodles, or family katsu in the park pavilion.", "logistics": "Park central plaza."},
                {"time": "14:45–16:30", "title": "Botanical Garden & Tropical Greenhouse", "detail": "Stroll through the warm indoor botanical conservatory filled with flowering orchids, desert cacti, and tropical palms (free entry).", "logistics": "Inside Children's Grand Park."},
                {"time": "17:00–18:30", "title": "Dongdaemun Design Plaza Twilight Walk", "detail": "Gentle stroll around DDP's futuristic curved gardens.", "logistics": "Dongdaemun History & Culture Park Station."},
                {"time": "19:00–21:00", "title": "Mild Korean Dumpling & Noodle Feast", "detail": "Enjoy steamed handmade pork dumplings and mild chicken broth kalguksu.", "logistics": "Central Seoul dining room."}
            ],
            [
                {"label": "Completely Free Family Park", "text": "Children's Grand Park provides a world-class zoo, botanical conservatory, and open lawns for zero admission."},
                {"label": "Flat, Relaxing Terrain", "text": "Gentle, wide paved walkways ideal for strollers and travelers seeking unhurried pacing."}
            ],
            "Lunch: Park pavilion family bibimbap and tonkatsu. Dinner: Steamed handmade pork mandu and warm kalguksu noodles.",
            "Children's Grand Park and Zoo are 100% free admission; open daily 05:00–22:00.",
            "Park is free; Lunch ~₩12,000; Dinner ~₩20,000 per person.",
            "Park stroller rentals available near main gate.",
            "Botanical Conservatory and indoor play pavilions provide covered shelter."
        ),
        # Day 5: Nov 5
        make_day(4, "Seoul", "National Treasures & Mirror Ponds", "Seoul · Myeongdong / Seoul Station edge",
            "10:00 AM start: National Museum of Korea (Mirror Pond & Contemplation) → Yongsan Family Park",
            "Accessible Masterpieces, Mirror Ponds & Flat Lawns",
            [
                {"time": "10:00–13:00", "title": "National Museum of Korea Masterpieces", "detail": "Explore the barrier-free permanent exhibition halls, viewing the Pensive Bodhisattva statues, Gyeongcheonsa Pagoda, and golden Silla crowns.", "logistics": "Ichon Station Line 4 direct underground museum walkway (fully elevator-accessible)."},
                {"time": "13:15–14:30", "title": "Museum Mirror Pond Dining Lunch", "detail": "Dine overlooking the traditional wooden pavilion and tranquil reflection lake.", "logistics": "Museum 1F dining hall."},
                {"time": "14:45–16:30", "title": "National Hangeul Museum & Children's Discovery Zone", "detail": "Explore King Sejong's scientific Korean alphabet through interactive touch screens and sound games (free admission).", "logistics": "Adjacent to National Museum."},
                {"time": "17:00–18:30", "title": "Yongsan Family Park Meadow Walk", "detail": "Relax along flat, unhurried tree-lined walking tracks and tranquil ponds.", "logistics": "Directly connected to museum grounds."},
                {"time": "19:00–21:00", "title": "Nourishing Korean Hanwoo Beef Gomtang Dinner", "detail": "Savor slow-simmered, non-spicy clear beef brisket soup with warm rice.", "logistics": "Samgakji / Myeongdong."}
            ],
            [
                {"label": "Universal Accessibility", "text": "National Museum offers barrier-free elevators, wide stone paths, and smooth ramps throughout."},
                {"label": "Mindful Pacing", "text": "Room of Quiet Contemplation provides a peaceful, meditative sanctuary without sensory overload."}
            ],
            "Lunch: National Museum Mirror Pond Korean set. Dinner: Mild Hanwoo beef gomtang soup with scallions.",
            "National Museum permanent galleries and Hangeul Museum are free admission.",
            "Museums free; Lunch ~₩15,000; Dinner ~₩22,000 per person.",
            "Elevators connect all floors; wheelchairs and strollers available free at information desk.",
            "National Museum of Korea is fully indoor, heated, and spacious."
        ),
        # Day 6: Nov 6
        make_day(5, "Seoul", "Riverside Cruises & Picnic Lawns", "Seoul · Myeongdong / Seoul Station edge",
            "10:00 AM start: Han River Scenic Cruise from Yeouido → Banpo Hangang Park Open Lawns",
            "Gentle River Cruises, Sunset Lawns & Family Picnics",
            [
                {"time": "10:30–12:30", "title": "Yeouido The Hyundai Seoul Indoor Garden Atrium", "detail": "Stroll through the 5th-floor indoor Sounds Forest atrium under natural glass skylights, visiting robotic cafes and boutique bakeries.", "logistics": "Yeouido Station Line 5/9 direct underground walkway."},
                {"time": "12:30–14:00", "title": "Tasty Seoul Gourmet Food Hall Lunch", "detail": "Enjoy family-friendly artisanal dining and desserts in the basement food hall.", "logistics": "The Hyundai Seoul B1."},
                {"time": "14:30–16:30", "title": "Han River Scenic Cruise (E-Land Cruise)", "detail": "Board a relaxing 40-minute sightseeing cruise along the Han River, feeding seagulls and viewing city bridges from the open deck.", "logistics": "Yeouido E-Land Cruise Pier."},
                {"time": "17:00–18:30", "title": "Yeouido Hangang Park Lawn Walk", "detail": "Relax along the grassy riverbank as twilight reflects on the water.", "logistics": "Yeouinaru Station Line 5 Exit 2."},
                {"time": "19:00–21:00", "title": "Mild Korean Chicken & Potato Feast", "detail": "Enjoy non-spicy honey butter Korean fried chicken and potato wedges.", "logistics": "Central Seoul dining room."}
            ],
            [
                {"label": "Scenic River Cruising", "text": "Cruising down the Han River provides magnificent panoramic views without walking fatigue."},
                {"label": "Indoor Atrium Serenity", "text": "Sounds Forest offers a climate-controlled botanical garden inside a modern architectural marvel."}
            ],
            "Lunch: The Hyundai Seoul gourmet food hall. Dinner: Non-spicy honey butter Korean chicken with crispy fries.",
            "Book Han River E-Land Cruise tickets at pier or online (passport required for manifest).",
            "Cruise ticket ~₩16,000; Dinner ~₩22,000 per person.",
            "Warm outer layer recommended for breezy open cruise decks.",
            "The Hyundai Seoul is 100% indoor and weatherproof."
        ),
        # Day 7: Nov 7
        make_day(6, "Seoul", "Mega Aquariums & KTX Prep", "Seoul · Myeongdong / Seoul Station edge",
            "10:00 AM start: Starfield COEX Aquarium & Library → Bongeunsa Flat Garden → Sunday KTX Prep",
            "Ocean Walkways, Giant Book Towers & Rail Preparation",
            [
                {"time": "10:00–12:30", "title": "COEX Aquarium (Gangnam Marine Sanctuary)", "detail": "Walk through 16 themed ocean zones, underwater glass tunnels, and see giant stingrays, sea turtles, and sand tiger sharks.", "logistics": "Samseong Station Line 2 or Bongeunsa Station Line 9."},
                {"time": "12:30–14:00", "title": "Parnas Mall Gourmet Arcade Lunch", "detail": "Enjoy mild beef soup (gomtang) or royal hot pot in the lower level arcade.", "logistics": "Directly connected to COEX."},
                {"time": "14:15–16:00", "title": "Starfield Library & Bongeunsa Temple", "detail": "Photograph the 13-meter tall open book towers and take a gentle walk through Bongeunsa Temple's flat stone courtyards.", "logistics": "Bongeunsa Station Exit 1."},
                {"time": "16:30–18:30", "title": "Seoul Station Packing & Train Verification", "detail": "Return to Seoul Station base, pack luggage for Sunday morning KTX to Cheonan-Asan, and confirm seat assignments.", "logistics": "Seoul Station hotel."},
                {"time": "19:00–21:00", "title": "Seoul Station Hearty Korean Stew Dinner", "detail": "Enjoy mild beef bulgogi hot pot or bibimbap.", "logistics": "Seoul Station dining lane."}
            ],
            [
                {"label": "Leisure Pacing", "text": "Spacious underground complexes provide gentle walking with zero traffic or weather stress."},
                {"label": "Short Rail Leap Prep", "text": "Packing early ensures a relaxed Sunday morning 35-minute train ride to Cheonan."}
            ],
            "Lunch: Hadongkwan traditional gomtang soup at COEX. Dinner: Mild beef bulgogi hot pot with glass noodles.",
            "COEX Aquarium open daily 10:00–20:00; admission ₩32,000 (discounts online).",
            "Aquarium ~₩30,000; Library free; Temple free; Dinner ~₩25,000 per person.",
            "COEX mall is vast; use interactive touchscreen floor directories.",
            "COEX complex is 100% enclosed, heated, and weatherproof."
        ),
        # Day 8: Nov 8
        make_day(7, "Cheonan", "City Transition & Thermal Water Park", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "10:00 AM KTX to Cheonan-Asan (35 mins) → Sono Belle Ocean Adventure (Indoor Thermal Pool)",
            "Short 35-Minute Rail Leap & Heated Mineral Waterparks",
            [
                {"time": "10:00–10:35", "title": "KTX High-Speed Rail Seoul to Cheonan-Asan", "detail": "Comfortable 35-minute high-speed journey from Seoul Station to Cheonan-Asan Station.", "logistics": "Board train at Seoul Station."},
                {"time": "10:45–12:00", "title": "Hotel Check-in & Base Setup", "detail": "Check into family comfort base (e.g. Shilla Stay Cheonan or Ramada Encore Cheonan-Asan) and drop bags.", "logistics": "Station area / Shinbu-dong."},
                {"time": "12:15–13:30", "title": "Shinbu-dong Family Gourmet Lunch", "detail": "Enjoy mild Korean beef noodles or handmade dumplings in central Cheonan.", "logistics": "Shinbu-dong dining district."},
                {"time": "14:00–18:00", "title": "Sono Belle Cheonan Ocean Adventure (Indoor Heated Spa)", "detail": "Relax in the heated indoor hydrotherapy spa pools, gentle lazy river, wave pool, and mineral thermal baths.", "logistics": "Dongnam-gu Seongnam-myeon; 20-min taxi from hotel."},
                {"time": "18:30–20:30", "title": "Cheonan Sizzling Beef Bulgogi Dinner", "detail": "Feast on tender beef bulgogi with mild side dishes.", "logistics": "Cheonan dining lane."}
            ],
            [
                {"label": "Shortest Intercity Rail Trip", "text": "At just 35 minutes, travel time is effortless for travelers of all ages."},
                {"label": "Heated Mineral Hydrotherapy", "text": "Sono Belle's indoor thermal pools provide warm, playful aquatic relaxation in November."}
            ],
            "Lunch: Shinbu-dong mild dumpling noodle soup. Dinner: Cheonan charcoal-grilled beef bulgogi with rice.",
            "Book KTX Seoul→Cheonan-Asan on Korail app 30 days prior.",
            "KTX ticket ~₩14,100; Sono Belle indoor spa pass ~₩30,000; Dinner ~₩25,000 per person.",
            "Swim caps/hats required inside Sono Belle indoor waterpark; rental available.",
            "Sono Belle Ocean Adventure indoor waterpark is heated and fully enclosed."
        ),
        # Day 9: Nov 9
        make_day(8, "Cheonan", "Astronomy & Interactive Science", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "10:00 AM start: Hong Dae-yong Science Museum & Planetarium → 3D Dome Cinema",
            "Interactive Space Simulators, 3D Astronomy & Stargazing",
            [
                {"time": "10:00–13:00", "title": "Hong Dae-yong Science Museum & Space Simulators", "detail": "Explore the legacy of Joseon astronomer Hong Dae-yong through interactive gravity-free simulators, lunar walking simulations, and optical illusions.", "logistics": "Dongnam-gu Susan-myeon; 25-min taxi or Bus 400."},
                {"time": "13:15–14:30", "title": "Museum Plaza Family Lunch", "detail": "Enjoy Korean rice sets, tonkatsu, or mild noodle soup.", "logistics": "Science museum cafe plaza."},
                {"time": "14:45–16:30", "title": "Planetarium 3D Digital Dome Theater", "detail": "Recline beneath a 15-meter hemispherical dome screen watching immersive 3D space voyages through the solar system.", "logistics": "Inside Science Museum 4F."},
                {"time": "17:00–18:30", "title": "Shinbu Cultural Street Stroll", "detail": "Explore youth fashion shops and dessert cafes.", "logistics": "Shinbu-dong."},
                {"time": "19:00–21:00", "title": "Cheonan Charcoal Pork BBQ Dinner", "detail": "Feast on tender pork neck and mild soybean stew.", "logistics": "Shinbu-dong dining lane."}
            ],
            [
                {"label": "Engaging Interactive Science", "text": "Space simulators and 3D planetarium screenings make astronomy exciting and accessible for all ages."},
                {"label": "Cultural Astronomer Roots", "text": "Honors Hong Dae-yong's pioneering 18th-century heliocentric astronomy in Korea."}
            ],
            "Lunch: Science museum family cafe dining. Dinner: Shinbu-dong charcoal pork BBQ with steamed egg custard.",
            "Hong Dae-yong Science Museum closed on Mondays; entry ₩3,000 (planetarium ₩2,000).",
            "Museum ~₩5,000 total; Taxi ~₩15,000 each way; Dinner ~₩25,000 per person.",
            "Space simulators have height requirements (minimum 120cm for gyro simulator).",
            "Science Museum and Planetarium are fully enclosed and climate-controlled."
        ),
        # Day 10: Nov 10
        make_day(9, "Cheonan", "Arboretum Gardens & Folk Pavilions", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "10:00 AM start: Beautiful Garden Hwasoomok Arboretum → Cheonan Samgeori Park",
            "Open Arboretum Lawns, Waterfall Cafes & Willow Ponds",
            [
                {"time": "10:00–13:00", "title": "Beautiful Garden Hwasoomok (Private Arboretum)", "detail": "Stroll Korea's designated Private Garden #1, exploring flat floral walking paths, a tropical greenhouse, bonsai gardens, and a scenic indoor waterfall bakery cafe.", "logistics": "Dongnam-gu Mokcheon-eup; 15-min taxi."},
                {"time": "13:15–14:30", "title": "Hwasoomok Arboretum Bakery & Dining Lunch", "detail": "Enjoy artisan wood-fired pizza, pasta, and freshly baked breads overlooking the gardens.", "logistics": "Inside Hwasoomok complex."},
                {"time": "15:00–17:00", "title": "Cheonan Samgeori Park Heritage Walk", "detail": "Walk around the peaceful willow-shaded lake and classical pavilions where Korea's royal highways intersected.", "logistics": "Dongnam-gu Samnyong-dong."},
                {"time": "17:30–19:00", "title": "1934 Original Hakhwa Hodu-gwaja Bakery", "detail": "Taste warm walnut cakes fresh from the oven and pick up gift boxes.", "logistics": "Cheonan Station branch."},
                {"time": "19:30–21:00", "title": "Cheonan Mild Beef Shabu-Shabu Dinner", "detail": "Enjoy thinly sliced beef and fresh vegetables simmered in clear kelp broth.", "logistics": "Central Cheonan."}
            ],
            [
                {"label": "Botanical Leisure", "text": "Hwasoomok offers pristine paved garden paths and spacious indoor dining pavilions."},
                {"label": "Historical Crossroad Serenity", "text": "Samgeori Park provides flat, peaceful willow-shaded walks."}
            ],
            "Lunch: Hwasoomok wood-fired pizza and artisan pasta. Afternoon: Warm 1934 Hakhwa walnut pastries. Dinner: Mild beef shabu-shabu hot pot.",
            "Hwasoomok garden entry ₩5,000 (includes greenhouse access); Samgeori Park is free.",
            "Garden ₩5,000; Hodu-gwaja ~₩6,000; Dinner ~₩25,000 per person.",
            "Flat walking paths suitable for all mobility levels.",
            "Hwasoomok greenhouse and Samgeori cultural pavilions provide sheltered viewing."
        ),
        # Day 11: Nov 11
        make_day(10, "Cheonan", "Lakeside Boardwalks & Sunset Patios", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "10:00 AM start: Seongseong Lake Park Flat Eco-Boardwalk → Lakefront Cafe Rest",
            "Wooden Lake Boardwalks & Relaxed Sunset Patios",
            [
                {"time": "10:00–13:00", "title": "Seongseong Lake Park & Wooden Boardwalk", "detail": "Walk the wide, barrier-free wooden boardwalk loop around Seongseong Lake, visiting bird observation decks and golden reed beds (free admission).", "logistics": "Seobuk-gu Seongseong-dong; Bus 5 or 15-min taxi."},
                {"time": "13:15–14:45", "title": "Seongseong Lakefront Cafe Lunch", "detail": "Enjoy family-friendly brunch, pasta, or Korean rice sets overlooking the sparkling water.", "logistics": "Seongseong cafe road."},
                {"time": "15:15–17:30", "title": "Seongseong Waterfront Sunset Stroll", "detail": "Relax on outdoor lakefront wooden terraces as twilight colors reflect on the water.", "logistics": "Wooden boardwalk path."},
                {"time": "18:00–19:30", "title": "Shinbu-dong Specialty Dessert & Tea", "detail": "Sample Korean shaved ice (bingsu) with sweet red beans and roasted soybean powder.", "logistics": "Shinbu-dong."},
                {"time": "20:00–21:30", "title": "Cheonan Sliced Pork Suyuk & Rice Dinner", "detail": "Enjoy tender boiled pork belly slices with mild side dishes.", "logistics": "Station area dining room."}
            ],
            [
                {"label": "Flat Barrier-Free Promenade", "text": "Seongseong Lake's wooden boardwalk has zero stairs, making it ideal for relaxed strolling."},
                {"label": "Scenic Lakeside Pace", "text": "Unhurried afternoon spent enjoying water reflections and cozy cafes."}
            ],
            "Lunch: Seongseong lakefront cafe brunch (~₩14,000). Dinner: Cheonan tender boiled pork suyuk set (~₩20,000).",
            "Seongseong Lake Park is open 24/7; admission is free.",
            "Park is free; Lunch ~₩14,000; Dinner ~₩20,000 per person.",
            "Benches are stationed every 100 meters along the boardwalk for rest.",
            "Lakefront cafes offer spacious heated indoor seating."
        ),
        # Day 12: Nov 12
        make_day(11, "Cheonan", "Colossal Buddha & KTX Prep", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "10:00 AM start: Gakwonsa Grand Bronze Buddha → Anseo Lake Stroll → KTX to Busan Prep",
            "Colossal Bronze Statues, Lake Strolls & Rail Prep",
            [
                {"time": "10:00–12:30", "title": "Gakwonsa Temple & Grand Bronze Buddha", "detail": "View the colossal 15-meter seated Bronze Amita Buddha overlooking Taejosan Mountain (free admission; ramped vehicular access available).", "logistics": "Dongnam-gu Anseo-dong; Bus 24 or 15-min taxi."},
                {"time": "12:45–14:15", "title": "Anseo Lake Village Lunch", "detail": "Enjoy buckwheat cold noodles, potato pancakes, and wild herb bibimbap overlooking the temple pond.", "logistics": "Gakwonsa lake restaurant row."},
                {"time": "14:30–16:30", "title": "Arario Sculpture Park Open Plaza Walk", "detail": "Stroll central Cheonan's open sculpture plaza viewing works by Damien Hirst and Keith Haring.", "logistics": "Shinbu-dong Arario Plaza."},
                {"time": "17:00–18:30", "title": "Hotel Packing & KTX Ticket Check", "detail": "Pack primary luggage for Friday morning KTX to coastal Busan and verify seat assignments.", "logistics": "Hotel room."},
                {"time": "19:00–21:00", "title": "Cheonan Farewell Korean Feast", "detail": "Celebrate 5 nights in Cheonan with mild pork galbi barbecue.", "logistics": "Shinbu-dong dining lane."}
            ],
            [
                {"label": "Monumental Icon", "text": "Gakwonsa's 60-ton Bronze Buddha is an unforgettable and majestic sight."},
                {"label": "Pre-Busan Preparation", "text": "Packing early ensures a relaxed Friday morning high-speed train directly to Busan."}
            ],
            "Lunch: Anseo-dong buckwheat noodles and potato pancake. Dinner: Mild charcoal-grilled pork galbi with steamed rice.",
            "Gakwonsa Temple is free admission; open year-round.",
            "Temple is free; Lunch ~₩12,000; Dinner ~₩22,000 per person.",
            "Ramped access avoids stairs for viewing the Buddha statue.",
            "Daeungbojeon hall and temple tea rooms provide shelter."
        ),
        # Day 13: Nov 13
        make_day(12, "Busan", "Coastward Rail & Beach Arrival", "Busan · Haeundae Beachfront",
            "10:00 AM KTX to Busan (1h45m) → Haeundae Check-in → Sunset Beachfront Stroll",
            "Direct High-Speed Coastal Rail to the Southern Sea",
            [
                {"time": "10:00–11:45", "title": "KTX High-Speed Rail to Busan", "detail": "Smooth 1-hour 45-minute direct journey from Cheonan-Asan to Busan Station on the southern sea.", "logistics": "Direct Gyeongbu high-speed line."},
                {"time": "12:00–13:15", "title": "Busan Station Choryang Milmyeon Lunch", "detail": "Savor authentic cold wheat noodles and steamed dumplings.", "logistics": "Opposite Busan Station."},
                {"time": "13:45–15:00", "title": "Transfer to Haeundae Beach Base", "detail": "Check into Haeundae hotel (e.g. Felix by STX or L7 Haeundae).", "logistics": "Metro Line 2 or taxi across harbor bridge."},
                {"time": "15:30–18:00", "title": "Haeundae Beachfront Promenade Walk", "detail": "Stroll white sands of Haeundae Beach and follow the flat Dongbaek Island wooden boardwalk to APEC House.", "logistics": "Paved oceanside walkway."},
                {"time": "18:30–21:00", "title": "Haeundae Traditional Market Feast", "detail": "Sample fresh grilled seafood hot pot, fishcakes, and seed hotteok.", "logistics": "Haeundae Traditional Market."}
            ],
            [
                {"label": "Direct Rail Speed", "text": "Direct KTX arrives in Busan by noon, maximizing afternoon coastal leisure."},
                {"label": "Haeundae Comfort Base", "text": "Haeundae provides seven nights of flat beach access without moving hotels."}
            ],
            "Lunch: Choryang Milmyeon (cold wheat noodles & dumplings ~₩8,500). Dinner: Haeundae Market grilled seafood & ssiat hotteok (~₩18,000).",
            "Book KTX Cheonan-Asan→Busan on Korail app 30 days in advance.",
            "KTX ticket ~₩46,500; Beach and Dongbaek trail are free.",
            "Dongbaek Island trail is paved and lighted; Nurimaru APEC House closes at 17:00.",
            "SEA LIFE Busan Aquarium on Haeundae beachfront provides indoor shelter."
        ),
        # Day 14: Nov 14
        make_day(13, "Busan", "Private Ocean Pods & Saturday Drones", "Busan · Haeundae Beachfront",
            "10:00 AM start: Haeundae Blueline Sky Capsule → Cheongsapo Harbor → Saturday Drone Show",
            "Private Sky Capsules, Twin Lighthouses & Saturday Night Drones",
            [
                {"time": "10:00–12:00", "title": "Haeundae Blueline Park Sky Capsule (Mipo to Cheongsapo)", "detail": "Ride a private colorful Sky Capsule cabin suspended 10 meters above the sea along scenic coastal cliff tracks.", "logistics": "Mipo Station; book tickets 2 weeks in advance."},
                {"time": "12:00–13:30", "title": "Cheongsapo Seaside Grilled Seafood Lunch", "detail": "Dine on fresh scallops, shrimp, and clams grilled over briquettes with butter and cheese.", "logistics": "Cheongsapo harbor row."},
                {"time": "14:00–16:30", "title": "Cheongsapo Ocean Skywalk & Cafe Lounge", "detail": "Walk Daritdol Skywalk over breaking waves and sip coffee overlooking the twin lighthouses.", "logistics": "Cheongsapo waterfront."},
                {"time": "17:00–18:30", "title": "Gwangalli Beach Sunset Walk", "detail": "Watch sunset illuminate Gwangan Suspension Bridge.", "logistics": "Gwangan Station Line 2."},
                {"time": "19:00–21:30", "title": "Gwangalli Saturday Night 500-Drone Show & Chimaek", "detail": "Watch 500+ synchronized LED drones dance above Gwangan Bridge from the sand, enjoying Korean fried chicken.", "logistics": "Gwangalli Beach (drones at 19:00 & 21:00)."}
            ],
            [
                {"label": "Private Ocean Pod Comfort", "text": "Sky Capsules provide a private, comfortable, seated ocean experience without crowds."},
                {"label": "Saturday Night Drone Wonder", "text": "Timed specifically for Saturday evening to experience Gwangalli's free weekly drone spectacle."}
            ],
            "Lunch: Cheongsapo seaside grilled clams (jogae-gui) with butter and cheese. Dinner: Gwangalli beachfront Korean fried chicken and draft beer (~₩18,000).",
            "Book Blueline Sky Capsule 14 days in advance on official website.",
            "Sky Capsule 2-person cabin ₩35,000; Drone show free public viewing on the sand.",
            "Arrive at Gwangalli Beach 20 mins early for prime sand seating.",
            "Gwangalli beachfront cafes provide heated indoor viewing."
        ),
        # Day 15: Nov 15
        make_day(14, "Busan", "Cinema Mega-Structures & Spa Land", "Busan · Haeundae Beachfront",
            "10:00 AM start: Centum Cinema Center → Spa Land Thermal Saunas & Shinsegae",
            "Guinness Cantilever LED Roofs & Luxury Hydrotherapy Saunas",
            [
                {"time": "10:00–12:30", "title": "Busan Cinema Center (BIFF Venue)", "detail": "Marvel at the Guinness World Record cantilevered roof spanning 85 meters without support columns, covered with 42,600 dynamic LED ceiling lights.", "logistics": "Centum City Station Line 2 Exit 6 or 12."},
                {"time": "12:30–14:00", "title": "Shinsegae Centum Gourmet Hall Lunch", "detail": "Dine in the world's largest department store food emporium on gourmet bibimbap or handmade noodles.", "logistics": "Shinsegae B1."},
                {"time": "14:15–18:30", "title": "Spa Land Centum City Luxury Thermal Bathhouse", "detail": "Experience 18 natural mineral pools and 13 aesthetic themed saunas (Himalayan salt, Roman steam, Finnish sauna) with heated ergonomic loungers.", "logistics": "Direct Shinsegae Mall connection."},
                {"time": "19:00–21:30", "title": "Shinsegae Sky Lounge Modern Korean Dinner", "detail": "Enjoy contemporary Korean dining overlooking Suyeong River.", "logistics": "Shinsegae 9F dining room."}
            ],
            [
                {"label": "Guinness Record Architecture", "text": "The Busan Cinema Center is an international engineering marvel."},
                {"label": "Ultimate Urban Spa", "text": "Spa Land Centum City delivers the world's most luxurious urban jjimjilbang experience."}
            ],
            "Lunch: Shinsegae Centum City gourmet food hall. Dinner: Modern Korean seasonal tasting dinner at Shinsegae 9F.",
            "Spa Land 4-hour pass ~₩20,000–₩23,000 at entrance.",
            "Cinema Center exterior free; Spa Land ~₩23,000; Dinner ~₩32,000 per person.",
            "Spa Land does not admit children under 7; maintains serene adult relaxation atmosphere.",
            "This entire day is 100% enclosed, heated, and weatherproof."
        ),
        # Day 16: Nov 16
        make_day(15, "Busan", "Marine Aquariums & Pine Walks", "Busan · Haeundae Beachfront",
            "10:00 AM start: SEA LIFE Busan Aquarium → Dongbaekseok Island Flat Pine Loop",
            "Underwater Ocean Tunnels, Sea Otters & Pine Boardwalks",
            [
                {"time": "10:00–12:30", "title": "SEA LIFE Busan Aquarium (Haeundae Beach)", "detail": "Walk through 80-meter underwater ocean tunnels surrounded by sharks, sea turtles, stingrays, and playful penguins right on Haeundae beachfront.", "logistics": "Haeundae beachfront (direct walk from hotel)."},
                {"time": "12:45–14:15", "title": "Haeundae Beachfront Lunch", "detail": "Enjoy fresh abalone bibimbap or handmade burger overlooking the beach.", "logistics": "Gunam-ro dining lane."},
                {"time": "14:30–16:30", "title": "Dongbaek Island Pine Forest Flat Loop", "detail": "Walk the barrier-free paved wooden boardwalk around Dongbaek Island to APEC Nurimaru House.", "logistics": "Direct walk from Haeundae beach."},
                {"time": "17:00–18:30", "title": "The Bay 101 Marine City Sunset", "detail": "Photograph the gleaming glass skyscrapers reflecting in the harbor.", "logistics": "Dongbaek Station Exit 1."},
                {"time": "19:00–21:00", "title": "Haeundae Korean Fried Chicken & Draft Beer", "detail": "Crispy golden chicken on Haeundae avenue.", "logistics": "Haeundae Gunam-ro."}
            ],
            [
                {"label": "Beachfront Convenience", "text": "All activities are within flat walking distance of your Haeundae hotel base."},
                {"label": "Underwater Wonder", "text": "SEA LIFE Aquarium offers an engaging marine education experience directly on the sand."}
            ],
            "Lunch: Haeundae fresh abalone bibimbap. Dinner: Haeundae artisanal Korean fried chicken and draft beer.",
            "Book SEA LIFE Aquarium tickets online in advance for discounts (~₩25,000).",
            "Aquarium ~₩25,000; Dongbaek walk free; Dinner ~₩22,000 per person.",
            "Flat paved boardwalk suitable for all walking paces.",
            "SEA LIFE Aquarium is completely indoor and climate-controlled."
        ),
        # Day 17: Nov 17
        make_day(16, "Busan", "Flat Ocean Boardwalks & Cable Cars", "Busan · Haeundae Beachfront",
            "10:00 AM start: Songdo Cloud Trails Flat Skywalk → Songdo Marine Cable Car",
            "Over-Water Glass Boardwalks & Gentle Marine Gondolas",
            [
                {"time": "10:00–12:30", "title": "Songdo Cloud Trails Ocean Skywalk", "detail": "Walk the 365-meter flat, curved glass skywalk over breaking ocean waves, enjoying sea breezes without stairs.", "logistics": "Songdo Beach; bus or taxi from Haeundae."},
                {"time": "12:30–14:00", "title": "Songdo Beachfront Seafood Lunch", "detail": "Enjoy fresh grilled mackerel or abalone porridge overlooking the bay.", "logistics": "Songdo waterfront."},
                {"time": "14:15–16:30", "title": "Songdo Marine Cable Car (Air Cruise)", "detail": "Glide across the open sea in a comfortable cable car gondola between Songdo Beach and Amnam Park.", "logistics": "Songdo Bay Station."},
                {"time": "17:00–18:30", "title": "Haeundae Sunset Beach Walk", "detail": "Relax along the sandy shore as twilight falls.", "logistics": "Haeundae beachfront."},
                {"time": "19:00–21:00", "title": "Traditional Busan Dwaeji Gukbap Dinner", "detail": "Enjoy mild, rich pork bone soup with tender pork slices and rice.", "logistics": "Haeundae soup lane."}
            ],
            [
                {"label": "Flat Barrier-Free Skywalk", "text": "Songdo Cloud Trails is flat and easily accessible for strollers and gentle walking."},
                {"label": "Seated Aerial Perspective", "text": "Cable car offers panoramic sea views comfortably seated."}
            ],
            "Lunch: Songdo seaside abalone porridge or grilled fish. Dinner: Traditional Busan Dwaeji Gukbap (pork bone soup).",
            "Songdo Cable Car standard cabin ₩17,000 round-trip; Skywalk is free.",
            "Cable Car ₩17,000; Skywalk free; Lunch ~₩16,000; Dinner ~₩12,000 per person.",
            "Wheelchairs and strollers permitted inside cable car cabins.",
            "Cable car stations provide indoor heated cafes."
        ),
        # Day 18: Nov 18
        make_day(17, "Busan", "Arts Complex & Cinema Archives", "Busan · Haeundae Beachfront",
            "10:00 AM start: F1963 Cultural Complex & Terarosa Coffee → Korean Film Archive",
            "Converted Wire Factory Bookstores & Cinema Galleries",
            [
                {"time": "10:00–12:30", "title": "F1963 Cultural Arts Complex (Former Factory)", "detail": "Explore the visionary industrial architecture of a 1963 wire rope factory converted into an eco-arts complex, featuring Yes24 giant book store and bamboo gardens.", "logistics": "Mangmi Station Line 3 or 15-min taxi from Haeundae."},
                {"time": "12:30–14:00", "title": "Terarosa Specialty Coffee & Bakery Lunch", "detail": "Enjoy pour-over specialty coffee and artisan sourdough in the dramatic factory interior.", "logistics": "Inside F1963."},
                {"time": "14:30–16:30", "title": "Korean Film Archive Busan Exhibition", "detail": "Browse historic cinema posters, director scripts, and vintage film cameras inside the Busan Cinema Center.", "logistics": "Busan Cinema Center 2F."},
                {"time": "17:00–18:30", "title": "Millak Waterfront Park Gentle Stroll", "detail": "Stroll the flat seaside promenade overlooking Gwangan Bridge.", "logistics": "Millak waterfront."},
                {"time": "19:00–21:00", "title": "Millak Raw Fish Feast / Modern Korean Dinner", "detail": "Enjoy fresh seasonal sliced fish or grilled beef.", "logistics": "Millak Raw Fish Town."}
            ],
            [
                {"label": "Adaptive Reuse", "text": "F1963 is a masterclass in post-industrial architectural revitalization."},
                {"label": "Cinema Heritage", "text": "Film Archive exhibits bring Korean cinema history to life."}
            ],
            "Lunch: Terarosa F1963 artisan sourdough sandwich and coffee. Dinner: Millak fresh flounder sashimi and maeuntang fish stew.",
            "F1963 exhibitions and bookstore are free admission; open daily 10:00–20:00.",
            "F1963 free; Film Archive free; Dinner ~₩30,000 per person.",
            "Yes24 bookstore inside F1963 has extensive children's and English book sections.",
            "F1963 is completely indoor and weatherproof."
        ),
        # Day 19: Nov 19
        make_day(18, "Busan", "Low-Stakes Ocean Tea Terrace (CSAT Day)", "Busan · Haeundae Beachfront",
            "10:00 AM start: Haeundae Beach Stroll → Dalmaji Sea-View Teahouse (CSAT Day)",
            "Mindful Ocean Waves, Herbal Tea & Gentle Pace (CSAT / Suneung Day)",
            [
                {"time": "10:30–12:30", "title": "Haeundae Beach Gentle Sand Walk", "detail": "Unhurried walk along Haeundae beach boardwalk watching waves roll in.", "logistics": "Direct walk from hotel."},
                {"time": "12:45–14:15", "title": "Haeundae Gourmet Cafe Lunch", "detail": "Enjoy fresh seasonal seafood bibimbap or artisan sandwiches.", "logistics": "Haeundae beachfront."},
                {"time": "14:30–17:00", "title": "Dalmaji Hill Panoramic Sea-View Tea Terrace", "detail": "Sip artisanal herbal teas while gazing out over the sparkling Korea Strait, reflecting on 7 restful Busan nights.", "logistics": "Dalmaji-gil teahouse."},
                {"time": "17:30–19:00", "title": "Sunset Beach Contemplation", "detail": "Watch the golden sun dip below the coastal horizon from Haeundae sands.", "logistics": "Haeundae beachfront."},
                {"time": "19:30–21:30", "title": "Busan Farewell Feast: Hanwoo Beef Barbecue", "detail": "Celebrate final night in Busan with premium charcoal-grilled Korean Hanwoo beef tenderloin.", "logistics": "Haeundae Somunnan Amso Galbi."}
            ],
            [
                {"label": "CSAT Low-Stakes Alignment", "text": "Nov 19 national CSAT exam day is kept 100% localized on Haeundae beachfront to avoid city transit hold zones."},
                {"label": "Mindful Coastal Completion", "text": "Leaves the traveler deeply rested and physically restored for Friday's return to Seoul."}
            ],
            "Lunch: Haeundae fresh abalone soup and vegetable bibimbap. Afternoon: Artisanal Korean herbal tea. Dinner: Haeundae Hanwoo beef short ribs with potato noodles.",
            "Haeundae Somunnan Amso Galbi: arrive by 17:30 to avoid queues.",
            "Lunch ~₩18,000; Farewell Hanwoo dinner ~₩48,000 per person.",
            "Keep evening calm; pack primary bags for Friday morning KTX to Seoul.",
            "Haeundae beachfront indoor cafes offer heated panoramic sea views."
        ),
        # Day 20: Nov 20
        make_day(19, "Seoul", "Capital Return & Covered Shopping", "Seoul · Seoul Station / Myeongdong",
            "10:00 AM KTX Busan to Seoul (2h15m) → Seoul Station Check-in → Lotte Mart Covered Shopping",
            "Comfortable High-Speed Rail & Doorstep Covered Shopping",
            [
                {"time": "09:45–10:15", "title": "Busan Station Departure", "detail": "Check out of Haeundae hotel, take taxi or metro to Busan Station, and board direct KTX.", "logistics": "Board train 10 minutes prior to departure."},
                {"time": "10:30–12:45", "title": "KTX High-Speed Rail to Seoul", "detail": "Comfortable 2-hour 15-minute smooth journey back to Seoul Station.", "logistics": "Direct arrival inside Seoul Station concourse."},
                {"time": "13:00–14:30", "title": "Seoul Station Hotel Check-in & Lunch", "detail": "Check into hotel directly at Seoul Station and drop bags.", "logistics": "Direct hotel connection."},
                {"time": "15:00–18:00", "title": "Seoul Station Lotte Mart Mega-Store Curation", "detail": "Browse covered food and souvenir aisles for premium seaweed, Korean snack boxes, tea sets, and condiments with instant tax refund.", "logistics": "Lotte Mart 2F immediate tax refund counter."},
                {"time": "18:30–21:00", "title": "Seoul Station Korean Beef Stew Dinner", "detail": "Enjoy mild beef bulgogi or hot pot near hotel doorstep.", "logistics": "Seoul Station dining lane."}
            ],
            [
                {"label": "Strategic Departure Buffer", "text": "Arriving in Seoul on Friday eliminates all risk of KTX weekend disruption before Sunday flight."},
                {"label": "Doorstep Convenience", "text": "Seoul Station hotel base eliminates luggage transfers on Friday and Sunday."}
            ],
            "Lunch: Seoul Station concourse dining. Dinner: Sizzling Hanwoo beef bulgogi with mild side dishes.",
            "Book KTX Busan→Seoul on Korail app 30 days in advance.",
            "KTX ticket ~₩59,800 per person.",
            "Friday afternoon KTX trains fill up quickly; secure reserved seats early.",
            "Lotte Mart and Seoul Station concourse are completely enclosed."
        ),
        # Day 21: Nov 21
        make_day(20, "Seoul", "Royal Greenhouses & Grand Farewell", "Seoul · Seoul Station / Myeongdong",
            "10:00 AM start: Changgyeonggung Palace Grand Greenhouse → Calm Packing → Grand Farewell Banquet",
            "Historic Royal Greenhouses, Calm Packing & Celebration Feast",
            [
                {"time": "10:00–12:30", "title": "Changgyeonggung Palace & Grand Greenhouse Walk", "detail": "Stroll flat, peaceful autumn palace gardens and visit Korea's first Western-style royal greenhouse built in 1909 (free palace admission for seniors).", "logistics": "Hyehwa Station Line 4 Exit 4."},
                {"time": "12:45–14:15", "title": "Daehak-ro Gourmet Lunch", "detail": "Enjoy handmade dumplings or mild bibimbap.", "logistics": "Daehak-ro dining lane."},
                {"time": "14:45–17:30", "title": "Afternoon Hotel Rest & Luggage Packing", "detail": "Return to hotel room, organize souvenirs, check luggage weight with front desk scale, and complete online flight check-in.", "logistics": "Hotel room."},
                {"time": "18:30–21:00", "title": "Grand Farewell Korean BBQ Feast", "detail": "Celebrate the 21-night journey with premium Korean Hanwoo beef barbecue and aged kimchi stew in central Seoul.", "logistics": "Myeongdong / Gwanghwamun dining room."}
            ],
            [
                {"label": "Botanical Heritage Sanctuary", "text": "Changgyeonggung Greenhouse provides a heated, tranquil botanical stroll under vintage white steel arches."},
                {"label": "Zero Departure Stress", "text": "All shopping and packing completed by Saturday night ensures Sunday morning is 100% serene."}
            ],
            "Lunch: Daehak-ro handmade dumpling soup and bibimbap. Dinner: Premium Hanwoo charcoal BBQ banquet (~₩45,000).",
            "Complete online airline check-in 24 hours prior; select seats and enter passport numbers.",
            "Palace entry ₩1,000; Farewell dinner ~₩45,000 per person.",
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
                {"time": "12:30–13:00", "title": "Boarding & Takeoff", "detail": "Board aircraft for the return flight home with unforgettable memories of relaxed, joyful travel across Korea.", "logistics": "Gates close 15 minutes before scheduled departure."}
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
        {"label": "Relaxed 10 AM Starts", "value": "5/5", "tone": "good"},
        {"label": "Family Accessibility", "value": "5/5", "tone": "good"},
        {"label": "Aquariums & Parks", "value": "5/5", "tone": "good"},
        {"label": "Short Rail Transfers", "value": "5/5", "tone": "good"}
    ]

    return {
        "id": "seoul-cheonan-busan-leisure",
        "shortTitle": "Seoul · Cheonan · Busan (Gentle Leisure & Family Comfort)",
        "title": "Family Comfort, Gentle Parks & Relaxed Leisure (Gentle Leisure & Family Comfort)",
        "routeLabel": "Seoul (7N) → Cheonan (5N) → Busan (7N) → Seoul (2N)",
        "badge": "Relaxed Pacing & Family Leisure",
        "bestFor": "Families with children, senior travelers, multi-generational groups, and travelers who prefer relaxed 10:00 AM starts, unhurried pacing, flat accessible walking paths, world-class aquariums, and heated mineral water parks.",
        "decisionSummary": "A thoughtfully paced, low-stress 21-night itinerary designed around 10:00 AM daily starts, barrier-free attractions, and spacious leisure destinations: Lotte World Tower & Aquarium, Children's Grand Park, Sono Belle indoor thermal water park, Hong Dae-yong science planetarium, Haeundae Sky Capsules, and Centum Cinema Center.",
        "recommendation": "Choose this route if you want to experience Korea's beauty without early morning alarms, frantic schedules, or strenuous mountain climbing.",
        "tradeoff": "Gentler pacing means fewer total attractions visited per day in exchange for deep comfort and rest.",
        "scorecard": scorecard,
        "bases": get_scb_common_bases(),
        "transfers": get_scb_common_transfers(),
        "budgetScenarios": get_scb_budget_scenarios(),
        "bookingPriorities": get_scb_booking_priorities(),
        "days": days
    }
