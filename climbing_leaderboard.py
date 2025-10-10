def climbingLeaderboard(ranked, player):
    unique_ranks = sorted(set(ranked), reverse=True)
    n = len(unique_ranks)
    results = []
    
    def binarySearch(score):
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if unique_ranks[mid] == score:
                return mid + 1
            elif unique_ranks[mid] > score:
                left = mid + 1
            else:
                right = mid - 1
        return left + 1
    
    for score in player:
        results.append(binarySearch(score))
    return results

if __name__ == '__main__':
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    for rank in result:
        print(rank)
