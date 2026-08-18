#!/usr/bin/env python3
"""Route Blueprint: Seoul · Daejeon · Busan (Active Nature, Thermal Hot Springs & Coastal Ridges)."""

from scripts.generate_all_itineraries import make_day
from scripts.itinerary_builder_sdb import (
    get_sdb_common_bases,
    get_sdb_common_transfers,
    get_sdb_budget_scenarios,
    get_sdb_booking_priorities
)

def get_sdb_wellness():
    days = [
        # Day 1: Nov 1
        make_day(0, "Seoul", "Arrival", "Seoul · Myeongdong / Seoul Station edge",
            "ICN arrival at 21:00 → late transfer → calming herbal tea & deep restorative sleep",
            "Gentle Arrival & Restorative Night Reset",
            [
                {"time": "21:00–22:15", "title": "ICN Arrival & Border Clearance", "detail": "Clear customs smoothly and collect essential connectivity tools.", "logistics": "Terminal 1 or 2."},
                {"time": "22:30–23:45", "title": "Direct Transfer to Central Seoul", "detail": "Airport Limousine Bus or official taxi directly to hotel doorstep.", "logistics": "Minimizes late-night physical strain."},
                {"time": "23:45–00:30", "title": "Warm Herbal Tea & Deep Sleep", "detail": "Hydrate with warm barley or chamomile tea, stretch lightly, and get restorative sleep.", "logistics": "Notify hotel of late arrival."}
            ],
            [
                {"label": "Wellness Priority", "text": "Arrive calmly and protect sleep quality to prepare for invigorating mountain and coastal trails."},
                {"label": "Low-Stress Transfer", "text": "Door-to-door transit prevents fatigue."}
            ],
            "Warm herbal tea and light convenience store fruit or rice snack.",
            "Confirm late check-in with hotel in writing.",
            "Limousine Bus ~₩17,000.",
            "Avoid alcohol and caffeine on arrival night to support circadian rhythm adjustment.",
            "Hotel front desk provides 24-hour check-in."
        ),
        # Day 2: Nov 2
        make_day(1, "Seoul", "Mountain Trails & Urban Foliage", "Seoul · Myeongdong / Seoul Station edge",
            "Namsan Mountain Autumn Trail Hike → N Seoul Tower Overlook → Herbal Ginseng Reset",
            "Pine Ridge Trails, 360° City Vistas & Herbal Revitalization",
            [
                {"time": "09:30–12:30", "title": "Namsan Mountain Southern Forest Trail", "detail": "Hike the paved, pine-shaded mountain trail up Mount Namsan under vibrant yellow and crimson foliage to the summit.", "logistics": "Walk from Myeongdong or take Namsan outdoor trail."},
                {"time": "12:30–14:00", "title": "Namsan Summit Panoramic Lunch", "detail": "Enjoy fresh Korean bibimbap or light dining while taking in 360-degree views over Seoul.", "logistics": "Namsan Tower plaza."},
                {"time": "14:30–16:30", "title": "Namsan Outdoor Botanical Garden & Forest Path", "detail": "Descend via the serene southern botanical garden, featuring wooden boardwalks, wild flower fields, and tranquil ponds.", "logistics": "Hannam-dong descent route."},
                {"time": "17:00–18:30", "title": "Dosan Herbal Spa / Foot Reflexology Experience", "detail": "Rejuvenate walking muscles with a soothing herbal foot bath and pressure point massage.", "logistics": "Apgujeong / Myeongdong wellness lounge."},
                {"time": "19:00–21:00", "title": "Tosokchon Ginseng Chicken Soup (Samgyetang) Dinner", "detail": "Nourish the body with young chicken simmered with whole fresh Korean ginseng root, jujubes, garlic, and glutinous rice.", "logistics": "Tosokchon (Gyeongbokgung Station Line 3 Exit 2)."}
            ],
            [
                {"label": "Natural Acclimatization", "text": "Gentle mountain hiking under autumn leaves circulates blood flow and eliminates jet lag."},
                {"label": "Boyang Herbal Recovery", "text": "Ginseng chicken soup provides warm, easily digestible protein and essential micronutrients."}
            ],
            "Lunch: Namsan summit mountain bibimbap with fresh mountain vegetables. Dinner: Tosokchon authentic Ginseng Chicken Soup (Samgyetang).",
            "Namsan trails are paved and lighted; wear comfortable athletic shoes.",
            "Namsan trail is free; Samgyetang dinner ~₩20,000 per person.",
            "Bring a light layer as summit breezes can feel brisk in November.",
            "N Seoul Tower indoor pavilions provide heated shelter if windy."
        ),
        # Day 3: Nov 3
        make_day(2, "Seoul", "National Park Ridge Hiking", "Seoul · Myeongdong / Seoul Station edge",
            "Bukhansan National Park Scenic Trail → Bukhansanseong Fortress Valley → Traditional Bath",
            "Granite Mountain Ridges & Clean Alpine Valleys",
            [
                {"time": "08:30–13:30", "title": "Bukhansan National Park Trail (Bukhansanseong Valley)", "detail": "Hike along crystal mountain streams, ancient stone temple pavilions, and granite peaks through golden autumn maple forests inside Korea's most visited national park.", "logistics": "Gupabal Station Line 3 Exit 1, then Bus 704 to Bukhansanseong fortress entrance."},
                {"time": "13:30–15:00", "title": "Trailhead Mountain Farmer Lunch", "detail": "Feast on warm country potato pancakes (gamjajeon), fresh acorn jelly salad (dotorimuk), and warm hand-cut noodle soup (kalguksu).", "logistics": "Bukhansan trailhead restaurant village."},
                {"time": "15:30–17:30", "title": "Traditional Korean Jjimjilbang Sauna Reset", "detail": "Soak in heated herbal pools (mugwort and jade) to soothe hiking legs.", "logistics": "Central Seoul traditional bathhouse."},
                {"time": "18:30–20:30", "title": "Nutritious Korean Beef Bulgogi & Ssam Greens Feast", "detail": "Enjoy tender grilled beef wrapped in abundant organic leafy greens, perilla, and crunchy peppers.", "logistics": "Jongno / Myeongdong dining hall."}
            ],
            [
                {"label": "Guinness World Record National Park", "text": "Bukhansan holds the world record for highest visitors per square foot, celebrated for pristine granite topography within city reach."},
                {"label": "Post-Hike Bathing Ritual", "text": "Pairing rigorous mountain trekking with immediate hot herbal bathing is Korea's definitive wellness tradition."}
            ],
            "Lunch: Bukhansan trailhead crispy potato pancakes, acorn jelly, and warm kalguksu. Dinner: Charcoal-grilled beef bulgogi with overflowing fresh organic ssam lettuce basket.",
            "Bukhansan National Park admission is free; open year-round.",
            "Park free; Lunch ~₩15,000; Jjimjilbang ~₩15,000; Dinner ~₩25,000 per person.",
            "Wear sturdy hiking shoes with good tread for granite rock surfaces; bring 1 liter of water.",
            "If weather turns rainy, replace mountain hike with the National Museum of Korea indoor art galleries."
        ),
        # Day 4: Nov 4
        make_day(3, "Seoul", "Forest Bathing & Riverside Reset", "Seoul · Myeongdong / Seoul Station edge",
            "Seoul Forest Autumn Ginkgo Canopy → Han River Eco-Walk → Ttukseom Sunset",
            "Urban Forest Sanctuaries & Riverside Serenity",
            [
                {"time": "10:00–12:30", "title": "Seoul Forest Park Metasequoia & Ginkgo Forest", "detail": "Immerse in forest bathing (Shinrin-yoku) along golden ginkgo paths, visiting the deer corral, eco-forest wetland boardwalks, and tranquil reflecting pond.", "logistics": "Seoul Forest Station Suin-Bundang Line Exit 4."},
                {"time": "12:45–14:15", "title": "Seongsu Organic Farm-to-Table Lunch", "detail": "Dine on organic Korean grain bowls, avocado bibimbap, or artisanal seasonal salads.", "logistics": "Seongsu Yeonmujang-gil dining lane."},
                {"time": "14:30–16:30", "title": "Seongsu Mindful Cafe & Tea Atelier", "detail": "Sip single-origin hand-drip coffee or organic green tea in a spacious, light-filled architectural greenhouse cafe.", "logistics": "Seongsu-dong."},
                {"time": "17:00–19:00", "title": "Ttukseom Hangang Riverside Sunset Walk", "detail": "Stroll along the Han River waterfront as twilight reflects on the water, watching rowers and city lights.", "logistics": "Jayang (Ttukseom Resort) Station Line 7 Exit 2."},
                {"time": "19:30–21:30", "title": "Warm Mushroom Shabu-Shabu Hot Pot Dinner", "detail": "Cook fresh shiitake, enoki, and king oyster mushrooms with thinly sliced beef in light kelp broth.", "logistics": "Seongsu / Central Seoul."}
            ],
            [
                {"label": "Forest Mindful Flow", "text": "Seoul Forest offers 180,000 pyeong of pristine green canopy, restoring mental focus."},
                {"label": "Gentle Pacing", "text": "A flat, unhurried day between mountain hiking excursions."}
            ],
            "Lunch: Seongsu organic farm-to-table grain bowl. Dinner: Mushroom and beef shabu-shabu hot pot with hand-pulled noodles.",
            "Seoul Forest admission is free; open 24/7.",
            "Free park; Lunch ~₩16,000; Dinner ~₩24,000 per person.",
            "Riverside winds can be cool at sunset; carry a windproof jacket.",
            "Insect Garden and Botanical Greenhouse inside Seoul Forest provide indoor warmth."
        ),
        # Day 5: Nov 5
        make_day(4, "Seoul", "Granite Ramparts & Tea Philosophy", "Seoul · Myeongdong / Seoul Station edge",
            "Inwangsan Mountain Sunset Ridge Trail → Cheongun Literature Library Hanok Reading Hall",
            "Ancient Stone Ramparts & Meditative Hanok Libraries",
            [
                {"time": "10:00–12:30", "title": "Cheongun Literature Library & Yun Dong-ju Memorial Hall", "detail": "Read poetry and relax in an authentic wooden hanok library built into the mountain slope with an indoor waterfall garden.", "logistics": "Gyeongbokgung Station Line 3 Exit 3 + Bus 7212 or 15-min walk."},
                {"time": "12:45–14:15", "title": "Seochon Village Traditional Lunch", "detail": "Enjoy buckwheat cold noodles (makguksu) or savory potato pancakes in historic Seochon village.", "logistics": "Seochon dining lane."},
                {"time": "14:30–17:30", "title": "Inwangsan Mountain Granite Ridge Trail", "detail": "Hike along 600-year-old stone fortress walls up Inwangsan's dramatic granite ridges, enjoying unobstructed sunset views over Gyeongbokgung Palace and central Seoul.", "logistics": "Trailhead near Changuimun Gate."},
                {"time": "18:00–19:30", "title": "Seochon Hanok Herbal Teahouse", "detail": "Sip hot ginger jujube tea (daechu-cha) in a peaceful wooden courtyard.", "logistics": "Seochon tea alley."},
                {"time": "20:00–21:30", "title": "Charcoal-Grilled Pork Collar & Aged Kimchi Stew", "detail": "Replenish hiking calories with tender grilled pork and probiotic-rich aged kimchi stew.", "logistics": "Gwanghwamun / Jongno."}
            ],
            [
                {"label": "Panoramic Stone Fortress", "text": "Inwangsan provides the most dramatic golden-hour mountain vista overlooking Seoul's imperial core."},
                {"label": "Hanok Literature Oasis", "text": "Cheongun Literature Library offers a peaceful architectural retreat for contemplative reading."}
            ],
            "Lunch: Seochon buckwheat makguksu and potato pancake. Afternoon: Traditional hot jujube tea. Dinner: Charcoal-grilled pork neck (moksal) with bubbling aged kimchi stew.",
            "Inwangsan trail is free; open 24/7 with wooden steps and illuminated night lights.",
            "Free trail and library; Teahouse ~₩8,000; Dinner ~₩25,000 per person.",
            "Wooden stair sections on Inwangsan are steep; take steady paces.",
            "Cheongun Hanok Library and Seochon cafes provide full shelter."
        ),
        # Day 6: Nov 6
        make_day(5, "Seoul", "Temple Valleys & Hanok Foot Baths", "Seoul · Myeongdong / Seoul Station edge",
            "Jingwansa Temple Mountain Valley Walk → Eunpyeong Hanok Foot Bath Atelier",
            "Sacred Forest Streams, Temple Traditions & Herbal Foot Baths",
            [
                {"time": "09:30–12:30", "title": "Jingwansa Temple (Bukhansan Western Valley)", "detail": "Stroll along serene crystal mountain streams and autumn pines to visit one of Seoul's four historic royal Buddhist temples, famed for traditional temple food preservation.", "logistics": "Yeonsinnae Station Line 3/6 Exit 3 + Bus 7211/701 to Jingwansa entrance."},
                {"time": "12:45–14:15", "title": "Balwoo Temple-Style Vegetarian Lunch", "detail": "Dine on clean, seasonal vegetarian temple dishes prepared with fermented mountain vegetables and wild mushrooms.", "logistics": "Eunpyeong dining area."},
                {"time": "14:30–16:30", "title": "Eunpyeong Hanok Village & Outdoor Foot Bath Cafe", "detail": "Walk through modern hanok residential architecture and enjoy an herbal foot bath overlooking the rocky peaks of Bukhansan.", "logistics": "Adjacent to Jingwansa entrance."},
                {"time": "17:00–18:30", "title": "Bukhansan Autumn Mountain View Stroll", "detail": "Relax along the wooden village promenade.", "logistics": "Eunpyeong village."},
                {"time": "19:30–21:30", "title": "Warm Mandu Jeongol (Dumpling Hot Pot) Dinner", "detail": "Enjoy bubbling handmade vegetable and beef dumpling hot pot with savory broth.", "logistics": "Central Seoul dining room."}
            ],
            [
                {"label": "Spiritual Harmony", "text": "Jingwansa's tranquil mountain stream valley offers complete silence and spiritual restoration."},
                {"label": "Herbal Foot Therapy", "text": "Soaking feet while gazing at Bukhansan's sheer granite cliffs connects bodily healing with natural grandeur."}
            ],
            "Lunch: Eunpyeong clean temple-style vegetarian banquet. Dinner: Steaming handmade mandu jeongol (dumpling hot pot) with organic mushrooms.",
            "Jingwansa Temple is free admission; open year-round.",
            "Temple free; Foot bath cafe ~₩12,000; Dinner ~₩22,000 per person.",
            "Quiet contemplation requested on Jingwansa temple grounds.",
            "Eunpyeong History & Hanok Museum provides indoor exhibits."
        ),
        # Day 7: Nov 7
        make_day(6, "Seoul", "Urban Park Meadows & Train Prep", "Seoul · Myeongdong / Seoul Station edge",
            "Olympic Park Autumn Meadows & World Peace Gate → Bongeunsa Temple Gardens → Sunday KTX Prep",
            "Sprawling Lawns, Ancient Ginkgo Trees & Rail Preparation",
            [
                {"time": "10:00–12:30", "title": "Olympic Park Autumn Meadows & Lone Tree", "detail": "Walk across vast rolling green lawns, view international monumental sculptures, and photograph the iconic Lone Tree on the hillside.", "logistics": "Olympic Park Station Line 5/9 Exit 3."},
                {"time": "12:45–14:00", "title": "Jamsil Gourmet Lunch", "detail": "Enjoy fresh Korean bibimbap or light noodles near the park lake.", "logistics": "Jamsil / Bangi-dong food alley."},
                {"time": "14:30–16:30", "title": "Bongeunsa Temple Meditation Walk", "detail": "Walk the tranquil pine forest paths behind Bongeunsa Temple in Gangnam, listening to wooden wind chimes.", "logistics": "Bongeunsa Station Line 9 Exit 1."},
                {"time": "17:00–18:30", "title": "Seoul Hotel Packing & Train Verification", "detail": "Return to Myeongdong / Seoul Station base, organize luggage for tomorrow's KTX to Daejeon, and verify seat bookings.", "logistics": "Seoul Station hotel."},
                {"time": "19:00–21:00", "title": "Nourishing Korean Hanwoo Beef Gomtang Dinner", "detail": "Enjoy rich, clear slow-simmered beef brisket soup with rice.", "logistics": "Hadongkwan or local gourmet soup hall."}
            ],
            [
                {"label": "Expansive Green Spaces", "text": "Olympic Park provides vast flat walking lawns, gentle on the joints before rail travel."},
                {"label": "Transit Assurance", "text": "Early evening packing guarantees a seamless Sunday departure to Daejeon."}
            ],
            "Lunch: Jamsil fresh dolsot bibimbap. Dinner: Hadongkwan traditional Hanwoo beef gomtang soup with scallions.",
            "Olympic Park and Bongeunsa Temple are free admission.",
            "Free park and temple; Dinner ~₩20,000 per person.",
            "Olympic Park is vast; rent a 4-wheel pedal carriage or take park tram if preferred.",
            "Coex Mall and Olympic Museum provide indoor shelter."
        ),
        # Day 8: Nov 8
        make_day(7, "Daejeon", "City Transition & Thermal Springs", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Morning KTX to Daejeon (55 mins) → Yuseong Outdoor Hot Spring Foot Bath Park → Hotel Onoma Pool & Spa",
            "High-Speed Rail into Korea's Premier Thermal Oasis",
            [
                {"time": "09:30–10:30", "title": "KTX High-Speed Rail Seoul to Daejeon", "detail": "55-minute smooth train transit from Seoul Station to Daejeon Station.", "logistics": "Direct Gyeongbu line."},
                {"time": "11:00–13:00", "title": "Sung Sim Dang 1956 Bakery & Clean Brunch", "detail": "Sample light sourdough breads, walnut rye, and fresh fruit tarts in Daejeon's historic center.", "logistics": "Jungangno Station Line 1 Exit 2."},
                {"time": "13:30–15:30", "title": "Hotel Check-in & Yuseong Thermal Spa Base", "detail": "Check into Daejeon wellness base (e.g. Hotel Onoma or Ramada Yuseong) and unpack.", "logistics": "Metro Line 1 to Yuseong Spa Station."},
                {"time": "16:00–18:00", "title": "Yuseong Hot Springs Outdoor Foot Bath Park", "detail": "Soak feet in 100% natural 42°C alkaline mineral waters under autumn trees in the landscaped public hot spring park.", "logistics": "Yuseong Spa Station Exit 7 (free public facility)."},
                {"time": "18:30–21:00", "title": "Yuseong Perilla Duck Stew (Boyang Oritang) Dinner", "detail": "Nourish the body with simmered duck stew rich in omega fatty acids and toasted perilla seed broth.", "logistics": "Yuseong Hot Springs dining quarter."}
            ],
            [
                {"label": "Natural Thermal Heritage", "text": "Yuseong Hot Springs has been celebrated for healing mineral waters since the Baekje Kingdom and Joseon Dynasty."},
                {"label": "Seamless Rail Transition", "text": "Arriving by 10:30 allows a leisurely afternoon soak without rush."}
            ],
            "Lunch: Sung Sim Dang artisan bakery brunch. Dinner: Yuseong rich Oritang duck stew with toasted perilla seeds and minari greens.",
            "Book KTX train 30 days prior on Korail app.",
            "KTX ticket ~₩23,700; Foot bath is free; Dinner ~₩25,000 per person.",
            "Bring a small towel for drying feet at Yuseong outdoor foot bath park.",
            "Hotel Onoma indoor pool and thermal sauna provide luxury covered wellness."
        ),
        # Day 9: Nov 9
        make_day(8, "Daejeon", "Barefoot Earthing & Clay Healing", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Gyejoksan Mountain 14.5km Barefoot Red Clay Trail (Earthing Therapy) → Acorn Jelly Mountain Feast",
            "Natural Red Clay Earthing & Forest Negative Ions",
            [
                {"time": "09:00–13:30", "title": "Gyejoksan Mountain Barefoot Red Clay Trail", "detail": "Walk barefoot along 14.5km of soft, smooth natural red clay spread along scenic mountain slopes up to Gyejoksanseong stone fortress, absorbing negative ions and forest phytoncides.", "logistics": "City Bus 74 or 25-min taxi to Jangdong forest entrance."},
                {"time": "13:30–15:00", "title": "Trailhead Village Acorn Jelly & Potato Pancake Lunch", "detail": "Feast on freshly seasoned dotorimuk (acorn jelly salad), golden potato pancakes, and wild herb bibimbap.", "logistics": "Jangdong trailhead rustic lodge."},
                {"time": "15:30–18:00", "title": "Yuseong Mineral Thermal Bathhouse Full Soak", "detail": "Immerse in mineral hot spring baths to relax foot soles and calf muscles after barefoot earthing.", "logistics": "Yuseong Hotel Onsen bathhouse."},
                {"time": "18:30–20:30", "title": "Daejeon Charcoal-Grilled Freshwater Eel Feast", "detail": "Replenish stamina with premium freshwater eel grilled over charcoal with ginger and sesame oil.", "logistics": "Yuseong / Dunsan dining street."}
            ],
            [
                {"label": "Korea's Master Earthing Trail", "text": "Gyejoksan's red clay trail is globally celebrated for stimulating acupressure points and reducing bodily inflammation."},
                {"label": "Complete Mineral Recovery", "text": "Post-hike Yuseong mineral bath locks in deep physical relaxation."}
            ],
            "Lunch: Jangdong rustic acorn jelly salad, potato pancake, and wild herb bibimbap. Dinner: Charcoal-grilled freshwater eel with sweet ginger soy glaze.",
            "Clean tap water wash stations available at Gyejoksan trail start/finish.",
            "Trail is free; Hot spring bath ~₩10,000; Dinner ~₩35,000 per person.",
            "Wear shoes easy to slip on and off; small foot towel recommended.",
            "If rainy, replace hiking with indoor full-day thermal spa at Yuseong."
        ),
        # Day 10: Nov 10
        make_day(9, "Daejeon", "Canopy Skywalks & Forest Bathing", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Jangtaesan Metasequoia Forest Canopy Skywalk → Forest Bathing Walk",
            "Soaring 30-Meter Metasequoias & Suspension Bridges",
            [
                {"time": "09:30–13:00", "title": "Jangtaesan Recreational Metasequoia Forest", "detail": "Walk through Korea's only pure metasequoia forest, traverse the elevated canopy skywalk bridge 15 meters above ground, and climb the wooden sky tower for sweeping autumn views.", "logistics": "City Bus 20 or 35-min taxi to Jangan-dong."},
                {"time": "13:15–14:45", "title": "Lakeside Village Chicken Stew Lunch", "detail": "Dine on hearty country chicken and wild mushroom stew (dakbokkeumtang) in a cozy forest cabin.", "logistics": "Jangan-dong village dining cabins."},
                {"time": "15:15–17:30", "title": "Jangtaesan Forest Meditation Trail", "detail": "Follow the wooden boardwalk around the serene forest reservoir and forest bathing therapy zone.", "logistics": "Forest reservoir trail."},
                {"time": "18:00–19:30", "title": "Yuseong Evening Foot Bath & Relaxation", "detail": "Soak feet in warm thermal waters.", "logistics": "Yuseong Spa Park."},
                {"time": "20:00–21:30", "title": "Daejeon Clam Kalguksu & Boiled Pork Suyuk", "detail": "Enjoy light, mineral-rich hand-cut clam noodle soup and lean boiled pork.", "logistics": "Dunsan / Yuseong."}
            ],
            [
                {"label": "Forest Phytoncide Therapy", "text": "Jangtaesan's dense metasequoia grove emits high concentrations of natural terpenes that lower stress hormone levels."},
                {"label": "Elevated Forest Perspective", "text": "The canopy skywalk puts you directly within the golden autumn tree crowns."}
            ],
            "Lunch: Jangtaesan rustic spicy chicken and wild mushroom stew. Dinner: Daejeon hand-cut clam kalguksu with lean boiled pork suyuk.",
            "Jangtaesan Forest and Skywalk are free admission; open 09:00–17:00.",
            "Forest entry is free; Taxi ~₩25,000 each way; Dinner ~₩22,000 per person.",
            "Hold handrails on the canopy suspension bridge in windy conditions.",
            "Forest information center and mountain cafes provide covered shelter."
        ),
        # Day 11: Nov 11
        make_day(10, "Daejeon", "Lakeside Eco-Trails & Botanical Gardens", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Daecheongho Lake Eco-Boardwalk Trail → Hanbat Botanical Arboretum",
            "Shimmering Waters, Autumn Reed Fields & Tropical Conservatories",
            [
                {"time": "09:30–12:30", "title": "Daecheongho Lake Waterfront Eco-Trail", "detail": "Walk the wooden boardwalk trails along vast Daecheongho Lake, capturing shimmering water reflections, autumn reed fields, and serene bird sanctuaries.", "logistics": "Daecheong Dam Water Culture Center."},
                {"time": "12:45–14:15", "title": "Lakeside Freshwater Fish Soup Lunch", "detail": "Enjoy light, mineral-rich spicy freshwater minnow soup (maeuntang) or grilled fish set.", "logistics": "Daecheong Dam restaurant row."},
                {"time": "14:45–17:00", "title": "Hanbat Arboretum Tropical Botanical Conservatory", "detail": "Stroll the lush, heated indoor tropical greenhouse filled with mangrove ecosystems and rare palms, followed by the golden East Garden metasequoia trail.", "logistics": "Govt Complex Daejeon Station Line 1."},
                {"time": "17:30–19:30", "title": "Daejeon Shinsegae Sky Garden Sunset", "detail": "Take in river valley views from the 38th-floor observation terrace.", "logistics": "Hotel Onoma complex."},
                {"time": "20:00–21:30", "title": "Daejeon Clay Pot Hanwoo Bulgogi Dinner", "detail": "Savor thinly sliced marinated beef with organic enoki mushrooms.", "logistics": "Dunsan dining street."}
            ],
            [
                {"label": "Lakeside Mindfulness", "text": "Daecheongho Lake offers miles of tranquil, uncrowded water-edge boardwalks."},
                {"label": "Botanical Warmth", "text": "Tropical greenhouse provides a comforting, humid botanical oasis in November."}
            ],
            "Lunch: Daecheong Dam freshwater fish stew or grilled trout. Dinner: Sizzling earthenware pot Hanwoo beef bulgogi with seasonal mountain roots.",
            "Hanbat Arboretum and Tropical Conservatory are free admission.",
            "Arboretum free; Sky lounge coffee ~₩6,500; Dinner ~₩25,000 per person.",
            "Bring binoculars if interested in seasonal migratory water birds at Daecheongho.",
            "Tropical Conservatory and Shinsegae complex are completely enclosed."
        ),
        # Day 12: Nov 12
        make_day(11, "Daejeon", "Riverside Cycling & Hot Spring Finale", "Daejeon · Yuseong Hot Springs / Dunsan",
            "Gapcheon River Eco-Walk / Tashu Bikeshare → Full Yuseong Thermal Spa Reset",
            "Riverbank Breezes, Public Bikeshare & Pre-Busan Reset",
            [
                {"time": "10:00–12:30", "title": "Gapcheon River Trail & Tashu City Bikeshare", "detail": "Enjoy a gentle autumn cycle or walk along the wide paved riverside paths of Gapcheon River, passing Hanbit Tower and reed beds.", "logistics": "Tashu public bikeshare stations located throughout riverside."},
                {"time": "12:45–14:15", "title": "Dunsan Cafe Boulevard Healthy Brunch", "detail": "Enjoy fresh avocado toast, ricotta salad, and fresh cold-pressed juice.", "logistics": "Dunsan central lane."},
                {"time": "14:30–17:30", "title": "Grand Yuseong Thermal Hot Spring Spa Bath", "detail": "Comprehensive mineral hot spring soak and body scrub to achieve peak physical relaxation.", "logistics": "Yuseong Onsen bathhouse."},
                {"time": "18:00–19:30", "title": "Sung Sim Dang DCC Fresh Pastry Curation", "detail": "Select fresh whole wheat breads and pastries for tomorrow's KTX train to Busan.", "logistics": "DCC branch 1F."},
                {"time": "20:00–21:30", "title": "Daejeon Farewell Hanwoo Barbecue Dinner", "detail": "Celebrate 5 nights in Daejeon with charcoal-grilled Hanwoo beef.", "logistics": "Yuseong / Dunsan."}
            ],
            [
                {"label": "Active Riverside Flow", "text": "Gapcheon River trail provides flat, scenic cycling with Korea's convenient Tashu bikeshare system."},
                {"label": "Pre-Coastal Renewal", "text": "Full thermal hot spring reset leaves body limber and refreshed for Busan's coastal ridges."}
            ],
            "Lunch: Dunsan healthy brunch salad and cold-pressed juice. Dinner: Charcoal-grilled Hanwoo beef tenderloin with aged doenjang stew.",
            "Tashu bikeshare is free for first 60 minutes via mobile app.",
            "Bikeshare free/minimal; Hot spring ~₩10,000; Hanwoo dinner ~₩45,000 per person.",
            "Pack primary bags tonight for Friday morning KTX to Busan.",
            "Hotel Onoma indoor fitness center and Yuseong spas are weatherproof."
        ),
        # Day 13: Nov 13
        make_day(12, "Busan", "Coastward Rail & Beachfront Earthing", "Busan · Haeundae Beachfront",
            "KTX Daejeon to Busan (1h30m) → Haeundae Beach Earthing Walk → Dongbaek Island Pines",
            "High-Speed Coastal Arrival, Sea Air & Pine Forest Trails",
            [
                {"time": "10:00–11:30", "title": "KTX High-Speed Rail to Busan", "detail": "90-minute comfortable train journey down to Busan Station on the southern coast.", "logistics": "Board train at Daejeon Station."},
                {"time": "11:45–13:15", "title": "Busan Station Choryang Milmyeon Lunch", "detail": "Enjoy refreshing cold wheat noodles in chilled spiced broth.", "logistics": "Opposite Busan Station."},
                {"time": "13:45–15:00", "title": "Transfer to Haeundae Oceanfront Base", "detail": "Check into Haeundae hotel (e.g. L7 Haeundae or Signiel Busan).", "logistics": "Metro Line 2 or taxi across harbor bridge."},
                {"time": "15:30–18:00", "title": "Haeundae Beachfront Barefoot Earthing Walk", "detail": "Walk barefoot along the soft white sand of Haeundae Beach, absorbing negative ions from ocean surf, and loop the pine-scented Dongbaek Island boardwalk to APEC House.", "logistics": "Paved and sandy coastal promenade."},
                {"time": "18:30–21:00", "title": "Haeundae Fresh Seafood & Vegetable Hot Pot", "detail": "Dine on clear blue crab, clam, and abalone hot pot (haemultang) with organic vegetables.", "logistics": "Haeundae market dining lane."}
            ],
            [
                {"label": "Ocean Earthing", "text": "Walking barefoot on wet ocean sand is one of the most effective natural grounding therapies known."},
                {"label": "Coastal Base", "text": "Haeundae provides seven nights of clean maritime air and direct beach access."}
            ],
            "Lunch: Choryang Milmyeon (cold wheat noodles with steamed mandu). Dinner: Haeundae clear seafood hot pot with abalone, clams, and blue crab.",
            "Book KTX Daejeon→Busan on Korail app 30 days prior.",
            "KTX ticket ~₩36,200; Beach and Dongbaek trail are free.",
            "Dongbaek Island trail is lighted at night; APEC Nurimaru House closes at 17:00.",
            "SEA LIFE Busan Aquarium on Haeundae beachfront provides indoor marine exhibits."
        ),
        # Day 14: Nov 14
        make_day(13, "Busan", "Dramatic Coastal Cliff Trekking", "Busan · Haeundae Beachfront",
            "Igidae Coastal Cliff Trail → Oryukdo Glass Skywalk → Saturday Drone Show",
            "Volcanic Sea Cliffs, Skywalks & Evening Light Spectacles",
            [
                {"time": "09:30–13:30", "title": "Igidae Coastal Cliff Trail Trekking", "detail": "Hike the 4.7km rugged coastal trail carved into volcanic cliff faces, suspended above crashing waves with panoramic views across the bay to Haeundae skyline.", "logistics": "Dongsaengmal entrance; Bus 20/22/39 or taxi."},
                {"time": "13:30–15:00", "title": "Oryukdo Seafood Kalguksu Lunch", "detail": "Enjoy warm seafood noodle soup and fresh steamed dumplings overlooking the five rocky islets of Oryukdo.", "logistics": "Oryukdo tourist pavilion."},
                {"time": "15:15–16:30", "title": "Oryukdo Glass Skywalk", "detail": "Step onto the transparent U-shaped glass platform hanging 35 meters over roaring coastal waves.", "logistics": "Free admission (shoe covers provided)."},
                {"time": "17:00–18:30", "title": "Gwangalli Beach Sunset Walk", "detail": "Stroll the sandy shore as Gwangan Bridge lights up in evening twilight.", "logistics": "Gwangan Station Line 2."},
                {"time": "19:00–21:30", "title": "Millak Raw Fish Feast & Saturday Drone Show", "detail": "Savor sliced seasonal yellowtail sashimi and watch 500+ synchronized LED drones dance above Gwangan Bridge.", "logistics": "Millak Raw Fish Tower / Gwangalli Beach (drones at 19:00 & 21:00)."}
            ],
            [
                {"label": "Pristine Coastal Topography", "text": "Igidae is Busan's premier geological coastal trek, combining wild sea cliffs with panoramic city views."},
                {"label": "Saturday Drone Magic", "text": "Timed specifically for Saturday evening to experience Gwangalli's illuminated drone performance."}
            ],
            "Lunch: Oryukdo Haemul Kalguksu (rich seafood noodle soup). Dinner: Millak Raw Fish Town fresh yellowtail sashimi, butter-grilled abalone, and spicy maeuntang.",
            "Oryukdo Skywalk open 09:00–18:00; admission is free.",
            "Trail and Skywalk free; Kalguksu ~₩10,000; Sashimi dinner ~₩40,000 per person.",
            "Igidae trail has wooden stairs and suspension bridges; wear athletic/trail shoes.",
            "Millak indoor restaurants have panoramic glass windows overlooking Gwangan Bridge."
        ),
        # Day 15: Nov 15
        make_day(14, "Busan", "Luxury Thermal Bathhouse Sanctuary", "Busan · Haeundae Beachfront",
            "Centum City Spa Land (18 Mineral Pools & 13 Saunas) → Shinsegae Gourmet Hall",
            "Deep Thermal Hydrotherapy & Luxury Sauna Healing",
            [
                {"time": "09:30–14:00", "title": "Spa Land Centum City Luxury Thermal Bathhouse", "detail": "Spend 4 full hours immersed in 18 natural hot spring pools drawn from two distinct underground mineral sources (sodium bicarbonate and sodium chloride), rotating through 13 themed saunas (Himalayan salt room, Roman steam, Finnish sauna, charcoal room, ice room) and relaxing on heated outdoor foot pools.", "logistics": "Centum City Station Line 2 direct basement connection."},
                {"time": "14:00–15:30", "title": "Shinsegae Centum Gourmet Hall Lunch", "detail": "Enjoy restorative Korean cold noodles, abalone bibimbap, or organic soft tofu stew.", "logistics": "Shinsegae Centum City B1."},
                {"time": "16:00–18:00", "title": "APEC Naru Waterfront Park Stroll", "detail": "Gentle digestive walk along Suyeong River tree-lined paths.", "logistics": "Adjacent to Centum City."},
                {"time": "18:30–20:30", "title": "Marine City Sunset & The Bay 101", "detail": "Photograph glittering glass skyscrapers reflecting across harbor waters.", "logistics": "Dongbaek Station Exit 1."},
                {"time": "20:30–22:00", "title": "Gourmet Korean Fried Chicken & Craft Beer", "detail": "Light evening meal on Haeundae avenue.", "logistics": "Haeundae Gunam-ro."}
            ],
            [
                {"label": "Pinnacle of Asian Hydrotherapy", "text": "Spa Land is universally regarded as one of the world's most luxurious and complete urban hot spring facilities."},
                {"label": "Complete Body Reset", "text": "Thermal minerals deep-clean pores, detoxify muscles, and reset metabolic rhythm."}
            ],
            "Lunch: Shinsegae Centum City abalone bibimbap and organic tofu stew. Dinner: The Bay 101 light dining / Haeundae artisanal Korean fried chicken.",
            "Spa Land 4-hour pass ~₩20,000–₩23,000 (purchased at entrance).",
            "Spa Land ~₩23,000; Lunch ~₩18,000; Dinner ~₩20,000 per person.",
            "Spa Land does not admit children under 7; maintains quiet, serene spa etiquette.",
            "This entire day is 100% weather-proof and indoor climate-controlled."
        ),
        # Day 16: Nov 16
        make_day(15, "Busan", "Marine Gondolas & Over-Water Trails", "Busan · Haeundae Beachfront",
            "Songdo Marine Cable Car (Crystal Gondola) → Songdo Cloud Trails → Amnam Coastal Forest",
            "Over-Water Aerial Gondolas & Coastal Pine Forests",
            [
                {"time": "09:30–12:30", "title": "Songdo Marine Cable Car (Air Cruise)", "detail": "Glide 86 meters above the open sea in a glass-bottom Crystal Cabin gondola across Songdo Bay, taking in aerial views of incoming ocean vessels and rocky headlands.", "logistics": "Songdo Bay Station; bus or taxi from Haeundae."},
                {"time": "12:30–14:00", "title": "Amnam Park Coastal Grilled Seafood Lunch", "detail": "Dine on fresh grilled scallops and shrimp at Amnam Park seaside pavilion.", "logistics": "Amnam Park station."},
                {"time": "14:15–16:30", "title": "Songdo Cloud Trails & Amnam Forest Boardwalk", "detail": "Walk the 365-meter curved glass skywalk over breaking ocean waves and explore the forested walking trails of Amnam Park.", "logistics": "Songdo Beach waterfront."},
                {"time": "17:00–18:30", "title": "Huinnyeoul Coastal Tunnel Sunset", "detail": "Walk the coastal cliff path and illuminated sea tunnel on Yeongdo.", "logistics": "Yeongdo coastal bus."},
                {"time": "19:30–21:30", "title": "Traditional Busan Dwaeji Gukbap Dinner", "detail": "Enjoy nourishing 24-hour pork bone soup with chives and rice.", "logistics": "Nampo / Choryang soup alley."}
            ],
            [
                {"label": "Ocean Gondola Perspectives", "text": "Songdo Cable Car offers thrilling aerial sea vistas without strenuous climbing."},
                {"label": "Over-Water Glass Skywalks", "text": "Songdo Cloud Trails allow you to watch ocean waves churn directly beneath your feet."}
            ],
            "Lunch: Amnam Park seaside grilled scallops and buttered shrimp. Dinner: Traditional Busan Dwaeji Gukbap (pork bone soup) with boiled suyuk.",
            "Songdo Cable Car Crystal Cabin ₩22,000 round-trip.",
            "Cable Car ₩22,000; Skywalk free; Lunch ~₩25,000; Dinner ~₩12,000 per person.",
            "Sea winds on the skywalk can be brisk; wear a windbreaker.",
            "Songdo Cable Car operates in light rain; indoor cafes available at both stations."
        ),
        # Day 17: Nov 17
        make_day(16, "Busan", "Mountain Cable Cars & Ancient Onsen", "Busan · Haeundae Beachfront",
            "Geumgang Park Ropeway Cable Car → Geumjeongsanseong Mountain Wall → Oncheonjang Hot Springs",
            "Mountain Peak Cable Cars & Historic Silla Onsen",
            [
                {"time": "09:30–12:30", "title": "Geumgang Park Ropeway Cable Car", "detail": "Ascend Mount Geumjeong via scenic ropeway cable car, hiking the gentle pine forest path along ancient granite fortress ramparts with sweeping views over Busan.", "logistics": "Oncheonjang Station Line 1 Exit 1, 10-min walk to Geumgang Park."},
                {"time": "12:45–14:15", "title": "Dongnae Halmae Pajeon (Busan Cultural Asset #1) Lunch", "detail": "Feast on 80-year-old royal scallion seafood pancake with Geumjeongsanseong mountain makgeolli.", "logistics": "Dongnae-gu Myeongnyun-dong."},
                {"time": "14:45–17:30", "title": "Oncheonjang Natural Mineral Hot Spring Bath", "detail": "Soak in Korea's oldest recorded natural hot springs (used since the 7th century Silla era), rich in magnesium and silica.", "logistics": "Oncheonjang Spa complex (Hurshimchung / Onsen)."},
                {"time": "18:00–19:30", "title": "Oncheoncheon Stream Eco-Walk", "detail": "Walk the landscaped urban stream path.", "logistics": "Oncheonjang Station."},
                {"time": "20:00–21:30", "title": "Dongnae Boiled Pork Suyuk & Kimchi Feast", "detail": "Enjoy tender boiled pork belly slices with fresh oyster kimchi.", "logistics": "Dongnae dining quarter."}
            ],
            [
                {"label": "Ancient Thermal Heritage", "text": "Oncheonjang is Korea's historic spa capital, celebrated for curing muscular fatigue for over 1,300 years."},
                {"label": "Mountain Cable Car Ease", "text": "Ropeway provides mountain views without intense physical strain."}
            ],
            "Lunch: Dongnae Halmae Pajeon (scallion seafood pancake) with Geumjeongsanseong makgeolli. Dinner: Dongnae pork suyuk and seasoned mountain roots.",
            "Geumgang Ropeway round-trip ₩11,000; Hurshimchung Hot Spring bath ~₩15,000.",
            "Ropeway ₩11,000; Spa ~₩15,000; Lunch ~₩25,000 per person.",
            "Hurshimchung spa includes colossal glass dome ceiling with natural daylight pools.",
            "Hurshimchung thermal spa facility is 100% indoor."
        ),
        # Day 18: Nov 18
        make_day(17, "Busan", "Gentle Beach Strolls & Tea Meditation", "Busan · Haeundae Beachfront",
            "Songjeong Beach Gentle Stroll → Haedong Yonggungsa Seaside Temple → Dalmaji Hill Teahouse",
            "Clean Coastal Surf, Seaside Sanctuaries & Ocean Teahouses",
            [
                {"time": "09:30–11:30", "title": "Songjeong Beach Scenic Coastal Stroll", "detail": "Walk the wide, quiet sands of Songjeong Beach, watching surfers catch clean autumn waves and exploring Jukdo Park pine pavilion.", "logistics": "Bus 100/181 from Haeundae or Blueline Beach Train."},
                {"time": "11:45–13:15", "title": "Haedong Yonggungsa Temple (Temple by the Sea)", "detail": "Visit the 1376 Buddhist cliffside sanctuary listening to rhythmic ocean waves crashing on the rocks below.", "logistics": "Short bus or taxi from Songjeong."},
                {"time": "13:30–15:00", "title": "Gijang Coastal Abalone Porridge (Jeonbok-juk) Lunch", "detail": "Enjoy thick, emerald-green abalone porridge simmered with whole abalone entrails and sesame oil.", "logistics": "Yeonhwa-ri seaside village."},
                {"time": "15:30–18:00", "title": "Dalmaji Hill Pine Forest Walk & Ocean Teahouse", "detail": "Stroll along Dalmaji-gil (Moontan Road) and sip traditional green tea overlooking the sunset sea.", "logistics": "Dalmaji Hill teahouse."},
                {"time": "18:30–21:00", "title": "Haeundae Charcoal Pork Galbi BBQ Dinner", "detail": "Enjoy sweet soy-marinated pork galbi grilled over real wood charcoal.", "logistics": "Haeundae dining lane."}
            ],
            [
                {"label": "Soothing Maritime Rhythms", "text": "Songjeong and Dalmaji offer serene oceanfront environments far from urban traffic noise."},
                {"label": "Nutrient-Dense Coastal Cuisine", "text": "Emerald abalone porridge delivers rich oceanic minerals and gentle digestion."}
            ],
            "Lunch: Yeonhwa-ri traditional abalone porridge (jeonbok-juk). Afternoon: Traditional Korean green tea. Dinner: Haeundae charcoal-grilled marinated pork galbi with cold noodles.",
            "Haedong Yonggungsa is free entry; open year-round from dawn to dusk.",
            "Temple free; Abalone lunch ~₩15,000; Teahouse ~₩8,000; Dinner ~₩25,000 per person.",
            "Wear shoes with good traction on Yonggungsa's stone steps down to the sea.",
            "Dalmaji teahouses and Haeundae restaurants provide comfortable indoor spaces."
        ),
        # Day 19: Nov 19
        make_day(18, "Busan", "Low-Stakes Beachfront Mindful Reset (CSAT Day)", "Busan · Haeundae Beachfront",
            "Haeundae Beach Pine Stroll → Sea-View Herbal Tea Atelier (CSAT Day)",
            "Mindful Waves, Pine Scents & Peaceful Farewell (CSAT / Suneung Day)",
            [
                {"time": "10:30–12:30", "title": "Haeundae Beach & Dongbaek Island Pine Loop", "detail": "Gentle, unhurried walk along Haeundae beach boardwalk and through pine-forested Dongbaek Island.", "logistics": "Direct walk from hotel."},
                {"time": "12:45–14:15", "title": "Haeundae Organic Grain Bowl & Seafood Lunch", "detail": "Enjoy fresh seasonal seafood bibimbap or light abalone soup.", "logistics": "Haeundae beachfront dining."},
                {"time": "14:30–17:00", "title": "Sea-View Tea Atelier & Foot Relaxation", "detail": "Sip artisanal herbal teas while gazing out over the sparkling Korea Strait, reflecting on 7 restorative Busan nights.", "logistics": "Dalmaji / Haeundae ocean-view lounge."},
                {"time": "17:30–19:00", "title": "Sunset Beach Contemplation", "detail": "Watch the golden sun dip below the coastal horizon from Haeundae sands.", "logistics": "Haeundae beachfront."},
                {"time": "19:30–21:30", "title": "Busan Farewell Feast: Hanwoo Beef Barbecue", "detail": "Celebrate final night in Busan with premium charcoal-grilled Korean Hanwoo beef tenderloin.", "logistics": "Haeundae Somunnan Amso Galbi."}
            ],
            [
                {"label": "CSAT Low-Stakes Alignment", "text": "Nov 19 national CSAT exam day is kept 100% localized on Haeundae beachfront to avoid any transit hold zones."},
                {"label": "Mindful Coastal Completion", "text": "Leaves the traveler deeply rested and physically restored for Friday's return to Seoul."}
            ],
            "Lunch: Haeundae fresh abalone soup and vegetable bibimbap. Afternoon: Artisanal Korean herbal tea. Dinner: Haeundae Hanwoo beef short ribs with potato noodles.",
            "Haeundae Somunnan Amso Galbi: arrive by 17:30 to avoid queues.",
            "Lunch ~₩18,000; Farewell Hanwoo dinner ~₩48,000 per person.",
            "Keep evening calm; pack primary bags for Friday morning KTX to Seoul.",
            "Haeundae beachfront indoor cafes offer heated panoramic sea views."
        ),
        # Day 20: Nov 20
        make_day(19, "Seoul", "Capital Return & Sky Garden", "Seoul · Seoul Station / Myeongdong",
            "Morning KTX Busan to Seoul → Seoullo 7017 Sky Garden Walk → Restorative Dinner",
            "Capital Return & Elevated Urban Botanical Garden",
            [
                {"time": "09:30–10:15", "title": "Busan Station Departure", "detail": "Check out of Haeundae hotel, take taxi or metro to Busan Station, and board direct KTX.", "logistics": "Board train 10 minutes prior to departure."},
                {"time": "10:30–12:45", "title": "KTX High-Speed Rail to Seoul", "detail": "2-hour 15-minute smooth train transit back to Seoul Station.", "logistics": "Direct arrival inside Seoul Station concourse."},
                {"time": "13:00–14:30", "title": "Seoul Station Hotel Check-in & Lunch", "detail": "Check into Seoul Station hotel base and enjoy warm Korean beef soup.", "logistics": "Drop bags at hotel doorstep."},
                {"time": "15:00–17:30", "title": "Seoullo 7017 Elevated Sky Garden Walk", "detail": "Walk the 1km transformed highway overpass landscaped with 24,000 Korean trees, shrubs, and flowers, connecting Seoul Station to Namdaemun.", "logistics": "Direct elevated walkway from Seoul Station."},
                {"time": "18:30–21:00", "title": "Nourishing Hanwoo Beef Brisket & Doenjang Stew", "detail": "Enjoy slow-simmered beef brisket stew with fermented soybean paste and barley rice.", "logistics": "Central Seoul dining room."}
            ],
            [
                {"label": "Strategic Departure Security", "text": "Arriving in Seoul on Friday eliminates all risk of KTX weekend disruption before Sunday flight."},
                {"label": "Botanical Sky Garden", "text": "Seoullo 7017 offers a pleasant, elevated urban nature stroll directly outside your hotel."}
            ],
            "Lunch: Seoul Station traditional beef gomtang soup. Dinner: Sizzling Hanwoo beef brisket with aged doenjang stew and barley rice.",
            "Book KTX Busan→Seoul 30 days in advance on Korail app.",
            "KTX ticket ~₩59,800; Seoullo 7017 is free; Dinner ~₩25,000 per person.",
            "Friday afternoon KTX trains sell out fast; reserve morning seat.",
            "Lotte Mart and Seoul Station concourse are completely enclosed."
        ),
        # Day 21: Nov 21
        make_day(20, "Seoul", "Herbal Teas, Gifts & Farewell Banquet", "Seoul · Seoul Station / Myeongdong",
            "Namsan Pine Walk → Seoul Station Lotte Mart Herbal Gifts → Grand Hanwoo Farewell Feast",
            "Ginseng & Tea Curation & Grand Farewell Feast",
            [
                {"time": "09:30–12:00", "title": "Namsan Outdoor Pine Forest Morning Stroll", "detail": "Gentle morning walk under pine trees to breathe crisp autumn mountain air.", "logistics": "Myeongdong / Namsan park trail."},
                {"time": "12:30–15:00", "title": "Seoul Station Lotte Mart Wellness Gift Curation", "detail": "Curate Korean wellness treasures: 6-year-old red ginseng extract (Hongsam), organic green tea from Boseong, toasted seaweed (gim), and dried persimmons with instant tax refund.", "logistics": "Lotte Mart 2F immediate tax refund counter."},
                {"time": "15:30–18:00", "title": "Luggage Packing & Scale Check", "detail": "Pack items safely into luggage, weigh bags at hotel front desk, and complete airline online check-in.", "logistics": "Hotel room."},
                {"time": "18:30–21:30", "title": "Grand Wellness Finale: Premium Hanwoo Barbecue Banquet", "detail": "Celebrate 21 nights of active wellness and thermal rejuvenation with charcoal-grilled Hanwoo beef tenderloin, cold naengmyeon noodles, and aged plum wine.", "logistics": "Central Seoul premier Hanwoo dining estate."}
            ],
            [
                {"label": "Health & Vitality Gifts", "text": "Korean Red Ginseng (Hongsam) and Boseong green tea are world-renowned superfoods."},
                {"label": "Serene Departure Readiness", "text": "All packing and check-in finished by Saturday night ensures Sunday morning is 100% calm."}
            ],
            "Lunch: Namdaemun handmade kalguksu noodle soup. Dinner: Grand Hanwoo charcoal beef banquet with Pyongyang cold noodles and maesil wine.",
            "Complete online airline check-in 24 hours prior to Sunday 13:00 departure.",
            "Wellness gifts ~₩60,000–₩150,000; Grand Farewell Dinner ~₩50,000 per person.",
            "Pack liquid ginseng tonics securely in checked baggage.",
            "Underground department store arcades connect Namdaemun to Myeongdong."
        ),
        # Day 22: Nov 22
        make_day(21, "Seoul", "Departure", "Departure · Incheon International Airport",
            "AREX Non-Stop Express to ICN → Airport Customs & Tax Refund → Flight at 13:00",
            "Seamless Airport Rail & Rejuvenated Departure",
            [
                {"time": "08:30–09:15", "title": "Hotel Checkout & AREX Express Boarding", "detail": "Check out of Seoul Station hotel and board direct AREX Non-Stop Express Train to Incheon Airport (43 mins).", "logistics": "B2 Seoul Station."},
                {"time": "09:30–10:15", "title": "AREX Express to ICN Terminal 1 / 2", "detail": "Fast, direct airport train ride with reserved seating and dedicated luggage racks.", "logistics": "43 min to T1 / 51 min to T2."},
                {"time": "10:15–12:15", "title": "Airport Customs, Tax Refunds & Departure Gate", "detail": "Drop luggage, clear security, collect tax refund cash, and reach departure gate by 12:20.", "logistics": "Target arriving 3 hours prior to 13:00 international flight."},
                {"time": "12:30–13:00", "title": "Boarding & Flight Departure at 13:00", "detail": "Board aircraft for the flight home, feeling physically refreshed, toned, and deeply rejuvenated from 22 days in Korea.", "logistics": "Flight departs at 13:00 local time."}
            ],
            [
                {"label": "Zero Departure Stress", "text": "Direct AREX express guarantees exact 43-minute transit to Incheon Airport."},
                {"label": "Peak Vitality", "text": "Return home feeling energized, limber, and thoroughly refreshed."}
            ],
            "Breakfast: Hotel café or airport lounge / Korean Food Street at ICN Terminal (warm abalone porridge or beef soup).",
            "Verify airline departure terminal (T1 vs T2) before boarding AREX.",
            "AREX Express ticket ₩13,000 per person (fare raised from ₩11,000; verified 2026).",
            "Terminal 2 is 8 minutes further on the AREX line than Terminal 1.",
            "If AREX express sells out, AREX all-stop commuter train departs every 8 minutes."
        )
    ]

    scorecard = [
        {"label": "Thermal Hot Springs", "value": "5/5", "tone": "good"},
        {"label": "Nature & Forest Trails", "value": "5/5", "tone": "good"},
        {"label": "Coastal Treks", "value": "5/5", "tone": "good"},
        {"label": "Physical Recovery", "value": "5/5", "tone": "good"}
    ]

    return {
        "id": "seoul-daejeon-busan-wellness",
        "shortTitle": "Seoul · Daejeon · Busan (Wellness & Nature)",
        "title": "Active Nature, Thermal Hot Springs & Coastal Ridges (Wellness & Nature)",
        "routeLabel": "Seoul (7N) → Daejeon (5N) → Busan (7N) → Seoul (2N)",
        "badge": "Thermal Springs & Mountain Trails",
        "bestFor": "Hikers, nature lovers, wellness seekers, and active travelers looking for rejuvenating hot spring baths, pristine autumn forest trails, earthing red clay walks, and dramatic coastal cliff walks.",
        "decisionSummary": "A restorative, nature-centered journey linking Seoul's national park peaks and pine ridges with Daejeon's famous Yuseong thermal springs and Gyejoksan red clay earthing, culminating in Busan's luxury jjimjilbang saunas and Igidae coastal trails.",
        "recommendation": "Choose this route if your ideal vacation balances invigorating daily nature walks with deep thermal mineral relaxation and nourishing herbal cuisine.",
        "tradeoff": "Requires comfortable walking fitness for outdoor trails, uneven granite steps, and willingness to experience traditional Korean public hot springs.",
        "scorecard": scorecard,
        "bases": get_sdb_common_bases(),
        "transfers": get_sdb_common_transfers(),
        "budgetScenarios": get_sdb_budget_scenarios(),
        "bookingPriorities": get_sdb_booking_priorities(),
        "days": days
    }
