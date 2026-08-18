#!/usr/bin/env python3
"""Route Blueprint: Seoul · Cheonan · Busan (Artisan Gastronomy, Regional Craft & Market Feasts)."""

from scripts.generate_all_itineraries import make_day
from scripts.itinerary_builder_scb import (
    get_scb_common_bases,
    get_scb_common_transfers,
    get_scb_budget_scenarios,
    get_scb_booking_priorities
)

def get_scb_gourmet():
    days = [
        # Day 1: Nov 1
        make_day(0, "Seoul", "Arrival", "Seoul · Myeongdong / Seoul Station edge",
            "ICN arrival at 21:00 → late transfer → gentle craft tea & light snack → restorative sleep",
            "Epicurean Landing & Calming Welcome Reset",
            [
                {"time": "21:00–22:15", "title": "ICN Arrival & Border Clearance", "detail": "Clear immigration smoothly, collect checked luggage, and pick up pre-arranged transportation cards.", "logistics": "Terminal 1 or 2."},
                {"time": "22:30–23:45", "title": "Direct Transfer to Central Seoul Base", "detail": "Airport Limousine Bus or official taxi directly to Myeongdong / Seoul Station hotel.", "logistics": "Direct drop-off eliminates luggage friction."},
                {"time": "23:45–00:30", "title": "Craft Barley Tea & Rest", "detail": "Hydrate with warm roasted grain tea, unpack essentials, and rest deeply before the culinary journey begins.", "logistics": "Late morning wakeup planned tomorrow."}
            ],
            [
                {"label": "Palate Preparation", "text": "Starting gently with roasted herbal tea protects the digestive system after international flights."},
                {"label": "Station Proximity", "text": "Seoul Station base provides immediate access to historic dining alleys and high-speed rail."}
            ],
            "Light roasted barley tea and warm rice snack.",
            "Confirm late check-in with hotel in writing.",
            "Limousine Bus ~₩17,000.",
            "Save full appetite for tomorrow's Michelin temple cuisine banquet.",
            "Hotel front desk provides 24-hour service."
        ),
        # Day 2: Nov 2
        make_day(1, "Seoul", "Michelin Temple Cuisine & Artisan Teahouses", "Seoul · Myeongdong / Seoul Station edge",
            "Balwoo Gongyang (Michelin Temple Cuisine) → Insadong Traditional Teahouses & Fermented Confectionery",
            "Michelin Buddhist Temple Dining & Centuries-Old Tea Lineages",
            [
                {"time": "10:30–12:00", "title": "Jogyesa Zen Buddhist Temple Stroll", "detail": "Walk among centuries-old locust trees and golden autumn chrysanthemum flower displays at the headquarters of Korean Zen Buddhism.", "logistics": "Anguk Station Line 3 Exit 6 or Jonggak Station Line 1 Exit 2."},
                {"time": "12:00–14:00", "title": "Balwoo Gongyang (Michelin-Starred Temple Cuisine)", "detail": "Experience Korea's definitive temple cuisine banquet, crafted without garlic, onions, or artificial seasonings, using 10-year aged soy sauces, fermented mountain mushrooms, and lotus root.", "logistics": "Directly opposite Jogyesa Temple (Temple Stay Information Center 5F)."},
                {"time": "14:30–17:00", "title": "Insadong Artisanal Teahouse & Confectionery", "detail": "Sip deep roasted Ssanggwa-cha (medicinal herbal tea with egg yolk) or sweet Omija tea paired with handmade yakgwa (honey pastry) in a 100-year-old wooden hanok teahouse.", "logistics": "Insadong Ssamzigil lane."},
                {"time": "17:30–19:30", "title": "Bukchon Hanok Promenade", "detail": "Stroll traditional stone alleys under autumn twilight.", "logistics": "Anguk Station Line 3."},
                {"time": "20:00–21:30", "title": "Myeongdong Kyoja Michelin Bib Gourmand Dinner", "detail": "Savor handmade kalguksu noodles in rich chicken broth and steamed pork mandu dumplings with pungent garlic kimchi.", "logistics": "Myeongdong 2-ga."}
            ],
            [
                {"label": "Philosophical Gastronomy", "text": "Balwoo Gongyang illustrates how Korean temple food elevates mindfulness and natural fermentation into haute cuisine."},
                {"label": "Artisan Tea Heritage", "text": "Insadong preserves Korea's ancient tea ceremony aesthetics and medicinal herbal decoctions."}
            ],
            "Lunch: Balwoo Gongyang Michelin Temple Course (fermented seasonal roots and temple broths). Afternoon: Traditional omija tea & yakgwa. Dinner: Myeongdong Kyoja kalguksu and steamed mandu.",
            "Reserve Balwoo Gongyang 30 days in advance online (essential for lunch tasting menu).",
            "Balwoo Gongyang course ~₩45,000–₩65,000; Dinner ~₩11,000 per person.",
            "Temple cuisine avoids the 5 pungent alliums (garlic, onion, chives, leeks, scallions) to promote clarity.",
            "Balwoo Gongyang and Insadong hanok teahouses are fully indoor."
        ),
        # Day 3: Nov 3
        make_day(2, "Seoul", "1++ Hanwoo Beef & Scented Coffee", "Seoul · Myeongdong / Seoul Station edge",
            "Majang Meat Wholesale Market 1++ Hanwoo Beef Tasting → Seongsu Artisan Coffee Roasteries",
            "Korea's Crown Jewel Beef & Master Specialty Roasters",
            [
                {"time": "10:30–13:30", "title": "Majang Meat Wholesale Market & Hanwoo Barbecue", "detail": "Select prime 1++ Korean Hanwoo beef ribeye, sirloin, and tenderloin directly from master butchers, grilling it over charcoal at a 2nd-floor specialty dining hall.", "logistics": "Majang Station Line 5 Exit 2 or Yongdu Station Line 2."},
                {"time": "14:00–16:30", "title": "Seongsu Specialty Coffee Roasters (Center Coffee, Daelim Warehouse)", "detail": "Sample single-origin pour-over brews, Geisha varietals, and artisan butter salt bread in converted industrial loft bakeries.", "logistics": "Seongsu Station Line 2 Exit 3."},
                {"time": "17:00–19:00", "title": "Seoul Forest Autumn Ginkgo Canopy Stroll", "detail": "Walk under golden ginkgo trees to refresh between rich feasts.", "logistics": "Seoul Forest Station Exit 4."},
                {"time": "19:30–21:30", "title": "Seongsu Modern Craft Makgeolli Pub", "detail": "Pair artisanal cloudy rice wine with crispy truffle potato pancakes and braised pork belly.", "logistics": "Yeonmujang-gil dining lane."}
            ],
            [
                {"label": "Peak Marbling Quality", "text": "1++ Hanwoo is Korea's indigenous beef marbling pinnacle, delivering intense umami and melt-in-mouth tenderness."},
                {"label": "Specialty Coffee Capital", "text": "Seongsu is East Asia's premier laboratory for third-wave specialty coffee roasting."}
            ],
            "Lunch: Majang Market 1++ Hanwoo beef charcoal grill with doenjang jjigae. Afternoon: Seongsu artisanal pour-over coffee & canelé. Dinner: Seongsu craft makgeolli & crispy gamjajeon potato pancake.",
            "Purchase meat cuts on 1F butcher stalls; pay table setting fee (₩6,000) at 2F grill room.",
            "Hanwoo lunch ~₩60,000–₩85,000 per person; exceptional direct wholesale value.",
            "Pair rich Hanwoo beef with fresh wasabi, ssam leafy greens, and sea salt.",
            "Majang indoor grill halls and Seongsu cafes are warm and sheltered."
        ),
        # Day 4: Nov 4
        make_day(3, "Seoul", "Historic Pyongyang Noodles & Markets", "Seoul · Myeongdong / Seoul Station edge",
            "Jongno Wooraeok (Historic 1946 Pyongyang Naengmyeon) → Gwangjang Traditional Food Market",
            "70-Year Cold Noodle Lineages & Midnight Market Griddles",
            [
                {"time": "11:00–13:00", "title": "Wooraeok (Since 1946 Heritage Pyongyang Naengmyeon)", "detail": "Savor Korea's definitive cold buckwheat noodles in 100% pure chilled Hanwoo beef broth, paired with traditional charcoal-grilled bulgogi.", "logistics": "Euljiro 4-ga Station Line 2/5 Exit 4 (arrive by 11:00 AM)."},
                {"time": "13:30–16:00", "title": "Cheonggyecheon Stream & Insadong Craft Alleys", "detail": "Walk the sunken urban stream to explore artisan ceramics and tea ware in Insadong.", "logistics": "Cheonggyecheon pedestrian path."},
                {"time": "16:30–18:30", "title": "Ikseon-dong Hanok Dessert Crawl", "detail": "Sample steamed egg toast, soufflé pancakes, and black sesame gelato in restored hanok courtyards.", "logistics": "Jongno 3-ga Station Exit 4."},
                {"time": "19:00–21:30", "title": "Gwangjang Traditional Market Grand Feast", "detail": "Feast on crispy bindaetteok (mung bean pancake fried in oil), mayak gimbap with mustard dip, fresh yukhoe (beef tartare with pear and raw egg yolk), and draft makgeolli.", "logistics": "Jongno 5-ga Station Line 1 Exit 8."}
            ],
            [
                {"label": "70-Year Cold Noodle Benchmark", "text": "Wooraeok is universally regarded as the gold standard of authentic North Korean Pyongyang-style beef cold noodles."},
                {"label": "Living Market Culture", "text": "Gwangjang Market offers the most vibrant street food theater in South Korea."}
            ],
            "Lunch: Wooraeok Pyongyang naengmyeon & Hanwoo beef bulgogi. Afternoon: Hanok cafe dessert. Dinner: Gwangjang Market bindaetteok, mayak gimbap, yukhoe, and draft makgeolli.",
            "Wooraeok does not accept reservations; register on tablet waitlist at 11:00 AM.",
            "Wooraeok lunch ~₩30,000; Gwangjang market dinner ~₩20,000 per person.",
            "Pyongyang naengmyeon broth has a subtle, clean beef flavor; taste broth before adding vinegar or mustard.",
            "Wooraeok and Gwangjang covered market roof provide complete weather protection."
        ),
        # Day 5: Nov 5
        make_day(4, "Seoul", "Charcoal Pork Ribs & Savory Pancakes", "Seoul · Myeongdong / Seoul Station edge",
            "Mapo Charcoal Pork Galbi BBQ → Gongdeok Jeon (Pancake) Alley → Mangwon Market",
            "Hardwood Charcoal Ribs & Assorted Savory Pancakes",
            [
                {"time": "10:30–13:00", "title": "Mangwon Traditional Neighborhood Market", "detail": "Sample sweet & spicy boneless fried chicken (dakgangjeong), handmade croquettes, and hotteok.", "logistics": "Mangwon Station Line 6 Exit 2."},
                {"time": "13:30–15:30", "title": "Gongdeok Jeon (Pancake) & Jokbal Alley", "detail": "Fill wicker trays with assorted savory pancakes (jeon, stuffed peppers, shrimp, fish, meat patties) fried fresh on massive flat-top griddles.", "logistics": "Gongdeok Station Line 5/6/AREX Exit 4."},
                {"time": "16:00–18:00", "title": "Gyeongui Line Forest Park Digestive Stroll", "detail": "Walk the transformed leafy railway corridor.", "logistics": "Gongdeok to Yeonnam."},
                {"time": "18:30–21:00", "title": "Mapo Charcoal Pork Galbi Feast", "detail": "Feast on succulent pork ribs marinated in sweet soy and garlic, grilled over glowing hardwood charcoal with steaming egg custard and cold dongchimi broth.", "logistics": "Mapo Station Line 5 BBQ Alley."}
            ],
            [
                {"label": "Historic BBQ Birthplace", "text": "Mapo is the historic birthplace of Seoul's charcoal galbi restaurant culture."},
                {"label": "Self-Curated Jeon Trays", "text": "Gongdeok Jeon alley allows guests to pick custom combinations of savory traditional pancakes."}
            ],
            "Lunch: Gongdeok assorted savory pancakes (jeon) with onion soy dipping sauce. Afternoon: Mangwon dakgangjeong snack. Dinner: Mapo charcoal-grilled pork galbi with cold dongchimi noodles.",
            "Gongdeok Jeon alley charges by weight; pay at counter before tableside heating.",
            "Daily food budget ~₩45,000 per person.",
            "Mapo BBQ restaurants provide plastic bags for coats to protect from charcoal smoke.",
            "All dining venues are fully enclosed and weatherproof."
        ),
        # Day 6: Nov 6
        make_day(5, "Seoul", "Live Seafood Auctions & Raw Crabs", "Seoul · Myeongdong / Seoul Station edge",
            "Noryangjin Fish Wholesale Market (Live King Crab & Sashimi) → Han River Sunset Stroll",
            "Live Giant King Crabs, Yellowtail Sashimi & Fish Stew Cauldrons",
            [
                {"time": "10:00–13:30", "title": "Noryangjin Wholesale Fisheries Market Feast", "detail": "Select live King Crab, Snow Crab, or fresh seasonal yellowtail (bangeo) sashimi from 1F stalls and have it steamed and prepared immediately on 2F with crab-roe fried rice and spicy fish stew (maeuntang).", "logistics": "Noryangjin Station Line 1/9 direct footbridge connection."},
                {"time": "14:00–16:30", "title": "Yeouido The Hyundai Gourmet Supermarket", "detail": "Browse the sprawling Tasty Seoul basement food hall, discovering boutique confectioneries, matcha lattes, and artisan snacks.", "logistics": "Yeouido Station Line 5/9 direct underground walkway."},
                {"time": "17:00–19:00", "title": "Yeouido Hangang Park Sunset Walk", "detail": "Relax along the Han River waterfront as twilight illuminates the bridges.", "logistics": "Yeouinaru Station Line 5 Exit 2."},
                {"time": "19:30–21:30", "title": "Sindang-dong Tteokbokki Town Feasting", "detail": "Experience the historic 1953 birthplace of tabletop tteokbokki, boiling rice cakes, fish cakes, ramen, and fried dumplings in sweet chili black-bean broth.", "logistics": "Sindang Station Line 2/6 Exit 8."}
            ],
            [
                {"label": "Wholesale Marine Freshness", "text": "Noryangjin connects ocean catch directly to your table within minutes of selection."},
                {"label": "Street Comfort Contrast", "text": "Transitions from luxury marine seafood to nostalgic comfort food in Sindang-dong."}
            ],
            "Lunch: Noryangjin steamed giant king crab, butter-grilled abalone, crab-roe fried rice, and spicy maeuntang. Dinner: Sindang-dong bubbling tabletop tteokbokki hot pot with cheese.",
            "Noryangjin 2F restaurants charge cooking fees (₩5,000–₩10,000 per kg) for steaming crab.",
            "Noryangjin lunch ~₩55,000–₩75,000 per person; Dinner ~₩12,000 per person.",
            "Wear closed-toe shoes on fish market floors.",
            "Noryangjin modern building and The Hyundai Seoul are completely enclosed and climate-controlled."
        ),
        # Day 7: Nov 7
        make_day(6, "Seoul", "Royal Soups & KTX Prep", "Seoul · Myeongdong / Seoul Station edge",
            "Hadongkwan 80-Year Gomtang Beef Soup → Samcheongdong Sujebi → Sunday KTX to Cheonan Prep",
            "Slow-Simmered Beef Broths, Hand-Torn Noodles & Rail Preparation",
            [
                {"time": "09:30–11:30", "title": "Hadongkwan Traditional Beef Gomtang (Since 1939)", "detail": "Taste Seoul's definitive slow-simmered beef brisket soup, served with tender tripe, spring onions, and aged radish kkakdugi.", "logistics": "Myeongdong 1-ga; open from early morning."},
                {"time": "12:00–14:30", "title": "Samcheong-dong Sujebi & Bukchon Walk", "detail": "Enjoy hand-torn dough pasta cooked in rich anchovy broth with tender clams in an earthenware pot.", "logistics": "Samcheong-dong main road."},
                {"time": "15:00–17:30", "title": "Seoul Station Lotte Mart Food Reconnaissance", "detail": "Preview Korean food gifts and pick up snacks for tomorrow's KTX train to Cheonan.", "logistics": "Seoul Station 2F."},
                {"time": "18:00–19:30", "title": "Luggage Packing & KTX Ticket Check", "detail": "Pack primary luggage for Sunday morning KTX to Cheonan-Asan (only 35 mins!).", "logistics": "Seoul Station hotel."},
                {"time": "20:00–21:30", "title": "Chuncheon Spicy Dakgalbi Feast", "detail": "Savor spicy gochujang-marinated chicken, sweet potatoes, and chewy rice cakes cooked on a tabletop cast iron skillet with mozzarella cheese.", "logistics": "Myeongdong dining lane."}
            ],
            [
                {"label": "Heritage Simmered Broths", "text": "Hadongkwan and Samcheongdong Sujebi showcase Korea's mastery of comforting bone and anchovy broths."},
                {"label": "Rail Preparation", "text": "Packing early ensures an effortless Sunday morning 35-minute rail leap to Cheonan."}
            ],
            "Breakfast/Brunch: Hadongkwan traditional Hanwoo gomtang soup. Lunch: Samcheong-dong handmade sujebi and gamjajeon. Dinner: Chuncheon spicy dakgalbi with mozzarella cheese and bokkeumbap.",
            "Hadongkwan closes early when broth runs out (typically around 15:30); go for morning brunch.",
            "Daily food budget ~₩40,000 per person.",
            "Dakgalbi sauce can splatter; wear the provided restaurant aprons.",
            "All dining venues are fully enclosed indoors."
        ),
        # Day 8: Nov 8
        make_day(7, "Cheonan", "City Transition & Heritage Walnut Pastries", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Morning KTX to Cheonan-Asan (35 mins) → 1934 Original Hakhwa Hodu-gwaja Bakery → Namsan Market Noodles",
            "Lightning 35-Min Rail Leap, 90-Year Walnut Pastry Lineages & Market Feasts",
            [
                {"time": "09:45–10:20", "title": "KTX High-Speed Rail Seoul to Cheonan-Asan", "detail": "Lightning 35-minute smooth high-speed transit from Seoul Station to Cheonan-Asan Station.", "logistics": "Direct Gyeongbu line."},
                {"time": "10:30–12:00", "title": "Hotel Check-in & Base Setup", "detail": "Check into hotel (e.g. Shilla Stay Cheonan or Ramada Encore Cheonan-Asan) and drop bags.", "logistics": "Station area / Shinbu-dong."},
                {"time": "12:30–14:30", "title": "1934 Original Hakhwa Halmi Hodu-gwaja (Main Flagship)", "detail": "Visit Korea's oldest walnut pastry bakery, founded in 1934 by Grandmother Sim Bok-sun, to taste steaming hot walnut cakes filled with whole crunchy walnuts and signature white bean paste (Baekang) and red bean paste.", "logistics": "Cheonan Station / Shinbu-dong branch."},
                {"time": "15:00–17:30", "title": "Cheonan Namsan Central Market Food Crawl", "detail": "Browse Cheonan's oldest covered market for knife-cut noodles (kalguksu), giant handmade pork dumplings, and vegetable japchae hotteok.", "logistics": "Sajik-dong (walk from Cheonan Station)."},
                {"time": "18:30–21:00", "title": "Cheonan Sizzling Beef Bulgogi & Suyuk Dinner", "detail": "Feast on tender seasoned beef bulgogi with fresh seasonal banchan side dishes.", "logistics": "Central Cheonan restaurant quarter."}
            ],
            [
                {"label": "90-Year Culinary Lineage", "text": "Hakhwa Hodu-gwaja has baked Korea's most iconic train snack continuously since 1934."},
                {"label": "Authentic Market Value", "text": "Namsan Central Market serves authentic knife-cut noodles at unbeatable traditional pricing."}
            ],
            "Lunch: 1934 Hakhwa freshly baked warm walnut pastries & tea. Afternoon: Namsan Market handmade dumplings & kalguksu. Dinner: Cheonan charcoal-grilled Hanwoo beef bulgogi.",
            "Book KTX Seoul→Cheonan-Asan on Korail app 30 days in advance.",
            "KTX ticket ~₩14,100; Hodu-gwaja box ~₩6,000; Market snacks ~₩8,000.",
            "Taste both the white bean paste (Baekang) and red bean paste variants of Hakhwa Hodu-gwaja for comparison.",
            "Hakhwa bakery and Namsan Central Market are fully enclosed and weatherproof."
        ),
        # Day 9: Nov 9
        make_day(8, "Cheonan", "Heritage Blood Sausage Alley & Independence", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Byeongcheon Soondae Alley (50-Year Lineage) → Aunae Traditional Market → Independence Hall Autumn Walk",
            "Korea's Famous Blood Sausage Capital & Radiant Autumn Foliage",
            [
                {"time": "09:30–12:30", "title": "Independence Hall of Korea & Autumn Maple Walk", "detail": "Tour the colossal Grand Hall of the Nation and stroll the 3.2km Maple Tree Tunnel under golden autumn foliage.", "logistics": "Dongnam-gu Mokcheon-eup; City Bus 381/382/383 or 20-min taxi."},
                {"time": "12:45–14:30", "title": "Byeongcheon Soondae Alley Feast (50-Year Tradition)", "detail": "Feast on authentic Byeongcheon Soondae Gukbap: tender small intestine stuffed with cellophane noodles, fresh cabbage, leeks, and pork blood simmered in rich bone broth, served with steaming sliced soondae and pork cuts.", "logistics": "Byeongcheon Soondae Street (over 20 heritage restaurants)."},
                {"time": "14:45–16:30", "title": "Aunae Traditional Marketplace Walk", "detail": "Stroll the historic marketplace, sampling traditional honey candy, puffed rice grains, and dried jujubes.", "logistics": "Byeongcheon marketplace."},
                {"time": "17:00–18:30", "title": "Return to Cheonan & Rest", "detail": "Relax at hotel or explore local cafes in Shinbu-dong.", "logistics": "Short taxi or bus return."},
                {"time": "19:00–21:00", "title": "Cheonan Charcoal Pork BBQ Dinner", "detail": "Feast on thick pork neck and steaming kimchi stew.", "logistics": "Shinbu-dong dining lane."}
            ],
            [
                {"label": "National Soondae Benchmark", "text": "Byeongcheon Soondae is nationally distinct for its heavy vegetable content and delicate, non-greasy flavor."},
                {"label": "Historic Market Soul", "text": "Aunae Market preserves the historic spirit of Korea's 1919 independence movement."}
            ],
            "Lunch: Famous Byeongcheon Soondae Gukbap (authentic pork blood sausage soup with assorted meats). Dinner: Shinbu-dong charcoal-grilled pork barbecue with soybean paste stew.",
            "Independence Hall of Korea is free admission; closed on Mondays (outdoor grounds remain open).",
            "Soondae lunch ~₩10,000; Dinner ~₩25,000 per person.",
            "Season soondae soup with salted shrimp (saeujeot) and red pepper paste (dadeagi) at your table.",
            "Byeongcheon restaurants and Independence Hall galleries are fully indoor."
        ),
        # Day 10: Nov 10
        make_day(9, "Cheonan", "Artisanal Pear Wine & Regional Makgeolli", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Cheonan Seonghwan Pear Wine & Makgeolli Brewery Tasting → Cheonan Samgeori Park",
            "Artisanal Fruit Wines, Living Fermentation & Royal Crossroad Pavilions",
            [
                {"time": "10:00–12:30", "title": "Cheonan Artisanal Brewery & Seonghwan Pear Wine Tasting", "detail": "Visit a local brewery crafting traditional Korean rice wine (makgeolli) and fruit wines made with famous sweet Cheonan Seonghwan pears.", "logistics": "Seobuk-gu Seonghwan-eup; short taxi or local bus."},
                {"time": "12:45–14:15", "title": "Seonghwan Traditional Market Lunch", "detail": "Enjoy regional sundae soup, potato pancakes, and fresh pear salad.", "logistics": "Seonghwan market dining row."},
                {"time": "14:45–17:00", "title": "Cheonan Samgeori Park Heritage Walk", "detail": "Walk around the scenic willow-lined lake and traditional pavilions where the historic Gyeongbu and Honam royal highways intersected.", "logistics": "Dongnam-gu Samnyong-dong."},
                {"time": "17:30–19:00", "title": "Shinbu Cultural Street Stroll", "detail": "Explore youth fashion shops and specialty coffee lounges.", "logistics": "Shinbu-dong."},
                {"time": "19:30–21:30", "title": "Cheonan Hanwoo Beef Barbecue Feast", "detail": "Savor premium charcoal-grilled Korean Hanwoo beef tenderloin with aged soybean stew.", "logistics": "Central Cheonan dining room."}
            ],
            [
                {"label": "Regional Fruit Wine Craft", "text": "Cheonan is famous throughout Korea for sweet Seonghwan pears, fermented into delicate artisan wines."},
                {"label": "Living Fermentation Heritage", "text": "Local makgeolli breweries preserve natural yeast and nuruk traditions."}
            ],
            "Lunch: Seonghwan regional potato pancakes and makgeolli. Dinner: Cheonan charcoal-grilled Hanwoo beef banquet with aged doenjang jjigae.",
            "Brewery tasting tours: call or check opening hours upon arrival.",
            "Tasting ~₩15,000; Hanwoo dinner ~₩45,000 per person.",
            "Seonghwan pear wine bottles make wonderful boxed souvenirs.",
            "Brewery tasting rooms and restaurants are fully indoor."
        ),
        # Day 11: Nov 11
        make_day(10, "Cheonan", "Freshwater Eel & Mountain Herbs", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Gakwonsa Temple Lake Walk → Cheonan Charcoal Freshwater Eel (Jangeo-gui) Feast",
            "Grand Bronze Statues & Stamina Freshwater Eel Feasts",
            [
                {"time": "09:30–12:30", "title": "Gakwonsa Temple & Grand Bronze Buddha", "detail": "Climb stone stairs to behold the colossal 15-meter seated Bronze Amita Buddha overlooking Taejosan Mountain.", "logistics": "Dongnam-gu Anseo-dong; City Bus 24 or 15-min taxi."},
                {"time": "12:45–14:15", "title": "Anseo Lake Buckwheat Makguksu Lunch", "detail": "Enjoy buckwheat cold noodles, potato pancakes, and wild herb bibimbap near the temple lake.", "logistics": "Gakwonsa lake restaurant row."},
                {"time": "14:45–17:30", "title": "Seongseong Lake Park Boardwalk Sunset", "detail": "Walk the wooden boardwalk loop around Seongseong Lake, visiting modern waterfront cafes.", "logistics": "Seobuk-gu Seongseong-dong; Bus 5 or 15-min taxi."},
                {"time": "18:00–19:30", "title": "Shinbu-dong Specialty Coffee & Dessert", "detail": "Taste Korean bingsu or hand-drip coffee.", "logistics": "Shinbu-dong."},
                {"time": "20:00–21:30", "title": "Cheonan Charcoal-Grilled Freshwater Eel (Jangeo-gui)", "detail": "Feast on thick cuts of freshwater eel grilled tableside over hardwood charcoal with sweet ginger glaze and pickled ginger.", "logistics": "Cheonan eel specialty hall."}
            ],
            [
                {"label": "Nutritional Stamina Cuisine", "text": "Charcoal-grilled freshwater eel provides rich omega-3 nutrients and stamina before traveling to coastal Busan."},
                {"label": "Scenic Balance", "text": "Pairs colossal Buddhist sculpture with serene lakeside walking."}
            ],
            "Lunch: Anseo-dong buckwheat makguksu and potato pancake. Dinner: Tableside charcoal-grilled freshwater eel with seasoned sticky rice.",
            "Gakwonsa Temple is free admission; open year-round.",
            "Temple free; Lunch ~₩12,000; Eel banquet ~₩38,000 per person.",
            "Wrap grilled eel with fresh perilla leaf, sliced garlic, and ginger to balance richness.",
            "Gakwonsa prayer halls and eel dining rooms are warm and indoor."
        ),
        # Day 12: Nov 12
        make_day(11, "Cheonan", "Artisan Pantry Curation & KTX Prep", "Cheonan · Cheonan-Asan Station area / Shinbu-dong",
            "Cheonan Namsan Market Pantry Curation → 1934 Hodu-gwaja → KTX to Busan Prep",
            "Artisanal Pantry Gifts, Walnut Pastries & Pre-Busan Rail Prep",
            [
                {"time": "10:00–12:30", "title": "Cheonan Namsan Central Market Pantry Curation", "detail": "Curate artisanal sesame oil, roasted perilla seeds, dried red peppers, and regional honey from market vendors.", "logistics": "Sajik-dong (walk from Cheonan Station)."},
                {"time": "12:45–14:15", "title": "Namsan Market Handmade Dumpling & Noodle Lunch", "detail": "Enjoy hand-pulled knife-cut noodle soup and steamed giant mandu.", "logistics": "Namsan market food alley."},
                {"time": "14:30–16:30", "title": "1934 Hakhwa Hodu-gwaja Gift Curation", "detail": "Pick up sealed gift boxes of authentic walnut cakes for friends and family.", "logistics": "Cheonan Station branch."},
                {"time": "17:00–18:30", "title": "Hotel Packing & KTX Ticket Check", "detail": "Pack primary luggage for Friday morning KTX to coastal Busan and verify seat assignments.", "logistics": "Hotel room."},
                {"time": "19:00–21:00", "title": "Cheonan Farewell Korean Feast", "detail": "Celebrate 5 nights in Cheonan with rich pork galbi barbecue.", "logistics": "Shinbu-dong dining lane."}
            ],
            [
                {"label": "Artisan Pantry Curation", "text": "Freshly pressed perilla oil and roasted sesame seeds from traditional markets are incomparable culinary gifts."},
                {"label": "Pre-Busan Preparation", "text": "Packing early ensures a relaxed Friday morning high-speed train directly to Busan."}
            ],
            "Lunch: Namsan Market handmade kalguksu and dumplings. Dinner: Charcoal-grilled pork galbi with cold noodles.",
            "Hakhwa Hodu-gwaja gift boxes have 4–5 days room-temperature shelf life (freeze for longer storage).",
            "Hodu-gwaja gift box ~₩12,000; Dinner ~₩25,000 per person.",
            "Pack primary bags tonight for Friday morning KTX to Busan.",
            "Namsan Central Market is a fully covered weather-proof arcade."
        ),
        # Day 13: Nov 13
        make_day(12, "Busan", "Coastward Rail & Wheat Noodle Legends", "Busan · Haeundae Beachfront",
            "KTX Cheonan-Asan to Busan (1h45m) → Choryang Milmyeon → Haeundae Market Grilled Sea Eel",
            "High-Speed Coastal Rail, Wheat Noodle Legends & Night Sea Eel Grills",
            [
                {"time": "10:00–11:45", "title": "KTX High-Speed Rail to Busan", "detail": "Smooth 1-hour 45-minute direct journey from Cheonan-Asan to Busan Station on the southern sea.", "logistics": "Direct Gyeongbu high-speed line."},
                {"time": "12:00–13:15", "title": "Choryang Milmyeon (Busan Wheat Noodle Icon)", "detail": "Taste authentic Busan Milmyeon: cold wheat noodles in chilled spiced broth with cucumber, boiled beef, and hot kettle broth.", "logistics": "Choryang-dong directly opposite Busan Station."},
                {"time": "13:45–15:00", "title": "Transfer to Haeundae Beach Base", "detail": "Check into Haeundae hotel (e.g. L7 Haeundae or Felix by STX).", "logistics": "Metro Line 2 or taxi across harbor bridge."},
                {"time": "15:30–18:00", "title": "Haeundae Beach Promenade Walk", "detail": "Stroll white sands of Haeundae Beach and follow the wooden coastal boardwalk around Dongbaek Island to APEC House.", "logistics": "Paved oceanside walkway."},
                {"time": "18:30–21:30", "title": "Haeundae Traditional Market Feast", "detail": "Sample sizzling grilled sea eel (godeulbaegi), fresh seafood hot pot, Korean tteokbokki, and famous Busan ssiat hotteok (brown sugar seed pancake).", "logistics": "Haeundae Market Gunam-ro lane."}
            ],
            [
                {"label": "Iconic Busan Wheat Noodles", "text": "Milmyeon is Busan's historical Korean War innovation, substituting wheat flour for buckwheat."},
                {"label": "Night Market Vibrancy", "text": "Haeundae Market comes alive at night with smoking street stalls and live seafood tanks."}
            ],
            "Lunch: Choryang Milmyeon (cold wheat noodles & giant dumplings). Dinner: Haeundae Market grilled sea eel, seafood pajeon, and ssiat hotteok.",
            "Book KTX Cheonan-Asan→Busan on Korail app 30 days in advance.",
            "KTX ticket ~₩46,500; Milmyeon ~₩8,500; Market dinner ~₩25,000.",
            "Sea eel is grilled with spicy red pepper sauce; ask for non-spicy salt grill (sogeum-gui) if preferred.",
            "Haeundae market is a covered pedestrian street."
        ),
        # Day 14: Nov 14
        make_day(13, "Busan", "Live Flounder Sashimi & Saturday Drones", "Busan · Haeundae Beachfront",
            "Minrak Raw Fish Town (Live Seasonal Yellowtail & Flounder) → Gwangalli Saturday Drone Show",
            "Live Sliced Sashimi Overlooking the Bay & 500-Drone Sky Ballet",
            [
                {"time": "10:30–13:30", "title": "Cheongsapo Seaside Grilled Clam Feast", "detail": "Dine on live scallops, abalone, and clams grilled over briquettes with butter and cheese overlooking the twin lighthouses.", "logistics": "Cheongsapo harbor row."},
                {"time": "14:00–16:30", "title": "Cheongsapo Ocean Skywalk & Cafe Street", "detail": "Walk Daritdol Skywalk over breaking ocean waves and sip artisan coffee.", "logistics": "Cheongsapo waterfront."},
                {"time": "17:00–18:30", "title": "Gwangalli Beach Twilight Stroll", "detail": "Watch the sunset illuminate Gwangan Suspension Bridge.", "logistics": "Gwangan Station Line 2 Exit 3/5."},
                {"time": "19:00–21:30", "title": "Minrak Raw Fish Town & Saturday Night 500-Drone Show", "detail": "Feast on seasonal sliced yellowtail (bangeo) and flounder sashimi with sea views, stepping out onto the sand to watch 500+ synchronized LED drones dance in the night sky.", "logistics": "Millak Raw Fish Tower / Gwangalli Beach (drones at 19:00 & 21:00)."}
            ],
            [
                {"label": "Oceanfront Charcoal Grilling", "text": "Cheongsapo's clam grilling tradition combines crashing waves with buttery charcoal-cooked shellfish."},
                {"label": "Saturday Night Drone Miracle", "text": "Gwangalli drone performance over Gwangan Diamond Bridge is Busan's premier evening spectacle."}
            ],
            "Lunch: Cheongsapo seaside grilled live clams (jogae-gui) with butter and melted cheese. Dinner: Millak Raw Fish Town sliced yellowtail sashimi, abalone, and spicy fish stew.",
            "Book Sky Capsule 14 days in advance on official website.",
            "Clam feast ~₩35,000 per person; Sashimi banquet ~₩40,000 per person.",
            "Clam shells get hot on the grill; use provided cloth gloves and tongs.",
            "Millak raw fish buildings have panoramic glass indoor dining rooms."
        ),
        # Day 15: Nov 15
        make_day(14, "Busan", "Royal Scallion Pancakes & Master Makgeolli", "Busan · Haeundae Beachfront",
            "Dongnae Halmae Pajeon (Busan Cultural Asset #1) → Geumjeongsanseong Makgeolli #1",
            "80-Year Royal Scallion Pancakes & Mountain Artisanal Rice Wine",
            [
                {"time": "10:30–12:30", "title": "Beomeosa Mountain Temple Autumn Walk", "detail": "Scenic mountain stroll to work up an appetite.", "logistics": "Beomeosa Station Line 1 + Bus 90."},
                {"time": "13:00–15:00", "title": "Dongnae Halmae Pajeon (Busan Cultural Asset #1)", "detail": "Feast on Korea's most celebrated scallion pancake: tender young green onions layered with beef, squid, mussels, and oysters in a glutinous rice batter, steamed with beaten egg.", "logistics": "Dongnae-gu Myeongnyun-dong; historic restaurant."},
                {"time": "15:30–17:30", "title": "Geumjeongsanseong Mountain Village & Makgeolli Tasting", "detail": "Sample Korea's only designated Food Master Makgeolli #1, crafted using traditional 500-year-old wheat nuruk fermentation in mountain stone rooms.", "logistics": "Sanseong village; Bus 203 from Oncheonjang Station."},
                {"time": "18:00–20:00", "title": "Oncheonjang Natural Hot Spring Foot Bath", "detail": "Rest tired feet in historic Oncheonjang outdoor mineral hot springs.", "logistics": "Oncheonjang Station Line 1."},
                {"time": "20:30–22:00", "title": "Korean Fried Chicken & Busan Craft Draft", "detail": "Crispy golden fried chicken in Haeundae.", "logistics": "Haeundae Gunam-ro."}
            ],
            [
                {"label": "Intangible Cultural Asset", "text": "Dongnae Pajeon was historically presented to Joseon kings and is distinct from ordinary flat jeon."},
                {"label": "Designated Folk Wine", "text": "Geumjeongsanseong Makgeolli is Korea's most historic artisanal rice wine."}
            ],
            "Lunch: Dongnae Halmae Pajeon (royal scallion seafood pancake) paired with Geumjeongsanseong Makgeolli. Dinner: Haeundae gourmet fried chicken with honey garlic sauce.",
            "Dongnae Halmae Pajeon is closed on Mondays; open Tuesday through Sunday.",
            "Dongnae Pajeon lunch ~₩25,000 per person; Makgeolli ~₩5,000 bottle.",
            "Dongnae Pajeon has a soft, tender, pudding-like center from rice flour and egg; this is traditional authenticity.",
            "Dongnae Pajeon restaurant and Oncheonjang spa are fully indoor."
        ),
        # Day 16: Nov 16
        make_day(15, "Busan", "Jagalchi Marine Bounty & Night Markets", "Busan · Haeundae Beachfront",
            "Jagalchi Fish Market Giant Seafood Feast → Bupyeong Kkangtong Night Market",
            "Korea's Marine Epicenter & Vibrant Night Street Eats",
            [
                {"time": "10:30–13:30", "title": "Jagalchi Fish Market Giant Seafood Banquet", "detail": "Pick live King Crab, Snow Crab, or live octopus (san-nakji) from 1F stalls and have it steamed and prepared immediately on 2F with crab-roe fried rice.", "logistics": "Jagalchi Station Line 1 Exit 10."},
                {"time": "14:00–16:00", "title": "BIFF Square Snack Crawl", "detail": "Taste original seed hotteok (crispy brown sugar pancake filled with sunflower seeds and pine nuts) and spicy rice cake skewers.", "logistics": "Nampo-dong BIFF Square."},
                {"time": "16:30–18:30", "title": "Gamcheon Culture Village Sunset Walk", "detail": "Stroll colorful hillside alleys and photograph the pastel harbor vistas.", "logistics": "Toseong Station Exit 6 + local bus."},
                {"time": "19:00–21:30", "title": "Bupyeong Kkangtong Night Market Feasting", "detail": "Sample iconic night market street dishes: Bibim Dangmyeon (glass noodles with spicy seasoning), giant fried Busan fishcakes (Eomuk), skewered grilled pork, and rolled egg omelets.", "logistics": "Bupyeong Market (stalls open from 19:30)."}
            ],
            [
                {"label": "Seafood Epicenter", "text": "Jagalchi is the largest and most legendary marine market in East Asia."},
                {"label": "Street Food Variety", "text": "Bupyeong Kkangtong is Korea's first official permanent night street food market."}
            ],
            "Lunch: Jagalchi Market steamed giant king crab with fried rice in crab carapace and seafood stew. Dinner: Bupyeong Kkangtong Night Market bibim dangmyeon, Samjin fishcakes, and street snacks.",
            "Market stalls are cash / T-Money preferred; cards accepted in 2F restaurants.",
            "King Crab lunch ~₩55,000–₩75,000 per person; Night market ~₩18,000.",
            "Crab prices are seasonal by weight; negotiate price before cooking.",
            "Jagalchi building and Bupyeong market are covered arcade facilities."
        ),
        # Day 17: Nov 17
        make_day(16, "Busan", "Giant Snow Crabs & Emerald Abalone", "Busan · Haeundae Beachfront",
            "Gijang Snow Crab Market → Yeonhwa-ri Abalone Porridge Village",
            "Steamed Coastal Snow Crabs & Oceanic Porridge Cauldron",
            [
                {"time": "10:30–13:30", "title": "Gijang Market Live Snow Crab Feast", "detail": "Select live Russian snow crabs and red king crabs from steaming wooden cedar boxes in Gijang market, served with rich crab-butter fried rice.", "logistics": "Donghae Line to Gijang Station or 25-min taxi from Haeundae."},
                {"time": "14:00–16:30", "title": "Yeonhwa-ri Coastal Tent Village & Sea-View Cafe", "detail": "Stroll past the scenic orange and red lighthouses and enjoy coffee at a modern oceanfront cafe in Gijang.", "logistics": "Yeonhwa-ri coastal road."},
                {"time": "17:00–19:00", "title": "Ananti Cove Ocean Promenade", "detail": "Relax along the coastal cliffs of Osiria tourism complex.", "logistics": "Near Haedong Yonggungsa."},
                {"time": "19:30–21:30", "title": "Yeonhwa-ri Abalone Porridge (Jeonbok-juk) Cauldron", "detail": "Dine on thick, emerald-green abalone porridge simmered with whole abalone entrails and sesame oil in a massive cast iron pot.", "logistics": "Yeonhwa-ri seafood village."}
            ],
            [
                {"label": "Gijang Snow Crab Authority", "text": "Gijang is Korea's premier East Sea snow crab distribution hub, offering peak freshness and direct wholesale value."},
                {"label": "Abalone Intestine Porridge", "text": "True Busan jeonbok-juk is emerald green from the fresh abalone liver (geu), imparting deep oceanic umami."}
            ],
            "Lunch: Gijang Market freshly steamed snow crab with seasoned crab-roe rice. Dinner: Yeonhwa-ri traditional abalone porridge (jeonbok-juk) in a cast iron pot.",
            "Gijang market vendors offer steaming service included with crab purchase.",
            "Snow crab lunch ~₩50,000–₩70,000 per person; Abalone porridge ~₩15,000 per person.",
            "Abalone porridge is cooked fresh to order in cauldrons; allow 20 mins preparation time.",
            "Gijang crab restaurants and Ananti complexes are comfortable and indoor."
        ),
        # Day 18: Nov 18
        make_day(17, "Busan", "Heritage Pork Bone Soup & Pojangmacha", "Busan · Haeundae Beachfront",
            "Songjeong 3-dae Dwaeji Gukbap Alley → Seomyeon Pojangmacha Street Tents",
            "Boiling Pork Bone Cauldrons & Atmospheric Orange Tents",
            [
                {"time": "10:30–12:30", "title": "Songjeong 3-dae Gukbap (Since 1946)", "detail": "Savor authentic Busan Dwaeji Gukbap: 24-hour simmered milky pork bone broth loaded with tender pork shoulder, spicy seasoned chives (buchu), and fermented saeujeot shrimp.", "logistics": "Seomyeon Station Line 1/2 Exit 1 (Gukbap Alley)."},
                {"time": "13:00–15:30", "title": "Seomyeon Youth Street & Cafe Alleys (Jeonpo-dong)", "detail": "Explore transformed tool-workshop cafes, artisan dessert bakeries, and specialty matcha shops in Jeonpo.", "logistics": "Jeonpo Station Line 2 Exit 7."},
                {"time": "16:00–18:30", "title": "Centum City Spa Land Thermal Soak", "detail": "Relax and detox in 18 mineral spring pools before evening street feasting.", "logistics": "Centum City Station Line 2."},
                {"time": "19:00–21:30", "title": "Seomyeon Pojangmacha (Orange Street Tents) Night", "detail": "Dine under iconic orange street tents: sizzling grilled pork belly, spicy stir-fried octopus, fishcake broth, and soju.", "logistics": "Lotte Department Store Seomyeon back alley."}
            ],
            [
                {"label": "70-Year Soup Lineage", "text": "Songjeong 3-dae is Busan's most celebrated pork soup institution, bubbling continuously since 1946."},
                {"label": "Cinematic Street Tents", "text": "Pojangmacha street tents represent Korea's most atmospheric night dining tradition."}
            ],
            "Lunch: Songjeong 3-dae Dwaeji Gukbap (pork soup with suyuk boiled pork). Afternoon: Jeonpo artisan pastry & coffee. Dinner: Seomyeon Pojangmacha street tents (grilled spam, eggs, spicy octopus, and soju).",
            "Songjeong 3-dae Gukbap is open 24 hours.",
            "Gukbap lunch ~₩9,500; Pojangmacha dinner ~₩22,000 per person.",
            "Pojangmacha street tents are cash or bank transfer preferred.",
            "Seomyeon underground shopping mall and Gukbap restaurants are completely indoor."
        ),
        # Day 19: Nov 19
        make_day(18, "Busan", "Seaside Porridge & Sunset Tea (CSAT Day)", "Busan · Haeundae Beachfront",
            "Dalmaji Hill Sea-View Teahouses → Cheongsapo Clam Stew (CSAT Day)",
            "Panoramic Ocean Teahouses & Clam Stew (CSAT / Suneung Day)",
            [
                {"time": "10:30–12:30", "title": "Dalmaji Hill Scenic Coastal Walk", "detail": "Gentle stroll along pine-covered Dalmaji Hill overlooking the sparkling Korea Strait.", "logistics": "Walk from Haeundae or short taxi."},
                {"time": "12:45–14:30", "title": "Cheongsapo Seafood Stew & Grilled Fish Lunch", "detail": "Enjoy boiling seafood casserole (haemultang) packed with blue crab, prawns, squid, and clams.", "logistics": "Cheongsapo waterfront."},
                {"time": "15:00–17:30", "title": "Traditional Korean Tea & Rice Cake Atelier", "detail": "Sip artisanal green tea from Boseong and fermented plum tea accompanied by freshly steamed rainbow rice cakes (mujigae-tteok).", "logistics": "Dalmaji-gil teahouse."},
                {"time": "18:00–21:00", "title": "Busan Farewell Feast: Hanwoo Beef Short Ribs", "detail": "Celebrate 7 unforgettable Busan nights with charcoal-grilled marinated Hanwoo beef short ribs and cold naengmyeon noodles.", "logistics": "Haeundae Somunnan Amso Galbi."}
            ],
            [
                {"label": "Low-Stakes CSAT Harmony", "text": "Nov 19 national exam day is spent peacefully in Haeundae and Dalmaji without city transit friction."},
                {"label": "Epicurean Finale", "text": "Haeundae's legendary beef short ribs provide the ultimate culinary celebration in Busan."}
            ],
            "Lunch: Cheongsapo bubbling seafood casserole (haemultang). Afternoon: Traditional plum tea & rice cakes. Dinner: Haeundae Somunnan Amso Galbi marinated beef short ribs with potato noodles.",
            "Book Haeundae Somunnan Amso Galbi table upon arrival or go at 17:30 to avoid wait.",
            "Lunch ~₩20,000; Farewell Hanwoo dinner ~₩50,000 per person.",
            "Add potato noodles (gamja-sari) to the beef galbi pan for the authentic local finish.",
            "Dalmaji teahouses and Haeundae indoor restaurants provide full comfort."
        ),
        # Day 20: Nov 20
        make_day(19, "Seoul", "Capital Return & BBQ", "Seoul · Seoul Station / Myeongdong",
            "Morning KTX Busan to Seoul → Mapo Aged Pork Belly Barbecue → Gwanghwamun Night Walk",
            "Return to Capital & Charcoal Pork Belly Feast",
            [
                {"time": "09:30–10:15", "title": "Busan Station Departure", "detail": "Pick up Samjin Amook warm fishcake snacks at Busan Station concourse and board direct KTX.", "logistics": "Busan Station 2F."},
                {"time": "10:30–12:45", "title": "KTX High-Speed Rail to Seoul", "detail": "2-hour 15-minute smooth transit back to Seoul Station.", "logistics": "Arrive inside Seoul Station."},
                {"time": "13:00–14:30", "title": "Seoul Station Hotel Check-in & Noodle Lunch", "detail": "Check into Seoul Station hotel and enjoy warm kalguksu or dumpling soup.", "logistics": "Direct hotel connection."},
                {"time": "15:00–18:00", "title": "Gwanghwamun Square & Kyobo Gourmet Bookstore", "detail": "Explore Kyobo bookstore foodie cookbook section and stroll Gwanghwamun square.", "logistics": "Gwanghwamun Station Line 5."},
                {"time": "18:30–21:00", "title": "Mapo Charcoal Aged Pork Belly (Samgyeopsal) Feast", "detail": "Savor thick-cut 14-day dry-aged pork belly grilled over oak charcoal, wrapped with aged kimchi, perilla leaves, and ssamjang.", "logistics": "Mapo / Gongdeok BBQ district."}
            ],
            [
                {"label": "Friday Departure Buffer", "text": "Arriving in Seoul on Friday guarantees 2 nights of relaxed dining and zero weekend travel stress."},
                {"label": "Aged Pork Excellence", "text": "Seoul's aged pork belly restaurants represent masterclass butchery and table-side grilling."}
            ],
            "Lunch: Busan Station Samjin Amook fishcakes + Seoul Station warm kalguksu. Dinner: Mapo 14-day dry-aged thick samgyeopsal pork belly with kimchi stew.",
            "Book KTX Busan→Seoul 30 days in advance on Korail app.",
            "KTX ticket ~₩59,800; Dinner ~₩28,000 per person.",
            "Friday afternoon KTX trains sell out fast; reserve morning departure.",
            "Lotte Mart and Seoul Station concourse are completely enclosed."
        ),
        # Day 21: Nov 21
        make_day(20, "Seoul", "Food Souvenirs & Farewell Banquet", "Seoul · Seoul Station / Myeongdong",
            "Namdaemun Market Food Alley → Seoul Station Lotte Mart Gourmet Curation → Grand Farewell Hanwoo Banquet",
            "Gourmet Pantry Curation & Michelin Farewell Feast",
            [
                {"time": "09:30–12:30", "title": "Namdaemun Market Kalguksu & Hotteok Alleys", "detail": "Taste fresh vegetable hotteok (japchae hotteok) and enjoy handmade kalguksu with complimentary bibim naengmyeon.", "logistics": "Hoehyeon Station Line 4 Exit 5."},
                {"time": "13:00–15:30", "title": "Seoul Station Lotte Mart Mega Gourmet Curation", "detail": "Fill luggage with culinary treasures: toasted seasoned seaweed (gim), artisan gochujang, sesame oil, Korean snack boxes, and dried seafood with instant tax refund.", "logistics": "Lotte Mart 2F immediate tax refund counter."},
                {"time": "16:00–18:00", "title": "Luggage Packing & Scale Verification", "detail": "Pack gourmet pantry items safely into luggage, weigh bags at hotel front desk, and complete online flight check-in.", "logistics": "Hotel room."},
                {"time": "18:30–21:30", "title": "Grand Culinary Finale: Charcoal Hanwoo Beef Banquet", "detail": "Celebrate the 21-night culinary odyssey with premium charcoal-grilled Korean Hanwoo beef tenderloin, cold naengmyeon, and fine Korean plum wine (maesil-ju).", "logistics": "Central Seoul premier Hanwoo dining room."}
            ],
            [
                {"label": "Culinary Souvenir Mastery", "text": "Curating authentic pantry essentials brings Korea's rich gastronomy home to your own kitchen."},
                {"label": "Zero Departure Stress", "text": "Completing all shopping, packing, and online check-in by Saturday night ensures Sunday morning is 100% serene."}
            ],
            "Lunch: Namdaemun Market japchae hotteok and hand-pulled kalguksu soup. Dinner: Grand Hanwoo charcoal beef banquet with Pyongyang cold noodles and maesil wine.",
            "Complete online airline check-in 24 hours prior to Sunday 13:00 departure.",
            "Gourmet souvenirs ~₩60,000–₩120,000; Grand Farewell Dinner ~₩50,000 per person.",
            "Pack liquid condiments (sesame oil, sauces) securely inside plastic bags in checked luggage.",
            "Shinsegae and Lotte underground arcades provide full rain-proof shopping."
        ),
        # Day 22: Nov 22
        make_day(21, "Seoul", "Departure", "Departure · Incheon International Airport",
            "AREX Non-Stop Express to ICN → Airport Korean Food Street Breakfast → Flight at 13:00",
            "Seamless Airport Rail & Farewell Korean Breakfast",
            [
                {"time": "08:30–09:15", "title": "Hotel Checkout & AREX Express Boarding", "detail": "Check out of Seoul Station hotel and board direct AREX Non-Stop Express Train to Incheon Airport (43 mins).", "logistics": "B2 Seoul Station."},
                {"time": "09:30–10:15", "title": "AREX Express to ICN Terminal 1 / 2", "detail": "Smooth, direct airport train ride with reserved seating and dedicated luggage racks.", "logistics": "43 min to T1 / 51 min to T2."},
                {"time": "10:15–12:15", "title": "Airport Customs, Tax Refunds & Farewell Breakfast", "detail": "Drop luggage, clear security, collect tax refund cash, and enjoy a warm bowl of Korean abalone porridge or beef soup at ICN Korean Food Street.", "logistics": "Target arriving at departure gate by 12:20."},
                {"time": "12:30–13:00", "title": "Boarding & Flight Departure at 13:00", "detail": "Board flight home after an extraordinary 22-day culinary journey across South Korea.", "logistics": "Flight departs at 13:00 local time."}
            ],
            [
                {"label": "Precision Logistics", "text": "Direct AREX express from Seoul Station guarantees exact, predictable airport arrival at 10:15."},
                {"label": "Relaxed Departure", "text": "Ample time for tax refunds, duty-free pickup, and a comforting farewell meal before boarding."}
            ],
            "Breakfast: ICN Airport Korean Food Street (warm abalone porridge or beef seolleongtang soup).",
            "Verify your airline departure terminal (T1 vs T2) before boarding AREX.",
            "AREX Express ticket ₩13,000 per person (fare raised from ₩11,000; verified 2026).",
            "Terminal 2 is 8 minutes further on the AREX line than Terminal 1.",
            "If AREX express sells out, AREX all-stop commuter train runs every 8 minutes."
        )
    ]

    scorecard = [
        {"label": "Michelin & Temple Dining", "value": "5/5", "tone": "good"},
        {"label": "Heritage Artisans", "value": "5/5", "tone": "good"},
        {"label": "Regional Gastronomy", "value": "5/5", "tone": "good"},
        {"label": "Live Seafood Banquets", "value": "5/5", "tone": "good"}
    ]

    return {
        "id": "seoul-cheonan-busan-gourmet",
        "shortTitle": "Seoul · Cheonan · Busan (Regional Gourmet & Artisans)",
        "title": "Artisan Gastronomy, Regional Craft & Market Feasts (Regional Gastronomy & Artisans)",
        "routeLabel": "Seoul (7N) → Cheonan (5N) → Busan (7N) → Seoul (2N)",
        "badge": "Temple Food & Artisanal Regional Feasts",
        "bestFor": "Connoisseurs of Korean culinary heritage, Michelin gourmands, lovers of centuries-old lineages (Hakhwa Hodu-gwaja, Byeongcheon Soondae, Dongnae Pajeon), and travelers seeking authentic regional craft wines and temple banquets.",
        "decisionSummary": "An epicurean odyssey linking Michelin-starred Buddhist temple cuisine and Majang 1++ Hanwoo beef in Seoul, 90-year-old Hakhwa walnut bakeries, Byeongcheon soondae alley, and Seonghwan pear wine in Cheonan, culminating in Busan's royal scallion pancakes, Gijang snow crabs, and emerald abalone cauldrons.",
        "recommendation": "Choose this route if you want to explore the finest regional culinary lineages and artisan food traditions across South Korea.",
        "tradeoff": "Requires reserving special Michelin temple dining in advance and traveling to regional culinary alleys for authentic dining.",
        "scorecard": scorecard,
        "bases": get_scb_common_bases(),
        "transfers": get_scb_common_transfers(),
        "budgetScenarios": get_scb_budget_scenarios(),
        "bookingPriorities": get_scb_booking_priorities(),
        "days": days
    }
