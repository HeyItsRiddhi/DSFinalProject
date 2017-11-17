Milestone_1_writeup.md

# Understanding Minority Voting in the United States

## Project statement:

The majority of information we have about minority voting is collected through non-representative phone surveys. Reseraches struggle to discern differences

### Central Question

**Can we use an name-based ethnicity classification model on public voting records to (1) draw conclusions about minority voting behavior and (2) build a model that predicts voter turnout?**

### Sub-Questions:

(A) Ethnicity Classification
	(i) What is the ideal classification model for name-ethnicity analysis?
	(ii) How can we tune the model's parameters to give us strong conclusions. 
		(Example: Is it preferrable to have high precision, low recall for each ethnicity? Is it better to "ignore" datapoints that are hard to classify?)
	(iii) How can we evaluate the model?

(B) Voter Analysis by Ethnicity
	(i) How did turnout among minority voters compare in 2016 to earlier years? 
	(ii) What is the probability that a member of a certain ethnic group voted?
	(iii) How do certain ethnic groups vote (to the extent we can tell from party registration data)? Are there differences? 

(C) Predictive Analysis
	(i) What factors are best at predicting an individual voter's turnout?
		(a) Have these changed over time?
		(b) Do these factors vary between ethnicities?
	(ii)

(D) Evaluation of model
	(i) How does classification perform on the test set?
	(ii) How does turnout prediction perform on the test set?
	(iii) How do our results compare to predicted polls?

### Datasets Available

Voter Registration File and Voter History for:
(A) Florida (> 8 million voters, > 250 million data points)
(B) North Carolina

We will focus on **Florida** primarily, as it is a swing state so it's an interesting case. Our findings may have an impact on electoral politics as candidates can leverage a stronger understanding of minorty voting behavior to improve and target their campaigns.

## Preliminary EDA (Pre-Classification)
Are there voter/election characteristics that correlate with turnout?
- Age
- Gender
- Political party affiliation
- Absentee Ballot vs In-person
- Elections Type (primary, general, local, etc)
- Years since received a voter ID (i.e. are people who just got their voter registration more likely to vote?)
- Previous voting behavior

Are there any inconsistencies / considerations in the data that may affect our results?
- How do we treat "uncounted" ballots. Are there enough of these cases to affect our findings?


These EDAs are important analyses to set up, because we can return to these analyses later and run them for each ethnicity to understand how these factors may vary 
