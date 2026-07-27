# 🎓 Blue Archive Gacha System Simulator (Monte Carlo Analysis)

A Python-based Monte Carlo simulator comparing the Old Blue Archive Gacha System (200-Spark Recruitment Points) against the New Blue Archive Gacha System (Recruitment Charges / Hybrid Pity Mechanics).

This project simulates up to 100,000+ Senseis across multiple banner configurations (Regular Dual Banners and Fest Anniversary Events) to calculate statistical averages for Pyroxene costs, hard pity frequencies, 3★ student yields, and total savings. It also includes an Individual Sensei Mode for live roll-by-roll inspection!

# 📌 Key Features

Mass Monte Carlo Simulation: Simulates up to 100,000+ Senseis to produce statistically significant data on pulls, Pyroxene costs, and hard pity frequencies.

10-Pull Set Distribution Histograms: Visualizes pull count distributions in 10-roll brackets (1-10, 11-20, ..., 391-400) using horizontal ASCII bar graphs (█ = 1%).

Interactive CLI Menu: Launch straight into mass simulation mode or inspect individual pull logs.

Individual Sensei Mode (Pull-by-Pull Stepper): Watch step-by-step gacha pulls in real time with charge/point tracking, 10-pull protections, and a detailed Student Yield Summary (1★, 2★, 3★ off-rate spooks, and featured copies).

Instant Keypress Navigation: Cross-platform single-keypress controls (Y/N) for quick re-runs without pressing Enter.

# 🛠 Gacha System Mechanics Compared

## 1. Old System (Recruitment Points / Spark)

Base 3★ Rate: 3.0% (0.7% Featured / 2.3% Off-rate spooks).

Spark Mechanic: Each pull awards 1 Recruitment Point.

Redemption: Reaching 200 Recruitment Points allows redeeming 1 Featured Student from the shop.

Reset Rules: Points reset to 0 upon spending 200 points. Pulling a featured student naturally does not reset points.

## 2. New System ("Recruitment Charge" / Hybrid Pity)

Base 3★ Rate: 3.0% (0.7% Featured / 2.3% Off-rate spooks).

100th Charge (Soft Pity / 50-50): Guarantees a 3★ student with a 50% chance to be the targeted Featured Student.

200th Charge (Hard Guarantee): Guarantees 100% to be the targeted Featured Student.

Crucial Rule: Pulling an off-rate (spook) 3★ DOES NOT reset the charge counter! The charge counter ONLY resets to 0 upon obtaining a Featured Student.

# 📊 Simulated Scenarios

Regular Dual Banner Event:

Senseis pull on concurrent banners (Banner A & Banner B) with a target of obtaining both featured 3★ students.

## Fest Anniversary Event (Two-Part Event):

### 1st Half (Pre-Fes Dual Banner): Senseis target both Pre-Fes featured students starting with 100 Free Pulls, spending Pyroxene only if needed after free rolls expire.

### 2nd Half (Dual Fes Banner - Double 6.0% 3★ Rate): Senseis pull on the 6.0% Fes dual banner under two distinct player behaviors:

#### Behavior A (Target-Stop): Pulls until both Fes featured students are acquired, then saves remaining Pyroxenes.

#### Behavior B (Full Gem-Dump): Commits at least 200 pulls (24,000 Pyroxene budget) to maximize total 3★ student yields, dupes, and eligma.

# 🚀 Quick Start

Prerequisites

Python 3.7 or higher installed on your system.

No external third-party libraries required (built using standard library modules).

Running the Simulation

Clone the repository:
```
git clone [https://github.com/SmezMorePrakezz/blue-archive-gacha-pull-statistic-old-and-new.git](https://github.com/SmezMorePrakezz/blue-archive-gacha-pull-statistic-old-and-new.git)
cd blue-archive-gacha-pull-statistic-old-and-new
```


Run the Python script:

```
python dual_banner_simulation.py
```


# 📈 Sample Statistical Output

```
==================================================================
       BLUE ARCHIVE GACHA SIMULATION (100,000 SENSEIS)
==================================================================

--- 1. REGULAR DUAL BANNER COMPARISON (GET BOTH A & B) ---
 Rules Supplement:
  • New System: 3.0% Rate (0.7% Featured), 100-Charge 50/50, 200-Charge Guarantee.
  • Old System: 3.0% Rate (0.7% Featured), 200 Points = 1 Shop Spark.

  [NEW SYSTEM DETAILED STATS]
   • Average Pulls Required:     178.51 pulls
   • Average Pyroxene Cost:      ~21,421 Pyroxenes
   • Min / Max Pulls Range:      2 - 400 pulls
   • Needed 0 Hard Pities (200):  76809 Senseis (76.81%)
   • Needed 1 Hard Pity  (200):  21689 Senseis (21.69%)
   • Needed 2 Hard Pities (200):   1502 Senseis (1.50%)

  [NEW SYSTEM 10-PULL SET BRACKETS]
   •   1 -  10 pulls:   1262 Senseis (  1.26%) | █
   •  11 -  20 pulls:   2488 Senseis (  2.49%) | ██
   •  21 -  30 pulls:   3690 Senseis (  3.69%) | ████
   ...
   • 191 - 200 pulls:   9845 Senseis (  9.85%) | ██████████

  [SAVINGS SUMMARY]
   • Avg Pulls Saved per Sensei: 11.97 pulls (6.28% reduction!)
   • Avg Pyroxenes Saved:        ~1,436 Pyroxenes
```

# 👤 Individual Sensei Mode Sample

```
Roll 001 | Charge: 001/200 | Result: ★1 Student
...
Roll 098 | Charge: 098/200 | Result: ★2 Student
Roll 099 | Charge: 099/200 | Result: ★1 Student
Roll 100 | Charge: 100/200 | Result: ★3 FEATURED STUDENT A! (Won 100-Charge 50/50)

SUCCESS! Acquired both students in 142 total rolls (~17,040 Pyroxenes).

STUDENT YIELD SUMMARY:
 • 1★ Students: 112
 • 2★ Students:  26
 • 3★ Students:   4 (Featured: 2 [A: 1, B: 1], Spooks: 2)
```

# 📜 License

This project is open source under the MIT License.
