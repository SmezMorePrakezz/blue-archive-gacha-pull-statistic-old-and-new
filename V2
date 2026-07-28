import random
import os
import sys

# Try importing matplotlib for graphical chart generation
try:
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

# ==============================================================================
# HELPER FUNCTIONS & DISTRIBUTIONS
# ==============================================================================

def clear_screen():
    """Clears the terminal console screen based on OS."""
    os.system('cls' if os.name == 'nt' else 'clear')


def safe_input(prompt=""):
    """Safely handles standard input calls, catching missing stream/PyInstaller errors."""
    if sys.stdin is None:
        print("\n[Error] No console stream attached (sys.stdin is None).")
        sys.exit(1)
    try:
        return input(prompt)
    except (RuntimeError, EOFError):
        print("\n[Error] Console input lost or detached.")
        sys.exit(1)


def flush_input():
    """Flushes leftover keypresses or newline characters from the stdin buffer."""
    if sys.stdin is None:
        return
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except (ImportError, Exception):
        try:
            import select
            if hasattr(sys.stdin, 'fileno'):
                while select.select([sys.stdin], [], [], 0)[0]:
                    sys.stdin.read(1)
        except Exception:
            pass


def get_single_keypress(prompt=""):
    """Reads a single keypress from the terminal without requiring the ENTER key."""
    if sys.stdin is None:
        return ""
        
    flush_input()
    if prompt:
        print(prompt, end="", flush=True)
    
    ch = ""
    try:
        import msvcrt
        ch = msvcrt.getch().decode('utf-8', errors='ignore')
        print(ch)
    except (ImportError, Exception):
        try:
            import tty, termios
            if hasattr(sys.stdin, 'fileno'):
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(fd)
                    ch = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                print(ch)
            else:
                ch = safe_input().strip()
        except Exception:
            ch = safe_input().strip()

    return ch


def print_10_pull_distribution(pull_counts, total_senseis, title="10-PULL BRACKET DISTRIBUTION"):
    """Displays pull count distribution in 10-roll brackets with horizontal bar graph."""
    if not pull_counts:
        return
    
    max_p = max(pull_counts)
    num_bins = (max_p + 9) // 10
    
    print(f"  [{title}]")
    for i in range(num_bins):
        low = i * 10 + 1
        high = (i + 1) * 10
        count = sum(1 for p in pull_counts if low <= p <= high)
        pct = (count / total_senseis) * 100
        bar_len = int(round(pct))
        bar = "█" * bar_len if bar_len > 0 else ("▏" if count > 0 else "")
        print(f"   • {low:3d} - {high:3d} pulls: {count:6d} Senseis ({pct:6.2f}%) | {bar}")
    print()


# ==============================================================================
# SECTION 1: MASS SIMULATION FUNCTIONS (DUAL BANNERS)
# ==============================================================================

def simulate_new_system_dual(total_3star_rate=0.03, featured_rate=0.007):
    """
    Simulates a single Sensei in the NEW 'Recruitment Charge' System:
    - Base 3★ rate: 3.0% (Featured: 0.7%, Off-rate spooks: 2.3%)
    - Charge ONLY resets when a featured student is obtained.
    - 100th charge: Guaranteed 3★ with a 50/50 chance for the featured student.
    - 200th charge: 100% Hard Guarantee for the featured student.
    - Milestone Rule: At rolls 70, 130, 170, 270, 330, 370... receives a 10-Ticket (used immediately).
    """
    TOTAL_3STAR_RATE = total_3star_rate
    FEATURED_RATE = featured_rate
    NATURAL_FEATURED_PROB = FEATURED_RATE / TOTAL_3STAR_RATE

    charge_count = 0
    total_pulls = 0
    spooks = 0
    ticket_pulls_remaining = 0
    pyro_spent = 0
    
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

            # Pyroxene cost calculation
            if ticket_pulls_remaining > 0:
                ticket_pulls_remaining -= 1
            else:
                pyro_spent += 120

            # 10-Ticket Milestone Reward Check
            if total_pulls % 200 in (70, 130, 170):
                ticket_pulls_remaining += 10

            # Case 1: Hard Guarantee at 200 Charges
            if charge_count == 200:
                students_obtained[target] = True
                pity_200_hits += 1
                charge_count = 0
                break

            # Case 2: 100th Charge Guarantee (50/50)
            elif charge_count == 100:
                is_featured = random.random() < 0.5
                if is_featured:
                    pity_100_wins += 1
                    students_obtained[target] = True
                    charge_count = 0
                    break
                else:
                    pity_100_losses += 1
                    spooks += 1

            # Case 3: Standard Pull
            else:
                if random.random() < TOTAL_3STAR_RATE:
                    if random.random() < NATURAL_FEATURED_PROB:
                        students_obtained[target] = True
                        charge_count = 0
                        break
                    else:
                        spooks += 1
                        other_target = "B" if target == "A" else "A"
                        if not students_obtained[other_target] and random.random() < 0.01:
                            students_obtained[other_target] = True

    return {
        "total_pulls": total_pulls,
        "pyro_spent": pyro_spent,
        "spooks": spooks,
        "pity_100_wins": pity_100_wins,
        "pity_100_losses": pity_100_losses,
        "pity_200_hits": pity_200_hits,
    }


def simulate_old_system_dual(total_3star_rate=0.03, featured_rate=0.007):
    """
    Simulates a single Sensei in the OLD 'Recruitment Points' (Spark) System.
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
            recruitment_points = 0

    return {
        "total_pulls": total_pulls,
        "pyro_spent": total_pulls * 120,
        "spooks": spooks,
        "sparks_used": sparks_used,
    }


def simulate_pre_fes_free_pulls_dual(system="NEW"):
    """First Half Pre-Fes Dual Banner (100 Free Pulls)."""
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
        ticket_pulls_remaining = 0
        free_event_pulls_remaining = 100

        for target in ["A", "B"]:
            if students_obtained[target]:
                continue

            while not students_obtained[target]:
                total_pulls += 1
                charge_count += 1

                if ticket_pulls_remaining > 0:
                    ticket_pulls_remaining -= 1
                elif free_event_pulls_remaining > 0:
                    free_event_pulls_remaining -= 1
                    free_pulls_used += 1
                else:
                    pyro_spent += 120

                if total_pulls % 200 in (70, 130, 170):
                    ticket_pulls_remaining += 10

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

    else:
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
    """Second Half 6.0% Fes Dual Banner."""
    TOTAL_3STAR_RATE = 0.06
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
            ticket_pulls_remaining = 0
            for target in ["A", "B"]:
                if students_obtained[target]:
                    continue

                while not students_obtained[target]:
                    total_pulls += 1
                    charge_count += 1

                    if ticket_pulls_remaining > 0:
                        ticket_pulls_remaining -= 1
                    else:
                        pyro_spent += 120

                    if total_pulls % 200 in (70, 130, 170):
                        ticket_pulls_remaining += 10

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

        else:
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

    else:  # Behavior "FULL_DUMP"
        total_pulls = 200
        charge_count = 0
        recruitment_points = 0

        if system == "NEW":
            pity_200_hits = 0
            ticket_pulls_remaining = 0
            for p in range(1, 201):
                target = "A" if not students_obtained["A"] else "B"
                charge_count += 1

                if ticket_pulls_remaining > 0:
                    ticket_pulls_remaining -= 1
                else:
                    pyro_spent += 120

                if p % 200 in (70, 130, 170):
                    ticket_pulls_remaining += 10

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

            while not (students_obtained["A"] and students_obtained["B"]):
                target = "A" if not students_obtained["A"] else "B"
                total_pulls += 1
                charge_count += 1

                if ticket_pulls_remaining > 0:
                    ticket_pulls_remaining -= 1
                else:
                    pyro_spent += 120

                if total_pulls % 200 in (70, 130, 170):
                    ticket_pulls_remaining += 10

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

        else:
            sparks_used = 0
            pyro_spent = 24000
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
# SECTION 2: GRAPHICAL CHART GENERATOR
# ==============================================================================

def generate_graphical_report(data_store, save_prefix="blue_archive_gacha_stats", show_plot=True):
    """Generates 6 separate visual report charts using Matplotlib."""
    if not MATPLOTLIB_AVAILABLE:
        print("\n[Notice] Matplotlib not found. Skipping PNG chart export.")
        return

    plt.style.use('dark_background')
    COLOR_NEW = '#38bdf8'
    COLOR_OLD = '#f43f5e'
    total_senseis = data_store['num_senseis']

    def plot_bracket_chart(new_pulls, old_pulls, title, filename_suffix, highlight_free_zone=False):
        max_p = max(max(new_pulls), max(old_pulls))
        num_bins = max(40, (max_p + 9) // 10)
        brackets = [f"{i*10+1}-{(i+1)*10}" for i in range(num_bins)]

        new_pcts = [(sum(1 for p in new_pulls if i*10+1 <= p <= (i+1)*10) / total_senseis) * 100 for i in range(num_bins)]
        old_pcts = [(sum(1 for p in old_pulls if i*10+1 <= p <= (i+1)*10) / total_senseis) * 100 for i in range(num_bins)]

        fig, ax = plt.subplots(figsize=(18, 8), facecolor='#0f172a')
        ax.set_facecolor('#1e293b')
        fig.suptitle(f"{title}\nNew System (Charge Pity + 10-Ticket Milestones) vs. Old System (200 Spark Points)",
                     fontsize=14, fontweight='bold', color='#f8fafc', y=0.97)

        x = range(num_bins)
        width = 0.40

        rects1 = ax.bar([p - width/2 for p in x], new_pcts, width, label='New System', color=COLOR_NEW, alpha=0.9)
        rects2 = ax.bar([p + width/2 for p in x], old_pcts, width, label='Old System', color=COLOR_OLD, alpha=0.9)

        if highlight_free_zone:
            ax.axvspan(-0.5, 9.5, color='#22c55e', alpha=0.1, label='100 Free Rolls Zone (0 Pyroxenes Spent)')

        ax.set_xticks(x)
        ax.set_xticklabels(brackets, rotation=60, ha='right', fontsize=8, color='#cbd5e1')
        ax.set_xlabel("10-Pull Roll Brackets", fontsize=11, fontweight='bold', color='#e2e8f0', labelpad=10)
        ax.set_ylabel("Percentage of Senseis (%)", fontsize=11, fontweight='bold', color='#e2e8f0')
        ax.legend(loc='upper right', framealpha=0.4, fontsize=11)
        ax.grid(True, linestyle='--', alpha=0.2)

        for rect in rects1:
            h = rect.get_height()
            if h >= 2.5:
                ax.annotate(f"{h:.1f}%", xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 2),
                            textcoords="offset points", ha='center', va='bottom', fontsize=7, color=COLOR_NEW, fontweight='bold')
        for rect in rects2:
            h = rect.get_height()
            if h >= 2.5:
                ax.annotate(f"{h:.1f}%", xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 2),
                            textcoords="offset points", ha='center', va='bottom', fontsize=7, color=COLOR_OLD, fontweight='bold')

        plt.tight_layout(rect=[0, 0, 1, 0.93])
        fn = f"{save_prefix}_{filename_suffix}.png"
        plt.savefig(fn, dpi=200, bbox_inches='tight')
        print(f"[SUCCESS] {title} Chart saved as: {os.path.abspath(fn)}")
        if show_plot:
            try:
                plt.show()
            except Exception:
                pass

    plot_bracket_chart(data_store['reg_new_pulls'], data_store['reg_old_pulls'], "REGULAR DUAL BANNER: 10-PULL BRACKET DISTRIBUTION (1 TO 400 PULLS)", "regular_brackets")
    plot_bracket_chart(data_store['pf_new_pulls'], data_store['pf_old_pulls'], "PRE-FES DUAL BANNER (+100 FREE ROLLS): BRACKET DISTRIBUTION (1 TO 400 PULLS)", "prefes_brackets", highlight_free_zone=True)
    plot_bracket_chart(data_store['fa_new_pulls'], data_store['fa_old_pulls'], "2ND HALF FES BANNER (6.0% RATE - BEHAVIOR A: TARGET STOP): BRACKET DISTRIBUTION", "fes_a_brackets")
    plot_bracket_chart(data_store['fb_new_pulls'], data_store['fb_old_pulls'], "2ND HALF FES BANNER (6.0% RATE - BEHAVIOR B: FULL DUMP): BRACKET DISTRIBUTION", "fes_b_brackets")

    # Pyroxene Cost Comparison Bar Chart
    fig5, ax5 = plt.subplots(figsize=(14, 8), facecolor='#0f172a')
    ax5.set_facecolor('#1e293b')
    fig5.suptitle("AVERAGE PYROXENE COST COMPARISON ACROSS ALL BANNER SCENARIOS\nNew System (with 10-Ticket Milestone Rewards) vs. Old System",
                  fontsize=14, fontweight='bold', color='#f8fafc', y=0.97)

    scenarios = ["Regular Dual Banner\n(Get A & B)", "Pre-Fes Dual Banner\n(100 Free Rolls)", "2nd Half Fes 6%\n(Behavior A)", "2nd Half Fes 6%\n(Behavior B)"]
    avg_pyro_new = [data_store['reg_new_pyro'], data_store['pf_new_pyro'], data_store['fa_new_pyro'], data_store['fb_new_pyro']]
    avg_pyro_old = [data_store['reg_old_pyro'], data_store['pf_old_pyro'], data_store['fa_old_pyro'], data_store['fb_old_pyro']]

    x_s = range(len(scenarios))
    w_s = 0.35
    b1 = ax5.bar([p - w_s/2 for p in x_s], avg_pyro_new, w_s, label='New System', color=COLOR_NEW, alpha=0.9)
    b2 = ax5.bar([p + w_s/2 for p in x_s], avg_pyro_old, w_s, label='Old System', color=COLOR_OLD, alpha=0.9)

    ax5.set_xticks(x_s)
    ax5.set_xticklabels(scenarios, fontsize=10, fontweight='bold', color='#e2e8f0')
    ax5.set_ylabel("Average Pyroxenes Spent", fontsize=11, fontweight='bold', color='#e2e8f0')
    ax5.legend(loc='upper left', framealpha=0.4, fontsize=11)
    ax5.grid(True, linestyle='--', alpha=0.2)

    for rect in b1:
        y = rect.get_height()
        ax5.annotate(f"{int(y):,} Pyros", xy=(rect.get_x() + rect.get_width()/2, y),
                     xytext=(0, 4), textcoords="offset points", ha='center', va='bottom', fontsize=9, color='#7dd3fc', fontweight='bold')
    for rect in b2:
        y = rect.get_height()
        ax5.annotate(f"{int(y):,} Pyros", xy=(rect.get_x() + rect.get_width()/2, y),
                     xytext=(0, 4), textcoords="offset points", ha='center', va='bottom', fontsize=9, color='#fda4af', fontweight='bold')

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    fn5 = f"{save_prefix}_pyro_costs.png"
    plt.savefig(fn5, dpi=200, bbox_inches='tight')
    print(f"[SUCCESS] Pyroxene Cost Comparison Chart saved as: {os.path.abspath(fn5)}")

    if show_plot:
        try:
            plt.show()
        except Exception:
            pass


# ==============================================================================
# SECTION 3: INDIVIDUAL SENSEI MODE
# ==============================================================================

def simulate_individual_regular_dual(system="NEW"):
    print(f"--- INDIVIDUAL RUN: REGULAR DUAL BANNER ({system} SYSTEM) ---")
    TOTAL_3STAR_RATE = 0.03
    FEATURED_RATE = 0.007
    NATURAL_FEATURED_PROB = FEATURED_RATE / TOTAL_3STAR_RATE
    BASE_2STAR_RATE = 0.185

    students_obtained = {"A": False, "B": False}
    count_1star = 0
    count_2star = 0
    count_3star_spook = 0
    count_featured = {"A": 0, "B": 0}

    total_pulls = 0
    ten_pull_counter = 0

    if system == "NEW":
        charge = 0
        ticket_pulls = 0
        for target in ["A", "B"]:
            if students_obtained[target]:
                continue
            print(f"\n>>> Target Banner Student {target} <<<")
            while not students_obtained[target]:
                total_pulls += 1
                charge += 1
                ten_pull_counter += 1
                cost_tag = "120 Pyro"

                if ticket_pulls > 0:
                    ticket_pulls -= 1
                    cost_tag = "TICKET  "

                res_text = ""

                if charge == 200:
                    students_obtained[target] = True
                    count_featured[target] += 1
                    res_text = f"★3 FEATURED STUDENT {target}! (200 Hard Guarantee)"
                    charge = 0
                    ten_pull_counter = 0
                elif charge == 100:
                    ten_pull_counter = 0
                    if random.random() < 0.5:
                        students_obtained[target] = True
                        count_featured[target] += 1
                        res_text = f"★3 FEATURED STUDENT {target}! (Won 100-Charge 50/50)"
                        charge = 0
                    else:
                        count_3star_spook += 1
                        res_text = "★3 Non-Featured Spook (Lost 100-Charge 50/50)"
                else:
                    if random.random() < TOTAL_3STAR_RATE:
                        ten_pull_counter = 0
                        if random.random() < NATURAL_FEATURED_PROB:
                            students_obtained[target] = True
                            count_featured[target] += 1
                            res_text = f"★3 FEATURED STUDENT {target}! (Won Rate-Up)"
                            charge = 0
                        else:
                            count_3star_spook += 1
                            res_text = "★3 Non-Featured Student (Spook)"
                    else:
                        if ten_pull_counter == 10:
                            count_2star += 1
                            res_text = "★2 Student (10-Pull Protection)"
                            ten_pull_counter = 0
                        else:
                            if random.random() < (BASE_2STAR_RATE / (1.0 - TOTAL_3STAR_RATE)):
                                count_2star += 1
                                res_text = "★2 Student"
                                ten_pull_counter = 0
                            else:
                                count_1star += 1
                                res_text = "★1 Student"

                if total_pulls % 200 in (70, 130, 170):
                    ticket_pulls += 10
                    res_text += " -> [MILESTONE REWARD! +10 Recruitment Ticket!]"

                print(f"Roll {total_pulls:03d} [{cost_tag}] | Charge: {charge:03d}/200 | Result: {res_text}")
                if students_obtained[target]:
                    break
    else:
        points = 0
        while not (students_obtained["A"] and students_obtained["B"]):
            target = "A" if not students_obtained["A"] else "B"
            total_pulls += 1
            points += 1
            ten_pull_counter += 1
            res_text = ""

            if random.random() < TOTAL_3STAR_RATE:
                ten_pull_counter = 0
                if random.random() < NATURAL_FEATURED_PROB:
                    students_obtained[target] = True
                    count_featured[target] += 1
                    res_text = f"★3 FEATURED STUDENT {target}! (Natural Pull)"
                else:
                    count_3star_spook += 1
                    res_text = "★3 Non-Featured Student (Spook)"
            else:
                if ten_pull_counter == 10:
                    count_2star += 1
                    res_text = "★2 Student (10-Pull Protection)"
                    ten_pull_counter = 0
                else:
                    if random.random() < (BASE_2STAR_RATE / (1.0 - TOTAL_3STAR_RATE)):
                        count_2star += 1
                        res_text = "★2 Student"
                        ten_pull_counter = 0
                    else:
                        count_1star += 1
                        res_text = "★1 Student"

            if points == 200 and not (students_obtained["A"] and students_obtained["B"]):
                missing = "A" if not students_obtained["A"] else "B"
                students_obtained[missing] = True
                count_featured[missing] += 1
                res_text += f" -> [200 SPARK SHOP: Redeemed Student {missing}!]"
                points = 0

            print(f"Roll {total_pulls:03d} [120 Pyro] | Points: {points:03d}/200 | Target: {target} | Result: {res_text}")

    total_3stars = count_3star_spook + sum(count_featured.values())
    total_featured = sum(count_featured.values())
    print("\n" + "=" * 66)
    print(f"SUCCESS! Acquired both students in {total_pulls} total rolls.")
    print("\nSTUDENT YIELD SUMMARY:")
    print(f" • 1★ Students: {count_1star:3d}")
    print(f" • 2★ Students: {count_2star:3d}")
    print(f" • 3★ Students: {total_3stars:3d} (Featured: {total_featured} [A: {count_featured['A']}, B: {count_featured['B']}], Spooks: {count_3star_spook})")


def run_individual_mode():
    while True:
        clear_screen()
        print("==================================================================")
        print("                  INDIVIDUAL SENSEI MODE")
        print("==================================================================")
        print(" [1] Regular Dual Banner (Get Both Student A & B)")
        print(" [0] Return to Main Menu")
        flush_input()
        choice = safe_input("\nEnter choice [0-1]: ").strip()
        if choice == "0":
            break
        elif choice == "1":
            print("\nSelect System:")
            print(" [1] New System (Recruitment Charge + Milestone Tickets)")
            print(" [2] Old System (Recruitment Points / Spark)")
            sys_choice = safe_input("Enter choice [1-2]: ").strip()
            system = "NEW" if sys_choice != "2" else "OLD"
            simulate_individual_regular_dual(system)
            flush_input()
            safe_input("\nPress ENTER to return...")


# ==============================================================================
# MAIN COMPARATIVE MASS SIMULATION EXECUTION
# ==============================================================================

def run_comparative_simulation(num_senseis=100000):
    print("==================================================================")
    print(f"       BLUE ARCHIVE GACHA SIMULATION ({num_senseis:,} SENSEIS)")
    print("==================================================================\n")

    new_results = [simulate_new_system_dual() for _ in range(num_senseis)]
    old_results = [simulate_old_system_dual() for _ in range(num_senseis)]

    new_pulls = [r["total_pulls"] for r in new_results]
    new_avg_pulls = sum(new_pulls) / num_senseis
    new_avg_pyro = sum(r["pyro_spent"] for r in new_results) / num_senseis

    old_pulls = [r["total_pulls"] for r in old_results]
    old_avg_pulls = sum(old_pulls) / num_senseis
    old_avg_pyro = sum(r["pyro_spent"] for r in old_results) / num_senseis

    saved_pulls = old_avg_pulls - new_avg_pulls
    saved_pyroxenes = old_avg_pyro - new_avg_pyro
    savings_pct = (saved_pulls / old_avg_pulls) * 100

    print("--- 1. REGULAR DUAL BANNER COMPARISON (GET BOTH A & B) ---")
    print(f"  [NEW SYSTEM DETAILED STATS]")
    print(f"   • Average Pulls Required:     {new_avg_pulls:.2f} pulls")
    print(f"   • Average Pyroxene Cost:      ~{int(new_avg_pyro):,} Pyroxenes")
    print(f"   • Min / Max Pulls Range:      {min(new_pulls)} - {max(new_pulls)} pulls\n")

    print_10_pull_distribution(new_pulls, num_senseis, "NEW SYSTEM 10-PULL SET BRACKETS")

    print(f"  [OLD SYSTEM DETAILED STATS]")
    print(f"   • Average Pulls Required:     {old_avg_pulls:.2f} pulls")
    print(f"   • Average Pyroxene Cost:      ~{int(old_avg_pyro):,} Pyroxenes")
    print(f"   • Min / Max Pulls Range:      {min(old_pulls)} - {max(old_pulls)} pulls\n")

    print_10_pull_distribution(old_pulls, num_senseis, "OLD SYSTEM 10-PULL SET BRACKETS")

    print("  [SAVINGS SUMMARY]")
    print(f"   • Avg Pulls Saved per Sensei: {saved_pulls:.2f} pulls ({savings_pct:.2f}% reduction!)")
    print(f"   • Avg Pyroxenes Saved:        ~{int(saved_pyroxenes):,} Pyroxenes\n")

    pre_fes_new = [simulate_pre_fes_free_pulls_dual("NEW") for _ in range(num_senseis)]
    pre_fes_old = [simulate_pre_fes_free_pulls_dual("OLD") for _ in range(num_senseis)]
    fes_new_stop = [simulate_fes_second_half_dual("NEW", "TARGET_STOP") for _ in range(num_senseis)]
    fes_old_stop = [simulate_fes_second_half_dual("OLD", "TARGET_STOP") for _ in range(num_senseis)]
    fes_new_dump = [simulate_fes_second_half_dual("NEW", "FULL_DUMP") for _ in range(num_senseis)]
    fes_old_dump = [simulate_fes_second_half_dual("OLD", "FULL_DUMP") for _ in range(num_senseis)]

    data_store = {
        'num_senseis': num_senseis,
        'reg_new_pulls': new_pulls,
        'reg_old_pulls': old_pulls,
        'reg_new_pyro': new_avg_pyro,
        'reg_old_pyro': old_avg_pyro,
        'pf_new_pulls': [r["total_pulls"] for r in pre_fes_new],
        'pf_old_pulls': [r["total_pulls"] for r in pre_fes_old],
        'pf_new_pyro': sum(r["pyro_spent"] for r in pre_fes_new) / num_senseis,
        'pf_old_pyro': sum(r["pyro_spent"] for r in pre_fes_old) / num_senseis,
        'fa_new_pulls': [r["total_pulls"] for r in fes_new_stop],
        'fa_old_pulls': [r["total_pulls"] for r in fes_old_stop],
        'fa_new_pyro': sum(r["pyro_spent"] for r in fes_new_stop) / num_senseis,
        'fa_old_pyro': sum(r["pyro_spent"] for r in fes_old_stop) / num_senseis,
        'fb_new_pulls': [r["total_pulls"] for r in fes_new_dump],
        'fb_old_pulls': [r["total_pulls"] for r in fes_old_dump],
        'fb_new_pyro': sum(r["pyro_spent"] for r in fes_new_dump) / num_senseis,
        'fb_old_pyro': sum(r["pyro_spent"] for r in fes_old_dump) / num_senseis,
    }

    generate_graphical_report(data_store)


def main_cli_menu():
    while True:
        clear_screen()
        print("==================================================================")
        print("                  BLUE ARCHIVE GACHA SIMULATOR")
        print("==================================================================")
        print(" [1] Run Mass Simulation (Monte Carlo & PNG Charts)")
        print(" [2] Enter Individual Sensei Mode")
        print(" [0] Exit Program")
        flush_input()
        choice = safe_input("\nEnter menu selection [0-2]: ").strip()

        if choice == "1":
            clear_screen()
            run_comparative_simulation(50000)
            flush_input()
            safe_input("\nPress ENTER to return...")
        elif choice == "2":
            run_individual_mode()
        elif choice == "0":
            break


if __name__ == "__main__":
    main_cli_menu()
