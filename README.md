# Help Desk Ticket Queue

EGN 310 — Data Structures, Module 8, Assignment 8.1.

This project implements a help desk priority queue in two ways: a binary heap using Python's `heapq` module and a plain list sorted after every insertion.

## Requirements

Python 3. No third-party packages are required.

## Files

| File | Purpose |
| --- | --- |
| `ticket_queue.py` | Heap-based priority queue and CSV runner. |
| `sorted_version.py` | Sorted-list implementation and CSV runner. |
| `tickets.csv` | Twelve supplied tickets in arrival order. |
| `output.txt` | Expected output from either program. |
| `COMPARISON.md` | Comparison of the work performed when inserting a ticket. |

## Run

Open a terminal in this repository and run:

```sh
python3 ticket_queue.py
python3 sorted_version.py
```

Each program loads `tickets.csv` from its own folder and prints all tickets in service order. To save and compare the results on macOS or Linux:

```sh
python3 ticket_queue.py > heap_output.txt
python3 sorted_version.py > sorted_output.txt
diff heap_output.txt sorted_output.txt
diff heap_output.txt output.txt
```

No output from either `diff` command means the files match.

## Queue behavior

Tickets use `(priority, number, description)` tuples. Priority 1 is most urgent, followed by 2 and 3. Ticket numbers must be unique and increase with arrival order so ties are served in arrival order.

Both implementations provide:

- `add_ticket(queue, priority, number, description)`: add a ticket; invalid priorities raise `ValueError` with the rejected value.
- `next_ticket(queue)`: remove and return the next ticket, or return `None` when empty.
- `pending_count(queue)`: return the number of waiting tickets.

For the supplied data, the ticket numbers are served in this order:

```text
102, 104, 108, 111, 101, 105, 107, 110, 103, 106, 109, 112
```

The heap restores its ordering along a heap path after insertion. The list implementation calls `sort()` on the entire list after each insertion. See `COMPARISON.md` for details.
