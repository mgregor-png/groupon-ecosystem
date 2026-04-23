# Save Everywhere Prototype v2 - Context for Iteration

Last updated: April 14, 2026

## What It Is
Interactive prototype connecting 10 Stitch-designed screens into a tap-through flow. Shows the complete Save Everywhere user journey from App Store download through ecosystem loop.

## Files
- **Prototype:** `deliverables/save-everywhere-prototype-v2.html`
- **Also deployed at:** `projects/CoS_coupons-dashboards/save-everywhere-prototype-v2.html` (for GitHub Pages)
- **Stitch screen PNGs:** `projects/CoS_coupons-dashboards/stitch_groupon_safari_offers/*/screen.png`
- **Stitch screen HTML code:** `projects/CoS_coupons-dashboards/stitch_groupon_safari_offers/*/code.html`
- **Design system spec:** `projects/CoS_coupons-dashboards/stitch_groupon_safari_offers/emerald_value/DESIGN.md`

## Stitch Screen Flow (10 Steps)
1. **App Store Download** - User searches for and downloads Groupon app (setup)
2. **Extension Onboarding** - Prompted to enable Safari extension during first launch (setup)
3. **iOS Settings Toggle** - One-time toggle in Safari settings (setup)
4. **Shopping on Nike** - User browses Nike.com in Safari (capture)
5. **Extension Popup** - Groupon surfaces coupon code + cashback offer (capture)
6. **Savings Applied** - Code applied, $19.50 saved, $2.40 Bucks earned (capture)
7. **Reward Notification** - Push notification on lock screen brings user back (engage)
8. **In-App Balance** - $14.60 Bucks balance, browse local deals (engage)
9. **Spending Bucks** - Bucks applied to local spa, earning more Bucks (engage)
10. **The Ecosystem Loop** - Circular flow visualization: capture -> engage -> repeat (engage)

## Prototype Features
- iPhone frame (320x693) with dynamic island
- PNG screenshots from Stitch displayed inside frame
- Tap left/right halves of phone to navigate
- Arrow key navigation + Space for auto-play
- Touch swipe support for mobile
- Progress bar with clickable segments
- Phase labels (Setup / Capture / Engage)
- Step number, title, and description
- Auto-play mode (3s per screen)
- Reset button
- Dark background (#0a0a0f)

## Design System (Stitch "Value Architect" / "Emerald Value")
- Font: Plus Jakarta Sans (400-800)
- Icons: Material Symbols Outlined
- Primary: #2f6900 (Growth Green)
- Primary Container: #3d8400
- Secondary: #116682 (Deep Sky)
- Tertiary: #006b19
- Surface: #f9f9ff
- On-surface: #161c26
- No 1px borders - use tonal layering
- Glassmorphism on floating elements (85% opacity, 12px backdrop-blur)
- CTA buttons: 135deg gradient from primary to primary-container
- Asymmetric card corners (top-left + bottom-right rounded)
- Tailwind CSS CDN + custom color tokens

## Stitch Image Hosting
All Stitch screen images use `lh3.googleusercontent.com/aida-public/` URLs. These are Google-hosted and should remain stable.

## What Needs Iteration (Carry Forward)
- **Screen image sizing:** Check if all 10 PNGs render well in the 320x693 frame - some screens (2, 3, 4) are full-page layouts that may not fit in phone dimensions
- **Transition style:** Currently using opacity + scale. Could try slide left/right for more app-like feel
- **Auto-play timing:** 3s per screen may be too fast or slow - test with audience
- **Mobile responsiveness:** Test on actual phone - the tap zones and progress bar should work on touch
- **Screen 7 (notification):** This is a lock screen mockup with its own phone bezel - may look like phone-in-phone. Consider using just the inner content
- **Consider adding:** Narrative annotations that appear alongside the phone explaining what's happening
- **Consider adding:** "Presenter mode" that auto-advances with a spoken script
- **GitHub Pages deployment:** Needs the stitch_groupon_safari_offers directory to be deployed alongside the HTML

## Rebecca-Structure Report
Also created: `deliverables/save-everywhere-rebecca-structure.html`
- Follows Rebecca's exact 6-section structure
- Uses her verbatim framing and language
- Populated data from BQ-verified master context
- Separate output for later combination with other versions
- Sections: Premise -> How It Works -> Numbers -> Unknowns -> Why All Three -> The Coupons Space
