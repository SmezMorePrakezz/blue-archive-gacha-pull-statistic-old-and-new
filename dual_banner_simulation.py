import random

# ==============================================================================
# SECTION 1: REGULAR DUAL BANNER FUNCTIONS (TARGET: BOTH A & B)
# ==============================================================================

def simulate_new_system_dual(total_3star_rate=0.03, featured_rate=0.007):
    """
    Simulates a single Sensei in the NEW 'Recruitment Charge' System:
    - Base 3★ rate: 3.0% (Featured: 0.7%, Off-rate spooks: 2.3%)
    - Charge ONLY resets when a featured student is obtained.
    - 100th charge: Guaranteed 3★ with a 50/50 chance for the featured student.
    - 200th charge: 100% Hard Guarantee for the featured student.
    """
    TOTAL_3STAR_RATE = total_3star_rate
    FEATURED_RATE = featured_rate
    NATURAL_FEATURED_PROB = FEATURED_RATE / TOTAL_3STAR_RATE

    charge_count = 0
    total_pulls = 0
    spooks = 0
    
    pity_100_wins = 0
    pity_100_losses = 0
    pity_200_hits = 0

    students_obtained = {"A": False, "B": False}

    for target in ["A", "B"]:
        if students_obtained[target]:
            continue

        while not students_obtained[target]:
            total_pulls += 1
            charge_count += 1

            # --- CASE 1: HARD GUARANTEE AT 200 CHARGES ---
            if charge_count == 200:
                students_obtained[target] = True
                pity_200_hits += 1
                charge_count = 0  # Reset charge after getting featured student
                break

            # --- CASE 2: 100TH CHARGE GUARANTEE (50/50) ---
            elif charge_count == 100:
                is_featured = random.random() < 0.5
                if is_featured:
                    pity_100_wins += 1
                    students_obtained[target] = True
                    charge_count = 0  # Reset charge after getting featured student
                    break
                else:
                    pity_100_losses += 1
                    spooks += 1
                    # Charge DOES NOT reset on off-rate 3★! Continues toward 200.

            # --- CASE 3: STANDARD PULL (1-99, 101-199) ---
            else:
                if random.random() < TOTAL_3STAR_RATE:
                    if random.random() < NATURAL_FEATURED_PROB:
                        students_obtained[target] = True
                        charge_count = 0  # Reset charge after getting featured student
                        break
                    else:
                        spooks += 1
                        other_target = "B" if target == "A" else "A"
                        if not students_obtained[other_target] and random.random() < 0.01:
                            students_obtained[other_target] = True

    return {
        "total_pulls": total_pulls,
        "spooks": spooks,
        "pity_100_wins": pity_100_wins,
        "pity_100_losses": pity_100_losses,
        "pity_200_hits": pity_200_hits,
    }


def simulate_old_system_dual(total_3star_rate=0.03, featured_rate=0.007):
    """
    Simulates a single Sensei in the OLD 'Recruitment Points' (Spark) System:
    - Base 3★ rate: 3.0% (Featured: 0.7%, Off-rate spooks: 2.3%)
    - No 100-roll 50/50, no charge carryovers or resets on featured.
    - Each pull awards 1 Recruitment Point.
    - 200 Recruitment Points = Redeem 1 featured student from shop (Spark).
    """
    TOTAL_3STAR_RATE = total_3star_rate
    FEATURED_RATE = featured_rate
    NATURAL_FEATURED_PROB = FEATURED_RATE / TOTAL_3STAR_RATE

    total_pulls = 0
    recruitment_points = 0
    spooks = 0
    sparks_used = 0

    students_obtained = {"A": False, "B": False}

    while not (students_obtained["A"] and students_obtained["B"]):
        target = "A" if not students_obtained["A"] else "B"

        total_pulls += 1
        recruitment_points += 1

        if random.random() < TOTAL_3STAR_RATE:
            if random.random() < NATURAL_FEATURED_PROB:
                students_obtained[target] = True
            else:
                spooks += 1
                other_target = "B" if target == "A" else "A"
                if not students_obtained[other_target] and random.random() < 0.01:
                    students_obtained[other_target] = True

        if students_obtained["A"] and students_obtained["B"]:
            break

        if recruitment_points == 200:
            if not students_obtained["A"]:
                students_obtained["A"] = True
            elif not students_obtained["B"]:
                students_obtained["B"] = True

            sparks_used += 1
            recruitment_points = 0  # Spend 200 points

    return {
        "total_pulls": total_pulls,
        "spooks": spooks,
        "sparks_used": sparks_used,
    }


# ==============================================================================
# SECTION 2: FEST EVENT FUNCTIONS (2 FEATURED STUDENTS PER HALF)
# ==============================================================================

def simulate_pre_fes_free_pulls_dual(system="NEW"):
    """
    Simulates First Half (Pre-Fes Dual Banner):
    - Target: Get BOTH Pre-Fes Student A and Pre-Fes Student B.
    - 100 Free Pulls awarded (0 Pyroxene cost for first 100 pulls).
    - Rate: 3.0% overall, 0.7% featured.
    """
    TOTAL_3STAR_RATE = 0.03
    FEATURED_RATE = 0.007
    NATURAL_FEATURED_PROB = FEATURED_RATE / TOTAL_3STAR_RATE

    students_obtained = {"A": False, "B": False}
    total_pulls = 0
    free_pulls_used = 0
    pyro_spent = 0
    pity_200_hits = 0
    sparks_used = 0

    if system == "NEW":
        charge_count = 0
        for target in ["A", "B"]:
            if students_obtained[target]:
                continue

            while not students_obtained[target]:
                total_pulls += 1
                charge_count += 1

                if total_pulls <= 100:
                    free_pulls_used += 1
                else:
                    pyro_spent += 120

                if charge_count == 200:
                    students_obtained[target] = True
                    pity_200_hits += 1
                    charge_count = 0
                    break
                elif charge_count == 100:
                    if random.random() < 0.5:
                        students_obtained[target] = True
                        charge_count = 0
                        break
                else:
                    if random.random() < TOTAL_3STAR_RATE:
                        if random.random() < NATURAL_FEATURED_PROB:
                            students_obtained[target] = True
                            charge_count = 0
                            break
                        else:
                            other = "B" if target == "A" else "A"
                            if not students_obtained[other] and random.random() < 0.01:
                                students_obtained[other] = True

        return {
            "total_pulls": total_pulls,
            "free_pulls_used": free_pulls_used,
            "pyro_spent": pyro_spent,
            "got_both_for_0_pyro": pyro_spent == 0,
            "pity_200_hits": pity_200_hits
        }

    else:  # OLD SYSTEM
        recruitment_points = 0
        while not (students_obtained["A"] and students_obtained["B"]):
            target = "A" if not students_obtained["A"] else "B"
            total_pulls += 1
            recruitment_points += 1

            if total_pulls <= 100:
                free_pulls_used += 1
            else:
                pyro_spent += 120

            if random.random() < TOTAL_3STAR_RATE:
                if random.random() < NATURAL_FEATURED_PROB:
                    students_obtained[target] = True
                else:
                    other = "B" if target == "A" else "A"
                    if not students_obtained[other] and random.random() < 0.01:
                        students_obtained[other] = True

            if students_obtained["A"] and students_obtained["B"]:
                break

            if recruitment_points == 200:
                if not students_obtained["A"]:
                    students_obtained["A"] = True
                elif not students_obtained["B"]:
                    students_obtained["B"] = True
                sparks_used += 1
                recruitment_points = 0

        return {
            "total_pulls": total_pulls,
            "free_pulls_used": free_pulls_used,
            "pyro_spent": pyro_spent,
            "got_both_for_0_pyro": pyro_spent == 0,
            "sparks_used": sparks_used
        }


def simulate_fes_second_half_dual(system="NEW", behavior="TARGET_STOP"):
    """
    Simulates Second Half (6.0% Double Rate Fes Dual Banner):
    - Target: Get BOTH Fes Student A and Fes Student B.
    - Behavior "TARGET_STOP": Stop pulling as soon as BOTH are obtained.
    - Behavior "FULL_DUMP": Pull at least 200 pulls (24,000 Pyroxenes) to maximize 3★ yield & spark dupes.
    """
    TOTAL_3STAR_RATE = 0.06  # 6.0% Fes Double Rate
    FEATURED_RATE = 0.007
    NATURAL_FEATURED_PROB = FEATURED_RATE / TOTAL_3STAR_RATE

    students_obtained = {"A": False, "B": False}
    total_pulls = 0
    pyro_spent = 0
    total_3stars = 0
    featured_copies = 0
    pity_200_hits = 0
    sparks_used = 0

    if behavior == "TARGET_STOP":
        if system == "NEW":
            charge_count = 0
            for target in ["A", "B"]:
                if students_obtained[target]:
                    continue

                while not students_obtained[target]:
                    total_pulls += 1
                    charge_count += 1
                    pyro_spent += 120

                    if charge_count == 200:
                        students_obtained[target] = True
                        pity_200_hits += 1
                        total_3stars += 1
                        featured_copies += 1
                        charge_count = 0
                        break
                    elif charge_count == 100:
                        total_3stars += 1
                        if random.random() < 0.5:
                            students_obtained[target] = True
                            featured_copies += 1
                            charge_count = 0
                            break
                    else:
                        if random.random() < TOTAL_3STAR_RATE:
                            total_3stars += 1
                            if random.random() < NATURAL_FEATURED_PROB:
                                students_obtained[target] = True
                                featured_copies += 1
                                charge_count = 0
                                break
                            else:
                                other = "B" if target == "A" else "A"
                                if not students_obtained[other] and random.random() < 0.01:
                                    students_obtained[other] = True
                                    featured_copies += 1

            return {
                "total_pulls": total_pulls,
                "pyro_spent": pyro_spent,
                "total_3stars": total_3stars,
                "featured_copies": featured_copies,
                "pity_200_hits": pity_200_hits
            }

        else:  # OLD SYSTEM
            recruitment_points = 0
            while not (students_obtained["A"] and students_obtained["B"]):
                target = "A" if not students_obtained["A"] else "B"
                total_pulls += 1
                recruitment_points += 1
                pyro_spent += 120

                if random.random() < TOTAL_3STAR_RATE:
                    total_3stars += 1
                    if random.random() < NATURAL_FEATURED_PROB:
                        students_obtained[target] = True
                        featured_copies += 1
                    else:
                        other = "B" if target == "A" else "A"
                        if not students_obtained[other] and random.random() < 0.01:
                            students_obtained[other] = True
                            featured_copies += 1

                if students_obtained["A"] and students_obtained["B"]:
                    break

                if recruitment_points == 200:
                    if not students_obtained["A"]:
                        students_obtained["A"] = True
                    elif not students_obtained["B"]:
                        students_obtained["B"] = True
                    featured_copies += 1
                    sparks_used += 1
                    recruitment_points = 0

            return {
                "total_pulls": total_pulls,
                "pyro_spent": pyro_spent,
                "total_3stars": total_3stars,
                "featured_copies": featured_copies,
                "sparks_used": sparks_used
            }

    else:  # Behavior "FULL_DUMP" (Burn at least 200 pulls / 24,000 Pyroxenes)
        total_pulls = 200
        pyro_spent = 24000
        charge_count = 0
        recruitment_points = 0

        if system == "NEW":
            pity_200_hits = 0
            for p in range(1, 201):
                target = "A" if not students_obtained["A"] else "B"
                charge_count += 1
                if charge_count == 200:
                    students_obtained[target] = True
                    total_3stars += 1
                    featured_copies += 1
                    pity_200_hits += 1
                    charge_count = 0
                elif charge_count == 100:
                    total_3stars += 1
                    if random.random() < 0.5:
                        students_obtained[target] = True
                        featured_copies += 1
                        charge_count = 0
                else:
                    if random.random() < TOTAL_3STAR_RATE:
                        total_3stars += 1
                        if random.random() < NATURAL_FEATURED_PROB:
                            students_obtained[target] = True
                            featured_copies += 1
                            charge_count = 0
                        else:
                            other = "B" if target == "A" else "A"
                            if not students_obtained[other] and random.random() < 0.01:
                                students_obtained[other] = True
                                featured_copies += 1

            # Ensure both students obtained (do extra pulls if missing B after 200)
            while not (students_obtained["A"] and students_obtained["B"]):
                target = "A" if not students_obtained["A"] else "B"
                total_pulls += 1
                charge_count += 1
                pyro_spent += 120
                if charge_count == 200:
                    students_obtained[target] = True
                    total_3stars += 1
                    featured_copies += 1
                    pity_200_hits += 1
                    charge_count = 0
                    break
                elif charge_count == 100:
                    total_3stars += 1
                    if random.random() < 0.5:
                        students_obtained[target] = True
                        featured_copies += 1
                        charge_count = 0
                        break
                else:
                    if random.random() < TOTAL_3STAR_RATE:
                        total_3stars += 1
                        if random.random() < NATURAL_FEATURED_PROB:
                            students_obtained[target] = True
                            featured_copies += 1
                            charge_count = 0
                            break

            return {
                "total_pulls": total_pulls,
                "pyro_spent": pyro_spent,
                "total_3stars": total_3stars,
                "featured_copies": featured_copies,
                "pity_200_hits": pity_200_hits
            }

        else:  # OLD SYSTEM
            sparks_used = 0
            for p in range(1, 201):
                target = "A" if not students_obtained["A"] else "B"
                recruitment_points += 1
                if random.random() < TOTAL_3STAR_RATE:
                    total_3stars += 1
                    if random.random() < NATURAL_FEATURED_PROB:
                        students_obtained[target] = True
                        featured_copies += 1

            if not students_obtained["A"]:
                students_obtained["A"] = True
            elif not students_obtained["B"]:
                students_obtained["B"] = True
            featured_copies += 1
            sparks_used += 1
            recruitment_points = 0

            while not (students_obtained["A"] and students_obtained["B"]):
                target = "A" if not students_obtained["A"] else "B"
                total_pulls += 1
                recruitment_points += 1
                pyro_spent += 120

                if random.random() < TOTAL_3STAR_RATE:
                    total_3stars += 1
                    if random.random() < NATURAL_FEATURED_PROB:
                        students_obtained[target] = True
                        featured_copies += 1

                if recruitment_points == 200:
                    if not students_obtained["A"]:
                        students_obtained["A"] = True
                    elif not students_obtained["B"]:
                        students_obtained["B"] = True
                    featured_copies += 1
                    sparks_used += 1
                    recruitment_points = 0
                    break

            return {
                "total_pulls": total_pulls,
                "pyro_spent": pyro_spent,
                "total_3stars": total_3stars,
                "featured_copies": featured_copies,
                "sparks_used": sparks_used
            }


# ==============================================================================
# MAIN COMPARATIVE SIMULATION EXECUTION
# ==============================================================================

def run_comparative_simulation(num_senseis=100000):
    print("==================================================================")
    print(f"       BLUE ARCHIVE GACHA SIMULATION ({num_senseis:,} SENSEIS)")
    print("==================================================================\n")

    # --------------------------------------------------------------------------
    # PART 1: REGULAR DUAL BANNER DETAILED COMPARISON
    # --------------------------------------------------------------------------
    new_results = [simulate_new_system_dual() for _ in range(num_senseis)]
    old_results = [simulate_old_system_dual() for _ in range(num_senseis)]

    new_pulls = [r["total_pulls"] for r in new_results]
    new_avg_pulls = sum(new_pulls) / num_senseis
    new_avg_pyro = new_avg_pulls * 120

    old_pulls = [r["total_pulls"] for r in old_results]
    old_avg_pulls = sum(old_pulls) / num_senseis
    old_avg_pyro = old_avg_pulls * 120

    old_0_sparks = sum(1 for r in old_results if r["sparks_used"] == 0)
    old_1_spark = sum(1 for r in old_results if r["sparks_used"] == 1)
    old_2_sparks = sum(1 for r in old_results if r["sparks_used"] == 2)

    saved_pulls = old_avg_pulls - new_avg_pulls
    saved_pyroxenes = old_avg_pyro - new_avg_pyro
    savings_pct = (saved_pulls / old_avg_pulls) * 100

    print("--- 1. REGULAR DUAL BANNER COMPARISON (GET BOTH A & B) ---")
    print(" Rules Supplement:")
    print("  • New System: 3.0% Rate (0.7% Featured), 100-Charge 50/50, 200-Charge Guarantee.")
    print("  • Old System: 3.0% Rate (0.7% Featured), 200 Points = 1 Shop Spark.")
    print(" Stats:")
    print("  [NEW SYSTEM DETAILED STATS]")
    print(f"   • Average Pulls Required:     {new_avg_pulls:.2f} pulls")
    print(f"   • Average Pyroxene Cost:      ~{int(new_avg_pyro):,} Pyroxenes")
    print(f"   • Min / Max Pulls Range:      {min(new_pulls)} - {max(new_pulls)} pulls")
    print(f"   • Needed 0 Hard Pities (200): {sum(1 for r in new_results if r['pity_200_hits'] == 0):6d} Senseis ({sum(1 for r in new_results if r['pity_200_hits'] == 0)/num_senseis*100:.2f}%)")
    print(f"   • Needed 1 Hard Pity  (200): {sum(1 for r in new_results if r['pity_200_hits'] == 1):6d} Senseis ({sum(1 for r in new_results if r['pity_200_hits'] == 1)/num_senseis*100:.2f}%)")
    print(f"   • Needed 2 Hard Pities (200): {sum(1 for r in new_results if r['pity_200_hits'] == 2):6d} Senseis ({sum(1 for r in new_results if r['pity_200_hits'] == 2)/num_senseis*100:.2f}%)\n")

    print("  [OLD SYSTEM DETAILED STATS]")
    print(f"   • Average Pulls Required:     {old_avg_pulls:.2f} pulls")
    print(f"   • Average Pyroxene Cost:      ~{int(old_avg_pyro):,} Pyroxenes")
    print(f"   • Min / Max Pulls Range:      {min(old_pulls)} - {max(old_pulls)} pulls")
    print(f"   • Needed 0 Sparks (Both Luck):{old_0_sparks:6d} Senseis ({old_0_sparks/num_senseis*100:.2f}%)")
    print(f"   • Needed 1 Spark  (1 Redeem):{old_1_spark:6d} Senseis ({old_1_spark/num_senseis*100:.2f}%)")
    print(f"   • Needed 2 Sparks (Max Pitied):{old_2_sparks:6d} Senseis ({old_2_sparks/num_senseis*100:.2f}%)\n")

    print("  [SAVINGS SUMMARY]")
    print(f"   • Avg Pulls Saved per Sensei: {saved_pulls:.2f} pulls ({savings_pct:.2f}% reduction!)")
    print(f"   • Avg Pyroxenes Saved:        ~{int(saved_pyroxenes):,} Pyroxenes\n")

    # --------------------------------------------------------------------------
    # PART 2: FEST EVENT SIMULATION (DUAL PRE-FES + DUAL FES BANNER)
    # --------------------------------------------------------------------------
    pre_fes_new = [simulate_pre_fes_free_pulls_dual("NEW") for _ in range(num_senseis)]
    pre_fes_old = [simulate_pre_fes_free_pulls_dual("OLD") for _ in range(num_senseis)]

    fes_new_stop = [simulate_fes_second_half_dual("NEW", "TARGET_STOP") for _ in range(num_senseis)]
    fes_old_stop = [simulate_fes_second_half_dual("OLD", "TARGET_STOP") for _ in range(num_senseis)]

    fes_new_dump = [simulate_fes_second_half_dual("NEW", "FULL_DUMP") for _ in range(num_senseis)]
    fes_old_dump = [simulate_fes_second_half_dual("OLD", "FULL_DUMP") for _ in range(num_senseis)]

    print("--- 2. FEST EVENT SIMULATION (DUAL BANNER 1ST HALF & DUAL BANNER 2ND HALF) ---")
    print(" Rules Supplement:")
    print("  • 1st Half (Pre-Fes Dual Banner): Target BOTH Pre-Fes A & B. 100 Free Pulls awarded.")
    print("  • 2nd Half (Fes Dual Banner): Target BOTH Fes A & B. Double 3★ Rate (6.0% overall, 0.7% featured).\n")

    # --- 2.1 FIRST HALF ---
    pn_pulls = [r["total_pulls"] for r in pre_fes_new]
    pn_avg_pulls = sum(pn_pulls) / num_senseis
    pn_avg_pyro = sum(r["pyro_spent"] for r in pre_fes_new) / num_senseis
    pn_zero = sum(1 for r in pre_fes_new if r["got_both_for_0_pyro"])

    po_pulls = [r["total_pulls"] for r in pre_fes_old]
    po_avg_pulls = sum(po_pulls) / num_senseis
    po_avg_pyro = sum(r["pyro_spent"] for r in pre_fes_old) / num_senseis
    po_zero = sum(1 for r in pre_fes_old if r["got_both_for_0_pyro"])

    p_saved_pulls = po_avg_pulls - pn_avg_pulls
    p_saved_pyro = po_avg_pyro - pn_avg_pyro
    p_savings_pct = (p_saved_pulls / po_avg_pulls) * 100 if po_avg_pulls > 0 else 0

    print(" [FIRST HALF: PRE-FES DUAL BANNER + 100 FREE PULLS (GET BOTH A & B)]")
    print("  [NEW SYSTEM DETAILED STATS]")
    print(f"   • Average Pulls Required:     {pn_avg_pulls:.2f} pulls")
    print(f"   • Average Pyroxene Cost:      ~{int(pn_avg_pyro):,} Pyroxenes")
    print(f"   • Min / Max Pulls Range:      {min(pn_pulls)} - {max(pn_pulls)} pulls")
    print(f"   • Got BOTH for 0 Pyroxene:    {pn_zero:6d} Senseis ({pn_zero/num_senseis*100:.2f}%)")
    print(f"   • Needed 0 Hard Pities (200): {sum(1 for r in pre_fes_new if r['pity_200_hits'] == 0):6d} Senseis ({sum(1 for r in pre_fes_new if r['pity_200_hits'] == 0)/num_senseis*100:.2f}%)")
    print(f"   • Needed 1 Hard Pity  (200): {sum(1 for r in pre_fes_new if r['pity_200_hits'] == 1):6d} Senseis ({sum(1 for r in pre_fes_new if r['pity_200_hits'] == 1)/num_senseis*100:.2f}%)")
    print(f"   • Needed 2 Hard Pities (200): {sum(1 for r in pre_fes_new if r['pity_200_hits'] >= 2):6d} Senseis ({sum(1 for r in pre_fes_new if r['pity_200_hits'] >= 2)/num_senseis*100:.2f}%)\n")

    print("  [OLD SYSTEM DETAILED STATS]")
    po_0_sparks = sum(1 for r in pre_fes_old if r["sparks_used"] == 0)
    po_1_spark = sum(1 for r in pre_fes_old if r["sparks_used"] == 1)
    po_2_sparks = sum(1 for r in pre_fes_old if r["sparks_used"] >= 2)
    print(f"   • Average Pulls Required:     {po_avg_pulls:.2f} pulls")
    print(f"   • Average Pyroxene Cost:      ~{int(po_avg_pyro):,} Pyroxenes")
    print(f"   • Min / Max Pulls Range:      {min(po_pulls)} - {max(po_pulls)} pulls")
    print(f"   • Got BOTH for 0 Pyroxene:    {po_zero:6d} Senseis ({po_zero/num_senseis*100:.2f}%)")
    print(f"   • Needed 0 Sparks (Both Luck):{po_0_sparks:6d} Senseis ({po_0_sparks/num_senseis*100:.2f}%)")
    print(f"   • Needed 1 Spark  (1 Redeem):{po_1_spark:6d} Senseis ({po_1_spark/num_senseis*100:.2f}%)")
    print(f"   • Needed 2 Sparks (Max Pitied):{po_2_sparks:6d} Senseis ({po_2_sparks/num_senseis*100:.2f}%)\n")

    print("  [SAVINGS SUMMARY]")
    print(f"   • Avg Pulls Saved per Sensei: {p_saved_pulls:.2f} pulls ({p_savings_pct:.2f}% reduction!)")
    print(f"   • Avg Pyroxenes Saved:        ~{int(p_saved_pyro):,} Pyroxenes\n")

    # --- 2.2 SECOND HALF: BEHAVIOR A ---
    fn_a_pulls = [r["total_pulls"] for r in fes_new_stop]
    fn_a_avg_pulls = sum(fn_a_pulls) / num_senseis
    fn_a_avg_pyro = sum(r["pyro_spent"] for r in fes_new_stop) / num_senseis
    fn_a_avg_3star = sum(r["total_3stars"] for r in fes_new_stop) / num_senseis

    fo_a_pulls = [r["total_pulls"] for r in fes_old_stop]
    fo_a_avg_pulls = sum(fo_a_pulls) / num_senseis
    fo_a_avg_pyro = sum(r["pyro_spent"] for r in fes_old_stop) / num_senseis
    fo_a_avg_3star = sum(r["total_3stars"] for r in fes_old_stop) / num_senseis

    fa_saved_pulls = fo_a_avg_pulls - fn_a_avg_pulls
    fa_saved_pyro = fo_a_avg_pyro - fn_a_avg_pyro
    fa_savings_pct = (fa_saved_pulls / fo_a_avg_pulls) * 100 if fo_a_avg_pulls > 0 else 0

    print(" [SECOND HALF: 6.0% DUAL FES BANNER - BEHAVIOR A (STOP WHEN BOTH OBTAINED)]")
    print("  [NEW SYSTEM DETAILED STATS]")
    print(f"   • Average Pulls Required:     {fn_a_avg_pulls:.2f} pulls")
    print(f"   • Average Pyroxene Cost:      ~{int(fn_a_avg_pyro):,} Pyroxenes")
    print(f"   • Min / Max Pulls Range:      {min(fn_a_pulls)} - {max(fn_a_pulls)} pulls")
    print(f"   • Avg 3★ Yielded (6% Rate):   {fn_a_avg_3star:.2f} 3-star students")
    print(f"   • Needed 0 Hard Pities (200): {sum(1 for r in fes_new_stop if r['pity_200_hits'] == 0):6d} Senseis ({sum(1 for r in fes_new_stop if r['pity_200_hits'] == 0)/num_senseis*100:.2f}%)")
    print(f"   • Needed 1 Hard Pity  (200): {sum(1 for r in fes_new_stop if r['pity_200_hits'] == 1):6d} Senseis ({sum(1 for r in fes_new_stop if r['pity_200_hits'] == 1)/num_senseis*100:.2f}%)")
    print(f"   • Needed 2 Hard Pities (200): {sum(1 for r in fes_new_stop if r['pity_200_hits'] >= 2):6d} Senseis ({sum(1 for r in fes_new_stop if r['pity_200_hits'] >= 2)/num_senseis*100:.2f}%)\n")

    print("  [OLD SYSTEM DETAILED STATS]")
    fo_a_0_sparks = sum(1 for r in fes_old_stop if r["sparks_used"] == 0)
    fo_a_1_spark = sum(1 for r in fes_old_stop if r["sparks_used"] == 1)
    fo_a_2_sparks = sum(1 for r in fes_old_stop if r["sparks_used"] >= 2)
    print(f"   • Average Pulls Required:     {fo_a_avg_pulls:.2f} pulls")
    print(f"   • Average Pyroxene Cost:      ~{int(fo_a_avg_pyro):,} Pyroxenes")
    print(f"   • Min / Max Pulls Range:      {min(fo_a_pulls)} - {max(fo_a_pulls)} pulls")
    print(f"   • Avg 3★ Yielded (6% Rate):   {fo_a_avg_3star:.2f} 3-star students")
    print(f"   • Needed 0 Sparks (Both Luck):{fo_a_0_sparks:6d} Senseis ({fo_a_0_sparks/num_senseis*100:.2f}%)")
    print(f"   • Needed 1 Spark  (1 Redeem):{fo_a_1_spark:6d} Senseis ({fo_a_1_spark/num_senseis*100:.2f}%)")
    print(f"   • Needed 2 Sparks (Max Pitied):{fo_a_2_sparks:6d} Senseis ({fo_a_2_sparks/num_senseis*100:.2f}%)\n")

    print("  [SAVINGS SUMMARY]")
    print(f"   • Avg Pulls Saved per Sensei: {fa_saved_pulls:.2f} pulls ({fa_savings_pct:.2f}% reduction!)")
    print(f"   • Avg Pyroxenes Saved:        ~{int(fa_saved_pyro):,} Pyroxenes\n")

    # --- 2.3 SECOND HALF: BEHAVIOR B ---
    fn_b_pulls = [r["total_pulls"] for r in fes_new_dump]
    fn_b_avg_pulls = sum(fn_b_pulls) / num_senseis
    fn_b_avg_pyro = sum(r["pyro_spent"] for r in fes_new_dump) / num_senseis
    fn_b_avg_3star = sum(r["total_3stars"] for r in fes_new_dump) / num_senseis
    fn_b_avg_copies = sum(r["featured_copies"] for r in fes_new_dump) / num_senseis

    fo_b_pulls = [r["total_pulls"] for r in fes_old_dump]
    fo_b_avg_pulls = sum(fo_b_pulls) / num_senseis
    fo_b_avg_pyro = sum(r["pyro_spent"] for r in fes_old_dump) / num_senseis
    fo_b_avg_3star = sum(r["total_3stars"] for r in fes_old_dump) / num_senseis
    fo_b_avg_copies = sum(r["featured_copies"] for r in fes_old_dump) / num_senseis

    fb_saved_pulls = fo_b_avg_pulls - fn_b_avg_pulls
    fb_saved_pyro = fo_b_avg_pyro - fn_b_avg_pyro

    print(" [SECOND HALF: 6.0% DUAL FES BANNER - BEHAVIOR B (FULL GEM DUMP / AT LEAST 200 PULLS)]")
    print("  [NEW SYSTEM DETAILED STATS]")
    print(f"   • Average Pulls Required:     {fn_b_avg_pulls:.2f} pulls")
    print(f"   • Average Pyroxene Cost:      ~{int(fn_b_avg_pyro):,} Pyroxenes")
    print(f"   • Min / Max Pulls Range:      {min(fn_b_pulls)} - {max(fn_b_pulls)} pulls")
    print(f"   • Total 3★ Yielded (6% Rate): {fn_b_avg_3star:.2f} 3-star students")
    print(f"   • Featured Copies Count:      {fn_b_avg_copies:.2f} copies")
    print(f"   • Needed 0 Hard Pities (200): {sum(1 for r in fes_new_dump if r['pity_200_hits'] == 0):6d} Senseis ({sum(1 for r in fes_new_dump if r['pity_200_hits'] == 0)/num_senseis*100:.2f}%)")
    print(f"   • Needed 1 Hard Pity  (200): {sum(1 for r in fes_new_dump if r['pity_200_hits'] == 1):6d} Senseis ({sum(1 for r in fes_new_dump if r['pity_200_hits'] == 1)/num_senseis*100:.2f}%)")
    print(f"   • Needed 2 Hard Pities (200): {sum(1 for r in fes_new_dump if r['pity_200_hits'] >= 2):6d} Senseis ({sum(1 for r in fes_new_dump if r['pity_200_hits'] >= 2)/num_senseis*100:.2f}%)\n")

    print("  [OLD SYSTEM DETAILED STATS]")
    fo_b_0_sparks = sum(1 for r in fes_old_dump if r["sparks_used"] == 0)
    fo_b_1_spark = sum(1 for r in fes_old_dump if r["sparks_used"] == 1)
    fo_b_2_sparks = sum(1 for r in fes_old_dump if r["sparks_used"] >= 2)
    print(f"   • Average Pulls Required:     {fo_b_avg_pulls:.2f} pulls")
    print(f"   • Average Pyroxene Cost:      ~{int(fo_b_avg_pyro):,} Pyroxenes")
    print(f"   • Min / Max Pulls Range:      {min(fo_b_pulls)} - {max(fo_b_pulls)} pulls")
    print(f"   • Total 3★ Yielded (6% Rate): {fo_b_avg_3star:.2f} 3-star students")
    print(f"   • Featured Copies Count:      {fo_b_avg_copies:.2f} copies")
    print(f"   • Needed 0 Sparks:            {fo_b_0_sparks:6d} Senseis ({fo_b_0_sparks/num_senseis*100:.2f}%)")
    print(f"   • Needed 1 Spark:             {fo_b_1_spark:6d} Senseis ({fo_b_1_spark/num_senseis*100:.2f}%)")
    print(f"   • Needed 2 Sparks (Max Pitied):{fo_b_2_sparks:6d} Senseis ({fo_b_2_sparks/num_senseis*100:.2f}%)\n")

    print("  [SAVINGS SUMMARY]")
    print(f"   • Avg Extra Pulls Saved:      {fb_saved_pulls:.2f} pulls")
    print(f"   • Avg Extra Pyroxenes Saved:  ~{int(fb_saved_pyro):,} Pyroxenes")
    print("==================================================================\n")

    input("Simulation complete! Press ENTER to exit...")

if __name__ == "__main__":
    run_comparative_simulation(100000)