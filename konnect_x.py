# Simple Python command-line program for a game of connect four
# Can be played solo (vs. AI) or two-player

import try_type as tt

def main():
    print("Welcome to connect four")
    num_players = 0
    while True:
        get_players = input("Choose how many players (1 or 2): ")
        if tt.try_int(get_players):
            get_players = int(get_players)
            if get_players == 1 or get_players == 2:
                num_players = get_players
                break
        print("Invalid entry! Please enter a correct value")

    if num_players == 1:
        print("Playing vs. AI")
    else:
        print("Playing vs. human")
    return

if __name__ == '__main__':
    main()
