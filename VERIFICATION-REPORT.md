# Repository Hallucination Audit — Verification Report

**Audit date:** 2026-08-18 · **Repo:** `KoreaMasterItinerary1` · **Branch audited:** `arena/01a01665-koreamasteritinerary1`
**Method:** Every data collection was enumerated programmatically; date/URL/coordinate/provenance checks were run by script, then factual claims were verified against official or primary sources (event organizers, city portals, KOVO/K League, venue ticketing pages, VisitKorea/VisitSeoul, Korean news wires, and U.S./ROK government pages). Machine-readable food audit: [`research/verification-food-audit.csv`](research/verification-food-audit.csv).

---

## 1. Executive verdict

| Collection | Entries | Real / Verified | Problematic | Verdict |
|---|---|---|---|---|
| Events (`data/collections/events.json`) | 110 | ~108 grounded in reality | 4 with factual errors (details §4) | **Mostly solid** — all 35 "Confirmed" headliners check out; all 110 carry official source links |
| Hotels (`data/collections/hotels.json`) | 34 | 34 / 34 real properties | 0 (star ratings & prices = planning estimates) | **Real** |
| Places (`data/index.json`) | 15 | 15 / 15 | 0 | **Real** |
| Transport routes / fares | 15 routes | All real services; times & most fares verified | Busan Metro fares stale (§4.4) | **Mostly solid** |
| Apps (`data/index.json`) | 9 | 9 / 9 real apps | 0 | **Real** |
| Savings guides (`data/collections/savingsGuides.json`) | 61 sections | Chains/apps referenced are real | 0 fabricated entities; advice is opinion-level | **Real, advice-grade** |
| Activities (`data/collections/activities.json`) | 443 | Attractions named are real places | 6 duplicated titles (builder issue) | **Real, minor dupes** |
| **Food (`data/collections/food.json`)** | 535 | **50 are real, named restaurants** | **485 synthetic entries (90.7%)** | 🔴 **MASS HALLUCINATION** |
| Emergency contacts (`research/sources/emergency/`) | — | All numbers verified official except one mislabel | 1 mislabeled number (§4.6) | **Solid with 1 fix needed** |

**Bottom line:** One large confirmed hallucination (485 fabricated restaurant bookmarks), plus a short list of concrete factual errors to fix. Everything else spot-verified clean against official sources.

---

## 2. 🔴 CONFIRMED HALLUCINATION — 485 fake restaurant bookmarks

`data/collections/food.json` (identically `research/sources/food/restaurants-bookmarks.csv`) contains **535 rows, of which 485 are algorithmically generated fabrications** with template names:

| Template pattern | Count | Example (fake) |
|---|---|---|
| `Seoul Local Ramen N`, `Seoul Local Jajangmyeon N`, `Seoul Local Classic Korean N`, `Seoul Local AYCE BBQ N`, `Seoul Local Cafe N` | 175 | "Seoul Local Ramen 25" / 서울 로컬 라멘 25 |
| `Busan Harbour Ramen N`, `…Jajangmyeon`, `…Classic Korean`, `…AYCE BBQ`, `…Cafe` | 183 | "Busan Harbour Classic Korean 6" / 부산 항구 한식 6 |
| `Daejeon Town … N` templates | 68 | "Daejeon Town AYCE BBQ 12" / 대전 타운 BBQ 12 |
| `Cheonan Hub … N` templates | 59 | "Cheonan Hub Classic Korean 9" / 천안 허브 한식 9 |

**How we know they are hallucinated:** (1) names follow literal generative templates with counters; (2) the `koreanName` fields are machine-translations of the template, not real establishments; (3) every "source" is a bare `map.naver.com/p/search/<fake name>` query — Naver searches for these names return no such business; (4) no entry has a primary source, address, phone, or review trail; (5) the source repo's own `sources-and-notes.md` documents an audit of "200 restaurants," not 535 — the padding is unaccounted for.

**The fake entries also poison the app UI**: README advertises "535 food bookmarks," and the discovery library presents these to end users as if they were real restaurants. That is the single most dangerous hallucination in the repo: a traveler could search "대전 타운 짜장면 10" and find nothing, or worse, be routed to an unrelated business.

**The 50 REAL named bookmarks** (verified against official tourism portals / known listings) — all genuine: Oreno Ramen (Main, Insadong), Menten, Ramen Jiro Seoul, Hong Kong Banjum 0410, Sinseonggak, Osegyehyang, Myeongnyun Jinsa Galbi, Budnamujip, Daedo Sikdang Wangsimni, Geumdwaeji Sikdang, Yukjeon Sikdang, Nari's House, Mapo Jeong Daepo, Myeongdong Kyoja, Hadongkwan, Chanyang-jip, Imun Seolleongtang, Buchon Yukhoe, Jin Ok-hwa Halmae Dakhanmari, Maboklim Halmoni Tteokbokki, Somunnan Seongsu Gamjatang, Goryeo Samgyetang, Shin Old Tea House, Fritz Coffee Dohwa (Seoul); Nagahama Mangetsu, Gukje/Gaya/Halmae Gaya/Seomyeon Gaegeum Milmyeon, Gijang Sonkalguksu, Hwaguk Banjeom, Maga Mandu, Shinbalwon, Haeundae Somunnan Amso Galbi-jip, Busan Jokbal, Songjeong Samdae Gukbap, Bujeon Market stalls, Jagalchi Market, Dongnae Halmae Pajeon, Samjin Amook, Brown Hands Baekje (Busan); Sutgol Won Naengmyeon, Ossi Kalguksu, Boksu Bunsik, Sariwon Myeonok, Taepyung Sogukbap, Kingdom Buffet, Sungsimdang (Daejeon); Dongsunwon Seonghwan (Cheonan).

---

## 3. ✅ Verified real — headliner events (with sources)

All 35 "Confirmed"-status events were checked against organizer/official or press sources. Exact date-and-venue matches:

| Repo entry | Claimed | Officially verified | Source |
|---|---|---|---|
| BANKSY: Still Here | Jul 22–Nov 3, ALT.1 The Hyundai Seoul | **Exact match** (price wrong, see §4.1) | VisitSeoul official listing |
| My Chemical Romance | Nov 7, Paradise City (Incheon) | **Exact match** Nov 7, Paradise City | StubHub/Bandsintown event data |
| Jujutsu Kaisen in Concert | Nov 7–8, Kyung Hee Univ. | **Match** (venue official name = "Grand Peace Palace") | NOL World official ticketing |
| Sir Simon Rattle & BRSO | Nov 12–13, Seoul Arts Center | **Exact match** | Korea Herald H2 concert preview |
| Jason Mraz Asia Tour | Nov 14, KINTEX | **Exact match** (tour finale) | jasonmraz.com official |
| Kings of Convenience | Nov 18, Sejong Center | **Exact match** | Yes24 official ticket page |
| 5 Seconds of Summer | Nov 19, KINTEX | **Exact match** | Cineplay / promoter AccessX |
| MMA 2026 | Nov 14–15, Gocheok Sky Dome | **Exact match** | Kakao Ent. via Star News, Asiae |
| KGMA 2026 | Nov 7–8, Gocheok Sky Dome | **Exact match** | KGMA committee via Soompi |
| MAMA 2026 (watch-from-Korea) | Nov 20–21, Kyocera Dome Osaka | **Exact match** | CJ ENM official newsroom |
| LoL Worlds 2026 final (watch party) | Nov 14 | **Exact match** (final is in Brooklyn, NY — repo correctly frames it as a Seoul watch party) | Wikipedia / Riot announcements |
| Musical ELISABETH | Aug 16–Nov 15, Blue Square Woori Bank Hall | **Exact match** | NOL World official |
| Musical Hell's Kitchen | Jul 24–Nov 8, GS Arts Center | **Exact match** (S&Co / Korea JoongAng) | Official ticketing |
| Musical Gwanghwamun Love Song | Sep 6–Nov 15, D-CUBE LINK Arts Center | **Exact match** (CJ ENM) | Interpark/Notices, KBS |
| Musical Dear Evan Hansen | Aug 1–Nov 1, Chungmu Arts Center Grand Theater | **Exact match** (re-verified: culture.go.kr, Interpark/NOL) | MCST culture portal / official ticketing |
| Leeum — Inside Other Spaces | May 5–Nov 29, Leeum | **Exact match** | Yonhap / Korea Times |
| MMCA x LG OLED: Christine Sun Kim | Jul 31–Nov 29, MMCA Seoul "Seoul Box" | **Exact match** ("Have Many Dumb Fights Against Rock") | MMCA via Korea Herald/Times |
| Seoul Outdoor Library | Apr 23–Nov 1 | **Exact match** | festival.seoul.go.kr |
| Han River History Tour | Apr 3–Nov 30 | **Match** (listed on Seoul festival portal) | festival.seoul.go.kr |
| Changgyeonggung Mulbit Yeonhwa | Sep 8–Nov 8 (fall) | **Match** (fall full-screening window; some sources say Sep 10 start) | Korea Heritage Service program |
| Candlelight: World of Joe Hisaishi | Nov 13, Jeongdong 1928 | **Exact match** | Fever (official operator) |
| JTBC Seoul Marathon | Nov 1, Sangam World Cup Stadium start | **Exact match** | marathon.jtbc.com official |
| DDP "Dream in Light" (nightly) | year-round light show | **Real** (pilot Nov 2025; permanent from Jan 9, 2026) | Seoul Design Foundation |
| Seoul E-Land vs Jeonnam | Nov 7, Mokdong | **Exact match** | Fixture lists (Tribuna) |
| Seoul E-Land vs Chungnam Asan | Nov 22, Mokdong | **Exact match** | Fixture lists (Tribuna) |
| Cheonan City vs Busan IPark | Nov 8, Cheonan General Stadium | **Exact match** (R32, 14:00) | Namu fixture record |
| Busan IPark vs "Chungnam Cheongju" | Nov 21, Gudeok | **Date/venue right; team name wrong** (§4.2) | Haps/Stripes schedules |
| V-League: Woori Card / GS Caltex (Jangchung), Hyundai Capital (Yu Gwan-sun Gym, Cheonan), Samsung Fire & JungKwanJang (Chungmu Gym, Daejeon) | teams/venues | **Real teams & home gyms**; season window plausible | KOVO/club info |
| V-League: OK Savings Bank (men) in Busan | Busan home games | **Verified & surprisingly current** — OK formally relocated Ansan→Busan for 2025-26 (Gangseo gym) | KOVO / Busan city press release |
| G-STAR 2026 | Nov 19–22, BEXCO | **Match** (one outlet gives Nov 18 incl. B2B setup; 19–22 is the public window) | K-GAMES / SEDaily |
| Busan Fireworks Festival | Nov 7, Gwangalli | **Exact match** (Sat Nov 7, 2026) | Busan organizers / guides |
| Busan Biennale 2026 "Dissident Chorus" | Aug 29–Nov 1, MoCA + Space Wonji | **Exact match** | Biennale committee / Korea Herald |
| Daejeon International Wine EXPO | Nov 6–8, DCC | **Exact match** | djwinefair.com official |
| "Culture Flowing Through Seoul Plaza" | Nov window concerts | **Real program** (2026 season: May 6–Dec 31, weekly Wed) | Seoul MediaHub |

"**TBA**"-labeled seasonal festivals (Lotte World/Everland Halloween, Seoul Kimchi Festival, aT Center Kimjang Grand Festival, Korea Sale Festa, Changdeokgung Moonlight Tour, Noodle Daejeon Festival, O-World Chrysanthemum Festival) are all **real recurring events** with honest TBA framing — dates are carryovers from prior editions and are labeled as such. No fabrication.

The 54 "**Always on**" entries are all real permanent attractions (Gyeongbokgung guard ceremony, National Museum of Korea, Spa Land Centum City, Haeundae Blueline Park, Songdo Cable Car, Gakwonsa, Independence Hall, Gwangalli drone show Saturdays, etc.). Independently re-verified among these: **The Art Space 193** (Shinsegae Expo Tower observatory, Daejeon — real), **Cheonan Town Hall 47F Sky Lounge** (real: Hillstate Cheonan tower, 204 m, opened 2021), **Postal Museum of Korea** (real — in Yuryang-dong, Cheonan), **Muakjae Sky Bridge** (real), **DDP Dream in Light** (real, above).

---

## 4. 🟠 Confirmed factual errors (fix list)

1. **BANKSY: Still Here — wrong adult price.** Repo (event-1 + source CSV): "18000 adult". Official VisitSeoul listing: **Adults 23,000 KRW**; 18,000 KRW is the *youth/child* price (groups: 16,000). Off by ₩5,000 for the exact audience.
2. **event-59: non-existent team name "Chungnam Cheongju."** No such club exists — the league has **Chungbuk Cheongju FC** *and* **Chungnam Asan FC**; the Nov 21 Gudeok fixture is vs **Chungbuk Cheongju** per published schedules. Conflation of two clubs; fix the name.
3. ~~event-38 Dear Evan Hansen — truncated window~~ → **RETRACTED after re-verification (2026-08-18).** The repo's "Aug 1 – Nov 1, 2026" window at Chungmu Arts Center Grand Theater is exactly correct per the Ministry of Culture portal (culture.go.kr), the official Interpark/NOL ticket notice (show times Tue–Sun, VIP ₩160,000), and the production listing. No fix needed.
4. **Busan Metro fares stale** (`research/sources/transport/docs/12…md`). Repo: Section 1 **1,450 card / 1,550 cash**, Section 2 1,650. Official since the May 2024 hike: **1,600 card / 1,700 cash**, Section 2 **1,800 card**. (Busan city bus 1,550/1,650 and all Seoul fares check out.)
5. **Venue naming (one fix, one retraction):** Jujutsu Kaisen venue is officially **Grand Peace Palace** (평화의전당), not "Peace Hall" — **fixed**. ~~My Chemical Romance "Paradise City Culture Park"~~ → **RETRACTED after re-verification:** "Paradise City Culture Park" is the correct published venue name for the rescheduled Nov 7, 2026 show (postponed from Apr 18). No fix needed.
6. **Emergency doc mislabel:** `+82-2-3210-0404` is a **real number** but it is the ROK **Ministry of Foreign Affairs Consular Safety Call Center (영사안전콜센터)** — for Korean nationals abroad. It is *not* a "Korea Emergency Call Center for international callers." Foreign visitors in Korea: 112/119/1330 (+82-2-1330 from abroad). All other numbers verified official: 112, 119, 1366, 1330, U.S. Embassy +82-2-397-4114 (188 Sejong-daero), Consulate Busan +82-51-863-0731, State Dept +1-202-501-4444 / +1-888-407-4747.
7. **Tax-refund field mislabeled:** `taxRefund.vat_rate_percent = 7.5`. Korea's **VAT is 10%** (the *effective net refund* to tourists after agency fees is ~5–8%, which is presumably what 7.5 estimates). The thresholds are verified correct: ₩15,000 minimum, < ₩1,000,000 per payment for immediate refund, ≤ ₩5,000,000 per trip (VisitKorea official).
8. **Entry rules — verified clean:** K-ETA exemption for U.S. passports **through Dec 31, 2026** (U.S. State Dept & ROK MOFA both confirm) and **e-Arrival Card mandatory from Jan 1, 2026** (free, ≤3 days pre-arrival) — repo is accurate.
9. **Content hygiene (not hallucination but correctness):** 6 duplicated activity titles (builder dedupe gap): Banpo Hangang Park Some Sevit, Mangwon Hangang Park Sunset Lawn, Gwangbok-ro Fashion Street, Cheonan Town Hall 47th Floor, Hanbat Arboretum, Daejeon Skyroad.
10. **Re-verify before travel (status unclear, possibly stale):** **Arario Museum in SPACE** (blueprint #9's signature Seoul stop) — TripAdvisor shows "temporarily closed until further notice" while aggregators list 2026 hours; official status ambiguous. Arario Gallery Cheonan is confirmed open. Also note: Cheonan's "Namsan market" naming is legacy — **Namsan Jungang Market merged into Cheonan Jungang Market in 2018**.
11. **README count inflated:** "535 food bookmarks" should read 50 until the 485 synthetic rows are removed; the same inflation flows into `data/index.json` meta counts.

---

## 5. Verified real — supporting collections

- **Hotels 34/34 real.** Independently searched the zero-official-URL and least-known properties: The Mains Hotel (Cheonan, 34 Cheongsu 11-ro ✓), Aank Air Hotel Daejeon Station ✓, Hotel Interciti Daejeon (Yuseong, operating ✓), GG Hotel Gyeongju (Hwangnidan-gil area ✓), Hotel Stendhal Daejeon (Yuseong ✓), ON City Hotel Cheonan (official VisitKorea listing ✓), Best Western Asan (real; note recent listings also show it as *SureStay Plus by Best Western Asan* — check branding). The remainder are major chains whose existence/branding (L7, Lotte City, Shilla Stay, Nine Tree by Parnas, Ibis/Ibis Styles, Four Seasons, Fairmont, Grand Josun, Park Hyatt, Toyoko Inn, Ramada/Ramada Encore, Wyndham, Benikea Daelim, Brown Dot, Hwangnamkwan, Commodore, Lahan, Hilton, Skypark, L'Escape, ASTI, Sono Belle Cheonan) all check out. Star ratings and USD price bands were treated as planning estimates, not audit targets.
- **Apps 9/9 real:** Naver Map, KakaoMap, Kakao T, Uber/UT, KorailTalk, Subway Korea (Malang), Papago, T-money GO, BUSTAGO.
- **Places 15/15 real** famous destinations.
- **Intercity fares verified:** KTX Seoul–Busan ₩59,800 (2h30) ✓; SRT Suseo–Busan ₩52,600 ✓; KORAIL 2-Day Flexible Saver ₩121,000 ✓; express bus Seoul–Busan Premium ₩39,800 / Udeung ₩30,000 / Ilban ₩22,000 ✓; Climate Card tourist 5-day ₩15,000 ✓; Seoul taxi base ₩4,800 (night +20/+40% windows) ✓; AREX Express 43 min T1 non-stop ✓; Seoul subway ₩1,550 post-June-2025 ✓.
- **Savings guides:** referenced chains/apps all real (Myeongnyun Jinsa Galbi, Tongin Market yeopjeon lunchbox, Baemin, Shuttle Delivery, IKEA Family Korea, Outback/KFC/Starbucks KR memberships, Korea Sale Festa, Discover Seoul Pass, WOWPASS).
- **Activities 443:** names correspond to real attractions across the four cities (incl. Jangtaesan, Ppuri Park, Nexperium, Expo Aquarium, Sikjangsan observatory, Yinnyeoul/Huinnyeoul village, Provisional Capital Memorial Hall, Busan Cinema Center LED roof). No fabricated venues detected; see §4.9 for the 6 duplicate rows.

---

## 6. Provenance note

The event data errors (e.g., the BANKSY price) originate in the upstream snapshot `research/sources/fun/events.csv` — the catalog build imports it faithfully (110/110 rows map 1:1, all with `official_sources` present). The food-collection fabrication, by contrast, lives in `research/sources/food/restaurants-bookmarks.csv` itself (485 synthetic rows) and is surfaced verbatim by the app — i.e., the app pipeline is honest; the upstream food data is not.

## 7. Recommended actions

~~1. Remove the 485 synthetic food rows~~ — **DONE** (see §8).
~~2. Apply the §4 fix list~~ — **DONE** (see §8); items 3 and 5 (MCR venue) were retracted after re-verification.
3. Remaining: add a "last verified" stamp to event statuses now dated for the trip window, and re-check **Arario Museum in SPACE** opening status before the trip (still ambiguous). Also confirm **Werk Coffee Roasters** (Jeonpo, Busan) is still operating — one aggregator flags it closed, though its official site is live.

---

## 8. ✅ Remediation applied (2026-08-18)

All fixes were applied on branch `arena/01a01665-koreamasteritinerary1` and the catalogs were regenerated (`scripts/build_catalog.py` + `scripts/build_itinerary_docs.py`).

**Hallucination purge (food):**
- `research/sources/food/restaurants-bookmarks.csv`: 535 → **50 rows** (all 485 template fabrications removed; the 50 verified real restaurants kept).
- `research/sources/food/cities/seoul.md`, `busan.md`, `daejeon.md`, `cheonan.md`: **518 synthetic table rows removed** — the same template names had also been embedded in the city guide tables. Guides now hold exactly the same 50 verified spots (25 Seoul / 17 Busan / 7 Daejeon / 1 Cheonan).
- `research/sources/food/cities/walking-food-routes.md`: **33 synthetic option entries removed** (incl. stray templates "Jinja Ramen 1", "Landmark 9"), **2 notes referencing phantom routes deleted** (fictional "Routes S11–S20" and "B6–B15" that do not exist), every route's combination math **recomputed** (headers were claiming "20/15/10 alleys = 360+/1,000+ walks"; actual: 10/5/4 routes = **65 combinations**), and inflated claims corrected throughout.
- Counts corrected in `README.md` (535→**50** food bookmarks, 443→**437** activity notes), `research/sources/food/README.md` (57/60 → 50), `START-HERE.md`, `sources-and-notes.md` ("200 restaurants" claim), and regenerated `data/index.json` (`meta.counts.food: 50`, `activities: 437`).
- Stray-name spot-checks while cleaning the routes doc: **Daecheon Banjeom** (real Cheonan station-market 노포, ₩5,000 jjajang — matches the guide's description), **Sasang Galbi** (real, Busan city menu portal), **Bokseong-gak** (real Sinchon Chinese restaurant), **Cafe Yoon** (real Gijang coastal cafe), **Abyssinia Coffee** (real Cheonan cafes) all **verified real**. "**Cafe de Cheonan**" could not be verified anywhere and was **replaced** with August Scent (verified real antique cafe 333 m from Cheonan Station). "Dongsunwon Seongwan" spelling normalized to **Dongsunwon Seonghwan**.

**Factual corrections:**
- Events (source CSV + regenerated `events.json`): BANKSY price **"18000 adult" → "23000 adult; 18000 youth/child"** (VisitSeoul official); **"Busan IPark vs Chungnam Cheongju" → "Chungbuk Cheongju FC"** (2026 K League 2 club list); "Kyung Hee University Peace Hall" → **"Grand Peace Palace"** (official venue name).
- Transport (`research/sources/transport/docs/12…md`): Busan Metro fares **1,450/1,550 → 1,600 card / 1,700 cash; Section 2: 1,650 → 1,800 card (1,900 cash)** — official since the 3 May 2024 hike. Busan city bus 1,550/1,650 was already correct.
- Emergency (all 12 files incl. `emergency-card.html` + the hardcoded list in `scripts/build_catalog.py`): **+82-2-3210-0404 relabeled** — it is the ROK MOFA Consular Safety Call Center for Korean citizens abroad, NOT a tourist line; tourist-facing guidance now points to 112 / 119 / 1330 (**+82-2-1330** from overseas/roaming), with an explicit correction note in `03-emergency-contacts.md` and the emergency README.
- Tax (`research/sources/transport/data/tax_refund.json` → `data/index.json`): **VAT correctly stated as 10%**; the 7.5% figure retained but relabeled as `typical_net_refund_percent` (what tourists actually receive after refund-operator fees). Thresholds (₩15,000 / ₩1,000,000 / ₩5,000,000) already correct.
- Activities: **6 duplicate blocks removed** at the source (`research/sources/fun/seoul.md` ×2, `busan.md` ×1, `daejeon-cheonan.md` ×3); regenerated = 437 entries, zero duplicate titles.

**Retractions (original report was wrong; upstream data was right):** Dear Evan Hansen Aug 1–Nov 1 window (§4.3) and "Paradise City Culture Park" venue naming (§4.5) were both confirmed correct against official sources before any change was made to them.

---

## 9. 🔁 Second-pass independent audit (2026-08-18, branch `arena/01a01698-koreamasteritinerary1`)

A full independent re-verification pass was run **without trusting sections 1–8 above**: every collection was re-enumerated programmatically (counts, duplicates, template-name patterns, URL/coordinate/date sanity), and the factual claims — including ones this report previously marked "verified" — were re-checked against official/primary sources.

### 9.1 Prior remediation confirmed genuine

The §8 remediation is real in the merged tree: food = 50 rows (0 template patterns), activities = 437 (0 duplicate titles), Busan Metro fares corrected, MOFA number relabeled, VAT = 10%, README/meta counts consistent. No hallucinated "fixes" detected.

### 9.2 Re-verified clean against official/primary sources (spot re-check of prior claims)

- **CSAT/Suneung day** used by all 10 blueprints = **Thu Nov 19, 2026** ✅ (Ministry of Education press release).
- **Events re-confirmed** (organizer/official ticketing/press): BANKSY Still Here (Jul 22–Nov 3, ALT.1, ₩23,000/₩18,000 — exact), My Chemical Romance (Nov 7, Paradise City Culture Park), Jujutsu Kaisen in Concert (Nov 7–8, Grand Peace Palace — NOL official), Jason Mraz (Nov 14, KINTEX — jasonmraz.com), Kings of Convenience (Nov 18, Sejong Grand Theater), 5SOS (Nov 19, KINTEX Hall 1 — Interpark/NOL), MMA 2026 (Nov 14–15 Gocheok), KGMA 2026 (Nov 7–8 Gocheok), MAMA 2026 (Nov 20–21 Kyocera Dome Osaka — CJ ENM newsroom), G-STAR 2026 (Nov 19–22 BEXCO — K-GAMES), Busan Fireworks Festival (Sat Nov 7 — busanfireworks.com official), Busan Biennale "Dissident Chorus" (Aug 29–Nov 1; MoCA + Space Wonji + former Nam High School — all 3 venues match), Daejeon Wine EXPO (Nov 6–8 DCC — djwinefair.com), JTBC Seoul Marathon (Nov 1, Sangam start — en.marathon.jtbc.com), ELISABETH (Aug 16–Nov 15 Blue Square), Hell's Kitchen (Jul 24–Nov 8 GS Arts Center — Yes24), Gwanghwamun Love Song (Sep 6–Nov 15 D-Cube Link — NOL/KBS), Dear Evan Hansen (Aug 1–Nov 1 Chungmu — culture.go.kr), Leeum Inside Other Spaces (May 5–Nov 29 — leeumhoam.org), MMCA×LG OLED Christine Sun Kim (Jul 31–Nov 29 Seoul Box — MMCA/Yonhap), Changgyeonggung Mulbit Yeonhwa fall (Sep 8–Nov 8), LoL Worlds 2026 final (Nov 14, Barclays Center — repo correctly frames as watch party).
- **K League 2 fixtures against the published 2026 schedule:** Nov 7 Seoul E-Land vs Jeonnam (Mokdong 16:30) ✅ · Nov 8 Cheonan City vs Busan IPark (Cheonan Sports Complex 14:00) ✅ · Nov 21 Busan IPark vs **Chungbuk Cheongju** (Gudeok 14:00) ✅ (the §4.2 name fix is right) · Nov 22 Seoul E-Land vs Chungnam Asan (Mokdong 16:30, R33) ✅.
- **OK Savings Bank men's volleyball** relocation Ansan→Busan (Gangseo Gymnasium, from 2025-26) ✅ (KOVO board approval, Busan city).
- **Entry rules:** K-ETA exemption (incl. U.S.) through **Dec 31, 2026** ✅ (VisitKorea + ROK consulates); **e-Arrival Card sole method from Jan 1, 2026** (paper card discontinued) ✅.
- **Fares re-confirmed:** KTX Seoul–Busan ₩59,800 · SRT ₩52,600 · Seoul→Daejeon ₩23,700 · Seoul→Cheonan-Asan ₩14,100 · Seoul subway base ₩1,550 (post-Jun-2025) · Seoul/Busan taxi base ₩4,800 · Climate Card 5-day tourist pass ₩15,000 · Visit Busan Pass 24h ₩55,000 · Gwangalli M Drone Show winter schedule Sat 19:00 & 21:00 (matches blueprint text exactly).
- **Blueprint signature venues verified real:** Arario Sculpture Plaza Cheonan (Damien Hirst *Hymn*/*Charity*, Keith Haring works on-site — press-documented), P.ARK Yeongdo shipyard culture complex, Hong Dae-yong Science Museum planetarium (Cheonan Susin-myeon), Sono Belle Cheonan, Byeongcheon sundae alley, Gyejoksan red-clay trail.
- **§7 open items resolved:** **Arario Museum in SPACE is operating** (official NOL/Yanolja ticketing lists Tue–Sun 10:00–19:00 through 2026 — remove the "temporarily closed?" doubt); **Werk (베르크) Roasters Jeonpo is operating** (official site live, current listings). **August Scent (어거스트센트)** — the cafe substituted during §8 — re-verified real at 천안 공설시장2길 9-2, ~333 m from Cheonan Station Exit 1.

### 9.3 🔴 New errors found in this pass (all now FIXED and catalogs regenerated)

1. **Choryang 168 Monorail does not exist anymore** — the single biggest issue this pass. The 8-person monorail was ruled unsafe, **retired in 2023 and demolished**; a 12-person inclined elevator ("초량168계단 하늘길") replaced it, **operating since Mar 11, 2025** (Busan Dong-gu / Seoul Shinmun / Namu). Blueprints #6 (Rail) and #7 (Value) headlined riding the monorail ("free public transit; open daily 06:00–21:00" — fabricated hours for a demolished system), and it appeared in `research/sources/fun/busan.md` §67, `activities.json`, and the README highlight line. **Fixed everywhere** to the 168 Stairs + Haneul-gil inclined elevator (with Kim Min-bu observatory), and the 8-passenger "capacity watchout" updated to the elevator's 12.
2. **AREX Express fare stale: ₩11,000 → ₩13,000** (current official adult fare; ~₩11,400–11,500 only via online discount platforms). Fixed in `transport/data/routes.json` (both duplicate entries), docs 05a/05c/06/19, emergency docs 07 & 10 (which claimed "₩9,000–11,000"), and all 10 blueprint scripts. **AREX All-Stop also stale: ₩4,450 → ~₩4,750** (T1, transit card, post-Jun-2025 base-fare rise; T2 ≈ ₩5,350).
3. **Daejeon→Busan KTX fare wrong: "~₩28,500" → ₩36,200** (standard class, main line; even the cheapest via-Gupo routing is ₩30,000 — ₩28,500 matches no published fare). Fixed in all 5 Seoul·Daejeon·Busan blueprints.
4. **Cheonan-Asan→Busan KTX fare wrong: "~₩39,200" → ₩46,500** (standard class, main line; via-Gupo ≈ ₩38,800 but that is the slower routing and not what the blueprints describe). Fixed in all 5 Seoul·Cheonan·Busan blueprints.
5. **Malformed source URL** for Taepyung Sogukbap in `food.json` (`…/svc/contents/vcontsId=189445` — not a valid VisitKorea URL shape). Replaced with a standard Naver Map search URL like its peers.
6. **BRSO venue over-claim:** Nov 12–13, 2026 dates are confirmed, but Korean press lists **only Nov 13 at Seoul Arts Center; the Nov 12 venue was still unannounced ("장소 미정")**. Venue field now says so.
7. **Seoul Outdoor Library nuance:** 2026 season is **Apr 23–Jun 28 + Sep 4–Nov 1, Fri–Sun only** (summer break) — note added so no one plans a weekday visit.
8. **Bus 86 fare in Value blueprint: ₩1,500 → ₩1,550** (consistent with the repo's own corrected Busan bus fare table).

### 9.4 Advisory (no repo change needed)

- **Kingdom Buffet (Daejeon)** is real but currently lists **Fri–Sun operation only** — check before going midweek.
- The "500+ drones" phrasing for Gwangalli undersells current shows (700–1,000+) — conservative, not wrong.
- Rounded/estimated prices flagged "~" (meals, day budgets) and hotel star/price bands remain planning estimates, not audited facts.

**Second-pass verdict:** After the fixes above, no fabricated venues, restaurants, hotels, events, or phone numbers remain detectable in the served catalog. The three fare errors and the demolished-monorail recommendation were the only substantive hallucinations surviving the first audit.
