def load_constituencies(file_name):
    constituencies = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) == 2:
                    constituencies[parts[0]] = int(parts[1])
    except FileNotFoundError:
        pass 
    return constituencies

def load_parties(file_name):
    parties = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) == 2:
                    parties[parts[0]] = parts[1]
    except FileNotFoundError:
        pass  
    return parties

def load_results(file_name, constituencies, parties):
    results = {}
    try:
        with open(file_name, 'r') as file:
            current_constituency = None
            for line in file:
                line = line.strip()
                if line in constituencies:
                    current_constituency = line
                    results[current_constituency] = []
                else:
                    parts = line.split(';')
                    if len(parts) == 2:
                        party_code = parts[0]
                        votes = int(parts[1])
                        if party_code in parties:
                            results[current_constituency].append((party_code, votes))
    except FileNotFoundError:
        pass  
    return results

def show_constituencies(constituencies):
    if constituencies:
        print(f"{'Constituency':<20}{'Electorals':>10}")
        print(f"{'-' * 30}")
        total_voters = 0
        for constituency, voters in constituencies.items():
            print(f"{constituency:<20}{voters:>10}")
            total_voters += voters
        print(f"{'-' * 30}")
        print(f"{'Total:':<20}{total_voters:>10}")
    else:
        pass  

def show_parties(parties):
    if parties:
        print(f"{'List':<6}{'Party':>26}")  
        print(f"{'-' * 32}")
        for party_code, party_name in parties.items():
            print(f"{party_code:<6}{party_name:>26}")  # List left-aligned, Party right-aligned
    else:
        pass  

def show_results(constituency, results, constituencies, parties):
    if constituency in results:
        total_votes = sum(votes for _, votes in results[constituency])
        turnout = (total_votes / constituencies[constituency]) * 100
        print(f"\n{constituency}")
        print(f"{'List':<10}{'Party':<26}{'Votes':>10}{'Ratio':>10}")  
        print(f"{'-' * 56}")
        for code, votes in results[constituency]:
            party_name = parties.get(code, "Unknown")
            ratio = (votes / total_votes) * 100
            print(f"{code:<10}{party_name:<26}{votes:>10}{ratio:>10.1f}")  
        print(f"{'-' * 56}")
        print(f"{'Total:':<36}{total_votes:>10}{'100.0':>10}")  # Fix alignment of 'Total'
        print(f"Turnout: {turnout:>47.1f}\n")  
    else:
        pass  

def main():
    constituencies = {}
    parties = {}
    results = {}

    while True:
        print("\n1. Show constituencies")
        print("2. Show parties")
        print("3. Show results")
        print("9. Quit")

        action = input("\nSelect an action: ").strip()
        
        if action == '1':
            if not constituencies:
                file_name = input("File name: ")
                constituencies = load_constituencies(file_name)
            show_constituencies(constituencies)

        elif action == '2':
            if not parties:
                file_name = input("File name: ")
                parties = load_parties(file_name)
            show_parties(parties)

        elif action == '3':
            if not constituencies or not parties:
                pass  
            else:
                if not results:
                    file_name = input("File name for results: ")
                    results = load_results(file_name, constituencies, parties)
                if results:
                    constituency = input("Constituency: ").strip()
                    if constituency in constituencies:
                        show_results(constituency, results, constituencies, parties)

        elif action == '9':
            break  # Quit without printing anything

if __name__ == "__main__":
    main()