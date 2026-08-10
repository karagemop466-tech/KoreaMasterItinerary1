#!/usr/bin/env python3
"""Detailed blueprints helper for the 5 Seoul · Cheonan · Busan itineraries."""

from scripts.generate_all_itineraries import make_day

def get_scb_common_bases():
    return [
        {
            "city": "Seoul",
            "dates": "Nov 1–8",
            "nights": 7,
            "recommendedArea": "Myeongdong / Seoul Station edge",
            "why": "Immediate access to Seoul Station for the short 35-minute KTX hop to Cheonan-Asan, direct AREX connection, and walking proximity to Deoksugung, Namdaemun, and Jongno.",
            "hotelIdeas": ["Four Points by Sheraton Josun Seoul Station", "Nine Tree Premier Hotel Myeongdong II", "L7 Myeongdong"]
        },
        {
            "city": "Cheonan",
            "dates": "Nov 8–13",
            "nights": 5,
            "recommendedArea": "Cheonan-Asan Station area / Shinbu-dong",
            "why": "Cheonan-Asan Station is a hyper-connected KTX/SRT high-speed rail junction with direct transit access to Independence Hall of Korea, Arario Sculpture Park, Gakwonsa Temple, and local food alleys.",
            "hotelIdeas": ["Shilla Stay Cheonan", "Ramada Encore by Wyndham Cheonan-Asan", "ON City Hotel Cheonan"]
        },
        {
            "city": "Busan",
            "dates": "Nov 13–20",
            "nights": 7,
            "recommendedArea": "Haeundae Beachfront / Marine City",
            "why": "Walk to Haeundae Beach, Blueline Park coastal train, Centum City Spa Land, and direct bus/metro connections across the eastern and southern coast.",
            "hotelIdeas": ["L7 Haeundae", "Felix by STX Hotel & Suites", "Signiel Busan", "Shilla Stay Haeundae"]
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

def get_scb_common_transfers():
    return [
        {
            "date": "2026-11-01",
            "leg": "Incheon Airport (ICN) → Central Seoul Hotel",
            "recommended": "Airport Limousine Bus (6001/6015) or official airport taxi queue directly to hotel in Myeongdong / Seoul Station.",
            "why": "Late arrival at 21:00 means clearing customs around 22:15. Direct bus or taxi drops luggage at hotel doorstep without late-night subway transfers."
        },
        {
            "date": "2026-11-08",
            "leg": "Seoul Station → Cheonan-Asan Station (KTX)",
            "recommended": "KTX High-Speed Rail (approx. 35–40 minutes, direct).",
            "why": "Extremely fast 35-minute rail leap; minimal travel time leaving the full day open for sightseeing and check-in."
        },
        {
            "date": "2026-11-13",
            "leg": "Cheonan-Asan Station → Busan Station (KTX)",
            "recommended": "KTX High-Speed Rail (approx. 1 hour 45 minutes, direct).",
            "why": "Direct high-speed connection from Cheonan-Asan hub down to coastal Busan Station, arriving in time for beach check-in."
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

def get_scb_budget_scenarios():
    return [
        {
            "label": "Value Comfort (3-Star Boutique & Station Stays)",
            "subtotal": "USD $1,890–$2,450 (avg. $90–$117/night for 21 nights)",
            "assumptions": "Double room with private bath; Nine Tree Myeongdong, Shilla Stay Cheonan, Felix by STX Haeundae.",
            "note": "Exceptional value in Cheonan; excellent station proximity, high walking score, clean modern amenities."
        },
        {
            "label": "Upscale Premium (4 to 5-Star City & Ocean View Stays)",
            "subtotal": "USD $3,570–$4,900 (avg. $170–$233/night for 21 nights)",
            "assumptions": "King room with breakfast; L7 Myeongdong, Ramada Encore Cheonan-Asan, Signiel or Grand Josun Busan.",
            "note": "Panoramic ocean views in Busan, premier bedding, luxury fitness, and central station ease."
        }
    ]

def get_scb_booking_priorities():
    return [
        "Reconcile SFO outbound flight with Nov 1 21:00 local ICN arrival and Nov 22 13:00 departure.",
        "Reserve 4 hotel base stays with free cancellation (Seoul 7N, Cheonan 5N, Busan 7N, Seoul 2N).",
        "Book 3 KTX rail legs on Korail app 30 days prior (Seoul→Cheonan-Asan, Cheonan-Asan→Busan, Busan→Seoul).",
        "Reserve AREX Non-Stop Airport Express tickets and pre-order Korea eSIM / T-Money / WOWPASS card.",
        "Secure timed reservations for special experiences (e.g. Changdeokgung Secret Garden, Blueline Sky Capsule, Spa Land)."
    ]
