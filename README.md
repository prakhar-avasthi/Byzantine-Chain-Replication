# Byzantine-Chain-Replication

you submission should contain a README with the following sections:

PLATFORM. 
DistAlgo version: 1.0.9
Python version: 3.5.2
OS: Ubuntu
Hosts: Laptop

INSTRUCTIONS.
1. Install Python3
2. Install Distalgo: "sudo pip3 install pyDistAlgo"
3. Open tow terminal in ubuntu
4. run command on Terminal 1: "python3 -m da -F info -f -n ClientNode Main.da"
5. run command on Terminal 2: "python3 -m da -F info -f -n OlympusNode -D Main.da"


WORKLOAD GENERATION.
PseudoRandom Workload generation Algorithm:

1. Generate Random sequence of size n from set {0-n} with random seed.
2. Map each command{put, append, slice, get} to a set of integer {0,1,2,3}.
3. Initilize an empty command list.
3. For each value in Random Sequence:
4. 	command_list.add(command[value%4])


BUGS AND LIMITATIONS.  a list of all known bugs in and limitations of your code.

CONTRIBUTIONS.
1. Prakhar Avasthi
	Responsibilities:
	    a. Implemented Initial Client, Olympus, Replica Processes and their communication.
	    b. Implemented Sending operations from Client to Replica and performing dictionary operation at Replica.
	    c. Implemented Sending of result from Tail Replica to Client.
	    d. Implemented Timeouts modules in Client and Replica.
	    e. Implemented Retransmition of operation on Client timeout.
	    f. Implemented sending cached result, error, forward request by replica on retransmit.
	    g. Implemented PseudoRandom Workload generation Algorithm.

2. Rajat Jain
	Responsibilities:
	    a. Implemented initial required class files.
	    b. Implemented parsing config file.
	    c. Implemented Implemented generating result hash and Signing of order and result statement at Client.
	    d. Implemented forward and result Shuttle creation.
	    e. Implemented shuttle propagation and validation at Replica.
	    f. Implemented Checking of signatures and hashes of Result proof in Client and Replica.
	    g. Implemented Fault injection triggers and failures.


MAIN FILES.
src\Main.da 		(Contains: 1. Olympus code., 2. Creation of ClientNode and OlympusNode
src\Client.da		(Contains: 1. Client code.)
src\Replica.da		(Contains: 1. Replica code.)

CODE SIZE.  (1a) report the numbers of non-blank non-comment lines of code (LOC) in your system in the following categories: algorithm, other, and total.  "algorithm" is for the algorithm itself and other functionality interleaved with it (fault injection, logging, debugging, etc.).  "other" is for everything that can easily be separated from the algorithm, e.g., configuration and testing.  (1b) report how you obtained the counts (I use CLOC https://github.com/AlDanial/cloc).  (2) give a rough estimate of how much of the "algorithm" code is for the algorithm itself, and how much is for other functionality interleaved with it.

LANGUAGE FEATURE USAGE. report the numbers of list comprehensions, dictionary comprehensions, set comprehensions, aggregations, and quantifications in your code.  the first two are Python features; the others are DistAlgo features.

OTHER COMMENTS.  anything else you want us to know.
