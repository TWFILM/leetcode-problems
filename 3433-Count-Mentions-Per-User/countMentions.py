# leetcode 3433. Count Mentions Per User
'''
You are given an integer numberOfUsers representing the total number of users and an array events of size n x 3.

Each events[i] can be either of the following two types:

    1. Message Event: ["MESSAGE", "timestampi", "mentions_stringi"]
        - This event indicates that a set of users was mentioned in a message at timestampi.
        - The mentions_stringi string can contain one of the following tokens:
            - id<number>: where <number> is an integer in range [0,numberOfUsers - 1]. There can be multiple ids separated by a single whitespace and may contain duplicates. This can mention even the offline users.
            - ALL: mentions all users.
            - HERE: mentions all online users.
    2. Offline Event: ["OFFLINE", "timestampi", "idi"]
        - This event indicates that the user idi had become offline at timestampi for 60 time units. The user will automatically be online again at time timestampi + 60.

Return an array mentions where mentions[i] represents the number of mentions the user with id i has across all MESSAGE events.

All users are initially online, and if a user goes offline or comes back online, their status change is processed before handling any message event that occurs at the same timestamp.

Note that a user can be mentioned multiple times in a single message event, and each mention should be counted separately.

Constraints:

1 <= numberOfUsers <= 100
1 <= events.length <= 100
events[i].length == 3
events[i][0] will be one of MESSAGE or OFFLINE.
1 <= int(events[i][1]) <= 105
The number of id<number> mentions in any "MESSAGE" event is between 1 and 100.
0 <= <number> <= numberOfUsers - 1
It is guaranteed that the user id referenced in the OFFLINE event is online at the time the event occurs.
'''

# My Solution
# Runtime: 87 ms, Memory: 18.15 MB
def countMentions(numberOfUsers: int, events: list[list[str]]) -> list[int]:
    mentions = [0] * numberOfUsers
    online = [[True, 0]] * numberOfUsers # [isOnline, timestamp]

    events.sort(key=lambda x: x[0] == "MESSAGE")        # sort by type
    events.sort(key=lambda x: int(x[1]))                # sort by timestamp
    for event in events:
        # update online status
        for i in range(numberOfUsers):
            if (not online[i][0]) and online[i][1] + 60 <= int(event[1]):
                online[i] = [True, online[i][1] + 60]

        # update mentions
        if event[0] == "MESSAGE":
            if event[2] == "ALL":
                for i in range(numberOfUsers):
                    mentions[i] += 1
            elif event[2] == "HERE":
                for i in range(numberOfUsers):
                    if online[i][0]:
                        mentions[i] += 1
            else:
                for id in event[2].split():
                    mentions[int(id[2:])] += 1
        elif event[0] == "OFFLINE":
            online[int(event[2])] = [False, int(event[1])]

    return mentions


# Better Solution
# Runtime: 27 ms, Memory: 17.91 MB
def countMentions(numberOfUsers: int, events: list[list[str]]) -> list[int]:
    events.sort(key = lambda x: (int(x[1]), x[0] == "MESSAGE"))
    online_lst = [0] * numberOfUsers
    mentions = [0] * numberOfUsers
    all_num = 0
    for event in events:
        if "MESSAGE" == event[0]:
            if "ALL" == event[2]:
                all_num += 1
            elif "HERE" == event[2]:
                time = int(event[1])
                for i in range(numberOfUsers):
                    if online_lst[i] <= time:
                        mentions[i] += 1
            else:
                for i in event[2].split():
                    mentions[int(i[2:])] += 1
        else:
            online_lst[int(event[2])] = int(event[1]) + 60
    for i in range(numberOfUsers):
        mentions[i] += all_num
    return mentions


# Test Case
numberOfUsers = 2
events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
'''
Explanation:

Initially, all users are online.
At timestamp 10, id1 and id0 are mentioned. mentions = [1,1]
At timestamp 11, id0 goes offline.
At timestamp 71, id0 comes back online and "HERE" is mentioned. mentions = [2,2]
'''
expected = [2,2]
output = countMentions(numberOfUsers, events)
assert output == expected

numberOfUsers = 2
events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]
'''
Explanation:

Initially, all users are online.
At timestamp 10, id1 and id0 are mentioned. mentions = [1,1]
At timestamp 11, id0 goes offline.
At timestamp 12, "ALL" is mentioned. This includes offline users, so both id0 and id1 are mentioned. mentions = [2,2]
'''
expected = [2,2]
output = countMentions(numberOfUsers, events)
assert output == expected

numberOfUsers = 2
events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]
'''
Explanation:

Initially, all users are online.
At timestamp 10, id0 goes offline.
At timestamp 12, "HERE" is mentioned. Because id0 is still offline, they will not be mentioned. mentions = [0,1]
'''
expected = [0,1]
output = countMentions(numberOfUsers, events)
assert output == expected

numberOfUsers = 3
events = [["MESSAGE","2","HERE"],["OFFLINE","2","1"],["OFFLINE","1","0"],["MESSAGE","61","HERE"]]
'''
Explanation:

Initially, all users are online.
At timestamp 1, id0 goes offline.
At timestamp 2, id1 goes offline.
At timestamp 2, "HERE" is mentioned. mentions = [0,0,1]
At timestamp 61, "HERE" is mentioned. mentions = [1,0,2]
'''
expected = [1,0,2]
output = countMentions(numberOfUsers, events)
assert output == expected

numberOfUsers = 1
events = [["MESSAGE","1","ALL"]]
'''
Explanation:

Initially, all users are online.
At timestamp 1, "ALL" is mentioned. All users are mentioned. mentions = [1]
'''
expected = [1]
output = countMentions(numberOfUsers, events)
assert output == expected

numberOfUsers = 2
events = [["MESSAGE","70","HERE"],["OFFLINE","10","0"],["OFFLINE","71","0"]]
'''
Explanation:

Initially, all users are online.
At timestamp 10, id0 goes offline.
At timestamp 70, id0 comes back online and "HERE" is mentioned. mentions = [1,1]
At timestamp 71, id0 goes offline.
'''
expected = [1,1]
output = countMentions(numberOfUsers, events)
assert output == expected

numberOfUsers = 15
events = [["MESSAGE","174","HERE"],["OFFLINE","426","0"],["MESSAGE","98","ALL"],["MESSAGE","383","ALL"],["MESSAGE","178","id13 id1 id6 id0 id8 id6 id0"],["OFFLINE","474","10"],["MESSAGE","190","ALL"],["MESSAGE","190","HERE"],["MESSAGE","366","ALL"],["OFFLINE","113","4"],["MESSAGE","130","HERE"],["OFFLINE","299","10"],["OFFLINE","352","8"],["MESSAGE","167","id12 id13 id2 id10"],["MESSAGE","120","ALL"],["MESSAGE","175","ALL"],["OFFLINE","150","2"],["MESSAGE","124","ALL"],["OFFLINE","70","13"]]

expected = [12,11,9,10,9,10,12,10,11,10,11,10,11,12,10]
output = countMentions(numberOfUsers, events)
assert output == expected

print("All test cases passed")

