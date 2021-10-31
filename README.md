# prediction
Prediction Market Analysis

I made this project to test a hypothesis that for logically related outcomes, changes in one could be used to give an early, exploitable signal, in another. The example was a US presidential primary election. Since there are state-specific contracts, and contracts for the overall winner, these contracts are related. My guess was that, if hypothetically, the price of the candidate A in Alaska went up (meaning, the probability of the red candidate winning that state's primry election was estimated by market participants to have gone up), then after a slight lag, the price of the red candidate overall contract would increase.

This experiment scraped data from the intrade website.

Conclusion
====
The data confirmed that my hypothesis was right! So why didn't I exploit this finding and become a billionaire? A few problems:

* Volume of trades - the prediction markets have relatively few participants, compared to something like popular stocks on the NYSE. If you want to buy or sell during the lag window, you have to actually have a human ready to buy or sell from you.
* The stated market price is not necessarily the price that somebody will be willing to pay. The lag could be an illusion - people trading in the overall contract may have already taken all related state-specific information into consideration.
