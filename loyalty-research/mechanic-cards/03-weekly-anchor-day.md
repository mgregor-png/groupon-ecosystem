# Mechanic Card 03 - Weekly Anchor Day
*Source: Rakuten Mobile Monday | 2026-04-21*

## What it is

A weekly recurring event on a specific weekday that rewards opening the app / extension / website that day.

**Rakuten Mobile Monday**: every Monday, in-app only, boosted cashback rates. Drives weekly app open. [Data - rakuten.com/double-cash-back; High] Rakuten has maintained this mechanic for multiple years, making it one of the longest-running weekly anchors in the cashback category.

## Why it works as a habit driver

- **Deterministic weekly hook.** Users learn "Monday = Groupon day" over 4-6 weeks of consistent pattern.
- **Low effort to participate.** Opening an app is trivial compared to purchasing.
- **Fills gap between quarterly payouts.** Without a sub-quarterly mechanic, the Big Fat Check cycle is 13 weeks between dopamine moments. Weekly anchor compresses this to 1 week.
- **Creates pushing surface.** Every Sunday night / Monday morning is a legitimate push notification opportunity without feeling spammy.

## Evidence this works

- Rakuten direct traffic 63% [Data - SimilarWeb Mar 2026]. Suggests strong habit-formation.
- Rakuten has maintained Mobile Monday as a standing program for multiple years. Survival = evidence.
- Category pattern: committed weekly anchors are present across multiple loyalty categories, not just cashback. The mechanic is generic and well-validated.

## Groupon adoption

**Monday is the obvious choice** (consistent with competitors, start of workweek mindset). Alternatives considered:

| Weekday | Argument | Verdict |
|---|---|---|
| **Monday** | Rakuten precedent; start-of-week; workweek-planning mindset | **Recommended** |
| Tuesday | Taco Tuesday / food-deal pairing | Alt - test if Monday saturates |
| Wednesday | Hump day optimism | Weak |
| Thursday | Pre-weekend ("Thirsty Thursday") | Weak |
| Friday | Weekend launch | Too late for "habit" framing |
| Weekend | Leisure browsing | Counter: users are distracted, conversion lower |

**Concrete Groupon pattern:**
- **Bucks Monday** - 2x Bucks earned on all qualifying purchases via app / extension every Monday.
- **Monday push notification** - 8am local time, "Your Monday Bucks are live."
- **Monday homepage takeover** - banner, boosted deals, curated "Monday-only" deals.
- **Monday-only deals** as a bonus surface - exclusive deals that only appear Mondays.

## Specifically do NOT copy

- **Daily reveal / streak-based mechanic.** Daily streaks are designed for daily-frequency products. Groupon's cadence is weekly-to-monthly. A daily streak would punish users for not visiting Groupon every day, which is not realistic. Weekly anchor is the right frequency.
- **Calendar complexity.** Keep it one day, same day every week. Rakuten has occasionally overloaded with "Double Cash Back Days" which dilutes the Monday signal.

## Interaction with other mechanics

- **Quarterly payout ritual (Card 01):** Monday feeds the Bucks balance that gets paid out quarterly. Clear narrative - "earn on Mondays, get paid on the 15th of Feb/May/Aug/Nov."
- **Challenge engine (separate card, planned Q3):** weekly challenges expire Sunday night - users rush to complete Mondays. Synergistic.
- **Push strategy:** Monday becomes the one confident-positive push day. Other days, push only for transactional or high-relevance events.

## Effort

- Merchant config for boosted Monday rate: ~0.5 sprint
- Push scheduling infrastructure: ~0.5 sprint (if not already in place - else ~0.1)
- Homepage Monday takeover UX: ~0.5 sprint
- Monday-only deal curation tooling: ~1 sprint (optional)

**Total: ~1.5-2.5 sprints.**

## Success metrics

- **App opens on Monday vs average weekday** (target: +40% Monday lift sustained over 8 weeks)
- **Push open rate** on Bucks Monday notification (target: 25-40%)
- **Conversion rate Monday vs average weekday** (target: Monday >= baseline; not significantly worse)
- **Repeat-visitor rate Monday** (same-user Mondays over 4 weeks; target: >= 30% return at least 3 of 4 Mondays after week 6)

## Risks

- **Saturation / tuning out.** If Monday is the only push day, users grow immune. Rotate creative, vary deals, occasional surprise boosts.
- **Merchant fatigue.** If Monday is always 2x rate, merchants may push back on margin. Alternative: 1.5x everyone, 2x-3x on rotating featured merchants.
- **Holiday Mondays** (Memorial Day, Labor Day etc in the US). Plan around: either skip, or go 3x for holiday Mondays as a "super Monday" brand beat.

## Related

- Mechanic Card 01 - Quarterly Payout Ritual (the longer-term flywheel)
- Mechanic Card 06 - Trust + Transparency (Monday is a good place to practice "here is why we are doing this" messaging)
