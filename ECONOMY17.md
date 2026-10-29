# ARENA club economy 17

The club's existing credits become one clearly named in-game coin wallet. Existing balances, roster, season and in-flight matches are retained; migration creates an opening ledger balance without granting or taking coins. Match weapon dollars remain a separate round economy.

## Earnings and expenses

- Official completed BO1/BO3 series pay 2,200 coins for a win or 900 for a loss, plus the active sponsor and fan/merchandise income. A BO3 pays once after the series, not after each map.
- Salaries cover every roster member, including reserves: `60 + max(0, overall - 50) × 3` coins per official series. Club services cost `40 + training level × 35`.
- The league covers any gap needed to leave at least 200 net coins after a completed loss. There are no entry fees, negative balances, interest charges, offline salary drains or rest-day charges.
- Example: the initial six-player club earns 2,200 + 650 sponsor + 320 fan income, pays 888 salaries and 75 services, and receives **2,207 net** for its first official win. Its first loss earns **707 net**. Amounts change with roster, fans, facility and sponsor.
- Each cycle includes three paid practice matches: 350 for a win, 180 for a loss. Further practice remains playable without coin/club-XP/fan rewards. A fully completed official series refreshes the allowance. Rest, app reload, practice forfeits and official forfeits do not refresh it.
- Season prizes retain the placement scale, multiplied by completed participation (5 league games, 6 for semifinal places, 7 for finalists). Skipping all fixtures produces no prize or prestige. One completed game and four forfeits earns only one fifth of the sixth-place prize.

## Sponsors, objectives and shop

Three fictional sponsors offer free, three-series contracts with fixed participation and win payments. Contracts cannot be swapped early and have no repeat signing bonus. Better offers require fans and reputation; renewals are explicit.

Five permanent objectives reward the first completed official match, first official win, three training sessions, a recruit and a championship. Each can be claimed once across saves and seasons.

The club shop sells four additional visual themes and three emblems at published fixed prices (1,200–6,500 coins). Classic gold and the ARENA shield are free. Purchased items are permanent, can be equipped again for free and never improve combat skills. Themes update club controls and accents; emblems appear in the header, opening and club view. Anime portraits are retained. There are no random boxes, premium currency, purchases with real money or cash withdrawals in this release.

## Records and saves

Every coin change uses a shared checked transaction function. The wallet stores a running balance and the last 120 ledger records with their actual amounts, categories and resulting balances. Older records roll into the retained history's anchor; lifetime income and expense totals remain. Invalid balances, malformed records, catalog ownership and result-display data are rejected on import.

Purchases and objective claims are checked again against the current state. Completed-series IDs prevent repeat settlement. A validated match identity also prevents a result from a prior new-version match being applied to a different current match. Legacy snapshots remain readable. This is an offline game economy, not a payment processor or server-authoritative monetary account.

## Interface and verification

Moliya is horizontally paginated with wallet history, cash flow, next-match forecast, costs, contracts, tasks and player salaries. The wallet header opens it directly. Do‘kon and Transfers are the only manager screens that scroll vertically; all ten sections remain available on phones, tablets and hinge layouts.

Validation: 59 Node checks (financial rules, real legacy save migration, career progression and existing map/audio/effect integration); 230 manager screen checks across 23 viewport sizes; book/tabletop emulation; actual UI purchases, training, claims, save/resume, three engine-driven result fixtures and sponsor renewal; production-prefix financial/shop offline reload; and existing source-map WebGL/offline checks. Browser emulation is not physical-device certification. The signed APK has not been rebuilt.
