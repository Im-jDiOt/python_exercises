class Solution1(object):
    def reorderLogFiles(self, logs):
        letter = []
        digit = []

        for log in logs:
            if log.split()[1].isalpha():
                letter.append(log)
            else:
                digit.append(log)
        
        letter.sort(key=lambda x : (x.split()[1:], x.split()[0]))
        return letter+digit

class Solution2:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def customSort(log):
            idx = log.index(' ') + 1
            if log[idx].isalpha():
                return (0, log[idx:], log[:idx]) # letter, content, identifier
            return (1,) # digit, maintain ordering

        return sorted(logs, key=customSort)
