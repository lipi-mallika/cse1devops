list=[("alice",25),("bob",56),("cat",87),("dog",86)]
list_sorted=sorted(list,key=lambda x:x[1],reverse=True)
print(list_sorted)