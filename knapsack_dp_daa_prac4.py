def knapsack(weights, values, capacity):
    n= len(values)
    dp = [[0] * (capacity+1) for _ in range(n+1)]

    for i in range (1, n+1):
        for w in range (1, capacity+1):
            if weights[i-1]<= w:
                dp[i][w]= max( values[i-1]+dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]

    w=capacity
    included_items=[]
    total_wt=0

    for i in range (n, 0, -1):
        if dp[i][w]!= dp[i-1][w]:
            included_items.append(i)
            total_wt+= weights[i-1]
            w-= weights[i-1]

    included_items.reverse()

    print("maximum val:",dp[n][capacity])
    print("weights used:",total_wt)
    print("included items:", included_items)

n=int(input("enter no of items:"))
values=[]
weights=[]

for i in range (n):
    values.append(int(input("enter values{i+1}:")))
    weights.append(int(input("enter weights{i+1}:")))

capacity= int(input("enter cap:"))

knapsack(weights, values, capacity)

        


    