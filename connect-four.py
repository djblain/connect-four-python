# Simple Python command-line program for a game of connect four
# Can be played solo (vs. AI) or two-player

def is_int(val):
    try:
        int(val)
    except:
        return False
    return True

def main():
    print("Welcome to connect four")
    num_players = 0
    while not (num_players == 1 or num_players == 2):
        get_players = input("Choose how many players (1 or 2): ")
        if is_int(get_players):
            num_players = int(get_players)
    return

if __name__ == '__main__':
    main()
