# 🎓 Blue Archive Gacha System Simulator (Monte Carlo Analysis)

A Python Monte Carlo simulation comparing the Old Blue Archive Gacha System (200-Spark Recruitment Points) against the New Blue Archive Gacha System (Recruitment Charges / Pity Mechanics).

This project simulates up to 100,000 Senseis pulling across multiple banner configurations (Regular Dual Banners and Fest Anniversary Events) to calculate statistical averages for Pyroxene costs, hard pity frequencies, 3★ student yields, and total savings.

# 📌 Gacha System Mechanics Compared

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

## Regular Dual Banner Event:

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

📈 Sample Statistical Output

```
==================================================================
       BLUE ARCHIVE GACHA SIMULATION (100,000 SENSEIS)
==================================================================

--- 1. REGULAR DUAL BANNER COMPARISON (GET BOTH A & B) ---
 Rules Supplement:
  • New System: 3.0% Rate (0.7% Featured), 100-Charge 50/50, 200-Charge Guarantee.
  • Old System: 3.0% Rate (0.7% Featured), 200 Points = 1 Shop Spark.
 Stats:
  [NEW SYSTEM DETAILED STATS]
   • Average Pulls Required:     178.59 pulls
   • Average Pyroxene Cost:      ~21,430 Pyroxenes
   • Min / Max Pulls Range:      2 - 400 pulls
   • Needed 0 Hard Pities (200):  76788 Senseis (76.79%)
   • Needed 1 Hard Pity  (200):  21719 Senseis (21.72%)
   • Needed 2 Hard Pities (200):   1493 Senseis (1.49%)

  [OLD SYSTEM DETAILED STATS]
   • Average Pulls Required:     190.70 pulls
   • Average Pyroxene Cost:      ~22,883 Pyroxenes
   • Min / Max Pulls Range:      2 - 400 pulls
   • Needed 0 Sparks (Both Luck): 41665 Senseis (41.66%)
   • Needed 1 Spark  (1 Redeem): 52612 Senseis (52.61%)
   • Needed 2 Sparks (Max Pitied):  5723 Senseis (5.72%)

  [SAVINGS SUMMARY]
   • Avg Pulls Saved per Sensei: 12.11 pulls (6.35% reduction!)
   • Avg Pyroxenes Saved:        ~1,452 Pyroxenes

--- 2. FEST EVENT SIMULATION (DUAL BANNER 1ST HALF & DUAL BANNER 2ND HALF) ---
 Rules Supplement:
  • 1st Half (Pre-Fes Dual Banner): Target BOTH Pre-Fes A & B. 100 Free Pulls awarded.
  • 2nd Half (Fes Dual Banner): Target BOTH Fes A & B. Double 3★ Rate (6.0% overall, 0.7% featured).

 [FIRST HALF: PRE-FES DUAL BANNER + 100 FREE PULLS (GET BOTH A & B)]
  [NEW SYSTEM DETAILED STATS]
   • Average Pulls Required:     178.73 pulls
   • Average Pyroxene Cost:      ~10,142 Pyroxenes
   • Min / Max Pulls Range:      2 - 400 pulls
   • Got BOTH for 0 Pyroxene:     16559 Senseis (16.56%)
   • Needed 0 Hard Pities (200):  76675 Senseis (76.68%)
   • Needed 1 Hard Pity  (200):  21806 Senseis (21.81%)
   • Needed 2 Hard Pities (200):   1519 Senseis (1.52%)

  [OLD SYSTEM DETAILED STATS]
   • Average Pulls Required:     190.84 pulls
   • Average Pyroxene Cost:      ~11,602 Pyroxenes
   • Min / Max Pulls Range:      2 - 400 pulls
   • Got BOTH for 0 Pyroxene:     15847 Senseis (15.85%)
   • Needed 0 Sparks (Both Luck): 41524 Senseis (41.52%)
   • Needed 1 Spark  (1 Redeem): 52782 Senseis (52.78%)
   • Needed 2 Sparks (Max Pitied):  5694 Senseis (5.69%)

  [SAVINGS SUMMARY]
   • Avg Pulls Saved per Sensei: 12.11 pulls (6.35% reduction!)
   • Avg Pyroxenes Saved:        ~1,459 Pyroxenes

 [SECOND HALF: 6.0% DUAL FES BANNER - BEHAVIOR A (STOP WHEN BOTH OBTAINED)]
  [NEW SYSTEM DETAILED STATS]
   • Average Pulls Required:     175.82 pulls
   • Average Pyroxene Cost:      ~21,098 Pyroxenes
   • Min / Max Pulls Range:      2 - 400 pulls
   • Avg 3★ Yielded (6% Rate):   11.67 3-star students
   • Needed 0 Hard Pities (200):  77183 Senseis (77.18%)
   • Needed 1 Hard Pity  (200):  21405 Senseis (21.40%)
   • Needed 2 Hard Pities (200):   1412 Senseis (1.41%)

  [OLD SYSTEM DETAILED STATS]
   • Average Pulls Required:     188.22 pulls
   • Average Pyroxene Cost:      ~22,586 Pyroxenes
   • Min / Max Pulls Range:      2 - 400 pulls
   • Avg 3★ Yielded (6% Rate):   11.29 3-star students
   • Needed 0 Sparks (Both Luck): 42691 Senseis (42.69%)
   • Needed 1 Spark  (1 Redeem): 51869 Senseis (51.87%)
   • Needed 2 Sparks (Max Pitied):  5440 Senseis (5.44%)

  [SAVINGS SUMMARY]
   • Avg Pulls Saved per Sensei: 12.40 pulls (6.59% reduction!)
   • Avg Pyroxenes Saved:        ~1,488 Pyroxenes

 [SECOND HALF: 6.0% DUAL FES BANNER - BEHAVIOR B (FULL GEM DUMP / AT LEAST 200 PULLS)]
  [NEW SYSTEM DETAILED STATS]
   • Average Pulls Required:     223.11 pulls
   • Average Pyroxene Cost:      ~26,773 Pyroxenes
   • Min / Max Pulls Range:      200 - 400 pulls
   • Total 3★ Yielded (6% Rate): 14.61 3-star students
   • Featured Copies Count:      2.39 copies
   • Needed 0 Hard Pities (200):  77034 Senseis (77.03%)
   • Needed 1 Hard Pity  (200):  21559 Senseis (21.56%)
   • Needed 2 Hard Pities (200):   1407 Senseis (1.41%)

  [OLD SYSTEM DETAILED STATS]
   • Average Pulls Required:     226.32 pulls
   • Average Pyroxene Cost:      ~27,158 Pyroxenes
   • Min / Max Pulls Range:      200 - 400 pulls
   • Total 3★ Yielded (6% Rate): 13.58 3-star students
   • Featured Copies Count:      2.65 copies
   • Needed 0 Sparks:                 0 Senseis (0.00%)
   • Needed 1 Spark:              93930 Senseis (93.93%)
   • Needed 2 Sparks (Max Pitied):  6070 Senseis (6.07%)

  [SAVINGS SUMMARY]
   • Avg Extra Pulls Saved:      3.21 pulls
   • Avg Extra Pyroxenes Saved:  ~384 Pyroxenes
==================================================================

Simulation complete! Press ENTER to exit...
```


# 🛠 Customization

You can adjust the sample size or individual probability parameters in dual_banner_simulation.py:

# Change the number of simulated Senseis (e.g., 10,000 for faster execution)
```
if __name__ == "__main__":
    run_comparative_simulation(num_senseis=10000)
```


📜 License

This project is open source under the MIT License.
