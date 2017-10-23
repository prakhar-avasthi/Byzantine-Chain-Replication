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
3. Open tow terminal in ubuntu
4. run command on Terminal 1: "python3 -m da -F info -f -n ClientNode Main.da"
5. run command on Terminal 2: "python3 -m da -F info -f -n OlympusNode -D Main.da"


## WORKLOAD GENERATION.
**PseudoRandom Workload generation Algorithm:**

1. Generate Random sequence of size n from set {0-n} with random seed.
2. Map each command{put, append, slice, get} to a set of integer {0,1,2,3}.
3. Initilize an empty command list.
3. For each value in Random Sequence:
4. 	command_list.add(command[value%4])


## BUGS AND LIMITATIONS.  
   - **Limitations:**
     - There can only be 1 PseudoRandom client.
     - Two Clients can't have same keys.
     - Buffer size should be 50000 bytes.
   
   - **Bugs:**
   

## CONTRIBUTIONS.
1. Prakhar Avasthi (@github/prakhar-avasthi)
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

2. Rajat Jain (@github/jainraj91)
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


## MAIN FILES.
1. **src\Main.da**
   - Olympus Code
   - Replica Code
   - Creation of ClientNode (Clients will run on this node)
   - Creation of OlympusNode (Olympus and Replicas will run on this node)

2. **src\Client.da**
   - Client Code


## CODE SIZE.
   - **Lines of Code(LOC)** 
    SLOC is used to obtain the LOC.
     - Algorithm:  
     - Other: 
     - Total: 1049 Loc
   
   - **Estimates**
     - Algorithm - 
     - Other functionality interleaved - 


## LANGUAGE FEATURE USAGE. 
- numbers of list comprehensions
- numbers of dictionary comprehensions
- numbers of set comprehensions
- numbers of aggregations - 0
- numbers of quantifications-0


## OTHER COMMENTS
- Command to be run on Client Node
   - **Singlehost**
     - python3 -m da -F info -f --message-buffer-size 50000 -n ClientNode src/Main.da config/test-case.txt
   - **Multihost**
     - python3 -m da -F info -f --message-buffer-size 50000 -n ClientNode src/Main.da config/test-case.txt 172.193.48.52
     
- Command to be run on Olympus Node
  - **SingleHost**
    - python3 -m da -F info -f --message-buffer-size 50000 -n OlympusNode -D src/Main.da config/test-case.txt
  - **MultiHost**
    - python3 -m da -F info -f --message-buffer-size 50000 -n OlympusNode -D src/Main.da config/test-case.txt 172.193.48.52
- If runnning both ClientNode and OlympusNode in same machine, please start ClientNode first and then start OlympusNode.
- If runnning both ClientNode and OlympusNode in different machines, please start OlympusNode first and then start ClientNode.
