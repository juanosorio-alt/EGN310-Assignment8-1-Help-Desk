"""Help desk priority queue implemented with heapq."""

import csv
from pathlib import Path


import heapq


def add_ticket(queue, priority, number, description):
    """Add a ticket; numbers must be unique and increase with arrival order."""
    if priority not in (1, 2, 3):
        raise ValueError(f"Invalid priority {priority!r}: expected 1, 2, or 3")
    heapq.heappush(queue, (priority, number, description))


def next_ticket(queue):
    """Remove the most urgent ticket, or return None if empty."""
    if not queue:
        return None
    return heapq.heappop(queue)


def pending_count(queue):
    """Return the number of waiting tickets."""
    return len(queue)


def load_tickets(path):
    """Read tickets in their original file order."""
    with open(path, newline="", encoding="utf-8-sig") as file:
        for row in csv.DictReader(file):
            yield int(row["priority"]), int(row["number"]), row["description"]


def main():
    queue = []
    for priority, number, description in load_tickets(
        Path(__file__).with_name("tickets.csv")
    ):
        add_ticket(queue, priority, number, description)

    while pending_count(queue):
        priority, number, description = next_ticket(queue)
        print(priority, number, description)


if __name__ == "__main__":
    main()
