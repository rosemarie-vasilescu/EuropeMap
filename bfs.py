import time

from queue import Queue, PriorityQueue






class ctNode:
    def __init__(self, city,distance):
        self.city = str(city)
        self.distance = str(distance)
europe = {}
class bfs:
    def __init__(self,src,dest):
        self.src= src
        self.dest = dest
        self.makedict()
        self.bfs(src,dest)



    def makedict(self):
        file = open("D:\Facultate\Anul 3\IA\input.txt", 'r')
        n = int(file.readline())
        #n = len(file.readlines())
        print(n)
        for i in range(n-1):

            line = file.readline().split(',')

            ct1 = line[0]
            # print("ct1",ct1)
            ct2 = line[1]
            # print("ct2",ct2)
            dist = int(line[2])
            # print("dist",dist)
            europe.setdefault(ct1, []).append(ctNode(ct2, dist))
            europe.setdefault(ct2, []).append(ctNode(ct1, dist))


    def bfs(self,start, end):
        path = {}
        distance = {}
        q = Queue()


        q.put(start)
        distance[start] = 0
        path[start] = None
        expandedList = []
        #new_explist = set(expandedList)

        while (q.empty() == False):
            current = q.get()
            if (current == end):
                break
            expandedList.append(current)



            for new in europe[current]:
                cost = distance[current] + int(new.distance)


                if (new.city not in expandedList ):
                    distance[new.city] = cost
                    q.put(new.city)
                    path[new.city] = current

        self.printoutput(start, end, path, distance, expandedList)
        with open('bfs.txt', 'w') as f:
            f.write(str(self.finalpath))
            f.write("#" + str(len(self.finalpath)))
            f.write("#" + str(self.mylist))
            f.write("#" + str(len(self.mylist)))
            f.write("#" + str(distance[end]))


    def printoutput(self,start, end, path, distance, expandedlist):
        self.finalpath = []
        i = end

        while (path.get(i) != None):
            self.finalpath.append(i)
            i = path[i]
        self.finalpath.append(start)
        self.finalpath.reverse()
        self.mylist = list(dict.fromkeys(expandedlist))
        # print("Lista orase vizitate \t\t: " + str(self.mylist))
        # print("Numar orase vizitate \t\t: " + str(len(self.mylist)))
        #
        # print("Cale \t\t: " + str(self.finalpath))
        # print("Lungime cale finala \t\t: " + str(len(self.finalpath)))
        print("Distanta totala \t\t: " + str(distance[end]))

