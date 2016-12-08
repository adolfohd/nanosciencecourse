import NLEngine

n = NLEngine.numberOfProcesses()
i = NLEngine.myRank()

for j in range(n):
    if i == j:
        print "MPI process %i of %i reporting." % (i+1, n)
    NLEngine.barrier()
