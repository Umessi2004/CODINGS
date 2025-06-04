const howsum = (targetsum, numbers, memo={})=>{
    if (targetsum in memo) return memo[targetsum];
    if (targetsum === 0) return [];  //basecase
    if (targetsum < 0) return null;

    for (let n of numbers ){
        const remainder = targetsum-n;
        const rem_result = howsum(remainder, numbers, memo);
        if (rem_result !== null){
            memo[targetsum] = [...rem_result, n];
            return memo[targetsum];
        }
    }
    memo[targetsum] = null;
    return null;
    
};

console.log(howsum(7,[2,4]));
console.log(howsum(100,[2,4]));
console.log(howsum(7,[5,3,7,4]));
