# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Discover Colorado -- a travel guide website built with Astro 5, Tailwind CSS 4, and deployed to Cloudflare Pages. Content is markdown-based using Astro's content collections with Zod schemas.

## Commands

```bash
npm run dev       # Start dev server at localhost:4321
npm run build     # Production build to ./dist/
npm run preview   # Preview production build locally
```

No test runner is configured. No linter is configured.

## Branding

- Colors: Ocean Teal #0D7377 (primary), Warm Coral #E8654A (accent)
- Deep Night #1A2332 (headings/dark backgrounds)
- Sand #F5F0E8 (light background), Sky #E8F4F5 (alt background)
- Warm Gold #D4A574
- Fonts: Outfit (sans), DM Serif Display (serif)

## Regions

- front-range
- ski-country
- national-parks
- western-slope

## Architecture

### Content Collections (`src/content/`)

Two collections defined in `src/content/config.ts`:
- **destinations** -- Travel destination pages with typed schema (region enum: front-range/ski-country/national-parks/western-slope, budgetPerDay in USD, highlights array, contentStatus workflow, gradientColors for per-destination theming)
- **blog** -- Articles with categories (destination, outdoor-adventure, skiing, practical, budget, history)

Both collections use a `draft: true` default. Content status tracks: draft -> review -> published -> needs-update.

### Routing (`src/pages/`)

- `index.astro` -- Home page
- `destinations/[...slug].astro` -- Dynamic catch-all route
- `blog/[...slug].astro` -- Blog post pages
- `404.astro` -- Custom error page

### Layouts

- `BaseLayout.astro` -- Root layout with SEO meta, imports FloatingNav + Footer + global styles
- `DestinationLayout.astro` -- Wraps BaseLayout, adds hero with per-destination gradient

### Deployment

- Domain: discovercolorado.info
- D1 database: trip-planner-cache-colorado (ID: TODO-CREATE-D1-FOR-COLORADO)
- Cloudflare Pages via `@astrojs/cloudflare` adapter

## Destinations (20)

Aspen, Black Canyon, Boulder, Breckenridge, Colorado Springs, Crested Butte, Denver, Durango, Estes Park, Fort Collins, Glenwood Springs, Great Sand Dunes, Keystone, Manitou Springs, Mesa Verde, Ouray, Steamboat Springs, Telluride, Vail, Winter Park

## Content Voice

- First-person singular -- Scott's perspective as a visitor
- Prices in USD only
- Honest, opinionated, insider perspective
- **Names rule:** Only use "Scott" and "I" in content. Never include names of family members, children, or other companions.
- Cross-link every page to at least 2 other content pillars
- Question-based H2/H3 headings for GEO
- Answer-first paragraphs: lead with the answer, then supporting detail

### Required Pro Tips (Every Destination Page)

1. **Getting There** -- Directions, parking tips, transit options
2. **Best Time to Visit** -- Season, weather, crowd levels
3. **Getting Around** -- Walking, shuttle systems, parking
4. **Budget Tips** -- Happy hours, free activities, local deals
5. **Safety** -- Altitude sickness, wildlife, weather awareness
6. **Packing** -- Layers, sun protection, altitude gear

Use `<div class="scott-tips">` block format.

## Affiliate Links

- Booking.com: aid=2778866, label=discovercolorado
- GetYourGuide: partner_id=IVN6IQ3
- Viator: pid=P00290009
- SafetyWing: referenceID=24858745

## Master Plan Updates

After completing significant work, update the **central master plan** at `C:\Users\scott\documents\discover-more\docs\master-plan.md`:
- Update the **Current Status table** row for this site
- Add a session log entry to `C:\Users\scott\documents\discover-more\docs\session-log.md` with date and summary
