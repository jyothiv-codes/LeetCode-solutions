class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        bank_set=set(bank)
        possible=['A','G','C','T']
        queue=deque()
        queue.append(startGene)
        visited=set()
        visited.add(startGene)
        count=0
        while len(queue)>0:
            size=len(queue)
            for i in range(size):
                gene=queue.popleft()
                if gene==endGene:
                    return count
                for j in range(len(gene)):
                    for option in possible:
                        newGene=gene[0:j]+option+gene[j+1:]
                        if newGene in bank_set and newGene not in visited:
                            visited.add(newGene)
                            queue.append(newGene)
            count+=1
        return -1

        