const climbingstairs = (target_stair, memo={}) => {
    if (target_stair in memo) return memo[target_stair];
    if (target_stair === 0) return 0;
    if (target_stair === 1) return 1;
    if (target_stair === 2) return 2;

    memo[target_stair] = climbingstairs( target_stair-1, memo) + climbingstairs(target_stair-2, memo);
    return memo[target_stair];
}
console.log(climbingstairs(0));
console.log(climbingstairs(1000));
console.log(climbingstairs(3));