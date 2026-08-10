#!/usr/bin/env python3
"""Master Builder for all 10 South Korea Itinerary Blueprints.

5 Itineraries for Seoul · Daejeon · Busan (Nov 1–22, 2026; 21 nights / 22 calendar days)
5 Itineraries for Seoul · Cheonan · Busan (Nov 1–22, 2026; 21 nights / 22 calendar days)
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITINERARIES_PATH = ROOT / "data" / "itineraries.json"

DATES = [
    ("2026-11-01", "Sun"),
    ("2026-11-02", "Mon"),
    ("2026-11-03", "Tue"),
    ("2026-11-04", "Wed"),
    ("2026-11-05", "Thu"),
    ("2026-11-06", "Fri"),
    ("2026-11-07", "Sat"),
    ("2026-11-08", "Sun"),
    ("2026-11-09", "Mon"),
    ("2026-11-10", "Tue"),
    ("2026-11-11", "Wed"),
    ("2026-11-12", "Thu"),
    ("2026-11-13", "Fri"),
    ("2026-11-14", "Sat"),
    ("2026-11-15", "Sun"),
    ("2026-11-16", "Mon"),
    ("2026-11-17", "Tue"),
    ("2026-11-18", "Wed"),
    ("2026-11-19", "Thu"),
    ("2026-11-20", "Fri"),
    ("2026-11-21", "Sat"),
    ("2026-11-22", "Sun"),
]

def make_day(idx, city, phase, stay, anchor, title, schedule, blocks, food, res_note, cost_note, watchouts, plan_b):
    dt, day_name = DATES[idx]
    return {
        "date": dt,
        "day": day_name,
        "city": city,
        "stay": stay,
        "phase": phase,
        "title": title,
        "anchor": anchor,
        "scheduleLabel": "Target schedule windows",
        "schedule": schedule,
        "blocks": blocks,
        "food": food,
        "reservationNote": res_note,
        "costNote": cost_note,
        "watchouts": watchouts,
        "planB": plan_b
    }

def get_shared_meta():
    return {
        "title": "November 2026 Korea route blueprints",
        "version": 2,
        "trip": {
            "arrival": {
                "date": "2026-11-01",
                "day": "Sunday",
                "time": "21:00",
                "airport": "Incheon International Airport (ICN)",
                "city": "Seoul"
            },
            "departure": {
                "date": "2026-11-22",
                "day": "Sunday",
                "time": "13:00",
                "airport": "Incheon International Airport (ICN)",
                "city": "Seoul"
            },
            "nights": 21,
            "partyAssumption": "Two travelers",
            "planningPrinciples": [
                "Use one practical hotel base per city; the only intentional return is the final two Seoul nights for a low-stress ICN departure.",
                "Travel by direct KTX on city-change days, with only a light neighborhood plan after check-in.",
                "Group sights by neighborhood rather than crisscrossing each city for a single attraction.",
                "Keep a weather-friendly indoor alternative every day and avoid making time-sensitive events the sole anchor.",
                "Treat all rail times, event dates, pricing, opening hours, and entry rules as details to verify in official apps and sites before purchase."
            ],
            "importantDates": [
                {
                    "date": "2026-11-19",
                    "label": "CSAT / Suneung day",
                    "note": "Keep this Busan day deliberately low-stakes. Morning traffic management, later office/bank opening, and an approximately 13:05–13:40 aviation hold; verify the current notice before travel."
                },
                {
                    "date": "2026-11-22",
                    "label": "13:00 ICN departure",
                    "note": "Plan to be at the airport around three hours before an international departure, subject to airline guidance. Stay in Seoul the final two nights instead of attempting a same-day Busan-to-ICN connection."
                }
            ],
            "sourceNote": "These are deliberately detailed planning blueprints synthesized from the retained transport, hotel, activity, food, savings, and emergency research. They are not confirmations or a live timetable.",
            "scheduleNote": "Times below are intentional planning windows, not a live timetable. They are designed to make the day explicit while retaining enough buffer for weather, queues, rests, and transit.",
            "flightReconciliation": "The Korea-based plan begins with a local ICN arrival at 21:00 on Nov. 1 and ends with a local ICN departure at 13:00 on Nov. 22. Because Seoul is well ahead of San Francisco, do not assume a Nov. 1 SFO departure can also be a Nov. 1 ICN arrival; reconcile the outbound calendar date, airline, terminal, and arrival time from the actual ticket before booking the first hotel night.",
            "weatherAndPacking": [
                "Use layers rather than one heavy coat: a warm mid-layer, wind/rain shell, comfortable broken-in walking shoes, and evening accessories are more useful than a fixed temperature promise.",
                "Check the actual forecast and AirKorea a few days before departure. The route includes outdoor palace, coast, park, and market days, but every one has an indoor or low-walking fallback.",
                "Carry a compact umbrella or waterproof layer, a power bank, a universal Type C/F adapter, any personal medicines in original packaging, and a small day bag for train days."
            ],
            "budgetFrame": [
                {
                    "label": "Stay strategy",
                    "detail": "Price live hotel rooms by exact dates and one-bed/private-bath requirements. The plans favor a practical Myeongdong/Seoul Station base, a station-oriented middle-city base, and one Haeundae base rather than costly hotel moves."
                },
                {
                    "label": "Transport strategy",
                    "detail": "Direct KTX is the value/convenience default for city changes. T-money/WOWPASS-style local payment remains useful, but re-check current accepted cards, pass coverage, and actual fares."
                },
                {
                    "label": "Experience strategy",
                    "detail": "Use a few paid anchors that matter to you, then layer in markets, parks, coastal walks, museums, and neighborhood food. Do not buy a pass solely because it is discounted; compare it with your actual saved list."
                },
                {
                    "label": "Food strategy",
                    "detail": "Keep one quality meal or market experience per day, then use convenience-store, bakery, café, or hotel-neighborhood meals to protect pace and budget."
                }
            ],
            "arrivalChecklist": [
                "Confirm hotel late check-in and save its Korean address before boarding the last flight.",
                "Keep passport, arrival/entry confirmation, insurance contact, final hotel address, and an offline emergency card accessible before landing.",
                "Choose the airport transfer based on live arrival time, luggage, terminal, and hotel—not a generic cheapest-fare rule.",
                "Do not schedule sightseeing, a nonrefundable dinner, or a timed ticket on the arrival night."
            ],
            "departureChecklist": [
                "Complete online check-in and verify the airline terminal, baggage allowance, and airport cutoff the day before.",
                "Pack passports, cards, devices, receipts/tax-refund paperwork, and medicines in a known carry-on location on Nov. 21.",
                "Leave central Seoul early enough to be at ICN around three hours before the 13:00 international departure, following airline advice.",
                "Handle airline, security, and any valid tax-refund process before duty-free browsing or a meal."
            ],
            "budgetMethodNote": "Hotel examples below multiply the retained research's indicative one-room nightly USD ranges by the planned nights. They are planning math only: taxes, service fees, room type, weekend/date demand, currency conversion, promotions, and availability can materially change the real total.",
            "dailySpendGuardrails": [
                "Keep food, local transit, and paid activities as separate envelopes rather than relying on the rough draft's old all-in daily price. Your actual balance depends on how many paid anchors you keep.",
                "Use the planner's saved ideas and route days to identify the handful of paid tickets, reservations, spa/cooking-class choices, and special meals that deserve a confirmed budget.",
                "Price the full transportation stack only after the airline, KTX trains, airport transfer, local payment card/pass, and hotel districts are selected."
            ],
            "flightBookingChecklist": [
                "Search to the actual local ICN arrival target first: 21:00 on Nov. 1. The originating SFO calendar date may be earlier because Seoul is far ahead of San Francisco.",
                "Compare live direct and one-stop options by total arrival time, baggage/cancellation terms, seat comfort, airline terminal, and the ability to reach the Seoul hotel after immigration—not by an old fare screenshot.",
                "After purchase, add flight numbers, both airport terminals, airline check-in cutoff, baggage allowance, seat assignment, and travel-insurance details to My plan.",
                "Do not build a nonrefundable Seoul arrival-night plan until the flight and the hotel's late check-in policy are confirmed."
            ]
        }
    }

def main():
    import sys
    sys.path.insert(0, str(ROOT))
    
    from scripts.routes_sdb_1_classic import get_sdb_classic
    from scripts.routes_sdb_2_foodie import get_sdb_foodie
    from scripts.routes_sdb_3_heritage import get_sdb_heritage
    from scripts.routes_sdb_4_wellness import get_sdb_wellness
    from scripts.routes_sdb_5_modern import get_sdb_modern
    from scripts.routes_scb_1_rail import get_scb_rail
    from scripts.routes_scb_2_value import get_scb_value
    from scripts.routes_scb_3_leisure import get_scb_leisure
    from scripts.routes_scb_4_arts import get_scb_arts
    from scripts.routes_scb_5_gourmet import get_scb_gourmet

    itineraries = [
        # Seoul · Daejeon · Busan (5 Blueprints)
        get_sdb_classic(),
        get_sdb_foodie(),
        get_sdb_heritage(),
        get_sdb_wellness(),
        get_sdb_modern(),
        # Seoul · Cheonan · Busan (5 Blueprints)
        get_scb_rail(),
        get_scb_value(),
        get_scb_leisure(),
        get_scb_arts(),
        get_scb_gourmet(),
    ]

    # Validate all 10 itineraries
    print(f"Generated {len(itineraries)} itinerary blueprints:")
    for idx, it in enumerate(itineraries, 1):
        num_days = len(it["days"])
        print(f"  {idx:2d}. [{it['id']}] {it['title']} ({num_days} days)")
        assert num_days == 22, f"Expected 22 days, got {num_days} for {it['id']}"
        assert it["days"][0]["date"] == "2026-11-01"
        assert it["days"][-1]["date"] == "2026-11-22"

    payload = {
        "meta": get_shared_meta()["meta"] if "meta" in get_shared_meta() else get_shared_meta(),
        "itineraries": itineraries
    }

    ITINERARIES_PATH.parent.mkdir(parents=True, exist_ok=True)
    ITINERARIES_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nSuccessfully wrote {len(itineraries)} complete itineraries to {ITINERARIES_PATH.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
