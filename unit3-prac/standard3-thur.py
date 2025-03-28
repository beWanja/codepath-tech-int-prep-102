
def manage_stage_changes(changes):
    output = []
    cancelled = []
    for change in changes:
        if change[0:8] == 'Schedule':
            output.append(change[8:])
            print(output)
        elif change == 'Cancel':
            cancelled.append(output.pop())
            print(output)
        elif change == 'Reschedule':    
            output.append(cancelled.pop())
            print(output)
    
    return output 



def main():

    print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))


    return None

if __name__ == "__main__":
    main()