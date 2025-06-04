const f = (day, last_task, task, memo) => {
    if (day === 0) {
        let maxi = 0;
        for (let i = 0; i <= 2; i++) {
            if (i !== last_task) {
                maxi = Math.max(maxi, task[0][i]);
            }
        }
        return maxi;
    }
    if (memo[day] && memo[day][last_task] !== undefined) { return memo[day][last_task]; }

    maxi = 0;
    for (let i = 0; i <= 2; i++) {
        if (i !== last_task) {
            let points = task[day][i] + f(day - 1, i, task, memo);
            maxi = Math.max(maxi, points);
        }
    }
    if (!memo[day]) {
        memo[day] = {};
    }
    memo[day][last_task] = maxi;
    return memo[day][last_task];
}


const ninjatraining = (days, task = {}) => {
    let memo = {};
    return f(days - 1, 3, task, memo);
}

console.log(ninjatraining(10, [[1, 2, 3], [8, 4, 2], [6, 1, 3], [4, 5, 6], [6, 7, 1], [8, 4, 2], [6, 1, 3], [4, 5, 6], [6, 7, 1], [4, 4, 4]]));
