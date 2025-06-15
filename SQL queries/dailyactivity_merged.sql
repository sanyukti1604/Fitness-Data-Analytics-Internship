use fitness_data;
show tables;
select * from dailyactivity_merged;

------- dailyactivity_merged.csv : removing null values ----------
DELETE FROM dailyactivity_merged
WHERE Id IS NULL 
   OR ActivityDate IS NULL 
   OR TotalSteps IS NULL 
   OR TotalDistance IS NULL
   OR TrackerDistance IS NULL
   OR LoggedActivitiesDistance IS NULL
   OR VeryActiveDistance IS NULL
   OR ModeratelyActiveDistance IS NULL
   OR LightActiveDistance IS NULL
   OR SedentaryActiveDistance IS NULL
   OR VeryActiveMinutes IS NULL
   OR FairlyActiveMinutes IS NULL
   OR LightlyActiveMinutes IS NULL
   OR SedentaryMinutes IS NULL
   OR Calories IS NULL;


