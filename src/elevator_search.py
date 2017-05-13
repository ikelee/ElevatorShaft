import sys
sys.setrecursionlimit(99999999)

def abs(x):
    return x if x >= 0 else -x

def elevator_search(start_position, contained_events, outstanding_events):

    def src(x, dests, events, time_taken):
        #print x, dests, events, time_taken
        if len(dests) == 0 and len(events) == 0:
            return 0, []
        else:
            best_time = 99999999
            best = None
            for e in dests:
                d = dests[:]
                d.remove(e)
                add_time = 0 if e["end"] == x else 3*abs(x - e["end"])+10
                res, bt = src(e["end"], d, events, time_taken + add_time)
                res += time_taken + add_time - 10
                if res < best_time:
                    best_time = res
                    best = bt
                    best.append(("drop off", e["end"]))
            if len(dests) < 5:
                for e in events:
                    v = events[:]
                    v.remove(e)
                    d = dests[:]
                    d.append(e)
                    add_time = 0 if e["start"] == x else 3*abs(x - e["start"])+10
                    #print "x", time_taken+add_time
                    res, bt = src(e["start"], d, v, time_taken + add_time)
                    #res += time_taken
                    if res < best_time:
                        best_time = res
                        best = bt
                        best.append(("pick up", e["start"]))
            #print "returning", best_time, best
            return best_time, best
    return src(start_position, contained_events, outstanding_events, 0)
