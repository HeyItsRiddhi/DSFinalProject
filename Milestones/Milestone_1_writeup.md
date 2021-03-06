Milestone_1_writeup.md

# Understanding Minority Voting in the United States

## Project Statement / Central Question

**Can we build a classification model on public voting records to (1) predict voter turnout (2) draw conclusions about minority voting behavior and (3) apply this model to voter turnout of minority ethnicities?**

### Sub-Questions:

We will first build a baseline model to predict voter turnout. Then, we will try to improve this model by adding a classificiation model to predict ethnicity, and then again predict voter turnout. 

1) **Ethnicity Classification**
    * What is the ideal classification model for name-ethnicity analysis?
    * How can we tune the model's parameters to give us strong conclusions. 
		(Example: Is it preferrable to have high precision, low recall for each ethnicity? Is it better to "ignore" datapoints that are hard to classify?)
    * How can we evaluate the model?

2) **Voter Analysis by Ethnicity**
    * How did turnout among minority voters compare in 2016 to earlier years? 
    * What is the probability that a member of a certain ethnic group voted?
    * How do certain ethnic groups vote (to the extent we can tell from party registration data)? Are there differences? 

3) **Predictive Analysis**
    * What factors are best at predicting an individual voter's turnout?
      * Have these changed over time?
      * Do these factors vary between ethnicities?

4) **Evaluation of model**
    * How does classification perform on the test set?
    * How does turnout prediction perform on the test set?
    * How do our results compare to predicted polls?

### Datasets Available

Voter Registration File and Voter History for:
* Florida (> 8 million voters, > 250 million data points)

We will focus on **Florida** primarily, as it is a swing state. Voter turnout is particularly pushed for by politicians in swin states like Florida. Florida is also very split ethnically, as southern Florida is diverse (large minority population) while the counties north tend to vary or be predominantly white. Our findings may have an impact on electoral politics as candidates can leverage a stronger understanding of minority voting behavior to improve and target their campaigns.

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

These EDAs are important analyses to set up, because we can return to these analyses later and run them for each ethnicity to understand how these factors may vary.

## The Path
- Create a base model with without ethnicity exploring the data in our dataset i.e age to voter turn out.
- Create a data set of names and ethnicity and a preliminary model 
- Optimize that model such that we get more name to ethnicity matches
- Use model to analyze minority voter turnout

The core focus of this project will be data munching for ethnic data and then applying that to voter turnout!
