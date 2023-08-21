base_defense = -1
leaderskill = -1
start_of_turn_passive = -1
multi_passive = -1
super_attack_effect = -1
links_defense = -1
active_skill_effect = -1
support_item_defense = -1

total_defense = -1  # Used to record unit defense at every step
recent_defense = -1  # Used to store defense from a previous iteration of calculations/a different unit, allowing for comparison


def input_base_defense():
    global base_defense
    global total_defense

    base_defense = int(input(f'[Base Defense]\n'
                             f'Please input the base defense of the unit: '))
    skill_orb_defense = int(input("Please input how much additional defense the unit gets from equipped skill orbs: "))
    base_defense += skill_orb_defense

    total_defense = base_defense
    print(f'>Current defense: {total_defense:.2f}')
    print()


def input_leader_skill():
    global leaderskill
    global total_defense

    choice = int(input(f'[Leader Skill]\n'
                       f'1) HP, ATK & DEF +150%\n'
                       f'2) HP, ATK & DEF +170%\n'
                       f'3) HP, ATK & DEF +200%\n'
                       f'\n'
                       f'Please input 1, 2, or 3 depending on how much stats the unit gains from the team\'s leader: '))
    if choice == 1:
        leaderskill = 4
    elif choice == 2:
        leaderskill = 4.4
    elif choice == 3:
        leaderskill = 5

    total_defense *= leaderskill
    print(f'>Current defense: {total_defense:.2f}')
    print()


def input_start_of_turn_defense():
    global start_of_turn_passive
    global total_defense

    start_of_turn_raw = float(input(f'[Start of Turn]\n'
                                    f'Please enter the static percent boost (+%) from the start of turn passive'
                                    f'(e.g. \"...at the start of turn\\...when attacking Super Class enemies\"): '))
    start_of_turn_passive = 1 + (start_of_turn_raw / 100)

    total_defense *= start_of_turn_passive
    print(f'>Current defense: {total_defense:.2f}')
    print()


def input_links_defense():
    global links_defense
    global total_defense

    links_raw = float(input(f'[Links]\n'
                            f'Please enter the percent boost (+%) from links: '))
    links_defense = 1 + (links_raw / 100)

    total_defense *= links_defense
    print(f'>Current defense: {total_defense:.2f}')
    print()
    return


def input_multiplicative_passive():
    global multi_passive
    global total_defense

    multi_raw = float(input(f"[Multiplicative]\n"
                            f"Please enter the static percent boost (+%) from the multiplicative passive"
                            f"(e.g. \"...when performing a Super Attack\\...after receiving an attack\"): "))
    multi_passive = 1 + (multi_raw / 100)

    total_defense *= multi_passive
    print(f'>Current defense: {total_defense:.2f}')
    print()
    return


def input_super_attack_effect():
    global super_attack_effect
    global total_defense

    super_attack_raw = float(input(f"[Super Attack Effect]\n"
                                   f"Please enter the static percent boost (+%) from the super attack effect "
                                   f"(i.e. \"...for 1 turn\") (SEPARATE FROM STACKS IN PREVIOUS TURNS): "))
    super_attack_effect = 1 + (super_attack_raw / 100)

    total_defense *= super_attack_effect
    print(f'>Current defense: {total_defense:.2f}')
    print()
    return


def input_active_skill():
    global active_skill_effect
    global total_defense

    active_skill_raw = float(input(f"[Active Skill]\n"
                                   f"Please enter the percent boost (+%) from active skills: "))
    active_skill_effect = 1 + (active_skill_raw / 100)

    total_defense *= active_skill_effect
    print(f'>Current defense: {total_defense:.2f}')
    print()
    return


def input_support_items():
    global support_item_defense
    global total_defense

    support_item_raw = float(input(f"[Support Items]\n"
                                   f"Please enter the total percent boost (+%) from support items: "))
    support_item_defense = 1 + (support_item_raw / 100)

    total_defense *= support_item_defense
    print(f'>Current defense: {total_defense:.2f}')
    print()
    return


def print_def_after_stacks():
    global recent_defense

    total_stacks = int(input(
        f"\n"
        f"[Stacking]"
        f"\n"
        f"Please enter the amount of stacks (effects on Super Attack) you would like to see this character at: "))
    stack_buildup = int(input(
        "Please enter the total percent boost (+%) per stack: ")) / 100

    print()
    stacks = 0
    while stacks <= total_stacks:
        pre_super_multiplier = (stacks * stack_buildup) + 1
        post_super_multiplier = (stacks * stack_buildup) + super_attack_effect
        pre_super_stacked_defense = (total_defense / super_attack_effect) * pre_super_multiplier
        post_super_stacked_defense = (total_defense / super_attack_effect) * post_super_multiplier
        print(f'{stacks} stack(s) pre-super: {pre_super_stacked_defense:.2f} '
              f'| post-super: {post_super_stacked_defense:.2f}')
        stacks += 1

    if recent_defense > -1:
        print(f'>Most recently stored defense stat: {recent_defense:.2f}\n')
    history_choice = int(input(
        f"\n"
        f"1) Use last turn pre-super defense\n"
        f"2) Use last turn post-super defense\n"
        f"3) No\n"
        f"\n"
        f"Update most recently stored defense?: "))
    if history_choice == 1:
        recent_defense = pre_super_stacked_defense
    elif history_choice == 2:
        recent_defense = post_super_stacked_defense
    print()
    menu()
    return


def print_multi_defense_after_buildup():
    global recent_defense

    total_multis = int(input(
        f"\n"
        f"[Multiplicative Buildup]"
        f"\n"
        f"Please enter the amount of multiplicative increments (hits received/attacks performed) "
        f"you would like to see this character at: "))
    multi_buildup = int(input(
        f"Please enter the total percent boost (+%) per action performed: ")) / 100

    print()
    multis = 0
    while multis <= total_multis:
        pre_super_multi_multiplier = (multi_buildup * multis) + 1
        post_super_multi_multiplier = (multi_buildup * multis) + multi_passive
        pre_super_multis_defense = ((total_defense / multi_passive) / super_attack_effect) * pre_super_multi_multiplier
        post_super_multis_defense = (total_defense / multi_passive) * post_super_multi_multiplier
        print(f'{multis} increments(s) pre-super: {pre_super_multis_defense:.2f} '
              f'| post-super: {post_super_multis_defense:.2f}')
        multis += 1

    if recent_defense > -1:
        print(f'\n'
              f'>Most recently stored defense stat: {recent_defense:.2f}')
    history_choice = int(input(f"\n"
                               f"1) Use last turn pre-super defense\n"
                               f"2) Use last turn post-super defense\n"
                               f"3) No\n"
                               f"\n"
                               f"Update most recently stored defense?: "))
    if history_choice == 1:
        recent_defense = pre_super_multis_defense
    elif history_choice == 2:
        recent_defense = post_super_multis_defense
    print()
    menu()
    return


def print_passive_defense_after_buildup():
    total_passes = int(input(
        f"\n"
        f"[Passive Buildup]"
        f"\n"
        f"Please enter the amount of passive increments (turns passed/orbs collected) you would like to see this character at: "))
    pass_buildup = int(input(
        "Please enter the total percent boost (+%) per action performed: ")) / 100

    passes = 1
    while passes <= total_passes:
        pass_multiplier = (pass_buildup * passes) + start_of_turn_passive
        pass_defense = (total_defense/start_of_turn_passive) * pass_multiplier
        print(f'{passes} increments(s): {pass_defense:.2f}')
        passes += 1

    print()
    menu()
    return


def print_stack_multi_defense():
    stack_rate = int(input("Please enter the total percent boost (+%) per stack: ")) / 100
    multi_rate = int(input("Please enter the total percent boost (+%) per multiplicative increment: ")) / 100
    stack_bound = int(input(f"Please select the amount of stacks to display: "))
    multi_bound = int(input(f"Please select the amount of increments to display: "))

    stacks = 0
    while stacks <= stack_bound:
        print(f"{stacks} stack(s) ", end="")
        stack_multiplier = (stack_rate * stacks) + super_attack_effect
        multis = 0
        while multis <= multi_bound:
            multi_multiplier = (multis * multi_rate) + multi_passive
            stack_multi_defense = ((
                                               total_defense / super_attack_effect) / multi_passive) * stack_multiplier * multi_multiplier
            print(f"| {multis} increment(s): {stack_multi_defense:.2f} ", end="")
            multis += 1
        print()
        stacks += 1

    print()
    menu()


def print_multi_stack_defense():
    multi_rate = int(input("Please enter the total percent boost (+%) per multiplicative increment: ")) / 100
    stack_rate = int(input("Please enter the total percent boost (+%) per stack: ")) / 100
    multi_bound = int(input(f"Please select the amount of increments to display: "))
    stack_bound = int(input(f"Please select the amount of stacks to display: "))

    multis = 0
    while multis <= multi_bound:
        print(f"{multis} multiplicative increments(s) ", end="")
        multi_multiplier = (multi_rate * multis) + multi_passive
        stacks = 0
        while stacks <= stack_bound:
            stack_multiplier = (stacks * stack_rate) + super_attack_effect
            stack_multi_defense = ((total_defense / super_attack_effect) / multi_passive) * stack_multiplier * multi_multiplier
            print(f"| {stacks} stacks(s): {stack_multi_defense:.2f} ", end="")
            stacks += 1
        print()
        multis += 1

    print()
    menu()


def print_stack_pass_defense():
    stack_rate = int(input("Please enter the total percent boost (+%) per stack: ")) / 100
    pass_rate = int(input("Please enter the total percent boost (+%) per start-of-turn increment: ")) / 100
    stack_bound = int(input(f"Please select the amount of stacks to display: "))
    pass_bound = int(input(f"Please select the amount of increments to display: "))

    stacks = 0
    while stacks <= stack_bound:
        print(f"{stacks} stack(s) ", end="")
        stack_multiplier = (stack_rate * stacks) + super_attack_effect
        passes = 0
        while passes <= pass_bound:
            pass_multiplier = (passes * pass_rate) + start_of_turn_passive
            stack_pass_defense = ((total_defense / super_attack_effect) / start_of_turn_passive) * stack_multiplier * pass_multiplier
            print(f"| {passes} multiplicative increment(s): {stack_pass_defense:.2f} ", end="")
            passes += 1
        print()
        stacks += 1

    print()
    menu()


def print_pass_stack_defense():
    pass_rate = int(input("Please enter the total percent boost (+%) per start-of-turn increment: ")) / 100
    stack_rate = int(input("Please enter the total percent boost (+%) per stack: ")) / 100
    pass_bound = int(input(f"Please select the amount of increments to display: "))
    stack_bound = int(input(f"Please select the amount of stacks to display: "))

    passes = 0
    while passes <= pass_bound:
        print(f"{passes} SoT increments(s) ", end="")
        pass_multiplier = (pass_rate * passes) + start_of_turn_passive
        stacks = 0
        while stacks <= stack_bound:
            stack_multiplier = (stacks * stack_rate) + super_attack_effect
            stack_pass_defense = ((total_defense / super_attack_effect) / start_of_turn_passive) * stack_multiplier * pass_multiplier
            print(f"| {stacks} stacks(s): {stack_pass_defense:.2f} ", end="")
            stacks += 1
        print()
        passes += 1

    print()
    menu()


def print_multi_pass_defense():
    multi_rate = int(input("Please enter the total percent boost (+%) per multiplicative increment: ")) / 100
    pass_rate = int(input("Please enter the total percent boost (+%) per start-of-turn increment: ")) / 100
    multi_bound = int(input(f"Please select the amount of multiplicative increments to display: "))
    pass_bound = int(input(f"Please select the amount of SoT increments to display: "))

    multis = 0
    while multis <= multi_bound:
        print(f"{multis} multiplicative increments(s) ", end="")
        multi_multiplier = (multi_rate * multis) + multi_passive
        passes = 0
        while passes <= pass_bound:
            pass_multiplier = (passes * pass_rate) + start_of_turn_passive
            multi_pass_defense = ((total_defense / multi_passive) / start_of_turn_passive) * multi_multiplier * pass_multiplier
            print(f"| {passes} SoT increment(s): {multi_pass_defense:.2f} ", end="")
            passes += 1
        print()
        multis += 1

    print()
    menu()


def print_pass_multi_defense():
    pass_rate = int(input("Please enter the total percent boost (+%) per start-of-turn increment: ")) / 100
    multi_rate = int(input("Please enter the total percent boost (+%) per multiplicative increment: ")) / 100
    pass_bound = int(input(f"Please select the amount of SoT increments to display: "))
    multi_bound = int(input(f"Please select the amount of multiplicative increments to display: "))

    passes = 0
    while passes <= pass_bound:
        print(f"{passes} SoT increments(s) ", end="")
        pass_multiplier = (pass_rate * passes) + start_of_turn_passive
        multis = 0
        while multis <= multi_bound:
            multi_multiplier = (multis * multi_rate) + multi_passive
            stack_pass_defense = ((total_defense / multi_passive) / start_of_turn_passive) * multi_multiplier * pass_multiplier
            print(f"| {passes} multiplicative increment(s): {stack_pass_defense:.2f} ", end="")
            passes += 1
        print()
        multis += 1

    print()
    menu()


def determine_custom_buildup():
    print(f"\n"
          f"[Custom Buildup]"
          f"\n"
          f"1) Stacking\n"
          f"2) Multiplicative\n"
          f"3) Start-of-turn\n")
    y_choice = int(input("Please select which mechanic will increase vertically: "))
    x_choice = int(input("Please select which mechanic will increase horizontally: "))


    if y_choice == x_choice:
        print("idiota")
        determine_custom_buildup()
    elif y_choice == 1 and x_choice == 2:
        print_stack_multi_defense()
    elif y_choice == 2 and x_choice == 1:
        print_multi_stack_defense()
    elif y_choice == 1 and x_choice == 3:
        print_stack_pass_defense()
    elif y_choice == 3 and x_choice == 1:
        print_pass_stack_defense()
    elif y_choice == 2 and x_choice == 3:
        print_multi_pass_defense()
    elif y_choice == 3 and x_choice == 2:
        print_pass_multi_defense()


def print_damage_taken():
    return


def menu():
    global recent_defense
    if recent_defense > -1:
        print(f'>Most recently stored defense stat: {recent_defense:.2f}\n')
    print(f'[Defense Menu]\n'
          f'1) Stacking\n'
          f'2) Multiplicative buildup\n'
          f'3) Start-of-turn buildup\n'
          f'4) Custom buildup\n'
          f'5) Damage taken\n'
          f'6) Calculate another defense stat\n')
    user_choice = int(input("Please input 1, 2, 3, 4, or 5 to indicate your selection: "))
    if user_choice == 1:  # Stacking
        print_def_after_stacks()
    elif user_choice == 2:  # Multiplicative buildup
        print_multi_defense_after_buildup()
    elif user_choice == 3:  # Start of turn buildup
        print_passive_defense_after_buildup()
    elif user_choice == 4:  # Custom buildup: players set their own increments for start of turn, multi, and stacking
        determine_custom_buildup()
    elif user_choice == 5:  # Outputs damage taken depending on other defensive factors eg guard and DR, def lowering, enemy damage
        print_damage_taken()
    else:  # Calculate something else
        if recent_defense == -1:
            recent_defense = total_defense
        print(f'\n'
              f'>Most recently stored defense stat: {recent_defense:.2f}\n')
        main()


def main():
    input_base_defense()
    input_leader_skill()
    input_start_of_turn_defense()
    input_links_defense()
    input_multiplicative_passive()
    input_active_skill()
    input_super_attack_effect()
    input_support_items()
    menu()


main()
