const cansum = (targetsum, numbers, memo={})=>{
    if (targetsum in memo){ return memo[targetsum];}
    if (targetsum===0) return true;
    if (targetsum<0) return false;
    for (let n of numbers){
        const remainder=targetsum-n;
        if (cansum(remainder, numbers, memo)=== true){
            memo[targetsum]= true;
            return true;
        }
    }
    memo[targetsum]=false;
    return false;
}
console.log(cansum(7, [5,3,4,7]));
console.log(cansum(7, [2,4]));
console.log(cansum(100, [1,1]));
