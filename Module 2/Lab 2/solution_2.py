def legoBlocks(n, m):
    "this function return the number of stable wall combinations "
    MOD = (10**9 +7)

    # The number of combinations to build a single row
    
    row_combinations = [1, 1, 2, 4]
    
    # Build row combinations up to current wall's width
    while len(row_combinations) <= m: 
        row_combinations.append(sum(row_combinations[-4:]) % MOD)
    
    # Step 2: O(W)
    # Compute total combinations 
    # for constructing a wall of height N of varying widths
    total = [pow(c, n, MOD) for c in row_combinations]
    
    # Find the number of unstable wall configurations 

    unstable = [0, 0]
    
   
    for i in range(2, m + 1):
        # f: (left part - previous vertical violation)*right part
        f = lambda j: (total[j] - unstable[j]) * total[i - j]
        result = sum(map(f, range(1, i)))
        unstable.append(result % MOD)
    
    # Print the number of stable wall combinations
    return (total[m] - unstable[m]) % MOD

def main():
    ''' Main Driver code where the function 'legoBlocks is called' '''
    print(legoBlocks(int(input()), int(input())))
    
if __name__ == '__main__':
    main()
                                                                                                                            
