function searchInsert(nums: number[], target: number): number {
    let lower = 0
    let higher = nums.length
    while (lower < higher) {
        let m = Math.floor(lower + ((higher - lower) / 2))
        let v = nums[m]
        if (target === v) {
            return m
        } else if (target < v) {
            higher = m
        } else {
            lower = m + 1
        }
    }
    return higher
};