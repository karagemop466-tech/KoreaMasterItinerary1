#!/usr/bin/env python3
"""Detailed blueprints for the 5 Seoul · Daejeon · Busan itineraries."""

from scripts.generate_all_itineraries import make_day

def get_sdb_common_bases():
    return [
        {
            "city": "Seoul",
            "dates": "Nov 1–8",
            "nights": 7,
            "recommendedArea": "Myeongdong / Seoul Station edge",
            "why": "Central subway interchange (Line 1/4/2 access), direct AREX connection, easy walking to Deoksugung, Namdaemun, and Myeongdong, and minimal friction for the Sunday morning KTX departure.",
            "hotelIdeas": ["Four Points by Sheraton Josun Seoul Station", "L7 Myeongdong", "Nine Tree Premier Hotel Myeongdong II"]
        },
        {
            "city": "Daejeon",
            "dates": "Nov 8–13",
            "nights": 5,
            "recommendedArea": "Yuseong Hot Springs / Dunsan-dong",
            "why": "Direct subway connection (Line 1) to Daejeon KTX Station, natural mineral hot spring foot baths on the street, and close proximity to KAIST, Expo Science Park, and Hanbat Arboretum.",
            "hotelIdeas": ["Hotel Onoma Daejeon (Autograph Collection)", "Lotte City Hotel Daejeon", "Yuseong Hotel / Ramada by Wyndham Daejeon"]
        },
        {
            "city": "Busan",
            "dates": "Nov 13–20",
            "nights": 7,
            "recommendedArea": "Haeundae Beachfront / Marine City",
            "why": "Walk to Haeundae Beach, Blueline Park coastal train, Centum City Spa Land, and direct bus/metro connections across the eastern and southern coast.",
            "hotelIdeas": ["L7 Haeundae", "Signiel Busan", "Felix by STX Hotel & Suites", "Shilla Stay Haeundae"]
        },
        {
            "city": "Seoul",
            "dates": "Nov 20–22",
            "nights": 2,
            "recommendedArea": "Seoul Station / Myeongdong",
            "why": "Guarantees a stress-free AREX Non-Stop express connection to Incheon Airport on Sunday morning and eliminates all risk of high-speed rail disruption on flight day.",
            "hotelIdeas": ["Four Points by Sheraton Josun Seoul Station", "Nine Tree Premier Hotel Myeongdong II", "Hotel 28 Myeongdong"]
        }
    ]

def get_sdb_common_transfers():
    return [
        {
            "date": "2026-11-01",
            "leg": "Incheon Airport (ICN) → Central Seoul Hotel",
            "recommended": "Airport Limousine Bus (e.g. 6001/6015) or AREX All-Stop/Express depending on terminal and hotel location; Official Airport Taxi queue if arriving with heavy luggage after 21:00.",
            "why": "Late arrival at 21:00 means clearing customs around 22:15. Direct bus or taxi drops luggage at hotel doorstep without late-night subway transfers."
        },
        {
            "date": "2026-11-08",
            "leg": "Seoul Station → Daejeon Station (KTX)",
            "recommended": "KTX High-Speed Rail (approx. 50–60 minutes, direct).",
            "why": "Frequent 15–20 minute departure intervals; smooth transition from central Seoul to central Daejeon with minimal transit fatigue."
        },
        {
            "date": "2026-11-13",
            "leg": "Daejeon Station → Busan Station (KTX)",
            "recommended": "KTX High-Speed Rail (approx. 1 hour 30 minutes, direct).",
            "why": "Fastest and most comfortable connection from central Daejeon to coastal Busan, arriving in time for check-in and sunset seafood dinner."
        },
        {
            "date": "2026-11-20",
            "leg": "Busan Station → Seoul Station (KTX)",
            "recommended": "KTX High-Speed Rail (approx. 2 hours 15 minutes, direct).",
            "why": "Returning to Seoul 2 nights before international flight buffers against rail weather delays and allows relaxed final souvenir shopping."
        },
        {
            "date": "2026-11-22",
            "leg": "Seoul Station → Incheon International Airport (ICN)",
            "recommended": "AREX Non-Stop Express Train (43 min to T1, 51 min to T2) with Seoul Station City Airport Terminal check-in if eligible.",
            "why": "Punctual, climate-controlled, dedicated luggage racks, arriving 3 hours before the 13:00 flight."
        }
    ]

def get_sdb_budget_scenarios():
    return [
        {
            "label": "Value Comfort (3-Star Boutique & Business Stays)",
            "subtotal": "USD $1,980–$2,640 (avg. $95–$125/night for 21 nights)",
            "assumptions": "Double room with private bath; Nine Tree Myeongdong, Ramada Daejeon, Felix by STX Haeundae.",
            "note": "Excellent cleanliness, prime station/metro proximity, laundry facilities, high walking score."
        },
        {
            "label": "Upscale Premium (4 to 5-Star City & Ocean View Stays)",
            "subtotal": "USD $3,780–$5,250 (avg. $180–$250/night for 21 nights)",
            "assumptions": "King room with breakfast; L7 Myeongdong, Hotel Onoma Daejeon, Signiel or Grand Josun Busan.",
            "note": "Panoramic skyline views, thermal spa access, luxury bedding, premier fitness amenities."
        }
    ]

def get_sdb_booking_priorities():
    return [
        "Reconcile SFO outbound flight with Nov 1 21:00 local ICN arrival and Nov 22 13:00 departure.",
        "Reserve 4 hotel base stays with free cancellation (Seoul 7N, Daejeon 5N, Busan 7N, Seoul 2N).",
        "Book 3 KTX rail legs on Korail app 30 days prior to travel (Seoul→Daejeon, Daejeon→Busan, Busan→Seoul).",
        "Reserve AREX Non-Stop Airport Express tickets and pre-order Korea eSIM / T-Money / WOWPASS card.",
        "Secure timed reservations for special experiences (e.g. Changdeokgung Secret Garden, Spa Land, fine dining)."
    ]
