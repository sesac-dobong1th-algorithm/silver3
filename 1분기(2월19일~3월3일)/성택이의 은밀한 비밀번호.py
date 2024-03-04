import sys

input = sys.stdin.readline
print(
    "\n".join(
        [
            "yes" if 6 <= len(input().rstrip()) <= 9 else "no"
            for _ in range(int(input()))
        ]
    )
)
