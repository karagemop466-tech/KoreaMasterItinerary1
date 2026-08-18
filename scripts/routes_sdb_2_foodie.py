#!/usr/bin/env python3
"""Route Blueprint: Seoul · Daejeon · Busan (The Great Korean Culinary & Market Trail)."""

from scripts.generate_all_itineraries import make_day
from scripts.itinerary_builder_sdb import (
    get_sdb_common_bases,
    get_sdb_common_transfers,
    get_sdb_budget_scenarios,
    get_sdb_booking_priorities
)

def get_sdb_foodie():
    days = [
        # Day 1: Nov 1
        make_day(0, "Seoul", "Arrival", "Seoul · Myeongdong / Seoul Station edge",
            "ICN arrival at 21:00 → late transfer → Korean convenience store snack testing → sleep",
            "Late Landing & Iconic Late-Night Convenience Store Reset",
            [
                {"time": "21:00–22:15", "title": "ICN Arrival & Welcome", "detail": "Clear customs and collect transport cards and pocket Wi-Fi / eSIM.", "logistics": "Terminal 1 or 2."},
                {"time": "22:30–23:45", "title": "Direct Transfer to Myeongdong / Seoul Station", "detail": "Take the airport limousine bus or official taxi directly to hotel doorstep.", "logistics": "Late-night luggage ease."},
                {"time": "23:45–00:30", "title": "CU / GS25 Late-Night Snack Intro", "detail": "Sample legendary Korean convenience store staples: Binggrae banana milk, tuna mayo samgak kimbap, and warm barley tea.", "logistics": "Convenience store adjacent to hotel."}
            ],
            [
                {"label": "Gentle Gastronomy", "text": "Starting with beloved convenience store snacks introduces Korean culinary culture without late-night digestive heaviness."},
                {"label": "Rest Priority", "text": "Save full appetite for tomorrow's market feasts."}
            ],
            "Late-night convenience store gourmet treats: banana milk, warm samgak kimbap, hot roasted chestnuts.",
            "Confirm late check-in with hotel in advance.",
            "Limousine Bus ~₩17,000 / Snacks ~₩6,000.",
            "Avoid overly spicy ramyun on arrival night to prevent stomach distress after flights.",
            "24-hour hotel neighborhood convenience store provides warm teas and light snacks."
        ),
        # Day 2: Nov 2
        make_day(1, "Seoul", "Culinary Heritage", "Seoul · Myeongdong / Seoul Station edge",
            "Myeongdong Kyoja Handmade Dumplings → Insadong Traditional Teahouse → Gwangjang Market Feast",
            "Michelin Bib Gourmand Noodles & Korea's Oldest Food Market",
            [
                {"time": "10:30–12:30", "title": "Myeongdong Kyoja (Since 1966)", "detail": "Savor Michelin Bib Gourmand handmade kalguksu noodles in rich chicken broth, steamed pork mandu, and famously pungent garlic kimchi.", "logistics": "Myeongdong 2-ga; arrive slightly before noon to beat queues."},
                {"time": "13:00–15:30", "title": "Insadong Traditional Hanok Teahouse & Confectionery", "detail": "Sip deep roasted Ssanggwa-cha (medicinal herb tea with egg yolk) or sweet Omija tea paired with handmade yakgwa (honey pastry).", "logistics": "Anguk Station Line 3 Exit 6."},
                {"time": "16:00–18:00", "title": "Ikseon-dong Dessert Alleys", "detail": "Sample soufflé pancakes, salt bread (so-geum bbang), and black sesame gelato in preserved hanok cafes.", "logistics": "Jongno 3-ga Station Exit 4."},
                {"time": "18:30–21:30", "title": "Gwangjang Traditional Market Grand Feast", "detail": "Dive into the vibrant food stalls: crispy bindaetteok (mung bean pancake fried in oil), addictive mayak gimbap with mustard sauce, and fresh yukhoe (beef tartare with pear and raw egg yolk).", "logistics": "Jongno 5-ga Station Line 1 Exit 8."}
            ],
            [
                {"label": "Legendary Institutions", "text": "Pairs 60-year-old culinary stalwarts with lively street market stall culture."},
                {"label": "Walkable Progression", "text": "Seamless walking route from Myeongdong across Cheonggyecheon to Jongno and Gwangjang."}
            ],
            "Lunch: Myeongdong Kyoja (kalguksu & mandu). Afternoon: Traditional tea & yakgwa. Dinner: Gwangjang Market bindaetteok, mayak gimbap, yukhoe, and draft makgeolli.",
            "Gwangjang market stalls are cash or T-Money friendly; ATM available on site.",
            "Daily food budget ~₩45,000 per person.",
            "Yukhoe alley can have brief lines during evening peak; stall rotation is fast.",
            "Gwangjang covered market roof shields from any autumn rain."
        ),
        # Day 3: Nov 3
        make_day(2, "Seoul", "Pork Galbi & Pancake Skewers", "Seoul · Myeongdong / Seoul Station edge",
            "Mangwon Neighborhood Food Market → Yeonnam Micro-Bakeries → Mapo Charcoal Galbi & Gongdeok Jeon Alley",
            "Local Market Stalls, Pajeon Skewers & Charcoal Ribs",
            [
                {"time": "10:00–12:30", "title": "Mangwon Traditional Market Exploration", "detail": "Sample beloved local snacks: sweet & spicy boneless fried chicken (dakgangjeong), marshmallow ice cream, and handmade croquettes.", "logistics": "Mangwon Station Line 6 Exit 2."},
                {"time": "13:00–15:00", "title": "Yeonnam-dong Artisan Coffee & Salt Bread", "detail": "Stroll Gyeongui Line Forest Park and discover Seoul's finest specialty third-wave coffee roasters and French butter salt bread bakeries.", "logistics": "Hongik Univ. Station Exit 3."},
                {"time": "15:30–17:30", "title": "Gongdeok Jeon (Pancake) & Jokbal Alley", "detail": "Pick your own assortment of freshly fried savory pancakes (jeon, stuffed peppers, shrimp, fish) piled onto wicker trays.", "logistics": "Gongdeok Station Line 5/6/AREX Exit 4."},
                {"time": "18:00–20:30", "title": "Mapo Charcoal Pork Galbi Feast", "detail": "Feast on succulent pork ribs marinated in sweet soy and garlic, grilled over glowing hardwood charcoal with steaming egg custard.", "logistics": "Mapo Station Line 5 BBQ Alley."}
            ],
            [
                {"label": "Authentic Local Markets", "text": "Mangwon is beloved by Seoul locals for authentic neighborhood pricing and artisan snack variety."},
                {"label": "Mapo Meat Heritage", "text": "Mapo is the historic birthplace of Seoul's charcoal galbi restaurant culture."}
            ],
            "Lunch: Mangwon Market street snacks (dakgangjeong & croquettes). Afternoon: Gongdeok assorted savory pancakes (jeon). Dinner: Mapo charcoal-grilled pork galbi with cold dongchimi noodles.",
            "Gongdeok Jeon alley is self-serve selection; pay by weight at the register.",
            "Daily food budget ~₩48,000 per person.",
            "Gongdeok gets lively with local office workers around 18:00; visit early.",
            "Mangwon Market is a fully covered arcade; Gongdeok restaurants are indoor."
        ),
        # Day 4: Nov 4
        make_day(3, "Seoul", "Hanwoo Beef & Artisan Roasteries", "Seoul · Myeongdong / Seoul Station edge",
            "Majang Meat Market 1++ Hanwoo Beef Tasting → Seongsu Industrial Lofts & Bakeries",
            "Korea's Crown Jewel Beef & Modernist Coffee Alleys",
            [
                {"time": "10:30–13:30", "title": "Majang Meat Market & Hanwoo Barbecue", "detail": "Browse Korea's premier meat wholesale district; select prime 1++ Korean Hanwoo beef ribeye, sirloin, and chuck flap, grilling it immediately at a second-floor charcoal restaurant.", "logistics": "Majang Station Line 5 Exit 2 or Yongdu Station Line 2."},
                {"time": "14:00–16:30", "title": "Seongsu-dong Cafe Hub (Center Coffee, Daelim Warehouse)", "detail": "Explore converted industrial shoe factories housing world-class barista counters, pour-over specialty brews, and bakery showrooms.", "logistics": "Seongsu Station Line 2 Exit 3."},
                {"time": "17:00–19:00", "title": "Seoul Forest Autumn Walk & Digestive Break", "detail": "Walk under golden ginkgo trees in Seoul Forest to refresh between heavy feasts.", "logistics": "Seoul Forest Station Suin-Bundang Line Exit 4."},
                {"time": "19:30–21:30", "title": "Seongsu Modern Korean Pub (Jumak)", "detail": "Pair regional cloudy rice wines (craft makgeolli) with crispy potato pancakes and braised pork belly.", "logistics": "Yeonmujang-gil dining lane."}
            ],
            [
                {"label": "Crown Jewel Beef", "text": "1++ Hanwoo is Korea's celebrated indigenous marbling standard, unmatched in tenderness and flavor."},
                {"label": "Artisan Contrast", "text": "Balances raw butcher market traditions with ultra-chic Seongsu coffee culture."}
            ],
            "Lunch: Majang Market 1++ Hanwoo beef charcoal grill with doenjang jjigae. Afternoon: Seongsu artisanal pour-over coffee & canelé. Dinner: Seongsu craft makgeolli & crispy gamjajeon potato pancake.",
            "In Majang Market, purchase meat cuts on 1F butcher counters, then pay small table-setting fee (₩6,000) at 2F grill restaurant.",
            "Hanwoo lunch ~₩60,000–₩85,000 per person; exceptional value compared to hotel steakhouses.",
            "Hanwoo is rich; enjoy with ssam leafy greens and wasabi.",
            "Majang indoor dining rooms and Seongsu cavernous cafes are warm and weather-proof."
        ),
        # Day 5: Nov 5
        make_day(4, "Seoul", "Live Seafood & Street Tteokbokki", "Seoul · Myeongdong / Seoul Station edge",
            "Noryangjin Fish Market Seafood Auction & Sashimi → Sindang-dong Tteokbokki Town",
            "Ocean Bounty in the Capital & Legendary Simmering Rice Cakes",
            [
                {"time": "10:00–13:30", "title": "Noryangjin Wholesale Fisheries Market", "detail": "Explore the massive multi-level fish market, selecting live king crab, snow crab, or fresh seasonal flatfish sashimi prepared fresh on the spot with spicy fish stew (maeuntang).", "logistics": "Noryangjin Station Line 1/9 direct footbridge connection."},
                {"time": "14:00–16:30", "title": "Yeouido The Hyundai Gourmet Supermarket", "detail": "Browse the sprawling Tasty Seoul basement food hall, discovering boutique confectioneries, matcha lattes, and artisan snacks.", "logistics": "Yeouido Station Line 5/9 or Yeouinaru Station."},
                {"time": "17:00–19:00", "title": "Cheonggyecheon Stream Evening Stroll", "detail": "Stroll illuminated urban waterfalls to work up an appetite.", "logistics": "Gwanghwamun / Euljiro access."},
                {"time": "19:30–21:30", "title": "Sindang-dong Tteokbokki Town Feasting", "detail": "Experience the historic 1953 birthplace of instant tteokbokki (Mabongnim Halmeoni), boiling rice cakes, fish cakes, ramen noodles, fried dumplings, and sweet black bean chili paste at the table.", "logistics": "Sindang Station Line 2/6 Exit 8."}
            ],
            [
                {"label": "Seafood to Street Food", "text": "Transitions from high-end marine treasures at Noryangjin to cozy, nostalgic street comfort food in Sindang."},
                {"label": "Historic Pedigree", "text": "Mabongnim Halmeoni restaurant has perfected tabletop tteokbokki for over 70 years."}
            ],
            "Lunch: Noryangjin fresh sashimi, butter-grilled abalone, and spicy maeuntang. Dinner: Sindang-dong Mabongnim Tteokbokki bubbling hot pot with fried dumplings and cheese.",
            "Noryangjin restaurant charges cooking fee (₩5,000–₩10,000 per kg) for steaming crab or grilling.",
            "Noryangjin lunch ~₩45,000 per person; Tteokbokki dinner ~₩12,000 per person.",
            "Fish market floors can be damp; wear closed-toe walking shoes.",
            "Noryangjin modern building and The Hyundai Seoul are completely enclosed and climate-controlled."
        ),
        # Day 6: Nov 6
        make_day(5, "Seoul", "Grilled Fish Alleys & Royal Soups", "Seoul · Myeongdong / Seoul Station edge",
            "Dongdaemun Grilled Fish Street → DDP Night Architecture → Euljiro Nogari Draft Beer Alley",
            "Smoky Briquette Grills & Industrial Alleys",
            [
                {"time": "10:30–12:30", "title": "Dongdaemun Grilled Fish Alley (Saengseon Gui)", "detail": "Dine in a narrow alley where fresh mackerel, Spanish mackerel (samchi), and croaker are continuously grilled over smoky outdoor briquettes until skin is blistered and crispy.", "logistics": "Dongdaemun Station Line 1/4 Exit 9."},
                {"time": "13:00–15:30", "title": "Dongdaemun Design Plaza & Fashion Arcade", "detail": "Explore DDP design exhibitions and surrounding textile fabric markets.", "logistics": "Dongdaemun History & Culture Park Station."},
                {"time": "16:00–18:00", "title": "Central Seoul Gourmet Dessert Cafe Stroll", "detail": "Enjoy Korean shaved ice dessert (bingsu) topped with sweet red beans, injeolmi rice cakes, and roasted soybean powder.", "logistics": "Myeongdong / Jongno Sulbing branch."},
                {"time": "18:30–21:30", "title": "Euljiro 'Hipjiro' Nogari Alley & Grilled Pork", "detail": "Join thousands of locals enjoying fresh draft lager, grilled dried pollack (nogari), garlic chicken, and thick pork collar in retro industrial alleys.", "logistics": "Euljiro 3-ga Station Exit 3/4."}
            ],
            [
                {"label": "Everyday Culinary Soul", "text": "Showcases the comforting, unpretentious alley dishes that fuel Seoul's working culture."},
                {"label": "Retro Atmosphere", "text": "Euljiro outdoor seating under glowing paper lanterns is an unforgettable cultural experience."}
            ],
            "Lunch: Dongdaemun briquette-grilled mackerel and spicy stir-fried squid (ojingeo bokkeum). Afternoon: Injeolmi Sulbing shaved ice. Dinner: Euljiro Nogari Alley draft beer, garlic chicken, and grilled pollack.",
            "Fish alley restaurants serve unlimited side dishes and warm rice with fish sets.",
            "Fish lunch ~₩12,000; Sulbing ~₩7,000; Euljiro beer night ~₩20,000.",
            "Dress warmly for Euljiro outdoor tables in November evening breezes.",
            "Indoor seating available in all Euljiro pubs if chilly."
        ),
        # Day 7: Nov 7
        make_day(6, "Seoul", "Traditional Soups & Station Prep", "Seoul · Myeongdong / Seoul Station edge",
            "Hadongkwan 80-Year Gomtang Beef Soup → Samcheongdong Sujebi → Sunday Train Prep",
            "Slow-Simmered Comfort & Weekend Market Prep",
            [
                {"time": "09:30–11:30", "title": "Hadongkwan Traditional Beef Gomtang", "detail": "Taste Seoul's definitive slow-simmered beef brisket soup (founded in 1939), served with tender tripe, spring onions, and aged radish kkakdugi.", "logistics": "Myeongdong 1-ga; open from early morning."},
                {"time": "12:00–14:30", "title": "Samcheong-dong Sujebi & Bukchon Walk", "detail": "Enjoy hand-torn dough pasta cooked in rich anchovy broth with tender clams in an earthenware pot.", "logistics": "Samcheong-dong main road."},
                {"time": "15:00–17:30", "title": "Seoul Station Lotte Mart Food Reconnaissance", "detail": "Preview Korean food gifts and pick up snacks for tomorrow morning KTX journey to Daejeon.", "logistics": "Seoul Station 2F."},
                {"time": "18:30–21:00", "title": "Feast of Chuncheon Dakgalbi (Spicy Stir-Fried Chicken)", "detail": "Savor spicy gochujang-marinated chicken, cabbage, sweet potatoes, and chewy rice cakes cooked on a giant tabletop cast iron skillet, finished with fried rice.", "logistics": "Myeongdong / Jongno dakgalbi specialty hall."}
            ],
            [
                {"label": "Restorative Broths", "text": "Hadongkwan and Samcheongdong Sujebi highlight Korea's mastery of comforting bone and anchovy broths."},
                {"label": "Transit Preparation", "text": "Packing early ensures a seamless Sunday morning KTX departure to Daejeon."}
            ],
            "Breakfast/Brunch: Hadongkwan traditional Hanwoo gomtang soup. Lunch: Samcheong-dong handmade sujebi and gamjajeon. Dinner: Chuncheon spicy dakgalbi with mozzarella cheese and bokkeumbap.",
            "Hadongkwan closes early when broth runs out (typically around 15:30); go for morning brunch.",
            "Daily food budget ~₩40,000 per person.",
            "Dakgalbi sauce can splatter; wear the provided restaurant aprons.",
            "All dining venues are fully enclosed indoors."
        ),
        # Day 8: Nov 8
        make_day(7, "Daejeon", "City Transition & Bakery Trail", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Morning KTX to Daejeon → Sung Sim Dang Bakery Mega-Trail → Daeheung-dong Spicy Tofu",
            "Korea's Bread Capital & Signature Fiery Tofu",
            [
                {"time": "09:30–10:30", "title": "KTX High-Speed Rail Seoul to Daejeon", "detail": "55-minute smooth train transit from Seoul Station to Daejeon Station.", "logistics": "Direct Gyeongbu line."},
                {"time": "11:00–13:30", "title": "Sung Sim Dang Legendary Bakery (Main Branch & Cake Boutique)", "detail": "Explore the multi-floor bakery empire: fresh Twigim Soboro (fried streusel pastry filled with sweet red bean), Bochoo Bread (leek & egg bun), and pure cream cakes.", "logistics": "Jungangno Station Line 1 Exit 2."},
                {"time": "14:00–15:30", "title": "Hotel Check-in & Rest in Yuseong / Dunsan", "detail": "Check into Daejeon hotel and drop luggage.", "logistics": "Metro Line 1 to Yuseong Spa Station."},
                {"time": "16:00–18:30", "title": "Jungang Market Street Snack Crawl", "detail": "Sample Daejeon traditional market specialties: handmade perilla oil seaweed, sundae blood sausage, and hot sugar-filled hotteok.", "logistics": "Daejeon Jungang Market adjacent to station."},
                {"time": "19:00–21:00", "title": "Daeheung-dong Gwangcheon Sikdang Dubu Duruchigi", "detail": "Feast on Daejeon legendary local dish: thick braised tofu cubes simmered in fiery red pepper broth, tossed with boiled kalguksu noodles.", "logistics": "Daeheung-dong restaurant street (30-year lineage)."}
            ],
            [
                {"label": "Bakery Capital of Korea", "text": "Sung Sim Dang is a national cultural icon, drawing pastry lovers from across the country."},
                {"label": "Daejeon Soul Food", "text": "Dubu Duruchigi is Daejeon's unique spicy comfort food invention."}
            ],
            "Lunch: Sung Sim Dang fresh warm pastries and Cake Boutique tarts. Dinner: Gwangcheon Sikdang spicy Dubu Duruchigi (braised tofu stir-fry with noodles and boiled pork suyuk).",
            "Book KTX train 30 days prior on Korail app.",
            "KTX fare ~₩23,700; Sung Sim Dang pastries ~₩15,000; Dinner ~₩18,000.",
            "Dubu Duruchigi is genuinely spicy; ask for mild ('deol-maep-ge') if sensitive.",
            "Sung Sim Dang and Gwangcheon Sikdang are comfortable indoor venues."
        ),
        # Day 9: Nov 9
        make_day(8, "Daejeon", "Kalguksu Pilgrimage & 5-Day Market", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Daejeon Kalguksu Alley Pilgrimage → Yuseong Traditional 5-Day Market",
            "Hand-Cut Noodle Heritage & Open-Air Market Aromas",
            [
                {"time": "10:30–12:30", "title": "Daejeon Hand-Cut Kalguksu Pilgrimage (Smoky Clam & Spicy Perilla)", "detail": "Taste Daejeon famous spicy clam kalguksu (Eolkeuni Kalguksu) enriched with crown daisy (ssukgat) and beaten egg.", "logistics": "Dunsan / Jungangno noodle quarter."},
                {"time": "13:00–15:30", "title": "Yuseong Traditional 5-Day Market & Street Treats", "detail": "Browse lively outdoor stalls selling roasted sweet chestnuts, fresh steamed corn, crispy hot bindaetteok, and traditional herbal medicines.", "logistics": "Yuseong Market area (held on dates ending in 4 and 9)."},
                {"time": "16:00–18:00", "title": "Yuseong Outdoor Foot Bath Spring Reset", "detail": "Soak feet in 42°C natural hot spring mineral waters while sipping roasted iced barley tea.", "logistics": "Yuseong Spa Park."},
                {"time": "18:30–21:00", "title": "Daejeon Suyuk & Bossam Dinner", "detail": "Enjoy tender boiled pork belly wrapped in freshly salted kimchi and sweet garlic sauce.", "logistics": "Yuseong dining street."}
            ],
            [
                {"label": "Noodle Capital Heritage", "text": "Daejeon developed Korea's most diverse kalguksu culture due to historic railway grain depots."},
                {"label": "Market Authenticity", "text": "Yuseong 5-day market offers unfiltered regional market sights, sounds, and snacks."}
            ],
            "Lunch: Famous Eolkeuni spicy clam kalguksu with ssukgat herbs. Dinner: Yuseong tender pork bossam with fresh oyster kimchi.",
            "Yuseong Market occurs on 4th, 9th, 14th, 19th, 24th, 29th of each month (Nov 9 is a market day!).",
            "Noodles ~₩9,000; Market snacks ~₩8,000; Bossam dinner ~₩25,000 per person.",
            "Foot bath requires removing shoes; clean feet at washing tap before entering pool.",
            "Indoor restaurants throughout Yuseong Spa district provide sheltered dining."
        ),
        # Day 10: Nov 10
        make_day(9, "Daejeon", "Acorn Jelly Village & Science Dining", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Gujeuk Muk-maeul (Acorn Jelly Village) → Shinsegae Art & Science Gourmet Hub",
            "Ancient Woodland Recipes & Sky-High Gourmet Delights",
            [
                {"time": "10:30–13:00", "title": "Gujeuk Muk-maeul (Historic Acorn Jelly Village)", "detail": "Visit Daejeon dedicated acorn jelly heritage village for warm Chae-muk (shredded acorn jelly in savory dried anchovy & kimchi broth) and acorn flour pancakes.", "logistics": "Yuseong-gu Gujeuk-dong; 20-min taxi or Bus 705."},
                {"time": "13:30–16:00", "title": "Expo Science Park & Hanbit Promenade Walk", "detail": "Digestive stroll around Hanbit Tower and Gapcheon River pedestrian bridge.", "logistics": "Near Shinsegae Complex."},
                {"time": "16:30–18:30", "title": "Shinsegae Art & Science Gourmet Market & Sky Lounge", "detail": "Explore the 38th-floor panoramic sky cafe and sample premium artisanal Korean pastries and boutique gelato.", "logistics": "Hotel Onoma / Shinsegae Tower."},
                {"time": "19:00–21:00", "title": "Daejeon Stone-Pot Bulgogi Feast", "detail": "Savor thinly sliced marinated Korean beef simmered in sweet soy broth with glass noodles and enoki mushrooms in a piping hot earthenware bowl.", "logistics": "Dunsan-dong restaurant quarter."}
            ],
            [
                {"label": "Unique Regional Specialty", "text": "Acorn jelly soup (dotorimuk-bap) is a historic Daejeon folk culinary treasure."},
                {"label": "Elevated Panoramas", "text": "Shinsegae 38F lounge provides 360-degree sunset views over Daejeon valley."}
            ],
            "Lunch: Gujeuk village warm Chae-muk acorn jelly soup with acorn pancake (muk-jeon). Dinner: Dunsan sizzling stone-pot beef bulgogi with seasonal banchan.",
            "Gujeuk muk-maeul restaurants are open daily 10:00–20:00.",
            "Muk lunch ~₩11,000; Sky lounge coffee ~₩6,500; Dinner ~₩22,000 per person.",
            "Acorn jelly has a subtle, pleasant herbal bitterness; season with kimchi and seaweed flakes.",
            "Shinsegae Art & Science is a multi-floor weatherproof indoor paradise."
        ),
        # Day 11: Nov 11
        make_day(10, "Daejeon", "Perilla Duck Stew & Herbal Recovery", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Gyejoksan Forest Walk → Yuseong Perilla Duck Stew (Oritang) Banquet",
            "Country Mountain Greens & Rich Herbal Duck Stew",
            [
                {"time": "09:30–12:30", "title": "Gyejoksan Mountain Autumn Trail Walk", "detail": "Take an invigorating autumn hike through pine woods to Gyejoksanseong fortress.", "logistics": "City Bus 74 or taxi to trail entrance."},
                {"time": "12:45–14:15", "title": "Country Village Dotorimuk & Potato Pancake", "detail": "Refuel with freshly made potato pancakes and seasoned mountain greens at a trailhead rustic lodge.", "logistics": "Jangdong trailhead restaurant."},
                {"time": "15:00–17:30", "title": "Yuseong Thermal Spa Bathhouse Soak", "detail": "Full mineral hot spring bath to soothe legs and stimulate appetite.", "logistics": "Yuseong Onsen bathhouse."},
                {"time": "18:30–21:00", "title": "Yuseong Famous Perilla Duck Stew (Oritang)", "detail": "Feast on rich, creamy simmered duck stew loaded with toasted perilla powder, water dropwort (minari), and wild mountain leeks.", "logistics": "Yuseong Hot Springs duck stew street."}
            ],
            [
                {"label": "Nutritional Stamina", "text": "Korean duck stew (Oritang) with perilla seed is considered the pinnacle of autumn stamina cuisine (boyang-sik)."},
                {"label": "Mountain to Mineral Spa", "text": "Pairs active morning hill walking with deeply relaxing evening hot spring bathing."}
            ],
            "Lunch: Rustic potato pancake and wild mountain herb bibimbap. Dinner: Yuseong bubbling Oritang duck stew with toasted perilla seeds and minari greens.",
            "Hot spring bathhouse fee ~₩10,000 payable at door.",
            "Lunch ~₩14,000; Hot spring ~₩10,000; Duck stew feast ~₩30,000 per person.",
            "Duck stew is served boiling hot in earthenware; dip tender duck meat in cho-gochujang perilla sauce.",
            "Yuseong spa facilities and duck stew dining halls are warm and sheltered."
        ),
        # Day 12: Nov 12
        make_day(11, "Daejeon", "Modern Pastry & Charcoal Freshwater Eel", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Sung Sim Dang DCC Robotic Bakery → Charcoal-Grilled Freshwater Eel Feast",
            "Futuristic Bakery Showrooms & High-Stamina Feasts",
            [
                {"time": "10:00–12:30", "title": "Sung Sim Dang DCC Branch & Bakery Lab", "detail": "Witness robotic tray delivery, sample freshly pulled sourdough, butter brioches, and signature walnut pies.", "logistics": "Daejeon Convention Center (DCC) 1F."},
                {"time": "13:00–15:00", "title": "Hanbat Arboretum Autumn Stroll", "detail": "Gentle walk among golden metasequoias and outdoor sculpture gardens.", "logistics": "Gapcheon River corridor."},
                {"time": "15:30–17:30", "title": "Dunsan Cafe Boulevard Artisanal Dessert", "detail": "Taste Korean bingsu or specialty hand-drip coffees.", "logistics": "Dunsan central boulevard."},
                {"time": "18:30–21:00", "title": "Daejeon Charcoal-Grilled Freshwater Eel (Jangeo-gui)", "detail": "Savor thick cuts of freshwater eel grilled table-side over charcoal with sweet teriyaki ginger glaze and pickled ginger slivers.", "logistics": "Yuseong / Dunsan eel specialty hall."}
            ],
            [
                {"label": "Bakery Innovation", "text": "DCC branch showcases high-tech modern iterations of Sung Sim Dang's master baking."},
                {"label": "Eel Stamina Banquet", "text": "Freshwater eel provides rich omega-3 nutrients and rich flavor to prepare for coastal Busan."}
            ],
            "Lunch: Sung Sim Dang DCC bakery brunch and freshly pressed fruit juices. Dinner: Table-side charcoal-grilled freshwater eel with seasoned sticky rice.",
            "No reservations needed for DCC bakery; peak hours 12:00–14:00.",
            "Bakery lunch ~₩15,000; Charcoal eel banquet ~₩38,000 per person.",
            "Wrap grilled eel with fresh perilla leaf, sliced garlic, and ginger to balance richness.",
            "DCC complex and eel restaurants are spacious and indoors."
        ),
        # Day 13: Nov 13
        make_day(12, "Busan", "Coastward Rail & Night Market", "Busan · Haeundae Beachfront",
            "KTX Daejeon to Busan (1h30m) → Choryang Milmyeon → Haeundae Market Grilled Clams & Sea Eel",
            "Maritime Arrival, Wheat Noodle Legends & Coastal Street Feasts",
            [
                {"time": "10:00–11:30", "title": "KTX High-Speed Rail to Busan", "detail": "Scenic 90-minute rail journey arriving at Busan Station on the southern sea.", "logistics": "Board train at Daejeon Station."},
                {"time": "11:45–13:15", "title": "Choryang Milmyeon (Busan Wheat Noodle Icon)", "detail": "Taste authentic Busan Milmyeon: cold wheat noodles in chilled spiced broth with cucumber, boiled beef, and hot kettle broth.", "logistics": "Choryang-dong directly opposite Busan Station."},
                {"time": "13:45–15:00", "title": "Metro to Haeundae Beach Base & Check-in", "detail": "Check into Haeundae hotel (e.g. L7 Haeundae or Felix by STX).", "logistics": "Metro Line 2 or taxi along harbor bridge."},
                {"time": "15:30–18:00", "title": "Haeundae Beach Promenade Walk", "detail": "Breathe fresh sea air walking from Dongbaek Island to Haeundae beach.", "logistics": "Paved oceanside walkway."},
                {"time": "18:30–21:30", "title": "Haeundae Traditional Market Feast", "detail": "Sample sizzling grilled sea eel (godeulbaegi), fresh seafood hot pot, Korean tteokbokki, and famous Busan ssiat hotteok (brown sugar seed pancake).", "logistics": "Haeundae Market Gunam-ro lane."}
            ],
            [
                {"label": "Iconic Busan Wheat Noodles", "text": "Milmyeon is Busan's historical Korean War innovation, substituting wheat flour for buckwheat."},
                {"label": "Night Market Vibrancy", "text": "Haeundae Market comes alive at night with smoking street stalls and live seafood tanks."}
            ],
            "Lunch: Choryang Milmyeon (cold wheat noodles & giant steamed mandu). Dinner: Haeundae Market grilled sea eel, seafood pajeon, and ssiat hotteok.",
            "Book KTX Daejeon→Busan on Korail app 30 days prior.",
            "KTX ticket ~₩36,200; Milmyeon ~₩8,500; Market dinner ~₩25,000.",
            "Sea eel is grilled with spicy red pepper sauce; ask for non-spicy salt grill (sogeum-gui) if preferred.",
            "Haeundae market is a covered pedestrian street."
        ),
        # Day 14: Nov 14
        make_day(13, "Busan", "Clam Grills & Raw Fish Skyline", "Busan · Haeundae Beachfront",
            "Cheongsapo Seaside Grilled Clams (Jogae-gui) → Millak Raw Fish Town & Gwangan Drone Show",
            "Ocean Clam Grills, Live Sashimi & Saturday Drones",
            [
                {"time": "10:30–13:30", "title": "Cheongsapo Fishing Village & Grilled Clam Feast", "detail": "Dine in an oceanfront terrace enjoying a giant platter of live scallops, clams, and abalone grilled over briquettes with butter, cheese, and spicy dipping sauce.", "logistics": "Blueline Park Sky Capsule or short taxi to Cheongsapo."},
                {"time": "14:00–16:30", "title": "Cheongsapo Cafe Street & Ocean Skywalk", "detail": "Sip artisanal pour-over coffee overlooking the red & white lighthouses and walk Daritdol Skywalk over the waves.", "logistics": "Cheongsapo waterfront."},
                {"time": "17:00–18:30", "title": "Gwangalli Beach Sunset Walk", "detail": "Watch the sun dip behind Gwangan Suspension Bridge from the sandy beachfront.", "logistics": "Gwangan Station Line 2 Exit 3/5."},
                {"time": "19:00–21:30", "title": "Millak Raw Fish Town & Saturday Night Drone Show", "detail": "Feast on seasonal sliced yellowtail (bangeo) and flounder sashimi with sea views, stepping out onto the sand to watch 500+ synchronized LED drones dance in the night sky.", "logistics": "Millak Raw Fish Tower / Gwangalli Beach (drones at 19:00 & 21:00)."}
            ],
            [
                {"label": "Oceanfront Charcoal Grilling", "text": "Cheongsapo's clam grilling tradition combines crashing waves with buttery charcoal-cooked shellfish."},
                {"label": "Saturday Night Highlight", "text": "Gwangalli drone performance over Gwangan Diamond Bridge is Busan's premier evening spectacle."}
            ],
            "Lunch: Cheongsapo seaside grilled live clams (jogae-gui) with butter and melted cheese. Dinner: Millak Raw Fish Town sliced yellowtail sashimi, abalone, and spicy fish stew.",
            "Book Sky Capsule 14 days in advance on official website.",
            "Clam feast ~₩35,000 per person; Sashimi banquet ~₩40,000 per person.",
            "Clam shells get hot on the grill; use provided cloth gloves and tongs.",
            "Millak raw fish buildings have panoramic glass indoor dining rooms."
        ),
        # Day 15: Nov 15
        make_day(14, "Busan", "Jagalchi Marine Bounty & Night Markets", "Busan · Haeundae Beachfront",
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
        # Day 16: Nov 16
        make_day(15, "Busan", "Giant Snow Crabs & Cliffside Abalone", "Busan · Haeundae Beachfront",
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
        # Day 17: Nov 17
        make_day(16, "Busan", "Historic Scallion Pancakes & Makgeolli", "Busan · Haeundae Beachfront",
            "Dongnae Halmae Pajeon (80-Year Lineage) → Geumjeongsanseong Makgeolli Brewery Tasting",
            "Royal Scallion Pancakes & Mountain Artisanal Rice Wine",
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
        # Day 18: Nov 18
        make_day(17, "Busan", "Heritage Pork Soup & Pojangmacha", "Busan · Haeundae Beachfront",
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
            "Dalmaji Hill Sea-View Teahouses → Cheongsapo Seafood Stew (CSAT Day)",
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
        {"label": "Market & Street Food", "value": "5/5", "tone": "good"},
        {"label": "Regional Specialties", "value": "5/5", "tone": "good"},
        {"label": "Michelin & Heritage", "value": "5/5", "tone": "good"},
        {"label": "Bakery Culture", "value": "5/5", "tone": "good"}
    ]

    return {
        "id": "seoul-daejeon-busan-foodie",
        "shortTitle": "Seoul · Daejeon · Busan (Foodie & Market Trail)",
        "title": "The Great Korean Culinary & Market Trail (Gastronomy & Street Eats)",
        "routeLabel": "Seoul (7N) → Daejeon (5N) → Busan (7N) → Seoul (2N)",
        "badge": "Street Markets & Gourmet Heritage",
        "bestFor": "Passionate food lovers, night market enthusiasts, and culinary adventurers who prioritize authentic regional flavors, Michelin bib gourmands, historic bakeries, and live seafood feasts.",
        "decisionSummary": "An immersive gastronomic expedition linking Seoul's legendary street alleys and Hanwoo beef markets with Daejeon's beloved bakeries and noodle culture, culminating in Busan's world-famous coastal seafood emporiums.",
        "recommendation": "Choose this route if your primary joy in travel is tasting authentic local dishes, exploring bustling night markets, and discovering centuries-old culinary traditions.",
        "tradeoff": "Requires hearty appetite and willingness to navigate lively, bustling market alleys and try authentic fermented and spicy specialties.",
        "scorecard": scorecard,
        "bases": get_sdb_common_bases(),
        "transfers": get_sdb_common_transfers(),
        "budgetScenarios": get_sdb_budget_scenarios(),
        "bookingPriorities": get_sdb_booking_priorities(),
        "days": days
    }
