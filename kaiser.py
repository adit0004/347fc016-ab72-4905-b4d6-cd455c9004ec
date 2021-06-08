class Kaiser:
    def order_cancellation(self, orders, ordersToCancel):
        # NOTE: The comments for the following DP implementation assume the table goes bottom left to top right, not top left to bottom right. Thought I should clarify when I mention directions.

        # Make copies of the original orders in case we need to go over them again with an increased ordersToCancel
        originalOrders = orders

        # Total number of orders
        n = len(orders)

        orders = [0] + orders
        values = [0] + [1 for x in range(len(orders) - 1)]

        # DP Table to hold count of elements that make up this subset sum
        itemCounter = [[0 for i in range(ordersToCancel + 1)] for j in range(n + 1)]

        # DP Table to hold truth values about whether the number at table[i][j] can be made with items in orders
        dpTable = [[False for i in range(ordersToCancel + 1)] for j in range(n + 1)]

        # Build up the table from bottom to top
        for i in range(1, n + 1):
            for orderCount in range(1, ordersToCancel + 1):
                
                # Initialize default values:
                itemCounter[i][orderCount] = itemCounter[i - 1][orderCount]
                dpTable[i][orderCount] = False

                # Check if we need to overwrite default values
                if orderCount >= orders[i]:
                    # Temp holds the current number of items in the knapsack, and we will use it to check if the current solution has fewer elements than the previous solution
                    temp = itemCounter[i - 1][orderCount - orders[i]]
                    if (orderCount == orders[i] or temp) and (
                        itemCounter[i][orderCount] == 0
                        or temp + values[i] < itemCounter[i][orderCount]
                    ):
                        dpTable[i][orderCount] = True
                        itemCounter[i][orderCount] = temp + values[i]
        
        # Build the final list of orders that need to be cancelled
        i = len(dpTable) - 1
        j = len(dpTable[0]) - 1
        finalList = []
        while i > 0 and j > 0:
            if dpTable[i][j]:
                finalList.append(orders[i])
                j -= orders[i]
            i -= 1

        # If a solution was not found, look for an over-cancel
        if(len(finalList) == 0):
            finalList = self.order_cancellation(originalOrders, ordersToCancel+1)

        finalList.sort(reverse=True)
        return finalList

# Driver code
if __name__ == "__main__":
    kaiser = Kaiser()
    orders1 = [3,2,3,1,5]
    orders2 = [5,2,7,2]
    orders3 = [1, 5, 5, 97, 20, 83, 29, 12, 8, 2,41, 4, 36, 7, 8, 15, 23, 31, 90,15, 7, 9, 6, 16, 12, 15, 13, 19,20, 15, 15, 9, 9, 9, 9, 19, 100,2, 4, 8, 18, 10, 7, 17, 3, 33, 23]

    cancelOrders1 = 2
    cancelOrders2 = 7
    cancelOrders3 = 3
    cancelOrders4 = 15
    cancelOrders5 = 375

    print(kaiser.order_cancellation(orders1, cancelOrders1))
    print(kaiser.order_cancellation(orders1, cancelOrders2))
    print(kaiser.order_cancellation(orders2, cancelOrders3))
    print(kaiser.order_cancellation(orders3, cancelOrders4))
    print(kaiser.order_cancellation(orders3, cancelOrders5))