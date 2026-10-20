# Heap versus sorted list

When a new ticket arrives, the heap version calls `heapq.heappush()` to append the ticket and restore the heap property. It compares the new ticket with its parent and moves it upward when necessary. Only one path through the heap may change; the entire queue is not sorted. With n pending tickets, this adjustment takes O(log n) time in the worst case.

The sorted-list version calls `append()` and then `sort()` after every arrival. The expensive step is sorting the whole list again. Python's adaptive sort can exploit the already sorted portion, so this particular pattern can take O(n) work rather than the general O(n log n) sorting bound. It still examines the list instead of adjusting only a heap path.

Both versions compare priority first and ticket number second. Because the supplied ticket numbers increase with arrival order, equal-priority tickets are served in arrival order. Both programs produce identical output for the twelve supplied tickets.
