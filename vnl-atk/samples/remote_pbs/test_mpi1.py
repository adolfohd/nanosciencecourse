import NLEngine
import socket

n = NLEngine.numberOfProcesses()
i = NLEngine.myRank()
hostname = socket.gethostname()

for j in range(n):
    if i == j:
        if processIsMaster():
            print "Master node: %s" % hostname
        else:
            print "Slave node:  %s" % hostname
    NLEngine.barrier()