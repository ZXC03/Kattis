import functools

num_items = int(input())
items = input().split()
num_prices = int(input())
prices = input().split()

item_sum = 0
answer = []
@functools.lru_cache(maxsize=None)
def main():
    for price in prices:
        if item_sum == price:
            answer += item_sum
        if item_sum < price:
            item_sum 