# SDET Take Home Assignment

### For actual solution

Based on only needing to do 2 weighing.

We have 9 bars. If we divide them up into thirds

1. First comparison will be first third and second third
    - If First is MORE than Second, we know the lighter bar is in Second
    - If First is LESS than Second, we know the lighter bar is in First
    - If First is EQUAL than Second, we know the lighter bar is in Third Half
2. Second Comparison, we'll know do something similar: Split up the thirds again
    - Comparison is exactly the same, except this time what goes in to the scales are single bars

3. Print the results from the Alert popup

4. Print the Weighings that we did.

The options for the first weighing are hardcoded in, so we avoid the duplicate issue if user is allowed to put in
any values.

### Observations and Notes

Assumptions made:
1. URL will work
2. User has correct drivers and browser binaries installed and their respective correct PATHs already set

Awot (Awit)'s Notes:
1. Took the POM approach to this to generalize interacting with page
2. Accounted for the reset button confusion since technically there are two, but one of them isn't supposed to be a button (the result one)
3. Hardcoded the URL, and there isn't any testing to make sure it actually opens correctly (try block normally and useful Exception msg)
4. There may be a duplicate alert that pops up, so POM won't protect user from that. If this is used by others,
   I'd normally have the POM check that the pop up appears and let user handle it, since that is a legitimate test case
5. There are no error checks and handling for Scale values
6. Accounted for the wait required after pressing Weigh button, seems like only way to tell is when either the Result changes or Weighings List changes
6. Happy to go over making this production ready and scaling to many parallel browsers and CI/CD systems, though too long to leave in notes like this.
