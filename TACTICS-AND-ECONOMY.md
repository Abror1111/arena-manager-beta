# ARENA 1.15 — squad tactics and match economy

Ten agents use seeded, reactive rules. This is a local tactical simulation, not human-level reasoning or the native CS2 bot/Source2 engine.

Entry leads; rifler follows; captain and sniper establish a second control lane; support carries C4 behind the entry. All five receive separate navigable staging/anchor goals. CT anchors divide between A and B, then rotate on recent teammate reports. Local nav-safe steering keeps a gap, queues in narrow passages and gives way after a short wait. Temporary convergence in a choke remains possible. There is no pushing through walls or teleporting.

Career matches, XP and tactics determine experience. Veterans identify visible approaching HE/Molotovs sooner. Friendly utility calls are shared; enemy grenades must be visible and not obscured. Agents seek a reachable escape away from danger and allies. Site outcomes from earlier attacking rounds influence later balanced plans. Gunfire still uses reaction delays, finite bursts/recoil, reloads, health and cover. Agents do not pursue an unseen enemy's live coordinates. One CT defuses while teammates cover; ongoing defuse progress has priority. Post-plant Ts spread and attempt to save when the explosion is near.

Smoke is amber for club 0 and blue for club 1, in both 3D volume rendering and the 2D fallback. Color tracks the club through a side swap. Visibility, extinction and blast holes use the same rules for both colors. Molotov combustion smoke remains natural gray.

MR12: 12-round halves, first to 13 before 12:12. MR3 overtime: 3-round halves, target 16, 19, 22, etc., with $10,000 resets each OT half. The HUD displays the current half/OT block, maximum remaining rounds, victory target and impending side swap. BO3 additionally displays the map number and series score. Rounds may end early once the target and two-round lead are reached.

All automatically acquired weapons, vest/helmet, utility and kits cost match money. Survivors keep weapons, remaining armor and unused utility. Dead players receive only the default pistol before purchases. Auto buys consider team funds, loss streak and opponent match point; rich teammates may fund a rifle for an underfunded teammate. A single designated sniper buys AWP; teams buy at most two kits automatically. Free armory swaps remain limited to practice.

The next-round selector offers automatic/full/eco/force policies. It never silently rebuys during a live round. A full policy buys only what available money covers. Pistol rounds start at $800. Defused/exploded wins pay $3,500, other wins $3,250. Loss rewards rise from $1,400 to $3,400; surviving Ts on a timeout do not receive the loss reward. A planted T loss adds $800; plant/defuse gives the actor $300. Kill rewards follow weapon families; a teamkill costs $300 and cannot generate a kill bounty. Match cash is capped at $16,000. Club credits remain separate.

Career schema 2 and arena-career-v2 remain compatible. Old tactical snapshots keep their current-round behavior and gain the new squad/economy at the next round. Source map navigation/model hashes and Android upgrade signing identity are unchanged.
