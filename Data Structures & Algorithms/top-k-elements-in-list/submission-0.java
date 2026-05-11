class Solution {
    public int[] topKFrequent(int[] nums, int k){
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num: nums){
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(Comparator.comparingInt(countMap::get));
        for (int num: countMap.keySet()){
            if (minHeap.size() < k){
                minHeap.add(num);               
            }
            else if (countMap.get(num) > countMap.get(minHeap.peek())){
                minHeap.poll();
                minHeap.add(num);
            }
        }
        List<Integer> result = new ArrayList<>();
        while (!minHeap.isEmpty()){
            result.add(minHeap.poll());
        }
        //convert list to array
        int[] resArray = new int[result.size()];
        for (int i = 0; i < result.size(); i++){
            resArray[i] = result.get(i);
        }     
        return resArray;
    }
}  