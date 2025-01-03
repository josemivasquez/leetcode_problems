class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def comp(l1, l2):
            i = 0
            j = 0
            while i < len(l1) and j < len(l2):
                if l1[i] == l2[j]:
                    return (i, j)
                elif li[i] < l2[j]:
                    i += 1
                else:
                    j += 1
            
            return None
        
        def merge(l1, l2):
            i = 0
            while i < len(l1) and 0 < len(l2):
                if l1[i] == l2[0]:
                    i += 1
                    l2.pop(0)
                elif l1[i] < l2[0]:
                    i += 1
                else:
                    l1.insert(i, l2[0])
                    l2.pop(0)
                    i += 1
            
            while 0 < len(l2):
                l1.append(l2.pop(0))

            
        
        accounts.sort(key=lambda x: x[0])
        for acc in accounts:
            name = acc.pop(0)
            acc.sort()
            acc.insert(0, name)
        for acc in accounts:
            i = 1
            while i < len(acc) - 1:
                if acc[i] == acc[i+1]:
                    acc.pop(i)
                else:
                    i += 1
        
        res = []
        mails2ids = dict()
        ids2mails = [[]]
        currentname = accounts[0][0]
        for m in accounts[0][1:]:
            # Init structures
            mails2ids[m] = 0
            ids2mails[0].append(m)

        for acc in accounts[1:]:
            name = acc[0]
            mails = acc[1:]
            if name != currentname:
                # New name
                for m in ids2mails:
                    if len(m) > 0:
                        res.append([currentname] + m)
                currentname = name
                ids2mails.clear()
                ids2mails = [[]]
                mails2ids.clear()
                for m in mails:
                    if m in mails2ids:
                        continue
                    mails2ids[m] = 0
                    ids2mails[0].append(m)
                continue
            
            # Same name
            matchingids = set()
            for m in mails:
                if m in mails2ids and m not in matchingids:
                    matchingids.add(mails2ids[m])
            matchingids = list(matchingids)
            matchingids.sort()

            if len(matchingids) == 0:
                # No matching, new id
                ids2mails.append(mails)
                newid = len(ids2mails) - 1
                for m in mails: mails2ids[m] = newid
                continue
            
            # Matching
            principal = matchingids[0]
            for m in mails:
                mails2ids[m] = principal
            merge(ids2mails[principal], mails)

            for id2merge in matchingids[1:]:
                mergemails = ids2mails[id2merge]
                for m in mergemails:
                    mails2ids[m] = principal
                merge(ids2mails[principal], mergemails)
        
        # New name code
        for m in ids2mails:
            if len(m) > 0:
                    res.append([currentname] + m)
        ids2mails.clear()
        ids2mails = [[]]
        mails2ids.clear()
        for m in mails:
            mails2ids[m] = 0
            ids2mails[0].append(m)
            
        return res


                
        
        

            

        

