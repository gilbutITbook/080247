def run_timing():
    number_of_runs = 0
    total_time = 0
    
    while True:
        timing = input("Enter 10k run time: ").strip()
        
        if not timing:
            break
            
        number_of_runs += 1
        total_time += float(timing)
        
    print(f'Average time per 10k run is {total_time/number_of_runs}')

run_timing()