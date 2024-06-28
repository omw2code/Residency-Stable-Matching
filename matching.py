import sys
from collections import deque, defaultdict

#globals:
#two dictionaries 
resident_preferences = dict()
hospital_preferences = dict()


def print_output(matches):
    for key, val in matches.items():
        print(val, key)


def stable_matching(resident_preferences, hospital_preferences):
    '''
        Invariant: For every Hospital H and resident R, H will be matched with
                   there favorited R that have proposed to them at each round.

        Initialization: Every hospital has no proposals. 

        Maintenence: If Hospital h is not matched with any proposed resident R or
                     H prefers R over their current R', 
                     there will always be (n - 2) total residents and hospitals left to make a match.

        Termination: Every hospital H has been proposed to. 
    '''
    #let M be the empty set of matches
    matching_dict = dict()

    #for hospital in hospitals:
        #set each hospitals' match to free (still needs a match)
    matching_dict = {hos: None for hos in hospital_preferences}
    
    #for each resident in residents:
        #set each residents' match to free (still need a match)
    res_proposals = {res: None for res in resident_preferences}

    #to avoid using .index(), prepocess the ranks of each resident for each hospital
    hospital_pref_ranks = defaultdict(dict)
    for hospital, preference in hospital_preferences.items():
        for rank, resident in enumerate(preference):
            hospital_pref_ranks[hospital][resident] = rank
    
    #while some resident in the list of Residents is not free and has not proposed to every hospital:
    while None in res_proposals.values():
        for resident, hospital in res_proposals.items():
            #let current_hospital = the first residency in the residents' list which they haven't proposed
            if(hospital == None):

                hospital = resident_preferences[resident].popleft()


                #if current_hospital is free:
                if(matching_dict[hospital] == None):
                    #add the pair (resident, current_hospital) to M
                    matching_dict[hospital] = resident
                    res_proposals[resident] = hospital

                #else if current_hospital prefers the new resident to its current resident
                    #remove the current pair(resident', current_hospital)
                    #add (resident, current_hospital)
                else:
                    curr_res = matching_dict[hospital]
                    if hospital_pref_ranks[hospital][curr_res] > hospital_pref_ranks[hospital][resident]:
                        res_proposals[resident] = hospital
                        matching_dict[hospital] = resident
                        res_proposals[curr_res] = None

    return matching_dict

def getMatchLen():
    try:
        with open(sys.argv[1], 'r') as file_input:
            size = int(file_input.readline())
        return size
    except FileNotFoundError:
        sys.exit(1)
    except IOError:
        sys.exit(1)



def parser(resident_preferences, hospital_prefences, size):
    #open the file
    try:
        with open(sys.argv[1], 'r') as file_input:
            file_input.readline()

            for i in range(size):
                line = file_input.readline().strip()
                entry = line.split(" ")
                resident_preferences[entry[0]] = deque(entry[1:])

            for i in range(size):
                line = file_input.readline().strip()
                entry = line.split(" ")
                hospital_prefences[entry[0]] = deque(entry[1:])

    except FileNotFoundError:
        sys.exit(1)
    except IOError:
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        parser(resident_preferences, hospital_preferences, getMatchLen())
    except IOError:
        sys.exit(1)

    print_output(stable_matching(resident_preferences, hospital_preferences))



if __name__ == "__main__":
    main()

