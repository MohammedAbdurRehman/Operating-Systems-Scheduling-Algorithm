# Operating-Systems-Scheduling-Algorithm

## 1. Introduction

   
This report presents the implementation of three process scheduling algorithms: First-Come-First-Served (FCFS), Shortest Job First (SJF), and Round Robin (RR). Each algorithm was tested with an input file containing process details. The comparative analysis includes the average waiting time, turnaround time, and insights into how each algorithm performs under different conditions.

## 2. Explanation of Each Algorithm

### 2.1 First-Come-First-Served (FCFS)

Description: FCFS is the simplest scheduling algorithm, where the processes are executed in the order they arrive, without any regard for their burst time.

Advantages: Simple to implement and understand.

Disadvantages: High waiting times for processes with larger burst times if they arrive later (convoy effect).

Formulae:

Waiting Time = Completion Time - Arrival Time - Burst Time

Turnaround Time = Completion Time - Arrival Time

### 2.2 Shortest Job First (SJF)

Description: In SJF, the process with the shortest burst time is selected for execution next. The algorithm can be preemptive or non-preemptive. Here, the non-preemptive version is implemented.

Advantages: Minimizes the average waiting time.

Disadvantages: Requires precise knowledge of burst times in advance and can lead to starvation of longer processes.

Formulae:

Waiting Time = Completion Time - Arrival Time - Burst Time

Turnaround Time = Completion Time - Arrival Time

### 2.3 Round Robin (RR)

Description: RR assigns a fixed time quantum to each process and cycles through the processes in a circular queue. Once a process's quantum expires, the next process is selected.

Advantages: Fair treatment of processes; no starvation.

Disadvantages: If the quantum is too small, too much time is spent switching between processes (context switching).

Formulae:

Waiting Time = Completion Time - Arrival Time - Burst Time

Turnaround Time = Completion Time - Arrival Time

## 3. Input and Output Data

### 3.1 Input Data

The input data consists of processes with their respective process ID (PID), arrival time, and burst time.

Example Input File (processes.txt)

PID, Arrival Time, Burst Time

1, 0, 5

2, 1, 3

3, 2, 8

4, 3, 6

### 3.2 Output Data

FCFS Output:


   PID  Arrival Time  Burst Time  Completion Time  Waiting Time  Turnaround Time
   
0    1             0           5                5             0                5

1    2             1           3                8             4                7

2    3             2           8               16             6               14

3    4             3           6               22            13               19


SJF Output:


   PID  Arrival Time  Burst Time  Completion Time  Waiting Time  Turnaround Time
   
0    2             1           3                4             0                3

1    1             0           5                9             4                9

2    4             3           6               15             6               12

3    3             2           8               23            13               21

Round Robin Output (Quantum = 2):


   PID  Arrival Time  Burst Time  Completion Time  Waiting Time  Turnaround Time
   
0    1             0           5                7             2                7

1    2             1           3                8             4                7

2    3             2           8               19             9               17

3    4             3           6               22            13               19

## 4. Comparative Analysis

### 4.1 Average Waiting Time

FCFS: 5.75 units

SJF: 5.75 units

Round Robin (Quantum=2): 7.0 units

### 4.2 Average Turnaround Time

FCFS: 11.25 units

SJF: 11.25 units

Round Robin (Quantum=2): 12.5 units

### 4.3 Graphical Comparison

Average Waiting Time Comparison

Average Turnaround Time Comparison

## 5. Observations

### 5.1 First-Come-First-Served (FCFS)

Performance: This algorithm performs well with a small number of processes with similar burst times but can lead to long waiting times for processes arriving later.

Best Suited For: Non-time-critical systems where fairness is the key priority.

### 5.2 Shortest Job First (SJF)

Performance: SJF minimizes the average waiting time but is vulnerable to starvation for long processes if shorter processes continuously arrive.

Best Suited For: Systems with predictable burst times where minimizing waiting time is crucial, such as batch processing.

### 5.3 Round Robin (RR)

Performance: RR offers a balance of fairness and efficiency. However, its performance is highly sensitive to the time quantum. With a smaller quantum, context switching overhead can reduce performance.

Best Suited For: Time-sharing systems or real-time environments where fairness and responsiveness are important.

### 5.4 General Insights

FCFS and SJF produced similar average waiting times and turnaround times in this test case, but SJF is generally more efficient in systems with varied burst times.
RR was more balanced but exhibited higher waiting and turnaround times due to frequent context switching with the chosen time quantum (2 units). Increasing the quantum can improve performance, though it may resemble FCFS behavior.

## 6. Conclusion

Each scheduling algorithm has its strengths and weaknesses, and the best algorithm depends on the specific system requirements:

FCFS: Simple and fair but can lead to higher waiting times for longer processes.

SJF: Minimizes average waiting time but risks starvation of longer processes.

Round Robin: Ensures fairness but can lead to higher average waiting and turnaround times depending on the quantum size.

In systems where minimizing waiting time is important, SJF performs better. Round Robin is ideal for real-time systems where process fairness is important. FCFS remains a simple and effective choice for systems where processes arrive and execute in a predictable manner.

## 7. Test Cases

Test Case 1 (Used in the report):


PID, Arrival Time, Burst Time

1, 0, 5

2, 1, 3

3, 2, 8

4, 3, 6

Test Case 2:


PID, Arrival Time, Burst Time

1, 0, 2

2, 1, 1

3, 2, 3

4, 4, 2

