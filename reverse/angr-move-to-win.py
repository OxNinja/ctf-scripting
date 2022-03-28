import angr

proj = Project(input("Path to the binary to explore: "))
win_str = input("String to look for: ").encode()

state = proj.factory.entry_state()
simgr = proj.factory.simgr(state)

simgr.run()
print(simgr)

simgr.move(from_stash="deadended",
        to_stash="ok", 
        filter_func=lambda x: win_str in x.posix.dumps(1)
        )

print(simgr)

if simgr.ok:
    for x in simgr.ok:
        print(f"Solution found: {x.posix.dumps(0)}")

else:
    print("No path found")
