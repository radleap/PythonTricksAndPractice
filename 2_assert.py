
# assertions to find irrecoverable errors in a program, not to signal file not found
# meant to be internal selfchecks, by declaring some conditions are impossible in the code.

# can help avoiding bad problems in coding -- is ugle but useful

# if cond == 'x':
#     do_x()
# elif cond == 'y':
#     do_y
# else:
#     assert False, ("error message custom")

# Caveat 1 - Security concerns: DON'T use asserts for data validation (not discussing testing here, but in programs)
# Caveat 2 - if you pass a tuple as the first argument in an assert statement, it is always true
# the following will never fail
assert(1==2, 'This should fail but doesnt') #but does give a syntax warning