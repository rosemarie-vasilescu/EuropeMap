import time

from queue import Queue, PriorityQueue




class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)


europe = {}

class astar:
    def __init__(self,src,dest):
        self.src= src
        self.dest = dest
        self.makedict()
        self.astar(src,dest)

    def makedict(self):
        file = open("D:\Facultate\Anul 3\IA\input.txt", 'r')
        n = int(file.readline())
        #n = len(file.readlines())
        print(n)
        city =[]
        for i in range(n-1):

            line = file.readline().split(',')

            ct1 = line[0]
            city.append(ct1)
            print("ct1",ct1)
            ct2 = line[1]
            print("ct2",ct2)
            dist = int(line[2])
            print("dist",dist)
            europe.setdefault(ct1, []).append(ctNode(ct2, dist))
            europe.setdefault(ct2, []).append(ctNode(ct1, dist))
            print("europe",europe)
            self.scity = set(city)
            print(self.scity)


    def makehuristikdict(self):
        h = {}

        with open("D:\Facultate\Anul 3\IA\heuristic.txt", 'r') as file:
            for line in file:
                line = line.strip().split(",")
                node = line[0].strip()

                sld = int(line[1].strip())
                h[node] = sld


        return h


    def heuristic(self,node, values):
        return values[node]


    def astar(self,start, end):
        path = {}
        distance = {}
        q = PriorityQueue()
        h = self.makehuristikdict()

        q.put(start, 0)
        distance[start] = 0
        path[start] = None
        expandedList = []

        while (q.empty() == False):
            current = q.get()
            expandedList.append(current)

            if (current == end):
                break
            i=0
            for new in europe[current]:

                g_cost = distance[current] + int(new.distance)


                if (new.city not in distance or g_cost < distance[new.city]):
                    #new.city nodurile parintelui

                    distance[new.city] = g_cost
                    f_cost = g_cost + self.heuristic(new.city, h)
                    q.put(new.city, f_cost)
                    path[new.city] = current


        self.printoutput(start, end, path, distance, expandedList)
        with open('astar.txt', 'w') as f:
            f.write(str(self.finalpath))
            f.write("#" + str(len(self.finalpath)))
            f.write("#" + str(self.cost))
            f.write("#" + str(expandedList))
            f.write("#" + str(len(expandedList)))





    def printoutput(self,start, end, path, distance, expandedlist):
        self.finalpath = []
        i = end

        while (path.get(i) != None):
            self.finalpath.append(i)
            i = path[i]
        self.finalpath.append(start)
        self.finalpath.reverse()
        self.vizitat = expandedlist
        self.cost = distance[end]
        print("Lista orase vizitate \t\t: " + str(expandedlist))
        print("Numar orase vizitate \t\t: " + str(len(expandedlist)))

        print("Cale \t\t: " + str(self.finalpath))
        print("Lungime cale finala \t\t: " + str(len(self.finalpath)))
        print("Distanta totala \t\t: " + str(distance[end]))

# tic = time.perf_counter()
# def main():
#     src = "Bucharest"
#     dst = "London"
#
#     astar(src, dst)
# toc = time.perf_counter()
# timp = toc - tic
# print("Timp executie: ",timp)
# if __name__ == "__main__":
#     main()