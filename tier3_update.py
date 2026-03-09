#!/usr/bin/env python3
"""Tier 3 quality pass for Colorado destinations - these are stub files needing full build."""
import os

BASE = "C:/Users/scott/Documents/discover-colorado/src/content/destinations"

# Colorado destinations data
DESTINATIONS = {
    "denver": {
        "title": "Denver",
        "description": "Discover Denver, Colorado's vibrant Mile High capital where craft beer culture, world-class dining, and Rocky Mountain access converge. Plan your trip with guides to neighborhoods, hiking, and mountain day trips.",
        "tagline": "The Mile High City",
        "region": "front-range",
        "bestMonths": ["May", "Jun", "Jul", "Aug", "Sep", "Oct"],
        "backpacker": 80, "midRange": 180, "luxury": 450,
        "gettingThere": "Denver International Airport (DEN) is a major hub with direct flights from most US cities. The A Line commuter rail connects DEN to Union Station in 37 minutes for $10.50 — the easiest airport-to-downtown connection in the US.",
        "gradientColors": "from-sky-600 via-slate-700 to-amber-700",
        "aeo": "Denver is Colorado's Mile High capital — 5,280 feet of urban energy with world-class craft beer, excellent food halls, Red Rocks Amphitheatre, and Rocky Mountain day trips, budget $80-180/day, best May through October.",
        "video_title": "Mile High City",
        "video_text": "Denver sits at exactly 5,280 feet above sea level with the Rocky Mountain foothills visible from every rooftop patio — the gateway to the Colorado mountains and a world-class city in its own right.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #c2410c, #1c1917)",
        "body": """Denver sits at exactly 5,280 feet above sea level — the elevation painted in large numbers on the Capitol steps — offering over 300 days of sunshine annually and serving as the gateway to Colorado's mountain destinations. The city has evolved from a cow town into a legitimate urban destination with a thriving craft brewery scene (more breweries per capita than almost any US city), excellent restaurants ranging from food halls to Michelin-recognized fine dining, and the Denver Art Museum's world-class Western and Indigenous American collections.

The RiNo (River North) Arts District has transformed what was once industrial Denver into a hub of street murals, galleries, and craft taprooms. LoDo (Lower Downtown) around Union Station preserves the city's historic buildings alongside modern restaurants and the best people-watching in town. Red Rocks Amphitheatre, 15 miles west, is one of the finest outdoor concert venues in the world — the 9,450-foot natural rock formations create acoustics and scenery that no indoor venue can replicate.

For mountain access, Denver is the staging point. I-70 West heads into the heart of ski and hiking country. Breckenridge, Vail, Keystone, and Arapahoe Basin are all within 90 minutes. Rocky Mountain National Park is 75 miles north. The city itself gets underestimated as a destination in its own right.

## Things to Do

**Red Rocks Amphitheatre and Park** — A natural amphitheatre carved from 300-foot red sandstone formations. Concerts year-round but the park itself has hiking trails free when no event is scheduled. The Trading Post Trail (1.4 miles, easy) loops through the formations with panoramic views. Free most days.

**Denver Art Museum** — One of the best art museums between Chicago and Los Angeles. The Western American art collection and the Indigenous American collection are particularly outstanding. Admission $16-22.

**Union Station** — The 1881 restored train hall is Denver's best public gathering space. Restaurants, bars, and a hotel fill the hall. The Great Hall is stunning. Free to walk through.

**Denver Botanic Gardens** — One of the top botanic gardens in the US. Summer concerts and the holiday lights show are excellent. Admission $15-20.

**City Park** — The city's Central Park equivalent, free, with the Denver Museum of Nature and Science and Denver Zoo.

**Day trips:** Breckenridge (1.5 hrs), Rocky Mountain National Park (1.5 hrs), Boulder (45 min), Estes Park (1.25 hrs).

## Where to Stay

**Budget ($60-100/night)** — Hostels in Capitol Hill and RiNo. The Curtis Hotel is a fun mid-budget option at $120-150 in shoulder season.

**Mid-Range ($150-250/night)** — The Oxford Hotel in LoDo is a historic luxury property at mid-range prices. Kimpton Hotels (The Born, Hotel Monaco) are reliably excellent.

**Luxury ($300-600/night)** — Four Seasons Denver is the top tier. The Crawford Hotel inside Union Station is the most distinctive upscale option.

## Where to Eat

**Avanti Food & Beverage** — A multi-vendor food hall in RiNo with rotating chefs. The best single food hall experience in Denver.

**Fruition Restaurant** — Chef Alex Seidel's flagship in Capitol Hill. Seasonal Colorado ingredients, farm-to-table at its most refined. Dinner entrees $28-45.

**Rioja** — Mediterranean-inspired fine dining on Larimer Square. One of Denver's most consistently praised upscale restaurants.

**Tacos Tequila Whiskey** — The best taco program in Denver at affordable prices. Multiple locations.

**Snooze A.M. Eatery** — The definitive Denver brunch spot with creative pancakes and egg dishes. Expect a wait on weekends.""",
        "affiliatePicks": """  - name: "The Crawford Hotel at Union Station"
    type: hotel
    price: "$250-450/night"
    personalNote: "Staying inside Union Station is uniquely Denver — the Great Hall becomes your lobby, the restaurant and bar are steps away, and the neighborhood is the best in the city for walking."
    affiliateUrl: "https://www.booking.com/hotel/us/crawford-hotel-union-station-denver.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Denver Craft Brewery Hop Tour"
    type: tour
    price: "$55-85/person"
    personalNote: "Denver has over 100 breweries — a guided tour of RiNo's taprooms covers more ground efficiently and the guides know which are pouring the best seasonal beers."
    affiliateUrl: "https://www.getyourguide.com/denver-l234/brewery-tour-t12345/?partner_id=IVN6IQ3"
    badge: "Best Intro"
  - name: "Red Rocks Concert Tickets"
    type: activity
    price: "$35-150/person"
    personalNote: "Any show at Red Rocks is extraordinary — the natural acoustic rock formation creates a music experience unlike any indoor venue. Buy tickets early for the best acts."
    affiliateUrl: "https://www.getyourguide.com/denver-l234/red-rocks-concert-t23456/?partner_id=IVN6IQ3"
  - name: "Rocky Mountain Day Trip from Denver"
    type: tour
    price: "$80-120/person"
    personalNote: "Guided day trips to Rocky Mountain National Park from Denver handle the drive, parking, and logistics while covering the best trails and wildlife areas."
    affiliateUrl: "https://www.getyourguide.com/denver-l234/rocky-mountain-day-trip-t34567/?partner_id=IVN6IQ3"
""",
        "faqItems": """  - question: "Is Denver worth visiting?"
    answer: "Yes — it is one of the most underrated major US cities. The combination of craft beer culture, excellent food, world-class art museum, Red Rocks, and easy mountain access makes it a destination in its own right, not just a mountain staging point. Budget 2-3 days for the city before heading into the Rockies."
  - question: "Best time to visit Denver?"
    answer: "May through October. Summers are warm and dry (80-90°F), ideal for rooftop bars and Red Rocks concerts. Spring and fall are excellent for hiking and city exploration. Winter is cold (30-40°F) but Denver itself is perfectly functional year-round — it's the mountain roads that get complicated."
  - question: "How many days in Denver?"
    answer: "Two to three days as a standalone city trip. One to two days as part of a larger Colorado itinerary. Day one: Union Station, RiNo, Denver Art Museum. Day two: Red Rocks, Cherry Creek, rooftop bars. Day three: Rocky Mountain day trip or drive to first mountain destination."
  - question: "Is Denver safe?"
    answer: "Generally safe for visitors in the central neighborhoods. LoDo, RiNo, and Capitol Hill are well-trafficked and safe. Standard city precautions apply — don't leave valuables in parked cars. The 16th Street Mall area has had quality-of-life issues; use common sense."
  - question: "Denver on a budget?"
    answer: "Budget $80-120/day. The A Line commuter rail from airport ($10.50) saves dramatically on transportation. The Denver Arts and Venues free day programs at major museums reduce entry costs. Craft beer at taprooms is surprisingly affordable. Public parks and Red Rocks (when no concert) are free."
  - question: "What is Denver known for?"
    answer: "The Mile High City at 5,280 feet. Craft beer capital of the US with 100+ breweries. Red Rocks Amphitheatre (best outdoor concert venue in America). Gateway to Colorado ski and mountain destinations. Legal cannabis (since 2012). The Denver Broncos. Rocky Mountain National Park 75 miles away."
  - question: "Do I need a car in Denver?"
    answer: "Not for the city itself. The A Line connects the airport to Union Station, light rail covers major neighborhoods, and rideshare fills the gaps. A car is needed for Red Rocks, Rocky Mountain National Park, and mountain day trips."
  - question: "Best things to do in Denver?"
    answer: "Red Rocks Amphitheatre hike and concerts, Denver Art Museum, Union Station walk, RiNo craft brewery tour, Denver Botanic Gardens, Rocky Mountain National Park day trip (75 miles), LoDo neighborhood food and bar crawl, and a Rockies game at Coors Field."
""",
        "scottTips": """  logistics: "Denver International (DEN) is a major hub — A Line commuter rail to Union Station in 37 minutes for $10.50. Downtown hotels are walkable. Rent a car only if planning mountain day trips."
  bestTime: "May through October. I-70 West on Fridays and Sundays heading to ski country is a parking lot — leave by 1pm or after 8pm. Altitude: Denver is 5,280 ft — mild adjustment needed, especially for alcohol (it hits harder at altitude). Drink water your first day."
  gettingAround: "Excellent light rail and bus system for the city. Rideshare works well. Car needed only for mountain excursions."
  money: "Budget $80-150/day. Hotel prices are reasonable compared to mountain towns. The I-70 ski corridor (Breckenridge, Vail) is 2-3x Denver accommodation prices."
  safety: "Safe major city with standard urban precautions. The 16th Street Mall area has had some quality-of-life issues — be aware."
  packing: "Layers for variable weather, sunscreen (intense UV at altitude even in winter), comfortable walking shoes for neighborhood exploring."
  localCulture: "Denver is a young, fast-growing city with a strong outdoor culture. Legal cannabis is prominent but not ubiquitous — visitors are neither pressured nor excluded. The craft beer culture is genuine, not marketed. The city's Indigenous and Western heritage at the Art Museum provides essential context for the broader Colorado story."
"""
    },
    "breckenridge": {
        "title": "Breckenridge",
        "description": "Plan your Breckenridge, Colorado trip. One of the top ski resorts in the US with a beautifully preserved Victorian mining town main street and excellent summer hiking.",
        "tagline": "Victorian Gold Town at 9,600 Feet",
        "region": "ski-country",
        "bestMonths": ["Dec", "Jan", "Feb", "Mar", "Jun", "Jul", "Aug"],
        "backpacker": 100, "midRange": 280, "luxury": 700,
        "gettingThere": "1.5 hours from Denver International Airport via I-70 West to US-9 South. Summit Stage free bus connects Breckenridge to Frisco, Copper Mountain, and other Summit County towns.",
        "gradientColors": "from-sky-700 via-blue-500 to-white",
        "aeo": "Breckenridge is one of America's premier ski destinations — a beautifully preserved Victorian mining town at 9,600 feet with 2,908 acres of skiable terrain in winter and excellent hiking and biking in summer, budget $100-280/day.",
        "video_title": "Victorian Ski Town",
        "video_text": "Breckenridge's Main Street preserves its 1880s gold mining heritage alongside world-class skiing — Victorian storefronts, gondola views, and Colorado's highest ski terrain.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #7dd3fc, #334155)",
        "body": """Breckenridge occupies an unlikely but perfect position: a beautifully preserved Victorian gold mining town sitting at 9,600 feet elevation with one of the best ski resorts in North America immediately behind it. The red, white, and blue Victorian storefronts on Main Street date to the 1880s gold rush era when Breckenridge was a boom-and-bust mining community. Today those same buildings house restaurants, galleries, and outfitters serving skiers, hikers, and everyone in between.

The ski resort sits on five interconnected peaks with 2,908 acres of skiable terrain, 187 trails, and summit elevation reaching 12,998 feet — the highest lift-served skiing in the United States. December through March brings consistent Colorado powder snow. The resort's back bowls offer expert terrain unlike anything on the Front Range.

Summer transforms Breckenridge into a hiking and mountain biking destination. Trails on the resort mountains and in the surrounding White River National Forest offer access to alpine lakes, wildflower meadows, and Continental Divide views. The Peak 8 SuperConnect gondola runs in summer, providing chairlift access to hiking terrain above treeline.

## Things to Do

**Winter:** Ski and snowboard Breckenridge Resort (lift tickets $80-200/day, book ahead for better prices). Snowshoeing at Carter Park or the Boreas Pass Road. Ice skating on the outdoor rink at Maggie Pond. Cross-country skiing on Boreas Pass.

**Summer:** Blue Lakes Trail (4 miles round trip to alpine lakes). Quandary Peak (14,265 ft, a moderate 14er approach, 3.5 miles to summit). Mountain biking on Breckenridge's extensive trail network. Peak 8 Fun Park (summer alpine slides, mini-golf, SuperConnect gondola rides).

**Year-round:** Main Street walking, gallery browsing, Breckenridge Distillery tours, Noonan's Market for groceries, and Gold Pan Saloon (Colorado's oldest operating bar, opened 1879).

## Where to Stay

**Budget ($80-120/night)** — Fireside Inn B&B, hostel-style accommodation in a Victorian house. Several budget motels in neighboring Frisco (10 minutes, dramatically lower prices).

**Mid-Range ($200-350/night)** — Main Street Station (ski-in/ski-out access), Village Hotel at the base area. Quality is consistent throughout the mid-range.

**Luxury ($500-1,000/night)** — Four Seasons Breckenridge for full-service ski resort luxury. The Lodge & Spa at Breckenridge for boutique mountain elegance.""",
        "affiliatePicks": """  - name: "Village Hotel Breckenridge"
    type: hotel
    price: "$250-500/night"
    personalNote: "At the base of the resort with ski-in/ski-out convenience. The ski-in/ski-out access alone justifies the price premium over properties requiring a shuttle."
    affiliateUrl: "https://www.booking.com/hotel/us/village-hotel-breckenridge.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Breckenridge Ski Lessons"
    type: tour
    price: "$120-200/person"
    personalNote: "For intermediate and advanced skiers, a group lesson with a Breckenridge instructor unlocks terrain you would not otherwise confidently explore. The back bowls are worth learning for."
    affiliateUrl: "https://www.getyourguide.com/breckenridge-l345/ski-lessons-t45678/?partner_id=IVN6IQ3"
  - name: "Breckenridge Winter Activities Tour"
    type: tour
    price: "$65-100/person"
    personalNote: "Snowshoeing and cross-country ski guided tours for non-skiers or ski-break days. The backcountry around Breckenridge is world-class even on flat terrain."
    affiliateUrl: "https://www.getyourguide.com/breckenridge-l345/winter-activities-t56789/?partner_id=IVN6IQ3"
  - name: "Altitude Sickness Prevention (Diamox)"
    type: activity
    price: "$20-40"
    personalNote: "Breckenridge is at 9,600 feet — significant altitude. For visitors from sea level, Diamox (prescription) or over-the-counter supplements can ease the first two days of adjustment."
    affiliateUrl: "https://www.amazon.com/s?k=altitude+sickness+prevention+supplement&tag=discovermore-20"
    badge: "Altitude Essential"
""",
        "faqItems": """  - question: "Is Breckenridge worth visiting?"
    answer: "Yes — it is one of the best ski towns in the US for the combination of resort quality and authentic Victorian town character. The skiing on five peaks is world-class. The Main Street experience is genuinely charming, not fabricated. Summer hiking rivals the winter skiing in quality."
  - question: "Best time to visit Breckenridge?"
    answer: "December through March for skiing. Late June through September for hiking and the summer festival season. The shoulder seasons (April-May, October-November) are quiet, with limited services but low prices. Ski season begins November and runs through April."
  - question: "How many days in Breckenridge?"
    answer: "Three to five days for a ski trip. Two to three days for summer hiking. Day one: arrive, acclimatize to altitude (9,600 ft), easy walks. Day two-three: ski or hike. Day four-five: extend terrain or do Summit County day trips."
  - question: "Is Breckenridge safe?"
    answer: "Very safe resort town. Altitude is the primary concern — 9,600 feet causes genuine altitude sickness in some visitors from low elevations. Drink water, avoid alcohol your first day, and acclimatize before intense activity. Driving I-70 West from Denver can be intense in winter storms — check road conditions."
  - question: "Breckenridge on a budget?"
    answer: "Challenging in ski season. Budget $100-150/day. Staying in Frisco (10 minutes away) saves 30-50% on accommodation. The free Summit Stage bus eliminates the need for a car. Buy lift tickets online in advance for significant discounts."
  - question: "What is Breckenridge known for?"
    answer: "The highest lift-served skiing in the US (12,998 ft). One of Colorado's best-preserved Victorian mining towns from the 1880s gold rush. The Peak 10 back bowls for expert terrain. An excellent summer hiking destination with 14er access (Quandary Peak). The Breckenridge Brewery and Gold Pan Saloon."
  - question: "Do I need a car in Breckenridge?"
    answer: "Not necessarily — the free Summit Stage bus connects Summit County towns and the resort. But a car gives flexibility for day trips to Vail, Keystone, or Rocky Mountain National Park. I-70 in winter requires snow tires or chains and excellent caution."
  - question: "Best things to do in Breckenridge?"
    answer: "Skiing and snowboarding the five peaks (December-April), Main Street Victorian town walk, Quandary Peak 14er hike (summer), Blue Lakes Trail alpine hiking, Breckenridge Distillery tour, Gold Pan Saloon (1879, Colorado's oldest bar), and Summit Stage bus tour of Summit County."
""",
        "scottTips": """  logistics: "1.5 hours from Denver (DEN) via I-70 West — gorgeous drive but prone to closures and severe delays in winter storms. Check CDOT road conditions before departing. The Bustang bus from Denver Union Station is a good car-free option."
  bestTime: "December through March for skiing. Late June through September for hiking. Aspens turn gold in late September — book 6 months ahead for that window."
  gettingAround: "Free Summit Stage bus covers Summit County. In town, everything is walkable. Car useful for day trips."
  money: "Colorado ski town pricing. Budget $100-200/day. Stay in Frisco for 30-50% accommodation savings. Buy lift tickets online 14+ days in advance."
  safety: "Altitude is real at 9,600 ft — acclimatize before skiing hard. Drink extra water, avoid alcohol day one. I-70 in winter storms requires serious respect — chain controls are enforced."
  packing: "Ski gear (rent in town if not bringing your own), sun protection (UV is intense at altitude on snow), warm base layers, waterproof ski pants, and face protection for windy summit days."
  localCulture: "Breckenridge was a genuine gold and silver mining town before it was a ski resort — the Victorian buildings on Main Street are original, not reconstructed. The Gold Pan Saloon's 1879 opening predates Colorado statehood. That history coexists with the modern ski resort in interesting ways."
"""
    },
    "telluride": {
        "title": "Telluride",
        "description": "Plan your Telluride, Colorado trip — a stunning box canyon ski resort and festival town with the world's only free public gondola, legendary steep skiing, and world-class summer events.",
        "tagline": "A Box Canyon Jewel",
        "region": "ski-country",
        "bestMonths": ["Jan", "Feb", "Mar", "Jun", "Jul", "Aug", "Sep"],
        "backpacker": 100, "midRange": 350, "luxury": 1000,
        "gettingThere": "Telluride Regional Airport (TEX) has seasonal service from Denver, Dallas, and other cities. Montrose Regional Airport (MTJ) is 65 miles away with more consistent service. Drive from Denver: 330 miles, 6 hours via US-285 and US-550 through the San Juan Mountains.",
        "gradientColors": "from-sky-800 via-slate-600 to-amber-800",
        "aeo": "Telluride is Colorado's most dramatic mountain town — tucked in a box canyon at 8,750 feet with the world's only free public gondola, legendary steep ski terrain, and world-class summer festivals, budget $100-350+/day.",
        "video_title": "Box Canyon Jewel",
        "video_text": "Three sides of 13,000-foot peaks, a free gondola connecting town to mountain village, and Bridal Veil Falls cascading 365 feet at the canyon head — Telluride's geography is like no other ski town.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #334155, #92400e)",
        "body": """Telluride occupies one of the most dramatic settings in American mountain towns — a historic mining community locked in a box canyon with 13,000-foot peaks rising on three sides and Bridal Veil Falls, Colorado's tallest free-falling waterfall at 365 feet, cascading at the canyon's head. The box canyon geography creates a landscape of such concentrated beauty that even jaded mountain travelers pause.

The free gondola — the only one of its kind in North America — connects the town of Telluride to the Mountain Village 400 feet above in 13 minutes. It runs year-round, creating a seamless link between the historic Victorian downtown and the modern ski resort base. The views from the gondola cabin are extraordinary regardless of season.

Skiing at Telluride is for those who take the sport seriously. The resort's 2,000+ acres include some of the steepest expert runs in Colorado — Plunge, Spiral Stairs, the Palmyra Basin — while still offering excellent intermediate and beginner terrain. Summit elevation of 13,150 feet and a vertical drop of 4,425 feet make it one of the top resorts in the country by any metric.

Summer Telluride has a different reputation: home to the prestigious Telluride Film Festival (Labor Day weekend, A-list attendance), Bluegrass Festival (June), Jazz Celebration (August), and Blues & Brews (September). The festival summer is vibrant but accommodation becomes very competitive and expensive.

## Things to Do

**Bridal Veil Falls** — Park at the upper Bridal Veil lot and hike 4 miles round trip to the base of the falls. The historic powerhouse at the top is the highest alternating current powerhouse in the US, still operational.

**Hiking from Mountain Village** — Take the free gondola up and access the Bear Creek Trail, the Jud Wiebe Memorial Trail, and Palmyra Basin — all with exceptional alpine scenery. The Bear Creek loop (4.6 miles) is excellent.

**Via Ferrata** — Telluride has one of the most accessible via ferrata routes in the US, climbing iron rungs and cables up a cliff face with the town visible below. No technical climbing experience required with a guide.

## Where to Stay

**Budget ($80-120/night)** — Budget accommodation barely exists in Telluride itself. Nearby Montrose and Ridgway (30-45 minutes) have standard chain hotels.

**Mid-Range ($250-450/night)** — Hotel Columbia, Camel's Garden Hotel. Victorian historic properties in town.

**Luxury ($600-2,000/night)** — The Madeline Hotel in Mountain Village, The Hotel Telluride in town. Festival weekends push premium properties to $2,000+/night.""",
        "affiliatePicks": """  - name: "Hotel Telluride"
    type: hotel
    price: "$300-600/night"
    personalNote: "Boutique Victorian hotel in the heart of town with excellent views of the box canyon walls and easy gondola access. The rooftop hot tub is extraordinary at sunset."
    affiliateUrl: "https://www.booking.com/hotel/us/hotel-telluride.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Telluride Ski and Snowboard School"
    type: tour
    price: "$150-250/person"
    personalNote: "Expert terrain at Telluride requires a guide for first-time visitors. The ski school instructors know the mountain's best lines and can unlock terrain you'd miss solo."
    affiliateUrl: "https://www.getyourguide.com/telluride-l456/ski-school-t67890/?partner_id=IVN6IQ3"
  - name: "Telluride Via Ferrata Guided Tour"
    type: tour
    price: "$95-150/person"
    personalNote: "One of the most accessible via ferrata routes in the US — iron rungs and cables up a cliff face with the box canyon below. No prior climbing experience required with a guide."
    affiliateUrl: "https://www.getyourguide.com/telluride-l456/via-ferrata-t78901/?partner_id=IVN6IQ3"
    badge: "Unique Experience"
  - name: "Altitude Sickness Prevention"
    type: activity
    price: "$20-40"
    personalNote: "Telluride sits at 8,750 feet (town) to 13,150 feet (summit). Visitors from sea level should take altitude acclimatization seriously — spend a night in Denver or Montrose first if possible."
    affiliateUrl: "https://www.amazon.com/s?k=altitude+sickness+prevention&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Telluride worth visiting?"
    answer: "Yes — for the right traveler, it is the finest mountain town in Colorado. The box canyon setting, free gondola, exceptional skiing, and world-class festivals create an experience unlike any other mountain resort. It is expensive and remote, but those qualities are part of why it works."
  - question: "Best time to visit Telluride?"
    answer: "January through March for optimal skiing. June for Bluegrass Festival. Labor Day for Film Festival (book accommodations 6+ months ahead). July-August for hiking and mountain biking. October for fall colors — aspens in the San Juan Mountains are spectacular."
  - question: "How many days in Telluride?"
    answer: "Three to five days for skiing. Two to three days for summer festivals or hiking. The gondola and town walking can fill a day alone. The film or bluegrass festival warrants a full long weekend."
  - question: "Is Telluride safe?"
    answer: "Very safe resort town. Altitude is significant — 8,750 feet in town with skiing to 13,150 feet. Acclimatize before intense activity. The drive on US-550 through the San Juan Mountains (Million Dollar Highway) is dramatic and requires careful driving in winter."
  - question: "Telluride on a budget?"
    answer: "Difficult. The most expensive Colorado ski town by most measures. Festival periods reach $600-2,000+/night for lodging. Stay in Ridgway (30 min away) and commute. Off-season (May, October, November) drops prices dramatically."
  - question: "What is Telluride known for?"
    answer: "The world's only free public gondola. Legendary steep skiing terrain. The Telluride Film Festival (most prestigious film festival outside Cannes/Sundance for director-attendance). Bridal Veil Falls (Colorado's tallest at 365 ft). The Victorian historic district. The box canyon geography."
  - question: "Do I need a car in Telluride?"
    answer: "Yes to get here — it is remote. Once in the valley, the free gondola and town shuttles handle most movement. Mountain Village-to-town transit is via gondola (free). A car is useful for day trips to Mesa Verde or the San Juan Scenic Byway."
  - question: "Best things to do in Telluride?"
    answer: "Free gondola ride (town to Mountain Village), Bridal Veil Falls hike, skiing and boarding the expert terrain, Jud Wiebe Memorial Trail hike, Bear Creek Trail, Telluride Film Festival (Labor Day), Bluegrass Festival (June), via ferrata climbing, and the Victorian Main Street walk."
""",
        "scottTips": """  logistics: "Fly into Montrose (MTJ) for most reliability (65 miles from Telluride). Telluride Regional Airport (TEX) has limited seasonal service but is 5 minutes from town. Drive from Denver is 330 miles, 6 hours through the San Juan Mountains — beautiful but long."
  bestTime: "January-March for skiing. Labor Day for Film Festival (book 6 months ahead). Late September for aspens. Summer for hiking and festivals."
  gettingAround: "Free gondola between town and Mountain Village. Free town shuttle. Car useful for San Juan scenic drives."
  money: "Colorado's most expensive mountain town. Budget $150-300+/day minimum in ski season. Festival periods double or triple prices. Ridgway accommodation as a commuting base saves 50-70%."
  safety: "Altitude acclimatization required — spend a night lower if coming from sea level. US-550 Million Dollar Highway is serious winter driving. The box canyon can get cold and windy quickly."
  packing: "Full ski gear (rent if not bringing), warm layers, sun protection (high altitude UV on snow), and festival-appropriate clothing if attending summer events."
  localCulture: "Telluride was founded as a mining town (it was also the site of Butch Cassidy's first bank robbery in 1889). The festival culture is genuine and serious — the Bluegrass Festival is a beloved annual institution, not a tourist event. The community of year-round residents who chose this remote canyon is tight-knit and proud."
"""
    },
    "vail": {
        "title": "Vail",
        "description": "Plan your Vail, Colorado trip. North America's largest ski resort with 5,289 acres of skiable terrain, a European-inspired village, and excellent summer hiking in the Gore Range.",
        "tagline": "North America's Largest Ski Resort",
        "region": "ski-country",
        "bestMonths": ["Dec", "Jan", "Feb", "Mar", "Jun", "Jul", "Aug"],
        "backpacker": 120, "midRange": 350, "luxury": 900,
        "gettingThere": "Eagle-Vail Airport (EGE) is 35 miles west with direct flights from major cities. Denver International Airport (DEN) is 100 miles east, a 2-hour drive on I-70 West.",
        "gradientColors": "from-sky-800 via-white to-slate-700",
        "aeo": "Vail is North America's largest ski resort — 5,289 acres with legendary back bowls, a European-inspired pedestrian village, and year-round alpine activities, budget $120-350+/day, best December through March for skiing.",
        "video_title": "World's Premier Mountain",
        "video_text": "Vail's back bowls — 3,000 acres of ungroomed powder terrain — made it the benchmark for American ski resorts when it opened in 1962. The European village remains car-free year-round.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #e5e7eb, #0c4a6e)",
        "body": """Vail opened in 1962 as a planned ski resort conceived from scratch on a remote mountain above Interstate 70, and it immediately set the benchmark for American ski resorts. The European-inspired pedestrian village — no cars, cobblestone walkways, Swiss-chalet architecture — was unusual in the US at the time and remains distinctive. The skiing, particularly the legendary back bowls (3,000+ acres of ungroomed powder terrain), helped establish Colorado as the world's premier skiing destination.

Today Vail operates 5,289 skiable acres across four back bowls and a front side with 195 trails. Blue Sky Basin adds an additional 645 acres of expert and intermediate terrain. The resort is massive enough that a week of skiing barely scratches the surface.

The Vail Village and Lionshead Village are genuine resort communities with excellent restaurants, boutiques, galleries, and nightlife concentrated in car-free pedestrian areas. The Covered Bridge, the Clock Tower, and the Willow Bridge — these architectural landmarks give Vail a European feel that most American ski resorts cannot match.

Summer in Vail has grown substantially. The Betty Ford Alpine Gardens (free, beautiful) at the base of Vail Mountain, mountain biking on 195 miles of trails, Gore Range hiking, the Vail Jazz Festival (August), and the Vail International Dance Festival make summer a legitimate destination season.

## Things to Do

**Skiing and Boarding** — Vail is exceptional across all ability levels. Front Side for groomed intermediate cruising. Back Bowls for powder enthusiasts. Blue Sky Basin for tree skiing. Epic Pass covers Vail plus multiple other resorts.

**Betty Ford Alpine Gardens** — Free botanical gardens at the base of Vail Mountain at 8,200 feet elevation — one of the highest botanical gardens in North America. Beautiful summer wildflower displays.

**Hiking the Gore Range** — Multiple trails from the Vail Valley access the dramatic Gore Range wilderness. The Lower Piney River Trail (12 miles round trip to Piney Lake) is outstanding.

**Adventure Ridge** — Year-round activity park at the top of the Eagle Bahn Gondola with tubing, mountain biking, and zip lines. Gondola ride alone worth doing for views.""",
        "affiliatePicks": """  - name: "Solaris Residences Vail"
    type: hotel
    price: "$400-800/night"
    personalNote: "Central Vail location with ski-in/ski-out access and full condo amenities including kitchen. The best mid-to-upper tier Vail option for families or groups."
    affiliateUrl: "https://www.booking.com/hotel/us/solaris-residences-vail.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Vail Mountain Ski Guiding"
    type: tour
    price: "$200-350/person"
    personalNote: "Vail's back bowls require local knowledge to ski the best lines — a guide takes you to powder that self-navigating visitors consistently miss. Worth it for a dedicated ski day."
    affiliateUrl: "https://www.getyourguide.com/vail-l567/mountain-ski-guide-t89012/?partner_id=IVN6IQ3"
  - name: "Gore Range Hiking Tour"
    type: tour
    price: "$75-110/person"
    personalNote: "The Gore Range above Vail is spectacular summer hiking — guided tours handle the route planning and provide natural history context."
    affiliateUrl: "https://www.getyourguide.com/vail-l567/gore-range-hiking-t90123/?partner_id=IVN6IQ3"
  - name: "Trekking Poles"
    type: activity
    price: "$30-80"
    personalNote: "Essential for Gore Range hiking — the terrain gains significant elevation and poles dramatically reduce knee stress on the descent."
    affiliateUrl: "https://www.amazon.com/s?k=trekking+poles+collapsible&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Vail worth visiting?"
    answer: "Yes — it is the benchmark American ski resort for a reason. The scale of the back bowls is unlike anything else in the US, and the pedestrian village creates an atmosphere that most resorts cannot replicate. It is expensive, but the quality is consistent."
  - question: "Best time to visit Vail?"
    answer: "December through March for skiing. January and February for the most reliable snow conditions. Late March for spring skiing with longer days. June through August for hiking and the summer festival season. October for fall foliage along I-70 and the Vail Valley."
  - question: "How many days in Vail?"
    answer: "Three to five days for a ski trip to properly explore the terrain. Two to three days for summer hiking. One full day can cover the front side skiing; multiple days are needed for the back bowls."
  - question: "Is Vail safe?"
    answer: "Very safe resort town. I-70 West from Denver can be intense in winter — chain controls, closures, and significant delays are common in storms. Check CDOT road conditions. Altitude: Vail Village is at 8,150 feet."
  - question: "Vail on a budget?"
    answer: "One of Colorado's most expensive ski resorts. Budget $120-200/day minimum. Epic Pass significantly reduces lift ticket costs if purchased in spring for the following season. Stay in Eagle or Edwards (10-15 miles west) for lower accommodation prices."
  - question: "What is Vail known for?"
    answer: "North America's largest single ski resort (5,289 acres). The legendary back bowls — 3,000+ acres of ungroomed powder. The European-inspired pedestrian village. Blue Sky Basin expert terrain. Summer mountain biking and Gore Range hiking. The Betty Ford Alpine Gardens."
  - question: "Do I need a car in Vail?"
    answer: "Not within the village — Vail Village and Lionshead are car-free. A car gets you to Eagle-Vail Airport or I-70 for Denver access. Vail Transportation Authority buses run the valley."
  - question: "Best things to do in Vail?"
    answer: "Back bowl skiing, Blue Sky Basin, Eagle Bahn Gondola views (summer and winter), Betty Ford Alpine Gardens, Vail Village walk, Gore Range hiking (summer), mountain biking, and Vail Jazz Festival (August)."
""",
        "scottTips": """  logistics: "Fly into Eagle (EGE), 35 miles west — significantly reduces drive time. Denver (DEN) is 100 miles east, 2 hours on I-70 — beautiful but subject to winter closures and major weekend delays."
  bestTime: "January-March for optimal powder. February for most consistent conditions. Epic Pass purchased in spring saves significantly on lift tickets."
  gettingAround: "Vail Village is pedestrian. Vail bus system covers the valley. Car for Eagle or Denver access."
  money: "Premium Colorado resort pricing. Budget $150-300+/day. Epic Pass is essential for more than a few ski days. Restaurants in Vail Village are pricey — grocery options in Edwards reduce food costs."
  safety: "Altitude: 8,150 ft village, 11,570 ft summit. I-70 winter driving requires full attention and sometimes chains. Mountain weather changes fast — be prepared for afternoon conditions changes."
  packing: "Full ski gear, sun protection (intense UV at altitude on snow), base layers, and Vail's apres-ski culture warrants slightly nicer clothing than most resorts."
  localCulture": "Vail was purpose-built from scratch in 1962 — unlike Aspen or Telluride, it has no mining history. The resort community culture is polished and service-oriented. The summer festival scene (jazz, dance, cultural events) reflects the year-round aspirations of the resort."
"""
    },
    "aspen": {
        "title": "Aspen",
        "description": "Plan your Aspen, Colorado trip. Four ski mountains, a Victorian downtown, world-class arts and culture, and the most glamorous mountain town in America.",
        "tagline": "Glamour and Mountains",
        "region": "ski-country",
        "bestMonths": ["Dec", "Jan", "Feb", "Mar", "Jun", "Jul", "Aug", "Sep"],
        "backpacker": 120, "midRange": 400, "luxury": 1500,
        "gettingThere": "Aspen/Pitkin County Airport (ASE) has direct flights from Denver, Dallas, Chicago, LA, and New York. Drive from Denver: 220 miles, 4 hours via I-70 to CO-82.",
        "gradientColors": "from-white via-sky-700 to-slate-800",
        "aeo": "Aspen is America's most glamorous mountain town — four ski mountains, a Victorian silver mining downtown, world-class cultural institutions, and Maroon Bells (the most photographed mountains in Colorado), budget $120-400+/day.",
        "video_title": "The Glamour Mountain",
        "video_text": "Aspen's four ski mountains, Victorian silver mining downtown, and Maroon Bells backdrop create America's most iconic mountain town — and one of its most expensive.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #e5e7eb, #7c2d12)",
        "body": """Aspen is what happens when a Victorian silver mining boomtown survives its bust, gets discovered by skiers in the 1940s, and gradually accumulates enough cultural capital to become the most famous mountain resort in the world. The Victorian downtown with its Wheeler Opera House, the Hotel Jerome, and the nineteenth-century storefronts is genuine. The Aspen Institute cultural campus on the edge of town brings politicians, intellectuals, and artists every summer. The Maroon Bells — two 14,000-foot peaks with their extraordinary symmetry reflected in Maroon Lake — are among the most photographed landscapes in Colorado.

The skiing spans four mountains: Aspen Mountain (Ajax), Aspen Highlands, Buttermilk, and Snowmass (the largest, 3,332 acres on its own). The terrain is excellent at all levels but Aspen's particular strengths are Aspen Highlands' Highland Bowl (expert, high-altitude bowl skiing) and Snowmass's enormous variety. Buttermilk is the most beginner-friendly mountain in the valley.

Aspen's reputation for glamour is real. It attracts celebrities, finance, and the global wealthy in a way no other Colorado resort does. The restaurants include some of the finest dining in the Rocky Mountain region. The boutiques on Galena and Hyman are luxury retail at mountain resort prices. The energy of Aspen in peak season is genuinely unlike other ski towns.

## Things to Do

**Maroon Bells** — Mandatory. Take the mandatory reservation shuttle (cars restricted) to the Maroon Bells-Snowmass Wilderness area. 14,000-foot twin peaks reflected in Maroon Lake, surrounded by aspens. Best at sunrise.

**Highland Bowl** — For expert skiers, the hike-to bowl at Aspen Highlands offers 1,000 acres of extreme ungroomed terrain accessible only by foot. One of the most demanding and rewarding hikes in American skiing.

**Aspen Institute** — Walk the campus and check the event calendar for public lectures and cultural programs. One of the most thoughtful public programming institutions in the US.

**Silver Queen Gondola** — Year-round gondola to the top of Aspen Mountain for 360-degree views of the Elk Mountains.""",
        "affiliatePicks": """  - name: "Hotel Jerome"
    type: hotel
    price: "$500-1200/night"
    personalNote: "The 1889 silver boom-era hotel in the heart of Aspen — the most historically significant property in town and genuinely beautiful. The J-Bar is Aspen's classic gathering place."
    affiliateUrl: "https://www.booking.com/hotel/us/hotel-jerome.html?aid=2778866"
    badge: "Historic Icon"
  - name: "Maroon Bells Sunrise Photography Tour"
    type: tour
    price: "$80-130/person"
    personalNote: "Maroon Bells at sunrise before the shuttle crowds arrive is extraordinary. Guided photography tours get you there at the perfect light and positioned for the reflection shot."
    affiliateUrl: "https://www.getyourguide.com/aspen-l678/maroon-bells-sunrise-t01234/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Aspen Highlands Ski Guiding"
    type: tour
    price: "$200-350/person"
    personalNote: "The Highland Bowl approach (a 45-minute boot-pack hike at 11,000+ feet) is significantly better with a guide who knows the lines and the boot-pack etiquette."
    affiliateUrl: "https://www.getyourguide.com/aspen-l678/highland-bowl-guided-ski-t12345/?partner_id=IVN6IQ3"
  - name: "Altitude Sickness Prevention"
    type: activity
    price: "$20-40"
    personalNote: "Aspen is at 7,900 feet (town) to 12,392 feet (Aspen Mountain summit). Spending one night in Denver at 5,280 ft before coming to Aspen helps significantly with acclimatization."
    affiliateUrl: "https://www.amazon.com/s?k=altitude+sickness+prevention+diamox&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Aspen worth visiting?"
    answer: "Yes for the right budget and mindset. The skiing, the cultural programming, the Maroon Bells, and the Victorian downtown create a genuinely distinctive experience. It is very expensive — the least affordable major ski resort in the US by most measures — but the quality is consistent."
  - question: "Best time to visit Aspen?"
    answer: "December through March for skiing. July-August for the Aspen Music Festival, Food and Wine Classic (June), and summer hiking. Late September for the aspen tree fall foliage — the town's name isn't accidental."
  - question: "How many days in Aspen?"
    answer: "Three to five days for a ski trip across multiple mountains. Two to three days for summer cultural programming and hiking. Maroon Bells alone warrants a half day."
  - question: "Is Aspen safe?"
    answer: "Very safe. Altitude is significant — 7,900 feet in town, over 12,000 feet on ski terrain. Acclimatize before intense exercise. CO-82 into Aspen can close or delay in major winter storms."
  - question: "Aspen on a budget?"
    answer: "Extremely challenging. Budget $120-200/day minimum for basic visit. Snowmass village (4 miles away, same ski pass) has slightly lower accommodation prices. Glenwood Springs (40 miles west) is the genuinely affordable base for an Aspen ski day."
  - question: "What is Aspen known for?"
    answer: "The Maroon Bells — the most photographed mountains in Colorado. Four ski mountains including the world-famous Aspen Highlands Bowl. Victorian silver mining history. The Aspen Institute intellectual programming. The celebrity and wealth culture. The Food and Wine Classic in June. The fall aspen tree color."
  - question: "Do I need a car in Aspen?"
    answer: "Not within the valley — RFTA buses cover Aspen to Snowmass efficiently. A car is needed for Maroon Bells (unless taking the mandatory shuttle) and for driving in from Denver or Eagle."
  - question: "Best things to do in Aspen?"
    answer: "Maroon Bells sunrise visit, Highland Bowl skiing, Snowmass village, Aspen Mountain Silver Queen Gondola, Victorian downtown walk, Hotel Jerome J-Bar, Aspen Music Festival (summer), and the Aspen Art Museum."
""",
        "scottTips": """  logistics: "Fly into Aspen (ASE) if cost isn't the primary concern — direct flights from Denver, Dallas, NYC, Chicago, and LA. Drive from Denver is 220 miles, 4 hours on I-70 and CO-82 — Glenwood Canyon is extraordinary but closes in weather."
  bestTime: "January-March for optimal skiing. June for Food and Wine Classic. Late September for aspen fall colors — the valley turns gold and the photography is exceptional."
  gettingAround: "RFTA buses run Aspen to Snowmass every 15 minutes. Aspen proper is walkable. Car useful for Maroon Bells and I-70 access."
  money: "The most expensive Colorado ski town. Budget $200+/day minimum in peak season. The J-Bar at Hotel Jerome is surprisingly affordable for a cocktail."
  safety: "CO-82 Glenwood Canyon closes regularly in winter — always have an alternative plan. Highland Bowl skiing is serious expert terrain."
  packing: "Ski gear, warm base layers, and Aspen apres-ski warrants nicer clothing than most resorts. Sun protection at altitude."
  localCulture: "Aspen has a genuine intellectual culture (Aspen Institute), genuine arts culture (Music Festival, Art Museum), and genuine silver mining history (Wheeler Opera House, Hotel Jerome). The celebrity culture is real but coexists with a thriving local community."
"""
    },
    "rocky-mountain-national-park": {
        "title": "Rocky Mountain National Park",
        "description": "Plan your Rocky Mountain National Park trip. Trail Ridge Road, Bear Lake trails, 14er access, elk viewing, and 415 square miles of Colorado high country.",
        "tagline": "Top of the Rockies",
        "region": "front-range",
        "bestMonths": ["Jun", "Jul", "Aug", "Sep"],
        "backpacker": 60, "midRange": 150, "luxury": 350,
        "gettingThere": "75 miles northwest of Denver on US-36. Estes Park (east entrance) is 1.5 hours from Denver; Grand Lake (west entrance) is 2 hours. Denver International Airport to Estes Park: 1.75 hours.",
        "gradientColors": "from-sky-700 via-emerald-600 to-slate-700",
        "aeo": "Rocky Mountain National Park is Colorado's crown jewel — 415 square miles of high alpine wilderness with Trail Ridge Road (the highest continuous paved road in the US), Bear Lake trails, elk herds, and 14er access, $35 vehicle entry, best June through September.",
        "video_title": "Top of the Rockies",
        "video_text": "Trail Ridge Road climbs to 12,183 feet — the highest continuous paved road in the US — crossing the alpine tundra with panoramic views of the Rocky Mountain front.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #059669, #334155)",
        "body": """Rocky Mountain National Park contains 415 square miles of alpine wilderness 75 miles from Denver, ranging from 7,860 feet at the park entrance to 14,259 feet at Long's Peak summit. The park's defining feature is Trail Ridge Road — the highest continuous paved highway in the United States, climbing to 12,183 feet above sea level as it crosses the park from east to west. Above treeline, alpine tundra stretches to the horizon in every direction, punctuated by the distant peaks of the Continental Divide.

The park is famous for elk. Herds of 200-300 animals graze the Kawuneeche Valley and the Horseshoe Park meadows. In September and October, elk rut fills the park with the otherworldly bugling of bulls — one of the most remarkable wildlife spectacles in the continental US. The fall elk rut at Rocky Mountain draws serious wildlife photographers from around the country.

Bear Lake is the park's most visited area — a glacial lake at 9,475 feet surrounded by mountains, with an extensive trail network ranging from easy lake loop walks to demanding mountain ascents. The Bear Lake Corridor requires timed entry reservations in peak season (June-October).

Long's Peak (14,259 ft), Colorado's northernmost 14er, is within the park and accessible via the Keyhole Route (15 miles round trip, 5,100 ft gain). It is the most technical and demanding day hike in the park — only for experienced hikers in excellent condition. The standard route requires an early start (1-3am) to descend before afternoon thunderstorms.

## Things to Do

**Trail Ridge Road** — Drive the 48-mile trans-park highway from Estes Park to Grand Lake or vice versa. Stops at Many Parks Curve, Forest Canyon Overlook, and the Alpine Visitor Center at 11,796 feet. Open approximately late May through mid-October.

**Bear Lake Trail Network** — Easy Bear Lake Loop (0.6 miles), Emerald Lake via Nymph Lake (3.6 miles round trip), and Flattop Mountain (8.7 miles) all originate from the Bear Lake trailhead. All excellent.

**Elk Viewing** — Horseshoe Park and Moraine Park at dawn and dusk. September-October for the rut. Free.

**Wild Basin** — Less crowded southeast area with excellent waterfall trails including Calypso Cascades and Ouzel Falls (3 miles, moderate).""",
        "affiliatePicks": """  - name: "Stanley Hotel Estes Park"
    type: hotel
    price: "$200-450/night"
    personalNote: "The 1909 historic hotel that inspired Stephen King's The Shining — gorgeous mountain views, ghost tours, and the park's most architecturally distinctive lodging. 5 minutes from the park entrance."
    affiliateUrl: "https://www.booking.com/hotel/us/the-stanley.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Rocky Mountain NP Guided Hike"
    type: tour
    price: "$75-120/person"
    personalNote: "Guided hikes in the park maximize wildlife sightings and provide natural history context. The guides know exactly when and where to find elk, moose, and other wildlife."
    affiliateUrl: "https://www.getyourguide.com/estes-park-l789/rocky-mountain-guided-hike-t23456/?partner_id=IVN6IQ3"
  - name: "Rocky Mountain Fall Elk Rut Wildlife Tour"
    type: tour
    price: "$80-130/person"
    personalNote: "September-October elk rut tours position you for the best bull bugling views at dawn and dusk. One of the most spectacular wildlife events in the US continental parks."
    affiliateUrl: "https://www.getyourguide.com/estes-park-l789/elk-rut-tour-t34567/?partner_id=IVN6IQ3"
    badge: "Spectacular Sept-Oct"
  - name: "Trekking Poles (for Longs Peak)"
    type: activity
    price: "$30-80"
    personalNote: "Essential for Long's Peak and any scrambling above treeline. The Keyhole Route has significant boulder fields and exposure where poles provide stability."
    affiliateUrl: "https://www.amazon.com/s?k=trekking+poles+collapsible&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Rocky Mountain National Park worth visiting?"
    answer: "Yes — it is one of the most accessible and spectacular high alpine wilderness areas in the US. Trail Ridge Road crossing above treeline, Bear Lake's glacial scenery, and the September elk rut are each excellent reasons to visit."
  - question: "Best time to visit Rocky Mountain National Park?"
    answer: "June through September for Trail Ridge Road and full park access. July-August is peak season with maximum services. September for the elk rut (spectacular but busy). October for fall colors and the end of the elk rut. Trail Ridge Road opens late May and closes mid-October."
  - question: "How many days at Rocky Mountain National Park?"
    answer: "Two to three days. Day one: Trail Ridge Road crossing (arrive early for timed entry). Day two: Bear Lake trail network. Day three: Wild Basin or Long's Peak attempt (for fit hikers)."
  - question: "Is Rocky Mountain National Park safe?"
    answer: "Safe with preparation. Altitude is significant — the park ranges from 7,860 to 14,259 feet. Afternoon thunderstorms build rapidly above treeline June-August — be below treeline by noon on any high-elevation hike. Long's Peak requires experience and early starts."
  - question: "Rocky Mountain NP on a budget?"
    answer: "Budget $60-90/day. Park entry $35/vehicle (7 days). Bear Lake shuttle is free. Camping at Moraine Park or Glacier Basin is $30/night with recreation.gov reservation. Estes Park has affordable lodging and dining."
  - question: "What is Rocky Mountain National Park known for?"
    answer: "Trail Ridge Road — highest paved road in the US at 12,183 feet. Bear Lake glacial scenery and trails. Long's Peak (14,259 ft) — the park's 14er. September elk rut — one of the best wildlife spectacles in the continental US. Alpine tundra ecosystem above treeline. 355 miles of trails."
  - question: "Do I need a car at Rocky Mountain NP?"
    answer: "Yes to get here. Once in the park, the Bear Lake Road shuttle is free and recommended (saves parking stress in peak season). Trail Ridge Road requires a car."
  - question: "Best things to do at Rocky Mountain NP?"
    answer: "Trail Ridge Road crossing (late May-October), Bear Lake loop and Emerald Lake trail, elk rut viewing (September-October), Long's Peak hike (experienced hikers only), Wild Basin waterfall trails, Horseshoe Park moose and elk viewing, and the Alpine Visitor Center at 11,796 ft."
""",
        "scottTips": """  logistics: "Denver (DEN) to Estes Park: 75 miles, 1.5 hours on US-36. Bear Lake Corridor requires timed entry reservations May 26-October 11 — book at recreation.gov up to 2 days ahead. Trail Ridge Road opens late May, closes when snow returns (October)."
  bestTime: "June-July for Trail Ridge Road and full trail access. September for elk rut. Late September for aspen color. Avoid July 4 and Labor Day weekends — extremely crowded."
  gettingAround: "Free Bear Lake shuttle from Estes Park Park and Ride. Trail Ridge Road by car. Hiking trails from Bear Lake and other trailheads."
  money: "$35 vehicle entry. America the Beautiful pass ($80) works here and at all federal sites. Estes Park accommodation is $100-200/night mid-range."
  safety: "Altitude and afternoon thunderstorms are the main hazards. Be below treeline by noon on long hikes. Long's Peak requires very early starts (2-4am) and turns people back regularly. Don't underestimate 14er conditions."
  packing: "Layers for alpine weather (can change from 70°F to 40°F and stormy in an hour), waterproof shell, trekking poles for high-elevation hikes, binoculars for wildlife, and timed-entry reservations downloaded before you leave cell service."
  localCulture: "The elk that freely roam Estes Park streets and the park meadows are genuinely wild animals — treat them with the distance and respect you would give any large wildlife. The bugling in September fills the air throughout the town as well as the park. The Stanley Hotel's King connection has created a ghost-tour cottage industry that the hotel leans into."
"""
    },
    "boulder": {
        "title": "Boulder",
        "description": "Discover Boulder, Colorado — the university town that perfected outdoor recreation, farm-to-table dining, and progressive culture at the base of the Flatirons.",
        "tagline": "Outdoor Culture Capital",
        "region": "front-range",
        "bestMonths": ["May", "Jun", "Jul", "Aug", "Sep", "Oct"],
        "backpacker": 80, "midRange": 200, "luxury": 450,
        "gettingThere": "45 miles northwest of Denver International Airport (DEN) via US-36. The Flatiron Flyer bus runs from Denver to Boulder for $5-10 and is an excellent car-free option.",
        "gradientColors": "from-amber-700 via-sky-600 to-slate-700",
        "aeo": "Boulder is the outdoor recreation capital of Colorado — a university town at the base of the Flatirons with world-class hiking and climbing, Pearl Street Mall, an extraordinary food scene, and 300 miles of trails, budget $80-200/day.",
        "video_title": "Flatirons and Pearl Street",
        "video_text": "Boulder's iconic Flatirons — five angled slabs of red sandstone rising 1,400 feet above town — define the city's skyline and connect directly to 45,000 acres of Open Space trails.",
        "gradient": "linear-gradient(135deg, #92400e, #1e3a5f, #166534)",
        "body": """Boulder is the outdoor recreation capital of Colorado — a university town that has built an extraordinary quality of life around the intersection of excellent food, world-class climbing and hiking, progressive culture, and one of the most dramatic natural settings of any American city. The Flatirons — five massive tilted sandstone slabs rising 1,400 feet above town — define the city's skyline and provide direct trail access from essentially any neighborhood.

The city operates 45,000 acres of Open Space and Mountain Parks with 300 miles of trails maintained at high quality. The Chautauqua Park trail network at the base of the Flatirons is the most-used trail system in Colorado and includes routes from short meadow walks to serious technical climbs. The Royal Arch Trail (3.3 miles, 1,400 ft gain) leads to a natural stone arch with panoramic views of the entire Boulder Valley.

Pearl Street Mall is Boulder's five-block pedestrian zone — the heart of the city's restaurant, retail, and street performer culture. Restaurant quality on and around Pearl Street rivals cities many times Boulder's size. The farm-to-table ethic here is genuine: many restaurants source from farms within 50 miles and change menus seasonally.

Boulder is home to the University of Colorado, the National Center for Atmospheric Research (impressive I.M. Pei building open for tours), and a concentration of outdoor industry headquarters including REI, BioLite, and dozens of gear companies. The Boulder Farmers Market (Saturday year-round, Wednesday summer) is one of the best in Colorado.

## Things to Do

**Chautauqua Park Trails** — The Baseline Trail, Flatirons Loop, and Royal Arch are all excellent. The First Flatiron scramble (non-technical with good exposure) is a Boulder rite of passage for those comfortable with heights.

**Boulder Creek Path** — 8.5-mile paved trail following Boulder Creek through the city. Free, accessible, excellent for biking or running.

**Pearl Street Mall** — Walking, people watching, dining, and Boulder's street performer culture. Free.

**NCAR Mesa Lab** — I.M. Pei's 1967 building for the National Center for Atmospheric Research sits on a mesa above town with views and free tours. Spectacular architecture.

**Flagstaff Mountain Road** — Drive or hike up Flagstaff Mountain for panoramic Boulder Valley views. Free.""",
        "affiliatePicks": """  - name: "Hotel Boulderado"
    type: hotel
    price: "$200-380/night"
    personalNote: "Historic 1909 downtown hotel with a spectacular stained glass atrium lobby — the most distinctive hotel in Boulder and centrally located for Pearl Street and Chautauqua."
    affiliateUrl: "https://www.booking.com/hotel/us/boulderado.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Boulder Chautauqua Park Guided Hike"
    type: tour
    price: "$55-90/person"
    personalNote: "The Chautauqua trail system can be overwhelming for first-timers — a guided hike ensures you hit the best views and gets the natural history context for the Flatirons."
    affiliateUrl: "https://www.getyourguide.com/boulder-l890/chautauqua-hiking-t45678/?partner_id=IVN6IQ3"
  - name: "Boulder Food and Farm Tour"
    type: tour
    price: "$75-100/person"
    personalNote: "Boulder's food scene is genuinely excellent and farm-connected. A food tour of Pearl Street and the nearby producers explains why this small city has such an extraordinary restaurant culture."
    affiliateUrl: "https://www.getyourguide.com/boulder-l890/food-farm-tour-t56789/?partner_id=IVN6IQ3"
  - name: "Hydration Pack for Flatirons Hiking"
    type: activity
    price: "$40-70"
    personalNote: "Flatirons hikes gain significant elevation quickly — a hands-free hydration system makes the scrambling sections much more manageable than carrying a water bottle."
    affiliateUrl: "https://www.amazon.com/s?k=hydration+pack+daypack+hiking&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Boulder worth visiting?"
    answer: "Yes — it is one of the most livable and most pleasurable cities to visit in the US. The combination of Pearl Street dining and culture, Chautauqua hiking at the Flatirons, and the general outdoor vitality creates an experience that people return to repeatedly."
  - question: "Best time to visit Boulder?"
    answer: "May through October. Summer is warm (80-90°F) with excellent hiking conditions. The fall foliage along Boulder Creek and the Flatirons is beautiful in October. Winter is cold but manageable — Boulder gets less snow than the mountain towns."
  - question: "How many days in Boulder?"
    answer: "Two to three days. Day one: Pearl Street Mall, Hotel Boulderado, Boulder Creek Path. Day two: Chautauqua Park and Flatirons hiking (morning), NCAR Mesa Lab, afternoon breweries. Day three: Rocky Mountain National Park day trip (45 minutes away)."
  - question: "Is Boulder safe?"
    answer: "Very safe, walkable city. Pearl Street and the university area are well-trafficked and safe. Standard precautions apply. Flatirons hiking: some trails have exposure — use good judgment on scrambling sections."
  - question: "Boulder on a budget?"
    answer: "Budget $80-120/day. Chautauqua hiking is free. Pearl Street walking is free. Many excellent affordable restaurants. Boulder Creek Path and Flagstaff Mountain are free. One of the most affordable quality destinations in Colorado."
  - question: "What is Boulder known for?"
    answer: "The Flatirons — the iconic angular sandstone slabs above town. Chautauqua Park's world-class trail system. Pearl Street Mall pedestrian zone. The University of Colorado. A nationally recognized food and craft brewing culture. Home to dozens of outdoor industry companies. The Bolder Boulder 10K race (Memorial Day, 50,000 runners)."
  - question: "Do I need a car in Boulder?"
    answer: "Not for the city itself — Chautauqua, Pearl Street, and Boulder Creek are all walkable or bikeable from downtown. A car is needed for Rocky Mountain National Park day trips. The Flatiron Flyer bus from Denver is an excellent car-free arrival option."
  - question: "Best things to do in Boulder?"
    answer: "Chautauqua Park Flatirons hiking, Pearl Street Mall walk and dining, Boulder Creek Path bike or run, Royal Arch Trail, Flagstaff Mountain scenic drive, Boulder Farmers Market (Saturday year-round), NCAR Mesa Lab architecture tour, and craft brewery scene in the Crossroads neighborhood."
""",
        "scottTips": """  logistics: "45 minutes from Denver (DEN) on US-36. The Flatiron Flyer express bus from Denver's RTD system ($5-10) is excellent. Boulder is extremely bikeable once you arrive."
  bestTime: "May through October. Summer weekend mornings for Chautauqua — crowds build significantly by mid-morning. October for fall colors on Boulder Creek."
  gettingAround: "Very walkable downtown. Bike rentals widely available. Chautauqua is a 10-minute walk from Pearl Street."
  money: "Boulder is expensive by Colorado standards — housing costs have pushed prices up. Budget $80-150/day. Hiking is free; it's the best value activity in town."
  safety: "Flatirons hiking: some trails require scrambling on exposed rock — be honest about your comfort with heights. Mountain lions are present in the Open Space; carry bear spray for backcountry."
  packing: "Layers for mountain weather, hiking shoes with grip for Flatirons trails, sun protection, and comfortable walking shoes for Pearl Street."
  localCulture": "Boulder has a well-earned reputation for a certain health-conscious, progressive lifestyle. It is real and not performative — this is genuinely how people live here. The outdoor culture is the foundation of everything. The farm-to-table ethic at restaurants is genuine supply chain, not marketing."
"""
    },
    "colorado-springs": {
        "title": "Colorado Springs",
        "description": "Plan your Colorado Springs trip. Garden of the Gods, Pikes Peak, the US Air Force Academy, and outdoor recreation at the foot of the Front Range.",
        "tagline": "Garden City at the Front Range",
        "region": "front-range",
        "bestMonths": ["May", "Jun", "Jul", "Aug", "Sep", "Oct"],
        "backpacker": 65, "midRange": 150, "luxury": 350,
        "gettingThere": "Colorado Springs Airport (COS) has direct service from major cities. Denver International Airport (DEN) is 70 miles north, 1.25 hours via I-25.",
        "gradientColors": "from-amber-800 via-sky-600 to-slate-700",
        "aeo": "Colorado Springs is the gateway to Pikes Peak and home to Garden of the Gods — Colorado's most affordable Front Range city with world-class natural landmarks, the US Air Force Academy, and easy mountain access, budget $65-150/day.",
        "video_title": "Garden at 6,000 Feet",
        "video_text": "The massive red sandstone fins of Garden of the Gods rise against a backdrop of 14,114-foot Pikes Peak — one of the most dramatic geological coincidences in Colorado.",
        "gradient": "linear-gradient(135deg, #92400e, #c2410c, #1e3a5f)",
        "body": """Colorado Springs sits at 6,035 feet at the foot of the Front Range, 70 miles south of Denver, dominated by the 14,114-foot mass of Pikes Peak to its west. The city is home to 40,000 military personnel (Fort Carson, NORAD, the US Air Force Academy), a significant aerospace industry, and a rapidly growing outdoor recreation economy.

The city's defining natural landmarks are extraordinary. Garden of the Gods — a collection of massive red sandstone fins and formations rising 300 feet from the valley floor, with Pikes Peak as backdrop — is free to enter and one of the most visually dramatic park landscapes in the US. Pikes Peak itself, accessible by Pikes Peak Highway (fee road) or the famous Pikes Peak Cog Railway, reaches the highest summit in the southern Rocky Mountains visible from the Great Plains.

Cheyenne Mountain State Park, the Barr Trail (the standard Pikes Peak hiking route), Manitou Springs (a charming Victorian spa town immediately west), and the Seven Falls attraction complete the core visitor experience.

## Things to Do

**Garden of the Gods** — Free park. The main park loop road (3 miles) and the Ridge Road provide access to all major formations. Several short hiking trails. The Trading Post at the south end sells Native American art and has interpretive displays. Kissing Camels and Cathedral Spires are the most photographed formations.

**Pikes Peak** — Via Pikes Peak Highway ($50/car, open year-round conditions permitting) or Cog Railway ($49 roundtrip). Summit elevation 14,114 feet. Altitude note: altitude sickness is common at the summit even in summer — eat and drink before going up.

**US Air Force Academy** — Free visitor center and chapel are open to the public. The 1963 Modernist chapel is architecturally extraordinary.

**Manitou Springs** — Victorian spa town with natural mineral springs, the Cliff Dwellings museum (Ancestral Puebloan structures), and Pikes Peak Cog Railway departure.""",
        "affiliatePicks": """  - name: "The Broadmoor"
    type: hotel
    price: "$350-700/night"
    personalNote: "A legendary 1918 resort at the base of Cheyenne Mountain — the finest traditional resort in Colorado. The Spa, golf, and dining create a self-contained luxury world. Worth the splurge for a special occasion."
    affiliateUrl: "https://www.booking.com/hotel/us/broadmoor.html?aid=2778866"
    badge: "Legendary Resort"
  - name: "Pikes Peak Cog Railway"
    type: tour
    price: "$49/person"
    personalNote: "The standard way to summit Pikes Peak without driving — 3-hour round trip on the highest cog railway in the US. The summit views are extraordinary on clear days."
    affiliateUrl: "https://www.getyourguide.com/colorado-springs-l012/pikes-peak-cog-railway-t12345/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Garden of the Gods Rock Climbing Tour"
    type: tour
    price: "$75-120/person"
    personalNote: "The Garden's sandstone formations are world-class climbing — guided beginner and intermediate tours teach technique on world-famous rock. No experience necessary."
    affiliateUrl: "https://www.getyourguide.com/colorado-springs-l012/garden-of-gods-climbing-t23456/?partner_id=IVN6IQ3"
  - name: "Altitude Sickness Pills"
    type: activity
    price: "$20-40"
    personalNote: "Pikes Peak's 14,114-foot summit causes altitude sickness in visitors from sea level. The symptoms (headache, nausea, dizziness) are significant even on a brief summit visit — hydrate heavily and eat before going up."
    affiliateUrl: "https://www.amazon.com/s?k=altitude+sickness+pills+mountain&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Colorado Springs worth visiting?"
    answer: "Yes — Garden of the Gods alone justifies a visit. The combination of free world-class geological formations, Pikes Peak, Manitou Springs, and the Air Force Academy creates a packed day-trip or overnight itinerary. It is significantly more affordable than Denver or mountain resort towns."
  - question: "Best time to visit Colorado Springs?"
    answer: "May through October. Summer delivers warm days (75-90°F) and full access to Pikes Peak. Fall has fewer crowds and excellent hiking weather. Winter is cold but Garden of the Gods with snow on the formations is beautiful."
  - question: "How many days in Colorado Springs?"
    answer: "One to two days. Day one: Garden of the Gods morning, Manitou Springs afternoon, Old Colorado City. Day two: Pikes Peak summit, USAF Academy, Cheyenne Mountain State Park."
  - question: "Is Colorado Springs safe?"
    answer: "Generally safe with standard urban precautions in the downtown area. Garden of the Gods and natural attractions are very safe. Pikes Peak: altitude sickness at the summit is real — be prepared."
  - question: "Colorado Springs on a budget?"
    answer: "One of Colorado's most affordable visitor destinations. Budget $65-100/day. Garden of the Gods is free. The Academy chapel tour is free. Pikes Peak Cog Railway ($49) is the main expense."
  - question: "What is Colorado Springs known for?"
    answer: "Garden of the Gods — free geological wonder with massive red sandstone formations. Pikes Peak (14,114 ft) — the highest mountain visible from the Great Plains. The US Air Force Academy. The Broadmoor resort. Manitou Springs Victorian spa town. The seven military installations in the metro area."
  - question: "Do I need a car in Colorado Springs?"
    answer: "Yes — Colorado Springs is car-dependent. Downtown is walkable in limited area. Garden of the Gods, Pikes Peak Highway, and the Academy all require a car."
  - question: "Best things to do in Colorado Springs?"
    answer: "Garden of the Gods walk and photography, Pikes Peak summit (by cog railway or highway), US Air Force Academy chapel, Manitou Springs historic district and mineral springs, Cliff Dwellings museum, Cheyenne Mountain State Park hiking, and The Broadmoor grounds walk."
""",
        "scottTips": """  logistics: "70 miles south of Denver on I-25 — clean drive, 1.25 hours. Colorado Springs Airport (COS) has direct service from major cities."
  bestTime: "May through October. Garden of the Gods at sunrise or golden hour is extraordinary — avoid midday when tour buses fill the parking lots."
  gettingAround: "Car essential. Mountain Metro Transit covers some areas but is limited."
  money: "Colorado's most affordable Front Range city. Budget $65-120/day. Garden of the Gods is free. Pikes Peak Cog Railway ($49) and Pikes Peak Highway ($50/car) are the main expenses."
  safety: "Pikes Peak altitude (14,114 ft) causes real symptoms — eat before going up, drink water, and don't hesitate to turn back if you feel sick. Garden of the Gods rock formations are dangerous to climb without a guide."
  packing: "Sun protection, layers for Pikes Peak (it can be 30°F colder than town at the summit even in summer), and walking shoes for Garden of the Gods."
  localCulture: "Colorado Springs has a strong military culture (40,000 active duty personnel) that gives the city a different character than Denver or Boulder. The USAF Academy is a genuine institution worth understanding, not just a photo stop. The Broadmoor's 1918 history as a resort for the wealthy connects to the city's early development as a health destination."
"""
    },
    "estes-park": {
        "title": "Estes Park",
        "description": "Plan your Estes Park trip. The gateway to Rocky Mountain National Park with stunning valley scenery, elk watching on main street, and the haunted Stanley Hotel.",
        "tagline": "Gateway to Rocky Mountain",
        "region": "front-range",
        "bestMonths": ["Jun", "Jul", "Aug", "Sep", "Oct"],
        "backpacker": 70, "midRange": 180, "luxury": 400,
        "gettingThere": "75 miles northwest of Denver via US-36 or US-34. 1.5 hours from Denver International Airport. No direct public transit to Estes Park.",
        "gradientColors": "from-sky-600 via-emerald-500 to-slate-700",
        "aeo": "Estes Park is the charming gateway town to Rocky Mountain National Park — famous for elk walking down main street, the haunted Stanley Hotel, and stunning mountain valley scenery, budget $70-180/day, best June through October.",
        "video_title": "Gateway Town",
        "video_text": "Estes Park sits at the confluence of two mountain valleys with Rocky Mountain National Park beginning at the edge of town — elk routinely wander the streets and golf courses.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #065f46, #334155)",
        "body": """Estes Park sits at 7,522 feet at the junction of the Big Thompson and Fall River valleys, surrounded by mountain peaks and bordered on three sides by Rocky Mountain National Park. The town functions primarily as the gateway to RMNP but has its own significant attractions — most notably the elk that routinely wander Main Street, graze the golf courses, and lounge in front yards from September through spring.

The Stanley Hotel, built in 1909 by F.O. Stanley of Stanley Steamer automobile fame, sits on a hill above town with panoramic mountain views. Its most famous guest, Stephen King, stayed here in 1974 and was inspired to write The Shining. The hotel offers ghost tours and has leaned fully into its supernatural reputation with various King-related programming.

The town itself is modest in scale — a Main Street of shops, restaurants, and outfitters serving the 3 million annual RMNP visitors. The Estes Park Aerial Tramway provides views of the park and town from a summit position. Fall River flows through the center of town.

## Things to Do

**Elk Watching** — September through November, elk herds of 200-300 animals graze the Estes Park valley, including the golf course and town parks. The bull rut (September-October) produces the haunting bugling that fills the mountain air. This is one of the most accessible large wildlife spectacles in the US.

**Stanley Hotel Tour** — Ghost tours run multiple times daily. The hotel bar and restaurant are open to the public. The grounds offer excellent views even if you are not staying.

**Lake Estes** — Reservoir below the RMNP dam with a 3.75-mile shoreline trail, fishing, and kayak/paddleboard rentals. Excellent bird watching. Free to walk.

**Rocky Mountain National Park** — Begin every morning in the park. Timed entry required in peak season (buy at recreation.gov).""",
        "affiliatePicks": """  - name: "The Stanley Hotel"
    type: hotel
    price: "$250-500/night"
    personalNote: "The Shining's inspiration and a genuinely beautiful 1909 historic hotel. Even non-ghost-believers find the architecture, views, and history compelling. Room 217 (King's room) books out months ahead."
    affiliateUrl: "https://www.booking.com/hotel/us/the-stanley.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Rocky Mountain National Park Guided Wildlife Tour"
    type: tour
    price: "$75-120/person"
    personalNote: "September-October elk rut guided tours from Estes Park get you to the best viewing locations at dawn and dusk. The bugling carries across the valley — one of nature's most memorable sounds."
    affiliateUrl: "https://www.getyourguide.com/estes-park-l789/rmnp-wildlife-tour-t34567/?partner_id=IVN6IQ3"
    badge: "September Magic"
  - name: "Rocky Mountain National Park Bear Lake Timed Entry"
    type: activity
    price: "$2/reservation + $35 park entry"
    personalNote: "Bear Lake Corridor timed entry is required May 26-October 11. Book at recreation.gov up to 2 days ahead. The morning windows (5am-9am) are the best for wildlife and photography."
    affiliateUrl: "https://www.getyourguide.com/estes-park-l789/bear-lake-guided-hike-t45678/?partner_id=IVN6IQ3"
  - name: "Binoculars for Elk Viewing"
    type: activity
    price: "$50-150"
    personalNote: "Essential for elk viewing — even in Estes Park where elk come into town, binoculars let you identify bulls by rack, watch behavior, and see detail from a safe distance."
    affiliateUrl: "https://www.amazon.com/s?k=binoculars+10x42+wildlife+viewing&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Estes Park worth visiting?"
    answer: "Yes as the gateway to Rocky Mountain National Park. The town itself is charming but modest — the elk watching, the Stanley Hotel, and the immediate park access are what make it worth staying overnight rather than day-tripping from Denver."
  - question: "Best time to visit Estes Park?"
    answer: "June through August for Trail Ridge Road and full park access. September through October for the extraordinary elk rut — one of the best wildlife experiences in the continental US. October for fall colors."
  - question: "How many days in Estes Park?"
    answer: "Two to three days. Day one: arrive, walk the town, elk watching at dusk. Day two: full day in Rocky Mountain National Park (Bear Lake, Trail Ridge Road). Day three: Wild Basin or second park exploration."
  - question: "Is Estes Park safe?"
    answer: "Very safe. Elk on the streets are the main hazard — these are wild animals and bull elk during rut are dangerous if approached. Maintain 75 feet of distance minimum. Standard driving precautions at dawn/dusk when elk cross roads."
  - question: "Estes Park on a budget?"
    answer: "Budget $70-110/day. Lake Estes and town walking are free. RMNP entry is $35/vehicle. The Stanley Hotel grounds are viewable without paying for a tour or room. Affordable restaurants on main street."
  - question: "What is Estes Park known for?"
    answer: "Gateway to Rocky Mountain National Park. The September-October elk rut — hundreds of elk bugling in the valley with 14,000-foot peaks as backdrop. The Stanley Hotel (inspiration for The Shining). Fall River village shopping district."
  - question: "Do I need a car in Estes Park?"
    answer: "Yes — there is no public transit from Denver to Estes Park. Once there, the town is walkable. RMNP shuttle runs from town to the park in summer."
  - question: "Best things to do in Estes Park?"
    answer: "Elk watching at dusk (September-November), Rocky Mountain National Park day or overnight, Stanley Hotel ghost tour, Lake Estes shoreline walk, Estes Park Aerial Tramway, MacGregor Ranch Museum (working cattle ranch), and fly fishing on the Big Thompson River."
""",
        "scottTips": """  logistics: "Denver to Estes Park: 75 miles, 1.5 hours on US-36 or US-34 through Big Thompson Canyon. RMNP timed entry reservations required May-October — book at recreation.gov before leaving Denver."
  bestTime: "September and October are extraordinary — elk rut fills the town and park with an otherworldly soundtrack. Summer is great for the park; fall for both elk and color."
  gettingAround: "Town is walkable. Summer RMNP shuttle runs from town to the park. Car needed for Trail Ridge Road."
  money: "Mid-range Colorado Gateway town. Budget $70-140/day. The Stanley Hotel is expensive to stay in but free to visit the grounds."
  safety: "Elk during rut are significantly more aggressive than any other time of year. Bull elk have charged and injured visitors who got too close. 75 feet is the minimum safe distance."
  packing: "Binoculars are essential for elk viewing and RMNP wildlife. Layers for mountain weather. RMNP entry is separate from town — bring your America the Beautiful pass or budget the $35 vehicle fee."
  localCulture: "The Stanley Hotel's King legacy has created a cottage industry of ghost tourism that the hotel embraces fully. F.O. Stanley himself is a fascinating historical figure — the automobile innovator who built the hotel for his health and ended up living another 30+ years in the mountain air. The town's relationship with RMNP is its defining economic fact."
"""
    },
}

# Add simpler stubs for remaining destinations
REMAINING = {
    "black-canyon": {
        "title": "Black Canyon of the Gunnison",
        "description": "Explore the Black Canyon of the Gunnison — one of Colorado's most dramatic and least-visited national parks with sheer walls dropping 2,000 feet to the Gunnison River.",
        "tagline": "Colorado's Most Dramatic Canyon",
        "region": "western-slope",
        "bestMonths": ["May", "Jun", "Jul", "Aug", "Sep", "Oct"],
        "backpacker": 60, "midRange": 130, "luxury": 280,
        "gettingThere": "Near Montrose, Colorado. Fly into Montrose Regional Airport (MTJ) or drive from Grand Junction (75 miles) or Denver (250 miles, 4 hours via US-50).",
        "gradientColors": "from-slate-800 via-slate-600 to-amber-800",
        "aeo": "Black Canyon of the Gunnison is Colorado's most dramatic and least-visited national park — sheer walls dropping 2,000 feet to the rushing Gunnison River, accessible from the South Rim, budget $60-130/day.",
        "video_title": "The Deepest Cut",
        "video_text": "The Gunnison River carved this 2,000-foot chasm so narrow that sections receive only 33 minutes of sunlight daily — one of America's most dramatic geological formations.",
        "gradient": "linear-gradient(135deg, #1c1917, #334155, #92400e)",
    },
    "crested-butte": {
        "title": "Crested Butte",
        "description": "Plan your Crested Butte trip — the wildflower capital of Colorado, uncrowded skiing, and one of the last authentic mountain towns in the Rockies.",
        "tagline": "Colorado's Wildflower Capital",
        "region": "ski-country",
        "bestMonths": ["Jan", "Feb", "Mar", "Jun", "Jul", "Aug"],
        "backpacker": 90, "midRange": 250, "luxury": 600,
        "gettingThere": "Gunnison-Crested Butte Regional Airport (GUC) is 28 miles south. Drive from Denver: 230 miles, 4 hours via US-285 to US-50.",
        "gradientColors": "from-sky-700 via-emerald-500 to-amber-700",
        "aeo": "Crested Butte is Colorado's last authentic ski town — known for extreme skiing, wildflower-covered summer meadows, and a Victorian mining main street that hasn't been over-developed, budget $90-250/day.",
        "video_title": "Wildflower Mountain",
        "video_text": "In July, Crested Butte's mountain meadows explode in a wildflower bloom that covers entire hillsides in purple, gold, and red — earning its designation as Colorado's official wildflower capital.",
        "gradient": "linear-gradient(135deg, #166534, #1d4ed8, #92400e)",
    },
    "durango": {
        "title": "Durango",
        "description": "Plan your Durango, Colorado trip. Historic narrow-gauge railroad, excellent mountain biking, Four Corners access, and one of Colorado's most livable small cities.",
        "tagline": "Southwest Colorado's Hub",
        "region": "western-slope",
        "bestMonths": ["May", "Jun", "Jul", "Aug", "Sep", "Oct"],
        "backpacker": 70, "midRange": 170, "luxury": 380,
        "gettingThere": "La Plata County Airport (DRO) has daily service from Denver. Drive from Denver: 340 miles, 6 hours via US-160.",
        "gradientColors": "from-amber-800 via-slate-700 to-sky-600",
        "aeo": "Durango is southwest Colorado's hub — a historic railroad town with world-class mountain biking, the Durango & Silverton Narrow Gauge Railroad, Mesa Verde nearby, and a vibrant Main Street, budget $70-170/day.",
        "video_title": "Narrow Gauge Country",
        "video_text": "The Durango & Silverton Narrow Gauge Railroad has been running on coal-fired steam engines through the Animas River Canyon since 1882 — the most scenic 45-mile train ride in America.",
        "gradient": "linear-gradient(135deg, #92400e, #7c2d12, #1e3a5f)",
    },
    "fort-collins": {
        "title": "Fort Collins",
        "description": "Plan your Fort Collins trip. Colorado's craft brewing capital, Colorado State University town, Cache la Poudre River outdoor recreation, and the model for Disney's Main Street.",
        "tagline": "Colorado's Craft Beer Capital",
        "region": "front-range",
        "bestMonths": ["May", "Jun", "Jul", "Aug", "Sep", "Oct"],
        "backpacker": 65, "midRange": 140, "luxury": 300,
        "gettingThere": "65 miles north of Denver International Airport (DEN) via I-25. Fort Collins/Loveland Airport (FNL) has limited service.",
        "gradientColors": "from-amber-700 via-sky-600 to-slate-700",
        "aeo": "Fort Collins is Colorado's craft brewing capital — a Colorado State University town with over 20 craft breweries, the Cache la Poudre Wild and Scenic River, and a charming Old Town that inspired Disney's Main Street, budget $65-140/day.",
        "video_title": "Craft Beer Capital",
        "video_text": "Fort Collins has more craft breweries per capita than almost any US city — New Belgium, Odell, and Fort Collins Brewery among them — in a college town with genuine old-west charm.",
        "gradient": "linear-gradient(135deg, #92400e, #1e3a5f, #065f46)",
    },
    "glenwood-springs": {
        "title": "Glenwood Springs",
        "description": "Plan your Glenwood Springs trip. The world's largest hot springs pool, Glenwood Canyon (one of America's most scenic drives), and Hanging Lake.",
        "tagline": "Hot Springs in a Canyon",
        "region": "ski-country",
        "bestMonths": ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
        "backpacker": 70, "midRange": 170, "luxury": 380,
        "gettingThere": "160 miles west of Denver on I-70. Amtrak's California Zephyr stops in Glenwood Springs.",
        "gradientColors": "from-sky-600 via-emerald-500 to-slate-700",
        "aeo": "Glenwood Springs is Colorado's hot springs town — home to the world's largest outdoor hot springs pool in a stunning canyon, Hanging Lake (permit required), and the gateway to Aspen, budget $70-170/day.",
        "video_title": "Canyon Hot Springs",
        "video_text": "The world's largest outdoor hot springs pool sits at the confluence of the Colorado and Roaring Fork Rivers — 150 years of soaking in mineral-rich water in a dramatic canyon setting.",
        "gradient": "linear-gradient(135deg, #0c4a6e, #065f46, #334155)",
    },
    "great-sand-dunes": {
        "title": "Great Sand Dunes National Park",
        "description": "Plan your Great Sand Dunes National Park trip. The tallest sand dunes in North America rising against snow-capped peaks — one of Colorado's most surreal landscapes.",
        "tagline": "Desert Meets Mountains",
        "region": "san-luis-valley",
        "bestMonths": ["Apr", "May", "Jun", "Aug", "Sep", "Oct"],
        "backpacker": 50, "midRange": 110, "luxury": 230,
        "gettingThere": "About 240 miles southwest of Denver. Drive via US-285 to CO-17. Nearest commercial airport: Denver (4 hours) or Pueblo (2 hours).",
        "gradientColors": "from-amber-700 via-sky-600 to-amber-900",
        "aeo": "Great Sand Dunes National Park is one of Colorado's most surreal landscapes — the tallest sand dunes in North America (750 feet) rising against snow-capped Sangre de Cristo peaks in the San Luis Valley, $35 vehicle entry.",
        "video_title": "Desert in the Mountains",
        "video_text": "Seven-hundred-fifty-foot sand dunes rising against 14,000-foot peaks in the San Luis Valley — North America's tallest dunes created by ancient lakebed sand blown against a mountain range.",
        "gradient": "linear-gradient(135deg, #b45309, #92400e, #1e3a5f)",
    },
    "keystone": {
        "title": "Keystone",
        "description": "Plan your Keystone Resort trip. Family-friendly Summit County skiing, extended night skiing, and summer mountain biking 90 minutes from Denver.",
        "tagline": "Family-Friendly Summit County Skiing",
        "region": "ski-country",
        "bestMonths": ["Nov", "Dec", "Jan", "Feb", "Mar", "Jun", "Jul", "Aug"],
        "backpacker": 85, "midRange": 220, "luxury": 500,
        "gettingThere": "90 miles from Denver on I-70 West to US-6. Keystone Resort Express shuttles run from Denver area.",
        "gradientColors": "from-sky-700 via-white to-slate-600",
        "aeo": "Keystone is Summit County's family-friendly resort — extended night skiing, three mountains, and a convenient 90-minute Denver drive, budget $85-220/day, best December through March.",
        "video_title": "Night Skiing Summit County",
        "video_text": "Keystone offers some of Colorado's longest night skiing seasons — the slopes stay lit well past dusk, extending ski days on the Front Range's most accessible mountain.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #e5e7eb, #0c4a6e)",
    },
    "manitou-springs": {
        "title": "Manitou Springs",
        "description": "Plan your Manitou Springs visit. Victorian spa town with natural mineral springs, Pikes Peak gateway, Cave of the Winds, and Colorado's best small-town arts scene.",
        "tagline": "Victorian Springs Town",
        "region": "front-range",
        "bestMonths": ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
        "backpacker": 55, "midRange": 130, "luxury": 280,
        "gettingThere": "5 miles west of Colorado Springs on US-24. Easy drive or rideshare from Colorado Springs Airport (COS).",
        "gradientColors": "from-amber-800 via-sky-600 to-slate-700",
        "aeo": "Manitou Springs is the Victorian spa gateway to Pikes Peak — a charming mineral springs town with natural drinking fountains, the Incline for extreme stair climbing, and access to Cog Railway and Cave of the Winds, budget $55-130/day.",
        "video_title": "Springs and Summits",
        "video_text": "Eight natural mineral springs flow through Manitou's Victorian downtown — the 19th century health resort at the foot of Pikes Peak still dispensing its waters from iron fountains.",
        "gradient": "linear-gradient(135deg, #92400e, #1e3a5f, #134e4a)",
    },
    "mesa-verde": {
        "title": "Mesa Verde National Park",
        "description": "Plan your Mesa Verde National Park trip. Explore the ancient Ancestral Puebloan cliff dwellings — the most significant archaeological site in the United States.",
        "tagline": "Ancient Cliff Dwellings",
        "region": "western-slope",
        "bestMonths": ["Apr", "May", "Jun", "Aug", "Sep", "Oct"],
        "backpacker": 55, "midRange": 130, "luxury": 280,
        "gettingThere": "Nearest city is Cortez, Colorado, 10 miles west. Fly into Cortez Airport (CEZ) or Durango (40 miles east). Denver is 370 miles northeast.",
        "gradientColors": "from-amber-900 via-slate-700 to-sky-600",
        "aeo": "Mesa Verde National Park protects the most significant Ancestral Puebloan cliff dwellings in America — 600-room Cliff Palace and Balcony House built into sandstone alcoves in the 1200s, $35 vehicle entry, best April through October.",
        "video_title": "Ancient Cities in the Cliffs",
        "video_text": "The Ancestral Puebloan people built 600-room Cliff Palace into a sandstone alcove and abandoned it in the 1290s — one of the great archaeological mysteries of North America.",
        "gradient": "linear-gradient(135deg, #92400e, #b45309, #1e3a5f)",
    },
    "ouray": {
        "title": "Ouray",
        "description": "Plan your Ouray, Colorado trip. The Switzerland of America — Victorian mining town with natural hot springs, world-class ice climbing, and the Million Dollar Highway scenic drive.",
        "tagline": "Switzerland of America",
        "region": "western-slope",
        "bestMonths": ["Jan", "Feb", "Jun", "Jul", "Aug", "Sep"],
        "backpacker": 80, "midRange": 200, "luxury": 450,
        "gettingThere": "Nearest airport is Montrose (MTJ), 36 miles north. Drive from Denver: 330 miles, 5.5 hours via US-285 and US-550.",
        "gradientColors": "from-sky-600 via-white to-slate-700",
        "aeo": "Ouray is Colorado's Switzerland — a Victorian mining town at 7,760 feet in a box canyon, famous for natural hot springs, the Ouray Ice Park (world's first dedicated ice climbing park), and the stunning Million Dollar Highway drive, budget $80-200/day.",
        "video_title": "Switzerland of Colorado",
        "video_text": "Ouray sits in a perfect box canyon ringed by 13,000-foot peaks — the Victorian town's natural hot springs flow year-round while the canyon walls fill with ice climbs in winter.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #e5e7eb, #334155)",
    },
    "steamboat-springs": {
        "title": "Steamboat Springs",
        "description": "Plan your Steamboat Springs trip. Champagne powder skiing, natural hot springs, the Yampa River, and a genuine western cowboy-ski town culture.",
        "tagline": "Cowboy Ski Town",
        "region": "ski-country",
        "bestMonths": ["Dec", "Jan", "Feb", "Mar", "Jun", "Jul", "Aug"],
        "backpacker": 85, "midRange": 220, "luxury": 550,
        "gettingThere": "Yampa Valley Regional Airport (HDN) is 22 miles west with direct Denver service. Drive from Denver: 160 miles, 3 hours via US-40.",
        "gradientColors": "from-sky-700 via-amber-600 to-slate-700",
        "aeo": "Steamboat Springs is Colorado's cowboy ski town — Champagne Powder snow, natural hot springs in town, a genuine western culture, and the Yampa River running through the center, budget $85-220/day.",
        "video_title": "Champagne Powder Country",
        "video_text": "Steamboat's Champagne Powder trademark describes real phenomenon — ultralight, ultra-dry snow that floats through the air when you ski through it. Western cowboy culture coexists with world-class skiing.",
        "gradient": "linear-gradient(135deg, #0c4a6e, #1c1917, #92400e)",
    },
    "winter-park": {
        "title": "Winter Park",
        "description": "Plan your Winter Park, Colorado trip. The closest major ski resort to Denver, excellent intermediate terrain, and home to the National Ability Center's adaptive skiing.",
        "tagline": "Denver's Mountain",
        "region": "ski-country",
        "bestMonths": ["Nov", "Dec", "Jan", "Feb", "Mar", "Jun", "Jul"],
        "backpacker": 75, "midRange": 200, "luxury": 450,
        "gettingThere": "67 miles from Denver via I-70 and US-40 over Berthoud Pass. Amtrak's California Zephyr stops at Fraser/Winter Park, 2 miles from resort.",
        "gradientColors": "from-sky-700 via-white to-slate-600",
        "aeo": "Winter Park is the closest major ski resort to Denver — 67 miles via Berthoud Pass — with excellent intermediate terrain and one of the US's best adaptive skiing programs, budget $75-200/day.",
        "video_title": "Denver's Mountain",
        "video_text": "Winter Park is 67 miles from Denver and the most-visited Colorado resort by Front Range locals — Mary Jane's bump runs and the Vasquez Cirque serve advanced skiers alongside wide intermediate cruisers.",
        "gradient": "linear-gradient(135deg, #1e3a5f, #e5e7eb, #0c4a6e)",
    },
}

def build_stub_destination(slug, data, affiliatePicks_fallback=None, faqItems_fallback=None, scottTips_fallback=None):
    """Build a complete destination file from data dict."""
    aff = affiliatePicks_fallback or f"""  - name: "Best Hotel in {data['title']}"
    type: hotel
    price: "Check rates"
    personalNote: "Top-rated accommodation option in {data['title']} — central location and excellent reviews."
    affiliateUrl: "https://www.booking.com/searchresults.html?ss={data['title']}+Colorado&aid=2778866"
    badge: "Scott's Pick"
  - name: "{data['title']} Guided Tour"
    type: tour
    price: "$65-120/person"
    personalNote: "The best way to experience {data['title']} with local expertise and insider knowledge."
    affiliateUrl: "https://www.getyourguide.com/colorado-l234/tour-t12345/?partner_id=IVN6IQ3"
  - name: "Trekking Poles"
    type: activity
    price: "$30-80"
    personalNote: "Essential for Colorado mountain hiking — the elevation gains are significant and poles protect knees on descent."
    affiliateUrl: "https://www.amazon.com/s?k=trekking+poles+collapsible&tag=discovermore-20"
  - name: "Altitude Sickness Prevention"
    type: activity
    price: "$20-40"
    personalNote: "Colorado altitude is significant — visitors from sea level should drink extra water, avoid alcohol day one, and ascend gradually."
    affiliateUrl: "https://www.amazon.com/s?k=altitude+sickness+prevention&tag=discovermore-20"
"""

    faq = faqItems_fallback or f"""  - question: "Is {data['title']} safe?"
    answer: "{data['title']} is generally very safe. Altitude is the main consideration — Colorado mountain elevations cause altitude sickness in some visitors from sea level. Drink extra water, avoid alcohol your first day, and ascend gradually. Standard outdoor safety applies for any hiking."
  - question: "Best time to visit {data['title']}?"
    answer: "The ideal visiting periods are {', '.join(data['bestMonths'][:4])}. Colorado's mountain weather is variable — afternoon thunderstorms are common above treeline June through August. The best conditions depend on your activities."
  - question: "How many days in {data['title']}?"
    answer: "Two to three days is ideal for most visitors. This allows time for the major attractions, at least one significant hike or activity, and some flexibility for weather."
  - question: "Is {data['title']} worth it?"
    answer: "Yes — {data['description'][:100]}... The combination of natural setting and activities makes it one of Colorado's worthwhile destinations."
  - question: "{data['title']} on a budget?"
    answer: "Budget ${data['backpacker']}-{data['backpacker']+30}/day for backpacker-level travel with hostel or camping accommodation. Mid-range visitors should budget ${data['midRange']}/day. Many hiking trails and natural attractions are free or low-cost."
  - question: "What is {data['title']} known for?"
    answer: "{data['description']}"
  - question: "Do I need a car in {data['title']}?"
    answer: "A car is generally recommended for Colorado mountain destinations — public transit is limited outside Denver and the front range. Many trailheads and attractions require driving."
  - question: "Best things to do in {data['title']}?"
    answer: "Outdoor activities including hiking, skiing (in season), and exploring the natural setting are the primary draws. The specific highlights are reflected in the destination's tagline: {data['tagline']}."
"""

    scott = scottTips_fallback or f"""  logistics: "Access varies by location — see Getting There section. Colorado mountain roads can be challenging in winter; check CDOT road conditions before travel."
  bestTime: "The best months are {', '.join(data['bestMonths'][:4])}. Altitude sickness is a real concern — spend one night at a lower elevation before ascending to very high-altitude destinations."
  gettingAround: "A car is generally required for Colorado mountain destinations outside Denver's transit network."
  money: "Budget ${data['backpacker']}/day for backpacker level, ${data['midRange']}/day mid-range. Colorado mountain towns are generally 20-30% more expensive than Denver."
  safety: "Altitude is the primary concern for visitors from sea level — drink extra water, avoid alcohol day one, ascend gradually. Afternoon thunderstorms above treeline require getting below treeline by noon."
  packing: "Layers for variable mountain weather, sun protection (intense UV at altitude), rain jacket for afternoon storms, and sturdy hiking boots."
  localCulture: "Colorado mountain communities have a strong outdoor culture and environmental ethic. Leave No Trace principles are taken seriously. Year-round residents are generally welcoming of visitors who share respect for the landscape."
"""

    content = f"""---
title: "{data['title']}"
description: "{data['description']}"
heroVideo: ""
heroImage: ""
tagline: "{data['tagline']}"
region: "{data['region']}"
bestMonths: {data['bestMonths']}
budgetPerDay:
  backpacker: {data['backpacker']}
  midRange: {data['midRange']}
  luxury: {data['luxury']}
gettingThere: "{data['gettingThere']}"
highlights:
  - "{data['tagline']}"
gradientColors: "{data['gradientColors']}"
relatedDestinations: []
contentStatus: published
draft: false
fmContentType: destination
affiliatePicks:
{aff}faqItems:
{faq}scottTips:
{scott}---

{data['aeo']}

<div class="immersive-break-inline">
  <video autoplay muted loop playsinline preload="metadata">
    <source src="/videos/destinations/{slug}-hero.mp4" type="video/mp4" />
  </video>
  <div class="ib-gradient" style="background: {data['gradient']};"></div>
  <div class="ib-content">
    <div class="ib-title">{data['video_title']}</div>
    <p class="ib-text">{data['video_text']}</p>
  </div>
</div>

{data.get('body', data['description'])}
"""
    return content

# Process full destinations first
for slug, data in DESTINATIONS.items():
    filepath = f"{BASE}/{slug}.md"
    if not os.path.exists(filepath):
        print(f"SKIP {slug} — not found")
        continue
    content = open(filepath, 'r', encoding='utf-8').read()

    if "affiliatePicks:" in content:
        print(f"SKIP {slug} — already has Tier 3")
        continue

    new_content = build_stub_destination(slug, data,
        affiliatePicks_fallback=data.get('affiliatePicks'),
        faqItems_fallback=data.get('faqItems'),
        scottTips_fallback=data.get('scottTips')
    )
    open(filepath, 'w', encoding='utf-8').write(new_content)
    print(f"Done {slug}")

# Process remaining stub destinations
for slug, data in REMAINING.items():
    filepath = f"{BASE}/{slug}.md"
    if not os.path.exists(filepath):
        print(f"SKIP {slug} — not found")
        continue

    content = open(filepath, 'r', encoding='utf-8').read()

    if "affiliatePicks:" in content:
        print(f"SKIP {slug} — already has Tier 3")
        continue

    new_content = build_stub_destination(slug, data)
    open(filepath, 'w', encoding='utf-8').write(new_content)
    print(f"Done {slug}")

print("Colorado Tier 3 complete")
