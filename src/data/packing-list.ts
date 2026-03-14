import type { PackingItem, PackingConfig, GearRecommendation } from './packing-base';

export const COLORADO_ESSENTIALS: PackingItem[] = [
  { id: 'co-altitude', name: 'Altitude Acclimatization Plan', category: 'destination', description: 'Denver is 5,280 feet. Breckenridge is 9,600 feet. Many visitors experience altitude sickness — headache, nausea, fatigue. Hydrate heavily before arrival and the first day; avoid strenuous activity the first 24 hours at elevation.', essential: false, quantityMultiplier: 0, localAlternative: 'Drink 3L water daily, avoid alcohol first 48 hours — most people adjust without medication' },
  { id: 'col-layers', name: 'Four-Season Layering System', category: 'destination', description: 'Colorado can deliver all four seasons in one day — sunny 70°F at noon, thunderstorm at 2pm, 45°F by sunset. The only solution is layers you can add and remove through the day.', essential: true, climate: ['cold', 'alpine'], amazonSearchFallback: 'merino+wool+base+layer+thermal', affiliatePrice: '$60–100' },
  { id: 'col-hikeboots', name: 'Hiking Boots (ankle support)', category: 'destination', description: '14ers, Rocky Mountain National Park, Maroon Bells — Colorado\'s trails are serious. Loose rock, steep grades, afternoon thunderstorm risk. Ankle-supporting waterproof boots are not optional above treeline.', essential: true, amazonSearchFallback: 'waterproof+hiking+boots+ankle+support', affiliatePrice: '$100–180' },
  { id: 'col-sunprotect', name: 'High-Altitude Sun Protection', category: 'destination', description: 'Every 1,000 feet of elevation increases UV intensity by 4%. At 12,000 feet, you\'re getting 50% more UV than at sea level. SPF 50+ sunscreen and UPF 50 clothing every day outdoors.', essential: true, amazonSearchFallback: 'sunscreen+spf+50+altitude+outdoor', affiliatePrice: '$12–20' },
  {
    id: 'vpn-subscription',
    name: 'VPN Subscription',
    category: 'electronics',
    description: 'Secure your data on public WiFi — essential for hotel, airport, and cafe networks abroad.',
    essential: false,
    affiliateUrl: 'https://go.nordvpn.net/aff_c?offer_id=15&aff_id=142311&url_id=902',
    affiliatePrice: '~$3/month',
    affiliatePartner: 'NordVPN',
  },
  {
    id: 'phone-gimbal',
    name: 'Phone Gimbal for Travel Vlogging',
    category: 'electronics',
    description: 'Stabilized video from your phone — no editing needed.',
    essential: false,
    affiliateUrl: 'https://www.insta360.com/sal/flow-2-pro?utm_source=AffiliateCenter&utm_medium=copylink&utm_term=INRSG7H5RTR',
    affiliatePrice: '~$149',
    affiliatePartner: 'Insta360',
  },
];

export const COLORADO_GEAR_RECOMMENDATIONS: GearRecommendation[] = [
  { id: 'gr-col-boots', name: 'Waterproof Hiking Boots', reason: 'Colorado trails get wet from afternoon thunderstorms and snowmelt year-round. Ankle support is critical on the loose rock of 14er approaches and Rocky Mountain trails. Don\'t compromise here.', amazonSearchFallback: 'waterproof+hiking+boots+ankle+support+trail', affiliatePrice: '~$130' },
  { id: 'gr-col-jacket', name: 'Packable Down Jacket', reason: 'Colorado afternoons at elevation drop fast. 70°F at 2pm → 45°F and wet by 4pm is common. A packable down jacket in your daypack turns a miserable situation into a comfortable one.', amazonSearchFallback: 'packable+down+jacket+lightweight+hiking', affiliatePrice: '~$85' },
  { id: 'gr-col-sunscreen', name: 'High-SPF Sunscreen (SPF 50+)', reason: 'At 12,000 feet, UV intensity is 50% higher than at sea level. Add snow reflection in winter or spring, and you\'re burning faster than you expect. SPF 50+ reapplied every 90 minutes.', amazonSearchFallback: 'sunscreen+spf+50+altitude+sport+outdoor', affiliatePrice: '~$14' },
  { id: 'gr-col-baselayer', name: 'Merino Wool Base Layer', reason: 'Colorado mornings start cold. Merino wool regulates temperature from cold start to warm midday, resists odor through multi-day trips, and stays warm even when wet from afternoon storms.', amazonSearchFallback: 'merino+wool+base+layer+hiking+outdoor', affiliatePrice: '~$75' },
  { id: 'gr-col-hydration', name: 'Hydration Pack (2L reservoir)', reason: 'High altitude dehydration is faster and more dangerous than sea-level dehydration. A hydration pack makes constant sipping automatic — which is what you need at 12,000 feet.', amazonSearchFallback: 'hydration+pack+2+liter+hiking+daypack', affiliatePrice: '~$50' },
];

export const COLORADO_CONFIG: PackingConfig = {
  sitePrefix: 'dcl',
  destination: 'Colorado',
  climate: ['cold', 'alpine'],
  currency: 'USD',
  plugType: 'Type A/B',
  plugVoltage: '120V',
  affiliateTag: 'discoverphili-20',
  seasons: [
    { value: 'spring', label: 'Spring (Mar–May)' },
    { value: 'summer', label: 'Summer (Jun–Aug)' },
    { value: 'fall', label: 'Autumn (Sep–Nov)' },
    { value: 'winter', label: 'Winter (Dec–Feb)' },
  ],
  activities: [
    { value: 'hiking', label: 'Hiking', icon: '🥾' },
    { value: 'skiing', label: 'Skiing / Snowboarding', icon: '⛷️' },
    { value: 'wildlife', label: 'Wildlife Viewing', icon: '🦅' },
    { value: 'camping', label: 'Camping', icon: '⛺' },
    { value: 'photography', label: 'Photography', icon: '📸' },
    { value: 'city-walk', label: 'City Exploring', icon: '🚶' },
  ],
  destinationEssentials: COLORADO_ESSENTIALS,
  gearRecommendations: COLORADO_GEAR_RECOMMENDATIONS,
};

export const SITE_CONFIG = COLORADO_CONFIG;

export const COLORADO_PACKING_FAQS = [
  { question: 'What should I pack for Colorado?', answer: 'The key items are a four-season layering system (Colorado delivers all four seasons in a single day), waterproof hiking boots with ankle support for 14ers and Rocky Mountain trails, high-SPF sunscreen (50% more UV at 12,000 feet than sea level), and a packable down jacket for the rapid afternoon temperature drops. No international adapter needed.' },
  { question: 'What is altitude sickness and how should I prepare?', answer: 'Denver is 5,280 feet; mountain towns like Breckenridge are 9,600 feet. Many visitors experience headache, fatigue, and shortness of breath — most adjust within 24–48 hours. Prep: arrive hydrated, drink 3L of water on day one, avoid strenuous activity the first 24 hours, and skip alcohol the first night. Most people adapt without medication.' },
  { question: 'What power adapter do I need for Colorado?', answer: 'No adapter needed. Colorado uses US standard Type A/B outlets at 120V.' },
  { question: 'Can I buy outdoor gear in Colorado?', answer: 'Yes — REI has stores throughout Colorado (Denver, Boulder, Fort Collins). Evo and local outdoor shops are in mountain towns. Colorado gear selection is excellent. However, specialty sizes and your preferred brands are better sourced before your trip — mountain town stores are small.' },
  { question: 'How many outfits should I pack for Colorado?', answer: 'Pack for 5–7 days with emphasis on technical gear (merino wool, waterproof layers) over quantity. Laundromats are in every town ($2–4/load). Most Colorado Airbnbs have washers and dryers. Pack fewer outfits and more functional gear.' },
  { question: 'What should I NOT bring to Colorado?', answer: 'Cotton base layers for hiking (cotton kills in Colorado — it holds moisture and loses insulation fast when wet). Light rain gear (Colorado afternoon thunderstorms are serious). And don\'t underestimate 14ers — altitude, weather, and loose rock make these serious mountains even for experienced hikers.' },
];
