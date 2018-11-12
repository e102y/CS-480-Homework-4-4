import random as rand

def F(x): # correct assuming a par tof getIn as input
    r1 = x[1]*4 + x[2]*2 + x[3]
    #print(r1)
    r2 = x[4]*4 + x[5]*2 + x[6]
    #print(r2)
    if(r1 > r2):
        return 1
    return 0

class neuron:
    def __init__(self): #correct
        imin = 0
        imax = 1
        rf = rand.randint
        #rf2 = rand.random
        self.Warr = [rf(imin, imax), rf(imin, imax), rf(imin, imax), rf(imin, imax),
                     rf(imin, imax), rf(imin, imax), rf(imin, imax)]
        #self.Warr = [rf2(), rf2(), rf2(), rf2(),
        #             rf2(), rf2(), rf2()]

    def Process(self, x): #correct
        res = []
        for a in range(len(x)):
            res.append(x[a]*self.Warr[a])
        r = sum(res)
        if(r > 0):
            return 1
        return 0

    def Correct(self, n, x, y): #probably wrong???
        for i in range(len(x)):
            self.Warr[i] = self.Warr[i] - n*(y)*x[i]

def getIn(): #correct
    ret = []
    for o1 in range(2):
        for o2 in range(2):
            for o3 in range(2):
                for o4 in range(2):
                    for o5 in range(2):
                        for o6 in range(2):
                            ret.append([-1, o1, o2, o3, o4, o5, o6])
    return ret


def Percept(): #Spaghetti
    eta = 0.1
    a = neuron()
    b = neuron()
    q = neuron()
    inputs = getIn()
    res = (0, [0, 0, 0], -1)
    cont = 0
    for i in range(1, 1001): #epochs
        cont += 1
        ratio = 0.0
        for x in inputs:
            tempa = a.Process(x)
            tempb = b.Process(x)
            tempq = q.Process([-1, tempa, tempb, 0, 0, 0, 0])
            if(tempq == F(x)):
               ratio += 1/64
            else:
                a.Correct(eta, x, 1 if tempa else -1)
                b.Correct(eta, x, 1 if tempb else -1)
                q.Correct(eta, [-1, tempa, tempb, 0, 0, 0, 0], 1 if tempq else -1)
        if(ratio > res[0]):
               res = (ratio, [a.Warr[:], b.Warr[:], [q.Warr[0], q.Warr[1], q.Warr[2]]], cont)
    return res

def PerceptFull(): #Spaghetti
    eta = 0.1
    a = neuron()
    b = neuron()
    q = neuron()
    inputs = getIn()
    res = (0, [0, 0, 0], -1)
    cont = 0
    while(res[0] != 1): #epochs
        cont += 1
        ratio = 0.0
        failed = []
        for x in inputs:
            tempa = a.Process(x)
            tempb = b.Process(x)
            tempq = q.Process([-1, tempa, tempb, 0, 0, 0, 0])
            if(tempq == F(x)):
               ratio += 1/64
            else:
                a.Correct(eta, x, 1 if tempa else -1)
                b.Correct(eta, x, 1 if tempb else -1)
                q.Correct(eta, [-1, tempa, tempb, 0, 0, 0, 0], 1 if tempq else -1)
        if(ratio > res[0]):
               res = (ratio, [a.Warr[:], b.Warr[:], [q.Warr[0], q.Warr[1], q.Warr[2]]], cont)
    return res

'''
def Percept(): #Spaghetti
    eta = 0.1
    a = neuron()
    b = neuron()
    q = neuron()
    inputs = getIn()
    res = (0, [0, 0, 0], -1)
    cont = 0
    for i in range(1, 1001): #epochs
        cont += 1
        ratio = 0.0
        failed = []
        for x in inputs:
            tempa = a.Process(x)
            tempb = b.Process(x)
            tempq = q.Process([-1, tempa, tempb, 0, 0, 0, 0])
            if(tempq == F(x)):
               ratio += 1/64
            else:
               failed.append((x, tempa, tempb, F(x)))
        if(ratio > res[0]):
               res = (ratio, [a.Warr[:], b.Warr[:], [q.Warr[0], q.Warr[1], q.Warr[2]]], cont)
        for y in failed: #training, I'm doing it wrong - how do I not?
               a.Correct(eta, y[0], -y[1])
               b.Correct(eta, y[0], -y[2])
               q.Correct(eta, [-1, y[1], y[2], 0, 0, 0, 0], y[3])
    return res
'''
               
res = Percept()
print(res)
            
            
            
