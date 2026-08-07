#!/usr/bin/env python3
"""Render readable route-blueprint Markdown from data/itineraries.json.

The JSON file is the source of truth for the app and this script creates a
printable/reviewable Markdown companion for each route.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "itineraries.json"
OUT = ROOT / "itineraries"


def pretty_date(iso: str) -> str:
    year, month, day = (int(part) for part in iso.split("-"))
    return date(year, month, day).strftime("%a, %b %-d, %Y")


def render_route(route: dict, trip: dict) -> str:
    lines = [
        f"# {route['title']}",
        "",
        f"> **Route:** {route['routeLabel']}",
        f"> **Arrival:** {pretty_date(trip['arrival']['date'])}, {trip['arrival']['time']} at {trip['arrival']['airport']}",
        f"> **Departure:** {pretty_date(trip['departure']['date'])}, {trip['departure']['time']} at {trip['departure']['airport']}",
        f"> **Length:** {trip['nights']} nights / {len(route['days'])} calendar days",
        "",
        "## Why choose this route",
        "",
        route["decisionSummary"],
        "",
        f"**Best for:** {route['bestFor']}",
        "",
        f"**Tradeoff to accept:** {route['tradeoff']}",
        "",
        "## Hotel-base strategy",
        "",
        "| City | Dates / nights | Recommended base | Why it works |",
        "| --- | --- | --- | --- |",
    ]
    for base in route["bases"]:
        lines.append(
            f"| {base['city']} | {base['dates']} / {base['nights']} nights | {base['recommendedArea']} | {base['why']} |"
        )

    lines += ["", "### Source-research hotel ideas", ""]
    for base in route["bases"]:
        lines.append(f"- **{base['city']}:** " + " · ".join(base["hotelIdeas"]))

    lines += ["", "## Transfer strategy", ""]
    for transfer in route["transfers"]:
        lines += [
            f"### {pretty_date(transfer['date'])} — {transfer['leg']}",
            "",
            f"**Recommended flow:** {transfer['recommended']}",
            "",
            f"**Why:** {transfer['why']}",
            "",
        ]

    lines += ["## Book in this order", ""]
    for priority in route["bookingPriorities"]:
        lines.append(f"1. {priority}")

    lines += ["", "## Day-by-day itinerary", ""]
    for day in route["days"]:
        lines += [
            f"### {pretty_date(day['date'])} — {day['city']} · {day['phase']}",
            "",
            f"**Stay:** {day['stay']}",
            "",
            f"**Day anchor:** {day['anchor']}",
            "",
            f"#### {day['title']}",
            "",
        ]
        for block in day["blocks"]:
            lines.append(f"- **{block['label']}:** {block['text']}")
        lines += [
            "",
            f"**Food rhythm:** {day['food']}",
            "",
            f"**Watch for:** {day['watchouts']}",
            "",
            f"**Plan B:** {day['planB']}",
            "",
        ]

    lines += [
        "## Verify before booking or travel",
        "",
        "- Confirm the live KTX timetable, sale/release window, departure station, seat availability, fare, and last-mile connection in Korail / the official provider.",
        "- Confirm hotel late check-in, current price, room type, address in Korean, and actual airport-transfer fit.",
        "- Confirm opening days/hours, paid tickets, event status, weather, air quality, entry rules, and all emergency information close to travel.",
        "- This is a detailed planning blueprint, not a booking confirmation or live timetable.",
        "",
    ]
    return "\n".join(lines)


def render_index(routes: list[dict], trip: dict) -> str:
    lines = [
        "# November 2026 route blueprints",
        "",
        f"**Actual trip window:** arrive ICN at **{trip['arrival']['time']} on {pretty_date(trip['arrival']['date'])}**; depart ICN at **{trip['departure']['time']} on {pretty_date(trip['departure']['date'])}**.",
        "",
        "Both options are 21-night, 22-calendar-day plans. They protect the final two Seoul nights before the 13:00 ICN departure, use direct KTX legs where practical, keep one hotel base per city, and group sightseeing by neighborhood.",
        "",
        "## Compare the two middle-city choices",
        "",
        "| Route | Choose it when | Main advantage | Tradeoff |",
        "| --- | --- | --- | --- |",
    ]
    for route in routes:
        lines.append(
            f"| [{route['shortTitle']}]({route['id']}.md) | {route['bestFor']} | {route['badge']} | {route['tradeoff']} |"
        )
    lines += ["", "## Common routing logic", ""]
    for principle in trip["planningPrinciples"]:
        lines.append(f"- {principle}")
    lines += ["", "## Important timing notes", ""]
    for item in trip["importantDates"]:
        lines.append(f"- **{pretty_date(item['date'])} — {item['label']}:** {item['note']}")
    lines += [
        "",
        "The app’s **Route options** screen renders these same plans and can load either route into the editable **My plan** timeline. Source material and official-link reminders are available in the main Korea Compass source desk.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    trip = payload["meta"]["trip"]
    routes = payload["itineraries"]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "README.md").write_text(render_index(routes, trip), encoding="utf-8")
    for route in routes:
        (OUT / f"{route['id']}.md").write_text(render_route(route, trip), encoding="utf-8")
    print(f"Built {len(routes)} detailed itinerary documents in {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
