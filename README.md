
# Service for Tracking All FIFA Matches Played Between Multiple Users

## Match Rules
1. No match can end in a draw.
2. For each match, the loser incurs a debt of €0.50 to the winner, regardless of whether the match ends in regular time, extra time, or penalties.
3. Every match must be played with two teams of equal level. The only criterion for comparison is the number of stars of the team (default FIFA rating).
4. Points will be awarded based on the following table:

| Win in 90 min   | Win in 120 min   | Win in Penalties |
|-----------------|------------------|------------------|
| 3 points        | 2 points         | 1 point          |

Goals scored and conceded are based only on regular and extra time, not penalties.

## Commands
The FIFA counter service should allow users the following commands:
- [[Fifa counter#add_match|add_match]]
- [[Fifa counter#remove_match|remove_match]]
- [[Fifa counter#stats|stats]]

### add_match
The user inputs a match into the database; adding the match will trigger an update to the database, not only for match data but also for debts/credits between players and statistics, all in accordance with the [[Fifa counter#Match Rules|match rules]].

The user will be asked to input:
- Date
- Player 1
- Player 2
- Team 1
- Team 2
- Number of stars
- Result

>[!warning]
>Handle the input appropriately, considering the rules for point assignment and goals scored/conceded, which differ for matches that end with or without penalties.

### remove_match
Allows the user to remove a selected match.

### stats
Allows the user to view tournament statistics with the following options:
- `stats`: shows the [[Fifa counter#Leaderboard|leaderboard]] (see dedicated section)
- `stats player1`: shows all statistics for a specific player, including:
  - Total points
  - Total Wins and Losses
  - Goals For, Goals Against, Goal Difference (total)
  - Wins and Losses excluding penalties
  - Wins and Losses in penalties
  - Goals For, Goals Against, Goal Difference in penalties
  - Averages: (average points, average goals, average goals conceded, etc.)
  - Preferred star rating: the star rating where the player has achieved the highest average points
  - Star rating filter: the same statistics, but filtered by a specific star rating chosen by the user
- `stats playerA playerB`: shows statistics for matches played between the two specified players:
  - Total wins of A over B
  - Total wins of B over A
  - Wins of A over B in penalties
  - Wins of B over A in penalties
  - Goals For, Goals Against, Goal Difference of A over B excluding penalties
  - Goals For, Goals Against, Goal Difference of B over A excluding penalties
  - Goals For, Goals Against, Goal Difference of A over B in penalties
  - Goals For, Goals Against, Goal Difference of B over A in penalties
  - The star rating where A has beaten B the most times
  - The star rating where B has beaten A the most times

## Leaderboard

