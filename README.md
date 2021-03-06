# Byzantine-Chain-Replication


## PLATFORM. 
1. DistAlgo version: 1.0.9
2. Python version: 3.5.2
3. PyNacl: 1.1.2
4. OS: Ubuntu
5. Hosts: Laptop


## INSTRUCTIONS.
1. Install Python3
2. Install Distalgo: "sudo pip3 install pyDistAlgo"
3. Install PyNacl: "sudo pip3 install pynacl"
3. Open two terminal in ubuntu
4. run command on Terminal 1(Client Node): "python3 -m da -F info -f --message-buffer-size 50000 -n ClientNode src/Main.da config/test-case.txt"
5. run command on Terminal 2 (Olympus Node): "python3 -m da -F info -f --message-buffer-size 50000 -n OlympusNode -D src/Main.da config/test-case.txt"


## WORKLOAD GENERATION.
**PseudoRandom Workload generation Algorithm:**

1. Generate Random sequence of size n from set {0-n} with random seed.
2. Map each command{put, append, slice, get} to a set of integer {0,1,2,3}.
3. Initilize an empty command list.
3. For each value in Random Sequence:
4. 	command_list.add(command[value%4])


## BUGS AND LIMITATIONS.  
   - **Limitations:**
     - There can only be 1 PseudoRandom client otherwise result may not match
     - Two Clients can't have same keys.
     - Buffer size should be 10,00,000 bytes.
   
   - **Bugs:**
      - Title: Getting StackOverflow error in Replica, [Frequencey: Sometimes]

## CONTRIBUTIONS.
1. Prakhar Avasthi (@github/prakhar-avasthi) 50%
   - **Responsibilities:**
     - Implemented Initial Client, Olympus, Replica Processes and their communication.
     - Implemented Sending operations from Client to Replica and performing dictionary operation at Replica.
     - Implemented Sending of result from Tail Replica to Client.
     - Implemented Timeouts modules in Client and Replica.
     - Implemented Retransmition of operation on Client timeout.
     - Implemented sending cached result, error, forward request by replica on retransmit.
     - Implemented PseudoRandom Workload generation Algorithm.
     - Implemented Retransmitted request sequence at Head Node.
     - Implemented dictionary validation after end of test case.
     - Ran the program on multiple hosts.
     - Written README.md
     - Implemented checking of whether configuration has changed at Olympus or not as Needed.
     - Implemented sending reconfiguration request in case of misbehaviour.
     - Implemented sending reconfiguration request in case of Replica timeout when waiting for retransmit.
     - Implemented "Wedge"-"Wedged" request and response sequence at Replica and Olympus.
     - Implemented "Catch-up"-"Caught-up" request and response sequence at Replica and Olympus.
     - Implemented creating longest history and validating caught-up histories at Olympus.
     - Implemented "get-running-state", "running-state" request and response sequence at Replica and Olympus.
     - Implemented setting up of new configuration after reconfiguration.

2. Rajat Jain (@github/jainraj91) 50%
   - **Responsibilities:**
     - Implemented initial required class files.
     - Implemented head, replica and tail related functionalities in Replica node.
     - Implemented parsing config file.
     - Implemented Sending of result from Tail Replica to Client.
     - Implemented Implemented generating result hash and Signing of order and result statement at Client.
     - Implemented forward and result Shuttle creation.
     - Implemented shuttle propagation and validation at Replica.
     - Implemented Checking of signatures and hashes of Result proof in Client and Replica.
     - Implemented Fault injection triggers and failures.
     - Implemented detect provable misbehavior and send reconfiguration request
     - Implemented initiating checkpoint shuttle periodically by head.
     - Implemented handling of checkpoint shuttl: validate completed checkpoint proof.
     - Implemented deleting history on receiving completed checkpoint shuttle.
     - Implemented history validation on the olympus node.
     - Implemented all the fault triggers.
     - Implemented all the fault injections corresponding to every fault trigger and handle all the faults.
     - Wrote testing.txt with expected behaviors corresponding to possible scenarios.


## MAIN FILES.
1. **src\Main.da**
   - Olympus Code
   - Replica Code
   - Creation of ClientNode (Clients will run on this node)
   - Creation of OlympusNode (Olympus and Replicas will run on this node)

2. **src\Client.da**
   - Client Code


## Performance
1. **Raft2.da**
   - Timing: 9.32 seconds
  
2. **BCR (Main.da)**
   - Single Host: 24.96 seconds
   - Multi Host: 26.76 seconds


## CODE SIZE.
   - **Lines of Code(LOC)** 
    Github is used to obtain the LOC.
     - Algorithm: 635 LOC
     - Other: 962 LOC
     - Total: 1597 LOC
   
   - **Estimates**
     - Algorithm - 60% (381 LOC)
     - Other functionality interleaved - 40% (254 LOC) 


## LANGUAGE FEATURE USAGE. 
- numbers of list comprehensions = 17
- numbers of dictionary comprehensions = 15
- numbers of set comprehensions - 10
- numbers of aggregations - 0
- numbers of quantifications-0


## OTHER COMMENTS
- If runnning both ClientNode and OlympusNode in same machine, please start ClientNode first and then start OlympusNode.
- If runnning both ClientNode and OlympusNode in different machines, please start OlympusNode first and then start ClientNode.

- Client Command : python -m da -n ClientNode --cookie COOKIE --hostname <Self_IP> --master src/Main.da <Config file name>    <Olympus Node Ip>
- Olympus Command: python3 -m da -n OlympusNode --cookie COOKIE --hostname <SELF_IP> -D src/Main.da <Config file name> <SELF_IP>
