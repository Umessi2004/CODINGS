// const bestsum = (targetsum, numbers, memo={}) => {
//     if (targetsum in memo) return memo[targetsum];
//     if (targetsum === 0) return []; //basecase
//     if (targetsum < 0) return null;

//     let shortest_combination = null;
//     for (let num of numbers) {
//         const remainder = targetsum - num;
//         const rem_comb= bestsum(remainder, numbers, memo);
//         if (rem_comb !== null ){
//             combination = [...rem_comb, num];
//             if (shortest_combination === null || combination.length < shortest_combination.length){
//                 shortest_combination = combination;
//                 //memo[targetsum] = [...shortest_combination];
//             }
//         }
//     }
//     memo[targetsum] = shortest_combination;
//     return memo[targetsum];
// };
// console.log(bestsum(7, [5,3,4,7]));
// console.log(bestsum(8, [2,4]));
// console.log(bestsum(1000, [1,5,25, 125]));

const bestsum = (targetsum, numbers) => {
    const table = Array(targetsum + 1).fill(null);
    table[0] = [];


    for (let i = 0; i <= targetsum; i++) {
        if (table[i] !== null) {
            for (let num of numbers) {
                const combination = [...table[i], num];
                //if this combination array is shorter than the previous array then change the array
                if (!table[i + num] || combination.length < table[i + num].length) {
                    table[i + num] = combination;
                }
            }
        }
    }
    return table[targetsum];
};

console.log(bestsum(7, [5,3,4,7]));
console.log(bestsum(8, [2,4]));
console.log(bestsum(1000, [1,5,25, 125]));