#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_min_price_so_far = prices[0]
  max_profit_so_far = prices[1] - prices[0]
  for i in range(len(prices)):
    


  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


  """
  Function needs to:
  - receives a list/array as input  
  - return maximum profit
   - single buy
   - single sell
  
  """
  ''' Steps Of Problem Solving
  - difference between smallest and largest prices in the list
  - subtract some price by another price that comes before it 
  - think of which algorithm resembles this action 
    - Thinking a bubble sort to sort in pairs but we can      start the sort from the left to right 

  * for loop to go through the lists of prices
  * starting point in the array should be the end 
  * implement the bubble sort 
    - 
  

  '''