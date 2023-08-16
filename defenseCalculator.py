base_defense = -1
leaderskill = -1
start_of_turn_passive = -1
multi_passive = -1
super_attack_effect = -1 #This will build up automatically
links_defense = -1
active_skill_effect = -1
support_item_defense = -1

total_defense = -1

start_of_turn_buildup = -1
multi_buildup = -1
support_item_buildup = -1

def input_base_defense():
    global base_defense
    base_defense = int(input("Please input the base defense of the unit: "))
    #print(base_defense)
    skill_orb_defense = int(input("Please input how much additional defense the unit gets from equipped skill orbs: "))
    base_defense += skill_orb_defense
    #print(base_defense)
    print()

def input_leader_skill():
    print(f'1) HP, ATK & DEF +150%\n2) HP, ATK & DEF +170%\n3) HP, ATK & DEF +200%')
    choice = int(input("Please input 1, 2, or 3 depending on how much stats the unit gains from the team's leader: "))
    global leaderskill
    if choice == 1:
        leaderskill = 4
    elif choice == 2:
        leaderskill = 4.4
    elif choice == 3:
        leaderskill = 5
    else:
        print("fail")
    #print(leaderskill)
    print()

def input_start_of_turn_defense ():
    global start_of_turn_passive
    global start_of_turn_buildup
    start_of_turn_raw = float(input("Please enter the static percent boost (+%) from the start of turn passive: "))
    start_of_turn_passive = 1 + (start_of_turn_raw / 100)
    #print(start_of_turn_passive)
    start_of_turn_buildup_raw = int(input(
        "Please enter the percent boost (+%) added to the unit's start of turn passive per instance of buildup: "))
    start_of_turn_buildup = start_of_turn_buildup_raw / 100
    #print(start_of_turn_buildup)
    print()

def input_links_defense ():
    global links_defense
    links_raw = float(input("Please enter the percent boost (+%) from links: "))
    links_defense = 1 + (links_raw / 100)
    #print(links_defense)
    print()
    return

def input_super_attack_effect ():
    global super_attack_effect
    super_attack_raw = float(input("Please enter the percent boost (+%) from the super attack effect: "))
    super_attack_effect = 1 + ( super_attack_raw/ 100)
    #print(super_attack_effect)
    print()
    return

def input_multiplicative_passive ():
    global multi_passive
    global multi_buildup
    multi_raw = float(input("Please enter the static percent boost (+%) from the multiplicative passive: "))
    multi_passive = 1 + (multi_raw / 100)
    #print(multiplicative_passive)
    multi_buildup_raw = int(input(
        "Please enter the percent boost (+%) added to the unit's multiplicative passive per instance of buildup: "))
    multi_buildup = multi_buildup_raw / 100
    #print(multi_buildup)
    print()
    return

def input_active_skill ():
    global active_skill_effect
    active_skill_raw = float(input("Please enter the percent boost (+%) from active skills: "))
    active_skill_effect = 1 + (active_skill_raw / 100)
    #print(active_skill_effect)
    print()
    return

def input_support_items ():
    global support_item_defense
    global support_item_buildup
    support_item_raw = float(input("Please enter the total percent boost (+%) from support items: "))
    support_item_defense = 1 + (support_item_raw / 100)
    #print(support_item_defense)
    print()
    return

def print_total_defense():
    global base_defense
    global leaderskill
    global start_of_turn_passive
    global multi_passive
    global super_attack_effect
    global links_defense
    global active_skill_effect
    global support_item_defense
    global total_defense
    total_defense = base_defense * leaderskill * start_of_turn_passive * multiplicative_passive * super_attack_effect * links_defense * active_skill_effect * support_item_defense
    print(f'Total Defense: {total_defense:.2f}')
    return

def print_multi_defense_after_buildup (total_multis):
    print("multiplicative_defense_after_buildup")
    global base_defense
    global leaderskill
    global start_of_turn_passive
    global multi_passive #drawing from this value
    global super_attack_effect
    global links_defense
    global active_skill_effect
    global support_item_defense
    global multi_buildup #drawing from this value

    multis = 0
    while multis <= total_multis:
        multi_multiplier = multi_passive + multi_buildup * multis
        multis_defense = base_defense * leaderskill * start_of_turn_passive * super_attack_effect * multi_multiplier * links_defense * active_skill_effect * support_item_defense
        print(f'{multis} activations(s): {multis_defense:.2f}')
        multis += 1
    print()
    return

def print_passive_defense_after_buildup (total_passes):
    global base_defense
    global leaderskill
    global start_of_turn_passive # drawing from this value
    global multi_passive
    global super_attack_effect
    global links_defense
    global active_skill_effect
    global support_item_defense
    global passive_buildup  # drawing from this value

    passes = 1
    while passes <= total_passes:
        pass_multiplier = start_of_turn_passive + start_of_turn_buildup * passes
        pass_defense = base_defense * leaderskill * pass_multiplier * super_attack_effect * multi_passive * links_defense * active_skill_effect * support_item_defense
        print(f'{passes} activations(s): {pass_defense:.2f}')
        passes += 1
    print()
    return

def determine_multi_defense_after_buildup ():
    #print(f'{multi_buildup} ; {start_of_turn_buildup}')
    if multi_buildup > 0 and start_of_turn_buildup <= 0:
        total_multis = int(input(
            "Please enter the amount of multiplicative activations (hits received/attacks performed) you would like to see this character at: "))
        print_multi_defense_after_buildup(total_multis)
    elif multi_buildup <= 0 and start_of_turn_buildup > 0:
        total_passes = int(input(
            "Please enter the amount of passive activations (turns passed/orbs collected) you would like to see this character at: "))
        print_passive_defense_after_buildup(total_passes)
    return


def print_def_after_stacks (total_stacks):
    global base_defense
    global leaderskill
    global start_of_turn_passive
    global multiplicative_passive
    global super_attack_effect #drawing from this value
    global links_defense
    global active_skill_effect
    global support_item_defense
    global total_defense

    stacks = 0
    while stacks <= total_stacks:
        stacked_multiplier = (stacks * (super_attack_effect-1))+1
        stacked_defense = base_defense * leaderskill * start_of_turn_passive * multi_passive * stacked_multiplier * links_defense * active_skill_effect * support_item_defense
        print(f'{stacks} stack(s): {stacked_defense:.2f}')
        stacks += 1
    print()

def determine_stack ():
    print(f'1) Stacks\n2) Does not stack')
    stack_check = int(input("Please input 1 or 2 to indicate whether the unit stacks or not: "))
    if stack_check == 1:
        total_stacks = int(input("Please enter the amount of stacks you would like to see this character at: "))
        print_def_after_stacks(total_stacks)
    else:
        print_def_after_stacks(1)


def main():
    input_base_defense()
    input_leader_skill()
    input_start_of_turn_defense()
    input_links_defense()
    input_super_attack_effect()
    input_multiplicative_passive()
    input_active_skill()
    input_support_items()
    determine_multi_defense_after_buildup()
    determine_stack()

main()





