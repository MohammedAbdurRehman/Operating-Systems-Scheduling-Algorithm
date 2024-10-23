import pandas as pd
import matplotlib.pyplot as plt

# First-Come-First-Served (FCFS) Scheduling Algorithm
# This function simulates FCFS scheduling, where processes are executed in the order they arrive.
def fcfs_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time

    completion_time = 0
    results = []

    # Loop through each process
    for i in range(n):
        pid, arrival, burst = processes[i]
        if completion_time < arrival:
            completion_time = arrival  # Wait for the process to arrive if necessary
        completion_time += burst  # Update completion time
        turnaround_time = completion_time - arrival  # Calculate turnaround time
        waiting_time = turnaround_time - burst  # Calculate waiting time
        results.append([pid, arrival, burst, completion_time, waiting_time, turnaround_time])

    # Store the results in a pandas DataFrame for better visualization
    df = pd.DataFrame(results, columns=["PID", "Arrival Time", "Burst Time", "Completion Time", "Waiting Time", "Turnaround Time"])
    return df

# Shortest Job First (SJF) Scheduling Algorithm (Non-preemptive)
# This function simulates SJF scheduling, which picks the process with the shortest burst time from the ready queue.
def sjf_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time

    completion_time = 0
    ready_queue = []  # Queue to hold processes that have arrived
    results = []
    i = 0

    # Loop until all processes are handled
    while i < n or ready_queue:
        # Add processes that have arrived to the ready queue
        if i < n and processes[i][1] <= completion_time:
            ready_queue.append(processes[i])
            ready_queue.sort(key=lambda x: x[2])  # Sort ready queue by Burst Time (Shortest first)
            i += 1
            continue

        if ready_queue:
            pid, arrival, burst = ready_queue.pop(0)  # Pop the shortest burst time process from queue
            completion_time += burst  # Update completion time
            turnaround_time = completion_time - arrival  # Calculate turnaround time
            waiting_time = turnaround_time - burst  # Calculate waiting time
            results.append([pid, arrival, burst, completion_time, waiting_time, turnaround_time])
        else:
            completion_time += 1  # If no process is ready, increment time

    # Store the results in a pandas DataFrame
    df = pd.DataFrame(results, columns=["PID", "Arrival Time", "Burst Time", "Completion Time", "Waiting Time", "Turnaround Time"])
    return df

# Round Robin (RR) Scheduling Algorithm
# This function simulates RR scheduling, where each process gets a limited time slice (quantum).
def round_robin_scheduling(processes, quantum):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time

    completion_time = 0
    ready_queue = []  # Queue to hold processes that have arrived
    remaining_burst = {pid: burst for pid, arrival, burst in processes}  # Track remaining burst time for each process
    results = []
    i = 0

    # Loop until all processes are handled
    while i < n or ready_queue:
        # Add processes that have arrived to the ready queue
        if i < n and processes[i][1] <= completion_time:
            ready_queue.append(processes[i])
            i += 1

        if ready_queue:
            pid, arrival, burst = ready_queue.pop(0)  # Pop the first process from the ready queue
            if remaining_burst[pid] <= quantum:  # If the remaining burst is less than or equal to quantum
                completion_time += remaining_burst[pid]  # Complete the process
                turnaround_time = completion_time - arrival  # Calculate turnaround time
                waiting_time = turnaround_time - burst  # Calculate waiting time
                results.append([pid, arrival, burst, completion_time, waiting_time, turnaround_time])
                remaining_burst.pop(pid)  # Remove the process from remaining burst time
            else:
                completion_time += quantum  # Process runs for the time quantum
                remaining_burst[pid] -= quantum  # Reduce remaining burst time
                ready_queue.append([pid, arrival, burst])  # Put the process back in the queue
        else:
            completion_time += 1  # If no process is ready, increment time

    # Store the results in a pandas DataFrame
    df = pd.DataFrame(results, columns=["PID", "Arrival Time", "Burst Time", "Completion Time", "Waiting Time", "Turnaround Time"])
    return df

# Function to calculate average waiting and turnaround times for comparison
def calculate_averages(df):
    avg_waiting_time = df["Waiting Time"].mean()  # Calculate average waiting time
    avg_turnaround_time = df["Turnaround Time"].mean()  # Calculate average turnaround time
    return avg_waiting_time, avg_turnaround_time

# Function to plot comparison of average waiting and turnaround times across algorithms
def plot_comparisons(fcfs_avg, sjf_avg, rr_avg):
    algorithms = ['FCFS', 'SJF', 'RR']
    waiting_times = [fcfs_avg[0], sjf_avg[0], rr_avg[0]]
    turnaround_times = [fcfs_avg[1], sjf_avg[1], rr_avg[1]]

    plt.figure(figsize=(10, 5))

    # Average Waiting Time Comparison
    plt.subplot(1, 2, 1)
    plt.bar(algorithms, waiting_times, color=['blue', 'green', 'red'])
    plt.title('Average Waiting Time')
    plt.ylabel('Time')

    # Average Turnaround Time Comparison
    plt.subplot(1, 2, 2)
    plt.bar(algorithms, turnaround_times, color=['blue', 'green', 'red'])
    plt.title('Average Turnaround Time')
    plt.ylabel('Time')

    plt.show()

# Main Program Execution
def main():
    # Reading input from a file
    processes = []
    with open('processes.txt', 'r') as f:
        for line in f:
            processes.append(list(map(int, line.strip().split(','))))  # Read and parse each process

    # Running FCFS scheduling
    print("FCFS Scheduling Results:")
    fcfs_result = fcfs_scheduling(processes)
    print(fcfs_result)

    # Running SJF scheduling
    print("\nSJF Scheduling Results:")
    sjf_result = sjf_scheduling(processes)
    print(sjf_result)

    # Running RR scheduling
    quantum = int(input("\nEnter the time quantum for Round Robin: "))  # Get the time quantum input for RR
    print("\nRound Robin Scheduling Results:")
    rr_result = round_robin_scheduling(processes, quantum)
    print(rr_result)

    # Comparative Analysis
    fcfs_avg = calculate_averages(fcfs_result)
    sjf_avg = calculate_averages(sjf_result)
    rr_avg = calculate_averages(rr_result)

    # Plot the comparisons
    plot_comparisons(fcfs_avg, sjf_avg, rr_avg)

if __name__ == "__main__":
    main()
