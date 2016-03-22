# Airbnb-case
The challenge gives a list of users along with their demographics, web session records, and some summary statistics. We are asked to predict which country a new user's first booking destination will be. All the users in this dataset are from the USA.
There are 12 possible outcomes of the destination country: 'US', 'FR', 'CA', 'GB', 'ES', 'IT', 'PT', 'NL','DE', 'AU', 'NDF' (no destination found, i.e. there is no booking), and 'other'. 
The training and test sets are split by dates. In the test set, you will predict all the new users with first activities after 12/5/15 In the sessions dataset, the data only dates back to 1/1/2014, while the users dataset dates back to 2010. 

File description</br>
•	train_users.csv - the training set of users/br>
•	test_users.csv - the test set of users </br>
  -id: user id  </br> 
  -date_account_created: the date of account creation </br>
  -timestamp_first_active: timestamp of the first activity, note that it can be earlier than date_account_created or date_first_booking because a user can search before signing up</br>
  -date_first_booking: date of first booking</br>
  -gender</br>
  -age</br>
  -signup_method</br>
  -signup_flow: the page a user came to signup up from</br>
  -language: international language preference</br>
  -affiliate_channel: what kind of paid marketing</br>
  -affiliate_provider: where the marketing is e.g. google, craigslist, other</br>
  -first_affiliate_tracked: whats the first marketing the user interacted with before the signing up</br>
  -signup_app</br>
  -first_device_type</br>
  -first_browser</br>
  -country_destination: this is the target variable you are to predict</br>
  
•	sessions.csv - web sessions log for users</br>
  -user_id: to be joined with the column 'id' in users table</br>
  -action</br>
  -action_type </br>
  -action_detail</br>
  -device_type</br>
  -secs_elapsed</br>
  
•	countries.csv - summary statistics of destination countries in this dataset and their locations

•	age_gender_bkts.csv - summary statistics of users' age group, gender, country of destination

<a href = 'data_explore.ipynb'>Data Explore</a>
