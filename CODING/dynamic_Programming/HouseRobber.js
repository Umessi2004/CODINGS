var f = (index, nums, memo) =>{
    if (index === 0) return nums[index];
    if (index < 0) return 0;
    if (index in memo) return memo[index];


    //this idea is given by striver by picking and not picking an element
    //i-2 is done to go to the non-adjecent index to calculat the value
    //here i-1 is done as no elemenet is choosen at i so we can take just previous element
    
    let pick = nums[index] + f(index - 2, nums, memo); 
    let notpick = 0 + f(index-1, nums, memo);

    memo[index] = Math.max(pick, notpick);
    return memo[index];
};
var rob = (nums) => {
    const index = nums.length -1 ;
    let memo = {}; //using the memoization technique
    return f(index, nums, memo);
    
};
console.log(rob([1,2,4,5,78,9,3,4,56,7,0,2,3,4,5,6,2,5,7,87,5,3,22,3,4,6,7,8,7,5,4,32,4,5,6,78]));
console.log(rob([2,7,9,3,1]));